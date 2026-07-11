import hashlib
import json

import pytest

from semantic_rsvp.validation_samples import (
    DEFAULT_MANIFEST_PATHS,
    LONG_FORM_COLLECTION,
    S030_CASE_IDS,
    S030_COLLECTION,
    load_validation_samples,
)

EXPECTED_IDS = [
    "DN-001",
    "TS-001",
    "PA-001",
    "NP-001",
    "NF-001",
    "AE-001",
]
EXPECTED_LONG_FORM_HASHES = {
    "DN-001": "aad7eed894d4700c01d084baa39d98ce8f785df909c34d75d3883453a0ff80aa",
    "TS-001": "a28e4beb9af90925a80fd4b6ad198082f0329a9739415fc971f0e8e28e2ddad3",
    "PA-001": "e5e3801c104b872f70bd513cea5c9b3cb9a461fe1dd1dc83b1bb014aab37eea2",
    "NP-001": "d72477697e0685d542dd98cdb70f35214b64b9746b88ed138a2e3afa9507ef0b",
    "NF-001": "ba9477378293e600b65975efe18f76801bc90ffb8d0bc7f93a3527dffd82ded9",
    "AE-001": "7837b44fbd563c453e1d2b0f3b17a7d1a0e0da57cc37c90d55c26f999de1feb2",
}


def _collection(name):
    return [sample for sample in load_validation_samples() if sample["collection"] == name]


def _manifest_records():
    records = []
    for path in DEFAULT_MANIFEST_PATHS:
        records.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip())
    return [record for record in records if record["case_id"] in S030_CASE_IDS]


def test_validation_samples_load_from_corpus():
    samples = _collection(LONG_FORM_COLLECTION)

    assert [sample["id"] for sample in samples] == EXPECTED_IDS
    assert all(sample["text"] for sample in samples)
    assert all(sample["category"] for sample in samples)
    assert all(sample["purpose"] for sample in samples)
    assert all(sample["expected_difficulty"] for sample in samples)


def test_validation_samples_keep_manual_reading_length():
    samples = _collection(LONG_FORM_COLLECTION)

    for sample in samples:
        word_count = len(sample["text"].split())
        assert 180 <= word_count <= 520, sample["id"]


def test_validation_samples_preserve_edge_case_coverage():
    text_by_id = {sample["id"]: sample["text"] for sample in _collection(LONG_FORM_COLLECTION)}

    assert '"' in text_by_id["DN-001"]
    assert ";" in text_by_id["DN-001"]
    assert "interoperability" in text_by_id["TS-001"]
    assert "hesitate" in text_by_id["PA-001"]
    assert "7 a.m." in text_by_id["NP-001"]
    assert "7:18 a.m." in text_by_id["NP-001"]
    assert "U.S." in text_by_id["NF-001"]
    assert "Sept. 3" in text_by_id["NF-001"]
    assert "trade-off" in text_by_id["AE-001"]


def test_long_form_samples_remain_present_and_unchanged():
    samples = _collection(LONG_FORM_COLLECTION)

    assert [sample["id"] for sample in samples] == EXPECTED_IDS
    assert {
        sample["id"]: hashlib.sha256(sample["text"].encode()).hexdigest()
        for sample in samples
    } == EXPECTED_LONG_FORM_HASHES


def test_s030_cases_are_loadable_in_exact_protocol_order():
    samples = _collection(S030_COLLECTION)

    assert [sample["id"] for sample in samples] == list(S030_CASE_IDS)
    assert all(sample["text"].strip() for sample in samples)
    assert all(sample["source"].startswith("evaluation/parser_assisted_chunking/manifests/") for sample in samples)


def test_s030_text_is_derived_from_manifest_records(tmp_path):
    records = _manifest_records()
    records[0] = {**records[0], "text": "Manifest-derived replacement text."}
    manifest = tmp_path / "visible.jsonl"
    manifest.write_text("\n".join(json.dumps(record) for record in records) + "\n", encoding="utf-8")

    samples = load_validation_samples(manifest_paths=(manifest,))
    s030 = [sample for sample in samples if sample["collection"] == S030_COLLECTION]

    assert s030[0]["id"] == S030_CASE_IDS[0]
    assert s030[0]["text"] == "Manifest-derived replacement text."


def test_missing_required_s030_id_fails_loudly(tmp_path):
    records = [record for record in _manifest_records() if record["case_id"] != S030_CASE_IDS[-1]]
    manifest = tmp_path / "missing.jsonl"
    manifest.write_text("\n".join(json.dumps(record) for record in records) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Missing S-030 validation case IDs"):
        load_validation_samples(manifest_paths=(manifest,))


def test_duplicate_required_s030_id_fails_loudly(tmp_path):
    records = _manifest_records()
    manifest = tmp_path / "duplicate.jsonl"
    manifest.write_text("\n".join(json.dumps(record) for record in [*records, records[0]]) + "\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Duplicate S-030 validation case IDs"):
        load_validation_samples(manifest_paths=(manifest,))


def test_validation_samples_endpoint_returns_samples(client):
    response = client.get("/api/validation-samples")

    assert response.status_code == 200
    payload = response.get_json()
    assert len(payload["samples"]) == 20
    assert payload["samples"][0]["id"] == "DN-001"
    assert {sample["collection_label"] for sample in payload["samples"]} == {
        "General long-form validation corpus",
        "S-030 semantic and structural cases",
    }
    assert [sample["id"] for sample in payload["samples"][6:]] == list(S030_CASE_IDS)
