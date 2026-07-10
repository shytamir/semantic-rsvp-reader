from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.timing.engine import (
    compute_duration_ms,
    explain_duration,
    has_comma_list_emphasis,
    is_extreme_semantic_density,
)
from semantic_rsvp.timing.models import TimingConfig


def make_chunk(text, syntactic_hint="dense", content_word_count=2):
    return Chunk(
        text=text,
        content_word_count=content_word_count,
        char_length=len(text),
        syntactic_hint=syntactic_hint,
    )


def chunk_texts(sentence: str) -> list[str]:
    return [chunk.text for chunk in RuleBasedChunker().chunk_sentence(sentence)]


def test_extreme_semantic_density_gets_more_duration_than_ordinary_dense_text():
    ordinary = make_chunk("pages can punish")
    extreme = make_chunk("a parenthetical may quietly")

    assert is_extreme_semantic_density(extreme)
    assert not is_extreme_semantic_density(ordinary)
    assert compute_duration_ms(extreme) > compute_duration_ms(ordinary)
    assert explain_duration(extreme)["extreme_density_bonus_ms"] > 0


def test_proper_noun_dense_chunk_receives_targeted_bonus():
    chunk = make_chunk("Department of Transportation")

    assert is_extreme_semantic_density(chunk)
    assert explain_duration(chunk)["extreme_density_bonus_ms"] > 0


def test_long_abstract_dense_chunk_receives_targeted_bonus():
    chunk = make_chunk("the duration is mathematically")

    assert is_extreme_semantic_density(chunk)
    assert explain_duration(chunk)["extreme_density_bonus_ms"] > 0


def test_ordinary_dense_chunk_does_not_receive_extreme_density_bonus():
    chunk = make_chunk("narrow the claim")

    assert not is_extreme_semantic_density(chunk)
    assert explain_duration(chunk)["extreme_density_bonus_ms"] == 0


def test_semicolon_and_colon_chunks_receive_bounded_followup_settling():
    semicolon = make_chunk("may rescue it;", "normal", content_word_count=1)
    colon = make_chunk("the rule:", "normal", content_word_count=1)

    assert explain_duration(semicolon)["punctuation_bonus_ms"] == 70
    assert explain_duration(colon)["punctuation_bonus_ms"] == 70


def test_quote_adjacent_chunks_receive_bounded_quote_rhythm_handling():
    quoted = make_chunk('intuition"', "normal", content_word_count=1)

    assert explain_duration(quoted)["punctuation_bonus_ms"] == 70


def test_comma_list_emphasis_is_handled_without_overpausing_every_comma():
    list_item = make_chunk("failures,", "normal", content_word_count=1)
    ordinary_comma = make_chunk("before it,", "normal", content_word_count=1)

    assert has_comma_list_emphasis(list_item.text)
    assert not has_comma_list_emphasis(ordinary_comma.text)
    assert explain_duration(list_item)["punctuation_bonus_ms"] == 20
    assert explain_duration(ordinary_comma)["punctuation_bonus_ms"] == 0


def test_light_chunks_are_not_globally_slowed_and_clamps_still_apply():
    light = make_chunk("as", "light", content_word_count=0)
    clamped = make_chunk("Department of Transportation.", "dense", content_word_count=2)
    config = TimingConfig(base_beat_ms=1000, max_duration_ms=900)

    assert compute_duration_ms(light) == 300
    assert compute_duration_ms(clamped, config) == 900


def test_as_is_not_orphaned_when_short_phrase_can_fit():
    assert "as" not in chunk_texts("as the reader moves")
    assert "as a result" in chunk_texts("as a result the reader paused.")
    assert any(
        chunk.startswith("as context changes")
        for chunk in chunk_texts("as context changes, the rule adapts.")
    )
    assert any(
        chunk.startswith("as a signal")
        for chunk in chunk_texts("The pause is understood as a signal.")
    )


def test_should_stays_near_main_verb_when_constraints_allow():
    chunks = chunk_texts("The system should preserve context.")

    assert "should" not in chunks
    assert any("should preserve" in chunk for chunk in chunks)


def test_should_not_remains_together_when_possible():
    chunks = chunk_texts("The reader should not hesitate.")

    assert "should" not in chunks
    assert "should not" not in chunks
    assert any("should not hesitate" in chunk for chunk in chunks)


def test_existing_auxiliary_modal_behavior_does_not_regress():
    chunks = chunk_texts(
        "If normalization removes too much punctuation, the segmenter may not know where the writer changed direction."
    )

    assert "may not" not in chunks
    assert any("may not know" in chunk for chunk in chunks)


def test_quote_spacing_cleanup_avoids_unreadable_join():
    assert normalize_text('intuition"cannot proceed') == 'intuition" cannot proceed'


def test_normal_quoted_phrases_remain_readable():
    assert (
        normalize_text('The phrase "semantic density" matters.')
        == 'The phrase "semantic density" matters.'
    )
    assert normalize_text('"however," the reader paused') == '"however," the reader paused'


def test_quote_spacing_cleanup_prevents_joined_chunks():
    chunks = chunk_texts(normalize_text('intuition"cannot proceed'))

    assert not any("intuition\"cannot" in chunk for chunk in chunks)
    assert any("cannot" in chunk for chunk in chunks)
