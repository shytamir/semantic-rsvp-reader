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
    assert payload["sentences"] == [
        "The system learns from the reader.",
        "It adapts slowly.",
    ]
    assert len(payload["sentences"]) == payload["sentence_count"]
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
        "in_quote",
        "quote_boundary",
        "in_parenthetical",
        "parenthetical_depth",
        "navigation",
    }


def test_schedule_items_include_navigation_metadata(client):
    response = client.post(
        "/api/schedule",
        json={"text": "The system learns from the reader."},
    )

    assert response.status_code == 200
    item = response.get_json()["schedule"][0]
    navigation = item["navigation"]
    assert "progress_percent" in navigation
    assert "paragraph_index" in navigation
    assert 0 <= navigation["progress_percent"] <= 100
    assert navigation["paragraph_index"] == 0


def test_schedule_items_include_quote_and_parenthetical_state(client):
    response = client.post(
        "/api/schedule",
        json={"text": 'The pilot said, "Air Force One is ready." It paused (briefly).'},
    )

    assert response.status_code == 200
    schedule = response.get_json()["schedule"]
    assert any(item["in_quote"] for item in schedule)
    assert any(item["quote_boundary"] in {"open", "close", "both"} for item in schedule)
    assert any(item["in_parenthetical"] for item in schedule)
    assert all(item["parenthetical_depth"] >= 0 for item in schedule)


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
