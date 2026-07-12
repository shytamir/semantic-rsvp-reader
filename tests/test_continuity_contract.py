import subprocess

import pytest

from scripts.check_js_syntax import find_js_runtime, project_root


def test_continuity_contract_with_node():
    runtime = find_js_runtime()
    if runtime is None:
        pytest.skip("Node.js is unavailable")

    result = subprocess.run(
        [runtime, "scripts/check_continuity_contract.mjs"],
        cwd=project_root(),
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr
    assert "S-041 continuity contract checks passed." in result.stdout


def test_mobile_shell_exposes_local_continuity_controls(client):
    html = client.get("/").data
    javascript = client.get("/static/js/app.js").data.decode("utf-8")

    assert b'id="remove-continuity-button"' in html
    assert b'id="clear-continuity-button"' in html
    assert b'id="continuity-status"' in html
    assert b'js/continuity.js' in html
    assert "restoreCurrentDocumentContinuity" in javascript
    assert "pause({ record: false, render: false })" in javascript
    assert "persistReaderPreferences" in javascript


def test_continuity_storage_contract_excludes_sensitive_transient_state(client):
    javascript = client.get("/static/js/continuity.js").data.decode("utf-8")

    assert "semantic-rsvp-reader.preferences.v1" in javascript
    assert "semantic-rsvp-reader.documents.v1" in javascript
    assert "MAX_DOCUMENTS = 12" in javascript
    assert "MAX_BREAKPOINTS = 64" in javascript
    assert "STALE_AFTER_MS = 90" in javascript
    for excluded in (
        "source_text",
        "defect_notes",
        "session_events",
        "telemetry",
        "timer_id",
    ):
        assert excluded not in javascript
