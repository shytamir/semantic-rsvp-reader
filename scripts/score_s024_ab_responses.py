from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    from chunking_experiment_common import EXPERIMENT_ROOT, REPO_ROOT, write_json
except ModuleNotFoundError:
    from scripts.chunking_experiment_common import EXPERIMENT_ROOT, REPO_ROOT, write_json


REDACTED_SCORE_PATH = EXPERIMENT_ROOT / "results" / "s024_human_ab_preference.json"
MARKDOWN_REPORT_PATH = REPO_ROOT / "docs" / "validation" / "s024_human_ab_preference_summary.md"
ALLOWED_CHOICES = {"A", "B", "equivalent", "both poor"}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}


def load_response_data(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        normalized = re.sub(
            r':\s*(A|B|equivalent|both poor|low|medium|high)(\s*[,}\n])',
            lambda match: f': "{match.group(1)}"{match.group(2)}',
            text,
        )
        return json.loads(normalized)


def score_responses(response: dict[str, Any], identity_key: dict[str, Any]) -> dict[str, Any]:
    assignments = identity_key["assignments"]
    choice_counts: Counter[str] = Counter()
    confidence_counts: Counter[str] = Counter()
    system_preference_counts: Counter[str] = Counter()
    system_confidence_counts: dict[str, Counter[str]] = defaultdict(Counter)
    notes_count = 0
    invalid: list[dict[str, str]] = []

    for entry in response.get("cases", []):
        case_id = entry.get("case_id")
        choice = entry.get("choice")
        confidence = entry.get("confidence")
        note = entry.get("note", "")
        if case_id not in assignments:
            invalid.append({"case_id": str(case_id), "reason": "missing_identity_assignment"})
            continue
        if choice not in ALLOWED_CHOICES:
            invalid.append({"case_id": str(case_id), "reason": f"invalid_choice:{choice}"})
            continue
        if confidence not in ALLOWED_CONFIDENCE:
            invalid.append({"case_id": str(case_id), "reason": f"invalid_confidence:{confidence}"})
            continue
        choice_counts[choice] += 1
        confidence_counts[confidence] += 1
        if note:
            notes_count += 1
        if choice in {"A", "B"}:
            system = assignments[case_id][choice]
            system_preference_counts[system] += 1
            system_confidence_counts[system][confidence] += 1
        else:
            system_preference_counts[choice.replace(" ", "_")] += 1

    decisive = system_preference_counts["rule_based"] + system_preference_counts["parser_assisted"]
    return {
        "case_count": len(response.get("cases", [])),
        "valid_response_count": len(response.get("cases", [])) - len(invalid),
        "invalid_responses": invalid,
        "raw_choice_counts": dict(sorted(choice_counts.items())),
        "confidence_counts": dict(sorted(confidence_counts.items())),
        "notes_count": notes_count,
        "system_preference_counts": {
            "rule_based": system_preference_counts["rule_based"],
            "parser_assisted": system_preference_counts["parser_assisted"],
            "equivalent": system_preference_counts["equivalent"],
            "both_poor": system_preference_counts["both_poor"],
        },
        "decisive_preference_counts": {
            "denominator": decisive,
            "rule_based": system_preference_counts["rule_based"],
            "parser_assisted": system_preference_counts["parser_assisted"],
        },
        "system_confidence_counts": {
            "rule_based": dict(sorted(system_confidence_counts["rule_based"].items())),
            "parser_assisted": dict(sorted(system_confidence_counts["parser_assisted"].items())),
        },
        "identity_key_committed": False,
        "per_case_system_mapping_committed": False,
    }


def build_markdown_report(score: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# S-024 Human A/B Preference Summary",
            "",
            "This repository-safe summary contains aggregate scoring only. It does not include the A/B identity key or per-case system mappings.",
            "",
            "## Response Status",
            "",
            f"- Cases in response file: {score['case_count']}",
            f"- Valid responses scored: {score['valid_response_count']}",
            f"- Invalid responses: {len(score['invalid_responses'])}",
            f"- Notes supplied: {score['notes_count']}",
            "",
            "## Aggregate Preferences",
            "",
            f"- Rule-based preferred: {score['system_preference_counts']['rule_based']}",
            f"- Parser-assisted preferred: {score['system_preference_counts']['parser_assisted']}",
            f"- Equivalent: {score['system_preference_counts']['equivalent']}",
            f"- Both poor: {score['system_preference_counts']['both_poor']}",
            "",
            "## Decisive Preferences",
            "",
            f"- Denominator: {score['decisive_preference_counts']['denominator']}",
            f"- Rule-based: {score['decisive_preference_counts']['rule_based']}",
            f"- Parser-assisted: {score['decisive_preference_counts']['parser_assisted']}",
            "",
            "## Confidence",
            "",
            f"- Overall confidence counts: {score['confidence_counts']}",
            f"- Rule-based confidence counts: {score['system_confidence_counts']['rule_based']}",
            f"- Parser-assisted confidence counts: {score['system_confidence_counts']['parser_assisted']}",
            "",
            "## Interpretation Boundary",
            "",
            "This completes the human A/B scoring evidence for S-024, but it does not by itself promote the parser-assisted system. Any product disposition remains an S-025 decision.",
            "",
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--responses", required=True, type=Path)
    parser.add_argument("--identity-key", required=True, type=Path)
    parser.add_argument("--write-redacted-results", action="store_true")
    args = parser.parse_args(argv)

    response = load_response_data(args.responses)
    identity_key = json.loads(args.identity_key.read_text(encoding="utf-8"))
    score = score_responses(response, identity_key)
    if args.write_redacted_results:
        write_json(REDACTED_SCORE_PATH, score)
        MARKDOWN_REPORT_PATH.write_text(build_markdown_report(score), encoding="utf-8")
        print(f"Wrote {REDACTED_SCORE_PATH.relative_to(REPO_ROOT)}")
        print(f"Wrote {MARKDOWN_REPORT_PATH.relative_to(REPO_ROOT)}")
    else:
        print(json.dumps(score, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
