# Document Reader Productization Program

## Status And Authority

The program is active under human authorization D-010, committed in `4baf3e8`, after S-036 completed with prototype disposition `ready`. S-037, S-038, and S-038A completed as `passed`. Only the scope named by [STATUS](STATUS.md) is authorized; S-039 is active and S-040 through S-043 remain provisional until separately activated.

## Entry Authorization And Architecture Clarification

D-010 is the human authorization to enter the **Document Reader Productization Program**. Its wording remains preserved verbatim in [DECISIONS](DECISIONS.md).

Within the ordered program, S-038A completed the bounded Parser CI evaluation-surface coverage maintenance that preceded S-039. S-039 now owns the application-service boundary and project-owned source-document contract required before ingestion, continuity, and long-document features advance. D-008 governs the separate architectural requirement that linguistic evidence reaching the RSVP optimizer remain backend-neutral. D-008 does not itself define or implement the application-service/source-document prerequisite.

## Objective

Move the validated RSVP prototype toward a bounded local-first document reader while preserving evidence discipline, deterministic project-owned policy, mandatory rule-based fallback, and a deliberately small technical footprint.

## Ordered Program

1. **[S-037: Evaluation Anomaly Investigation and Parser Operating-Policy Decision](s037_evaluation_anomaly_parser_policy.md)** — completed as `passed` at human-evidence commit `b95df256c0b26a8ff51e37e539f1a859bf31a56c` with disposition `retain_parser_default_with_mandatory_automatic_fallback`; GitHub issue #12.
2. **[S-038: Minimal Browser Regression Baseline](s038_minimal_browser_regression_baseline.md)** — completed as `passed` at human-evidence commit `b97c189e55f259fbe80eccc7072d415af6dbb87f`; GitHub issue #13.
3. **[S-038A: Parser CI Evaluation-Surface Coverage](s038_parser_ci_evaluation_surface.md)** — completed as `passed`; GitHub issues #23 and #25 are closed.
4. **[S-039: Application-Service Boundary and Source-Document Contract](s039_application_service_source_document_contract.md)** — `READY_FOR_IMPLEMENTATION`, owned by Codex, and active; GitHub issue #2 is bounded implementation work S-039A.
5. **[S-040: Plain Text, Markdown, and Bounded Clean-HTML Ingestion](s040_document_ingestion.md)** — `PROVISIONAL`, inactive, and unauthorized; add initial document formats through the S-039 contract.
6. **[S-041: Local Reading Continuity](s041_local_reading_continuity.md)** — `PROVISIONAL`, inactive, and unauthorized; preserve local state after document identity is stable.
7. **[S-042: EPUB Ingestion and Long-Document Navigation](s042_epub_long_document_navigation.md)** — `PROVISIONAL`, inactive, and unauthorized; extend ingestion with lightweight long-document orientation.
8. **[S-043: Limited Beta Distribution and External Trial](s043_limited_beta_external_trial.md)** — `PROVISIONAL`, inactive, and unauthorized; its external-trial gate is not interpreted or advanced by S-037 activation.

## Program Boundaries

- Only one scope may be active through [STATUS](STATUS.md); S-040 through S-043 remain provisional until separately activated. GitHub issue #24 is an authorized non-blocking follow-up and is not active.
- Later scopes may be revised or declined when S-034, S-035, or S-036 evidence changes their assumptions.
- PDF extraction remains a separate later research and validation problem.
- Accounts, cloud sync, analytics, native packaging, frontend-framework migration, broad browser automation, production infrastructure, public performance claims, broad handwritten grammar expansion, and unauthorized optimizer retuning remain outside this program.
- No successor activates automatically.
