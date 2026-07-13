from pathlib import Path

from scripts.build_portfolio_demo_epub import build_epub
from semantic_rsvp.application.epub_ingestion import ingest_epub_document
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


def test_portfolio_text_is_project_owned_and_structured_for_the_reader():
    text = (ROOT / "samples" / "portfolio-demo.md").read_text(encoding="utf-8")

    assert text.startswith("# A Local-First Reading Session")
    assert text.count("\n## ") == 3
    assert "private evaluation" not in text.lower()
