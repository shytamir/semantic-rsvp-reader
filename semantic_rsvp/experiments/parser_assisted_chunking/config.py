from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class OptimizerConfig:
    version: str = "parser-assisted-spike-v1"
    max_chars: int = 32
    max_content_words: int = 2
    max_candidate_tokens: int = 8
    allow_unsplittable_token_exception: bool = True
    underfilled_chunk_penalty: float = 6.0
    content_word_overage_penalty: float = 18.0
    long_chunk_penalty: float = 8.0
    balance_target_chars: int = 18
    balance_penalty: float = 0.15
    span_split_penalty: float = 35.0
    entity_split_penalty: float = 55.0
    date_number_split_penalty: float = 45.0
    relation_split_penalty: float = 30.0
    strong_dependency_split_penalty: float = 18.0
    punctuation_boundary_reward: float = -8.0
    clause_boundary_reward: float = -5.0
    terminal_boundary_reward: float = -12.0
    tie_breaker: str = "lowest_cost_then_fewest_chunks_then_leftmost_longest"

    def __post_init__(self) -> None:
        numeric_values = {
            "max_chars": self.max_chars,
            "max_content_words": self.max_content_words,
            "max_candidate_tokens": self.max_candidate_tokens,
            "balance_target_chars": self.balance_target_chars,
        }
        for name, value in numeric_values.items():
            if value < 1:
                raise ValueError(f"{name} must be positive.")

    def stable_hash(self) -> str:
        payload = json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()
