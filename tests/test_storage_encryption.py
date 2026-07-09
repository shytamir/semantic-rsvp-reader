import subprocess

from semantic_rsvp.security.storage_encryption import check_storage_encryption


def test_storage_encryption_check_unknown_platform(monkeypatch, tmp_path):
    monkeypatch.setattr("platform.system", lambda: "Plan9")

    status = check_storage_encryption(tmp_path)

    assert status.status == "unknown"
    assert status.warning


def test_windows_storage_encryption_detects_bitlocker_on(monkeypatch, tmp_path):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    monkeypatch.setattr(
        "subprocess.run",
        lambda *args, **kwargs: subprocess.CompletedProcess(
            args[0],
            0,
            stdout="Protection Status: Protection On",
            stderr="",
        ),
    )

    status = check_storage_encryption(tmp_path)

    assert status.status == "encrypted"
    assert status.warning is None


def test_storage_encryption_check_does_not_raise_when_tool_missing(
    monkeypatch,
    tmp_path,
):
    monkeypatch.setattr("platform.system", lambda: "Darwin")

    def raise_missing(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr("subprocess.run", raise_missing)

    status = check_storage_encryption(tmp_path)

    assert status.status == "unknown"
    assert status.warning
