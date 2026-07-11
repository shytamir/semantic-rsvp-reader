import json

from scripts import validate_repository_integrity as integrity


def test_repository_integrity_passes():
    assert integrity.validate_repository() == []


def test_committed_placeholder_is_rejected(monkeypatch, tmp_path):
    record = tmp_path / "record.json"
    record.write_text(json.dumps({"integration_commit": "pending_until_commit"}), encoding="utf-8")
    monkeypatch.setattr(integrity, "_tracked_files", lambda: [record])
    monkeypatch.setattr(integrity, "STATUS_PATH", integrity.STATUS_PATH)

    failures = integrity.validate_repository()

    assert any("committed placeholder pending_until_commit" in failure for failure in failures)
