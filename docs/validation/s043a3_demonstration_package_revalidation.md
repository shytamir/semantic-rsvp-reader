# S-043A3 Demonstration Package Revalidation

## Outcome

S-043A3 completed as `passed` on 2026-07-13 from objective evidence. The complete replacement package is immutable commit `88cc5433d85c6dcfc632412f6796af25702e1c7b`. Historical commit `2d16a91fdfc95c384094de5f6cf0d59f666dcd8c` remains immutable evidence and is withdrawn only as the active rehearsal identity.

Issues #27, #28, and #29 are closed after final chain reconciliation. Issue #18 remains open. S-043 returns to `AWAITING_HUMAN_VALIDATION`, owned by Human, with the fixed twelve-step protocol blank and restarted from step 1.

## Package Evidence

- The builder reproducibly verifies project-owned unchanged, normalization-required, and encrypted-rejection EPUBs.
- `unchanged` preserves exact bytes and canonical identity.
- `normalized` is deterministic across repeats, preserves H1/H2 and reader identity, and demonstrates legacy-doctype, `<link>`, `<meta>`, CSS, and style removal.
- The encrypted fixture produces a bounded rejection without opening the reader.
- Short/full protocols, fallback commands, claims, privacy boundary, and limitations match S-043A1/A2 behavior.
- No screenshot, recording, rehearsal timing, Human observation, or disposition was fabricated.

## Validation

- Focused package, preparation, and application tests: 19 passed.
- Complete Python suite: 347 passed, 1 existing skip.
- Deterministic fixture check, JavaScript syntax, Markdown links, repository integrity, frozen baseline, S-037 characterization, dependency check, standard-profile identity, `/health`, and Flask smoke: passed.
- Optional security tools were unavailable and reported as skips.
- CI run `29220233534`: core, integrity, and extended browser smoke passed.
- CodeQL run `29220233356`: Actions, Python, and JavaScript/TypeScript passed.
