from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_environment_contract_and_requirements_record_accepted_profiles_and_versions():
    contract = (ROOT / "docs/development/environment_contract.md").read_text(encoding="utf-8")
    core = (ROOT / "requirements-core.txt").read_text(encoding="utf-8")
    parser = (ROOT / "requirements-nlp-spike.txt").read_text(encoding="utf-8")

    assert "Flask==3.1.3" in core
    assert "pytest==9.1.1" in core
    assert "click==8.1.8" in parser
    assert "spacy==3.7.5" in parser
    assert "en_core_web_sm-3.7.1" in parser
    assert "`standard`" in contract
    assert "`core`" in contract
    assert "Python `3.12.x`" in contract
    assert contract.count("py -3.12 -m venv .venv") == 2
    assert contract.count("sys.version_info[:2] == (3, 12)") == 2
    assert "Remove-Item -Recurse -Force -LiteralPath .venv" in contract
    assert "Remove-Item Env:RSVP_CHUNKER_MODE -ErrorAction SilentlyContinue" in contract


def test_environment_contract_matches_actual_configuration_sources():
    contract = (ROOT / "docs/development/environment_contract.md").read_text(encoding="utf-8")

    for setting in (
        "RSVP_CHUNKER_MODE",
        "DEFECT_REPORT_DIR",
        "CHECK_STORAGE_ENCRYPTION",
        "MAX_CONTENT_LENGTH",
        "FLASK_DEBUG",
    ):
        assert f"`{setting}`" in contract
    assert contract.count("No environment-variable support.") == 3
    assert "Explicit `create_app(config)` value, then environment variable" in contract
    assert "direct `python semantic_rsvp/web.py` execution" in contract
