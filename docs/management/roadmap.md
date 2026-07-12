# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-035: Service Surfaces and Fallback**
   - State: `READY_FOR_IMPLEMENTATION`
   - Owner: Codex
   - Scope: [S-035](s035_service_surfaces_fallback.md).

## Next

1. **S-036: End-to-End Prototype Readiness** — `SCHEDULED`; [scope](s036_end_to_end_prototype_readiness.md).

These slices are ordered but not authorized for implementation until separately activated.

## Provisional Document Reader Productization Program

After S-036, and subordinate to the recorded outcomes of S-034 through S-036:

1. **S-037: Evaluation Anomaly Investigation and Parser Operating-Policy Decision** — `PROVISIONAL`; [scope](s037_evaluation_anomaly_parser_policy.md).
2. **S-038: Minimal Browser Regression Baseline** — `PROVISIONAL`; [scope](s038_minimal_browser_regression_baseline.md).
3. **S-039: Application-Service Boundary and Source-Document Contract** — `PROVISIONAL`; [scope](s039_application_service_source_document_contract.md). Includes tracked work item S-039A, GitHub issue #2.
4. **S-040: Plain Text, Markdown, and Bounded Clean-HTML Ingestion** — `PROVISIONAL`; [scope](s040_document_ingestion.md).
5. **S-041: Local Reading Continuity** — `PROVISIONAL`; [scope](s041_local_reading_continuity.md).
6. **S-042: EPUB Ingestion and Long-Document Navigation** — `PROVISIONAL`; [scope](s042_epub_long_document_navigation.md).
7. **S-043: Limited Beta Distribution and External Trial** — `PROVISIONAL`; [scope](s043_limited_beta_external_trial.md).

The [Document Reader Productization Program](document_reader_productization_program.md) defines dependency order and shared boundaries. None of these slices is active or authorized.

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
