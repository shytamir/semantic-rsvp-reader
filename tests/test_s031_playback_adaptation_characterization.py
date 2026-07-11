from scripts.characterize_s031_playback_adaptation import build_report


def test_shipped_playback_and_adaptation_invariants_are_present():
    report = build_report()

    assert report["hard_failures"] == []
    assert report["speed_levels"] == [0.75, 0.85, 1.0, 1.15, 1.3, 1.5]
    assert report["default_speed"] == 1.0
    assert all(item["passed"] for item in report["invariants"])
    assert report["runtime_changes"] == []


def test_missing_shipped_invariants_fail_loudly():
    report = build_report(source_text="const SPEED_LEVELS = [];")

    assert "speed_levels_changed" in report["hard_failures"]
    assert len(report["hard_failures"]) > 1
