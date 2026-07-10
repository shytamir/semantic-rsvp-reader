import re

from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.timing.models import TimingConfig

_HINT_MULTIPLIERS = {
    "punctuation": 0.5,
    "light": 0.75,
    "normal": 1.0,
    "dense": 1.3,
}
_DENSE_SETTLING_BONUS_MS = 40
_EXTRA_DENSE_BONUS_MS = 50
_DENSE_SENTENCE_END_BONUS_MS = 40
_QUOTE_BOUNDARY_BONUS_MS = 60
_STRONG_PUNCTUATION_BONUS_MS = 40
_COMMA_QUOTE_PRIMING_BONUS_MS = 30
_LONG_CONTENT_WORD_MIN_LENGTH = 9
_REFLECTIVE_WORDS = {
    "consider",
    "contemplate",
    "evaluate",
    "hesitate",
    "interpret",
    "preserve",
    "preserves",
    "reconstruct",
    "reconstructs",
    "reflect",
    "responding",
    "ruminate",
}
_WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def compute_duration_ms(chunk: Chunk, config: TimingConfig | None = None) -> int:
    explanation = explain_duration(chunk, config)
    return int(explanation["duration_ms"])


def explain_duration(chunk: Chunk, config: TimingConfig | None = None) -> dict:
    timing_config = config or TimingConfig()
    multiplier = _HINT_MULTIPLIERS.get(chunk.syntactic_hint, 1.0)

    duration = timing_config.base_beat_ms * multiplier
    length_bonus_ms = _length_adjustment_ms(chunk)
    dense_bonus_ms = _dense_settling_bonus_ms(chunk)
    extra_dense_bonus_ms = _extra_dense_bonus_ms(chunk)
    punctuation_bonus_ms = _punctuation_bonus_ms(chunk)
    sentence_pause_ms = timing_config.sentence_pause_ms if _ends_sentence(chunk.text) else 0
    dense_sentence_end_bonus_ms = (
        _DENSE_SENTENCE_END_BONUS_MS
        if chunk.syntactic_hint == "dense" and _ends_sentence(chunk.text)
        else 0
    )

    duration += length_bonus_ms
    duration += dense_bonus_ms
    duration += extra_dense_bonus_ms
    duration += punctuation_bonus_ms
    duration += sentence_pause_ms
    duration += dense_sentence_end_bonus_ms

    duration_ms = _clamp(round(duration), timing_config)
    return {
        "base_beat_ms": timing_config.base_beat_ms,
        "syntactic_hint": chunk.syntactic_hint,
        "syntactic_multiplier": multiplier,
        "length_bonus_ms": length_bonus_ms,
        "dense_settling_bonus_ms": dense_bonus_ms,
        "extra_dense_bonus_ms": extra_dense_bonus_ms,
        "punctuation_bonus_ms": punctuation_bonus_ms,
        "sentence_pause_ms": sentence_pause_ms,
        "dense_sentence_end_bonus_ms": dense_sentence_end_bonus_ms,
        "duration_ms": duration_ms,
    }


def _length_adjustment_ms(chunk: Chunk) -> int:
    if chunk.char_length <= 8:
        return 0
    if chunk.char_length <= 18:
        return 40
    if chunk.char_length <= 32:
        return 80
    return 120


def _dense_settling_bonus_ms(chunk: Chunk) -> int:
    if chunk.syntactic_hint != "dense":
        return 0
    return _DENSE_SETTLING_BONUS_MS


def _extra_dense_bonus_ms(chunk: Chunk) -> int:
    if not is_extra_dense_chunk(chunk):
        return 0
    return _EXTRA_DENSE_BONUS_MS


def is_extra_dense_chunk(chunk: Chunk) -> bool:
    if chunk.syntactic_hint != "dense":
        return False
    words = _words(chunk.text)
    return any(
        len(word) >= _LONG_CONTENT_WORD_MIN_LENGTH or word.lower() in _REFLECTIVE_WORDS
        for word in words
    )


def _punctuation_bonus_ms(chunk: Chunk) -> int:
    bonus = 0
    text = chunk.text.strip()
    if _has_quote_boundary(text):
        bonus += _QUOTE_BOUNDARY_BONUS_MS
    if _has_strong_internal_punctuation(text):
        bonus += _STRONG_PUNCTUATION_BONUS_MS
    if _is_quote_priming_comma(text):
        bonus += _COMMA_QUOTE_PRIMING_BONUS_MS
    return bonus


def _has_quote_boundary(text: str) -> bool:
    stripped = text.strip()
    return stripped.startswith(('"', "'")) or stripped.endswith(('"', "'"))


def _has_strong_internal_punctuation(text: str) -> bool:
    return any(mark in text for mark in (";", ":"))


def _is_quote_priming_comma(text: str) -> bool:
    stripped = text.strip()
    return stripped.startswith(('"', "'")) and stripped.endswith(",")


def _ends_sentence(text: str) -> bool:
    stripped = text.strip()
    return stripped.rstrip("\"'").endswith(("...", ".", "!", "?"))


def _words(text: str) -> list[str]:
    return _WORD_PATTERN.findall(text)


def has_quote_boundary(text: str) -> bool:
    return _has_quote_boundary(text)


def has_strong_internal_punctuation(text: str) -> bool:
    return _has_strong_internal_punctuation(text)


def has_sentence_ending_punctuation(text: str) -> bool:
    return _ends_sentence(text)


def _clamp(duration_ms: int, config: TimingConfig) -> int:
    return max(config.min_duration_ms, min(config.max_duration_ms, duration_ms))
