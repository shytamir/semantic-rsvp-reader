# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first Flask + HTML5 prototype for reading text as deterministic semantic chunks. It explores whether inspectable chunking, rhythm control, and lightweight validation tooling can make RSVP-style reading easier to study while keeping chunking policy project-owned and fallback-safe.

## Project Status

- Status: stabilized prototype; S-036 disposition `ready` with no acceptance-blocking defect.
- Current phase: Document Reader Productization Program.
- Active scope: S-039 Application-Service Boundary and Source-Document Contract (`AWAITING_HUMAN_VALIDATION`), owned by Human.
- Primary focus: review whether S-039 document identity and bounded provenance are sufficient for S-040/S-041. S-040 through S-043 remain inactive and unauthorized.
- Timing, playback, navigation, and adaptation semantics are intentionally stable during this phase.
- Canonical status and roadmap live in [docs/management/](docs/management/index.md).

## Core Capabilities

- Mobile-first Flask/HTML5 RSVP reader.
- Parser-assisted semantic chunking is the provisional Flask prototype default.
- Pure-Python rule-based semantic chunker remains the mandatory fallback and explicit baseline.
- Deterministic timing engine.
- Phone-browser playback with tap, swipe, hold-swipe, and long-press controls.
- Session-only speed controls, debug summary, and conservative adaptation.
- In-app compressed Markdown defect reports with security hardening.
- Quote/parenthetical display-state metadata.
- Passive spatial anchor, coarse seek, breakpoint traversal, ghost previous chunk, drift recovery, and structural hierarchy anchor.
- Validation corpus, defect taxonomy, and review utilities.

## Quick Start

Use the authoritative [Development Environment Contract](docs/development/environment_contract.md) to select the `standard` or `core` profile, create a Python 3.12 environment, verify exact dependencies, capture environment identity, and start the local development server. The `core` profile requires `RSVP_CHUNKER_MODE=rule_based`; the `standard` profile uses parser-assisted chunking by default.

## Test

```bash
python -m pytest
python scripts/check_js_syntax.py
python scripts/validate_repository_integrity.py
```

`scripts/check_js_syntax.py` uses `node --check` or `nodejs --check` when available. If Node is missing locally, it skips cleanly; CI installs Node and enforces the check.

GitHub Actions runs compact `integrity`, dependency-light `core`, and pinned parser-default `parser` jobs. The integrity validator checks management/evidence structure, finalized integration identities, registered hashes, committed placeholders, and private blind-identity filenames; the existing Markdown, corpus, and frozen-baseline validators run alongside it.

## Security Checks

```bash
python scripts/run_security_checks.py
```

The runner uses optional public tools such as Bandit, pip-audit, Semgrep, Gitleaks, and detect-secrets when they are available locally, and skips missing tools clearly. See [docs/security/](docs/security/index.md) for details.

## Development Workflow

- Use `python -m pytest` before committing.
- Use the prepare screen to load validation samples.
- Use in-app defect reporting during reader playback.
- Review saved reports with `scripts/review_defects.py`.
- Keep behavior changes tied to observed validation evidence.

More details:

- [Setup](docs/development/setup.md)
- [Development environment contract](docs/development/environment_contract.md)
- [Testing](docs/development/testing.md)
- [Architecture](docs/development/architecture.md)
- [Manual validation](docs/development/manual_testing.md)

## Documentation Map

- [Docs index](docs/index.md)
- [Security docs](docs/security/index.md)
- [Feature docs](docs/index.md#features)
- [Parser-assisted chunking experiment](docs/experiments/parser_assisted_chunking/README.md)
- [Validation docs](docs/validation/index.md)
- [Management docs](docs/management/index.md)
- [Defect taxonomy](docs/validation/defect_taxonomy.md)
- [Validation corpus](docs/validation/corpus.md)

## Current Roadmap

See [docs/management/STATUS.md](docs/management/STATUS.md) for the active slice and [docs/management/roadmap.md](docs/management/roadmap.md) for the canonical Now / Next / Later / Parked roadmap.

## Non-Goals

- No public performance claims.
- No permanent universal commitment to spaCy or any single parser provider.
- No frontend framework, npm toolchain, or browser automation.
- No accounts, analytics, service workers, database, or cloud sync.
- No native app, PDF ingestion, or production-grade deployment infrastructure in the current phase.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
