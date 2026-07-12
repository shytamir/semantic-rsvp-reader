import json

from scripts.characterize_s033_mobile_presentation_accessibility import (
    CSS_PATH,
    OUTPUT_PATH,
    TEMPLATE_PATH,
    build_report,
)


def test_presentation_characterization_is_complete_and_reproducible():
    report = build_report()

    assert report["hard_failures"] == []
    assert all(item["passed"] for item in report["invariants"])
    assert {item["id"] for item in report["viewport_content_matrix"]} == {
        "phone_portrait_ordinary",
        "phone_landscape_structural",
        "narrow_long_token",
        "wide_ordinary",
        "speed_overlay",
        "report_overlay",
        "semantic_cues",
        "keyboard_focus",
    }
    assert report["stabilized_defects"] == []
    assert report["human_validation_required"] is True
    assert json.loads(OUTPUT_PATH.read_text(encoding="utf-8")) == report


def test_missing_presentation_invariants_fail_loudly():
    report = build_report({CSS_PATH: "", TEMPLATE_PATH: ""})

    assert len(report["hard_failures"]) == len(report["invariants"])
    assert all(failure.startswith("missing_invariant:") for failure in report["hard_failures"])
