from semantic_rsvp.validation_samples import load_validation_samples

EXPECTED_IDS = [
    "DN-001",
    "TS-001",
    "PA-001",
    "NP-001",
    "NF-001",
    "AE-001",
]


def test_validation_samples_load_from_corpus():
    samples = load_validation_samples()

    assert [sample["id"] for sample in samples] == EXPECTED_IDS
    assert all(sample["text"] for sample in samples)
    assert all(sample["category"] for sample in samples)
    assert all(sample["purpose"] for sample in samples)
    assert all(sample["expected_difficulty"] for sample in samples)


def test_validation_samples_keep_manual_reading_length():
    samples = load_validation_samples()

    for sample in samples:
        word_count = len(sample["text"].split())
        assert 180 <= word_count <= 520, sample["id"]


def test_validation_samples_preserve_edge_case_coverage():
    text_by_id = {sample["id"]: sample["text"] for sample in load_validation_samples()}

    assert '"' in text_by_id["DN-001"]
    assert ";" in text_by_id["DN-001"]
    assert "interoperability" in text_by_id["TS-001"]
    assert "hesitate" in text_by_id["PA-001"]
    assert "7 a.m." in text_by_id["NP-001"]
    assert "7:18 a.m." in text_by_id["NP-001"]
    assert "U.S." in text_by_id["NF-001"]
    assert "Sept. 3" in text_by_id["NF-001"]
    assert "trade-off" in text_by_id["AE-001"]


def test_validation_samples_endpoint_returns_samples(client):
    response = client.get("/api/validation-samples")

    assert response.status_code == 200
    payload = response.get_json()
    assert len(payload["samples"]) == 6
    assert payload["samples"][0]["id"] == "DN-001"
