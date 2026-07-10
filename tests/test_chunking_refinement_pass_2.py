from semantic_rsvp.chunking.rules import RuleBasedChunker, tokenize


def chunk_texts(sentence: str) -> list[str]:
    return [chunk.text for chunk in RuleBasedChunker().chunk_sentence(sentence)]


def test_air_force_one_stays_together_from_observed_report():
    chunks = chunk_texts(
        "The temporary plane did not have all the equipment usually found on an Air Force One."
    )

    assert any("Air Force One" in chunk for chunk in chunks)
    assert "an Air Force" not in chunks
    assert "One." not in chunks


def test_repeated_air_force_entities_stay_recognizable():
    chunks = chunk_texts(
        "Two former Air Force officials were involved with the older Air Force One planes."
    )

    assert any("Air Force officials" in chunk for chunk in chunks)
    assert any("Air Force One" in chunk for chunk in chunks)
    assert not any(chunk.startswith("Force") for chunk in chunks)


def test_observed_compact_proper_names_stay_together():
    examples = [
        ("President Trump talked to reporters.", "President Trump"),
        ("Mr. Trump attended a NATO summit.", "Mr. Trump"),
        ("Dr. Kudrenko said the result was clear.", "Dr. Kudrenko"),
        ("The New Hampshire Legislature approved an amendment.", "New Hampshire Legislature"),
        ("The article cited Dartmouth College and Williams College.", "Dartmouth College"),
        ("The article cited Dartmouth College and Williams College.", "Williams College"),
        ("Explosions were reported near Bandar Abbas.", "Bandar Abbas"),
    ]

    for sentence, expected in examples:
        chunks = chunk_texts(sentence)
        assert any(expected in chunk for chunk in chunks), chunks


def test_title_and_religious_leader_names_from_observed_report():
    chunks = chunk_texts(
        "Iran buried its slain Supreme Leader Ayatollah Ali Khamenei at a shrine in Mashhad."
    )

    assert "Supreme Leader" in chunks
    assert "Ayatollah Ali Khamenei" in chunks
    assert not any(chunk.startswith("Leader") for chunk in chunks)
    assert not any(chunk.startswith("Ali Khamenei at") for chunk in chunks)


def test_multiword_media_and_military_names_from_observed_report():
    chunks = chunk_texts(
        "Iran's Revolutionary Guards Navy reopened shipping through the Strait of Hormuz."
    )

    assert "Iran's Revolutionary Guards Navy" in chunks
    assert any("Strait of Hormuz" in chunk for chunk in chunks)


def test_curly_contractions_and_possessives_do_not_orphan_suffixes():
    assert "didn\u2019t" in tokenize("Time didn\u2019t permit all changes.")
    assert "Trump\u2019s" in tokenize("Trump\u2019s personal comfort mattered.")

    chunks = chunk_texts("Time didn\u2019t permit all the normal modifications.")
    assert not any(chunk.startswith("t ") for chunk in chunks)

    chunks = chunk_texts("Trump\u2019s personal comfort mattered.")
    assert not any(chunk.startswith("s ") for chunk in chunks)


def test_preposition_led_noun_phrases_avoid_weak_two_word_chunks():
    chunks = chunk_texts(
        "The procession included a week of funeral processions and rallies."
    )

    assert "of funeral" not in chunks
    assert "of funeral processions" in chunks


def test_definite_article_modifier_head_stays_together():
    chunks = chunk_texts("The reader noticed the current model immediately.")

    assert "the current model" in chunks
    assert "the current" not in chunks
