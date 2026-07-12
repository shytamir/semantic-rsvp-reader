# Development Environment Contract

This document is the authority for supported development runtime, profiles, setup, configuration, source-checkout deployment, and environment identity. These are development and bounded-validation contracts, not production runtime packages or a production hosting design.

## Support And Evidence Boundaries

- Supported development runtime: Python `3.12.x`.
- CI-tested environment: Ubuntu with Python 3.12; the core job uses Node.js 22 for JavaScript syntax validation, and the bounded browser-smoke job uses Node.js 22, pinned Playwright `1.61.1`, and Chromium.
- Documented setup shells: Windows PowerShell and POSIX-compatible shells. Documentation is not evidence that every shell/platform procedure was executed.
- Node.js is optional for ordinary local startup and required to reproduce `scripts/check_js_syntax.py` or `scripts/run_browser_smoke.mjs`; a missing local Node/browser harness is a reported skip, never a pass.
- The current known-successful managed Windows environment used Python `3.12.13`, Flask `3.1.3`, pytest `9.1.1`, Click `8.1.8`, spaCy `3.7.5`, and `en-core-web-sm` `3.7.1`. S-035 human evidence exercised both profiles; it did not record a broad platform support matrix.
- Parser CI is the authoritative standard-profile remote gate for the S-024/S-037 evaluation surface. It runs the two focused evaluation test files and the committed S-037 characterization check under the existing pinned Python 3.12 environment.

## Canonical Profiles And Accepted Versions

| Profile | Requirements | Required mode | Purpose |
| --- | --- | --- | --- |
| `standard` | `requirements.txt` | Default `parser_assisted` | Ordinary development, parser integration, validation, and normal prototype operation. |
| `core` | `requirements-core.txt` | `RSVP_CHUNKER_MODE=rule_based` | Dependency-light development and fallback validation without parser dependencies. |

Accepted versions are derived from the successful Python 3.12 environment and pinned requirements, not selected from latest releases:

| Dependency | Accepted version | Profiles |
| --- | --- | --- |
| Flask | `3.1.3` | `standard`, `core` |
| pytest | `9.1.1` | `standard`, `core` |
| Click | `8.1.8` | `standard` |
| spaCy | `3.7.5` | `standard` |
| `en-core-web-sm` | `3.7.1` | `standard` |

Do not use alternative profile names such as `full`, `normal`, `default`, `minimal`, or `nlp`.

## Setup Procedures

Start from a source checkout at the commit that will be tested.

### Windows PowerShell

The Windows procedures require the Python launcher to select Python 3.12
explicitly. Before retrying a failed setup, deactivate the environment if it is
active and remove only this checkout's failed environment:

```powershell
deactivate
Remove-Item -Recurse -Force -LiteralPath .venv
```

If `deactivate` is unavailable because the environment is not active, omit that
command. Confirm that `.venv` is the intended checkout-local path before
removing it.

Standard:

```powershell
py -3.12 -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -c "import sys; assert sys.version_info[:2] == (3, 12), sys.version"
Remove-Item Env:RSVP_CHUNKER_MODE -ErrorAction SilentlyContinue
python -m pip install -r requirements.txt
python -m pip check
python -m pytest
python scripts/check_js_syntax.py
python scripts/smoke_test_app.py
```

Core:

```powershell
py -3.12 -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -c "import sys; assert sys.version_info[:2] == (3, 12), sys.version"
python -m pip install -r requirements-core.txt
python -m pip check
python -m pytest --ignore=tests/test_parser_assisted_spacy_integration.py --ignore=tests/test_standard_profile_api.py
python scripts/check_js_syntax.py
$env:RSVP_CHUNKER_MODE = "rule_based"
python scripts/smoke_test_app.py
```

### POSIX-Compatible Shell

Standard:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
python -m pytest
python scripts/check_js_syntax.py
python scripts/smoke_test_app.py
```

Core:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-core.txt
python -m pip check
python -m pytest --ignore=tests/test_parser_assisted_spacy_integration.py --ignore=tests/test_standard_profile_api.py
python scripts/check_js_syntax.py
RSVP_CHUNKER_MODE=rule_based python scripts/smoke_test_app.py
```

Create separate environments when comparing profiles. To recreate one, deactivate it, remove only that checkout's `.venv`, and repeat the selected procedure. On Windows, never substitute a generic `python -m venv` invocation: it may silently select an unsupported installed Python version.

The standard procedure clears any inherited `RSVP_CHUNKER_MODE` override before
validation so the documented parser-assisted default is actually exercised.
The core procedure sets the override only after its test suite, for the
rule-based smoke check and subsequent core-profile identity capture.

## Configuration Contract

| Setting | Accepted value/type and built-in default | Source and precedence | Exposure and sensitivity |
| --- | --- | --- | --- |
| `RSVP_CHUNKER_MODE` | `parser_assisted` or `rule_based`; default `parser_assisted` | Explicit `create_app(config)` value, then environment variable, then built-in default. | Configured/active mode and provider state appear in `/health`; startup logs include state but not source text. |
| `DEFECT_REPORT_DIR` | Path; default `data/defect_reports` | Flask application config only. No environment-variable support. | Not exposed through `/health`; it may contain sensitive local validation reports. |
| `CHECK_STORAGE_ENCRYPTION` | Boolean; default `True` | Flask application config only. No environment-variable support. | Not exposed through `/health`; an unconfirmed check emits a warning without report contents. |
| `MAX_CONTENT_LENGTH` | Integer bytes; effective default `1_000_000` when Flask config is `None` | Flask application config only. No environment-variable support. | Not exposed through `/health`; bounds request bodies. |
| `FLASK_DEBUG` | String; debug is enabled only when exactly `1`; default disabled | Environment variable read only by direct `python semantic_rsvp/web.py` execution. It is not a symmetric `create_app(config)` setting. | Not exposed through `/health`; development only and must not be used as a production-hosting control. |

These findings document current behavior. No configuration redesign contradiction was found during S-035A.

## Project Identity And Naming

- Repository/deployment identity: `semantic-rsvp-reader`.
- Python import package: `semantic_rsvp`.
- Flask application factory: `semantic_rsvp.web:create_app`.
- Environment-variable prefix: `RSVP_`.
- Profiles: `standard`, `core`.
- Python modules/files: `snake_case`.
- Configuration constants: `UPPER_SNAKE_CASE`.

Existing public names are preserved.

## Source-Checkout Deployment And Identity

The supported development deployment unit is:

> A source checkout at a recorded Git commit, a Python 3.12 virtual environment, and one selected development profile.

Record identity before validation:

```text
git rev-parse HEAD
python --version
python -m pip check
python -c "import importlib.metadata as m; print({n: m.version(n) for n in ('Flask','pytest')})"
python -c "from semantic_rsvp.web import create_app; print(create_app({'TESTING': True}).test_client().get('/health').get_json()['chunking'])"
```

For `standard`, also record Click, spaCy, and model versions:

```text
python -c "import importlib.metadata as m; print({n: m.version(n) for n in ('Click','spacy','en-core-web-sm')})"
```

Record the profile name explicitly. For `core`, set `RSVP_CHUNKER_MODE=rule_based` before capturing health state.

The frozen rule-based baseline records the Python patch version used when it was
created. Its reproducibility check requires Python 3.12 and exact scientific
output and dependency identity, but does not require a different supported
Python 3.12 patch to equal that historical capture field.

Start locally:

```text
python -m flask --app semantic_rsvp.web:create_app run
```

For bounded same-LAN phone validation only:

```text
python -m flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Confirm `http://127.0.0.1:5000/health` and run `python scripts/smoke_test_app.py`. Stop the development server with `Ctrl+C`. The Flask development server is for local development and bounded prototype validation, not production hosting.
