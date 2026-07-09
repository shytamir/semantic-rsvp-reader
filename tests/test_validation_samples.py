from semantic_rsvp.validation_samples import load_validation_samples


def test_validation_samples_load_from_corpus():
    samples = load_validation_samples()

    assert [sample["id"] for sample in samples] == [
        "DN-001",
        "TS-001",
        "PA-001",
        "NP-001",
        "NF-001",
        "AE-001",
    ]
    assert all(sample["text"] for sample in samples)
    assert all(sample["category"] for sample in samples)


def test_validation_samples_endpoint_returns_samples(client):
    response = client.get("/api/validation-samples")

    assert response.status_code == 200
    payload = response.get_json()
    assert len(payload["samples"]) == 6
    assert payload["samples"][0]["id"] == "DN-001"
