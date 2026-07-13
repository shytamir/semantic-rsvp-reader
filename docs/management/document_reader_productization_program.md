# Document Reader Productization Program

## Status And Authority

The program is active under human authorization D-010, committed in `4baf3e8`, after S-036 completed with prototype disposition `ready`. S-037 through S-042, S-043A1, and S-043A2 completed as `passed`. S-043 remains the current parent under issue #18, with rehearsal suspended behind the S-043A chain. No scope is active; S-043A3 awaits explicit activation.

## Entry Authorization And Architecture Clarification

D-010 is the human authorization to enter the **Document Reader Productization Program**. Its wording remains preserved verbatim in [DECISIONS](DECISIONS.md).

Within the ordered program, S-039 completed the project-owned source-document contract and S-040 completed bounded local ingestion. S-041 now owns browser-local reading continuity keyed by stable document identity. D-008 continues to govern the separate architectural requirement that linguistic evidence reaching the RSVP optimizer remain backend-neutral.

## Objective

Move the validated RSVP prototype toward a bounded local-first document reader while preserving evidence discipline, deterministic project-owned policy, mandatory rule-based fallback, and a deliberately small technical footprint.

## Ordered Program

1. **[S-037: Evaluation Anomaly Investigation and Parser Operating-Policy Decision](archive/s037_evaluation_anomaly_parser_policy.md)** — completed as `passed` at human-evidence commit `b95df256c0b26a8ff51e37e539f1a859bf31a56c` with disposition `retain_parser_default_with_mandatory_automatic_fallback`; GitHub issue #12.
2. **[S-038: Minimal Browser Regression Baseline](archive/s038_minimal_browser_regression_baseline.md)** — completed as `passed` at human-evidence commit `b97c189e55f259fbe80eccc7072d415af6dbb87f`; GitHub issue #13.
3. **[S-038A: Parser CI Evaluation-Surface Coverage](archive/s038_parser_ci_evaluation_surface.md)** — completed as `passed`; GitHub issues #23 and #25 are closed.
4. **[S-039: Application-Service Boundary and Source-Document Contract](archive/s039_application_service_source_document_contract.md)** — completed as `passed` at human-evidence commit `806dbaea92d9638cc7cea439fe33ce9168f97c58`; GitHub issues #2 and #14 are closed.
5. **[S-040: Plain Text, Markdown, and Bounded Clean-HTML Ingestion](archive/s040_document_ingestion.md)** — completed as `passed` at human-evidence commit `fb618d269f70f5497154f1309db84e69bf8f5451`; GitHub issue #15 is closed.
6. **[S-041: Local Reading Continuity](s041_local_reading_continuity.md)** — completed as `passed` at human-evidence commit `a865f563b50b9fa62bc65cb8e618ddcac04b0c6f`; GitHub issue #16 is closed.
7. **[S-042: EPUB Ingestion and Long-Document Navigation](s042_epub_long_document_navigation.md)** — completed as `passed` at human-evidence commit `6b85767b79fad7330403774a005eef465f2b4a0a`; GitHub issue #17 is closed.
8. **[S-043: Portfolio Demonstration and Interview Readiness](s043_portfolio_demonstration_and_interview_readiness.md)** — current parent under open issue #18; Human rehearsal suspended by the [S-043A chain](s043a_epub_preparation_chain.md).
   1. **S-043A1: Core Demo-Safe EPUB Preparation Engine and CLI** — completed as `passed`; issue #27 remains open.
   2. **S-043A2: Prepare EPUB Application Integration** — completed as `passed`; issue #28 remains open.
   3. **S-043A3: Demonstration Package Revalidation and Rehearsal Re-entry** — `PROVISIONAL`, inactive, and unauthorized; issue #29; depends on S-043A2.

## Program Boundaries

- Only one scope may be active through [STATUS](STATUS.md); no scope is active within parent S-043. GitHub issue #24 is an authorized non-blocking follow-up and is not active.
- Later scopes may be revised or declined when S-034, S-035, or S-036 evidence changes their assumptions.
- PDF extraction remains a separate later research and validation problem.
- Accounts, cloud sync, analytics, native packaging, frontend-framework migration, broad browser automation, production infrastructure, public performance claims, broad handwritten grammar expansion, and unauthorized optimizer retuning remain outside this program.
- No successor activates automatically.
