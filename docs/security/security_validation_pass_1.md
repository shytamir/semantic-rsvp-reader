# Security Validation Pass 1

Date: 2026-07-10

## Purpose

Run a quick development security validation pass using lightweight static/public checks where available, inspect obvious Flask/frontend/file-writing footguns, and leave behind a repeatable checklist.

## Scope

In scope:

- Python static security scan orchestration.
- Dependency vulnerability scan orchestration.
- Secret leakage scan orchestration.
- Basic Flask/dev-server footgun review.
- Defect-report storage path and input-safety review.
- Frontend unsafe DOM insertion review.
- Git hygiene review for generated/private artifacts.

Out of scope:

- Production auth, accounts, rate limiting, CSP overhaul, deployment hardening, secrets-management infrastructure, cloud security, WAF rules, containers, formal compliance, frontend rewrites, and heavy dependencies.

## Validators Attempted

The new runner supports:

- `bandit -r semantic_rsvp -q`
- `pip-audit -r requirements.txt`
- `semgrep --config semgrep.yml --error semantic_rsvp static templates` when a repo-local `semgrep.yml` exists
- `gitleaks detect --source . --no-banner`
- `detect-secrets scan --all-files`

The runner uses only Python standard library code, checks whether each tool exists on `PATH`, and skips missing tools clearly.

Semgrep is intentionally not run with registry/auto configs in this script, because this pass avoids network-backed checks inside the runner.

## Validators Available Locally

None of the optional validators were available in this environment.

Actual runner output:

```text
Security check summary:
- bandit: skipped - bandit not found on PATH
- pip-audit: skipped - pip-audit not found on PATH
- semgrep: skipped - semgrep not found on PATH
- gitleaks: skipped - gitleaks not found on PATH
- detect-secrets: skipped - detect-secrets not found on PATH
```

## Findings

- Frontend user text is rendered with `textContent`; no `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `eval`, or dynamic script creation was found.
- Defect reports use generated filenames rather than user-controlled paths.
- Defect report fields are bounded and escaped before Markdown rendering.
- Request bodies have a Flask `MAX_CONTENT_LENGTH` limit.
- Compressed reports are written under a configured report directory.
- No tracked `.venv`, `.pytest_cache`, generated defect reports, or compressed `.md.gz` defect artifacts were found.
- Direct `python semantic_rsvp/web.py` previously forced Flask debug mode.

## Fixes Made

- Added `scripts/run_security_checks.py`.
- Changed direct `python semantic_rsvp/web.py` execution so debug mode is opt-in via `FLASK_DEBUG=1`.
- Added `.env`, `*.log`, and `Thumbs.db` to `.gitignore`.
- Added security documentation and README/testing links.

## False Positives / Accepted Development Risks

- The development server can bind to `0.0.0.0` because phone-on-LAN validation is an explicit project workflow. This remains a development-only setup, not a deployment recommendation.
- The security runner skips missing optional tools instead of failing; this is intentional so the repo does not gain heavy development dependencies or brittle CI behavior.
- Semgrep is skipped unless a repo-local `semgrep.yml` exists. The script does not install Semgrep, fetch registry rules, or add it to CI.

## How To Rerun

```bash
python scripts/run_security_checks.py
python -m pytest
python scripts/check_js_syntax.py
```

## Verification Results

- `python -m pytest`: 195 passed.
- `python scripts/check_js_syntax.py`: ran and skipped cleanly because no local `node` or `nodejs` runtime was available.
- `python scripts/run_security_checks.py`: ran and skipped all optional validators because none were available on `PATH`.

Optional local tools:

```bash
python -m pip install bandit pip-audit detect-secrets
```

Install `semgrep` and `gitleaks` using their official installation instructions if those checks are desired locally.

## Notes For Future Passes

- Consider running the optional tools in a developer environment where they are installed.
- Do not add the runner as a hard CI gate unless optional tool absence remains non-failing.
- Treat production security work as a separate, scoped pass.
