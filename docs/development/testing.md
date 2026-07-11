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

## Security Checks

```bash
python scripts/run_security_checks.py
```

The security runner uses optional public tools such as Bandit, pip-audit, Semgrep, Gitleaks, and detect-secrets when they are available locally. Missing tools are reported as skipped. Semgrep requires a repo-local `semgrep.yml` so the runner does not rely on network-backed registry configs. The script does not install dependencies, intentionally make network calls, or modify files.

## CI

GitHub Actions runs:

- Python dependency installation.
- `python -m pytest`.
- JavaScript syntax checking with Node installed by CI.

Security checks are not a hard CI gate in this development pass because the validators are optional local tools.

## Slice-document archive maintenance

Check whether completed slice documents exceed the deterministic root retention limits:

```bash
python scripts/archive_slice_docs.py --check
```

When the check prints a pending plan, start from a clean worktree and apply it explicitly with `--apply`. Review and commit the resulting moves, link rewrites, and archive indexes. CI never applies or commits archival changes.

## Validation-Driven Testing

Chunking, timing, navigation, and layout changes should be paired with focused regression tests derived from observed validation reports whenever practical.
