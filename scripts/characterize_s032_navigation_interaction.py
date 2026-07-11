from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.timing.schedule import schedule_text


SOURCE_PATH = REPO_ROOT / "static" / "js" / "app.js"
OUTPUT_PATH = REPO_ROOT / "evaluation" / "navigation_interaction" / "s032_characterization.json"
ORDINARY_TEXT = (
    "First paragraph establishes the ordinary traversal path and gives the reader enough chunks to move in both directions.\n\n"
    "Second paragraph provides a coarse progress milestone and several useful breakpoint targets for deterministic validation.\n\n"
    "Third paragraph closes the stream so reset, end boundaries, and cancellation can be checked without changing timing policy."
)
STRUCTURAL_TEXT = (
    "# Main Route\n\nIntroductory navigation text.\n\n"
    "## First Turn\n\nThe first section supplies several chunks for a breakpoint and a recovery lead-in.\n\n"
    "## Second Turn\n\nThe second section confirms that structural orientation changes during traversal."
)
REQUIRED_INVARIANTS = {
    "gesture_direction_consistency": (
        'if (deltaX < 0) {\n      traverseBreakpointOrStep("previous");\n    } else {\n      traverseBreakpointOrStep("next");',
        'if (direction === "previous") {\n      previousChunk();\n    } else {\n      nextChunk();',
        'const targetIndex = direction === "next"\n    ? getNextBreakpointIndex()\n    : getPreviousBreakpointIndex();',
    ),
    "gesture_arbitration": (
        'readerArea.addEventListener("pointercancel", cancelGesture);',
        "if (longPressActivated) {",
        "if (isSwipe(deltaX, deltaY)) {",
        "handleReaderTap();",
    ),
    "coarse_seek_pauses_and_resolves_milestone": (
        'cancelPendingDriftRecovery("progress_seek");',
        "const nextIndex = getNearestProgressMilestoneIndex(targetPercent);",
        "pause({ record: false, render: false });",
        'recordSessionEvent("progress_seek", {',
    ),
    "breakpoint_toggle_and_ordered_traversal": (
        'recordSessionEvent("breakpoint_added", metadata);',
        'recordSessionEvent("breakpoint_removed", metadata);',
        ".sort((left, right) => left - right);",
        "startDriftRecoveryToBreakpoint(targetIndex, direction);",
    ),
    "ghost_context_tracks_current_index": (
        "const previousItem = getPreviousDisplayedScheduleItem();",
        "return schedule[clampIndex(currentIndex - 1)] || null;",
        "renderPreviousChunk();\n  updateStructureAnchor();",
    ),
    "drift_recovery_lead_in_resume_and_cancel": (
        "const DRIFT_RECOVERY_DELAY_MS = 500;",
        "const DRIFT_RECOVERY_LEAD_IN_CHUNKS = 3;",
        "driftRecoveryTimerId = window.setTimeout(\n    completeDriftRecovery,",
        'recordSessionEvent("drift_recovery_resumed", {',
        'recordSessionEvent("drift_recovery_cancelled", {',
    ),
    "reset_and_new_stream_boundaries": (
        "function resetReader() {",
        "currentIndex = 0;",
        "function resetNavigationScaffold() {",
        "clearBreakpoints();",
    ),
    "structural_orientation_tracks_schedule_metadata": (
        "function getCurrentStructureLabel() {",
        "structure.active_label",
        "showStructureAnchor(label);",
        "resetStructureAnchor();",
    ),
}


def _stream(text: str) -> list[dict]:
    schedule = schedule_text(text, chunker=RuleBasedChunker())
    return [
        {
            "index": item.index,
            "text": item.chunk.text,
            "paragraph_index": item.navigation.paragraph_index,
            "progress_percent": item.navigation.progress_percent,
            "is_progress_milestone": item.navigation.is_progress_milestone,
            "active_label": item.structure.active_label,
            "active_path": list(item.structure.active_path),
            "is_header_chunk": item.structure.is_header_chunk,
        }
        for item in schedule
    ]


def build_report(source_text: str | None = None) -> dict:
    source = SOURCE_PATH.read_text(encoding="utf-8") if source_text is None else source_text
    invariants = []
    hard_failures = []
    for invariant, fragments in REQUIRED_INVARIANTS.items():
        passed = all(fragment in source for fragment in fragments)
        invariants.append({"id": invariant, "passed": passed})
        if not passed:
            hard_failures.append(f"missing_invariant:{invariant}")
    cancellation_reasons = sorted(
        set(re.findall(r'cancelPendingDriftRecovery\("([a-z_]+)"\)', source))
    )
    ordinary = _stream(ORDINARY_TEXT)
    structural = _stream(STRUCTURAL_TEXT)
    if len(ordinary) < 8:
        hard_failures.append("ordinary_stream_too_short")
    if not any(item["is_progress_milestone"] for item in ordinary):
        hard_failures.append("ordinary_stream_has_no_milestone")
    if not {"Main Route", "First Turn", "Second Turn"}.issubset(
        {item["active_label"] for item in structural}
    ):
        hard_failures.append("structural_stream_missing_orientation_labels")

    return {
        "slice": "S-032",
        "method": "static_source_and_deterministic_stream_characterization",
        "source": "static/js/app.js",
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "gesture_thresholds": {
            "swipe_min_distance_px": 40,
            "swipe_max_vertical_drift_px": 60,
            "tap_max_distance_px": 12,
            "long_press_ms": 500,
            "double_tap_ms": 280,
        },
        "drift_recovery": {"delay_ms": 500, "lead_in_chunks": 3},
        "cancellation_reasons": cancellation_reasons,
        "invariants": invariants,
        "interaction_matrix": [
            {"path": "ordinary_traversal", "actions": ["tap", "swipe_left", "swipe_right", "hold_swipe"], "expected": "tap toggles playback; left moves to previous and right moves to next; hold-swipe moves five chunks"},
            {"path": "breakpoints", "actions": ["double_tap_toggle", "swipe_left", "swipe_right"], "expected": "toggle has no play side effect; swipe direction matches ordinary traversal and starts lead-in recovery"},
            {"path": "coarse_seek", "actions": ["tap_progress_anchor"], "expected": "pending recovery cancels, playback pauses, and the nearest milestone is selected"},
            {"path": "reset", "actions": ["reset", "load_new_stream"], "expected": "reset returns to index zero while same-stream breakpoints remain; loading new text clears navigation state"},
            {"path": "drift_recovery", "actions": ["breakpoint_traversal", "wait_500ms"], "expected": "three-chunk lead-in renders, then playback resumes through the target context"},
            {"path": "cancellation", "actions": ["start_recovery", "tap_or_control_before_delay"], "expected": "the pending timer clears, cancellation is recorded, and delayed playback does not resume"},
            {"path": "ghost_and_structure", "actions": ["ordinary", "seek", "breakpoint", "reset"], "expected": "ghost is index minus one and active H1/H2 label follows schedule metadata"},
        ],
        "streams": {
            "ordinary": {"source_text": ORDINARY_TEXT, "schedule": ordinary},
            "structural": {"source_text": STRUCTURAL_TEXT, "schedule": structural},
        },
        "hard_failures": hard_failures,
        "stabilized_defects": [
            {
                "id": "breakpoint_swipe_direction_mismatch",
                "before": "left/right swipes reversed direction only when breakpoints existed",
                "after": "ordinary and breakpoint traversal share left-previous and right-next semantics",
            }
        ],
        "presentation_findings_for_s033": [],
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
            print("S-032 characterization does not match the committed record.")
            return 1
        if report["hard_failures"]:
            print(f"S-032 hard failures: {report['hard_failures']}")
            return 1
        print("S-032 navigation/interaction characterization is reproducible and invariants pass.")
    if not args.write and not args.check:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
