from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    text: str
    content_word_count: int
    char_length: int
    syntactic_hint: str = "unknown"
