from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
EVALUATION_ROOT = REPO_ROOT / "evaluation" / "parser_assisted_chunking"
STATUS_PATH = REPO_ROOT / "docs" / "management" / "STATUS.md"
ROADMAP_PATH = REPO_ROOT / "docs" / "management" / "roadmap.md"
HISTORY_PATH = REPO_ROOT / "docs" / "management" / "HISTORY.md"
INTEGRATION_PATH = EVALUATION_ROOT / "freeze" / "provisional_integration_record.json"
EXPECTED_INTEGRATION_COMMIT = "f8ec923f03b46aa75904e4cb4c11024b9ac9185e"


def _tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "-c", f"safe.directory={REPO_ROOT.as_posix()}", "ls-files", "-z"],
        cwd=REPO_ROOT,
    ).decode("utf-8")
    return [REPO_ROOT / path for path in output.rstrip("\0").split("\0") if path]


def _load_records(path: Path) -> list[Any]:
    if path.suffix == ".jsonl":
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return [json.loads(path.read_text(encoding="utf-8"))]


def _contains_value(value: Any, prohibited: str) -> bool:
    if isinstance(value, dict):
        return any(_contains_value(item, prohibited) for item in value.values())
    if isinstance(value, list):
        return any(_contains_value(item, prohibited) for item in value)
    return value == prohibited


def _sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def _display_path(path: Path) -> Path:
    return path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path


def validate_repository() -> list[str]:
    failures: list[str] = []
    tracked = _tracked_files()
    records: dict[Path, list[Any]] = {}
    for path in tracked:
        if path.suffix not in {".json", ".jsonl"}:
            continue
        try:
            records[path] = _load_records(path)
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            failures.append(f"{_display_path(path)}: invalid {path.suffix[1:].upper()}: {error}")

    for path, values in records.items():
        if any(_contains_value(value, "pending_until_commit") for value in values):
            failures.append(f"{_display_path(path)}: committed placeholder pending_until_commit")

    required_shapes = {
        EVALUATION_ROOT / "freeze" / "parser_assisted_implementation_freeze.json": {"slice", "implementation_commit", "scoring_configuration", "dependencies", "visible_corpus"},
        EVALUATION_ROOT / "freeze" / "s024_objective_run_record.json": {"ab_identity_key_committed", "private_output_dir", "python_version"},
        EVALUATION_ROOT / "results" / "s024_objective_comparison.json": {"metadata", "cases", "summaries", "human_ab_packet"},
        EVALUATION_ROOT / "results" / "s024_human_ab_preference.json": {"case_count", "identity_key_committed", "per_case_system_mapping_committed", "system_preference_counts"},
        INTEGRATION_PATH: {"slice", "scientific_experiment_freeze", "provisional_integration", "dependencies", "file_hashes_sha256"},
    }
    for path, fields in required_shapes.items():
        value = records.get(path, [{}])[0]
        missing = fields - set(value) if isinstance(value, dict) else fields
        if missing:
            failures.append(f"{path.relative_to(REPO_ROOT)}: missing fields: {', '.join(sorted(missing))}")

    status = STATUS_PATH.read_text(encoding="utf-8")
    roadmap = ROADMAP_PATH.read_text(encoding="utf-8")
    history = HISTORY_PATH.read_text(encoding="utf-8")
    current = re.search(r"^current_slice:\s*(S-\d+)\s*$", status, re.MULTILINE)
    now = re.search(r"^## Now\s*(.*?)(?=^## )", roadmap, re.MULTILINE | re.DOTALL)
    active = re.findall(r"\*\*(S-\d+):", now.group(1) if now else "")
    if not current or active != [current.group(1)]:
        failures.append(f"management: STATUS current slice and roadmap Now disagree: current={current.group(1) if current else None}, now={active}")
    previous = re.search(r"^previous_slice:\s*(S-\d+)\s*$", status, re.MULTILINE)
    if previous and previous.group(1) not in history:
        failures.append(f"management: previous slice {previous.group(1)} is absent from HISTORY.md")

    integration = records.get(INTEGRATION_PATH, [{}])[0]
    provisional = integration.get("provisional_integration", {})
    if provisional.get("integration_commit") != EXPECTED_INTEGRATION_COMMIT:
        failures.append("integration record: S-026 commit identity is not finalized")
    for relative, expected in integration.get("file_hashes_sha256", {}).items():
        path = REPO_ROOT / relative
        if not path.is_file():
            failures.append(f"integration record: missing registered file {relative}")
        elif _sha256(path) != expected:
            failures.append(f"integration record: SHA-256 mismatch for {relative}")

    private_names = [path.relative_to(REPO_ROOT).as_posix() for path in tracked if re.search(r"(?:identity[_-]?key|system[_-]?mapping|s024-private)", path.name, re.IGNORECASE)]
    if private_names:
        failures.append(f"private blind identity material is tracked: {', '.join(private_names)}")
    preference = records.get(EVALUATION_ROOT / "results" / "s024_human_ab_preference.json", [{}])[0]
    if preference.get("identity_key_committed") is not False or preference.get("per_case_system_mapping_committed") is not False:
        failures.append("redacted human preference record exposes private identity material")

    return failures


def main() -> int:
    failures = validate_repository()
    if failures:
        print("Repository integrity validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Repository integrity validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
