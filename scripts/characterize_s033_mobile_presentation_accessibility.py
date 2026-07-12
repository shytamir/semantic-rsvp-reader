from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = REPO_ROOT / "static" / "css" / "app.css"
TEMPLATE_PATH = REPO_ROOT / "templates" / "index.html"
OUTPUT_PATH = (
    REPO_ROOT
    / "evaluation"
    / "mobile_presentation_accessibility"
    / "s033_characterization.json"
)

REQUIRED_INVARIANTS = {
    "visible_keyboard_focus": (
        (CSS_PATH, "button:focus-visible,"),
        (CSS_PATH, ".reader-area:focus-visible"),
        (CSS_PATH, "outline: 3px solid #2f73d8"),
        (TEMPLATE_PATH, 'id="reader-area" class="reader-area" tabindex="0"'),
    ),
    "safe_area_and_dynamic_viewport": (
        (CSS_PATH, "min-height: calc(100dvh - 24px)"),
        (CSS_PATH, "env(safe-area-inset-top)"),
        (CSS_PATH, "env(safe-area-inset-bottom)"),
    ),
    "stable_long_content_states": (
        (CSS_PATH, ".chunk-display.is-long-chunk"),
        (CSS_PATH, ".chunk-display.is-extra-long-token"),
        (CSS_PATH, "font-size: var(--reader-chunk-font-size)"),
    ),
    "ghost_and_structure_are_subordinate": (
        (CSS_PATH, ".previous-chunk"),
        (CSS_PATH, "opacity: 0.45"),
        (CSS_PATH, "text-overflow: ellipsis"),
        (CSS_PATH, ".reader-mode:has(.structure-anchor:not(.is-hidden)) .reader-area"),
    ),
    "semantic_state_cues": (
        (CSS_PATH, ".chunk-display.state-quote"),
        (CSS_PATH, ".chunk-display.state-parenthetical"),
    ),
    "reachable_controls_and_bounded_overlays": (
        (CSS_PATH, "grid-template-columns: repeat(4, minmax(0, 1fr))"),
        (CSS_PATH, ".speed-overlay"),
        (CSS_PATH, ".defect-panel"),
        (TEMPLATE_PATH, 'role="dialog" aria-modal="false"'),
        (TEMPLATE_PATH, 'aria-label="Reader controls"'),
    ),
}


def build_report(overrides: dict[Path, str] | None = None) -> dict:
    overrides = overrides or {}
    sources = {
        path: overrides.get(path, path.read_text(encoding="utf-8"))
        for path in (CSS_PATH, TEMPLATE_PATH)
    }
    invariants = []
    hard_failures = []
    for invariant, requirements in REQUIRED_INVARIANTS.items():
        passed = all(fragment in sources[path] for path, fragment in requirements)
        invariants.append({"id": invariant, "passed": passed})
        if not passed:
            hard_failures.append(f"missing_invariant:{invariant}")

    return {
        "slice": "S-033",
        "method": "static_shell_characterization_with_fixed_human_viewport_matrix",
        "sources": {
            str(path.relative_to(REPO_ROOT)).replace("\\", "/"): hashlib.sha256(
                text.encode("utf-8")
            ).hexdigest()
            for path, text in sources.items()
        },
        "invariants": invariants,
        "viewport_content_matrix": [
            {"id": "phone_portrait_ordinary", "content": "general_long_form", "state": "reader_and_controls"},
            {"id": "phone_landscape_structural", "content": "s032_structural_stream", "state": "ghost_structure_and_controls"},
            {"id": "narrow_long_token", "content": "dev-width-0006", "state": "long_content_classes"},
            {"id": "wide_ordinary", "content": "general_long_form", "state": "reader_hierarchy"},
            {"id": "speed_overlay", "content": "general_long_form", "state": "speed_controls"},
            {"id": "report_overlay", "content": "general_long_form", "state": "defect_form_and_context"},
            {"id": "semantic_cues", "content": "dev-quote-0007_and_dev-parenthetical-0008", "state": "quote_and_parenthetical"},
            {"id": "keyboard_focus", "content": "general_long_form", "state": "focus_order_and_visibility"},
        ],
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
            print("S-033 characterization does not match the committed record.")
            return 1
        if report["hard_failures"]:
            print(f"S-033 hard failures: {report['hard_failures']}")
            return 1
        print("S-033 presentation/accessibility characterization is reproducible and invariants pass.")
    if not args.write and not args.check:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
