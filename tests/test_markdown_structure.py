from semantic_rsvp.navigation.metadata import compute_navigation_metadata
from semantic_rsvp.structure.markdown_headers import (
    compute_structure_metadata,
    detect_markdown_headers,
)


def structure_for_text(text: str):
    chunk_texts = [
        chunk
        for chunk in text.replace("\n\n", "\n").split("\n")
        if chunk.strip()
    ]
    navigation = compute_navigation_metadata(text, chunk_texts)
    return compute_structure_metadata(text, navigation)


def test_detects_h1_header():
    headers = detect_markdown_headers("# Title\nBody text.")

    assert len(headers) == 1
    assert headers[0].level == 1
    assert headers[0].text == "Title"


def test_detects_h2_header():
    headers = detect_markdown_headers("## Section\nBody text.")

    assert len(headers) == 1
    assert headers[0].level == 2
    assert headers[0].text == "Section"


def test_requires_space_after_hash():
    assert detect_markdown_headers("#Not a header\nBody text.") == []


def test_ignores_h3_for_this_slice():
    assert detect_markdown_headers("### Too deep\nBody text.") == []


def test_tracks_h1_then_h2_context():
    structures = structure_for_text("# Title\n\nIntro.\n\n## Section\n\nBody.")

    assert structures[1].active_h1 == "Title"
    assert structures[1].active_label == "Title"
    assert structures[-1].active_h1 == "Title"
    assert structures[-1].active_h2 == "Section"
    assert structures[-1].active_label == "Section"
    assert structures[-1].active_path == ("Title", "Section")


def test_text_before_first_header_has_no_active_label():
    structures = structure_for_text("Intro.\n\n# Title\n\nBody.")

    assert structures[0].active_label is None
    assert structures[0].active_path == ()
    assert structures[-1].active_label == "Title"


def test_consecutive_h2_sections_update_active_h2():
    structures = structure_for_text("# Title\n\n## First\n\nA.\n\n## Second\n\nB.")

    assert structures[2].active_h2 == "First"
    assert structures[-1].active_h2 == "Second"
    assert structures[-1].active_label == "Second"


def test_new_h1_clears_previous_h2():
    structures = structure_for_text("# First\n\n## Child\n\nA.\n\n# Second\n\nB.")

    assert structures[2].active_h2 == "Child"
    assert structures[-1].active_h1 == "Second"
    assert structures[-1].active_h2 is None
    assert structures[-1].active_label == "Second"
