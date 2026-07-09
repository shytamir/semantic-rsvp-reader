# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

## Current Scope

This repository currently contains the Week 1 foundation only:

- Flask app factory and routes for `/`, `/health`, and `/api/ingest`
- Mobile-first HTML/CSS/vanilla JS shell
- Pure-Python text normalization
- Deterministic sentence segmentation
- Lightweight placeholder models for future chunking and timing work
- Pytest coverage for the web app, normalization, segmentation, and ingest API
- GitHub Actions CI that installs minimal dependencies and runs pytest

## Non-Goals

This version does not implement semantic chunking, a timing engine, gestures, adaptive speed, the reader playback loop, persistence, accounts, databases, EPUB/PDF import, ML models, NLP services, spaCy, transformers, or a frontend framework.

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

## Next Milestones

1. Semantic chunking engine
2. Timing/rhythm engine
3. Mobile reader loop
4. Touch gestures
5. Session-only adaptation
