from __future__ import annotations

from dataclasses import dataclass
import logging
from threading import Lock

from semantic_rsvp.chunking.interface import Chunker
from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter import (
    PINNED_MODEL_NAME,
    PINNED_MODEL_VERSION,
    PINNED_SPACY_VERSION,
    availability as provider_availability,
)

DEFAULT_CHUNKER_MODE = "parser_assisted"
RULE_BASED_MODE = "rule_based"
PARSER_ASSISTED_MODE = "parser_assisted"
VALID_CHUNKER_MODES = (PARSER_ASSISTED_MODE, RULE_BASED_MODE)

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class ChunkingState:
    configured_mode: str
    active_mode: str
    provider: str | None
    provider_available: bool
    provider_reason: str
    fallback: str

    def to_dict(self) -> dict[str, str | bool | None]:
        return {
            "configured_mode": self.configured_mode,
            "active_mode": self.active_mode,
            "provider": self.provider,
            "provider_available": self.provider_available,
            "provider_reason": self.provider_reason,
            "fallback": self.fallback,
        }


class ObservedParserAssistedChunker(Chunker):
    """Wrap the frozen S-023 parser chunker with production observability."""

    def __init__(
        self,
        parser_chunker: ParserAssistedChunker | None = None,
        logger: logging.Logger | None = None,
    ):
        self._parser_chunker = parser_chunker or ParserAssistedChunker()
        self._logger = logger or _LOGGER
        self._logged_fallback_reasons: set[str] = set()
        self._log_lock = Lock()

    def chunk_sentence(self, sentence: str) -> list[Chunk]:
        result = self._parser_chunker.chunk_sentence_with_trace(sentence)
        if result.optimization.fallback_used:
            self._log_fallback(result.optimization.fallback_reason or "unknown")
        return list(result.chunks)

    def _log_fallback(self, reason: str) -> None:
        reason_category = reason.split(":", 1)[0]
        with self._log_lock:
            if reason_category in self._logged_fallback_reasons:
                return
            self._logged_fallback_reasons.add(reason_category)
        self._logger.warning(
            "Parser-assisted chunker fell back to rule_based; reason_category=%s",
            reason_category,
        )


def normalize_chunker_mode(mode: str | None) -> str:
    normalized = (mode or DEFAULT_CHUNKER_MODE).strip().lower()
    if normalized not in VALID_CHUNKER_MODES:
        valid = ", ".join(VALID_CHUNKER_MODES)
        raise ValueError(f"Invalid RSVP_CHUNKER_MODE '{mode}'. Expected one of: {valid}.")
    return normalized


def create_chunker(mode: str | None = None) -> Chunker:
    normalized_mode = normalize_chunker_mode(mode)
    if normalized_mode == RULE_BASED_MODE:
        return RuleBasedChunker()
    return ObservedParserAssistedChunker()


def inspect_chunking_state(mode: str | None = None) -> ChunkingState:
    normalized_mode = normalize_chunker_mode(mode)
    if normalized_mode == RULE_BASED_MODE:
        return ChunkingState(
            configured_mode=RULE_BASED_MODE,
            active_mode=RULE_BASED_MODE,
            provider=None,
            provider_available=False,
            provider_reason="not_configured",
            fallback=RULE_BASED_MODE,
        )

    available, reason = provider_availability()
    return ChunkingState(
        configured_mode=PARSER_ASSISTED_MODE,
        active_mode=PARSER_ASSISTED_MODE,
        provider=f"spacy:{PINNED_SPACY_VERSION}/{PINNED_MODEL_NAME}:{PINNED_MODEL_VERSION}",
        provider_available=available,
        provider_reason=reason,
        fallback=RULE_BASED_MODE,
    )
