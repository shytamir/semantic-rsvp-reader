# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first Flask + HTML5 prototype for reading text as deterministic semantic chunks. It explores whether inspectable chunking, rhythm control, and lightweight validation tooling can make RSVP-style reading easier to study without adding opaque ML dependencies.

## Project Status

- Status: green prototype.
- Current phase: validation-driven refinement.
- Latest completed slice: Post-Validation Stabilization Pass 1.
- Primary focus: mobile layout, source-boundary chunking, long-form dates, and phrase cohesion.
- Timing, playback, navigation, and adaptation semantics are intentionally stable during this phase.
- Canonical status and roadmap live in [docs/management/](docs/management/index.md).

## Core Capabilities

- Mobile-first Flask/HTML5 RSVP reader.
- Pure-Python rule-based semantic chunker.
- Deterministic timing engine.
- Phone-browser playback with tap, swipe, hold-swipe, and long-press controls.
- Session-only speed controls, debug summary, and conservative adaptation.
- In-app compressed Markdown defect reports with security hardening.
- Quote/parenthetical display-state metadata.
- Passive spatial anchor, coarse seek, breakpoint traversal, ghost previous chunk, drift recovery, and structural hierarchy anchor.
- Validation corpus, defect taxonomy, and review utilities.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Open `http://127.0.0.1:5000` on the host machine, or use the host machine's LAN IP address from another device on the same network.

## Test

```bash
python -m pytest
python scripts/check_js_syntax.py
```

`scripts/check_js_syntax.py` uses `node --check` or `nodejs --check` when available. If Node is missing locally, it skips cleanly; CI installs Node and enforces the check.

## Development Workflow

- Use `python -m pytest` before committing.
- Use the prepare screen to load validation samples.
- Use in-app defect reporting during reader playback.
- Review saved reports with `scripts/review_defects.py`.
- Keep behavior changes tied to observed validation evidence.

More details:

- [Setup](docs/development/setup.md)
- [Testing](docs/development/testing.md)
- [Architecture](docs/development/architecture.md)
- [Manual validation](docs/development/manual_testing.md)

## Documentation Map

- [Docs index](docs/index.md)
- [Feature docs](docs/index.md#features)
- [Validation docs](docs/validation/index.md)
- [Management docs](docs/management/index.md)
- [Defect taxonomy](docs/validation/defect_taxonomy.md)
- [Validation corpus](docs/validation/corpus.md)

## Current Roadmap

1. Post-Stabilization Validation Pass focused on mobile layout and source-boundary chunking.
2. Chunking Regression Corpus Expansion if stabilization validates well.
3. Post-navigation usability validation.
4. Demo/beta readiness cleanup.

See [docs/management/roadmap.md](docs/management/roadmap.md) for the canonical roadmap.

## Non-Goals

- No public performance claims.
- No ML/NLP dependency additions.
- No frontend framework, npm toolchain, or browser automation.
- No accounts, analytics, service workers, database, or cloud sync.
- No native app, EPUB/PDF import, or deployment infrastructure.

## License

No license has been selected yet.
