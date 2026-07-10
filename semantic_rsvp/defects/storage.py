from __future__ import annotations

import gzip
from html import escape
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REPORT_DIR = PROJECT_ROOT / "data" / "defect_reports"
MAX_REPORT_MARKDOWN_CHARS = 24_000
MAX_FIELD_CHARS = 4_000
MAX_CHUNKS_PER_SIDE = 5

KNOWN_CATEGORIES = {
    "bad_chunk_split",
    "orphan_function_word",
    "honorific_name_split",
    "title_name_split",
    "proper_name_split",
    "article_noun_split",
    "weak_boundary_chunk",
    "pronoun_or_preposition_bookend",
    "overlong_chunk",
    "underdense_chunk",
    "rushed_dense_chunk",
    "overpaused_light_chunk",
    "punctuation_rhythm_issue",
    "gesture_interference",
    "adaptation_annoyance",
    "completion_or_reset_confusion",
    "layout_or_visibility_issue",
    "quote_state_confusion",
    "parenthetical_state_confusion",
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
    if len(markdown) > MAX_REPORT_MARKDOWN_CHARS:
        raise DefectReportValidationError("Defect report is too large.")
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

    notes = _validated_string(payload.get("notes", ""), "Notes")
    preferred_behavior = _validated_string(
        payload.get("preferred_behavior", ""),
        "Preferred behavior",
    )

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
        "reader_state": _sanitize_reader_state(reader_state),
        "client": _sanitize_client(client),
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
            "## Timing Context",
            "",
            f"Base duration ms: {_value(reader_state, 'base_duration_ms')}",
            f"Effective duration ms: {_value(reader_state, 'effective_duration_ms')}",
            f"Playback speed: {_value(reader_state, 'playback_speed')}x",
            f"Duration source: {_value(reader_state, 'duration_source')}",
            f"Current syntactic hint: {_value(reader_state, 'current_syntactic_hint')}",
            f"Current content word count: {_value(reader_state, 'current_content_word_count')}",
            f"Character length: {_value(reader_state, 'char_length')}",
            f"In quote: {_value(reader_state, 'in_quote')}",
            f"Quote boundary: {_value(reader_state, 'quote_boundary')}",
            f"In parenthetical: {_value(reader_state, 'in_parenthetical')}",
            f"Parenthetical depth: {_value(reader_state, 'parenthetical_depth')}",
            f"Navigation progress percent: {_value(reader_state.get('navigation', {}), 'progress_percent')}",
            f"Navigation paragraph index: {_value(reader_state.get('navigation', {}), 'paragraph_index')}",
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
            f"Elapsed session ms: {_value(session_summary, 'elapsed_session_ms')}",
            f"Estimated remaining chunks: {_value(session_summary, 'estimated_remaining_chunks')}",
            f"Average effective duration ms: {_value(session_summary, 'average_effective_duration_ms')}",
            f"Last adaptation reason: {_value(session_summary, 'last_adaptation_reason')}",
            f"Last adaptation direction: {_value(session_summary, 'last_adaptation_direction')}",
            "",
            "## Client",
            "",
            "User agent:",
            _string_value(client, "user_agent"),
            "",
            "Viewport:",
            f"{_value(client, 'viewport_width')}x{_value(client, 'viewport_height')}",
            "",
            "Display:",
            f"Reader width px: {_value(client, 'display_width_px')}",
            f"Chunk scroll width px: {_value(client, 'chunk_scroll_width_px')}",
            f"Chunk client width px: {_value(client, 'chunk_client_width_px')}",
            f"Chunk may overflow: {_value(client, 'chunk_may_overflow')}",
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
    return _sanitize_text(str(value), max_chars=500)


def _string_value(source: dict, key: str) -> str:
    value = source.get(key, "")
    return _sanitize_text(value) if isinstance(value, str) and value else "unknown"


def _format_chunks(chunks) -> list[str]:
    if not isinstance(chunks, list) or not chunks:
        return ["- none"]

    formatted = []
    for chunk in chunks[:MAX_CHUNKS_PER_SIDE]:
        if not isinstance(chunk, dict):
            continue
        formatted.append(
            "- [{index}] \"{text}\" - {base}ms base / {effective}ms effective - "
            "{hint} - {content_words} content word(s) - {chars} chars - "
            "quote={in_quote}/{quote_boundary} - parenthetical={in_parenthetical}/"
            "{parenthetical_depth} - navigation={progress_percent}%/p{paragraph_index}".format(
                index=_value(chunk, "index"),
                text=_string_value(chunk, "text"),
                base=_value(chunk, "base_duration_ms"),
                effective=_value(chunk, "effective_duration_ms"),
                hint=_value(chunk, "syntactic_hint"),
                content_words=_value(chunk, "content_word_count"),
                chars=_value(chunk, "char_length"),
                in_quote=_value(chunk, "in_quote"),
                quote_boundary=_value(chunk, "quote_boundary"),
                in_parenthetical=_value(chunk, "in_parenthetical"),
                parenthetical_depth=_value(chunk, "parenthetical_depth"),
                progress_percent=_value(chunk.get("navigation", {}), "progress_percent"),
                paragraph_index=_value(chunk.get("navigation", {}), "paragraph_index"),
            )
        )
    return formatted or ["- none"]


def _sanitize_reader_state(reader_state: dict) -> dict:
    sanitized = {}
    for key in (
        "current_index",
        "sentence_index",
        "current_duration_ms",
        "base_duration_ms",
        "effective_duration_ms",
        "current_content_word_count",
        "char_length",
        "playback_speed",
        "adaptation_enabled",
        "in_quote",
        "in_parenthetical",
        "parenthetical_depth",
    ):
        sanitized[key] = reader_state.get(key)

    for key in (
        "current_chunk",
        "current_syntactic_hint",
        "duration_source",
        "quote_boundary",
        "original_sentence",
    ):
        sanitized[key] = _bounded_text(reader_state.get(key, ""))

    sanitized["previous_chunks"] = _sanitize_chunks(reader_state.get("previous_chunks"))
    sanitized["next_chunks"] = _sanitize_chunks(reader_state.get("next_chunks"))
    sanitized["navigation"] = _sanitize_navigation(reader_state.get("navigation"))
    sanitized["session_summary"] = _sanitize_session_summary(
        reader_state.get("session_summary", {})
    )
    return sanitized


def _sanitize_client(client: dict) -> dict:
    return {
        "user_agent": _bounded_text(client.get("user_agent", "")),
        "viewport_width": client.get("viewport_width"),
        "viewport_height": client.get("viewport_height"),
        "display_width_px": client.get("display_width_px"),
        "chunk_scroll_width_px": client.get("chunk_scroll_width_px"),
        "chunk_client_width_px": client.get("chunk_client_width_px"),
        "chunk_may_overflow": client.get("chunk_may_overflow"),
    }


def _sanitize_session_summary(summary) -> dict:
    if not isinstance(summary, dict):
        return {}
    return {
        "event_count": summary.get("event_count"),
        "rewind_count": summary.get("rewind_count"),
        "pause_count": summary.get("pause_count"),
        "speed_change_count": summary.get("speed_change_count"),
        "adaptation_count": summary.get("adaptation_count"),
        "completed": summary.get("completed"),
        "elapsed_session_ms": summary.get("elapsed_session_ms"),
        "estimated_remaining_chunks": summary.get("estimated_remaining_chunks"),
        "average_effective_duration_ms": summary.get("average_effective_duration_ms"),
        "last_adaptation_reason": _bounded_text(summary.get("last_adaptation_reason", "")),
        "last_adaptation_direction": _bounded_text(
            summary.get("last_adaptation_direction", "")
        ),
    }


def _sanitize_chunks(chunks) -> list[dict]:
    if not isinstance(chunks, list):
        return []
    sanitized = []
    for chunk in chunks[:MAX_CHUNKS_PER_SIDE]:
        if not isinstance(chunk, dict):
            continue
        sanitized.append(
            {
                "index": chunk.get("index"),
                "sentence_index": chunk.get("sentence_index"),
                "text": _bounded_text(chunk.get("text", ""), max_chars=500),
                "duration_ms": chunk.get("duration_ms"),
                "base_duration_ms": chunk.get("base_duration_ms"),
                "effective_duration_ms": chunk.get("effective_duration_ms"),
                "duration_source": _bounded_text(chunk.get("duration_source", "")),
                "syntactic_hint": _bounded_text(chunk.get("syntactic_hint", "")),
                "content_word_count": chunk.get("content_word_count"),
                "char_length": chunk.get("char_length"),
                "in_quote": chunk.get("in_quote"),
                "quote_boundary": _bounded_text(chunk.get("quote_boundary", "")),
                "in_parenthetical": chunk.get("in_parenthetical"),
                "parenthetical_depth": chunk.get("parenthetical_depth"),
                "navigation": _sanitize_navigation(chunk.get("navigation")),
            }
        )
    return sanitized


def _sanitize_navigation(navigation) -> dict:
    if not isinstance(navigation, dict):
        return {}
    return {
        "char_start": navigation.get("char_start"),
        "char_end": navigation.get("char_end"),
        "char_count_total": navigation.get("char_count_total"),
        "progress_ratio": navigation.get("progress_ratio"),
        "progress_percent": navigation.get("progress_percent"),
        "paragraph_index": navigation.get("paragraph_index"),
        "is_paragraph_start": navigation.get("is_paragraph_start"),
        "is_paragraph_end": navigation.get("is_paragraph_end"),
        "is_progress_milestone": navigation.get("is_progress_milestone"),
    }


def _sanitize_text(value, max_chars: int = MAX_FIELD_CHARS) -> str:
    if not isinstance(value, str):
        return ""
    without_controls = "".join(
        char if char in "\n\t" or ord(char) >= 32 else " " for char in value
    )
    return escape(without_controls[:max_chars], quote=False)


def _validated_string(value, label: str) -> str:
    if not isinstance(value, str):
        raise DefectReportValidationError(f"{label} must be a string.")
    if len(value) > MAX_FIELD_CHARS:
        raise DefectReportValidationError(f"{label} is too large.")
    return value


def _bounded_text(value, max_chars: int = MAX_FIELD_CHARS) -> str:
    if not isinstance(value, str):
        return ""
    if len(value) > max_chars:
        raise DefectReportValidationError("Defect report field is too large.")
    return value
