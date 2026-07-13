# S-043A1 Demo-Safe EPUB Preparation Evidence

## Outcome

S-043A1 completed as `passed` on 2026-07-13. The parent S-043 Human rehearsal remains suspended, historical demonstration SHA `2d16a91fdfc95c384094de5f6cf0d59f666dcd8c` remains immutable evidence and is not the active target, issue #27 remains open, and S-043A2 awaits explicit management activation.

## Implemented Boundary

- `prepare_epub` returns exact original bytes in `unchanged` mode when the final adapter accepts them.
- `normalized` mode produces deterministic minimal EPUB bytes after bounded EPUB 2/3 inspection and safe XHTML simplification.
- `EpubPreparationError` rejects encryption, malformed or unsafe containers, resource-limit violations, unreadable content, and ambiguous structures without including source text.
- Every successful result is passed through `ingest_epub_document` and rule-based `ScheduleService` generation before return.
- The offline CLI refuses same paths and implicit overwrites, leaves input untouched, writes a same-directory temporary file, and replaces output only after successful verification.
- No Flask/browser integration, final-adapter change, network access, telemetry, demonstration refresh, third-party content, or successor activation is included.

## Objective Evidence

- Focused preparation and final-adapter tests: 16 passed.
- Exact no-op evidence: returned object retains the original bytes; SHA-256, ZIP representation, unrelated resource bytes, and canonical `SourceDocument` identity remain equal.
- Normalization evidence: project-owned synthetic EPUB 2 and EPUB 3 cases preserve linear readable text, H1/H2 structure, lists and block quotes; H3/H4 text is retained without promotion; removable markup/resources are excluded.
- Determinism evidence: repeated preparation of identical source bytes produces identical normalized bytes; preparing normalized output returns exact-byte `unchanged`; canonical identity remains stable.
- Rejection evidence: encrypted, unsafe-path, malformed, and ambiguous table inputs raise bounded failures; existing adapter resource-limit tests remain passing.
- CLI evidence: exact-copy no-op, deterministic normalized output, same-path refusal, overwrite protection, successful final ingestion, and failed-write cleanup passed.
- Complete Python suite: 344 passed, 1 skipped.
- Frozen rule-based baseline and S-037 characterization: reproducible.
- Optional security tools Bandit, pip-audit, Semgrep, Gitleaks, and detect-secrets: unavailable and reported as skips.

Terminal remote evidence for implementation commit `22c9a8b68ef222473eaca25deeca643291e06fae` is recorded on issue #27: CI run `29218777855`, Parser CI run `29218777861`, and CodeQL run `29218777624` all completed successfully.
