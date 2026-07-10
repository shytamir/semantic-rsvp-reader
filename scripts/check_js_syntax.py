from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


RUNTIME_CANDIDATES = ("node", "nodejs")
JS_FILE = Path("static/js/app.js")


def find_js_runtime(candidates: tuple[str, ...] = RUNTIME_CANDIDATES) -> str | None:
    for candidate in candidates:
        runtime = shutil.which(candidate)
        if runtime:
            return runtime
    return None


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def target_js_file(root: Path | None = None) -> Path:
    return (root or project_root()) / JS_FILE


def run_syntax_check(runtime: str, js_file: Path) -> int:
    print(f"JavaScript runtime found: {runtime}")
    print(f"Checking JavaScript syntax: {js_file}")
    result = subprocess.run(
        [runtime, "--check", str(js_file)],
        text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if result.returncode == 0:
        print("JavaScript syntax check passed.")
    else:
        print("JavaScript syntax check failed.")
    return result.returncode


def main() -> int:
    root = project_root()
    js_file = target_js_file(root)
    runtime = find_js_runtime()
    if runtime is None:
        print(
            "Warning: no JavaScript runtime found. "
            "Install node or nodejs to run local syntax checks."
        )
        print(f"Skipped JavaScript syntax check for: {js_file}")
        return 0
    return run_syntax_check(runtime, js_file)


if __name__ == "__main__":
    raise SystemExit(main())
