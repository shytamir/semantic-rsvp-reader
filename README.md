# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

## Current Scope

This repository currently contains the Week 3/4 touch refinement foundation:

- Flask app factory and routes for `/`, `/health`, `/api/ingest`, and `/api/schedule`
- Optional `/api/chunk` endpoint for chunking one sentence
- Mobile-first HTML/CSS/vanilla JS playback loop
- Pure-Python text normalization
- Deterministic sentence segmentation
- Pure-Python rule-based semantic chunking v1
- Deterministic timing and full text-to-schedule generation
- Touch gestures for play/pause and chunk navigation
- Placeholder speed overlay for the next speed-control slice
- Pytest coverage for the web app, normalization, segmentation, ingestion API, chunking, timing, and scheduling
- GitHub Actions CI that installs minimal dependencies and runs pytest

## Non-Goals

This version does not implement real speed controls, adaptive speed, persistence, accounts, databases, EPUB/PDF import, ML models, NLP services, spaCy, transformers, or a frontend framework.

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the App

```bash
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Open `http://127.0.0.1:5000` on the host machine, or use the host machine's LAN IP address from a phone or another device on the same network.

## Run Tests

```bash
pytest
```

The repository includes `pyproject.toml` so pytest can import the local `semantic_rsvp` package directly from a fresh clone.

## Next Milestones

1. Real speed controls
2. Session-only event tracking
3. Session-only adaptation
4. Mobile hardening
5. Demo validation

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

Touch gesture manual test:

1. Open app on a phone browser.
2. Paste a short paragraph and load it.
3. Confirm first chunk appears centered and paused.
4. Tap reader area.
5. Confirm playback starts.
6. Tap reader area again.
7. Confirm playback pauses.
8. Swipe left.
9. Confirm reader moves back one chunk and pauses.
10. Swipe right.
11. Confirm reader moves forward one chunk and pauses.
12. Swipe left at the first chunk.
13. Confirm it stays on the first chunk and remains paused.
14. Swipe right at the final chunk.
15. Confirm it stays on the final chunk and remains paused.
16. Long press reader area.
17. Confirm speed overlay placeholder appears.
18. Long press again or close overlay.
19. Confirm overlay disappears.
20. Confirm swipes do not accidentally toggle play/pause.
21. Confirm long press does not accidentally toggle play/pause.
22. Confirm buttons still work.
23. Confirm Back/Edit Text stops playback and returns to input mode.
