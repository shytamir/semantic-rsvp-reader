# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

## Current Scope

This repository currently contains the Week 2 foundation:

- Flask app factory and routes for `/`, `/health`, and `/api/ingest`
- Optional `/api/chunk` endpoint for chunking one sentence
- Mobile-first HTML/CSS/vanilla JS shell
- Pure-Python text normalization
- Deterministic sentence segmentation
- Pure-Python rule-based semantic chunking v1
- Lightweight placeholder models for future timing work
- Pytest coverage for the web app, normalization, segmentation, ingestion API, and chunking
- GitHub Actions CI that installs minimal dependencies and runs pytest

## Non-Goals

This version does not implement a timing engine, gestures, adaptive speed, the reader playback loop, persistence, accounts, databases, EPUB/PDF import, ML models, NLP services, spaCy, transformers, or a frontend framework.

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

1. Timing/rhythm engine
2. Chunk schedule API
3. Mobile reader loop
4. Touch gestures
5. Session-only adaptation
