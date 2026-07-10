"""Check repository-local Markdown links.

This intentionally stays small and standard-library only. It verifies relative
file links in Markdown docs and ignores external URLs, mailto links, and pure
in-page anchors.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "data:",
)


def iter_markdown_files() -> list[Path]:
    ignored_parts = {".git", ".venv", "__pycache__"}
    return [
        path
        for path in REPO_ROOT.rglob("*.md")
        if not ignored_parts.intersection(path.parts)
    ]


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if not target:
        return ""
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target.split("#", 1)[0])


def is_checkable_target(target: str) -> bool:
    lower_target = target.lower()
    return bool(target) and not lower_target.startswith(EXTERNAL_PREFIXES)


def check_file(path: Path) -> list[str]:
    failures: list[str] = []
    text = path.read_text(encoding="utf-8")
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in MARKDOWN_LINK_RE.finditer(line):
            target = normalize_target(match.group(1))
            if not is_checkable_target(target):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(REPO_ROOT)
            except ValueError:
                failures.append(f"{path.relative_to(REPO_ROOT)}:{line_number}: outside repo: {match.group(1)}")
                continue
            if not resolved.exists():
                failures.append(f"{path.relative_to(REPO_ROOT)}:{line_number}: missing target: {match.group(1)}")
    return failures


def main() -> int:
    failures: list[str] = []
    for path in iter_markdown_files():
        failures.extend(check_file(path))

    if failures:
        print("Broken Markdown links found:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
