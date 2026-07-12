from __future__ import annotations

import argparse
import gzip
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.web import create_app


OUTPUT_PATH = REPO_ROOT / "evaluation" / "evidence_capture" / "s034_characterization.json"
CATEGORIES = (
    "bad_chunk_split",
    "rushed_dense_chunk",
    "gesture_interference",
    "layout_or_visibility_issue",
)
REQUIRED_SECTIONS = (
    "## Classification",
    "## Reader State",
    "## Timing Context",
    "## Structural Context",
    "## Navigability Context",
    "## Session Summary",
    "## Client",
)


def _payload(category: str) -> dict:
    return {
        "category": category,
        "severity": 2,
        "notes": "Synthetic bounded S-034 report <check>.",
        "preferred_behavior": "Preserve complete reviewable context.",
        "reader_state": {
            "current_index": 4,
            "sentence_index": 1,
            "current_chunk": "synthetic context",
            "current_duration_ms": 420,
            "base_duration_ms": 420,
            "effective_duration_ms": 420,
            "duration_source": "schedule",
            "current_syntactic_hint": "normal",
            "current_content_word_count": 2,
            "char_length": 17,
            "in_quote": False,
            "quote_boundary": "none",
            "in_parenthetical": False,
            "parenthetical_depth": 0,
            "navigation": {"progress_percent": 40, "paragraph_index": 1},
            "structure": {
                "active_h1": "Synthetic Evidence",
                "active_h2": "Review",
                "active_label": "Review",
                "active_path": ["Synthetic Evidence", "Review"],
                "is_header_chunk": False,
                "header_level": None,
            },
            "previous_displayed_chunk": {"index": 3, "text": "previous context"},
            "breakpoints": {"count": 1, "indices": [4], "current_is_breakpoint": True},
            "drift_recovery": {"active": False, "pending": False},
            "original_sentence": "This is synthetic project-owned evidence.",
            "previous_chunks": [{"index": 3, "text": "previous context", "duration_ms": 390}],
            "next_chunks": [{"index": 5, "text": "next context", "duration_ms": 440}],
            "playback_speed": 1.0,
            "adaptation_enabled": False,
            "session_summary": {
                "event_count": 8,
                "rewind_count": 1,
                "pause_count": 2,
                "speed_change_count": 0,
                "adaptation_count": 0,
                "completed": False,
                "elapsed_session_ms": 5000,
                "estimated_remaining_chunks": 6,
                "average_effective_duration_ms": 420,
            },
        },
        "client": {
            "user_agent": "S-034 synthetic characterization",
            "viewport_width": 390,
            "viewport_height": 844,
            "display_width_px": 366,
            "chunk_scroll_width_px": 320,
            "chunk_client_width_px": 320,
            "chunk_may_overflow": False,
            "layout_context": {
                "previous_chunk_visible": True,
                "previous_chunk_text_length": 16,
                "active_chunk_text_length": 17,
                "viewport_width": 390,
                "viewport_height": 844,
            },
        },
    }


def build_report() -> dict:
    with tempfile.TemporaryDirectory(prefix="s034_characterization_") as directory:
        report_dir = Path(directory) / "reports"
        app = create_app()
        app.config.update(TESTING=True, DEFECT_REPORT_DIR=report_dir)
        client = app.test_client()
        captures = []
        markdown_records = []
        for category in CATEGORIES:
            response = client.post("/api/defects", json=_payload(category))
            body = response.get_json()
            filename = body.get("filename", "") if isinstance(body, dict) else ""
            path = report_dir / filename
            markdown = gzip.open(path, "rt", encoding="utf-8").read() if path.is_file() else ""
            captures.append(
                {
                    "category": category,
                    "status_code": response.status_code,
                    "saved": body.get("status") == "saved" if isinstance(body, dict) else False,
                    "generated_filename": bool(re.fullmatch(r"defect_\d{8}_\d{6}_[0-9a-f]{6}\.md\.gz", filename)),
                    "gzip_readable": bool(markdown),
                    "required_sections_present": all(section in markdown for section in REQUIRED_SECTIONS),
                    "html_sensitive_text_escaped": "&lt;check&gt;" in markdown and "<check>" not in markdown,
                }
            )
            markdown_records.append(markdown)

        review = subprocess.run(
            [sys.executable, "scripts/review_defects.py", "--report-dir", str(report_dir)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        hard_failures = []
        if not all(all(value for key, value in capture.items() if key not in {"category", "status_code"}) and capture["status_code"] == 200 for capture in captures):
            hard_failures.append("synthetic_capture_or_context_incomplete")
        if review.returncode != 0 or "Included reports: 4" not in review.stdout:
            hard_failures.append("review_tool_did_not_read_all_synthetic_reports")

    return {
        "slice": "S-034",
        "method": "temporary_synthetic_capture_and_review_characterization",
        "synthetic_report_count": len(CATEGORIES),
        "categories": list(CATEGORIES),
        "captures": captures,
        "review_tool": {"returncode": review.returncode, "included_reports": 4 if "Included reports: 4" in review.stdout else None},
        "generated_reports_committed": False,
        "private_blind_material_used": False,
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
            print("S-034 characterization does not match the committed record.")
            return 1
        if report["hard_failures"]:
            print(f"S-034 hard failures: {report['hard_failures']}")
            return 1
        print("S-034 synthetic evidence capture is reproducible and complete.")
    if not args.write and not args.check:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
