from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.text.segment import split_sentences


def chunk_texts(sentence: str) -> list[str]:
    return [chunk.text for chunk in RuleBasedChunker().chunk_sentence(sentence)]


def test_source_title_byline_date_boundaries_from_observed_report_are_preserved():
    text = (
        "The End of War Without the End of Power\n"
        "Toward a Global Security System Built on Economic Deterrence\n"
        "Alex\n"
        "Apr 02, 2026\n\n"
        "There is a persistent mistake in how we imagine peace."
    )

    assert split_sentences(text) == [
        "The End of War Without the End of Power",
        "Toward a Global Security System Built on Economic Deterrence",
        "Alex",
        "Apr 02, 2026",
        "There is a persistent mistake in how we imagine peace.",
    ]


def test_long_form_dates_stay_coherent_and_do_not_merge_into_body_prose():
    sentences = split_sentences("July 4, 2026\nInherent in the peace talks are questions.")

    assert sentences == ["July 4, 2026", "Inherent in the peace talks are questions."]
    assert "July 4, 2026" in chunk_texts(sentences[0])
    assert "2026 Inherent" not in chunk_texts(" ".join(sentences))


def test_phrasal_verbs_from_observed_report_stay_together():
    chunks = chunk_texts("During his tenure, he had built up his office into a center.")

    assert "built up" in chunks
    assert "up his" not in chunks


def test_qualifier_pair_from_observed_report_stays_together():
    chunks = chunk_texts("He had far less impressive religious credentials.")

    assert "far less impressive" in chunks
    assert not any(chunk.endswith(" far") for chunk in chunks)


def test_compact_coordinated_form_from_observed_report_stays_together():
    chunks = chunk_texts("He sought balance between Iran's left and right wings.")

    assert any("left and right wings" in chunk for chunk in chunks)
    assert "left" not in chunks
    assert "and right" not in chunks


def test_noun_preposition_phrase_from_observed_report_stays_coherent():
    chunks = chunk_texts("Power projection remains the primary language of international credibility.")

    assert "the primary language" in chunks
    assert "of international credibility." in chunks
    assert "language of international" not in chunks


def test_two_word_person_and_title_phrases_from_observed_report_stay_together():
    chunks = chunk_texts(
        "The divisions were described by Ray Takeyh, a senior fellow at the Council on Foreign Relations."
    )

    assert any("Ray Takeyh" in chunk for chunk in chunks)
    assert "a senior fellow" in chunks
    assert "Council on Foreign Relations." in chunks


def test_underdense_observed_subject_fragment_is_repaired():
    chunks = chunk_texts(
        "Although the two men who led the movement were loyal to the Islamic Revolution, they demanded change."
    )

    assert "men who led" in chunks
    assert "led" not in chunks


def test_overlong_subject_verb_observed_case_can_split_cleanly():
    chunks = chunk_texts("The country will navigate the issue.")

    assert "The country" in chunks
    assert "will navigate" in chunks
    assert "The country will navigate" not in chunks


def test_pass_2_named_entities_and_curly_apostrophes_do_not_regress():
    chunks = chunk_texts(
        "Ayatollah Ali Khamenei met Air Force officials near the Strait of Hormuz."
    )

    assert "Ayatollah Ali Khamenei" in chunks
    assert "Air Force officials" in chunks
    assert any("Strait of Hormuz" in chunk for chunk in chunks)
    assert "didn\u2019t" in chunk_texts("The system didn\u2019t split the contraction.")[1]
