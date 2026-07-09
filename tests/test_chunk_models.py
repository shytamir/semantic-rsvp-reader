from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.chunking.rules import RuleBasedChunker


def test_chunk_stores_expected_fields():
    chunk = Chunk(
        text="The system",
        content_word_count=1,
        char_length=10,
        syntactic_hint="normal",
    )

    assert chunk.text == "The system"
    assert chunk.content_word_count == 1
    assert chunk.char_length == 10
    assert chunk.syntactic_hint == "normal"


def test_chunker_sets_char_length_from_text_length():
    chunk = RuleBasedChunker().chunk_sentence("The system learns.")[0]

    assert chunk.char_length == len(chunk.text)
