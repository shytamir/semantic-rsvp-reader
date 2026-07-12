from pathlib import Path

import pytest

from semantic_rsvp.application.document_ingestion import (
    DocumentIngestionError,
    MAX_SOURCE_BYTES,
    ingest_local_document,
)
from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.chunking.rules import RuleBasedChunker
from scripts.inspect_document_ingestion import main as inspect_main


FIXTURES = Path(__file__).parent / "fixtures" / "ingestion"


@pytest.mark.parametrize(
    ("filename", "source_type", "heading_paths"),
    [
        ("representative.txt", "plain_text", []),
        ("representative.md", "markdown", [(1, "Field Notes"), (2, "Details")]),
        ("representative.html", "clean_html", [(1, "Local Article"), (2, "Details")]),
    ],
)
def test_representative_adapters_produce_source_documents(
    filename, source_type, heading_paths
):
    document = ingest_local_document(
        (FIXTURES / filename).read_bytes(),
        source_name=filename,
    )

    assert document.source_type == source_type
    assert [(item.level, item.text) for item in document.structure] == heading_paths
    assert dict(document.provenance) == {
        "adapter": "local_document_v1",
        "encoding": "utf-8",
        "media_type": {
            "plain_text": "text/plain",
            "markdown": "text/markdown",
            "clean_html": "text/html",
        }[source_type],
        "name": filename,
    }
    assert document.document_id


def test_utf8_bom_and_line_endings_have_equivalent_identity():
    plain = ingest_local_document(b"First.\nSecond.\n", source_name="sample.txt")
    bom_crlf = ingest_local_document(
        b"\xef\xbb\xbfFirst.\r\nSecond.\r\n",
        source_name="sample.txt",
    )

    assert plain.document_id == bom_crlf.document_id
    assert dict(bom_crlf.provenance)["encoding"] == "utf-8-sig"


def test_documents_feed_existing_reader_service_without_behavior_changes():
    document = ingest_local_document(
        (FIXTURES / "representative.md").read_bytes(),
        source_name="representative.md",
    )

    result = ScheduleService(chunker=RuleBasedChunker()).generate(document.text)

    assert result.normalized_text.startswith("# Field Notes")
    assert result.schedule
    assert result.schedule[-1].navigation.progress_percent == 100
    assert result.schedule[-1].structure.active_h2 == "Details"


@pytest.mark.parametrize(
    ("data", "source_name", "message"),
    [
        ((FIXTURES / "unsupported.pdf").read_bytes(), "unsupported.pdf", "Unsupported document type"),
        (b"text", "https://example.invalid/sample.txt", "Remote sources are not supported"),
        (b"\xff", "sample.txt", "must be UTF-8"),
        (b"hello\x00world", "sample.txt", "unsupported NUL"),
        ((FIXTURES / "unsafe.html").read_bytes(), "unsafe.html", "Unsupported HTML element"),
        (b"<article><p>open</article>", "sample.html", "mismatched elements"),
    ],
)
def test_bounded_failures_are_explicit(data, source_name, message):
    with pytest.raises(DocumentIngestionError, match=message):
        ingest_local_document(data, source_name=source_name)


def test_size_and_complexity_limits_are_explicit():
    with pytest.raises(DocumentIngestionError, match="1000000-byte limit"):
        ingest_local_document(b"x" * (MAX_SOURCE_BYTES + 1), source_name="large.txt")

    with pytest.raises(DocumentIngestionError, match="20000-line limit"):
        ingest_local_document(b"x\n" * 20_001, source_name="long.txt")

    nested = ("<div>" * 33 + "text" + "</div>" * 33).encode()
    with pytest.raises(DocumentIngestionError, match="32-level nesting limit"):
        ingest_local_document(nested, source_name="deep.html")

    many_elements = ("<p>x</p>" * 10_001).encode()
    with pytest.raises(DocumentIngestionError, match="10000-element limit"):
        ingest_local_document(many_elements, source_name="complex.html")


def test_local_inspection_script_reports_record_and_reader_output(capsys):
    assert inspect_main([str(FIXTURES / "representative.md")]) == 0

    output = capsys.readouterr().out
    assert '"source_type": "markdown"' in output
    assert '"reader_chunks"' in output
    assert '"Details"' in output


def test_local_inspection_script_reports_bounded_failure(capsys):
    assert inspect_main([str(FIXTURES / "unsafe.html")]) == 1

    assert "Unsupported HTML element: <script>." in capsys.readouterr().err
