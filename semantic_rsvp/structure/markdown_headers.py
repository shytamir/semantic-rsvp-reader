from __future__ import annotations

from dataclasses import dataclass

from semantic_rsvp.navigation.models import NavigationMeta


@dataclass(frozen=True)
class MarkdownHeader:
    level: int
    text: str
    line_index: int
    char_start: int
    char_end: int


@dataclass(frozen=True)
class StructureMeta:
    active_h1: str | None = None
    active_h2: str | None = None
    active_label: str | None = None
    active_path: tuple[str, ...] = ()
    is_header_chunk: bool = False
    header_level: int | None = None


def strip_header_marker(line: str) -> str:
    stripped = line.strip()
    if stripped.startswith("# ") and not stripped.startswith("## "):
        return stripped[2:].strip()
    if stripped.startswith("## ") and not stripped.startswith("### "):
        return stripped[3:].strip()
    return ""


def detect_markdown_headers(raw_text: str) -> list[MarkdownHeader]:
    if not isinstance(raw_text, str):
        raise TypeError("detect_markdown_headers expects a string.")

    headers: list[MarkdownHeader] = []
    cursor = 0
    for line_index, line_with_ending in enumerate(raw_text.splitlines(keepends=True)):
        line = line_with_ending.rstrip("\n")
        if line.endswith("\r"):
            line = line[:-1]
        stripped = line.strip()
        if stripped.startswith("### "):
            cursor += len(line_with_ending)
            continue
        if stripped.startswith("# "):
            level = 1
            text = stripped[2:].strip()
        elif stripped.startswith("## "):
            level = 2
            text = stripped[3:].strip()
        else:
            cursor += len(line_with_ending)
            continue

        if text:
            headers.append(
                MarkdownHeader(
                    level=level,
                    text=text,
                    line_index=line_index,
                    char_start=cursor,
                    char_end=cursor + len(line),
                )
            )
        cursor += len(line_with_ending)
    return headers


def compute_structure_metadata(
    normalized_text: str,
    navigation_metadata: list[NavigationMeta],
) -> list[StructureMeta]:
    headers = detect_markdown_headers(normalized_text)
    if not navigation_metadata:
        return []
    if not headers:
        return [StructureMeta() for _ in navigation_metadata]

    return [
        _structure_for_position(headers, navigation.char_start)
        for navigation in navigation_metadata
    ]


def _structure_for_position(
    headers: list[MarkdownHeader],
    position: int,
) -> StructureMeta:
    active_h1 = None
    active_h2 = None
    header_level = None
    is_header_chunk = False

    for header in headers:
        if header.char_start > position:
            break
        if header.level == 1:
            active_h1 = header.text
            active_h2 = None
        elif header.level == 2:
            active_h2 = header.text
        if header.char_start <= position < header.char_end:
            is_header_chunk = True
            header_level = header.level

    active_path = tuple(label for label in (active_h1, active_h2) if label)
    active_label = active_h2 or active_h1
    return StructureMeta(
        active_h1=active_h1,
        active_h2=active_h2,
        active_label=active_label,
        active_path=active_path,
        is_header_chunk=is_header_chunk,
        header_level=header_level,
    )
