from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from pathlib import Path

try:
    from chunking_experiment_common import (
        EXPERIMENT_ROOT,
        REPO_ROOT,
        load_cases,
        load_json,
        manifest_hashes,
        write_json,
    )
except ModuleNotFoundError:
    from scripts.chunking_experiment_common import (
        EXPERIMENT_ROOT,
        REPO_ROOT,
        load_cases,
        load_json,
        manifest_hashes,
        write_json,
    )

sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.chunker import ParserAssistedChunker
from semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter import availability
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences


OUTPUT_PATH = EXPERIMENT_ROOT / "results" / "parser_assisted_development_regression.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", action="append", choices=["development", "regression"], default=[])
    parser.add_argument("--write", action="store_true")
    parser.add_argument(
        "--include-latency",
        action="store_true",
        help="Include run-specific latency measurements in the output.",
    )
    args = parser.parse_args(argv)

    corpora = set(args.corpus or ["development", "regression"])
    cases = [case for case in load_cases() if case["corpus"] in corpora]
    baseline = RuleBasedChunker()
    experimental = ParserAssistedChunker()
    available, availability_reason = availability()
    results = []
    fallback_count = 0
    start_all = time.perf_counter()
    for case in cases:
        start = time.perf_counter()
        normalized = normalize_text(case["text"])
        sentences = split_sentences(normalized)
        exp_results = [experimental.chunk_sentence_with_trace(sentence) for sentence in sentences]
        elapsed_ms = round((time.perf_counter() - start) * 1000, 3)
        fallback_used = any(result.optimization.fallback_used for result in exp_results)
        fallback_count += int(fallback_used)
        experimental_chunks = [chunk for result in exp_results for chunk in result.chunks]
        baseline_chunks = [
            chunk
            for sentence in sentences
            for chunk in baseline.chunk_sentence(sentence)
        ]
        trace_payload = [
            {
                "start": trace.start,
                "end": trace.end,
                "text": trace.text,
                "char_length": trace.char_length,
                "content_word_count": trace.content_word_count,
                "cost": trace.cost,
                "positive": [factor.__dict__ for factor in trace.positive_factors],
                "negative": [factor.__dict__ for factor in trace.negative_factors],
                "hard_constraints": list(trace.hard_constraints),
                "features": list(trace.parser_features),
            }
            for result in exp_results
            for trace in result.optimization.traces
        ]
        width_violations = [
            trace["text"]
            for trace in trace_payload
            if trace["char_length"] > experimental.config.max_chars
            and "unsplittable_token_exception" not in trace["hard_constraints"]
        ]
        result_payload = {
            "case_id": case["case_id"],
            "corpus": case["corpus"],
            "sentence_count": len(sentences),
            "baseline_chunks": [chunk.text for chunk in baseline_chunks],
            "experimental_chunks": [chunk.text for chunk in experimental_chunks],
            "fallback_used": fallback_used,
            "fallback_reason": ";".join(
                sorted(
                    {
                        result.optimization.fallback_reason
                        for result in exp_results
                        if result.optimization.fallback_reason
                    }
                )
            ) or None,
            "config_version": exp_results[0].optimization.config_version if exp_results else "",
            "config_hash": exp_results[0].optimization.config_hash if exp_results else "",
            "hard_compliance": {
                "source_ordering": True,
                "width_violation_count": len(width_violations),
                "width_violations": width_violations,
                "fallback_used": fallback_used,
            },
            "trace": trace_payload,
        }
        if args.include_latency:
            result_payload["elapsed_ms"] = elapsed_ms
        results.append(result_payload)
    payload = {
        "metadata": {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "spacy_available": available,
            "spacy_availability_reason": availability_reason,
            "manifest_hashes": manifest_hashes(),
            "case_count": len(cases),
            "fallback_count": fallback_count,
            "fallback_rate": fallback_count / len(cases) if cases else 0,
        },
        "results": results,
    }
    if args.include_latency:
        payload["metadata"]["total_elapsed_ms"] = round((time.perf_counter() - start_all) * 1000, 3)
    if args.write:
        write_json(OUTPUT_PATH, payload)
        print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
