from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.chunking_experiment_common import load_cases
from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.engine import explain_duration
from semantic_rsvp.timing.models import TimingConfig


WORD_PATTERN = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?")


def _distribution(values: list[int]) -> dict:
    ordered = sorted(values)
    return {
        "min": min(ordered),
        "median": statistics.median(ordered),
        "p90": ordered[min(len(ordered) - 1, int((len(ordered) - 1) * 0.9))],
        "max": max(ordered),
        "mean": round(statistics.mean(ordered), 3),
    }


def _measure(text: str, chunker) -> dict:
    chunks = [chunk for sentence in split_sentences(normalize_text(text)) for chunk in chunker.chunk_sentence(sentence)]
    config = TimingConfig()
    explanations = [explain_duration(chunk, config) for chunk in chunks]
    words = [len(WORD_PATTERN.findall(chunk.text)) for chunk in chunks]
    content_words = [chunk.content_word_count for chunk in chunks]
    durations = [item["duration_ms"] for item in explanations]
    word_total = sum(words)
    content_total = sum(content_words)
    return {
        "chunk_count": len(chunks),
        "word_count": word_total,
        "content_word_count": content_total,
        "words_per_chunk": round(word_total / len(chunks), 3),
        "content_words_per_chunk": round(content_total / len(chunks), 3),
        "character_length": _distribution([chunk.char_length for chunk in chunks]),
        "syntactic_hints": dict(sorted(Counter(chunk.syntactic_hint for chunk in chunks).items())),
        "total_duration_ms": sum(durations),
        "milliseconds_per_word": round(sum(durations) / word_total, 3),
        "milliseconds_per_content_word": round(sum(durations) / content_total, 3),
        "minimum_clamp_count": sum(duration == config.min_duration_ms for duration in durations),
        "maximum_clamp_count": sum(duration == config.max_duration_ms for duration in durations),
    }


def _aggregate(samples: list[dict], mode: str) -> dict:
    metrics = [sample[mode] for sample in samples]
    chunks = sum(item["chunk_count"] for item in metrics)
    words = sum(item["word_count"] for item in metrics)
    content = sum(item["content_word_count"] for item in metrics)
    duration = sum(item["total_duration_ms"] for item in metrics)
    hints = Counter()
    for item in metrics:
        hints.update(item["syntactic_hints"])
    return {
        "sample_count": len(metrics),
        "chunk_count": chunks,
        "word_count": words,
        "content_word_count": content,
        "words_per_chunk": round(words / chunks, 3),
        "content_words_per_chunk": round(content / chunks, 3),
        "syntactic_hints": dict(sorted(hints.items())),
        "total_duration_ms": duration,
        "milliseconds_per_word": round(duration / words, 3),
        "milliseconds_per_content_word": round(duration / content, 3),
        "minimum_clamp_count": sum(item["minimum_clamp_count"] for item in metrics),
        "maximum_clamp_count": sum(item["maximum_clamp_count"] for item in metrics),
    }


def build_report(phase: str) -> dict:
    samples = []
    parser = ParserAssistedChunker()
    rule_based = RuleBasedChunker()
    for case in load_cases():
        samples.append({
            "case_id": case["case_id"],
            "corpus": case["corpus"],
            "rule_based": _measure(case["text"], rule_based),
            "parser_assisted": _measure(case["text"], parser),
        })
    aggregate = {mode: _aggregate(samples, mode) for mode in ("rule_based", "parser_assisted")}
    rule = aggregate["rule_based"]
    parser_metrics = aggregate["parser_assisted"]
    aggregate["comparison"] = {
        "chunk_count_change_percent": round((parser_metrics["chunk_count"] / rule["chunk_count"] - 1) * 100, 3),
        "words_per_chunk_change_percent": round((parser_metrics["words_per_chunk"] / rule["words_per_chunk"] - 1) * 100, 3),
        "content_words_per_chunk_change_percent": round((parser_metrics["content_words_per_chunk"] / rule["content_words_per_chunk"] - 1) * 100, 3),
        "parser_minus_rule_ms_per_word": round(parser_metrics["milliseconds_per_word"] - rule["milliseconds_per_word"], 3),
        "parser_effective_rate_change_percent": round((rule["milliseconds_per_word"] / parser_metrics["milliseconds_per_word"] - 1) * 100, 3),
    }
    return {"slice": "S-029", "phase": phase, "timing_config": vars(TimingConfig()), "samples": samples, "aggregate": aggregate}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", required=True, choices=("before", "after"))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    report = build_report(args.phase)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["aggregate"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
