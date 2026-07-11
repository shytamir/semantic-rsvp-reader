from __future__ import annotations

from dataclasses import dataclass
from dataclasses import replace

from semantic_rsvp.chunking.interface import Chunker
from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.selection import create_chunker
from semantic_rsvp.navigation.metadata import compute_navigation_metadata
from semantic_rsvp.structure.markdown_headers import compute_structure_metadata
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.models import TimingConfig
from semantic_rsvp.timing.schedule import ScheduledChunk, build_schedule


@dataclass(frozen=True)
class ScheduleResult:
    normalized_text: str
    sentences: tuple[str, ...]
    schedule: tuple[ScheduledChunk, ...]


@dataclass(frozen=True)
class ChunkResult:
    normalized_text: str
    chunks: tuple[Chunk, ...]


class ScheduleService:
    def __init__(self, chunker: Chunker | None = None):
        self._chunker = chunker or create_chunker()

    @property
    def chunker(self) -> Chunker:
        return self._chunker

    def generate(
        self,
        raw_text: str,
        *,
        timing_config: TimingConfig | None = None,
    ) -> ScheduleResult:
        normalized_text = normalize_text(raw_text)
        if not normalized_text:
            return ScheduleResult("", (), ())

        sentences = tuple(split_sentences(normalized_text))
        schedule = build_schedule(
            list(sentences),
            chunker=self._chunker,
            config=timing_config,
        )
        schedule_with_metadata = _attach_metadata(normalized_text, schedule)
        return ScheduleResult(
            normalized_text=normalized_text,
            sentences=sentences,
            schedule=tuple(schedule_with_metadata),
        )

    def chunk(self, raw_sentence: str) -> ChunkResult:
        normalized_sentence = normalize_text(raw_sentence)
        if not normalized_sentence:
            return ChunkResult("", ())
        return ChunkResult(
            normalized_text=normalized_sentence,
            chunks=tuple(self._chunker.chunk_sentence(normalized_sentence)),
        )

    def chunk_sentence(self, raw_sentence: str) -> tuple[Chunk, ...]:
        return self.chunk(raw_sentence).chunks


def _attach_metadata(
    normalized_text: str,
    schedule: list[ScheduledChunk],
) -> list[ScheduledChunk]:
    metadata = compute_navigation_metadata(
        normalized_text,
        [scheduled_chunk.chunk.text for scheduled_chunk in schedule],
    )
    structure_metadata = compute_structure_metadata(normalized_text, metadata)
    return [
        replace(scheduled_chunk, navigation=navigation, structure=structure)
        for scheduled_chunk, navigation, structure in zip(
            schedule,
            metadata,
            structure_metadata,
        )
    ]
