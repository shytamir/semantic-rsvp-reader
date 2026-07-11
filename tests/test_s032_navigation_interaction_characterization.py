import json

from scripts.characterize_s032_navigation_interaction import (
    ORDINARY_FIXTURE_PATH,
    OUTPUT_PATH,
    STRUCTURAL_FIXTURE_PATH,
    build_report,
)


def test_navigation_interaction_invariants_and_streams_are_reproducible():
    report = build_report()

    assert report["hard_failures"] == []
    assert all(item["passed"] for item in report["invariants"])
    ordinary = report["streams"]["ordinary"]
    structural = report["streams"]["structural"]
    assert ordinary["source_text"]
    assert [item["index"] for item in ordinary["schedule"]] == list(
        range(len(ordinary["schedule"]))
    )
    assert {item["active_label"] for item in structural["schedule"]} >= {
        "Main Route",
        "First Turn",
        "Second Turn",
    }
    assert {item["path"] for item in report["interaction_matrix"]} == {
        "ordinary_traversal",
        "breakpoints",
        "coarse_seek",
        "reset",
        "drift_recovery",
        "cancellation",
        "ghost_and_structure",
    }
    assert json.loads(OUTPUT_PATH.read_text(encoding="utf-8")) == report


def test_plain_text_fixtures_are_the_committed_stream_sources():
    report = build_report()

    for name, path in (
        ("ordinary", ORDINARY_FIXTURE_PATH),
        ("structural", STRUCTURAL_FIXTURE_PATH),
    ):
        assert path.is_file()
        assert path.read_text(encoding="utf-8").removesuffix("\n") == report["streams"][name]["source_text"]


def test_missing_direction_consistency_fails_loudly():
    report = build_report(source_text="const placeholder = true;")

    assert "missing_invariant:gesture_direction_consistency" in report["hard_failures"]
    assert len(report["hard_failures"]) > 1
