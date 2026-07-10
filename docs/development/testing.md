# Testing

## Full Test Suite

```bash
python -m pytest
```

The repository includes `pyproject.toml` so pytest imports the local `semantic_rsvp` package directly from a fresh clone.

## JavaScript Syntax Check

```bash
python scripts/check_js_syntax.py
```

The script checks `static/js/app.js` with `node --check` or `nodejs --check` when either runtime is available. If Node is missing locally, the script prints a warning and skips without failing. GitHub Actions installs Node and enforces the syntax check in CI.

No npm packages, frontend framework, bundler, transpiler, Jest, Playwright, or Selenium are used.

## CI

GitHub Actions runs:

- Python dependency installation.
- `python -m pytest`.
- JavaScript syntax checking with Node installed by CI.

## Validation-Driven Testing

Chunking, timing, navigation, and layout changes should be paired with focused regression tests derived from observed validation reports whenever practical.
