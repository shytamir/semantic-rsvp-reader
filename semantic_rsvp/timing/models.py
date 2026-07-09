from dataclasses import dataclass


@dataclass(frozen=True)
class TimingConfig:
    base_beat_ms: int = 400
    min_duration_ms: int = 150
    max_duration_ms: int = 1200
    sentence_pause_ms: int = 180
