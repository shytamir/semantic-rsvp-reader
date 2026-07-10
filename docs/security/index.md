# Security Docs

This project is an early development prototype. Security work here is lightweight hygiene, not production hardening.

## Current Security Notes

- [Security Validation Pass 1](security_validation_pass_1.md)
- [Defect reporting feature notes](../features/defect_reporting.md)
- [In-app defect reporting workflow](../validation/in_app_defect_reporting.md)

## Quick Check

```bash
python scripts/run_security_checks.py
```

The runner uses optional public tools when they are available locally and skips missing tools clearly. It does not install dependencies, make project changes, or provide a production security guarantee.
