from dataclasses import FrozenInstanceError

import pytest

from semantic_rsvp.application.source_document import SourceDocument


def test_source_document_has_deterministic_identity_structure_and_bounded_provenance():
    first = SourceDocument.from_text(
        "# Main\r\n\r\nText.",
        source_type="markdown",
        provenance={"name": "sample.md", "origin": "local_file"},
    )
    second = SourceDocument.from_text(
        "# Main\n\nText.",
        source_type="markdown",
        provenance={"origin": "another_import", "name": "renamed.md"},
    )

    assert first.document_id == second.document_id
    assert first.source_type == "markdown"
    assert first.text == "# Main\r\n\r\nText."
    assert [(item.level, item.text) for item in first.structure] == [(1, "Main")]
    assert first.provenance == (("name", "sample.md"), ("origin", "local_file"))
    with pytest.raises(FrozenInstanceError):
        first.text = "changed"


def test_source_document_identity_includes_source_type():
    plain = SourceDocument.from_text("Text.", source_type="plain_text")
    markdown = SourceDocument.from_text("Text.", source_type="markdown")

    assert plain.document_id != markdown.document_id


def test_source_document_rejects_unbounded_provenance():
    with pytest.raises(ValueError, match="at most 8 fields"):
        SourceDocument.from_text(
            "Text.",
            provenance={f"field-{index}": "value" for index in range(9)},
        )
