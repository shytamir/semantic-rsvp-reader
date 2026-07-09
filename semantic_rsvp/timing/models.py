from dataclasses import dataclass


@dataclass(frozen=True)
class TimingConfig:
    base_beat_ms: int = 400
    min_duration_ms: int = 150
    max_duration_ms: int = 1200
    sentence_pause_ms: int = 180

    def __post_init__(self) -> None:
        if self.base_beat_ms < 1:
            raise ValueError("base_beat_ms must be at least 1.")
        if self.min_duration_ms < 1:
            raise ValueError("min_duration_ms must be at least 1.")
        if self.max_duration_ms < self.min_duration_ms:
            raise ValueError("max_duration_ms must be greater than or equal to min_duration_ms.")
        if self.sentence_pause_ms < 0:
            raise ValueError("sentence_pause_ms must be zero or greater.")
