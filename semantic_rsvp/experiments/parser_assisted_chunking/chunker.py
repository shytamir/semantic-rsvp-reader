from __future__ import annotations

from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.config import OptimizerConfig
from semantic_rsvp.experiments.parser_assisted_chunking.models import (
    OptimizationResult,
    ParseResult,
    ParserAssistedResult,
)
from semantic_rsvp.experiments.parser_assisted_chunking.optimizer import optimize_chunks
from semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter import (
    availability,
    parse_text,
)


class ParserAssistedChunker:
    def __init__(
        self,
        config: OptimizerConfig | None = None,
        fallback_chunker: RuleBasedChunker | None = None,
    ):
        self.config = config or OptimizerConfig()
        self.fallback_chunker = fallback_chunker or RuleBasedChunker(
            max_chars=self.config.max_chars,
            max_content_words=self.config.max_content_words,
        )

    def chunk_sentence(self, sentence: str) -> list[Chunk]:
        return list(self.chunk_sentence_with_trace(sentence).chunks)

    def chunk_sentence_with_trace(self, sentence: str) -> ParserAssistedResult:
        available, reason = availability()
        if not available:
            return self._fallback(sentence, None, f"parser_unavailable:{reason}")
        parse = parse_text(sentence)
        if parse.failure_reason:
            return self._fallback(sentence, parse, parse.failure_reason)
        optimization = optimize_chunks(parse, self.config)
        if optimization.fallback_used:
            return self._fallback(sentence, parse, optimization.fallback_reason or "optimization_failed")
        if not _postconditions_hold(sentence, optimization, self.config.max_chars):
            return self._fallback(sentence, parse, "postcondition_failed")
        return ParserAssistedResult(tuple(optimization.chunks), parse, optimization)

    def _fallback(
        self,
        sentence: str,
        parse: ParseResult | None,
        reason: str,
    ) -> ParserAssistedResult:
        chunks = tuple(self.fallback_chunker.chunk_sentence(sentence))
        optimization = OptimizationResult(
            chunks=chunks,
            traces=(),
            total_cost=0,
            config_version=self.config.version,
            config_hash=self.config.stable_hash(),
            fallback_used=True,
            fallback_reason=reason,
        )
        return ParserAssistedResult(chunks, parse, optimization)


def _postconditions_hold(sentence: str, optimization: OptimizationResult, max_chars: int) -> bool:
    if not optimization.chunks:
        return not sentence.strip()
    cursor = 0
    for trace in optimization.traces:
        start = sentence.find(trace.text, cursor)
        if start == -1:
            return False
        cursor = start + len(trace.text)
        if trace.char_length > max_chars and "unsplittable" not in trace.hard_constraints:
            return False
    return True
