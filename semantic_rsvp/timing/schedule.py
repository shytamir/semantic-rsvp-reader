from dataclasses import dataclass

from semantic_rsvp.chunking.interface import Chunker
from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.engine import compute_duration_ms
from semantic_rsvp.timing.models import TimingConfig


@dataclass(frozen=True)
class ScheduledChunk:
    chunk: Chunk
    duration_ms: int
    index: int
    sentence_index: int


def build_schedule(
    sentences: list[str],
    chunker: Chunker | None = None,
    config: TimingConfig | None = None,
) -> list[ScheduledChunk]:
    active_chunker = chunker or RuleBasedChunker()
    schedule: list[ScheduledChunk] = []

    for sentence_index, sentence in enumerate(sentences):
        for chunk in active_chunker.chunk_sentence(sentence):
            schedule.append(
                ScheduledChunk(
                    chunk=chunk,
                    duration_ms=compute_duration_ms(chunk, config),
                    index=len(schedule),
                    sentence_index=sentence_index,
                )
            )

    return schedule


def schedule_text(
    raw_text: str,
    config: TimingConfig | None = None,
) -> list[ScheduledChunk]:
    normalized_text = normalize_text(raw_text)
    if not normalized_text:
        return []
    return build_schedule(split_sentences(normalized_text), config=config)
