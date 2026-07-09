# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

## Current Scope

This repository currently contains the Week 3 Part 2 foundation:

- Flask app factory and routes for `/`, `/health`, `/api/ingest`, and `/api/schedule`
- Optional `/api/chunk` endpoint for chunking one sentence
- Mobile-first HTML/CSS/vanilla JS playback loop
- Pure-Python text normalization
- Deterministic sentence segmentation
- Pure-Python rule-based semantic chunking v1
- Deterministic timing and full text-to-schedule generation
- Pytest coverage for the web app, normalization, segmentation, ingestion API, chunking, timing, and scheduling
- GitHub Actions CI that installs minimal dependencies and runs pytest

## Non-Goals

This version does not implement gestures, adaptive speed, persistence, accounts, databases, EPUB/PDF import, ML models, NLP services, spaCy, transformers, or a frontend framework.

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the App

```bash
flask --app semantic_rsvp.web:create_app run
```

Open `http://127.0.0.1:5000`.

## Run Tests

```bash
pytest
```

The repository includes `pyproject.toml` so pytest can import the local `semantic_rsvp` package directly from a fresh clone.

## Next Milestones

1. Touch gestures
2. Rewind buffer refinement
3. Speed controls
4. Session-only adaptation
5. Mobile hardening

## Manual Test Checklist

Mobile playback manual test:

1. Open app on a phone browser.
2. Paste a short paragraph.
3. Tap Load/Prepare.
4. Confirm first chunk appears centered.
5. Tap Play.
6. Confirm chunks advance automatically.
7. Tap Pause.
8. Confirm playback stops immediately.
9. Tap Previous.
10. Confirm it moves back one chunk and remains paused.
11. Tap Next.
12. Confirm it moves forward one chunk and remains paused.
13. Tap Reset.
14. Confirm it returns to first chunk and remains paused.
15. Let playback reach the end.
16. Confirm it stops cleanly.
17. Tap Back/Edit Text.
18. Confirm input mode returns and no timer keeps running.
