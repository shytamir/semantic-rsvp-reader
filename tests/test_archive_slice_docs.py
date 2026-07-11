from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts.archive_slice_docs import ArchiveError, apply_plan, build_plan, render_archive_index, run


MANAGEMENT = Path("docs/management")
VALIDATION = Path("docs/validation")


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


def repo(tmp_path: Path, management: dict[int, int], validation: dict[int, int] | None = None, current: int = 31, previous: int = 30, history: tuple[int, ...] = tuple(range(1, 31))) -> Path:
    root = tmp_path / "repo"
    for directory in (MANAGEMENT, VALIDATION):
        (root / directory).mkdir(parents=True, exist_ok=True)
    (root / MANAGEMENT / "STATUS.md").write_text(f"current_slice: S-{current:03d}\nprevious_slice: S-{previous:03d}\n", encoding="utf-8")
    (root / MANAGEMENT / "HISTORY.md").write_text("\n".join(f"S-{value:03d}" for value in history), encoding="utf-8")
    for directory, groups in ((MANAGEMENT, management), (VALIDATION, validation or {})):
        for ordinal, count in groups.items():
            for number in range(count):
                suffix = "scope" if number == 0 else f"note_{number}"
                (root / directory / f"s{ordinal:03d}_{suffix}.md").write_text(f"# S-{ordinal:03d} {suffix}\n", encoding="utf-8")
    _git(root, "init")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "user.name", "Test")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "fixture")
    return root


def moves(plan) -> list[str]:
    return [source.as_posix() for source, _ in plan.moves]


@pytest.mark.parametrize("count", [2, 3])
def test_no_operation_at_or_below_threshold(tmp_path, count):
    root = repo(tmp_path, {1: 1, 2: 1, 3: count - 2})
    plan = build_plan(root, {MANAGEMENT: 3})
    assert plan.moves == ()


def test_oldest_numeric_eligible_group_selected_first(tmp_path):
    root = repo(tmp_path, {2: 1, 10: 1, 29: 1})
    plan = build_plan(root, {MANAGEMENT: 2})
    assert moves(plan) == ["docs/management/s002_scope.md"]


@pytest.mark.parametrize("protected", [30, 31, 32])
def test_current_previous_and_future_are_protected(tmp_path, protected):
    root = repo(tmp_path, {1: 1, protected: 1})
    plan = build_plan(root, {MANAGEMENT: 1})
    assert moves(plan) == ["docs/management/s001_scope.md"]
    assert all(f"s{protected:03d}_" not in path for path in moves(plan))


def test_slice_absent_from_history_is_protected(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1}, history=(2,))
    plan = build_plan(root, {MANAGEMENT: 1})
    assert moves(plan) == ["docs/management/s002_scope.md"]


def test_same_slice_files_move_atomically_and_may_undershoot_limit(tmp_path):
    root = repo(tmp_path, {1: 2, 2: 1, 3: 1})
    plan = build_plan(root, {MANAGEMENT: 3})
    assert moves(plan) == ["docs/management/s001_note_1.md", "docs/management/s001_scope.md"]
    assert len(plan.directories[0].root_files) - len(plan.moves) == 2


def test_existing_destination_collision_is_rejected(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1})
    destination = root / MANAGEMENT / "archive/s001_scope.md"
    destination.parent.mkdir()
    destination.write_text("collision", encoding="utf-8")
    with pytest.raises(ArchiveError, match="collision"):
        build_plan(root, {MANAGEMENT: 1})


def test_check_performs_no_writes(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1})
    assert run("check", root, {MANAGEMENT: 1}) == 1
    assert (root / MANAGEMENT / "s001_scope.md").is_file()
    assert not (root / MANAGEMENT / "archive").exists()


def test_apply_refuses_dirty_worktree(tmp_path):
    root = repo(tmp_path, {1: 1})
    (root / "dirty.txt").write_text("dirty", encoding="utf-8")
    assert run("apply", root, {MANAGEMENT: 1}) == 2


def test_incoming_and_outgoing_links_and_anchors_are_rewritten(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1})
    source = root / MANAGEMENT / "s001_scope.md"
    source.write_text("# One\n[status](STATUS.md#state) [web](https://example.com) [local](#one)\n", encoding="utf-8")
    incoming = root / "README.md"
    incoming.write_text("[one](docs/management/s001_scope.md#one)\n", encoding="utf-8")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "links")
    plan = build_plan(root, {MANAGEMENT: 1})
    apply_plan(plan)
    moved = root / MANAGEMENT / "archive/s001_scope.md"
    assert "[status](../STATUS.md#state)" in moved.read_text(encoding="utf-8")
    assert "[web](https://example.com)" in moved.read_text(encoding="utf-8")
    assert "[local](#one)" in moved.read_text(encoding="utf-8")
    assert "[one](docs/management/archive/s001_scope.md#one)" in incoming.read_text(encoding="utf-8")


def test_archive_index_is_deterministic_descending_and_uses_h1(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1, 3: 1})
    plan = build_plan(root, {MANAGEMENT: 1})
    apply_plan(plan)
    text = (root / MANAGEMENT / "archive/index.md").read_text(encoding="utf-8")
    assert text.index("## S-002") < text.index("## S-001")
    assert "[S-002 scope](s002_scope.md)" in text
    assert "generated" not in text.lower()


def test_second_application_is_idempotent_and_archive_excluded_from_count(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1})
    apply_plan(build_plan(root, {MANAGEMENT: 1}))
    _git(root, "add", ".")
    _git(root, "commit", "-m", "archive")
    plan = build_plan(root, {MANAGEMENT: 1})
    assert plan.pending is False
    assert len(plan.directories[0].root_files) == 1


def test_configuration_overflow_is_actionable(tmp_path):
    root = repo(tmp_path, {30: 1, 31: 1, 32: 1})
    with pytest.raises(ArchiveError, match="protected or otherwise ineligible"):
        build_plan(root, {MANAGEMENT: 2})


def test_outside_repository_link_is_rejected(tmp_path):
    root = repo(tmp_path, {1: 1, 2: 1})
    source = root / MANAGEMENT / "s001_scope.md"
    source.write_text("# One\n[out](../../../outside.md)\n", encoding="utf-8")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "unsafe")
    with pytest.raises(ArchiveError, match="outside repository"):
        build_plan(root, {MANAGEMENT: 1})
