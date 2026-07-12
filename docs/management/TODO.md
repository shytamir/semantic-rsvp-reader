# Parked And Unscheduled Inventory

This file is non-authoritative. It preserves ideas that should not compete with the current slice.

- Current work lives in [STATUS](STATUS.md).
- Priority order lives in [roadmap](roadmap.md).
- Completed work lives in [HISTORY](HISTORY.md).
- Durable project decisions live in [DECISIONS](DECISIONS.md).

## Folded Into Active Validation

- Quote/parenthetical validation is included in S-021 as a display-state clarity check. It should be classified separately from punctuation rhythm defects using [Quote and Parenthetical State Indicators](../validation/quote_parenthetical_state_indicators.md).

## Planned After Stabilization

The authoritative order is in the [roadmap](roadmap.md). These are approved destinations, not active implementation authorizations:

1. S-037: Evaluation Anomaly Investigation and Parser Operating-Policy Decision.
2. S-038: Minimal Browser Regression Baseline for stabilized critical flows.
3. S-039: Application-Service Boundary and Source-Document Contract, including S-039A tracked by GitHub issue #2.
4. S-040: Plain Text, Markdown, and Bounded Clean-HTML Ingestion.
5. S-041: Local Reading Continuity without accounts or cloud services.
6. S-042: EPUB Ingestion and Long-Document Navigation with heading navigation and a lightweight contents view.
7. S-043: Limited Beta Distribution and External Trial with explicit prototype/privacy limitations.

These scopes are defined by the [Document Reader Productization Program](document_reader_productization_program.md). S-037 is active under D-010; S-038 through S-043 remain provisional and unauthorized. PDF is not bundled with EPUB; its extraction and reading-order quality remain a separate post-S-043 evaluation problem.

## Parked

- Native app.
- PDF ingestion pending dedicated evaluation.
- Cloud sync.
- Accounts.
- Analytics.
- Service workers.
- Production-grade deployment infrastructure.
- Frontend framework migration.
- General npm toolchain migration.
- Browser-automation expansion beyond the minimal S-038 baseline.
- Full Markdown rendering.
- Rich-document rendering beyond the scoped S-040/S-042 foundations.
- Native packaging.
- Public performance claims.
- Broad hand-written semantic or grammatical exception-family expansion while the parser-assisted chunking experiment is pending.
- Unauthorized optimizer retuning or parser promotion.

## Unscheduled Hygiene

- Additional CI, packaging, or release automation beyond the provisional S-038/S-043 boundaries should wait for a concrete need and separate authorization.
- Further documentation consolidation should be done only if new docs begin competing with STATUS or the roadmap again.
