def test_chunk_rejects_empty_sentence(client):
    response = client.post("/api/chunk", json={"sentence": "   "})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_chunk_returns_chunks_for_valid_sentence(client):
    response = client.post(
        "/api/chunk",
        json={"sentence": "The system learns from the reader."},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["chunk_count"] == 3
    assert [chunk["text"] for chunk in payload["chunks"]] == [
        "The system",
        "learns from",
        "the reader.",
    ]
