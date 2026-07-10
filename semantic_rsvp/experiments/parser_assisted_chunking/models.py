from __future__ import annotations

from dataclasses import dataclass, field

from semantic_rsvp.chunking.models import Chunk


@dataclass(frozen=True)
class LinguisticToken:
    token_id: int
    text: str
    start: int
    end: int
    sentence_index: int
    pos: str = ""
    tag: str = ""
    dep: str = ""
    head_id: int | None = None
    entity_type: str = ""
    whitespace: str = ""


@dataclass(frozen=True)
class LinguisticSpan:
    start: int
    end: int
    span_type: str
    label: str = ""
    evidence_source: str = ""


@dataclass(frozen=True)
class LinguisticRelation:
    source_id: int
    target_id: int
    relation_type: str
    evidence_source: str = ""


@dataclass(frozen=True)
class ParseResult:
    text: str
    tokens: tuple[LinguisticToken, ...]
    spans: tuple[LinguisticSpan, ...] = ()
    relations: tuple[LinguisticRelation, ...] = ()
    parser_library: str = ""
    parser_version: str = ""
    model_name: str = ""
    model_version: str = ""
    alignment_status: str = "unknown"
    alignment_diagnostics: tuple[str, ...] = ()
    failure_reason: str | None = None


@dataclass(frozen=True)
class ScoreFactor:
    name: str
    value: float
    detail: str = ""


@dataclass(frozen=True)
class ChunkTrace:
    start: int
    end: int
    text: str
    char_length: int
    content_word_count: int
    cost: float
    positive_factors: tuple[ScoreFactor, ...] = ()
    negative_factors: tuple[ScoreFactor, ...] = ()
    hard_constraints: tuple[str, ...] = ()
    parser_features: tuple[str, ...] = ()


@dataclass(frozen=True)
class OptimizationResult:
    chunks: tuple[Chunk, ...]
    traces: tuple[ChunkTrace, ...]
    total_cost: float
    config_version: str
    config_hash: str
    fallback_used: bool = False
    fallback_reason: str | None = None
    diagnostics: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ParserAssistedResult:
    chunks: tuple[Chunk, ...]
    parse_result: ParseResult | None
    optimization: OptimizationResult
