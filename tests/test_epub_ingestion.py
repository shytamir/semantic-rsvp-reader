import io
import zipfile
from pathlib import Path

import pytest

from semantic_rsvp.application.document_ingestion import DocumentIngestionError
from semantic_rsvp.application.epub_ingestion import ingest_epub_document
from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.chunking.rules import RuleBasedChunker


FIXTURE = Path(__file__).parent / "fixtures" / "epub"


def _epub(*, package=None, chapters=None, extras=None, compression=zipfile.ZIP_DEFLATED):
    package = package or (FIXTURE / "package.opf").read_bytes()
    chapters = chapters or {
        "EPUB/chapter-1.xhtml": (FIXTURE / "chapter-1.xhtml").read_bytes(),
        "EPUB/chapter-2.xhtml": (FIXTURE / "chapter-2.xhtml").read_bytes(),
    }
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        archive.writestr("mimetype", b"application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", (FIXTURE / "container.xml").read_bytes(), compress_type=compression)
        archive.writestr("EPUB/package.opf", package, compress_type=compression)
        for name, data in chapters.items():
            archive.writestr(name, data, compress_type=compression)
        for name, data in (extras or {}).items():
            archive.writestr(name, data, compress_type=compression)
    return stream.getvalue()


def test_project_fixture_extracts_spine_order_metadata_and_headings():
    document = ingest_epub_document(_epub(), source_name="project-fixture.epub")

    assert document.source_type == "epub"
    assert document.text.index("Opening") < document.text.index("Continuation")
    assert [(item.level, item.text) for item in document.structure] == [
        (1, "Opening"),
        (2, "Continuation"),
    ]
    assert dict(document.provenance) == {
        "adapter": "epub_v1",
        "identifier": "urn:semantic-rsvp:fixture",
        "language": "en",
        "media_type": "application/epub+zip",
        "name": "project-fixture.epub",
        "spine_items": "2",
        "title": "Project Fixture",
    }


def test_identity_is_stable_across_container_compression_and_filename():
    first = ingest_epub_document(_epub(), source_name="first.epub")
    second = ingest_epub_document(
        _epub(compression=zipfile.ZIP_STORED), source_name="renamed.epub"
    )
    assert first.document_id == second.document_id


def test_document_is_compatible_with_existing_schedule_and_continuity_identity():
    document = ingest_epub_document(_epub(), source_name="book.epub")
    result = ScheduleService(chunker=RuleBasedChunker()).generate(document.text)

    assert result.schedule
    assert result.schedule[-1].navigation.progress_percent == 100
    assert result.schedule[-1].structure.active_h2 == "Continuation"
    assert len(document.document_id) == 64


@pytest.mark.parametrize(
    ("data", "message"),
    [
        (b"not zip", "valid ZIP"),
        (_epub(extras={"META-INF/encryption.xml": b"<encryption/>"}), "Encrypted or DRM"),
        (_epub(extras={"../escape": b"x"}), "unsafe or duplicate"),
    ],
)
def test_unsafe_containers_fail_explicitly(data, message):
    with pytest.raises(DocumentIngestionError, match=message):
        ingest_epub_document(data, source_name="unsafe.epub")


def test_required_metadata_and_spine_references_fail_explicitly():
    missing_title = (FIXTURE / "package.opf").read_text().replace(
        "<dc:title>Project Fixture</dc:title>", ""
    ).encode()
    with pytest.raises(DocumentIngestionError, match="requires dc:title"):
        ingest_epub_document(_epub(package=missing_title), source_name="book.epub")

    missing_item = (FIXTURE / "package.opf").read_text().replace(
        "chapter-2.xhtml", "missing.xhtml"
    ).encode()
    with pytest.raises(DocumentIngestionError, match="missing content item"):
        ingest_epub_document(_epub(package=missing_item), source_name="book.epub")


def test_only_bounded_utf8_xhtml_subset_is_accepted():
    unsupported = {"EPUB/chapter-1.xhtml": b"<html><body><img/></body></html>", "EPUB/chapter-2.xhtml": b"<html><body><p>ok</p></body></html>"}
    with pytest.raises(DocumentIngestionError, match="Unsupported HTML element"):
        ingest_epub_document(_epub(chapters=unsupported), source_name="book.epub")

    invalid_utf8 = {"EPUB/chapter-1.xhtml": b"\xff", "EPUB/chapter-2.xhtml": b"<html><body><p>ok</p></body></html>"}
    with pytest.raises(DocumentIngestionError, match="XHTML must be UTF-8"):
        ingest_epub_document(_epub(chapters=invalid_utf8), source_name="book.epub")
