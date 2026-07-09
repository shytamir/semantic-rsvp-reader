import pytest

from semantic_rsvp.text.normalize import normalize_text


def test_repeated_spaces_and_tabs_are_collapsed():
    assert normalize_text("One   two\t\tthree") == "One two three"


def test_windows_line_endings_are_normalized():
    assert normalize_text("One\r\nTwo\rThree") == "One\nTwo\nThree"


def test_leading_and_trailing_whitespace_is_trimmed():
    assert normalize_text("  \n  Hello world.  \n ") == "Hello world."


def test_unicode_is_normalized_to_nfc():
    assert normalize_text("Cafe\u0301") == "Caf\u00e9"


def test_excessive_blank_lines_are_collapsed():
    assert normalize_text("One\n\n\n\nTwo") == "One\n\nTwo"


def test_non_string_input_raises_clear_exception():
    with pytest.raises(TypeError, match="expects a string"):
        normalize_text(None)
