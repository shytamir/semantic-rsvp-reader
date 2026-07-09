def test_ingest_rejects_empty_text(client):
    response = client.post("/api/ingest", json={"text": "   "})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_ingest_rejects_missing_json_object(client):
    response = client.post("/api/ingest", data="not json", content_type="text/plain")

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_ingest_returns_normalized_text_and_sentences(client):
    response = client.post(
        "/api/ingest",
        json={"text": "  Hello   world.\r\nDr. Smith agrees!  "},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["normalized_text"] == "Hello world.\nDr. Smith agrees!"
    assert payload["sentences"] == ["Hello world.", "Dr. Smith agrees!"]
    assert payload["sentence_count"] == 2
