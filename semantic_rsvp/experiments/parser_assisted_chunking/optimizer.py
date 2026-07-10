from __future__ import annotations

import math
import re
from dataclasses import dataclass

from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import count_content_words, tokenize
from semantic_rsvp.experiments.parser_assisted_chunking.alignment import validate_alignment
from semantic_rsvp.experiments.parser_assisted_chunking.config import OptimizerConfig
from semantic_rsvp.experiments.parser_assisted_chunking.models import (
    ChunkTrace,
    LinguisticRelation,
    LinguisticSpan,
    ParseResult,
    OptimizationResult,
    ScoreFactor,
)

_WORD_RE = re.compile(r"[A-Za-z0-9]")
_CLAUSE_DEPS = {"advcl", "relcl", "ccomp", "xcomp", "conj"}
_STRONG_DEPS = {"compound", "amod", "det", "poss", "nummod"}
_DATE_NUMBER_SPANS = {"date", "time", "money", "quantity", "cardinal", "ordinal", "number"}


@dataclass(frozen=True)
class _Candidate:
    start_index: int
    end_index: int
    start: int
    end: int
    text: str
    content_word_count: int
    cost: float
    positive: tuple[ScoreFactor, ...]
    negative: tuple[ScoreFactor, ...]
    constraints: tuple[str, ...]
    features: tuple[str, ...]


def optimize_chunks(parse: ParseResult, config: OptimizerConfig | None = None) -> OptimizationResult:
    active_config = config or OptimizerConfig()
    aligned, diagnostics = validate_alignment(parse)
    if not aligned:
        return OptimizationResult(
            chunks=(),
            traces=(),
            total_cost=math.inf,
            config_version=active_config.version,
            config_hash=active_config.stable_hash(),
            fallback_used=True,
            fallback_reason="alignment_invalid",
            diagnostics=diagnostics,
        )
    if not parse.tokens:
        return OptimizationResult(
            chunks=(),
            traces=(),
            total_cost=0,
            config_version=active_config.version,
            config_hash=active_config.stable_hash(),
        )

    best: list[tuple[float, int, tuple[_Candidate, ...]] | None] = [None] * (len(parse.tokens) + 1)
    best[0] = (0.0, 0, ())
    for end in range(1, len(parse.tokens) + 1):
        candidates: list[tuple[float, int, int, tuple[_Candidate, ...]]] = []
        for start in range(max(0, end - active_config.max_candidate_tokens), end):
            previous = best[start]
            if previous is None:
                continue
            candidate = _build_candidate(parse, start, end, active_config)
            if candidate is None:
                continue
            total_cost = previous[0] + candidate.cost
            chunk_count = previous[1] + 1
            candidates.append((total_cost, chunk_count, -len(candidate.text), (*previous[2], candidate)))
        if candidates:
            total_cost, chunk_count, _tie, path = min(candidates, key=lambda item: (round(item[0], 8), item[1], item[2]))
            best[end] = (total_cost, chunk_count, path)

    final = best[-1]
    if final is None:
        return OptimizationResult(
            chunks=(),
            traces=(),
            total_cost=math.inf,
            config_version=active_config.version,
            config_hash=active_config.stable_hash(),
            fallback_used=True,
            fallback_reason="no_valid_optimization_path",
        )

    path = final[2]
    chunks = tuple(_chunk_from_candidate(candidate) for candidate in path)
    traces = tuple(_trace_from_candidate(candidate) for candidate in path)
    return OptimizationResult(
        chunks=chunks,
        traces=traces,
        total_cost=final[0],
        config_version=active_config.version,
        config_hash=active_config.stable_hash(),
    )


def _build_candidate(parse: ParseResult, start: int, end: int, config: OptimizerConfig) -> _Candidate | None:
    tokens = parse.tokens[start:end]
    source_start = tokens[0].start
    source_end = tokens[-1].end
    text = parse.text[source_start:source_end].strip()
    if not text:
        return None
    unsplittable = (
        config.allow_unsplittable_token_exception
        and len(tokens) == 1
        and len(text) > config.max_chars
    )
    if len(text) > config.max_chars and not unsplittable:
        return None

    content_words = count_content_words(tokenize(text))
    positive: list[ScoreFactor] = []
    negative: list[ScoreFactor] = []
    constraints = ["contiguous_source_range", "safe_alignment"]
    if unsplittable:
        constraints.append("unsplittable_token_exception")
    features: list[str] = []
    cost = abs(len(text) - config.balance_target_chars) * config.balance_penalty
    if len(text) <= 6:
        cost += config.underfilled_chunk_penalty
        negative.append(ScoreFactor("underfilled_chunk_penalty", config.underfilled_chunk_penalty, text))
    if content_words > config.max_content_words:
        overage = content_words - config.max_content_words
        penalty = overage * config.content_word_overage_penalty
        cost += penalty
        negative.append(ScoreFactor("content_word_overage_penalty", penalty, str(content_words)))
    if len(text) > 26 and not unsplittable:
        cost += config.long_chunk_penalty
        negative.append(ScoreFactor("long_chunk_penalty", config.long_chunk_penalty, str(len(text))))

    boundary = source_end
    if end < len(parse.tokens):
        boundary_cost, boundary_positive, boundary_negative, boundary_features = _boundary_cost(parse, boundary, config)
        cost += boundary_cost
        positive.extend(boundary_positive)
        negative.extend(boundary_negative)
        features.extend(boundary_features)
    else:
        cost += config.terminal_boundary_reward
        positive.append(ScoreFactor("terminal_boundary_reward", config.terminal_boundary_reward, "end of sentence"))

    if text[-1:] in ",;:!?.":
        cost += config.punctuation_boundary_reward
        positive.append(ScoreFactor("punctuation_boundary_reward", config.punctuation_boundary_reward, text[-1]))

    return _Candidate(
        start_index=start,
        end_index=end,
        start=source_start,
        end=source_end,
        text=text,
        content_word_count=content_words,
        cost=cost,
        positive=tuple(positive),
        negative=tuple(negative),
        constraints=tuple(constraints),
        features=tuple(features),
    )


def _boundary_cost(
    parse: ParseResult,
    boundary: int,
    config: OptimizerConfig,
) -> tuple[float, list[ScoreFactor], list[ScoreFactor], list[str]]:
    cost = 0.0
    positive: list[ScoreFactor] = []
    negative: list[ScoreFactor] = []
    features: list[str] = []
    for span in parse.spans:
        if span.start < boundary < span.end:
            penalty = _span_penalty(span, config)
            cost += penalty
            negative.append(ScoreFactor(f"{span.span_type}_split_penalty", penalty, span.label))
            features.append(f"split_span:{span.span_type}:{span.label}")
    for relation in parse.relations:
        source = _token_by_id(parse, relation.source_id)
        target = _token_by_id(parse, relation.target_id)
        if not source or not target:
            continue
        left = min(source.start, target.start)
        right = max(source.end, target.end)
        if left < boundary < right:
            penalty = config.relation_split_penalty
            if relation.relation_type in {"aux_main", "negation", "verb_particle"}:
                penalty += 20
            if relation.relation_type == "dependency" and source.dep in _STRONG_DEPS:
                penalty += config.strong_dependency_split_penalty
            cost += penalty
            negative.append(ScoreFactor(f"{relation.relation_type}_split_penalty", penalty))
            features.append(f"split_relation:{relation.relation_type}")
    previous_token = next((token for token in parse.tokens if token.end == boundary), None)
    if previous_token and previous_token.dep in _CLAUSE_DEPS:
        cost += config.clause_boundary_reward
        positive.append(ScoreFactor("clause_boundary_reward", config.clause_boundary_reward, previous_token.dep))
    return cost, positive, negative, features


def _span_penalty(span: LinguisticSpan, config: OptimizerConfig) -> float:
    span_type = span.span_type.lower()
    label = span.label.lower()
    if span_type == "entity" or label in {"person", "org", "gpe", "loc"}:
        return config.entity_split_penalty
    if span_type in _DATE_NUMBER_SPANS or label in _DATE_NUMBER_SPANS:
        return config.date_number_split_penalty
    return config.span_split_penalty


def _token_by_id(parse: ParseResult, token_id: int):
    return next((token for token in parse.tokens if token.token_id == token_id), None)


def _chunk_from_candidate(candidate: _Candidate) -> Chunk:
    hint = "dense" if candidate.content_word_count > 1 else "normal"
    if not any(_WORD_RE.search(char) for char in candidate.text):
        hint = "punctuation"
    elif candidate.content_word_count == 0:
        hint = "light"
    return Chunk(
        text=candidate.text,
        content_word_count=candidate.content_word_count,
        char_length=len(candidate.text),
        syntactic_hint=hint,
    )


def _trace_from_candidate(candidate: _Candidate) -> ChunkTrace:
    return ChunkTrace(
        start=candidate.start,
        end=candidate.end,
        text=candidate.text,
        char_length=len(candidate.text),
        content_word_count=candidate.content_word_count,
        cost=candidate.cost,
        positive_factors=candidate.positive,
        negative_factors=candidate.negative,
        hard_constraints=candidate.constraints,
        parser_features=candidate.features,
    )
