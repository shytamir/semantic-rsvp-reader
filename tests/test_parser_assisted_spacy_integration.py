import pytest

from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.chunking.selection import ObservedParserAssistedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter import (
    availability,
    parse_text,
)


pytestmark = pytest.mark.nlp_spike


def require_spacy():
    available, reason = availability()
    if not available:
        pytest.skip(f"Optional NLP spike dependencies unavailable: {reason}")


def test_spacy_adapter_loads_pinned_model_and_aligns_offsets():
    require_spacy()
    parse = parse_text("The careful pilot did not back down.")

    assert parse.parser_library == "spacy"
    assert parse.alignment_status == "ok"
    assert parse.tokens
    assert all(parse.text[token.start:token.end] == token.text for token in parse.tokens)
    assert parse.parser_version == "3.7.5"
    assert parse.model_version == "3.7.1"


def test_spacy_adapter_produces_project_owned_records():
    require_spacy()
    parse = parse_text("The careful pilot visited Paris on July 4, 2026.")

    assert all(token.__class__.__name__ == "LinguisticToken" for token in parse.tokens)
    assert any(span.span_type in {"entity", "noun_phrase"} for span in parse.spans)
    assert parse.relations


def test_parser_assisted_chunker_uses_experimental_path_deterministically():
    require_spacy()
    chunker = ParserAssistedChunker()
    first = chunker.chunk_sentence_with_trace("The careful pilot did not back down.")
    second = chunker.chunk_sentence_with_trace("The careful pilot did not back down.")

    assert not first.optimization.fallback_used
    assert [chunk.text for chunk in first.chunks] == [chunk.text for chunk in second.chunks]
    assert all(trace.text for trace in first.optimization.traces)
    assert all(trace.char_length <= 32 for trace in first.optimization.traces)


def test_integration_wrapper_preserves_frozen_parser_output():
    require_spacy()
    sentence = "The careful pilot did not back down."
    frozen_chunker = ParserAssistedChunker()
    wrapped_chunker = ObservedParserAssistedChunker(parser_chunker=ParserAssistedChunker())

    assert [chunk.text for chunk in wrapped_chunker.chunk_sentence(sentence)] == [
        chunk.text for chunk in frozen_chunker.chunk_sentence(sentence)
    ]
