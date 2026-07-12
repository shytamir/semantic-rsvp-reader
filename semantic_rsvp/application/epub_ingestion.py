from __future__ import annotations

import io
import posixpath
import zipfile
from pathlib import PurePosixPath
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

from semantic_rsvp.application.document_ingestion import (
    DocumentIngestionError,
    _extract_clean_html,
)
from semantic_rsvp.application.source_document import SourceDocument
from semantic_rsvp.text.normalize import normalize_text


MAX_EPUB_BYTES = 20_000_000
MAX_EPUB_ENTRIES = 1_000
MAX_EPUB_UNCOMPRESSED_BYTES = 50_000_000
MAX_EPUB_ENTRY_BYTES = 5_000_000
MAX_EPUB_COMPRESSION_RATIO = 100
MAX_EPUB_SPINE_ITEMS = 200
MAX_EPUB_TEXT_CHARS = 5_000_000

_CONTAINER = "META-INF/container.xml"
_MIMETYPE = b"application/epub+zip"
_CONTAINER_NS = "urn:oasis:names:tc:opendocument:xmlns:container"
_OPF_NS = "http://www.idpf.org/2007/opf"
_DC_NS = "http://purl.org/dc/elements/1.1/"


def ingest_epub_document(data: bytes, *, source_name: str) -> SourceDocument:
    """Ingest the bounded, unencrypted EPUB 2/3 subset into a SourceDocument."""
    if not isinstance(data, bytes):
        raise TypeError("document data must be bytes.")
    if not isinstance(source_name, str) or not source_name or len(source_name) > 256:
        raise DocumentIngestionError(
            "source_name must be a non-empty string of at most 256 characters."
        )
    if "://" in source_name:
        raise DocumentIngestionError("Remote sources are not supported.")
    if not source_name.lower().endswith(".epub"):
        raise DocumentIngestionError("EPUB source_name must end with .epub.")
    if len(data) > MAX_EPUB_BYTES:
        raise DocumentIngestionError("EPUB exceeds the 20000000-byte limit.")

    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except (OSError, zipfile.BadZipFile) as error:
        raise DocumentIngestionError("EPUB is not a valid ZIP container.") from error

    with archive:
        entries = _validate_archive(archive)
        if "META-INF/encryption.xml" in entries:
            raise DocumentIngestionError("Encrypted or DRM-protected EPUBs are not supported.")
        rootfile = _read_rootfile(archive, entries)
        metadata, spine_paths = _read_package(archive, entries, rootfile)
        parts = []
        for path in spine_paths:
            raw = _read_entry(archive, entries[path])
            try:
                xhtml = raw.decode("utf-8-sig")
            except UnicodeDecodeError as error:
                raise DocumentIngestionError("EPUB XHTML must be UTF-8.") from error
            part = _extract_clean_html(xhtml)
            if part:
                parts.append(part)
        text = normalize_text("\n\n".join(parts))
        if not text:
            raise DocumentIngestionError("EPUB spine contains no readable text.")
        if len(text) > MAX_EPUB_TEXT_CHARS:
            raise DocumentIngestionError("EPUB exceeds the 5000000-character text limit.")

    return SourceDocument.from_text(
        text,
        source_type="epub",
        provenance={
            "adapter": "epub_v1",
            "identifier": metadata["identifier"],
            "language": metadata["language"],
            "media_type": "application/epub+zip",
            "name": source_name,
            "spine_items": str(len(spine_paths)),
            "title": metadata["title"],
        },
    )


def _validate_archive(archive: zipfile.ZipFile) -> dict[str, zipfile.ZipInfo]:
    infos = archive.infolist()
    if not infos or len(infos) > MAX_EPUB_ENTRIES:
        raise DocumentIngestionError("EPUB must contain 1 to 1000 ZIP entries.")
    first = infos[0]
    if first.filename != "mimetype" or first.compress_type != zipfile.ZIP_STORED:
        raise DocumentIngestionError("EPUB mimetype must be the first uncompressed entry.")
    entries: dict[str, zipfile.ZipInfo] = {}
    total = 0
    for info in infos:
        name = info.filename
        if not _safe_path(name) or name in entries:
            raise DocumentIngestionError("EPUB contains an unsafe or duplicate ZIP path.")
        if info.compress_type not in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}:
            raise DocumentIngestionError("EPUB uses an unsupported ZIP compression method.")
        if (info.external_attr >> 16) & 0o170000 == 0o120000:
            raise DocumentIngestionError("EPUB symbolic-link entries are not supported.")
        if info.file_size > MAX_EPUB_ENTRY_BYTES:
            raise DocumentIngestionError("EPUB entry exceeds the 5000000-byte limit.")
        if info.file_size and info.compress_size == 0:
            raise DocumentIngestionError("EPUB entry has an unsafe compression ratio.")
        if info.compress_size and info.file_size / info.compress_size > MAX_EPUB_COMPRESSION_RATIO:
            raise DocumentIngestionError("EPUB entry exceeds the 100:1 compression-ratio limit.")
        total += info.file_size
        if total > MAX_EPUB_UNCOMPRESSED_BYTES:
            raise DocumentIngestionError("EPUB exceeds the 50000000-byte expanded limit.")
        entries[name] = info
    if "mimetype" not in entries or _read_entry(archive, entries["mimetype"]) != _MIMETYPE:
        raise DocumentIngestionError("EPUB mimetype entry is invalid.")
    return entries


def _read_rootfile(archive, entries) -> str:
    if _CONTAINER not in entries:
        raise DocumentIngestionError("EPUB is missing META-INF/container.xml.")
    root = _parse_xml(_read_entry(archive, entries[_CONTAINER]), "container")
    rootfiles = root.findall(f".//{{{_CONTAINER_NS}}}rootfile")
    if len(rootfiles) != 1:
        raise DocumentIngestionError("EPUB must declare exactly one package rootfile.")
    path = rootfiles[0].get("full-path", "")
    if rootfiles[0].get("media-type") != "application/oebps-package+xml" or not _safe_path(path):
        raise DocumentIngestionError("EPUB package rootfile is invalid.")
    if path not in entries:
        raise DocumentIngestionError("EPUB package rootfile is missing.")
    return path


def _read_package(archive, entries, rootfile):
    root = _parse_xml(_read_entry(archive, entries[rootfile]), "package")
    version = root.get("version", "")
    if not (version.startswith("2.") or version.startswith("3.")):
        raise DocumentIngestionError("Only EPUB 2 and EPUB 3 packages are supported.")
    unique_id = root.get("unique-identifier", "")
    identifiers = {item.get("id"): normalize_text(item.text or "") for item in root.findall(f".//{{{_DC_NS}}}identifier")}
    metadata = {
        "identifier": identifiers.get(unique_id, ""),
        "title": _required_text(root, f".//{{{_DC_NS}}}title", "title"),
        "language": _required_text(root, f".//{{{_DC_NS}}}language", "language"),
    }
    if not metadata["identifier"]:
        raise DocumentIngestionError("EPUB requires a unique dc:identifier.")
    for value in metadata.values():
        if len(value) > 256:
            raise DocumentIngestionError("EPUB metadata values must not exceed 256 characters.")
    manifest = {}
    for item in root.findall(f".//{{{_OPF_NS}}}manifest/{{{_OPF_NS}}}item"):
        item_id, href, media_type = item.get("id", ""), item.get("href", ""), item.get("media-type", "")
        if item_id in manifest or not item_id:
            raise DocumentIngestionError("EPUB manifest identifiers must be unique and non-empty.")
        manifest[item_id] = (href, media_type)
    refs = root.findall(f".//{{{_OPF_NS}}}spine/{{{_OPF_NS}}}itemref")
    if not refs or len(refs) > MAX_EPUB_SPINE_ITEMS:
        raise DocumentIngestionError("EPUB spine must contain 1 to 200 items.")
    base = posixpath.dirname(rootfile)
    paths = []
    for ref in refs:
        if ref.get("linear", "yes").lower() == "no":
            continue
        href, media_type = manifest.get(ref.get("idref", ""), ("", ""))
        if media_type != "application/xhtml+xml":
            raise DocumentIngestionError("EPUB spine supports only XHTML content items.")
        path = _resolve_href(base, href)
        if path not in entries:
            raise DocumentIngestionError("EPUB spine references a missing content item.")
        paths.append(path)
    if not paths:
        raise DocumentIngestionError("EPUB spine contains no supported linear XHTML items.")
    return metadata, paths


def _required_text(root, query, label):
    item = root.find(query)
    value = normalize_text(item.text or "") if item is not None else ""
    if not value:
        raise DocumentIngestionError(f"EPUB requires dc:{label} metadata.")
    return value


def _resolve_href(base: str, href: str) -> str:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or parsed.query:
        raise DocumentIngestionError("EPUB manifest href must be a local relative path.")
    path = unquote(parsed.path)
    resolved = posixpath.normpath(posixpath.join(base, path))
    if not path or not _safe_path(resolved):
        raise DocumentIngestionError("EPUB manifest href is unsafe.")
    return resolved


def _safe_path(path: str) -> bool:
    pure = PurePosixPath(path)
    return bool(path) and "\\" not in path and not pure.is_absolute() and ".." not in pure.parts


def _read_entry(archive, info):
    try:
        return archive.read(info)
    except (OSError, RuntimeError, zipfile.BadZipFile) as error:
        raise DocumentIngestionError("EPUB ZIP entry could not be read safely.") from error


def _parse_xml(data: bytes, label: str):
    if b"<!DOCTYPE" in data.upper() or b"<!ENTITY" in data.upper():
        raise DocumentIngestionError(f"EPUB {label} XML declarations are not supported.")
    try:
        return ElementTree.fromstring(data)
    except ElementTree.ParseError as error:
        raise DocumentIngestionError(f"EPUB {label} XML is invalid.") from error
