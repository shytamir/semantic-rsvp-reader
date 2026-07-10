from __future__ import annotations

from semantic_rsvp.navigation.models import NavigationMeta


def split_paragraphs(normalized_text: str) -> list[str]:
    if not normalized_text:
        return []
    return [
        paragraph.strip()
        for paragraph in normalized_text.split("\n\n")
        if paragraph.strip()
    ]


def locate_sentence_paragraphs(
    normalized_text: str,
    sentences: list[str],
) -> list[int]:
    if not normalized_text or not sentences:
        return []

    spans = _paragraph_spans(normalized_text)
    cursor = 0
    paragraph_indices: list[int] = []
    for sentence in sentences:
        position = normalized_text.find(sentence, cursor)
        if position < 0:
            paragraph_indices.append(0)
            continue
        paragraph_indices.append(_paragraph_index_for_position(spans, position))
        cursor = position + len(sentence)
    return paragraph_indices


def compute_navigation_metadata(
    normalized_text: str,
    chunk_texts: list[str],
) -> list[NavigationMeta]:
    if not normalized_text or not chunk_texts:
        return []

    total_chars = max(len(normalized_text), 0)
    spans = _paragraph_spans(normalized_text)
    raw_items = []
    cursor = 0
    for chunk_text in chunk_texts:
        start = normalized_text.find(chunk_text, cursor)
        if start < 0:
            start = min(cursor, total_chars)
            end = min(start + len(chunk_text), total_chars)
        else:
            end = min(start + len(chunk_text), total_chars)
        paragraph_index = _paragraph_index_for_position(spans, start)
        raw_items.append(
            {
                "char_start": max(start, 0),
                "char_end": max(end, 0),
                "paragraph_index": paragraph_index,
            }
        )
        cursor = end

    next_milestone = 0
    metadata: list[NavigationMeta] = []
    for index, item in enumerate(raw_items):
        previous_item = raw_items[index - 1] if index > 0 else None
        next_item = raw_items[index + 1] if index + 1 < len(raw_items) else None
        progress_ratio = _clamp_ratio(item["char_end"], total_chars)
        progress_percent = _progress_percent(progress_ratio)
        is_paragraph_start = (
            previous_item is None
            or item["paragraph_index"] != previous_item["paragraph_index"]
        )
        is_paragraph_end = (
            next_item is None
            or item["paragraph_index"] != next_item["paragraph_index"]
        )
        crossed_threshold = progress_percent >= next_milestone
        is_progress_milestone = is_paragraph_start or crossed_threshold
        if crossed_threshold:
            next_milestone = min(100, ((progress_percent // 5) + 1) * 5)

        metadata.append(
            NavigationMeta(
                char_start=item["char_start"],
                char_end=item["char_end"],
                char_count_total=total_chars,
                progress_ratio=progress_ratio,
                progress_percent=progress_percent,
                paragraph_index=max(item["paragraph_index"], 0),
                is_paragraph_start=is_paragraph_start,
                is_paragraph_end=is_paragraph_end,
                is_progress_milestone=is_progress_milestone,
            )
        )
    return metadata


def _paragraph_spans(normalized_text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    cursor = 0
    for paragraph in split_paragraphs(normalized_text):
        start = normalized_text.find(paragraph, cursor)
        if start < 0:
            continue
        end = start + len(paragraph)
        spans.append((start, end))
        cursor = end
    return spans or [(0, max(len(normalized_text), 0))]


def _paragraph_index_for_position(
    spans: list[tuple[int, int]],
    position: int,
) -> int:
    for index, (start, end) in enumerate(spans):
        if start <= position < end:
            return index
    return 0


def _clamp_ratio(char_end: int, total_chars: int) -> float:
    if total_chars <= 0:
        return 0.0
    return min(max(char_end / total_chars, 0.0), 1.0)


def _progress_percent(progress_ratio: float) -> int:
    return min(max(int(progress_ratio * 100), 0), 100)
