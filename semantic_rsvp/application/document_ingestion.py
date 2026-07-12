from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

from semantic_rsvp.application.source_document import SourceDocument
from semantic_rsvp.text.normalize import normalize_text


MAX_SOURCE_BYTES = 1_000_000
MAX_SOURCE_LINES = 20_000
MAX_HTML_TAGS = 10_000
MAX_HTML_DEPTH = 32

_SOURCE_TYPES = {
    ".txt": ("plain_text", "text/plain"),
    ".md": ("markdown", "text/markdown"),
    ".markdown": ("markdown", "text/markdown"),
    ".html": ("clean_html", "text/html"),
    ".htm": ("clean_html", "text/html"),
}


class DocumentIngestionError(ValueError):
    pass


def ingest_local_document(data: bytes, *, source_name: str) -> SourceDocument:
    if not isinstance(data, bytes):
        raise TypeError("document data must be bytes.")
    if not isinstance(source_name, str) or not source_name or len(source_name) > 256:
        raise DocumentIngestionError(
            "source_name must be a non-empty string of at most 256 characters."
        )
    if "://" in source_name:
        raise DocumentIngestionError("Remote sources are not supported.")
    source_type = _SOURCE_TYPES.get(Path(source_name).suffix.lower())
    if source_type is None:
        raise DocumentIngestionError(
            "Unsupported document type. Expected .txt, .md, .markdown, .html, or .htm."
        )
    text, encoding = _decode_source(data)
    _validate_text_limits(text)
    document_type, media_type = source_type
    if document_type == "clean_html":
        text = _extract_clean_html(text)
    if not normalize_text(text):
        raise DocumentIngestionError("Document contains no readable text.")
    return SourceDocument.from_text(
        text,
        source_type=document_type,
        provenance={
            "adapter": "local_document_v1",
            "encoding": encoding,
            "media_type": media_type,
            "name": source_name,
        },
    )


def _decode_source(data: bytes) -> tuple[str, str]:
    if len(data) > MAX_SOURCE_BYTES:
        raise DocumentIngestionError("Document exceeds the 1000000-byte limit.")
    encoding = "utf-8-sig" if data.startswith(b"\xef\xbb\xbf") else "utf-8"
    try:
        text = data.decode(encoding)
    except UnicodeDecodeError as error:
        raise DocumentIngestionError(
            "Document must be UTF-8 or UTF-8 with a BOM."
        ) from error
    if "\x00" in text:
        raise DocumentIngestionError("Document contains unsupported NUL characters.")
    return text, encoding


def _validate_text_limits(text: str) -> None:
    if len(text.splitlines()) > MAX_SOURCE_LINES:
        raise DocumentIngestionError("Document exceeds the 20000-line limit.")


class _CleanHTMLExtractor(HTMLParser):
    _BLOCKS = {
        "article",
        "blockquote",
        "body",
        "div",
        "h1",
        "h2",
        "html",
        "li",
        "main",
        "ol",
        "p",
        "section",
        "ul",
    }
    _INLINE = {"a", "b", "em", "i", "span", "strong"}
    _VOID = {"br", "hr"}
    _ALLOWED = _BLOCKS | _INLINE | _VOID | {"head", "title"}
    _REJECTED = {"iframe", "noscript", "script", "style", "svg", "template"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[str] = []
        self.current: list[str] = []
        self.stack: list[str] = []
        self.tag_count = 0
        self.heading_level: int | None = None
        self.in_head = False

    def handle_starttag(self, tag: str, attrs) -> None:
        tag = tag.lower()
        self._count_tag(tag)
        if tag in self._REJECTED or tag not in self._ALLOWED:
            raise DocumentIngestionError(f"Unsupported HTML element: <{tag}>.")
        if any(name.lower().startswith("on") for name, _ in attrs):
            raise DocumentIngestionError("HTML event-handler attributes are not supported.")
        if tag == "head":
            self.in_head = True
        if tag in self._BLOCKS:
            self._flush()
        if tag in {"h1", "h2"}:
            self.heading_level = int(tag[1])
        if tag == "li":
            self.current.append("- ")
        elif tag == "br":
            self.current.append("\n")
        elif tag == "hr":
            self._flush()
        if tag not in self._VOID:
            self.stack.append(tag)
            if len(self.stack) > MAX_HTML_DEPTH:
                raise DocumentIngestionError("HTML exceeds the 32-level nesting limit.")

    def handle_startendtag(self, tag: str, attrs) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if not self.stack or self.stack[-1] != tag:
            raise DocumentIngestionError("HTML contains mismatched elements.")
        self.stack.pop()
        if tag in {"h1", "h2"}:
            self._flush(heading_level=self.heading_level)
            self.heading_level = None
        elif tag in self._BLOCKS:
            self._flush()
        if tag == "head":
            self.in_head = False

    def handle_data(self, data: str) -> None:
        if not self.in_head:
            self.current.append(data)

    def handle_decl(self, decl: str) -> None:
        if decl.lower() != "doctype html":
            raise DocumentIngestionError("Only the HTML5 doctype is supported.")

    def close(self) -> None:
        super().close()
        if self.stack:
            raise DocumentIngestionError("HTML contains unclosed elements.")
        self._flush()

    def _count_tag(self, tag: str) -> None:
        self.tag_count += 1
        if self.tag_count > MAX_HTML_TAGS:
            raise DocumentIngestionError("HTML exceeds the 10000-element limit.")

    def _flush(self, heading_level: int | None = None) -> None:
        text = normalize_text("".join(self.current))
        self.current.clear()
        if not text:
            return
        if heading_level:
            text = f"{'#' * heading_level} {text}"
        self.blocks.append(text)


def _extract_clean_html(text: str) -> str:
    extractor = _CleanHTMLExtractor()
    try:
        extractor.feed(text)
        extractor.close()
    except DocumentIngestionError:
        raise
    except Exception as error:
        raise DocumentIngestionError("HTML could not be parsed safely.") from error
    return normalize_text("\n\n".join(extractor.blocks))
