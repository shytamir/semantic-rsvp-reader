from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.timing.engine import (
    compute_duration_ms,
    explain_duration,
    has_quote_boundary,
    has_sentence_ending_punctuation,
    has_strong_internal_punctuation,
    is_extra_dense_chunk,
)
from semantic_rsvp.timing.models import TimingConfig


def make_chunk(
    text="chunk",
    syntactic_hint="normal",
    char_length=None,
    content_word_count=1,
):
    return Chunk(
        text=text,
        content_word_count=content_word_count,
        char_length=char_length if char_length is not None else len(text),
        syntactic_hint=syntactic_hint,
    )


def test_same_chunk_produces_same_duration():
    chunk = make_chunk("The system", "normal")

    assert compute_duration_ms(chunk) == compute_duration_ms(chunk)


def test_light_chunks_are_faster_than_normal_chunks():
    light = make_chunk("of the", "light")
    normal = make_chunk("system", "normal")

    assert compute_duration_ms(light) < compute_duration_ms(normal)


def test_dense_chunks_are_slower_than_normal_chunks():
    dense = make_chunk("modern systems", "dense", content_word_count=2)
    normal = make_chunk("modern systems", "normal", content_word_count=2)

    assert compute_duration_ms(dense) > compute_duration_ms(normal)


def test_dense_chunks_receive_calibrated_settling_bonus():
    dense = make_chunk("pages can punish", "dense", content_word_count=2)
    explanation = explain_duration(dense)

    assert explanation["syntactic_multiplier"] == 1.3
    assert explanation["dense_settling_bonus_ms"] == 40
    assert compute_duration_ms(dense) == 600


def test_representative_dense_chunk_avoids_problematic_effective_band_at_115x():
    dense = make_chunk("pages can punish", "dense", content_word_count=2)

    effective_at_115 = compute_duration_ms(dense) / 1.15

    assert effective_at_115 >= 520


def test_extra_dense_chunk_gets_bounded_bonus():
    simple = make_chunk("pages can punish", "dense", content_word_count=2)
    extra_dense = make_chunk(
        "hesitate before responding",
        "dense",
        content_word_count=2,
    )
    explanation = explain_duration(extra_dense)

    assert is_extra_dense_chunk(extra_dense)
    assert explanation["extra_dense_bonus_ms"] == 50
    assert compute_duration_ms(extra_dense) > compute_duration_ms(simple)


def test_extra_dense_bonus_only_applies_to_dense_chunks():
    normal = make_chunk("hesitate before responding", "normal", content_word_count=2)

    assert not is_extra_dense_chunk(normal)
    assert explain_duration(normal)["extra_dense_bonus_ms"] == 0


def test_sentence_ending_punctuation_adds_pause():
    plain = make_chunk("system", "normal")
    ended = make_chunk("system.", "normal")

    assert compute_duration_ms(ended) > compute_duration_ms(plain)


def test_dense_sentence_ending_chunks_receive_extra_settling_time():
    plain = make_chunk("return a response", "dense", content_word_count=2)
    ended = make_chunk("return a response.", "dense", content_word_count=2)
    explanation = explain_duration(ended)

    assert explanation["sentence_pause_ms"] == 180
    assert explanation["dense_sentence_end_bonus_ms"] == 40
    assert compute_duration_ms(ended) > compute_duration_ms(plain)


def test_quote_boundary_chunks_receive_small_bonus():
    plain = make_chunk("however,", "punctuation")
    quoted = make_chunk('"however,', "punctuation")
    explanation = explain_duration(quoted)

    assert has_quote_boundary(quoted.text)
    assert explanation["punctuation_bonus_ms"] == 100
    assert compute_duration_ms(quoted) > compute_duration_ms(plain)


def test_closing_quote_boundary_chunks_receive_small_bonus():
    plain = make_chunk("is incomplete", "normal")
    quoted = make_chunk('is incomplete"', "normal")

    assert has_quote_boundary(quoted.text)
    assert compute_duration_ms(quoted) > compute_duration_ms(plain)


def test_colon_and_semicolon_chunks_receive_bounded_bonus():
    plain = make_chunk("mind", "normal")
    semicolon = make_chunk("mind;", "normal")
    colon = make_chunk("qualitative:", "normal")

    assert has_strong_internal_punctuation(semicolon.text)
    assert has_strong_internal_punctuation(colon.text)
    assert compute_duration_ms(semicolon) > compute_duration_ms(plain)
    assert explain_duration(semicolon)["punctuation_bonus_ms"] == 70
    assert explain_duration(colon)["punctuation_bonus_ms"] == 70


def test_light_comma_chunks_are_not_overpaused_by_punctuation_calibration():
    light_comma = make_chunk("and,", "light")
    light_plain = make_chunk("and", "light")
    normal = make_chunk("system", "normal")

    assert compute_duration_ms(light_comma) == compute_duration_ms(light_plain)
    assert compute_duration_ms(light_comma) < compute_duration_ms(normal)


def test_punctuation_helpers_detect_reported_boundaries():
    assert has_quote_boundary('"however,')
    assert has_quote_boundary('incomplete"')
    assert has_strong_internal_punctuation("qualitative:")
    assert has_sentence_ending_punctuation('response."')


def test_duration_is_clamped_to_minimum():
    config = TimingConfig(base_beat_ms=100, min_duration_ms=180)
    punctuation = make_chunk(",", "punctuation")

    assert compute_duration_ms(punctuation, config) == 180


def test_duration_is_clamped_to_maximum():
    config = TimingConfig(base_beat_ms=1000, max_duration_ms=900)
    dense = make_chunk("a very long dense chunk.", "dense", char_length=60)

    assert compute_duration_ms(dense, config) == 900


def test_unknown_syntactic_hint_falls_back_safely():
    unknown = make_chunk("system", "mystery")
    normal = make_chunk("system", "normal")

    assert compute_duration_ms(unknown) == compute_duration_ms(normal)
