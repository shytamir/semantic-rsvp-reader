from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = REPO_ROOT / "static" / "js" / "app.js"
OUTPUT_PATH = REPO_ROOT / "evaluation" / "playback_adaptation" / "s031_characterization.json"

REQUIRED_INVARIANTS = {
    "single_playback_timer_replaced_before_schedule": (
        "function scheduleNextChunk() {\n  clearPlaybackTimer();",
        "timerId = window.setTimeout(",
    ),
    "pause_cancels_timer": (
        "function stopPlayback({ render = true } = {}) {\n  isPlaying = false;\n  clearPlaybackTimer();",
    ),
    "completion_cancels_timer_and_is_recorded_once": (
        "function renderCompletion() {\n  clearPlaybackTimer();",
        "if (completionRecorded) {\n    return;\n  }",
        'recordSessionEvent("playback_completed");',
    ),
    "hidden_page_pauses_without_auto_resume": (
        'document.addEventListener("visibilitychange", handleVisibilityChange);',
        'recordSessionEvent("page_hidden_pause");\n  pause({ record: false });',
    ),
    "manual_speed_change_is_bounded_and_suppresses_adaptation": (
        "speedIndex = Math.min(Math.max(nextIndex, 0), SPEED_LEVELS.length - 1);",
        "resetAdaptationWindow();",
        "adaptationSuppressedUntilEventCount = sessionEvents.length + 3;",
    ),
    "new_schedule_resets_speed_session_and_adaptation": (
        "resetSpeed({ record: false });\n    resetSessionEvents();\n    resetAdaptationState();",
    ),
    "progress_seek_pauses_and_suppresses_adaptation": (
        'cancelPendingDriftRecovery("progress_seek");',
        "pause({ record: false, render: false });",
        "adaptationSuppressedUntilEventCount = sessionEvents.length + 3;\n  resetAdaptationWindow();",
    ),
    "adaptation_is_session_only_and_conservative": (
        "const ADAPTATION_REWIND_THRESHOLD = 2;",
        "const ADAPTATION_PAUSE_THRESHOLD = 3;",
        "const ADAPTATION_SMOOTH_CHUNK_THRESHOLD = 12;",
        "if (!adaptationEnabled) {\n    return;\n  }",
    ),
    "session_summary_is_observable": (
        "function getSessionSummary() {",
        "event_count: sessionEvents.length,",
        'adaptation_count: countSessionEvents("adaptation_applied"),',
        "current_speed: playbackSpeed,",
        "current_index: currentIndex,",
    ),
}


def build_report(source_text: str | None = None) -> dict:
    source = SOURCE_PATH.read_text(encoding="utf-8") if source_text is None else source_text
    speed_match = re.search(r"const SPEED_LEVELS = \[([^]]+)\];", source)
    speed_levels = (
        [float(value.strip()) for value in speed_match.group(1).split(",")]
        if speed_match
        else []
    )
    invariants = []
    hard_failures = []
    for invariant, fragments in REQUIRED_INVARIANTS.items():
        passed = all(fragment in source for fragment in fragments)
        invariants.append({"id": invariant, "passed": passed})
        if not passed:
            hard_failures.append(f"missing_invariant:{invariant}")
    if speed_levels != [0.75, 0.85, 1.0, 1.15, 1.3, 1.5]:
        hard_failures.append("speed_levels_changed")

    return {
        "slice": "S-031",
        "method": "static_source_characterization",
        "source": "static/js/app.js",
        "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "speed_levels": speed_levels,
        "default_speed": speed_levels[2] if len(speed_levels) > 2 else None,
        "adaptation_thresholds": {
            "minimum_events": 3,
            "rewinds_for_slower_step": 2,
            "pauses_for_slower_step": 3,
            "smooth_chunks_for_faster_step": 12,
            "manual_or_seek_suppression_events": 3,
        },
        "characterized_behavior": [
            "play_pause_resume_uses_one_replaceable_timeout",
            "manual_navigation_and_reset_pause_playback",
            "automatic_completion_cancels_the_timer_and_records_once",
            "backgrounding_pauses_and_foregrounding_does_not_auto_resume",
            "speed_changes_are_bounded_and_reschedule_the_current_chunk_when_playing",
            "new_text_resets_speed_session_events_and_adaptation_state",
            "adaptation_can_be_disabled_or_reset_and_is_not_persisted",
            "rewinds_or_pauses_can_slow_by_one_step_and_a_smooth_run_can_speed_by_one_step",
            "manual_speed_changes_and_progress_seeking_suppress_immediate_adaptation",
            "session_summary_exposes_counts_completion_speed_and_adaptation_state",
        ],
        "invariants": invariants,
        "hard_failures": hard_failures,
        "runtime_changes": [],
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
            print("S-031 characterization does not match the committed record.")
            return 1
        if report["hard_failures"]:
            print(f"S-031 hard failures: {report['hard_failures']}")
            return 1
        print("S-031 playback/adaptation characterization is reproducible and invariants pass.")
    if not args.write and not args.check:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
