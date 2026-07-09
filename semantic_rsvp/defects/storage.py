from __future__ import annotations

import gzip
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REPORT_DIR = PROJECT_ROOT / "data" / "defect_reports"

KNOWN_CATEGORIES = {
    "bad_chunk_split",
    "orphan_function_word",
    "overlong_chunk",
    "underdense_chunk",
    "rushed_dense_chunk",
    "overpaused_light_chunk",
    "punctuation_rhythm_issue",
    "gesture_interference",
    "adaptation_annoyance",
    "completion_or_reset_confusion",
    "layout_or_visibility_issue",
    "comprehension_drop",
    "fatigue_or_discomfort",
    "other",
}


class DefectReportValidationError(ValueError):
    pass


def save_defect_report(payload: dict, report_dir: Path | None = None) -> dict[str, str]:
    normalized = validate_defect_payload(payload)
    created_at = datetime.now(UTC)
    report_id = f"defect_{created_at:%Y%m%d_%H%M%S}_{uuid4().hex[:6]}"
    filename = f"{report_id}.md.gz"

    active_report_dir = Path(report_dir or DEFAULT_REPORT_DIR)
    active_report_dir.mkdir(parents=True, exist_ok=True)
    report_path = active_report_dir / filename

    markdown = render_defect_report_markdown(normalized, report_id, created_at)
    with gzip.open(report_path, "wt", encoding="utf-8") as file:
        file.write(markdown)

    return {"report_id": report_id, "filename": filename}


def validate_defect_payload(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise DefectReportValidationError("Expected a JSON object.")

    category = payload.get("category")
    if not isinstance(category, str) or not category.strip():
        raise DefectReportValidationError("Category must be a non-empty string.")
    category = category.strip()
    if category not in KNOWN_CATEGORIES:
        raise DefectReportValidationError("Category is not recognized.")

    severity = payload.get("severity")
    if not isinstance(severity, int) or isinstance(severity, bool):
        raise DefectReportValidationError("Severity must be an integer from 1 to 4.")
    if severity < 1 or severity > 4:
        raise DefectReportValidationError("Severity must be between 1 and 4.")

    notes = payload.get("notes", "")
    preferred_behavior = payload.get("preferred_behavior", "")
    if not isinstance(notes, str):
        raise DefectReportValidationError("Notes must be a string.")
    if not isinstance(preferred_behavior, str):
        raise DefectReportValidationError("Preferred behavior must be a string.")

    reader_state = payload.get("reader_state", {})
    client = payload.get("client", {})
    if not isinstance(reader_state, dict):
        raise DefectReportValidationError("Reader state must be an object.")
    if not isinstance(client, dict):
        raise DefectReportValidationError("Client must be an object.")

    return {
        "category": category,
        "severity": severity,
        "notes": notes,
        "preferred_behavior": preferred_behavior,
        "reader_state": reader_state,
        "client": client,
    }


def render_defect_report_markdown(
    payload: dict,
    report_id: str,
    created_at: datetime,
) -> str:
    reader_state = payload["reader_state"]
    session_summary = _dict_value(reader_state, "session_summary")
    client = payload["client"]

    return "\n".join(
        [
            "# Semantic RSVP Defect Report",
            "",
            f"Report ID: {report_id}",
            f"Created at: {created_at.isoformat().replace('+00:00', 'Z')}",
            "",
            "## Classification",
            "",
            f"Category: {payload['category']}",
            f"Severity: {payload['severity']}",
            "Notes:",
            _string_value(payload, "notes"),
            "",
            "Preferred behavior:",
            _string_value(payload, "preferred_behavior"),
            "",
            "## Reader State",
            "",
            f"Current index: {_value(reader_state, 'current_index')}",
            f"Sentence index: {_value(reader_state, 'sentence_index')}",
            f"Playback speed: {_value(reader_state, 'playback_speed')}x",
            f"Adaptation enabled: {_value(reader_state, 'adaptation_enabled')}",
            "",
            "Current chunk:",
            _string_value(reader_state, "current_chunk"),
            "",
            f"Current duration ms: {_value(reader_state, 'current_duration_ms')}",
            f"Current syntactic hint: {_value(reader_state, 'current_syntactic_hint')}",
            f"Current content word count: {_value(reader_state, 'current_content_word_count')}",
            "",
            "Original sentence:",
            _string_value(reader_state, "original_sentence"),
            "",
            "Previous chunks:",
            *_format_chunks(reader_state.get("previous_chunks")),
            "",
            "Next chunks:",
            *_format_chunks(reader_state.get("next_chunks")),
            "",
            "## Session Summary",
            "",
            f"Event count: {_value(session_summary, 'event_count')}",
            f"Rewind count: {_value(session_summary, 'rewind_count')}",
            f"Pause count: {_value(session_summary, 'pause_count')}",
            f"Speed change count: {_value(session_summary, 'speed_change_count')}",
            f"Adaptation count: {_value(session_summary, 'adaptation_count')}",
            f"Completed: {_value(session_summary, 'completed')}",
            "",
            "## Client",
            "",
            "User agent:",
            _string_value(client, "user_agent"),
            "",
            "Viewport:",
            f"{_value(client, 'viewport_width')}x{_value(client, 'viewport_height')}",
            "",
        ]
    )


def _dict_value(source: dict, key: str) -> dict:
    value = source.get(key, {})
    return value if isinstance(value, dict) else {}


def _value(source: dict, key: str) -> str:
    value = source.get(key, "unknown")
    if value is None:
        return "unknown"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def _string_value(source: dict, key: str) -> str:
    value = source.get(key, "")
    return value if isinstance(value, str) and value else "unknown"


def _format_chunks(chunks) -> list[str]:
    if not isinstance(chunks, list) or not chunks:
        return ["- none"]

    formatted = []
    for chunk in chunks:
        if not isinstance(chunk, dict):
            continue
        formatted.append(f"- [{_value(chunk, 'index')}] {_string_value(chunk, 'text')}")
    return formatted or ["- none"]
