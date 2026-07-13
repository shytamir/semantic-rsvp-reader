# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-042: EPUB Ingestion and Long-Document Navigation**
   - State: S-042C `STABILIZATION_IN_PROGRESS`
   - Owner: Codex
   - Active scope: S-042C Lightweight Contents Navigation and Integrated EPUB Validation.
   - Scope: [S-042](s042_epub_long_document_navigation.md); umbrella authority: GitHub issue #17.

## Next

S-043 remains `PROVISIONAL`, inactive, and unauthorized.

## Document Reader Productization Program

Human decision D-010 authorizes program entry after the recorded S-036 `ready` disposition. S-037 through S-042B completed as `passed`; only S-042C is active:

1. **S-037: Evaluation Anomaly Investigation and Parser Operating-Policy Decision** — completed as `passed`; disposition `retain_parser_default_with_mandatory_automatic_fallback`; [scope](archive/s037_evaluation_anomaly_parser_policy.md); GitHub issue #12.
2. **S-038: Minimal Browser Regression Baseline** — completed as `passed`; human-evidence commit `b97c189e55f259fbe80eccc7072d415af6dbb87f`; [scope](archive/s038_minimal_browser_regression_baseline.md); GitHub issue #13.
3. **S-038A: Parser CI Evaluation-Surface Coverage** — completed as `passed`; [scope](archive/s038_parser_ci_evaluation_surface.md).
4. **S-039: Application-Service Boundary and Source-Document Contract** — completed as `passed`; [scope](archive/s039_application_service_source_document_contract.md); human-evidence commit `806dbaea92d9638cc7cea439fe33ce9168f97c58`.
5. **S-040: Plain Text, Markdown, and Bounded Clean-HTML Ingestion** — completed as `passed`; [scope](s040_document_ingestion.md); human-evidence commit `fb618d269f70f5497154f1309db84e69bf8f5451`; GitHub issue #15.
6. **S-041: Local Reading Continuity** — completed as `passed`; [scope](s041_local_reading_continuity.md); GitHub issue #16 is closed.
7. **S-042: EPUB Ingestion and Long-Document Navigation** — S-042A and S-042B completed as `passed`; S-042C `READY_FOR_IMPLEMENTATION`; [scope](s042_epub_long_document_navigation.md); open umbrella issue #17.
8. **S-043: Limited Beta Distribution and External Trial** — `PROVISIONAL`; [scope](s043_limited_beta_external_trial.md).

The [Document Reader Productization Program](document_reader_productization_program.md) defines dependency order and shared boundaries. Only S-042C is active; S-043 is not authorized. GitHub issue #24 is an authorized non-blocking follow-up and is not active. S-043's external-trial gate is not interpreted or advanced by this transition.

## Later

- Provider ablation or dependency reduction when a concrete platform need arises.
- Native/mobile provider evaluation when native distribution becomes a real objective.
- Application-service refinements beyond S-039 only if validation exposes a concrete need.
- Management-document cleanup if the solo human/Codex workflow materially changes.
- PDF ingestion evaluation after S-043 as a distinct research and validation problem covering extraction quality, reading order, columns, headers, footers, captions, and hyphenation.

## Parked

- Native app, cloud sync, accounts, analytics, service workers, and production-grade deployment infrastructure.
- PDF ingestion pending its dedicated post-S-043 evaluation.
- Frontend framework migration, a general npm toolchain, and browser-automation expansion beyond the deliberately small S-038 baseline.
- Full Markdown rendering and rich-document rendering.
- Permanent universal commitment to spaCy.
- Immediate native packaging.
- Public performance claims.
- Broad expansion of hand-written semantic and grammatical exception families.
- Optimizer retuning without a new experimental slice.

Quote/parenthetical validation is not parked as a standalone queue item. It is folded into S-021 as a display-state clarity check.

Newly observed grammatical or semantic defects should become evaluation cases first. They do not automatically become new production rules while the parser-assisted experiment is pending.
