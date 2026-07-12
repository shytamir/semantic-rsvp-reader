from semantic_rsvp.web import create_app


def _assert_json_native(value):
    if value is None or isinstance(value, (bool, int, float, str)):
        return
    if isinstance(value, list):
        for item in value:
            _assert_json_native(item)
        return
    assert isinstance(value, dict)
    assert all(isinstance(key, str) for key in value)
    for item in value.values():
        _assert_json_native(item)


def test_standard_profile_api_contracts_use_real_pinned_parser_and_json_records():
    app = create_app({"TESTING": True})
    client = app.test_client()

    health = client.get("/health")
    assert health.status_code == 200
    assert health.get_json()["chunking"]["configured_mode"] == "parser_assisted"
    assert health.get_json()["chunking"]["provider_available"] is True

    ingest = client.post(
        "/api/ingest",
        json={"text": "The system learns from the reader. It adapts slowly."},
    )
    chunk = client.post(
        "/api/chunk",
        json={"sentence": "The system learns from the reader."},
    )
    schedule = client.post(
        "/api/schedule",
        json={"text": "The system learns from the reader. It adapts slowly."},
    )
    defect = client.post("/api/defects", json={"category": "bad_chunk_split"})

    assert ingest.status_code == 200
    assert set(ingest.get_json()) == {
        "normalized_text",
        "sentences",
        "sentence_count",
        "chunked_sentences",
    }
    assert ingest.get_json()["sentence_count"] == 2
    assert ingest.get_json()["chunked_sentences"]

    assert chunk.status_code == 200
    assert set(chunk.get_json()) == {"chunks", "chunk_count"}
    assert chunk.get_json()["chunk_count"] == len(chunk.get_json()["chunks"])
    assert set(chunk.get_json()["chunks"][0]) == {
        "text",
        "content_word_count",
        "char_length",
        "syntactic_hint",
    }

    assert schedule.status_code == 200
    assert set(schedule.get_json()) == {
        "schedule",
        "chunk_count",
        "sentence_count",
        "sentences",
    }
    assert schedule.get_json()["chunk_count"] == len(schedule.get_json()["schedule"])
    assert set(schedule.get_json()["schedule"][0]) == {
        "index",
        "sentence_index",
        "text",
        "content_word_count",
        "char_length",
        "syntactic_hint",
        "duration_ms",
        "in_quote",
        "quote_boundary",
        "in_parenthetical",
        "parenthetical_depth",
        "navigation",
        "structure",
    }

    assert defect.status_code == 400
    assert set(defect.get_json()) == {"error"}
    for response in (health, ingest, chunk, schedule, defect):
        _assert_json_native(response.get_json())


def test_standard_profile_post_only_apis_reject_get_with_405():
    client = create_app({"TESTING": True}).test_client()

    for path in ("/api/ingest", "/api/chunk", "/api/schedule", "/api/defects"):
        response = client.get(path)
        assert response.status_code == 405
