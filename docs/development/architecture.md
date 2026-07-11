# Architecture

Semantic RSVP Reader is intentionally small and inspectable.

## Application Shape

- `semantic_rsvp/web.py`: Flask app, API routes, schedule serialization.
- `semantic_rsvp/application/`: framework-independent schedule/chunking service.
- `semantic_rsvp/text/`: text normalization and sentence/source-boundary segmentation.
- `semantic_rsvp/chunking/`: chunker interface, chunker selection policy, rule-based fallback, and chunk model.
- `semantic_rsvp/experiments/parser_assisted_chunking/`: frozen S-023 parser-assisted implementation used provisionally by the Flask prototype through a wrapper.
- `semantic_rsvp/timing/`: deterministic duration model, schedule assembly, quote/parenthetical display state.
- `semantic_rsvp/navigation/`: paragraph/progress metadata used by orientation aids.
- `semantic_rsvp/structure/`: Markdown H1/H2 structural metadata.
- `semantic_rsvp/defects/`: in-app defect report validation, sanitization, and compressed Markdown storage.
- `semantic_rsvp/security/`: local storage encryption warning.
- `templates/`, `static/css/`, `static/js/`: mobile-first HTML/CSS/vanilla JavaScript UI.
- `tests/`: backend, static shell, chunking, timing, validation, and utility coverage.

## Request Flow

1. The browser posts text to `/api/schedule`.
2. Flask routes delegate text processing to the application schedule service.
3. The service normalizes and segments the text once.
4. The configured chunker emits chunks: parser-assisted by default, rule-based when explicitly configured or when parser fallback is required.
5. The timing engine assigns deterministic durations.
6. Navigation, structure, quote, and parenthetical metadata are attached.
7. The frontend renders and advances the schedule.
8. Optional in-app defect reports are saved as compressed Markdown by the backend.

## Design Constraints

- spaCy is a provisional server-side evidence provider for the current Flask prototype, not a permanent or exclusive architecture.
- Flask responses must not expose parser-native objects or optimizer traces.
- Missing or failed parser dependencies must degrade to `RuleBasedChunker` without runtime model downloads.
- No frontend framework or build step.
- No timing/playback behavior changes unless a pass explicitly targets them.
- Validation evidence should drive refinements.
- Defect report payloads must remain bounded and sanitized.
