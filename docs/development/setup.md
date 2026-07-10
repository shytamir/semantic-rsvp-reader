# Development Setup

## Requirements

- Python 3.12 or compatible Python 3 runtime.
- Flask dependencies from `requirements.txt`.
- Optional Node.js runtime for local JavaScript syntax checks.

## Local Environment

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run The App

```bash
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Use `--host 0.0.0.0` when testing from a phone or another device on the same network.

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
