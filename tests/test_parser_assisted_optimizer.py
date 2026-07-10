import dataclasses

from semantic_rsvp.experiments.parser_assisted_chunking.alignment import validate_alignment
from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.config import OptimizerConfig
from semantic_rsvp.experiments.parser_assisted_chunking.models import (
    LinguisticRelation,
    LinguisticSpan,
    LinguisticToken,
    ParseResult,
)
from semantic_rsvp.experiments.parser_assisted_chunking.optimizer import optimize_chunks


def token(token_id, text, start, dep="", head_id=None, pos="NOUN"):
    return LinguisticToken(
        token_id=token_id,
        text=text,
        start=start,
        end=start + len(text),
        sentence_index=0,
        pos=pos,
        dep=dep,
        head_id=head_id,
    )


def parse_from_words(text, words, spans=(), relations=()):
    cursor = 0
    tokens = []
    for index, word in enumerate(words):
        start = text.index(word, cursor)
        tokens.append(token(index, word, start))
        cursor = start + len(word)
    return ParseResult(text=text, tokens=tuple(tokens), spans=tuple(spans), relations=tuple(relations))


def test_optimizer_selects_deterministic_global_path():
    parse = parse_from_words("Alpha beta gamma delta.", ["Alpha", "beta", "gamma", "delta", "."])

    first = optimize_chunks(parse)
    second = optimize_chunks(parse)

    assert [chunk.text for chunk in first.chunks] == [chunk.text for chunk in second.chunks]
    assert first.config_hash == second.config_hash
    assert not first.fallback_used


def test_span_penalty_keeps_named_entity_together():
    text = "Nora Vale arrived."
    parse = parse_from_words(
        text,
        ["Nora", "Vale", "arrived", "."],
        spans=[LinguisticSpan(0, 9, "entity", "PERSON", "test")],
    )

    result = optimize_chunks(parse, OptimizerConfig(max_chars=18))

    assert any(chunk.text == "Nora Vale" for chunk in result.chunks)


def test_date_number_span_penalty_keeps_date_together():
    text = "July 4 2026 arrived."
    parse = parse_from_words(
        text,
        ["July", "4", "2026", "arrived", "."],
        spans=[LinguisticSpan(0, 11, "date", "DATE", "test")],
    )

    result = optimize_chunks(parse, OptimizerConfig(max_chars=18))

    assert any(chunk.text == "July 4 2026" for chunk in result.chunks)


def test_relation_penalties_cover_aux_negation_particle_and_noun_phrase():
    text = "They did not back down."
    parse = parse_from_words(
        text,
        ["They", "did", "not", "back", "down", "."],
        spans=[LinguisticSpan(0, 4, "noun_phrase", "", "test")],
        relations=[
            LinguisticRelation(1, 3, "aux_main", "test"),
            LinguisticRelation(2, 3, "negation", "test"),
            LinguisticRelation(4, 3, "verb_particle", "test"),
        ],
    )

    result = optimize_chunks(parse, OptimizerConfig(max_chars=24))

    assert any("did not back down" in chunk.text for chunk in result.chunks)


def test_punctuation_and_clause_rewards_are_explained():
    text = "When rain stopped, people left."
    parse = parse_from_words(
        text,
        ["When", "rain", "stopped", ",", "people", "left", "."],
    )

    result = optimize_chunks(parse, OptimizerConfig(max_chars=20))

    factors = [
        factor.name
        for trace in result.traces
        for factor in trace.positive_factors
    ]
    assert "punctuation_boundary_reward" in factors


def test_width_and_unsplittable_token_policy():
    text = "antidisestablishmentarianism"
    parse = parse_from_words(text, [text])

    result = optimize_chunks(parse, OptimizerConfig(max_chars=10))

    assert result.chunks[0].text == text
    assert "unsplittable_token_exception" in result.traces[0].hard_constraints


def test_alignment_rejection_and_no_valid_path_fallback():
    bad = ParseResult(
        text="abc",
        tokens=(LinguisticToken(0, "xyz", 0, 3, 0),),
    )
    assert validate_alignment(bad)[0] is False
    assert optimize_chunks(bad).fallback_used

    text = "alpha beta gamma"
    parse = parse_from_words(text, ["alpha", "beta", "gamma"])
    result = optimize_chunks(
        parse,
        OptimizerConfig(max_chars=4, allow_unsplittable_token_exception=False),
    )
    assert result.fallback_used
    assert result.fallback_reason == "no_valid_optimization_path"


def test_parser_unavailable_fallback_is_diagnostic(monkeypatch):
    import semantic_rsvp.experiments.parser_assisted_chunking.chunker as chunker_module

    monkeypatch.setattr(chunker_module, "availability", lambda: (False, "spacy_unavailable"))

    result = ParserAssistedChunker().chunk_sentence_with_trace("The system learns.")

    assert result.optimization.fallback_used
    assert result.optimization.fallback_reason == "parser_unavailable:spacy_unavailable"
    assert [chunk.text for chunk in result.chunks]


def test_config_hash_is_stable_and_records_are_parser_native_free():
    config = OptimizerConfig()
    assert config.stable_hash() == OptimizerConfig().stable_hash()

    parse = parse_from_words("Alpha beta.", ["Alpha", "beta", "."])
    for token in parse.tokens:
        assert dataclasses.is_dataclass(token)
        assert token.__class__.__module__.startswith("semantic_rsvp.")
