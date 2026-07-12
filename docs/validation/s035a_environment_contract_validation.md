# S-035A Development Environment Contract Validation

## Automated Evidence

- The known-successful managed Windows environment runs Python `3.12.13` with Flask `3.1.3`, pytest `9.1.1`, Click `8.1.8`, spaCy `3.7.5`, and `en-core-web-sm` `3.7.1`; `python -m pip check` passes.
- A disposable clean Windows `core` environment installed from `requirements-core.txt`, reported the accepted Flask/pytest versions, passed `python -m pip check`, passed the rule-based smoke test, and passed 15 focused environment/service/storage tests.
- The current standard environment passes the pinned parser/API suite. A separate disposable clean `standard` installation did not finish within the automated execution window and is not recorded as passed.
- Ubuntu Python 3.12 and Node.js 22 are CI configuration claims; this preparation did not inspect a resulting remote run.
- POSIX procedures are documented but were not executed on this Windows host.

## Fixed Human Protocol

Use the committed [Development Environment Contract](../development/environment_contract.md) and record the target commit, shell, operating system, profile, and every command outcome.

1. In Windows PowerShell, follow the clean `standard` procedure from a new virtual environment. Confirm installation, `python -m pip check`, the accepted dependency versions, the parser-default smoke test, and `/health` identity. Record any unclear or incorrect step.
2. Confirm the environment-identity commands capture commit SHA, profile, Python, key dependency versions, and configured/active chunker state without manual reconstruction.
3. If a POSIX-compatible Python 3.12 environment is actually available, execute one documented profile procedure and record its result. If unavailable, record this step as `skipped`; do not mark it passed.
4. Review the configuration table against actual startup behavior, especially that only `RSVP_CHUNKER_MODE` has the documented app-config/environment precedence and that the three Flask-config-only settings are not presented as environment variables.
5. Record `passed`, `partially_passed`, `failed`, or `inconclusive`, plus any separate issue needed for a contradiction requiring application-level configuration redesign.

## Human Disposition

Pending. S-035A remains `AWAITING_HUMAN_VALIDATION`, owned by the human.
