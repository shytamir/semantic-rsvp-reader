from semantic_rsvp.chunking.rules import RuleBasedChunker


def chunk_texts(sentence: str) -> list[str]:
    return [chunk.text for chunk in RuleBasedChunker().chunk_sentence(sentence)]


def test_article_adjective_noun_unit_from_observed_report_stays_together():
    chunks = chunk_texts(
        "This is why a paragraph can feel easy when read in a quiet room and nearly impossible on a train."
    )

    assert "a quiet room" in chunks
    assert "room and nearly" not in chunks


def test_connector_therefore_starts_new_chunk_after_compound_noun():
    chunks = chunk_texts("A reading tool therefore has to respect two different forms of effort.")

    assert "A reading tool" in chunks
    assert not any(chunk.startswith("tool therefore") for chunk in chunks)


def test_infinitive_marker_stays_with_following_verb_when_possible():
    chunks = chunk_texts(
        "The surrounding interruptions keep asking to be noticed."
    )

    assert "to be noticed." in chunks
    assert "asking to" not in chunks


def test_modal_negation_does_not_become_underdense_chunk():
    chunks = chunk_texts(
        "If normalization removes too much punctuation, the segmenter may not know where the writer changed direction."
    )

    assert "too much punctuation," in chunks
    assert "may not" not in chunks
    assert any("may not know" in chunk for chunk in chunks)


def test_negation_stays_with_governed_verb_from_observed_report():
    chunks = chunk_texts("This is why validation should not begin with a large automated benchmark.")

    assert any("not begin" in chunk for chunk in chunks)
    assert "not" not in chunks


def test_quotes_attach_to_enclosed_phrase_start():
    chunks = chunk_texts(
        'A phrase such as "not because the evidence is weak, but because the explanation is incomplete" asks the reader.'
    )

    assert 'such as "' not in chunks
    assert any(chunk.startswith('"not because') for chunk in chunks)
    assert not any(chunk.startswith('"asks') for chunk in chunks)


def test_clear_connectors_can_stand_alone_to_preserve_dense_phrase():
    chunks = chunk_texts(
        'The failures are likely to be qualitative: a chunk that begins with "however," a pause after a phrase that should flow, or a dense definition that disappears too quickly.'
    )

    assert "or" in chunks
    assert "a dense definition" in chunks
    assert "or a dense" not in chunks


def test_colon_and_semicolon_create_clean_boundaries():
    chunks = chunk_texts(
        "The material does not simply enter the mind; it must be held long enough for relationships to become visible."
    )

    assert any(chunk.endswith("mind;") for chunk in chunks)
    assert not any(chunk.startswith(";") or chunk.startswith(":") for chunk in chunks)


def test_whether_modal_clause_splits_before_modal_after_subject():
    chunks = chunk_texts("The question is whether leaving would change the result.")

    assert "whether" not in chunks
    assert "whether leaving would" not in chunks
    assert "whether leaving" in chunks
    assert any(chunk.startswith("would change") for chunk in chunks)


def test_whether_system_would_preserves_context_without_modal_orphan():
    chunks = chunk_texts("They asked whether the system would preserve context.")

    assert "whether" not in chunks
    assert "would" not in chunks
    assert "whether the system" in chunks
    assert any(chunk.startswith("would preserve") for chunk in chunks)


def test_may_not_know_whether_keeps_negation_and_starts_clause_cleanly():
    chunks = chunk_texts("The model may not know whether leaving would help.")

    assert "may not know" in chunks
    assert "whether leaving would" not in chunks
    assert "whether leaving" in chunks
    assert any(chunk.startswith("would help") for chunk in chunks)
