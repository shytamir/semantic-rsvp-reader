# S-043A2 EPUB Application Integration Evidence

## Outcome

S-043A2 completed as `passed` on 2026-07-13 from objective evidence. Issues #27 and #28 remain open pending the next management transition. Parent S-043 rehearsal remains suspended, historical demonstration SHA `2d16a91fdfc95c384094de5f6cf0d59f666dcd8c` remains immutable and is not the active rehearsal target, and S-043A3 remains provisional, inactive, and unauthorized.

## Implemented Boundary

- Existing `POST /api/epub/schedule` receives the same raw media type, filename hint, and dedicated request limit.
- The configured S-043A1 preparer runs first; only `result.data` reaches the unchanged final EPUB adapter.
- Exact original bytes are handed through for `unchanged`; deterministic transient bytes are handed through for `normalized`.
- The existing schedule service, response document identity, paused reader initialization, contents mapping, breakpoints, and continuity restoration remain unchanged.
- The response adds only bounded preparation mode, detected EPUB version, discarded-resource count, and transformation category names.
- No source/prepared archive bytes, hashes, converted download, server file, browser storage field, route, selector, or converter-policy change was added.

## Objective Evidence

- Focused API, preparation, continuity, and contents tests: 21 passed, 1 documented Node-dependent skip.
- Preparation-order seam proves raw request bytes reach the preparer first and the final adapter receives the exact returned bytes object only.
- Project-owned safe EPUBs report `unchanged`; the existing canonical identity and schedule contract remain stable.
- Project-owned legacy-doctype, `<link>`, `<meta>`, and removable-style input reports `normalized`, reaches final ingestion, and produces stable identity across filenames.
- Malformed and encrypted inputs remain bounded `400` failures and do not enter the reader.
- Existing dedicated EPUB versus JSON request-size test remains passing.
- Static continuity/browser assertions exclude source/prepared byte fields; bounded preparation metadata contains no bytes or hashes.
- Extended browser smoke covers unchanged, normalized/reselection continuity, paused heading position, and rejected paths. Local execution was unavailable because the managed Playwright package lacked `playwright-core`; terminal CI is the required browser result.
- Complete Python suite initially executed 345 passes and 1 existing skip; its sole failure was the expected registered `web.py` hash mismatch caused by this authorized route edit. Only that registered normalized-text SHA-256 was updated before the clean repair rerun.
- Frozen rule-based baseline and S-037 characterization remained reproducible.
- Local JavaScript syntax via the repository wrapper reported Node unavailable; direct managed-Node syntax validation is recorded after the final edit.
- Optional security tools Bandit, pip-audit, Semgrep, Gitleaks, and detect-secrets were unavailable and reported as skips.

Terminal remote evidence for implementation commit `a7731af361fab49aaca7025643d9f1d38b15c1ec` is recorded on issues #27 and #28: CI run `29219544902` passed core, integrity, and extended browser smoke; Parser CI run `29219544919` passed; CodeQL run `29219544707` passed Actions, Python, and JavaScript/TypeScript analyses.
