# S-037 Evaluation Anomaly Investigation and Parser Operating-Policy Decision

## Status

Completed as `passed` on 2026-07-12 with disposition `retain_parser_default_with_mandatory_automatic_fallback`, pinned to human-evidence commit `b95df256c0b26a8ff51e37e539f1a859bf31a56c`. The correction concerns evidence classification, not a parser regression or reduced fallback safety; unsafe mapping and unscorable output remain accepted limitations. GitHub issue #24 is an authorized non-blocking follow-up and is not active. S-038 is active separately at `READY_FOR_IMPLEMENTATION`; S-039 through S-043 remain provisional, inactive, and unauthorized.

## Objective

Resolve remaining S-024 coverage and evaluation-mapping anomalies sufficiently to make an evidence-based parser operating-policy decision.

## Dependency And Initiating Reason

Begins only after S-036 and uses completed stabilization evidence. The anomalies are scientific/evaluation debt, not automatic authority for parser retuning or promotion.

D-010, committed in `4baf3e8`, authorizes entry into the Document Reader Productization Program. S-037 does not implement the S-039 application-service/source-document prerequisite. D-008 continues to govern backend-neutral linguistic evidence.

## In Scope

- Reproduce and classify rule-based coverage and evaluation-mapping anomalies.
- Verify case identities, mapping logic, metrics, and provenance without exposing private blind identity material.
- Compare defensible parser-default, explicit rule-based, and automatic-fallback operating policies.

## Codex Preparation

Prepare deterministic reproductions, integrity checks, traceable case records, and a decision packet separating evidence from inference.

## Human Handoff

Review classifications and choose an operating-policy disposition.

## Permissible Narrow Work

Correct only reproduced evaluation plumbing, mapping, or record-integrity defects. Parser behavior changes require separate authorization.

## Non-Goals

No optimizer retuning, parser promotion, broad handwritten-rule expansion, new provider, frozen-result reinterpretation, or private blind-material disclosure.

## Completion Boundary

Anomalies are reproducibly explained or bounded and a human-owned operating-policy decision is recorded. No successor activates automatically.
