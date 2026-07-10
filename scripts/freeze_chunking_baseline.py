from __future__ import annotations

import argparse
import difflib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path
from typing import Any

try:
    from chunking_experiment_common import (
        BASELINE_OUTPUT_PATH,
        MANIFEST_HASH_PATH,
        REPO_ROOT,
        load_cases,
        load_json,
        manifest_hashes,
        sha256_text,
        write_json,
    )
except ModuleNotFoundError:
    from scripts.chunking_experiment_common import (
        BASELINE_OUTPUT_PATH,
        MANIFEST_HASH_PATH,
        REPO_ROOT,
        load_cases,
        load_json,
        manifest_hashes,
        sha256_text,
        write_json,
    )

sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.models import TimingConfig
from semantic_rsvp.timing.schedule import schedule_text


BASELINE_COMMIT = "8b50a3049bb5d92a304a03527385c519194ce8da"


def _dependency_versions() -> dict[str, str | None]:
    versions: dict[str, str | None] = {}
    for package in ("Flask", "pytest"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    return versions


def _find_source_offsets(normalized_text: str, chunk_texts: list[str]) -> list[tuple[int | None, int | None]]:
    offsets: list[tuple[int | None, int | None]] = []
    cursor = 0
    for chunk_text in chunk_texts:
        start = normalized_text.find(chunk_text, cursor)
        if start == -1:
            offsets.append((None, None))
            continue
        end = start + len(chunk_text)
        offsets.append((start, end))
        cursor = end
    return offsets


def _display_state_payload(display_state: Any) -> dict[str, Any]:
    return {
        "in_quote": display_state.in_quote,
        "quote_boundary": display_state.quote_boundary,
        "in_parenthetical": display_state.in_parenthetical,
        "parenthetical_depth": display_state.parenthetical_depth,
    }


def _navigation_payload(navigation: Any) -> dict[str, Any]:
    return {
        "char_start": navigation.char_start,
        "char_end": navigation.char_end,
        "char_count_total": navigation.char_count_total,
        "progress_ratio": navigation.progress_ratio,
        "progress_percent": navigation.progress_percent,
        "paragraph_index": navigation.paragraph_index,
        "is_paragraph_start": navigation.is_paragraph_start,
        "is_paragraph_end": navigation.is_paragraph_end,
        "is_progress_milestone": navigation.is_progress_milestone,
    }


def _structure_payload(structure: Any) -> dict[str, Any]:
    return {
        "active_h1": structure.active_h1,
        "active_h2": structure.active_h2,
        "active_label": structure.active_label,
        "active_path": list(structure.active_path),
        "is_header_chunk": structure.is_header_chunk,
        "header_level": structure.header_level,
    }


def build_baseline_payload() -> dict[str, Any]:
    cases = load_cases()
    hashes = manifest_hashes()
    timing_config = TimingConfig()
    chunker = RuleBasedChunker()

    payload_cases = []
    for case in cases:
        normalized = normalize_text(case["text"])
        sentences = split_sentences(normalized)
        schedule = schedule_text(case["text"])
        chunk_texts = [scheduled.chunk.text for scheduled in schedule]
        offsets = _find_source_offsets(normalized, chunk_texts)
        payload_cases.append(
            {
                "case_id": case["case_id"],
                "corpus": case["corpus"],
                "input_sha256": sha256_text(normalized),
                "normalized_text": normalized,
                "sentence_count": len(sentences),
                "sentences": sentences,
                "chunks": [
                    {
                        "index": scheduled.index,
                        "sentence_index": scheduled.sentence_index,
                        "text": scheduled.chunk.text,
                        "source_start": offsets[index][0],
                        "source_end": offsets[index][1],
                        "char_length": scheduled.chunk.char_length,
                        "content_word_count": scheduled.chunk.content_word_count,
                        "syntactic_hint": scheduled.chunk.syntactic_hint,
                        "duration_ms": scheduled.duration_ms,
                        "display_state": _display_state_payload(scheduled.display_state),
                        "navigation": _navigation_payload(scheduled.navigation),
                        "structure": _structure_payload(scheduled.structure),
                    }
                    for index, scheduled in enumerate(schedule)
                ],
            }
        )

    return {
        "metadata": {
            "baseline_commit": BASELINE_COMMIT,
            "python_version": platform.python_version(),
            "dependency_versions": _dependency_versions(),
            "chunker_entry_point": "semantic_rsvp.chunking.rules.RuleBasedChunker",
            "normalization_entry_point": "semantic_rsvp.text.normalize.normalize_text",
            "segmentation_entry_point": "semantic_rsvp.text.segment.split_sentences",
            "schedule_entry_point": "semantic_rsvp.timing.schedule.schedule_text",
            "chunker_config": {
                "max_chars": chunker.max_chars,
                "max_content_words": chunker.max_content_words,
            },
            "timing_config": {
                "base_beat_ms": timing_config.base_beat_ms,
                "min_duration_ms": timing_config.min_duration_ms,
                "max_duration_ms": timing_config.max_duration_ms,
                "sentence_pause_ms": timing_config.sentence_pause_ms,
            },
            "manifest_hashes": hashes,
            "fallback_behavior": "schedule_text uses RuleBasedChunker() when no chunker is supplied.",
        },
        "cases": payload_cases,
    }


def ensure_manifest_hashes(write_hashes: bool) -> None:
    actual = manifest_hashes()
    if write_hashes:
        write_json(MANIFEST_HASH_PATH, actual)
        return
    if not MANIFEST_HASH_PATH.exists():
        raise SystemExit("Manifest hash file is missing. Run with --write-hashes after reviewing manifests.")
    expected = load_json(MANIFEST_HASH_PATH)
    if expected != actual:
        raise SystemExit("Manifest hash mismatch. Review corpus changes before regenerating baseline artifacts.")


def check_reproducible(payload: dict[str, Any]) -> int:
    if not BASELINE_OUTPUT_PATH.exists():
        print(f"Missing baseline output: {BASELINE_OUTPUT_PATH.relative_to(REPO_ROOT)}")
        return 1
    expected = json.dumps(load_json(BASELINE_OUTPUT_PATH), indent=2, sort_keys=True) + "\n"
    actual = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if expected == actual:
        print("Rule-based baseline output is reproducible.")
        return 0
    diff = difflib.unified_diff(
        expected.splitlines(),
        actual.splitlines(),
        fromfile=str(BASELINE_OUTPUT_PATH.relative_to(REPO_ROOT)),
        tofile="regenerated-baseline",
        lineterm="",
    )
    print("Rule-based baseline output changed:")
    for line in diff:
        print(line)
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write baseline output.")
    parser.add_argument("--check", action="store_true", help="Compare regenerated output to the committed baseline.")
    parser.add_argument("--write-hashes", action="store_true", help="Write manifest hashes before generating output.")
    args = parser.parse_args(argv)

    if not args.write and not args.check:
        args.check = True

    ensure_manifest_hashes(args.write_hashes)
    payload = build_baseline_payload()

    if args.write:
        write_json(BASELINE_OUTPUT_PATH, payload)
        print(f"Wrote {BASELINE_OUTPUT_PATH.relative_to(REPO_ROOT)}")
    if args.check:
        return check_reproducible(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
