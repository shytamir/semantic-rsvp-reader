from dataclasses import dataclass


@dataclass(frozen=True)
class NavigationMeta:
    char_start: int = 0
    char_end: int = 0
    char_count_total: int = 0
    progress_ratio: float = 0.0
    progress_percent: int = 0
    paragraph_index: int = 0
    is_paragraph_start: bool = False
    is_paragraph_end: bool = False
    is_progress_milestone: bool = False
