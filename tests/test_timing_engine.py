from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.timing.engine import compute_duration_ms
from semantic_rsvp.timing.models import TimingConfig


def make_chunk(text="chunk", syntactic_hint="normal", char_length=None):
    return Chunk(
        text=text,
        content_word_count=1,
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
    dense = make_chunk("modern systems", "dense")
    normal = make_chunk("system", "normal")

    assert compute_duration_ms(dense) > compute_duration_ms(normal)


def test_sentence_ending_punctuation_adds_pause():
    plain = make_chunk("system", "normal")
    ended = make_chunk("system.", "normal")

    assert compute_duration_ms(ended) > compute_duration_ms(plain)


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
