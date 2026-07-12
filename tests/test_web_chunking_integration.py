import pytest

from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.chunking.models import Chunk
from semantic_rsvp.web import create_app


class StubChunker:
    def chunk_sentence(self, sentence):
        return [Chunk(sentence, 1, len(sentence), "injected")]


def test_app_creation_uses_parser_assisted_default():
    app = create_app({"TESTING": True})

    assert app.config["RSVP_CHUNKER_MODE"] == "parser_assisted"
    assert app.config["CHUNKING_STATE"].configured_mode == "parser_assisted"


def test_app_creation_rejects_invalid_chunker_mode():
    with pytest.raises(ValueError, match="Invalid RSVP_CHUNKER_MODE"):
        create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "client_choice"})


def test_health_retains_status_and_reports_chunking_state():
    app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "rule_based"})
    response = app.test_client().get("/health")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert payload["chunking"]["configured_mode"] == "rule_based"
    assert payload["chunking"]["fallback"] == "rule_based"


def test_health_does_not_load_spacy_model(monkeypatch):
    def fail_load():
        raise AssertionError("health should not load the spaCy model")

    monkeypatch.setattr(
        "semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter._load_pipeline",
        fail_load,
    )

    app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "parser_assisted"})
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json()["chunking"]["configured_mode"] == "parser_assisted"


def test_text_processing_endpoints_use_configured_service():
    app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "rule_based"})
    client = app.test_client()

    ingest = client.post("/api/ingest", json={"text": "The system learns."})
    chunk = client.post("/api/chunk", json={"sentence": "The system learns."})
    schedule = client.post("/api/schedule", json={"text": "The system learns."})

    assert ingest.status_code == 200
    assert chunk.status_code == 200
    assert schedule.status_code == 200
    assert ingest.get_json()["chunked_sentences"][0]["chunks"][0]["text"] == "The system"
    assert chunk.get_json()["chunks"][0]["text"] == "The system"
    assert schedule.get_json()["schedule"][0]["text"] == "The system"


def test_routes_accept_substituted_schedule_service():
    app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "rule_based"})
    app.config["SCHEDULE_SERVICE"] = ScheduleService(chunker=StubChunker())

    response = app.test_client().post("/api/chunk", json={"sentence": "Injected."})

    assert response.status_code == 200
    assert response.get_json()["chunks"][0]["syntactic_hint"] == "injected"


def test_default_parser_assisted_app_schedules_when_provider_is_unavailable(monkeypatch):
    monkeypatch.setattr(
        "semantic_rsvp.chunking.selection.provider_availability",
        lambda: (False, "spacy_unavailable"),
    )
    monkeypatch.setattr(
        "semantic_rsvp.experiments.parser_assisted_chunking.spacy_adapter.availability",
        lambda: (False, "spacy_unavailable"),
    )
    monkeypatch.setattr(
        "semantic_rsvp.experiments.parser_assisted_chunking.chunker.availability",
        lambda: (False, "spacy_unavailable"),
    )
    app = create_app({"TESTING": True, "RSVP_CHUNKER_MODE": "parser_assisted"})

    response = app.test_client().post(
        "/api/schedule",
        json={"text": "The system learns from the reader."},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["chunk_count"] > 0
    assert [item["text"] for item in payload["schedule"]][:3] == [
        "The system",
        "learns from",
        "the reader.",
    ]
