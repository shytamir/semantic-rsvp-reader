from typing import Protocol

from semantic_rsvp.chunking.models import Chunk


class Chunker(Protocol):
    def chunk_sentence(self, sentence: str) -> list[Chunk]:
        ...
