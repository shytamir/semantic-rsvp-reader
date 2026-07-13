from __future__ import annotations

import hashlib
import html
import io
import posixpath
import zipfile
from dataclasses import dataclass
from html.parser import HTMLParser

from semantic_rsvp.application.document_ingestion import (
    MAX_HTML_DEPTH,
    MAX_HTML_TAGS,
    DocumentIngestionError,
)
from semantic_rsvp.application.epub_ingestion import (
    MAX_EPUB_TEXT_CHARS,
    _CONTAINER_NS,
    _DC_NS,
    _OPF_NS,
    _parse_xml,
    _read_entry,
    _read_package,
    _read_rootfile,
    _validate_archive,
    ingest_epub_document,
)
from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.chunking.rules import RuleBasedChunker


_CONTAINER_XML = b'<?xml version="1.0" encoding="UTF-8"?>\n<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0"><rootfiles><rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>\n'
_DISCARD_SUBTREES = {
    "audio", "canvas", "embed", "form", "iframe", "math", "noscript",
    "object", "script", "style", "svg", "template", "video",
}
_DISCARD_VOID = {"area", "base", "img", "input", "link", "meta", "source", "track"}
_PASSIVE = {
    "abbr", "address", "aside", "cite", "code", "del", "details", "dfn",
    "figure", "figcaption", "font", "footer", "header", "ins", "kbd", "mark",
    "q", "s", "samp", "small", "summary", "sub", "sup", "time", "u", "var",
}
_OUTPUT = {
    "a", "article", "b", "blockquote", "br", "div", "em", "h1", "h2", "hr",
    "i", "li", "main", "ol", "p", "section", "span", "strong", "ul",
}
_VOID = _DISCARD_VOID | {"br", "hr"}
_AMBIGUOUS = {"col", "colgroup", "dd", "dl", "dt", "frame", "frameset", "table", "tbody", "td", "tfoot", "th", "thead", "tr"}


class EpubPreparationError(DocumentIngestionError):
    """A bounded EPUB preparation rejection with no source-text disclosure."""


@dataclass(frozen=True)
class EpubPreparationResult:
    data: bytes
    mode: str
    epub_version: str
    spine_items: int
    discarded_resources: int
    changes: tuple[str, ...]
    output_size: int
    extracted_characters: int
    heading_count: int
    document_id: str

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest()


def prepare_epub(data: bytes, *, source_name: str) -> EpubPreparationResult:
    """Return exact original or deterministic demo-safe EPUB bytes."""
    if not isinstance(data, bytes):
        raise TypeError("document data must be bytes.")
    try:
        inspection = _inspect(data)
        try:
            document = ingest_epub_document(data, source_name=source_name)
        except DocumentIngestionError:
            normalized, changes = _normalize(inspection)
            document = ingest_epub_document(normalized, source_name=source_name)
            return _verified_result(
                normalized,
                "normalized",
                inspection,
                document,
                changes,
                max(0, len(inspection.entries) - len(inspection.spine_paths) - 3),
            )
        return _verified_result(data, "unchanged", inspection, document, (), 0)
    except EpubPreparationError:
        raise
    except DocumentIngestionError as error:
        raise EpubPreparationError(str(error)) from error
    except (OSError, UnicodeError, zipfile.BadZipFile) as error:
        raise EpubPreparationError("EPUB could not be prepared safely.") from error


@dataclass(frozen=True)
class _Inspection:
    archive_data: bytes
    entries: dict[str, zipfile.ZipInfo]
    rootfile: str
    version: str
    metadata: dict[str, str]
    spine_paths: list[str]


def _inspect(data: bytes) -> _Inspection:
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except (OSError, zipfile.BadZipFile) as error:
        raise EpubPreparationError("EPUB is not a valid ZIP container.") from error
    with archive:
        entries = _validate_archive(archive)
        if "META-INF/encryption.xml" in entries:
            raise EpubPreparationError("Encrypted or DRM-protected EPUBs are not supported.")
        rootfile = _read_rootfile(archive, entries)
        metadata, spine_paths = _read_package(archive, entries, rootfile)
        package = _parse_xml(_read_entry(archive, entries[rootfile]), "package")
        version = package.get("version", "")
    return _Inspection(data, entries, rootfile, version, metadata, spine_paths)


def _normalize(inspection: _Inspection) -> tuple[bytes, tuple[str, ...]]:
    changes: set[str] = set()
    chapters: list[bytes] = []
    with zipfile.ZipFile(io.BytesIO(inspection.archive_data)) as archive:
        for path in inspection.spine_paths:
            raw = _read_entry(archive, inspection.entries[path])
            try:
                source = raw.decode("utf-8-sig")
            except UnicodeDecodeError as error:
                raise EpubPreparationError("EPUB XHTML must be UTF-8.") from error
            sanitizer = _XhtmlSanitizer()
            try:
                sanitizer.feed(source)
                sanitizer.close()
            except EpubPreparationError:
                raise
            except Exception as error:
                raise EpubPreparationError("EPUB XHTML could not be normalized safely.") from error
            body = sanitizer.output()
            changes.update(sanitizer.changes)
            title = html.escape(inspection.metadata["title"], quote=False)
            chapters.append(
                f"<!doctype html>\n<html><head><title>{title}</title></head><body>{body}</body></html>\n".encode("utf-8")
            )
    if not changes:
        raise EpubPreparationError("EPUB requires unsupported or ambiguous normalization.")
    package = _package_xml(inspection.metadata, len(chapters))
    entries = [
        ("mimetype", b"application/epub+zip", zipfile.ZIP_STORED),
        ("META-INF/container.xml", _CONTAINER_XML, zipfile.ZIP_DEFLATED),
        ("OEBPS/package.opf", package, zipfile.ZIP_DEFLATED),
    ]
    entries.extend(
        (f"OEBPS/chapter-{index:03d}.xhtml", chapter, zipfile.ZIP_DEFLATED)
        for index, chapter in enumerate(chapters, 1)
    )
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        for name, content, compression in entries:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = compression
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return stream.getvalue(), tuple(sorted(changes))


def _package_xml(metadata: dict[str, str], count: int) -> bytes:
    identifier = html.escape(metadata["identifier"], quote=True)
    title = html.escape(metadata["title"], quote=True)
    language = html.escape(metadata["language"], quote=True)
    manifest = "".join(
        f'<item id="item-{index:03d}" href="chapter-{index:03d}.xhtml" media-type="application/xhtml+xml"/>'
        for index in range(1, count + 1)
    )
    spine = "".join(f'<itemref idref="item-{index:03d}"/>' for index in range(1, count + 1))
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id">'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
        f'<dc:identifier id="book-id">{identifier}</dc:identifier><dc:title>{title}</dc:title><dc:language>{language}</dc:language>'
        f'</metadata><manifest>{manifest}</manifest><spine>{spine}</spine></package>\n'
    ).encode("utf-8")


def _verified_result(data, mode, inspection, document, changes, discarded_resources):
    schedule = ScheduleService(chunker=RuleBasedChunker()).generate(document.text)
    if not schedule.schedule:
        raise EpubPreparationError("Prepared EPUB could not produce a reading schedule.")
    heading_count = sum(1 for item in document.structure if item.level in {1, 2})
    if len(document.text) > MAX_EPUB_TEXT_CHARS:
        raise EpubPreparationError("EPUB exceeds the 5000000-character text limit.")
    return EpubPreparationResult(
        data=data,
        mode=mode,
        epub_version=inspection.version,
        spine_items=len(inspection.spine_paths),
        discarded_resources=discarded_resources,
        changes=tuple(changes),
        output_size=len(data),
        extracted_characters=len(document.text),
        heading_count=heading_count,
        document_id=document.document_id,
    )


class _XhtmlSanitizer(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.stack: list[tuple[str, str | None, bool]] = []
        self.changes: set[str] = set()
        self.discard_depth = 0
        self.tag_count = 0

    def handle_decl(self, decl):
        if decl.lower() != "doctype html":
            self.changes.add("legacy_doctype")

    def handle_pi(self, data):
        if not data.lower().startswith("xml"):
            raise EpubPreparationError("Unsupported EPUB XHTML processing instruction.")
        self.changes.add("xml_declaration")

    def handle_comment(self, data):
        self.changes.add("comments")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag.lower() not in _VOID:
            self.handle_endtag(tag)

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        self.tag_count += 1
        if self.tag_count > MAX_HTML_TAGS:
            raise EpubPreparationError("HTML exceeds the 10000-element limit.")
        if tag in _AMBIGUOUS:
            raise EpubPreparationError("EPUB XHTML contains ambiguous structured content.")
        if self.discard_depth or tag in _DISCARD_SUBTREES or tag == "head":
            if tag not in _VOID:
                self.discard_depth += 1
                self.stack.append((tag, None, True))
            self.changes.add(f"removed_{tag}")
            return
        if tag in _DISCARD_VOID:
            self.changes.add(f"removed_{tag}")
            return
        if tag in {"html", "body"}:
            output = None
        elif tag in {"h3", "h4", "h5", "h6"}:
            output = "p"
            self.changes.add("lower_heading_to_paragraph")
        elif tag in _PASSIVE:
            output = None
            self.changes.add(f"unwrapped_{tag}")
        elif tag in _OUTPUT:
            output = tag
        else:
            raise EpubPreparationError("EPUB XHTML contains unsupported ambiguous markup.")
        if any(name.lower().startswith("on") for name, _ in attrs):
            self.changes.add("removed_event_handlers")
        if attrs:
            self.changes.add("removed_attributes")
        if output:
            self.parts.append(f"<{output}>")
        if tag not in _VOID:
            self.stack.append((tag, output, False))
            if len(self.stack) > MAX_HTML_DEPTH:
                raise EpubPreparationError("HTML exceeds the 32-level nesting limit.")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if not self.stack or self.stack[-1][0] != tag:
            raise EpubPreparationError("EPUB XHTML contains mismatched elements.")
        _, output, discarded = self.stack.pop()
        if discarded:
            self.discard_depth -= 1
        elif output:
            self.parts.append(f"</{output}>")

    def handle_data(self, data):
        if not self.discard_depth:
            self.parts.append(html.escape(data, quote=False))

    def close(self):
        super().close()
        if self.stack:
            raise EpubPreparationError("EPUB XHTML contains unclosed elements.")

    def output(self):
        value = "".join(self.parts).strip()
        if not value:
            raise EpubPreparationError("EPUB spine contains no readable text.")
        return value
