import pytest

from semantic_rsvp.chunking.rules import (
    RuleBasedChunker,
    count_content_words,
    is_stopword,
    tokenize,
)


def test_tokenize_simple_words():
    assert tokenize("The system learns") == ["The", "system", "learns"]


def test_tokenize_commas_and_periods():
    assert tokenize("Hello, world.") == ["Hello", ",", "world", "."]


def test_tokenize_keeps_simple_contractions_together():
    assert tokenize("Don't split what isn't broken.") == [
        "Don't",
        "split",
        "what",
        "isn't",
        "broken",
        ".",
    ]


def test_tokenize_returns_no_empty_tokens():
    assert "" not in tokenize("  Hello,   world.  ")


def test_stopword_and_content_word_count_helpers():
    assert is_stopword("the")
    assert is_stopword("The")
    assert not is_stopword("reader")
    assert count_content_words(["The", "system", "learns"]) == 2


def test_chunks_simple_sentence_with_natural_punctuation():
    chunks = RuleBasedChunker().chunk_sentence("The system learns from the reader.")

    assert [chunk.text for chunk in chunks] == [
        "The system",
        "learns from",
        "the reader.",
    ]


def test_chunks_dense_nonfiction_sentence():
    chunks = RuleBasedChunker().chunk_sentence(
        "Modern AI systems are moving beyond sealed text generators."
    )

    assert [chunk.text for chunk in chunks] == [
        "Modern AI",
        "systems are moving",
        "beyond sealed",
        "text generators.",
    ]


def test_chunks_one_sentence_at_a_time():
    chunks = RuleBasedChunker().chunk_sentence("That is not only a memory problem.")

    assert [chunk.text for chunk in chunks] == [
        "That is not",
        "only a memory",
        "problem.",
    ]


def test_content_word_limit_is_respected_unless_unavoidable_long_token():
    chunker = RuleBasedChunker(max_content_words=1)
    chunks = chunker.chunk_sentence("Alpha beta gamma.")

    assert [chunk.content_word_count for chunk in chunks] == [1, 1, 1]


def test_char_limit_is_respected_unless_single_token_is_too_long():
    chunker = RuleBasedChunker(max_chars=12)
    chunks = chunker.chunk_sentence("Short words fit supercalifragilistic.")

    assert [chunk.text for chunk in chunks] == [
        "Short words",
        "fit",
        "supercalifragilistic.",
    ]
    assert len(chunks[-1].text) > 12
    assert all(len(chunk.text) <= 12 for chunk in chunks[:-1])


def test_punctuation_attaches_naturally():
    chunks = RuleBasedChunker().chunk_sentence("Hello, world.")

    assert [chunk.text for chunk in chunks] == ["Hello,", "world."]


def test_empty_input_returns_empty_list():
    assert RuleBasedChunker().chunk_sentence("   ") == []


def test_output_is_deterministic_across_repeated_calls():
    chunker = RuleBasedChunker()
    sentence = "The system learns from the reader."

    first = chunker.chunk_sentence(sentence)
    second = chunker.chunk_sentence(sentence)

    assert first == second


def test_invalid_limits_raise_clear_errors():
    with pytest.raises(ValueError, match="max_chars"):
        RuleBasedChunker(max_chars=0)
    with pytest.raises(ValueError, match="max_content_words"):
        RuleBasedChunker(max_content_words=0)
