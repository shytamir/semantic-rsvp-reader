from __future__ import annotations

import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Check:
    name: str
    command: list[str]
    note: str = ""
    parse_detect_secrets: bool = False
    local_config: Path | None = None


@dataclass
class Result:
    name: str
    status: str
    detail: str


CHECKS = [
    Check(
        name="bandit",
        command=["bandit", "-r", "semantic_rsvp", "-q"],
    ),
    Check(
        name="pip-audit",
        command=["pip-audit", "-r", "requirements.txt"],
    ),
    Check(
        name="semgrep",
        command=[
            "semgrep",
            "--config",
            "semgrep.yml",
            "--error",
            "semantic_rsvp",
            "static",
            "templates",
        ],
        note="requires a repo-local semgrep.yml to avoid network-backed registry configs",
        local_config=PROJECT_ROOT / "semgrep.yml",
    ),
    Check(
        name="gitleaks",
        command=["gitleaks", "detect", "--source", ".", "--no-banner"],
    ),
    Check(
        name="detect-secrets",
        command=["detect-secrets", "scan", "--all-files"],
        parse_detect_secrets=True,
    ),
]


def main() -> int:
    results = [run_check(check) for check in CHECKS]
    print()
    print("Security check summary:")
    for result in results:
        print(f"- {result.name}: {result.status} - {result.detail}")
    return 1 if any(result.status == "failed" for result in results) else 0


def run_check(check: Check) -> Result:
    executable = check.command[0]
    if shutil.which(executable) is None:
        return Result(check.name, "skipped", f"{executable} not found on PATH")
    if check.local_config is not None and not check.local_config.exists():
        return Result(check.name, "skipped", f"{check.local_config.name} not found; {check.note}")

    print(f"Running {check.name}: {' '.join(check.command)}")
    completed = subprocess.run(
        check.command,
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.stdout.strip():
        print(completed.stdout.rstrip())
    if completed.stderr.strip():
        print(completed.stderr.rstrip(), file=sys.stderr)

    if check.parse_detect_secrets and completed.returncode == 0:
        return parse_detect_secrets_result(completed.stdout)

    if completed.returncode == 0:
        detail = check.note or "completed successfully"
        return Result(check.name, "passed", detail)

    detail = f"exit code {completed.returncode}"
    if check.note:
        detail = f"{detail}; {check.note}"
    return Result(check.name, "failed", detail)


def parse_detect_secrets_result(output: str) -> Result:
    try:
        payload = json.loads(output)
    except json.JSONDecodeError:
        return Result("detect-secrets", "passed", "scan completed; output was not JSON")

    results = payload.get("results", {})
    if not isinstance(results, dict):
        return Result("detect-secrets", "passed", "scan completed")

    finding_count = sum(
        len(findings)
        for findings in results.values()
        if isinstance(findings, list)
    )
    if finding_count:
        return Result("detect-secrets", "failed", f"{finding_count} potential secret(s) found")
    return Result("detect-secrets", "passed", "no potential secrets reported")


if __name__ == "__main__":
    raise SystemExit(main())
