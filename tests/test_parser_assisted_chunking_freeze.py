import subprocess
import sys

from scripts.chunking_experiment_common import (
    BASELINE_OUTPUT_PATH,
    VISIBLE_CORPORA,
    load_cases,
    load_json,
    manifest_hashes,
)
from scripts.freeze_chunking_baseline import build_baseline_payload
from scripts.validate_chunking_corpus import validate_baseline, validate_cases


def test_visible_corpus_cases_are_valid():
    cases = load_cases()

    assert len(cases) == 22
    assert {case["corpus"] for case in cases} == set(VISIBLE_CORPORA)
    assert validate_cases(cases) == []


def test_manifest_hashes_match_frozen_record():
    expected = load_json(BASELINE_OUTPUT_PATH.parent / "manifest_hashes.json")

    assert manifest_hashes() == expected


def test_rule_based_baseline_covers_visible_corpus():
    cases = load_cases()

    assert validate_baseline(cases) == []


def test_rule_based_baseline_is_reproducible():
    regenerated = build_baseline_payload()
    committed = load_json(BASELINE_OUTPUT_PATH)

    assert regenerated == committed


def test_freeze_script_check_mode_passes():
    result = subprocess.run(
        [sys.executable, "scripts/freeze_chunking_baseline.py", "--check"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "reproducible" in result.stdout
