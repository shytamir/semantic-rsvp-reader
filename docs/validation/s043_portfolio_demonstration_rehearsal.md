# S-043 Portfolio Demonstration Rehearsal

## Immutable Demonstration Identity

- Demonstration SHA: `2d16a91fdfc95c384094de5f6cf0d59f666dcd8c`.
- Profile: `standard` (`parser_assisted` default; mandatory automatic rule-based fallback).
- Runtime: Python 3.12.x and the exact accepted dependencies in the [environment contract](../development/environment_contract.md).
- Startup: `python -m flask --app semantic_rsvp.web:create_app run`.
- Intended environments: documented managed Windows development environment; established Samsung Galaxy S23 Ultra / Android 16 / Firefox 152 qualitative path.
- Formats: pasted text/Markdown and the deliberately limited supported EPUB subset.
- Withdrawal: stop using the pinned SHA and record a blocker on issue #18 if a reproducible demonstration defect invalidates a supported claim. No tag or mutable alias is used.

## Automated Evidence

The complete package commit was validated without changing application behavior:

- `python scripts/build_portfolio_demo_epub.py --check`: passed; the committed EPUB exactly matches deterministic output from the project-owned fixture elements.
- Focused EPUB/package tests: 16 passed.
- Full Python suite: 336 passed, 1 skipped. The first managed-workspace run executed all cases successfully but could not clean a shared sandbox temp symlink; the clean rerun used a verified checkout-local `--basetemp`.
- Markdown links, repository integrity, visible chunking corpus, frozen rule-based baseline, and S-037 characterization checks: passed.
- Standard-profile identity: Python `3.12.13`; Flask `3.1.3`; pytest `9.1.1`; Click `8.1.8`; spaCy `3.7.5`; `en-core-web-sm` `3.7.1`; `/health` reported configured and active `parser_assisted`, provider available, and `rule_based` fallback. `pip check` and the Flask smoke passed.
- Local JavaScript syntax: skipped because Node/nodejs was unavailable. CI supplied the applicable Node and browser evidence.
- Optional security tools Bandit, pip-audit, Semgrep, Gitleaks, and detect-secrets: unavailable and reported as skips.
- GitHub Actions CI run [29216823831](https://github.com/shytamir/semantic-rsvp-reader/actions/runs/29216823831): terminal success for core, integrity, and browser-smoke jobs.
- GitHub CodeQL run [29216823472](https://github.com/shytamir/semantic-rsvp-reader/actions/runs/29216823472): terminal success for Actions, Python, and JavaScript/TypeScript analyses.

This is objective package/startup evidence, not human rehearsal evidence. No screenshots, recording, rehearsal timings, or qualitative observations were fabricated.

## Fixed Human Rehearsal Protocol

Human records observations without changing the twelve steps:

1. Confirm the pinned SHA opens in the intended Windows environment.
   - Evidence:
2. Complete setup and startup using only committed instructions.
   - Evidence:
3. Complete the short protocol within three to five minutes.
   - Evidence:
4. Complete the full protocol without undocumented recovery steps.
   - Evidence:
5. Confirm both prepared text and EPUB paths behave as documented.
   - Evidence:
6. Confirm contents navigation, heading jumps, and paused continuity remain coherent.
   - Evidence:
7. Confirm the established mobile/browser path supports the critical EPUB workflow.
   - Evidence:
8. Check every spoken or displayed technical claim against committed evidence.
   - Evidence:
9. Replace a failed live path with the bounded fallback without exposing private material.
   - Evidence:
10. Confirm no hidden dependency, sensitive source, credential, or private evaluation asset is required.
    - Evidence:
11. Explain the known limitations clearly without undermining the demonstrated value.
    - Evidence:
12. Record every blocker or presentation friction before disposition.
    - Evidence:

## Human Disposition

Owner: Human. Select exactly one after the rehearsal; Codex must not fill this section:

- `portfolio_demo_ready`
- `ready_with_known_limitations`
- `rehearsal_blocked`
- `documentation_blocked`
- `inconclusive`

Disposition:

Notes:
