# Development Setup

## Requirements

- Python 3.12 or compatible Python 3 runtime.
- Standard prototype dependencies from `requirements.txt`, including pinned server-side parser-assisted chunking dependencies.
- Optional Node.js runtime for local JavaScript syntax checks.

## Local Environment

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

The standard prototype install pins spaCy `3.7.5` and `en-core-web-sm` `3.7.1`. The Flask server uses them only for the provisional parser-assisted chunking path; the browser client does not download or execute spaCy.

For dependency-light fallback development without spaCy:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-core.txt
set RSVP_CHUNKER_MODE=rule_based
```

## Run The App

```bash
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Use `--host 0.0.0.0` when testing from a phone or another device on the same network.

Set `RSVP_CHUNKER_MODE=rule_based` to force the deterministic baseline. The default mode is `parser_assisted`; parser failures or missing parser dependencies fall back automatically to the rule-based chunker.

Open:

- Host machine: `http://127.0.0.1:5000`
- External device: `http://<host LAN IP>:5000`

## Useful Commands

Inspect a schedule from a file:

```bash
python scripts/schedule_sample.py sample.txt
```

Inspect a schedule from stdin:

```bash
python scripts/schedule_sample.py --json < sample.txt
```

Review stored defect reports:

```bash
python scripts/review_defects.py
```
