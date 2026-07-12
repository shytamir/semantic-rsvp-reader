import json

from scripts.characterize_s034_evidence_capture import OUTPUT_PATH, build_report


def test_s034_synthetic_capture_and_review_are_reproducible():
    report = build_report()

    assert report["hard_failures"] == []
    assert report["synthetic_report_count"] == 4
    assert report["generated_reports_committed"] is False
    assert report["private_blind_material_used"] is False
    assert report["stabilized_defects"] == []
    assert all(capture["status_code"] == 200 for capture in report["captures"])
    assert all(capture["required_sections_present"] for capture in report["captures"])
    assert json.loads(OUTPUT_PATH.read_text(encoding="utf-8")) == report
