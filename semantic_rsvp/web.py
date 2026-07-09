from flask import Flask, jsonify, render_template, request

from semantic_rsvp.text.normalize import normalize_text
from semantic_rsvp.text.segment import split_sentences


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

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
        return jsonify(
            {
                "normalized_text": normalized_text,
                "sentences": sentences,
                "sentence_count": len(sentences),
            }
        )

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
