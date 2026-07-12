from __future__ import annotations

import argparse
import io
import json
import logging
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.web import create_app


OUTPUT_PATH = REPO_ROOT / "evaluation" / "service_surfaces" / "s035_characterization.json"
CORE_REQUIREMENTS = REPO_ROOT / "requirements-core.txt"
PARSER_REQUIREMENTS = REPO_ROOT / "requirements-nlp-spike.txt"
ADAPTER_SOURCE = REPO_ROOT / "semantic_rsvp" / "experiments" / "parser_assisted_chunking" / "spacy_adapter.py"


def _endpoint_matrix() -> list[dict]:
    with tempfile.TemporaryDirectory(prefix="s035_services_") as directory:
        app = create_app(
            {
                "TESTING": True,
                "RSVP_CHUNKER_MODE": "rule_based",
                "DEFECT_REPORT_DIR": Path(directory) / "reports",
            }
        )
        client = app.test_client()
        requests = (
            ("health", client.get("/health")),
            ("validation_samples", client.get("/api/validation-samples")),
            ("ingest", client.post("/api/ingest", json={"text": "First sentence. Second sentence."})),
            ("chunk", client.post("/api/chunk", json={"sentence": "The reader preserves context."})),
            ("schedule", client.post("/api/schedule", json={"text": "The reader preserves context."})),
            ("bounded_defect_rejection", client.post("/api/defects", json={"category": "bad_chunk_split"})),
        )
        return [
            {
                "surface": name,
                "status_code": response.status_code,
                "json_object": isinstance(response.get_json(), dict),
            }
            for name, response in requests
        ]


def _automatic_fallback() -> dict:
    source_text = "Private synthetic fallback sentence must not appear in logs."
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger = logging.getLogger("semantic_rsvp.chunking.selection")
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)
    try:
        with (
            patch("semantic_rsvp.chunking.selection.provider_availability", return_value=(False, "spacy_unavailable")),
            patch("semantic_rsvp.experiments.parser_assisted_chunking.chunker.availability", return_value=(False, "spacy_unavailable")),
        ):
            app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "parser_assisted"})
            health = app.test_client().get("/health").get_json()
            schedule = app.test_client().post("/api/schedule", json={"text": source_text})
    finally:
        logger.removeHandler(handler)
    log_text = stream.getvalue()
    return {
        "health_status": health["status"],
        "configured_mode": health["chunking"]["configured_mode"],
        "provider_available": health["chunking"]["provider_available"],
        "provider_reason": health["chunking"]["provider_reason"],
        "fallback": health["chunking"]["fallback"],
        "schedule_status_code": schedule.status_code,
        "schedule_has_chunks": bool(schedule.get_json().get("schedule")),
        "reason_category_logged": "reason_category=parser_unavailable" in log_text,
        "source_text_absent_from_log": source_text not in log_text,
    }


def build_report() -> dict:
    endpoints = _endpoint_matrix()
    fallback = _automatic_fallback()
    default_app = create_app({"TESTING": True})
    default_health = default_app.test_client().get("/health").get_json()["chunking"]
    core = CORE_REQUIREMENTS.read_text(encoding="utf-8")
    parser = PARSER_REQUIREMENTS.read_text(encoding="utf-8")
    adapter = ADAPTER_SOURCE.read_text(encoding="utf-8")
    dependency_contract = {
        "core_excludes_spacy": "spacy" not in core.lower() and "en-core-web-sm" not in core.lower(),
        "parser_pins_click_8_1_8": "click==8.1.8" in parser.lower(),
        "parser_pins_spacy_3_7_5": "spacy==3.7.5" in parser.lower(),
        "parser_pins_model_3_7_1": "en_core_web_sm-3.7.1" in parser,
        "adapter_has_no_download_call": "download(" not in adapter,
    }
    expected_statuses = {
        "health": 200,
        "validation_samples": 200,
        "ingest": 200,
        "chunk": 200,
        "schedule": 200,
        "bounded_defect_rejection": 400,
    }
    hard_failures = []
    if any(item["status_code"] != expected_statuses[item["surface"]] or not item["json_object"] for item in endpoints):
        hard_failures.append("service_surface_contract_failed")
    if (
        fallback["provider_available"] is not False
        or not fallback["schedule_has_chunks"]
        or not fallback["reason_category_logged"]
        or not fallback["source_text_absent_from_log"]
        or fallback["schedule_status_code"] != 200
    ):
        hard_failures.append("automatic_fallback_or_log_privacy_failed")
    if fallback["fallback"] != "rule_based" or fallback["provider_reason"] != "spacy_unavailable":
        hard_failures.append("fallback_state_reporting_failed")
    if not all(dependency_contract.values()):
        hard_failures.append("dependency_or_download_contract_failed")

    return {
        "slice": "S-035",
        "method": "deterministic_service_fallback_and_dependency_characterization",
        "default_state": {
            "configured_mode": default_health["configured_mode"],
            "fallback": default_health["fallback"],
            "provider": default_health["provider"],
        },
        "rule_based_endpoint_matrix": endpoints,
        "automatic_fallback": fallback,
        "dependency_contract": dependency_contract,
        "hard_failures": hard_failures,
        "stabilized_defects": [],
        "human_validation_required": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(serialized, encoding="utf-8")
        print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    if args.check:
        if not OUTPUT_PATH.is_file() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            print("S-035 characterization does not match the committed record.")
            return 1
        if report["hard_failures"]:
            print(f"S-035 hard failures: {report['hard_failures']}")
            return 1
        print("S-035 service/fallback characterization is reproducible and complete.")
    if not args.write and not args.check:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
