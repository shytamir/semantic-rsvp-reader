# Architecture

Semantic RSVP Reader is intentionally small and inspectable.

## Application Shape

- `semantic_rsvp/web.py`: Flask app, API routes, schedule serialization.
- `semantic_rsvp/text/`: text normalization and sentence/source-boundary segmentation.
- `semantic_rsvp/chunking/`: rule-based chunker and chunk model.
- `semantic_rsvp/timing/`: deterministic duration model, schedule assembly, quote/parenthetical display state.
- `semantic_rsvp/navigation/`: paragraph/progress metadata used by orientation aids.
- `semantic_rsvp/structure/`: Markdown H1/H2 structural metadata.
- `semantic_rsvp/defects/`: in-app defect report validation, sanitization, and compressed Markdown storage.
- `semantic_rsvp/security/`: local storage encryption warning.
- `templates/`, `static/css/`, `static/js/`: mobile-first HTML/CSS/vanilla JavaScript UI.
- `tests/`: backend, static shell, chunking, timing, validation, and utility coverage.

## Request Flow

1. The browser posts text to `/api/schedule`.
2. Flask normalizes and segments the text.
3. The rule-based chunker emits chunks.
4. The timing engine assigns deterministic durations.
5. Navigation, structure, quote, and parenthetical metadata are attached.
6. The frontend renders and advances the schedule.
7. Optional in-app defect reports are saved as compressed Markdown by the backend.

## Design Constraints

- No ML/NLP runtime dependency.
- No frontend framework or build step.
- No timing/playback behavior changes unless a pass explicitly targets them.
- Validation evidence should drive refinements.
- Defect report payloads must remain bounded and sanitized.
