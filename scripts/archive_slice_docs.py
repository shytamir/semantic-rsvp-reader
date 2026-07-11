from __future__ import annotations

import argparse
import os
import posixpath
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANAGEMENT_LIMIT = 8
VALIDATION_LIMIT = 6
TARGETS = {
    Path("docs/management"): MANAGEMENT_LIMIT,
    Path("docs/validation"): VALIDATION_LIMIT,
}
SLICE_RE = re.compile(r"^s(?P<ordinal>\d{3})_[a-z0-9][a-z0-9_-]*\.md$")
LINK_RE = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target>[^)]+)(?P<suffix>\))")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:")


class ArchiveError(RuntimeError):
    pass


@dataclass(frozen=True)
class DirectoryPlan:
    directory: Path
    limit: int
    root_files: tuple[Path, ...]
    selected_groups: tuple[tuple[int, tuple[Path, ...]], ...]


@dataclass(frozen=True)
class ArchivePlan:
    root: Path
    directories: tuple[DirectoryPlan, ...]
    rewrites: tuple[tuple[Path, str], ...]
    index_updates: tuple[tuple[Path, str], ...]

    @property
    def moves(self) -> tuple[tuple[Path, Path], ...]:
        pairs = []
        for plan in self.directories:
            for _, files in plan.selected_groups:
                for source in files:
                    pairs.append((source, plan.directory / "archive" / source.name))
        return tuple(sorted(pairs, key=lambda pair: pair[0].as_posix()))

    @property
    def pending(self) -> bool:
        return bool(self.moves or self.rewrites or self.index_updates)


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *args],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise ArchiveError(result.stderr.strip() or "Git command failed")
    return result.stdout


def tracked_files(root: Path) -> list[Path]:
    output = _git(root, "ls-files", "-z")
    return [root / item for item in output.rstrip("\0").split("\0") if item]


def management_state(root: Path) -> tuple[int, int, set[int]]:
    status = (root / "docs/management/STATUS.md").read_text(encoding="utf-8")
    history = (root / "docs/management/HISTORY.md").read_text(encoding="utf-8")
    current_match = re.search(r"^current_slice:\s*S-(\d{3})\s*$", status, re.MULTILINE)
    previous_match = re.search(r"^previous_slice:\s*S-(\d{3})\s*$", status, re.MULTILINE)
    if not current_match or not previous_match:
        raise ArchiveError("Invalid management state: STATUS.md needs current_slice and previous_slice as S-NNN")
    completed = {int(value) for value in re.findall(r"\bS-(\d{3})\b", history)}
    return int(current_match.group(1)), int(previous_match.group(1)), completed


def _root_slice_files(root: Path, directory: Path, tracked: list[Path]) -> list[Path]:
    absolute = root / directory
    return sorted(
        (
            path.relative_to(root)
            for path in tracked
            if path.is_file() and path.parent == absolute and SLICE_RE.fullmatch(path.name)
        ),
        key=lambda path: (int(SLICE_RE.fullmatch(path.name).group("ordinal")), path.name),
    )


def _directory_plan(
    root: Path,
    directory: Path,
    limit: int,
    tracked: list[Path],
    current: int,
    previous: int,
    completed: set[int],
) -> DirectoryPlan:
    if limit < 0:
        raise ArchiveError(f"Malformed configuration: negative limit for {directory.as_posix()}")
    files = _root_slice_files(root, directory, tracked)
    groups: dict[int, list[Path]] = {}
    for path in files:
        ordinal = int(SLICE_RE.fullmatch(path.name).group("ordinal"))
        groups.setdefault(ordinal, []).append(path)
    if len(files) <= limit:
        return DirectoryPlan(directory, limit, tuple(files), ())

    eligible = [
        ordinal
        for ordinal in groups
        if ordinal < current and ordinal != previous and ordinal in completed
    ]
    projected = len(files)
    selected = []
    for ordinal in sorted(eligible):
        group = tuple(sorted(groups[ordinal], key=lambda path: path.as_posix()))
        for source in group:
            destination = directory / "archive" / source.name
            if (root / destination).exists():
                raise ArchiveError(f"Archive destination collision: {destination.as_posix()}")
        selected.append((ordinal, group))
        projected -= len(group)
        if projected <= limit:
            break
    if projected > limit:
        raise ArchiveError(
            f"Configuration overflow for {directory.as_posix()}: {projected} protected or "
            f"otherwise ineligible root slice files exceed limit {limit}"
        )
    return DirectoryPlan(directory, limit, tuple(files), tuple(selected))


def _split_target(raw: str) -> tuple[str, str, bool]:
    stripped = raw.strip()
    bracketed = stripped.startswith("<") and stripped.endswith(">")
    if bracketed:
        stripped = stripped[1:-1]
    path, separator, fragment = stripped.partition("#")
    return path, f"#{fragment}" if separator else "", bracketed


def _rewrite_markdown(
    root: Path,
    original_path: Path,
    final_path: Path,
    text: str,
    move_map: dict[Path, Path],
) -> str:
    def replace(match: re.Match[str]) -> str:
        raw = match.group("target")
        path_part, fragment, bracketed = _split_target(raw)
        lower = path_part.lower()
        if not path_part or lower.startswith(EXTERNAL_PREFIXES):
            return match.group(0)
        resolved = (root / original_path.parent / Path(path_part)).resolve()
        try:
            old_target = resolved.relative_to(root.resolve())
        except ValueError as error:
            raise ArchiveError(
                f"Unsafe Markdown link outside repository in {original_path.as_posix()}: {raw}"
            ) from error
        final_target = move_map.get(old_target, old_target)
        if original_path == final_path and final_target == old_target:
            return match.group(0)
        relative = posixpath.relpath(final_target.as_posix(), final_path.parent.as_posix())
        new_target = f"{relative}{fragment}"
        if bracketed or " " in new_target:
            new_target = f"<{new_target}>"
        return f"{match.group('prefix')}{new_target}{match.group('suffix')}"

    return LINK_RE.sub(replace, text)


def _first_h1(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.name


def render_archive_index(root: Path, directory: Path, incoming: dict[Path, Path]) -> str:
    archive = root / directory / "archive"
    paths = {path.relative_to(root) for path in archive.glob("s*.md") if SLICE_RE.fullmatch(path.name)} if archive.exists() else set()
    paths.update(destination for destination in incoming.values() if destination.parent == directory / "archive")
    groups: dict[int, list[Path]] = {}
    for path in paths:
        groups.setdefault(int(SLICE_RE.fullmatch(path.name).group("ordinal")), []).append(path)
    lines = [
        "# Archived Slice Documents",
        "",
        "These documents are preserved as historical evidence. They are not the current project-management authority.",
        "",
    ]
    for ordinal in sorted(groups, reverse=True):
        lines.extend([f"## S-{ordinal:03d}", ""])
        for relative in sorted(groups[ordinal], key=lambda path: path.name):
            source = next((old for old, new in incoming.items() if new == relative), relative)
            label = _first_h1(root / source)
            lines.append(f"- [{label}]({relative.name})")
        lines.append("")
    return "\n".join(lines)


def build_plan(root: Path = REPO_ROOT, limits: dict[Path, int] | None = None) -> ArchivePlan:
    root = root.resolve()
    configured = limits or TARGETS
    tracked = tracked_files(root)
    current, previous, completed = management_state(root)
    directories = tuple(
        _directory_plan(root, directory, limit, tracked, current, previous, completed)
        for directory, limit in configured.items()
    )
    move_map = {source: destination for plan in directories for _, group in plan.selected_groups for source in group for destination in [plan.directory / "archive" / source.name]}
    rewrites = []
    for absolute in tracked:
        if absolute.suffix.lower() != ".md" or not absolute.is_file():
            continue
        original = absolute.relative_to(root)
        final = move_map.get(original, original)
        old_text = absolute.read_text(encoding="utf-8")
        new_text = _rewrite_markdown(root, original, final, old_text, move_map)
        if new_text != old_text:
            rewrites.append((original, new_text))
    index_updates = []
    for directory in configured:
        index_path = directory / "archive" / "index.md"
        expected = render_archive_index(root, directory, move_map)
        current_text = (root / index_path).read_text(encoding="utf-8") if (root / index_path).is_file() else None
        if current_text != expected:
            index_updates.append((index_path, expected))
    return ArchivePlan(root, directories, tuple(rewrites), tuple(index_updates))


def apply_plan(plan: ArchivePlan) -> None:
    move_map = dict(plan.moves)
    rewrite_map = dict(plan.rewrites)
    for source, destination in plan.moves:
        target = plan.root / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        (plan.root / source).replace(target)
    for original, text in plan.rewrites:
        final = move_map.get(original, original)
        (plan.root / final).write_text(text, encoding="utf-8")
    for path, text in plan.index_updates:
        target = plan.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")


def _print_plan(plan: ArchivePlan) -> None:
    print("Slice-document archive check")
    for item in plan.directories:
        print(f"\n{item.directory.as_posix()}:")
        print(f"  root slice files: {len(item.root_files)}")
        print(f"  configured limit: {item.limit}")
        if item.selected_groups:
            print("  archive required:")
            for ordinal, files in item.selected_groups:
                print(f"    S-{ordinal:03d}")
                for path in files:
                    print(f"      {path.as_posix()}")
        else:
            print("  archive required: none")


def run(mode: str, root: Path = REPO_ROOT, limits: dict[Path, int] | None = None) -> int:
    try:
        if mode == "apply" and _git(root.resolve(), "status", "--porcelain").strip():
            raise ArchiveError("Apply refused: Git worktree is not clean")
        plan = build_plan(root, limits)
        _print_plan(plan)
        if mode == "check":
            if plan.pending:
                print("\nArchive or archive-index maintenance is pending.")
                return 1
            print("\nNo archiving required.")
            return 0
        apply_plan(plan)
        print(f"\nApplied {len(plan.moves)} move(s), {len(plan.rewrites)} link rewrite(s), and {len(plan.index_updates)} archive index update(s).")
        return 0
    except (ArchiveError, OSError, UnicodeError) as error:
        print(f"Archive operation failed: {error}", file=sys.stderr)
        return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    return run("check" if args.check else "apply")


if __name__ == "__main__":
    raise SystemExit(main())
