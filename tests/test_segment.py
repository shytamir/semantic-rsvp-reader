from semantic_rsvp.text.segment import split_sentences


def test_simple_sentence_splitting():
    assert split_sentences("One sentence. Another sentence.") == [
        "One sentence.",
        "Another sentence.",
    ]


def test_questions_and_exclamations_split():
    assert split_sentences("Ready? Go! Done.") == ["Ready?", "Go!", "Done."]


def test_common_abbreviations_do_not_split_sentences():
    assert split_sentences("Dr. Smith used e.g. examples. Ms. Jones listened.") == [
        "Dr. Smith used e.g. examples.",
        "Ms. Jones listened.",
    ]


def test_ellipses_are_preserved_and_can_end_sentence():
    assert split_sentences("Wait... Then continue.") == ["Wait...", "Then continue."]


def test_empty_results_are_ignored():
    assert split_sentences("   \n\n  ") == []
