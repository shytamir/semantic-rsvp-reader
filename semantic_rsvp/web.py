from dataclasses import asdict

from flask import Flask, jsonify, render_template, request

from semantic_rsvp.chunking.rules import RuleBasedChunker
from semantic_rsvp.defects.storage import (
    DEFAULT_REPORT_DIR,
    DefectReportValidationError,
    save_defect_report,
)
from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences
from semantic_rsvp.timing.models import TimingConfig
from semantic_rsvp.timing.schedule import schedule_text
from semantic_rsvp.validation_samples import load_validation_samples


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    app.config.setdefault("DEFECT_REPORT_DIR", DEFAULT_REPORT_DIR)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

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

        normalized_text = normalize_text(raw_text)
        if not normalized_text:
            return jsonify({"error": "Text must not be empty."}), 400

        sentences = split_sentences(normalized_text)
        chunker = RuleBasedChunker()
        chunked_sentences = [
            {
                "sentence": sentence,
                "chunks": [
                    asdict(chunk) for chunk in chunker.chunk_sentence(sentence)
                ],
            }
            for sentence in sentences
        ]
        return jsonify(
            {
                "normalized_text": normalized_text,
                "sentences": sentences,
                "sentence_count": len(sentences),
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

        normalized_sentence = normalize_text(sentence)
        if not normalized_sentence:
            return jsonify({"error": "Sentence must not be empty."}), 400

        chunks = RuleBasedChunker().chunk_sentence(normalized_sentence)
        return jsonify(
            {
                "chunks": [asdict(chunk) for chunk in chunks],
                "chunk_count": len(chunks),
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

        normalized_text = normalize_text(raw_text)
        if not normalized_text:
            return jsonify({"error": "Text must not be empty."}), 400

        try:
            config = _timing_config_from_payload(payload)
        except (TypeError, ValueError) as error:
            return jsonify({"error": str(error)}), 400

        sentences = split_sentences(normalized_text)
        scheduled_chunks = schedule_text(normalized_text, config=config)
        sentence_count = len(sentences)
        return jsonify(
            {
                "schedule": [
                    _scheduled_chunk_to_dict(scheduled_chunk)
                    for scheduled_chunk in scheduled_chunks
                ],
                "chunk_count": len(scheduled_chunks),
                "sentence_count": sentence_count,
                "sentences": sentences,
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
    return {
        "index": scheduled_chunk.index,
        "sentence_index": scheduled_chunk.sentence_index,
        "text": chunk.text,
        "content_word_count": chunk.content_word_count,
        "char_length": chunk.char_length,
        "syntactic_hint": chunk.syntactic_hint,
        "duration_ms": scheduled_chunk.duration_ms,
    }


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", debug=True)
