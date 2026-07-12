# Development Setup

The [Development Environment Contract](environment_contract.md) is the authority for Python support, the `standard` and `core` profiles, exact dependency versions, PowerShell/POSIX setup, configuration precedence, identity capture, and clean environment recreation. Do not infer support for other profile names, Python minors, or operating systems from this summary.

Use `standard` for ordinary parser-default development and `core` with `RSVP_CHUNKER_MODE=rule_based` for dependency-light fallback work. Always install with `python -m pip` and run `python -m pip check` as specified by the contract.

## Run The App

```bash
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Use `--host 0.0.0.0` when testing from a phone or another device on the same network.

The default mode is `parser_assisted`; explicit `rule_based` mode and automatic fallback remain available as documented in the contract.

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
