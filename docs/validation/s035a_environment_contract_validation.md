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

## Human Disposition

Validation failed in the first step of the protocol. Did not proceed to next steps. Returning to CODEX with the pytest failures report appended below.

```
====================================================== FAILURES =======================================================
______________________________________ test_rule_based_baseline_is_reproducible _______________________________________

    def test_rule_based_baseline_is_reproducible():
        regenerated = build_baseline_payload()
        committed = load_json(BASELINE_OUTPUT_PATH)

>       assert regenerated == committed
E       AssertionError: assert {'metadata': ...', ...}, ...]} == {'cases': [{'...9.1.1'}, ...}}
E
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'metadata': {'baseline_commit': '8b50a3049bb5d92a304a03527385c519194ce8da', 'python_version': '3.12.10', 'dependency_...': {'Flask': '3.1.3...
E
E         ...Full output truncated (2 lines hidden), use '-vv' to show

tests\test_parser_assisted_chunking_freeze.py:39: AssertionError
________________________________________ test_freeze_script_check_mode_passes _________________________________________

    def test_freeze_script_check_mode_passes():
        result = subprocess.run(
            [sys.executable, "scripts/freeze_chunking_baseline.py", "--check"],
            text=True,
            capture_output=True,
            check=False,
        )

>       assert result.returncode == 0, result.stdout + result.stderr
E       AssertionError: Rule-based baseline output changed:
E         --- evaluation\parser_assisted_chunking\baseline\rule_based_baseline.json
E         +++ regenerated-baseline
E         @@ -4754,7 +4754,7 @@
E                "regression": "e9c55c2e957c924d699b57e2622111f044997e821d43d472c7b203b28ba4fe68"
E              },
E              "normalization_entry_point": "semantic_rsvp.text.normalize.normalize_text",
E         -    "python_version": "3.12.13",
E         +    "python_version": "3.12.10",
E              "schedule_entry_point": "semantic_rsvp.timing.schedule.schedule_text",
E              "segmentation_entry_point": "semantic_rsvp.text.segment.split_sentences",
E              "timing_config": {
E
E       assert 1 == 0
E        +  where 1 = CompletedProcess(args=['D:\\Shy\\semantic-rsvp-reader\\.venv\\Scripts\\python.exe', 'scripts/freeze_chunking_baseline....n     "segmentation_entry_point": "semantic_rsvp.text.segment.split_sentences",\n     "timing_config": {\n', stderr='').returncode

tests\test_parser_assisted_chunking_freeze.py:50: AssertionError
___________________________ test_s035_service_characterization_is_complete_and_reproducible ___________________________

    def test_s035_service_characterization_is_complete_and_reproducible():
        report = build_report()

        assert report["hard_failures"] == []
>       assert report["default_state"]["configured_mode"] == "parser_assisted"
E       AssertionError: assert 'rule_based' == 'parser_assisted'
E
E         - parser_assisted
E         + rule_based

tests\test_s035_service_surfaces_characterization.py:10: AssertionError
-------------------------------------------------- Captured log call --------------------------------------------------
WARNING  semantic_rsvp.chunking.selection:selection.py:71 Parser-assisted chunker fell back to rule_based; reason_category=parser_unavailable
_____________________ test_standard_profile_api_contracts_use_real_pinned_parser_and_json_records _____________________

    def test_standard_profile_api_contracts_use_real_pinned_parser_and_json_records():
        app = create_app({"TESTING": True})
        client = app.test_client()

        health = client.get("/health")
        assert health.status_code == 200
>       assert health.get_json()["chunking"]["configured_mode"] == "parser_assisted"
E       AssertionError: assert 'rule_based' == 'parser_assisted'
E
E         - parser_assisted
E         + rule_based

tests\test_standard_profile_api.py:23: AssertionError
___________________________________ test_app_creation_uses_parser_assisted_default ____________________________________

    def test_app_creation_uses_parser_assisted_default():
        app = create_app({"TESTING": True})

>       assert app.config["RSVP_CHUNKER_MODE"] == "parser_assisted"
E       AssertionError: assert 'rule_based' == 'parser_assisted'
E
E         - parser_assisted
E         + rule_based

tests\test_web_chunking_integration.py:9: AssertionError
=============================================== short test summary info ===============================================
FAILED tests/test_parser_assisted_chunking_freeze.py::test_rule_based_baseline_is_reproducible - AssertionError: assert {'metadata': ...', ...}, ...]} == {'cases': [{'...9.1.1'}, ...}}
FAILED tests/test_parser_assisted_chunking_freeze.py::test_freeze_script_check_mode_passes - AssertionError: Rule-based baseline output changed:
FAILED tests/test_s035_service_surfaces_characterization.py::test_s035_service_characterization_is_complete_and_reproducible - AssertionError: assert 'rule_based' == 'parser_assisted'
FAILED tests/test_standard_profile_api.py::test_standard_profile_api_contracts_use_real_pinned_parser_and_json_records - AssertionError: assert 'rule_based' == 'parser_assisted'
FAILED tests/test_web_chunking_integration.py::test_app_creation_uses_parser_assisted_default - AssertionError: assert 'rule_based' == 'parser_assisted'
=========================================== 5 failed, 286 passed in 18.09s ============================================
```
