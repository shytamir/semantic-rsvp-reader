import gzip
from pathlib import Path

import pytest

from semantic_rsvp.web import create_app


@pytest.fixture()
def defect_report_dir(tmp_path):
    return tmp_path / "reports"


@pytest.fixture()
def defect_client(defect_report_dir):
    app = create_app()
    app.config.update(TESTING=True, DEFECT_REPORT_DIR=defect_report_dir)
    return app.test_client()


def minimal_report():
    return {
        "category": "bad_chunk_split",
        "severity": 2,
        "notes": "The phrase feels fragmented.",
        "preferred_behavior": "Keep the negation closer to the verb.",
        "reader_state": {
            "current_index": 14,
            "sentence_index": 3,
            "current_chunk": "merely retrieve",
            "current_duration_ms": 400,
            "base_duration_ms": 400,
            "effective_duration_ms": 348,
            "duration_source": "schedule",
            "current_syntactic_hint": "normal",
            "current_content_word_count": 2,
            "char_length": 15,
            "original_sentence": "The system does not merely retrieve context.",
            "previous_chunks": [
                {
                    "index": 13,
                    "sentence_index": 3,
                    "text": "does not",
                    "duration_ms": 360,
                    "base_duration_ms": 360,
                    "effective_duration_ms": 313,
                    "duration_source": "schedule",
                    "syntactic_hint": "normal",
                    "content_word_count": 1,
                    "char_length": 8,
                }
            ],
            "next_chunks": [
                {
                    "index": 15,
                    "sentence_index": 3,
                    "text": "context.",
                    "duration_ms": 580,
                    "base_duration_ms": 580,
                    "effective_duration_ms": 504,
                    "duration_source": "schedule",
                    "syntactic_hint": "normal",
                    "content_word_count": 1,
                    "char_length": 8,
                }
            ],
            "playback_speed": 1.0,
            "adaptation_enabled": True,
            "session_summary": {
                "event_count": 23,
                "rewind_count": 2,
                "pause_count": 4,
                "speed_change_count": 1,
                "adaptation_count": 0,
                "completed": False,
                "elapsed_session_ms": 12000,
                "estimated_remaining_chunks": 10,
                "average_effective_duration_ms": 430,
                "last_adaptation_reason": "rewinds",
                "last_adaptation_direction": "slower",
            },
        },
        "client": {
            "user_agent": "pytest",
            "viewport_width": 390,
            "viewport_height": 844,
        },
    }


def test_defects_rejects_missing_json_body(defect_client):
    response = defect_client.post(
        "/api/defects",
        data="not json",
        content_type="text/plain",
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_defects_rejects_missing_category(defect_client):
    payload = minimal_report()
    payload.pop("category")

    response = defect_client.post("/api/defects", json=payload)

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_defects_rejects_invalid_severity(defect_client):
    payload = minimal_report()
    payload["severity"] = 5

    response = defect_client.post("/api/defects", json=payload)

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_defects_accepts_valid_minimal_report(defect_client, defect_report_dir):
    assert not defect_report_dir.exists()

    response = defect_client.post("/api/defects", json=minimal_report())

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "saved"
    assert payload["report_id"].startswith("defect_")
    assert payload["filename"] == f"{payload['report_id']}.md.gz"
    assert not Path(payload["filename"]).is_absolute()

    report_path = defect_report_dir / payload["filename"]
    assert report_path.exists()


def test_defects_writes_readable_markdown_gzip(defect_client, defect_report_dir):
    response = defect_client.post("/api/defects", json=minimal_report())
    report_path = defect_report_dir / response.get_json()["filename"]

    with gzip.open(report_path, "rt", encoding="utf-8") as file:
        markdown = file.read()

    assert "# Semantic RSVP Defect Report" in markdown
    assert "Category: bad_chunk_split" in markdown
    assert "Severity: 2" in markdown
    assert "The phrase feels fragmented." in markdown
    assert "merely retrieve" in markdown


def test_defects_writes_timing_context_to_markdown(defect_client, defect_report_dir):
    response = defect_client.post("/api/defects", json=minimal_report())
    report_path = defect_report_dir / response.get_json()["filename"]

    with gzip.open(report_path, "rt", encoding="utf-8") as file:
        markdown = file.read()

    assert "## Timing Context" in markdown
    assert "Base duration ms: 400" in markdown
    assert "Effective duration ms: 348" in markdown
    assert "Playback speed: 1.0x" in markdown
    assert "Duration source: schedule" in markdown
    assert "Current syntactic hint: normal" in markdown
    assert "Current content word count: 2" in markdown
    assert "Character length: 15" in markdown


def test_defects_writes_nearby_chunk_timing_details(defect_client, defect_report_dir):
    response = defect_client.post("/api/defects", json=minimal_report())
    report_path = defect_report_dir / response.get_json()["filename"]

    with gzip.open(report_path, "rt", encoding="utf-8") as file:
        markdown = file.read()

    assert '"does not" - 360ms base / 313ms effective - normal' in markdown
    assert '"context." - 580ms base / 504ms effective - normal' in markdown


def test_defects_escape_html_in_markdown(defect_client, defect_report_dir):
    payload = minimal_report()
    payload["notes"] = '<script>alert("x")</script>'

    response = defect_client.post("/api/defects", json=payload)
    report_path = defect_report_dir / response.get_json()["filename"]

    with gzip.open(report_path, "rt", encoding="utf-8") as file:
        markdown = file.read()

    assert "<script>" not in markdown
    assert "&lt;script&gt;" in markdown


def test_defects_rejects_oversized_report(defect_client):
    payload = minimal_report()
    payload["notes"] = "x" * 40_000

    response = defect_client.post("/api/defects", json=payload)

    assert response.status_code == 400
    assert "too large" in response.get_json()["error"]


def test_defects_rejects_oversized_request_body(tmp_path):
    app = create_app()
    app.config.update(
        TESTING=True,
        DEFECT_REPORT_DIR=tmp_path / "reports",
        MAX_CONTENT_LENGTH=128,
    )
    client = app.test_client()

    response = client.post("/api/defects", json=minimal_report())

    assert response.status_code == 413
    assert response.get_json() == {"error": "Request body is too large."}
