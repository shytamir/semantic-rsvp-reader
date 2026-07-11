from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts.archive_slice_docs import ArchiveError, apply_plan, build_plan, run


MANAGEMENT = Path("docs/management")
VALIDATION = Path("docs/validation")


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


def repo(
    tmp_path: Path,
    management: dict[int, int],
    validation: dict[int, int] | None = None,
    current: int = 32,
    history: tuple[int, ...] = tuple(range(1, 32)),
    state: str = "AWAITING_HUMAN_VALIDATION",
    owner: str = "Human",
) -> Path:
    root = tmp_path / "repo"
    for directory in (MANAGEMENT, VALIDATION):
        (root / directory).mkdir(parents=True, exist_ok=True)
    (root / MANAGEMENT / "STATUS.md").write_text(
        f"current_slice: S-{current:03d}\nstate: {state}\nowner: {owner}\nprevious_slice: S-{current - 1:03d}\n",
        encoding="utf-8",
    )
    (root / MANAGEMENT / "HISTORY.md").write_text(
        "\n".join(f"S-{value:03d}" for value in history), encoding="utf-8"
    )
    for directory, groups in ((MANAGEMENT, management), (VALIDATION, validation or {})):
        for ordinal, count in groups.items():
            for number in range(count):
                suffix = "scope" if number == 0 else f"note_{number}"
                (root / directory / f"s{ordinal:03d}_{suffix}.md").write_text(
                    f"# S-{ordinal:03d} {suffix}\n", encoding="utf-8"
                )
    _git(root, "init")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "user.name", "Test")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "fixture")
    return root


def moves(plan) -> list[str]:
    return [source.as_posix() for source, _ in plan.moves]


@pytest.mark.parametrize("protected", [30, 31, 32, 33])
def test_current_two_previous_and_future_are_protected(tmp_path, protected):
    root = repo(tmp_path, {protected: 1})
    assert build_plan(root, (MANAGEMENT,)).moves == ()


def test_current_minus_three_and_older_completed_slices_are_eligible(tmp_path):
    root = repo(tmp_path, {20: 1, 28: 1, 29: 1, 30: 1})
    assert moves(build_plan(root, (MANAGEMENT,))) == [
        "docs/management/s020_scope.md",
        "docs/management/s028_scope.md",
        "docs/management/s029_scope.md",
    ]


@pytest.mark.parametrize(
    ("state", "owner"),
    [("READY_FOR_IMPLEMENTATION", "Codex"), ("AWAITING_HUMAN_VALIDATION", "Human")],
)
def test_state_and_owner_do_not_affect_boundary(tmp_path, state, owner):
    root = repo(tmp_path, {29: 1, 30: 1}, state=state, owner=owner)
    plan = build_plan(root, (MANAGEMENT,))
    assert plan.archive_boundary == 29
    assert moves(plan) == ["docs/management/s029_scope.md"]


def test_ordinal_gaps_do_not_backfill_retention_window(tmp_path):
    root = repo(tmp_path, {10: 1, 32: 1})
    assert moves(build_plan(root, (MANAGEMENT,))) == ["docs/management/s010_scope.md"]


def test_same_slice_files_move_atomically(tmp_path):
    root = repo(tmp_path, {29: 2, 30: 1})
    assert moves(build_plan(root, (MANAGEMENT,))) == [
        "docs/management/s029_note_1.md",
        "docs/management/s029_scope.md",
    ]


def test_directories_may_retain_different_file_counts(tmp_path):
    root = repo(tmp_path, {29: 2, 30: 1, 31: 1, 32: 1}, {29: 1, 30: 3, 31: 1})
    plan = build_plan(root)
    assert [len(item.root_files) - sum(len(group) for _, group in item.selected_groups) for item in plan.directories] == [3, 4]


def test_slice_absent_from_history_remains_protected(tmp_path):
    root = repo(tmp_path, {28: 1, 29: 1}, history=(29,))
    plan = build_plan(root, (MANAGEMENT,))
    assert moves(plan) == ["docs/management/s029_scope.md"]
    assert plan.directories[0].protected_groups == (28,)


def test_existing_destination_collision_is_rejected(tmp_path):
    root = repo(tmp_path, {29: 1})
    destination = root / MANAGEMENT / "archive/s029_scope.md"
    destination.parent.mkdir()
    destination.write_text("collision", encoding="utf-8")
    with pytest.raises(ArchiveError, match="collision"):
        build_plan(root, (MANAGEMENT,))


def test_check_performs_no_writes(tmp_path):
    root = repo(tmp_path, {29: 1})
    assert run("check", root, (MANAGEMENT,)) == 1
    assert (root / MANAGEMENT / "s029_scope.md").is_file()
    assert not (root / MANAGEMENT / "archive").exists()


def test_apply_refuses_dirty_worktree(tmp_path):
    root = repo(tmp_path, {30: 1})
    (root / "dirty.txt").write_text("dirty", encoding="utf-8")
    assert run("apply", root, (MANAGEMENT,)) == 2


def test_incoming_and_outgoing_links_and_anchors_are_rewritten(tmp_path):
    root = repo(tmp_path, {29: 1})
    source = root / MANAGEMENT / "s029_scope.md"
    source.write_text("# Twenty Nine\n[status](STATUS.md#state) [web](https://example.com) [local](#one)\n", encoding="utf-8")
    incoming = root / "README.md"
    incoming.write_text("[scope](docs/management/s029_scope.md#one)\n", encoding="utf-8")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "links")
    plan = build_plan(root, (MANAGEMENT,))
    apply_plan(plan)
    moved = root / MANAGEMENT / "archive/s029_scope.md"
    assert "[status](../STATUS.md#state)" in moved.read_text(encoding="utf-8")
    assert "[web](https://example.com)" in moved.read_text(encoding="utf-8")
    assert "[local](#one)" in moved.read_text(encoding="utf-8")
    assert "[scope](docs/management/archive/s029_scope.md#one)" in incoming.read_text(encoding="utf-8")


def test_archive_index_is_deterministic_descending_and_uses_h1(tmp_path):
    root = repo(tmp_path, {28: 1, 29: 1})
    apply_plan(build_plan(root, (MANAGEMENT,)))
    text = (root / MANAGEMENT / "archive/index.md").read_text(encoding="utf-8")
    assert text.index("## S-029") < text.index("## S-028")
    assert "[S-029 scope](s029_scope.md)" in text
    assert "generated" not in text.lower()


def test_second_application_is_idempotent_and_archived_files_are_excluded(tmp_path):
    root = repo(tmp_path, {29: 1, 30: 1})
    apply_plan(build_plan(root, (MANAGEMENT,)))
    _git(root, "add", ".")
    _git(root, "commit", "-m", "archive")
    plan = build_plan(root, (MANAGEMENT,))
    assert plan.pending is False
    assert plan.directories[0].root_groups == (30,)


def test_outside_repository_link_is_rejected(tmp_path):
    root = repo(tmp_path, {29: 1})
    source = root / MANAGEMENT / "s029_scope.md"
    source.write_text("# Twenty Nine\n[out](../../../outside.md)\n", encoding="utf-8")
    _git(root, "add", ".")
    _git(root, "commit", "-m", "unsafe")
    with pytest.raises(ArchiveError, match="outside repository"):
        build_plan(root, (MANAGEMENT,))
