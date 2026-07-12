# Testing

Environment/profile setup and dependency verification are governed by the [Development Environment Contract](environment_contract.md). This file summarizes repository test surfaces rather than duplicating those setup procedures.

Risk-based gate selection, evidence terminology, and traceability are governed by the [QA Authority](../qa/index.md).

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

S-038 adds one bounded Playwright runner without a package manifest, lockfile,
frontend framework, bundler, transpiler, Jest, Selenium, or general npm
workflow. To reproduce the CI browser smoke in an environment with Node.js 22:

```bash
npm install --no-save --package-lock=false playwright@1.61.1
npx playwright install chromium
node scripts/run_browser_smoke.mjs
```

The runner starts the Flask app in explicit `rule_based` mode, uses a
deterministic fixture, and protects text loading, play/pause, progress seeking,
breakpoint creation, reset, and one catastrophic narrow-layout invariant.

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
- The bounded S-038 Playwright/Chromium browser smoke in its own CI job.
- Parser CI coverage for the S-024/S-037 evaluation surface: path triggers, manual dispatch, the two focused evaluation test files, and the committed S-037 characterization check under the pinned standard profile.

Reproduce the S-038A focused evidence in the standard profile with:

```bash
python -m pytest tests/test_s024_comparison.py tests/test_s037_evaluation_anomaly_characterization.py
python scripts/characterize_s037_evaluation_anomalies.py --check
```

Security checks are not a hard CI gate in this development pass because the validators are optional local tools.

Commits `58576ba` and `3177188` updated only the GitHub Actions environment setup versions used by the existing workflows to eliminate Node 20 deprecation alerts. The human validated the resulting workflows successfully. This is completed DevOps runtime maintenance, not S-033 validation evidence or an S-033 outcome.

## Slice-document archive maintenance

Check whether completed slice documents fall outside the active slice and two-previous-ordinal working-memory window:

```bash
python scripts/archive_slice_docs.py --check
```

The current slice in `docs/management/STATUS.md` defines the boundary. Completed groups at current minus three or earlier are archived without file-count thresholds or gap backfilling. When the check prints a pending plan, start from a clean worktree and apply it explicitly with `--apply`. Review and commit the resulting moves, link rewrites, and archive indexes. CI never applies or commits archival changes.

## Validation-Driven Testing

Chunking, timing, navigation, and layout changes should be paired with focused regression tests derived from observed validation reports whenever practical.
