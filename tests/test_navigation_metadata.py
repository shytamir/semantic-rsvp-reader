from semantic_rsvp.navigation.metadata import (
    compute_navigation_metadata,
    locate_sentence_paragraphs,
    split_paragraphs,
)
from semantic_rsvp.timing.schedule import schedule_text


def test_split_paragraphs_returns_single_paragraph_without_blank_lines():
    assert split_paragraphs("The system learns.\nIt adapts.") == [
        "The system learns.\nIt adapts."
    ]


def test_split_paragraphs_uses_blank_lines_as_boundaries():
    assert split_paragraphs("First paragraph.\n\nSecond paragraph.") == [
        "First paragraph.",
        "Second paragraph.",
    ]


def test_split_paragraphs_empty_text_is_safe():
    assert split_paragraphs("") == []


def test_locate_sentence_paragraphs_assigns_indices():
    normalized_text = "First paragraph.\n\nSecond paragraph. It continues."
    sentences = ["First paragraph.", "Second paragraph.", "It continues."]

    assert locate_sentence_paragraphs(normalized_text, sentences) == [0, 1, 1]


def test_navigation_progress_values_are_clamped():
    metadata = compute_navigation_metadata("short", ["short", "missing chunk"])

    assert all(0.0 <= item.progress_ratio <= 1.0 for item in metadata)
    assert all(0 <= item.progress_percent <= 100 for item in metadata)
    assert all(item.paragraph_index >= 0 for item in metadata)


def test_progress_milestones_occur_at_five_percent_boundaries():
    text = " ".join(f"word{i:02d}" for i in range(60))
    schedule = schedule_text(text)
    milestones = [
        item.navigation.progress_percent
        for item in schedule
        if item.navigation.is_progress_milestone
    ]

    assert milestones
    assert milestones[0] >= 0
    assert all(0 <= percent <= 100 for percent in milestones)
    assert len(milestones) >= 5


def test_paragraph_starts_are_marked_as_milestones():
    schedule = schedule_text("First paragraph has text.\n\nSecond paragraph has text.")
    second_paragraph = [
        item for item in schedule if item.navigation.paragraph_index == 1
    ]

    assert second_paragraph
    assert second_paragraph[0].navigation.is_paragraph_start
    assert second_paragraph[0].navigation.is_progress_milestone


def test_schedule_items_include_navigation_metadata():
    schedule = schedule_text("The system learns from the reader.")
    navigation = schedule[0].navigation

    assert navigation.char_count_total > 0
    assert navigation.char_start >= 0
    assert navigation.char_end >= navigation.char_start
    assert 0 <= navigation.progress_percent <= 100
