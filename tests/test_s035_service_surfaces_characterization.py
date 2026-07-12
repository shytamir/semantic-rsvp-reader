import json

from scripts.characterize_s035_service_surfaces import OUTPUT_PATH, build_report


def test_s035_service_characterization_is_complete_and_reproducible():
    report = build_report()

    assert report["hard_failures"] == []
    assert report["default_state"]["configured_mode"] == "parser_assisted"
    assert report["default_state"]["fallback"] == "rule_based"
    assert report["automatic_fallback"]["schedule_has_chunks"] is True
    assert report["automatic_fallback"]["source_text_absent_from_log"] is True
    assert all(report["dependency_contract"].values())
    assert report["stabilized_defects"] == []
    assert json.loads(OUTPUT_PATH.read_text(encoding="utf-8")) == report
