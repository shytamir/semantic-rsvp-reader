from pathlib import Path

from scripts import check_js_syntax


def test_find_js_runtime_returns_first_available_candidate(monkeypatch):
    def fake_which(candidate):
        return f"/bin/{candidate}" if candidate == "nodejs" else None

    monkeypatch.setattr(check_js_syntax.shutil, "which", fake_which)

    assert check_js_syntax.find_js_runtime(("node", "nodejs")) == "/bin/nodejs"


def test_find_js_runtime_returns_none_when_missing(monkeypatch):
    monkeypatch.setattr(check_js_syntax.shutil, "which", lambda candidate: None)

    assert check_js_syntax.find_js_runtime(("node", "nodejs")) is None


def test_target_js_file_points_at_static_app_js():
    assert check_js_syntax.target_js_file(Path("repo")) == Path("repo/static/js/app.js")


def test_main_skips_cleanly_when_runtime_is_missing(monkeypatch, capsys):
    monkeypatch.setattr(check_js_syntax, "find_js_runtime", lambda: None)

    assert check_js_syntax.main() == 0
    output = capsys.readouterr().out
    assert "Warning: no JavaScript runtime found" in output
    assert "static/js/app.js" in output.replace("\\", "/")
