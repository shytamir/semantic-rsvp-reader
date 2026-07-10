# Repository Maintenance Pass 1

Date: 2026-07-10

## What Was Audited

- Root files: `README.md`, `TODO.md`, `.gitignore`, `pyproject.toml`, `requirements.txt`.
- Documentation: `docs/`, `docs/management/`, `docs/validation/`, `docs/architecture/`.
- Code and UI structure: `semantic_rsvp/`, `templates/`, `static/`.
- Tooling and tests: `.github/workflows/`, `scripts/`, `tests/`.
- Tracked files via `git ls-files`.

## README Changes

- Replaced the long project-history README with a concise front page.
- Kept quick answers for purpose, status, capabilities, setup, tests, documentation map, roadmap, and non-goals.
- Moved detailed setup/testing/manual-validation/feature material into linked Markdown docs.

## Docs Moved Or Extracted

New development docs:

- `docs/development/setup.md`
- `docs/development/testing.md`
- `docs/development/architecture.md`
- `docs/development/manual_testing.md`

New feature docs:

- `docs/features/chunking.md`
- `docs/features/timing.md`
- `docs/features/navigation.md`
- `docs/features/defect_reporting.md`
- `docs/features/adaptation.md`

New index docs:

- `docs/index.md`
- `docs/management/index.md`
- `docs/validation/index.md`

## Canonical Docs Chosen

- Status: `docs/management/STATUS.md`
- Roadmap: `docs/management/roadmap.md`
- Detailed TODO: `docs/management/TODO.md`
- Validation map: `docs/validation/index.md`

Root `TODO.md` remains as a short pointer and current-focus summary. `docs/project_status.md` is now a compatibility stub pointing to the canonical status file.

## Stale Claims Corrected

- README no longer presents a full project history as front-page content.
- Root status path no longer duplicates canonical management status.
- Management TODO no longer leaves the pass-2 validation follow-up as the active next step.
- Status terminology now uses validation-driven refinement instead of stale chunker-dominant wording where appropriate.

## Generated / Outlier Files

Tracked files did not include `.venv`, `.pytest_cache`, generated defect reports, `__pycache__`, or `.gz` defect artifacts.

Local untracked development directories observed:

- `.venv/`
- `.pytest_cache/`

These are ignored.

## `.gitignore` Changes

- Added `*.md.gz` to reduce risk of accidentally tracking compressed defect reports outside `data/defect_reports/`.

## Link / Index Changes

- Added `docs/index.md` as the top-level documentation map.
- Added management and validation index pages.
- Linked the README to canonical setup, testing, architecture, validation, feature, and management docs.

## Tests Run

- `python -m pytest`: 195 passed.
- `python scripts/check_js_syntax.py`: ran and skipped cleanly because no local `node` or `nodejs` runtime was available.

## Known Remaining Cleanup

- Historical validation files are intentionally preserved and not rewritten.
- Manual validation docs are summarized; historical long-form protocols remain in validation documents.
- No dedicated Markdown link checker was added; links were checked lightly with a local script during the pass.
