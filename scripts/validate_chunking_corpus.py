from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    from chunking_experiment_common import (
        BASELINE_OUTPUT_PATH,
        MANIFEST_HASH_PATH,
        REPO_ROOT,
        VISIBLE_CORPORA,
        load_cases,
        load_json,
        manifest_hashes,
        sha256_text,
    )
except ModuleNotFoundError:
    from scripts.chunking_experiment_common import (
        BASELINE_OUTPUT_PATH,
        MANIFEST_HASH_PATH,
        REPO_ROOT,
        VISIBLE_CORPORA,
        load_cases,
        load_json,
        manifest_hashes,
        sha256_text,
    )

sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.chunking.rules import tokenize
from semantic_rsvp.text.normalize import normalize_text


REQUIRED_FIELDS = {
    "case_id",
    "corpus",
    "text",
    "document_role",
    "language",
    "source_id",
    "provenance",
    "existing_project_defect",
    "normalization",
    "char_count",
    "related_refs",
    "licensing",
    "notes",
    "frozen",
}


def _case_location(case: dict[str, Any]) -> str:
    return f"{case.get('_manifest')}:{case.get('_line_number')}"


def validate_cases(cases: list[dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    seen_ids: set[str] = set()
    for case in cases:
        location = _case_location(case)
        missing = sorted(REQUIRED_FIELDS - set(case))
        if missing:
            failures.append(f"{location}: missing required fields: {', '.join(missing)}")
            continue

        case_id = case["case_id"]
        if case_id in seen_ids:
            failures.append(f"{location}: duplicate case_id {case_id}")
        seen_ids.add(case_id)

        if case["corpus"] not in VISIBLE_CORPORA:
            failures.append(f"{location}: unsupported corpus {case['corpus']}")
        if not case["case_id"].startswith(case["corpus"][:3]):
            failures.append(f"{location}: case_id should begin with corpus prefix")
        if not case["frozen"]:
            failures.append(f"{location}: committed visible cases must be frozen")
        if case["char_count"] != len(case["text"]):
            failures.append(
                f"{location}: char_count {case['char_count']} does not match text length {len(case['text'])}"
            )
        if not case["licensing"]:
            failures.append(f"{location}: licensing must be recorded")
        if not isinstance(case["related_refs"], list) or not isinstance(case["notes"], list):
            failures.append(f"{location}: related_refs and notes must be arrays")
        for ref in case.get("related_refs", []):
            if ref and not (REPO_ROOT / ref).exists():
                failures.append(f"{location}: related ref does not exist: {ref}")
    return failures


def validate_manifest_hashes() -> list[str]:
    if not MANIFEST_HASH_PATH.exists():
        return [f"missing manifest hash file: {MANIFEST_HASH_PATH.relative_to(REPO_ROOT)}"]
    expected = load_json(MANIFEST_HASH_PATH)
    actual = manifest_hashes()
    failures = []
    for corpus, digest in actual.items():
        if expected.get(corpus) != digest:
            failures.append(f"manifest hash mismatch for {corpus}")
    return failures


def _has_unsplittable_long_token(text: str, max_chars: int) -> bool:
    return any(len(token.strip(".,!?;:\"'()[]")) > max_chars for token in tokenize(text))


def validate_baseline(cases: list[dict[str, Any]]) -> list[str]:
    if not BASELINE_OUTPUT_PATH.exists():
        return [f"missing baseline output: {BASELINE_OUTPUT_PATH.relative_to(REPO_ROOT)}"]

    baseline = load_json(BASELINE_OUTPUT_PATH)
    failures: list[str] = []
    cases_by_id = {case["case_id"]: case for case in cases if "case_id" in case}
    baseline_cases = {case["case_id"]: case for case in baseline.get("cases", [])}

    missing = sorted(set(cases_by_id) - set(baseline_cases))
    extra = sorted(set(baseline_cases) - set(cases_by_id))
    if missing:
        failures.append(f"baseline missing cases: {', '.join(missing)}")
    if extra:
        failures.append(f"baseline has extra cases: {', '.join(extra)}")

    max_chars = baseline.get("metadata", {}).get("chunker_config", {}).get("max_chars", 32)
    for case_id, case in cases_by_id.items():
        baseline_case = baseline_cases.get(case_id)
        if not baseline_case:
            continue
        normalized = normalize_text(case["text"])
        if baseline_case.get("input_sha256") != sha256_text(normalized):
            failures.append(f"{case_id}: baseline input hash mismatch")
        for chunk in baseline_case.get("chunks", []):
            text = chunk.get("text", "")
            start = chunk.get("source_start")
            end = chunk.get("source_end")
            if start is None or end is None:
                failures.append(f"{case_id}: unsafe source alignment for chunk {chunk.get('index')}")
                continue
            if not (0 <= start <= end <= len(normalized)):
                failures.append(f"{case_id}: invalid source offsets for chunk {chunk.get('index')}")
            if normalized[start:end] != text:
                failures.append(f"{case_id}: chunk text does not match source offsets for chunk {chunk.get('index')}")
            if len(text) > max_chars and not _has_unsplittable_long_token(text, max_chars):
                failures.append(f"{case_id}: chunk exceeds max_chars without unsplittable-token exception: {text}")
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-baseline", action="store_true")
    args = parser.parse_args(argv)

    cases = load_cases()
    failures = validate_cases(cases)
    failures.extend(validate_manifest_hashes())
    if not args.skip_baseline:
        failures.extend(validate_baseline(cases))

    if failures:
        print("Chunking corpus validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Chunking corpus validation passed for {len(cases)} visible cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
