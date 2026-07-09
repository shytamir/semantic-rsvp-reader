def test_schedule_rejects_empty_text(client):
    response = client.post("/api/schedule", json={"text": "   "})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_schedule_rejects_missing_json_body(client):
    response = client.post("/api/schedule", data="not json", content_type="text/plain")

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_schedule_rejects_non_string_text(client):
    response = client.post("/api/schedule", json={"text": 123})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_schedule_returns_valid_json_for_normal_text(client):
    response = client.post(
        "/api/schedule",
        json={"text": "The system learns from the reader. It adapts slowly."},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert "schedule" in payload
    assert payload["chunk_count"] == len(payload["schedule"])
    assert payload["sentence_count"] == 2
    assert payload["chunk_count"] > 0


def test_schedule_items_include_required_fields(client):
    response = client.post(
        "/api/schedule",
        json={"text": "The system learns from the reader."},
    )

    item = response.get_json()["schedule"][0]
    assert set(item) == {
        "index",
        "sentence_index",
        "text",
        "content_word_count",
        "char_length",
        "syntactic_hint",
        "duration_ms",
    }


def test_schedule_accepts_simple_timing_config(client):
    response = client.post(
        "/api/schedule",
        json={"text": "The system learns.", "base_beat_ms": 500},
    )

    assert response.status_code == 200
    assert response.get_json()["schedule"][0]["duration_ms"] >= 500


def test_schedule_rejects_invalid_timing_config(client):
    response = client.post(
        "/api/schedule",
        json={"text": "The system learns.", "base_beat_ms": "fast"},
    )

    assert response.status_code == 400
    assert "error" in response.get_json()
