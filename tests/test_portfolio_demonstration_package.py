from pathlib import Path

import pytest

from scripts.build_portfolio_demo_epub import (
    build_epub,
    build_normalization_required_epub,
    build_rejected_epub,
)
from semantic_rsvp.application.epub_ingestion import ingest_epub_document
from semantic_rsvp.application.epub_preparation import EpubPreparationError, prepare_epub
from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.chunking.rules import RuleBasedChunker


ROOT = Path(__file__).resolve().parents[1]


def test_committed_portfolio_epub_is_reproducible_and_reader_compatible():
    path = ROOT / "samples" / "portfolio-demo.epub"
    assert path.read_bytes() == build_epub()

    document = ingest_epub_document(path.read_bytes(), source_name=path.name)
    schedule = ScheduleService(chunker=RuleBasedChunker()).generate(document.text)

    assert document.source_type == "epub"
    assert [(item.level, item.text) for item in document.structure] == [
        (1, "Opening"),
        (2, "Continuation"),
    ]
    assert len(document.document_id) == 64
    assert schedule.schedule[-1].navigation.progress_percent == 100
    assert schedule.schedule[-1].structure.active_h2 == "Continuation"


def test_committed_portfolio_epub_paths_cover_unchanged_normalized_and_rejected():
    unchanged_path = ROOT / "samples" / "portfolio-demo.epub"
    normalized_path = ROOT / "samples" / "portfolio-demo-normalization-required.epub"
    rejected_path = ROOT / "samples" / "portfolio-demo-encrypted-rejected.epub"

    assert unchanged_path.read_bytes() == build_epub()
    assert normalized_path.read_bytes() == build_normalization_required_epub()
    assert rejected_path.read_bytes() == build_rejected_epub()

    unchanged = prepare_epub(unchanged_path.read_bytes(), source_name=unchanged_path.name)
    normalized = prepare_epub(normalized_path.read_bytes(), source_name=normalized_path.name)
    repeated = prepare_epub(normalized_path.read_bytes(), source_name="renamed.epub")

    assert unchanged.mode == "unchanged" and unchanged.data == unchanged_path.read_bytes()
    assert normalized.mode == repeated.mode == "normalized"
    assert normalized.data == repeated.data
    assert normalized.document_id == repeated.document_id
    assert {"legacy_doctype", "removed_link", "removed_meta", "removed_attributes"} <= set(normalized.changes)
    with pytest.raises(EpubPreparationError, match="Encrypted or DRM"):
        prepare_epub(rejected_path.read_bytes(), source_name=rejected_path.name)


def test_portfolio_text_is_project_owned_and_structured_for_the_reader():
    text = (ROOT / "samples" / "portfolio-demo.md").read_text(encoding="utf-8")

    assert text.startswith("# A Local-First Reading Session")
    assert text.count("\n## ") == 3
    assert "private evaluation" not in text.lower()
