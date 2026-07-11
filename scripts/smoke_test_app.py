import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semantic_rsvp.web import create_app


def main() -> int:
    app = create_app({"TESTING": True})
    client = app.test_client()
    requests = (
        (client.get, "/health", None),
        (client.post, "/api/chunk", {"sentence": "The system learns from the reader."}),
        (client.post, "/api/schedule", {"text": "The system learns from the reader."}),
    )
    for request, path, payload in requests:
        response = request(path, json=payload) if payload else request(path)
        if response.status_code != 200:
            raise RuntimeError(f"{path} returned {response.status_code}: {response.get_data(as_text=True)}")
    print(f"Flask smoke tests passed in {app.config['RSVP_CHUNKER_MODE']} mode.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
