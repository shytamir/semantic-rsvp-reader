from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.timing.schedule import build_schedule, schedule_text


def test_empty_sentence_list_returns_empty_schedule():
    assert build_schedule([]) == []


def test_sentence_order_is_preserved():
    schedule = build_schedule(["The system learns.", "It adapts slowly."])

    assert schedule[0].sentence_index == 0
    assert schedule[-1].sentence_index == 1


def test_chunk_order_is_preserved():
    schedule = build_schedule(["The system learns from the reader."])

    assert [item.chunk.text for item in schedule] == [
        "The system",
        "learns from",
        "the reader.",
    ]


def test_indices_are_monotonic():
    schedule = build_schedule(["The system learns.", "It adapts slowly."])

    assert [item.index for item in schedule] == list(range(len(schedule)))


def test_sentence_indices_are_correct():
    schedule = build_schedule(["The system learns.", "It adapts slowly."])

    assert {item.sentence_index for item in schedule} == {0, 1}


def test_default_chunker_works():
    schedule = build_schedule(["The system learns from the reader."])

    assert len(schedule) == 3
    assert all(item.duration_ms > 0 for item in schedule)


def test_custom_chunker_can_be_supplied():
    chunker = RuleBasedChunker(max_content_words=1)
    schedule = build_schedule(["Alpha beta."], chunker=chunker)

    assert [item.chunk.text for item in schedule] == ["Alpha", "beta."]


def test_schedule_generation_is_deterministic():
    sentences = ["The system learns from the reader.", "It adapts slowly."]

    assert build_schedule(sentences) == build_schedule(sentences)


def test_schedule_text_normalizes_segments_chunks_and_times():
    schedule = schedule_text(" The system learns.\r\nIt adapts slowly. ")

    assert [item.sentence_index for item in schedule] == [0, 0, 1, 1]
    assert all(item.duration_ms > 0 for item in schedule)
