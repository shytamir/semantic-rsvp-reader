from dataclasses import dataclass, replace

from semantic_rsvp.chunking.interface import Chunker
from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.navigation.metadata import compute_navigation_metadata
from semantic_rsvp.navigation.models import NavigationMeta
from semantic_rsvp.structure.markdown_headers import (
    StructureMeta,
    compute_structure_metadata,
)
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.display_state import DisplayState, DisplayStateTracker
from semantic_rsvp.timing.engine import compute_duration_ms
from semantic_rsvp.timing.models import TimingConfig


@dataclass(frozen=True)
class ScheduledChunk:
    chunk: Chunk
    duration_ms: int
    index: int
    sentence_index: int
    display_state: DisplayState
    navigation: NavigationMeta
    structure: StructureMeta


def build_schedule(
    sentences: list[str],
    chunker: Chunker | None = None,
    config: TimingConfig | None = None,
) -> list[ScheduledChunk]:
    active_chunker = chunker or RuleBasedChunker()
    schedule: list[ScheduledChunk] = []
    display_state_tracker = DisplayStateTracker()

    for sentence_index, sentence in enumerate(sentences):
        for chunk in active_chunker.chunk_sentence(sentence):
            display_state = display_state_tracker.annotate(chunk.text)
            schedule.append(
                ScheduledChunk(
                    chunk=chunk,
                    duration_ms=compute_duration_ms(chunk, config),
                    index=len(schedule),
                    sentence_index=sentence_index,
                    display_state=display_state,
                    navigation=NavigationMeta(),
                    structure=StructureMeta(),
                )
            )

    return schedule


def schedule_text(
    raw_text: str,
    config: TimingConfig | None = None,
    chunker: Chunker | None = None,
) -> list[ScheduledChunk]:
    normalized_text = normalize_text(raw_text)
    if not normalized_text:
        return []
    schedule = build_schedule(split_sentences(normalized_text), chunker=chunker, config=config)
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
