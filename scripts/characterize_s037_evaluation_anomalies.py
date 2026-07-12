from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.chunking_experiment_common import load_cases, manifest_hashes
from scripts.run_s024_comparison import hard_compliance, run_rule_based


S024_RESULT = ROOT / "evaluation/parser_assisted_chunking/results/s024_objective_comparison.json"
IMPLEMENTATION_FREEZE = ROOT / "evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json"
INTEGRATION_RECORD = ROOT / "evaluation/parser_assisted_chunking/freeze/provisional_integration_record.json"
OUTPUT = ROOT / "evaluation/evaluation_anomaly_policy/s037_characterization.json"
SYSTEMS = ("rule_based", "parser_assisted")
METRICS = (
    "forbidden",
    "protected_spans",
    "required",
    "required_structural",
    "preferred",
    "acceptable",
)


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _case_by_id(payload: dict[str, Any], corpus: str, case_id: str) -> dict[str, Any]:
    return next(case for case in payload["cases"][corpus] if case["case_id"] == case_id)


def _zero_annotation_coverage(payload: dict[str, Any], corpus: str) -> dict[str, Any]:
    cases = payload["cases"][corpus]
    denominators = {
        system: {
            metric: sum(case[system]["annotation"][metric]["denominator"] for case in cases)
            for metric in METRICS
        }
        for system in SYSTEMS
    }
    return {
        "corpus": corpus,
        "case_count": len(cases),
        "case_ids": [case["case_id"] for case in cases],
        "denominators": denominators,
        "annotation_validation_failure_count": sum(bool(case["annotation_validation_failures"]) for case in cases),
        "classification": "annotation_or_denominator_coverage",
        "finding": "visible cases were evaluated for distribution and hard compliance without annotations; zero denominators are not zero observed violations",
    }


def build_report() -> dict[str, Any]:
    payload = _load(S024_RESULT)
    freeze = _load(IMPLEMENTATION_FREEZE)
    integration = _load(INTEGRATION_RECORD)
    blind = payload["cases"]["blind"]
    blind_mapping = _case_by_id(payload, "blind", "blind-0004")
    blind_coverage = _case_by_id(payload, "blind", "blind-0011")
    visible = load_cases()
    quote_case = next(case for case in visible if case["case_id"] == "dev-quote-0007")
    quote_hard = hard_compliance(quote_case["text"], run_rule_based(quote_case["text"]))

    current_hashes = manifest_hashes()
    recorded_hashes = payload["metadata"]["manifest_hashes"]
    freeze_hashes = {
        name: freeze["visible_corpus"][f"{name}_manifest_sha256"]
        for name in ("development", "generalization", "regression")
    }
    blind_ids = [case["case_id"] for case in blind]
    blind_hashes = [case["source_sha256"] for case in blind]

    historical_rule_summary = payload["summaries"]["blind"]["rule_based"]
    blind_0004_parser = blind_mapping["parser_assisted"]["annotation"]
    denominator_deltas = {
        metric: (
            payload["summaries"]["blind"]["parser_assisted"]["annotation_metrics"][metric]["denominator"]
            - historical_rule_summary["annotation_metrics"][metric]["denominator"]
        )
        for metric in (*METRICS, "complete_segmentation_match")
    }

    return {
        "schema_version": 1,
        "slice": "S-037",
        "source_evidence": {
            "s024_result": str(S024_RESULT.relative_to(ROOT)).replace("\\", "/"),
            "s024_result_sha256": _sha256(S024_RESULT),
            "implementation_freeze": str(IMPLEMENTATION_FREEZE.relative_to(ROOT)).replace("\\", "/"),
            "implementation_freeze_sha256": _sha256(IMPLEMENTATION_FREEZE),
            "integration_record": str(INTEGRATION_RECORD.relative_to(ROOT)).replace("\\", "/"),
            "integration_record_sha256": _sha256(INTEGRATION_RECORD),
            "private_ab_identity_required": False,
        },
        "identity_and_provenance": {
            "blind_case_count": len(blind_ids),
            "blind_case_ids_unique": len(blind_ids) == len(set(blind_ids)),
            "blind_source_hashes_unique": len(blind_hashes) == len(set(blind_hashes)),
            "blind_case_ids": blind_ids,
            "blind_annotation_validation_failure_count": sum(bool(case["annotation_validation_failures"]) for case in blind),
            "visible_manifest_hashes_match_result": current_hashes == recorded_hashes,
            "visible_manifest_hashes_match_freeze": current_hashes == freeze_hashes,
            "implementation_commit_matches_freeze": payload["metadata"]["implementation_commit"] == freeze["implementation_commit"],
            "config_hash_matches_freeze": payload["metadata"]["config_hash"] == freeze["scoring_configuration"]["hash"],
        },
        "anomalies": [
            _zero_annotation_coverage(payload, "regression"),
            _zero_annotation_coverage(payload, "generalization"),
            {
                "case_id": "blind-0004",
                "source_sha256": blind_mapping["source_sha256"],
                "classification": "source_to_chunk_mapping_failure",
                "scope": "historical_evaluation_runner_behavior",
                "historical_rule_based_hard": blind_mapping["rule_based"]["hard"],
                "parser_assisted_hard": blind_mapping["parser_assisted"]["hard"],
                "finding": "rule-based output was unscorable because chunk-to-source mapping failed; source coverage, dropped text, and ordering cannot be inferred from that failure",
            },
            {
                "case_id": "blind-0011",
                "source_sha256": blind_coverage["source_sha256"],
                "classification": "product_behavior_observed_in_historical_run",
                "scope": "historical_rule_based_output",
                "historical_rule_based_hard": blind_coverage["rule_based"]["hard"],
                "parser_assisted_hard": blind_coverage["parser_assisted"]["hard"],
                "finding": "mapping succeeded but non-whitespace source coverage differed; this is a distinct historical rule-based coverage failure, bounded without private source reconstruction",
            },
            {
                "classification": "reporting_only_anomaly",
                "scope": "historical_blind_summary",
                "historical_hard_compliance": historical_rule_summary["hard_compliance"],
                "defensible_classification": {
                    "confirmed_source_coverage_failure": 1,
                    "confirmed_dropped_text": 1,
                    "confirmed_source_ordering_failure": 0,
                    "unsafe_mapping_failure": 1,
                    "unscorable_cases": 1,
                },
                "finding": "the historical runner counted the blind-0004 mapping failure as three additional product failures; future runs no longer do so",
            },
            {
                "classification": "reporting_only_denominator_difference",
                "scope": "historical_blind_summary",
                "parser_minus_rule_denominator_deltas": denominator_deltas,
                "blind_0004_parser_denominators": {
                    metric: (
                        blind_0004_parser[metric]["denominator"]
                        if metric != "complete_segmentation_match"
                        else blind_0004_parser["complete_segmentation_denominator"]
                    )
                    for metric in (*METRICS, "complete_segmentation_match")
                },
                "finding": "system denominators differ only because blind-0004 rule-based annotations were correctly removed after mapping became unscorable",
            },
            {
                "classification": "annotation_or_denominator_coverage",
                "scope": "historical_blind_required_boundaries",
                "required_denominator": {
                    system: payload["summaries"]["blind"][system]["annotation_metrics"]["required"]["denominator"]
                    for system in SYSTEMS
                },
                "required_structural_denominator": {
                    system: payload["summaries"]["blind"][system]["annotation_metrics"]["required_structural"]["denominator"]
                    for system in SYSTEMS
                },
                "finding": "the blind annotations contain no generic required boundaries; required-structural boundaries are separately covered and must not be reported as required-boundary recall",
            },
            {
                "case_id": "dev-quote-0007",
                "source_sha256": hashlib.sha256(quote_case["text"].encode("utf-8")).hexdigest(),
                "classification": "product_behavior_public_analogue",
                "scope": "current_explicit_rule_based_operation",
                "current_rule_based_hard": quote_hard,
                "finding": "a repository-owned curly-quote case reproduces rule-based source-character loss without a mapping failure; it bounds the historical blind-0011 class but does not identify private source",
            },
        ],
        "plumbing_repair": {
            "file": "scripts/run_s024_comparison.py",
            "behavior": "mapping failures remain unsafe and unscorable but no longer assert dropped text, source-coverage failure, or source-ordering failure",
            "historical_artifacts_modified": False,
        },
        "operating_policy_evidence": {
            "current_default": integration["provisional_integration"]["default_mode"],
            "explicit_baseline_mode": integration["provisional_integration"]["explicit_baseline_mode"],
            "mandatory_fallback": integration["provisional_integration"]["fallback_implementation"],
            "optimizer_behavior_unchanged": integration["provisional_integration"]["optimizer_behavior_unchanged"],
            "runtime_model_downloads": integration["provisional_integration"]["runtime_model_downloads"],
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(text, encoding="utf-8")
        print(f"Wrote {OUTPUT.relative_to(ROOT)}")
        return 0
    if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
        print("S-037 characterization differs from the committed record.")
        return 1
    print("S-037 evaluation anomaly characterization is reproducible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
