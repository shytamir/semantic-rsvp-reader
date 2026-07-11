from semantic_rsvp.application import schedule_service
from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.timing.models import TimingConfig


class StubChunker:
    def __init__(self):
        self.sentences = []

    def chunk_sentence(self, sentence):
        self.sentences.append(sentence)
        return [Chunk(sentence, 1, len(sentence), "stub")]


def test_schedule_service_generates_schedule_without_flask():
    chunker = StubChunker()
    service = ScheduleService(chunker=chunker)

    result = service.generate(" First sentence. Second sentence. ")

    assert result.normalized_text == "First sentence. Second sentence."
    assert result.sentences == ("First sentence.", "Second sentence.")
    assert chunker.sentences == ["First sentence.", "Second sentence."]
    assert [scheduled.chunk.text for scheduled in result.schedule] == [
        "First sentence.",
        "Second sentence.",
    ]


def test_schedule_service_normalizes_and_segments_once(monkeypatch):
    calls = {"normalize": 0, "segment": 0}

    def fake_normalize(raw_text):
        calls["normalize"] += 1
        return "One sentence."

    def fake_split(normalized_text):
        calls["segment"] += 1
        return ["One sentence."]

    monkeypatch.setattr(schedule_service, "normalize_text", fake_normalize)
    monkeypatch.setattr(schedule_service, "split_sentences", fake_split)

    service = ScheduleService(chunker=StubChunker())
    result = service.generate("ignored")

    assert calls == {"normalize": 1, "segment": 1}
    assert result.sentences == ("One sentence.",)


def test_schedule_service_accepts_stub_chunker_and_preserves_schedule_semantics():
    chunker = StubChunker()
    service = ScheduleService(chunker=chunker)

    result = service.generate(
        '# Main\n\nThe pilot said, "Ready."',
        timing_config=TimingConfig(base_beat_ms=500),
    )

    assert len(result.schedule) == 2
    scheduled = result.schedule[1]
    assert scheduled.index == 1
    assert scheduled.sentence_index == 1
    assert scheduled.duration_ms >= 500
    assert scheduled.navigation.progress_percent == 100
    assert scheduled.structure.active_h1 == "Main"
    assert scheduled.display_state.quote_boundary in {"open", "close", "both", None}
