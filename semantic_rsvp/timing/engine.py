from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.timing.models import TimingConfig

_HINT_MULTIPLIERS = {
    "punctuation": 0.5,
    "light": 0.75,
    "normal": 1.0,
    "dense": 1.25,
}


def compute_duration_ms(chunk: Chunk, config: TimingConfig | None = None) -> int:
    timing_config = config or TimingConfig()
    multiplier = _HINT_MULTIPLIERS.get(chunk.syntactic_hint, 1.0)

    duration = timing_config.base_beat_ms * multiplier
    duration += _length_adjustment_ms(chunk)

    if _ends_sentence(chunk.text):
        duration += timing_config.sentence_pause_ms

    return _clamp(round(duration), timing_config)


def _length_adjustment_ms(chunk: Chunk) -> int:
    if chunk.char_length <= 8:
        return 0
    if chunk.char_length <= 18:
        return 40
    if chunk.char_length <= 32:
        return 80
    return 120


def _ends_sentence(text: str) -> bool:
    stripped = text.strip()
    return stripped.endswith(("...", ".", "!", "?"))


def _clamp(duration_ms: int, config: TimingConfig) -> int:
    return max(config.min_duration_ms, min(config.max_duration_ms, duration_ms))
