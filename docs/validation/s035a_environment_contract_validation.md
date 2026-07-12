# S-035A Development Environment Contract Validation

## Automated Evidence

- The known-successful managed Windows environment runs Python `3.12.13` with Flask `3.1.3`, pytest `9.1.1`, Click `8.1.8`, spaCy `3.7.5`, and `en-core-web-sm` `3.7.1`; `python -m pip check` passes.
- A disposable clean Windows `core` environment installed from `requirements-core.txt`, reported the accepted Flask/pytest versions, passed `python -m pip check`, passed the rule-based smoke test, and passed 15 focused environment/service/storage tests.
- The current standard environment passes the pinned parser/API suite. A separate disposable clean `standard` installation did not finish within the automated execution window and is not recorded as passed.
- Ubuntu Python 3.12 and Node.js 22 are CI configuration claims; this preparation did not inspect a resulting remote run.
- POSIX procedures are documented but were not executed on this Windows host.

## Fixed Human Protocol

Use the committed [Development Environment Contract](../development/environment_contract.md) and record the target commit, shell, operating system, profile, and every command outcome.

The prior attempt created a Python 3.14 environment, as shown by the `cp314`
wheel tags in the preserved failure below. Python 3.14 is outside the S-035A
contract. Before retrying, follow the contract's removal instructions for the
failed checkout-local `.venv`.

1. In Windows PowerShell, run the clean `standard` procedure exactly, beginning with `py -3.12 -m venv .venv`. Confirm that the mandatory version assertion passes before dependency installation, then confirm `python -m pip check`, accepted dependency versions, parser-default smoke behavior, and `/health` identity.
2. Remove that checkout-local `.venv` using the contract's safe retry instructions. In Windows PowerShell, run the clean `core` procedure exactly, again beginning with `py -3.12 -m venv .venv` and completing the version assertion before installation. Confirm dependency consistency, rule-based smoke behavior, and `/health` identity.
3. Confirm the environment-identity commands capture commit SHA, profile, Python, key dependency versions, and configured/active chunker state without manual reconstruction.
4. Review the configuration table against actual startup behavior, especially that only `RSVP_CHUNKER_MODE` has the documented app-config/environment precedence and that the three Flask-config-only settings are not presented as environment variables.
5. Record `passed`, `partially_passed`, `failed`, or `inconclusive`, plus any separate issue needed for a contradiction requiring application-level configuration redesign. POSIX execution is not part of this human gate.

The corrected standard procedure clears an inherited `RSVP_CHUNKER_MODE`
before running tests. The baseline check accepts any supported Python 3.12
patch only for its historical `python_version` metadata field; all frozen cases,
configuration, hashes, dependencies, and outputs remain exact comparisons.

## Human Disposition

After pushing some fixes from CODEX I was able to complete the protocol.

standard venv `passed` health identity: {"chunking":{"active_mode":"parser_assisted","configured_mode":"parser_assisted","fallback":"rule_based","provider":"spacy:3.7.5/en_core_web_sm:3.7.1","provider_available":true,"provider_reason":"available"},"status":"ok"}

core venv `passed` health identity: {"chunking":{"active_mode":"rule_based","configured_mode":"rule_based","fallback":"rule_based","provider":null,"provider_available":false,"provider_reason":"not_configured"},"status":"ok"}

The configuration contract was fulfilled correctly.