from types import SimpleNamespace

import pytest

from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.chunking.selection import (
    ObservedParserAssistedChunker,
    create_chunker,
    inspect_chunking_state,
    normalize_chunker_mode,
)
from semantic_rsvp.web import create_app


def test_default_mode_selects_parser_assisted_chunker():
    assert isinstance(create_chunker(), ObservedParserAssistedChunker)


def test_rule_based_mode_selects_rule_based_chunker():
    assert isinstance(create_chunker("rule_based"), RuleBasedChunker)


def test_invalid_mode_fails_clearly():
    with pytest.raises(ValueError, match="Invalid RSVP_CHUNKER_MODE"):
        normalize_chunker_mode("client_choice")


def test_chunking_state_reports_provider_without_forcing_parser(monkeypatch):
    monkeypatch.setattr(
        "semantic_rsvp.chunking.selection.provider_availability",
        lambda: (False, "spacy_unavailable"),
    )

    state = inspect_chunking_state("parser_assisted")

    assert state.configured_mode == "parser_assisted"
    assert state.provider_available is False
    assert state.provider_reason == "spacy_unavailable"
    assert state.fallback == "rule_based"


@pytest.mark.parametrize(
    "reason",
    [
        "parser_unavailable:spacy_unavailable",
        "parser_unavailable:spacy_version_mismatch:3.8.0",
        "parser_unavailable:model_unavailable",
        "model_initialization_failed",
        "parser_exception",
        "alignment_invalid",
        "optimization_failed",
        "postcondition_failed",
    ],
)
def test_observed_parser_fallback_logs_reason_category_without_source_text(
    reason,
    caplog,
):
    source_text = "Private source sentence should never appear in fallback logs."
    fallback_chunk = Chunk("Private source", 2, 14, "normal")

    class FakeParser:
        def chunk_sentence_with_trace(self, sentence):
            assert sentence == source_text
            return SimpleNamespace(
                chunks=(fallback_chunk,),
                optimization=SimpleNamespace(
                    fallback_used=True,
                    fallback_reason=reason,
                ),
            )

    chunker = ObservedParserAssistedChunker(parser_chunker=FakeParser())

    with caplog.at_level("WARNING"):
        chunks = chunker.chunk_sentence(source_text)

    assert chunks == [fallback_chunk]
    assert reason.split(":", 1)[0] in caplog.text
    assert source_text not in caplog.text


def test_clients_cannot_select_backend_through_api_payload():
    app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "rule_based"})
    client = app.test_client()

    response = client.post(
        "/api/chunk",
        json={
            "sentence": "The system learns from the reader.",
            "chunker_mode": "parser_assisted",
        },
    )

    assert response.status_code == 200
    assert [chunk["text"] for chunk in response.get_json()["chunks"]] == [
        "The system",
        "learns from",
        "the reader.",
    ]
