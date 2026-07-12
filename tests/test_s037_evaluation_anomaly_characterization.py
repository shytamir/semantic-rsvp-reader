import json

from scripts.characterize_s037_evaluation_anomalies import OUTPUT, build_report


def test_s037_committed_characterization_is_reproducible():
    assert json.loads(OUTPUT.read_text(encoding="utf-8")) == build_report()


def test_s037_characterization_preserves_identity_and_classifies_anomalies():
    report = build_report()
    identities = report["identity_and_provenance"]

    assert identities["blind_case_count"] == 16
    assert identities["blind_case_ids_unique"] is True
    assert identities["blind_source_hashes_unique"] is True
    assert identities["blind_annotation_validation_failure_count"] == 0
    assert identities["visible_manifest_hashes_match_result"] is True
    assert identities["visible_manifest_hashes_match_freeze"] is True
    assert identities["implementation_commit_matches_freeze"] is True
    assert identities["config_hash_matches_freeze"] is True

    anomalies = report["anomalies"]
    mapping = next(item for item in anomalies if item.get("case_id") == "blind-0004")
    coverage = next(item for item in anomalies if item.get("case_id") == "blind-0011")
    analogue = next(item for item in anomalies if item.get("case_id") == "dev-quote-0007")

    assert mapping["classification"] == "source_to_chunk_mapping_failure"
    assert mapping["historical_rule_based_hard"]["unscorable_reason"] == "chunk_mapping_failed"
    assert coverage["classification"] == "product_behavior_observed_in_historical_run"
    assert coverage["historical_rule_based_hard"]["unsafe_mapping_failure"] is False
    assert analogue["current_rule_based_hard"]["source_coverage_failure"] is True
    assert report["source_evidence"]["private_ab_identity_required"] is False


def test_s037_characterization_separates_coverage_and_reporting_effects():
    report = build_report()
    anomalies = report["anomalies"]
    visible = [item for item in anomalies if item.get("corpus") in {"regression", "generalization"}]
    reporting = next(item for item in anomalies if item["classification"] == "reporting_only_anomaly")
    denominators = next(
        item for item in anomalies if item["classification"] == "reporting_only_denominator_difference"
    )

    assert {item["case_count"] for item in visible} == {6, 8}
    assert all(
        denominator == 0
        for item in visible
        for system in item["denominators"].values()
        for denominator in system.values()
    )
    assert reporting["historical_hard_compliance"]["source_coverage_failure"] == 2
    assert reporting["defensible_classification"]["confirmed_source_coverage_failure"] == 1
    assert denominators["parser_minus_rule_denominator_deltas"]["forbidden"] == 2
    assert denominators["parser_minus_rule_denominator_deltas"]["protected_spans"] == 2


def test_s037_characterization_keeps_current_operating_policy_unchanged():
    policy = build_report()["operating_policy_evidence"]

    assert policy == {
        "current_default": "parser_assisted",
        "explicit_baseline_mode": "rule_based",
        "mandatory_fallback": "semantic_rsvp.chunking.rules.RuleBasedChunker",
        "optimizer_behavior_unchanged": True,
        "runtime_model_downloads": False,
    }
