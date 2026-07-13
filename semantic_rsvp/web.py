from dataclasses import asdict
import logging
import os

from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge

from semantic_rsvp.application.schedule_service import ScheduleService
from semantic_rsvp.application.document_ingestion import DocumentIngestionError
from semantic_rsvp.application.epub_ingestion import MAX_EPUB_BYTES, ingest_epub_document
from semantic_rsvp.application.epub_preparation import prepare_epub
from semantic_rsvp.chunking.selection import (
    DEFAULT_CHUNKER_MODE,
    create_chunker,
    inspect_chunking_state,
    normalize_chunker_mode,
)
from semantic_rsvp.defects.storage import (
    DEFAULT_REPORT_DIR,
    DefectReportValidationError,
    save_defect_report,
)
from semantic_rsvp.security.storage_encryption import check_storage_encryption
from semantic_rsvp.timing.models import TimingConfig
from semantic_rsvp.validation_samples import load_validation_samples


def create_app(config: dict | None = None) -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    if config:
        app.config.update(config)
    app.config.setdefault("DEFECT_REPORT_DIR", DEFAULT_REPORT_DIR)
    app.config.setdefault("CHECK_STORAGE_ENCRYPTION", True)
    app.config.setdefault(
        "RSVP_CHUNKER_MODE",
        os.environ.get("RSVP_CHUNKER_MODE", DEFAULT_CHUNKER_MODE),
    )
    if app.config.get("MAX_CONTENT_LENGTH") is None:
        app.config["MAX_CONTENT_LENGTH"] = 1_000_000
    chunker_mode = normalize_chunker_mode(app.config["RSVP_CHUNKER_MODE"])
    app.config["RSVP_CHUNKER_MODE"] = chunker_mode
    chunking_state = inspect_chunking_state(chunker_mode)
    schedule_service = ScheduleService(chunker=create_chunker(chunker_mode))
    app.config["SCHEDULE_SERVICE"] = schedule_service
    app.config["CHUNKING_STATE"] = chunking_state
    app.config.setdefault("EPUB_PREPARER", prepare_epub)
    app.config.setdefault("EPUB_INGESTOR", ingest_epub_document)
    logging.getLogger(__name__).info(
        "Configured RSVP chunking mode: %s; provider_available=%s; provider_reason=%s",
        chunking_state.configured_mode,
        chunking_state.provider_available,
        chunking_state.provider_reason,
    )
    encryption_checked = False

    @app.before_request
    def warn_if_storage_encryption_unconfirmed():
        nonlocal encryption_checked
        if encryption_checked or app.config.get("TESTING"):
            return
        encryption_checked = True
        if not app.config.get("CHECK_STORAGE_ENCRYPTION"):
            return
        status = check_storage_encryption(app.config["DEFECT_REPORT_DIR"])
        if status.warning:
            logging.getLogger(__name__).warning(
                "Defect report storage encryption warning: %s",
                status.warning,
            )

    @app.errorhandler(RequestEntityTooLarge)
    def request_too_large(error):
        return jsonify({"error": "Request body is too large."}), 413

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify(
            {
                "status": "ok",
                "chunking": app.config["CHUNKING_STATE"].to_dict(),
            }
        )

    @app.get("/api/validation-samples")
    def validation_samples():
        return jsonify({"samples": load_validation_samples()})

    @app.post("/api/defects")
    def defects():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Expected a JSON object."}), 400

        try:
            saved_report = save_defect_report(
                payload,
                report_dir=app.config["DEFECT_REPORT_DIR"],
            )
        except DefectReportValidationError as error:
            return jsonify({"error": str(error)}), 400

        return jsonify({"status": "saved", **saved_report})

    @app.post("/api/ingest")
    def ingest():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Expected a JSON object with a text field."}), 400

        raw_text = payload.get("text")
        if not isinstance(raw_text, str):
            return jsonify({"error": "Text must be a string."}), 400

        result = app.config["SCHEDULE_SERVICE"].generate(raw_text)
        if not result.normalized_text:
            return jsonify({"error": "Text must not be empty."}), 400

        schedule_by_sentence = {index: [] for index in range(len(result.sentences))}
        for scheduled_chunk in result.schedule:
            schedule_by_sentence[scheduled_chunk.sentence_index].append(
                scheduled_chunk.chunk
            )
        chunked_sentences = [
            {
                "sentence": sentence,
                "chunks": [asdict(chunk) for chunk in schedule_by_sentence[index]],
            }
            for index, sentence in enumerate(result.sentences)
        ]
        return jsonify(
            {
                "normalized_text": result.normalized_text,
                "sentences": list(result.sentences),
                "sentence_count": len(result.sentences),
                "chunked_sentences": chunked_sentences,
            }
        )

    @app.post("/api/chunk")
    def chunk():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Expected a JSON object with a sentence field."}), 400

        sentence = payload.get("sentence")
        if not isinstance(sentence, str):
            return jsonify({"error": "Sentence must be a string."}), 400

        chunk_result = app.config["SCHEDULE_SERVICE"].chunk(sentence)
        if not chunk_result.normalized_text:
            return jsonify({"error": "Sentence must not be empty."}), 400

        return jsonify(
            {
                "chunks": [asdict(chunk) for chunk in chunk_result.chunks],
                "chunk_count": len(chunk_result.chunks),
            }
        )

    @app.post("/api/schedule")
    def schedule():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "Expected a JSON object with a text field."}), 400

        raw_text = payload.get("text")
        if not isinstance(raw_text, str):
            return jsonify({"error": "Text must be a string."}), 400

        try:
            config = _timing_config_from_payload(payload)
        except (TypeError, ValueError) as error:
            return jsonify({"error": str(error)}), 400

        result = app.config["SCHEDULE_SERVICE"].generate(raw_text, timing_config=config)
        if not result.normalized_text:
            return jsonify({"error": "Text must not be empty."}), 400

        return jsonify(
            {
                "schedule": [
                    _scheduled_chunk_to_dict(scheduled_chunk)
                    for scheduled_chunk in result.schedule
                ],
                "chunk_count": len(result.schedule),
                "sentence_count": len(result.sentences),
                "sentences": list(result.sentences),
            }
        )

    @app.post("/api/epub/schedule")
    def epub_schedule():
        request.max_content_length = MAX_EPUB_BYTES
        source_name = request.headers.get("X-EPUB-Filename", "")
        if request.mimetype != "application/epub+zip":
            return jsonify({"error": "Expected application/epub+zip bytes."}), 415
        try:
            preparation = app.config["EPUB_PREPARER"](
                request.get_data(cache=False), source_name=source_name
            )
            document = app.config["EPUB_INGESTOR"](
                preparation.data, source_name=source_name
            )
        except DocumentIngestionError as error:
            return jsonify({"error": str(error)}), 400
        result = app.config["SCHEDULE_SERVICE"].generate(document.text)
        if not result.normalized_text:
            return jsonify({"error": "EPUB contains no schedulable text."}), 400
        provenance = dict(document.provenance)
        return jsonify(
            {
                "document": {
                    "document_id": document.document_id,
                    "source_type": document.source_type,
                    "display_name": provenance.get("title") or source_name,
                    "source_name": source_name,
                },
                "preparation": {
                    "mode": preparation.mode,
                    "epub_version": preparation.epub_version,
                    "discarded_resources": preparation.discarded_resources,
                    "changes": list(preparation.changes),
                },
                "schedule": [
                    _scheduled_chunk_to_dict(scheduled_chunk)
                    for scheduled_chunk in result.schedule
                ],
                "chunk_count": len(result.schedule),
                "sentence_count": len(result.sentences),
                "sentences": list(result.sentences),
            }
        )

    return app


def _timing_config_from_payload(payload: dict) -> TimingConfig:
    fields = {
        "base_beat_ms",
        "min_duration_ms",
        "max_duration_ms",
        "sentence_pause_ms",
    }
    values = {}
    for field in fields:
        if field not in payload:
            continue
        value = payload[field]
        if not isinstance(value, int):
            raise TypeError(f"{field} must be an integer.")
        values[field] = value
    return TimingConfig(**values)


def _scheduled_chunk_to_dict(scheduled_chunk):
    chunk = scheduled_chunk.chunk
    display_state = scheduled_chunk.display_state
    navigation = scheduled_chunk.navigation
    structure = scheduled_chunk.structure
    return {
        "index": scheduled_chunk.index,
        "sentence_index": scheduled_chunk.sentence_index,
        "text": chunk.text,
        "content_word_count": chunk.content_word_count,
        "char_length": chunk.char_length,
        "syntactic_hint": chunk.syntactic_hint,
        "duration_ms": scheduled_chunk.duration_ms,
        "in_quote": display_state.in_quote,
        "quote_boundary": display_state.quote_boundary,
        "in_parenthetical": display_state.in_parenthetical,
        "parenthetical_depth": display_state.parenthetical_depth,
        "navigation": asdict(navigation),
        "structure": {
            **asdict(structure),
            "active_path": list(structure.active_path),
        },
    }


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", debug=os.environ.get("FLASK_DEBUG") == "1")
