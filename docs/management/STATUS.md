# Project Status

```yaml
current_slice: S-038
active_scope: S-038
name: Minimal Browser Regression Baseline
state: READY_FOR_IMPLEMENTATION
owner: Codex
agent_action: implement the bounded S-038 scope from GitHub issue #13
blocked_on: none
started: 2026-07-12
scope: docs/management/s038_minimal_browser_regression_baseline.md
previous_slice: S-037
```

## Current Slice

The **Document Reader Productization Program** is active under human authorization D-010 from commit `4baf3e8`. S-038 is the sole active scope at `READY_FOR_IMPLEMENTATION`, owned by Codex, with GitHub issue #13 open as detailed authority. S-039 through S-043 remain provisional, inactive, and unauthorized.

## S-037 Outcome

S-037 completed as `passed` on 2026-07-12 with disposition `retain_parser_default_with_mandatory_automatic_fallback`, pinned to human-evidence commit `b95df256c0b26a8ff51e37e539f1a859bf31a56c`. The correction concerns evidence classification, not a parser regression or reduced fallback safety; unsafe mapping and unscorable output remain accepted limitations. GitHub issue #24 is an authorized non-blocking follow-up for rule-based fallback preservation of normalized source characters, particularly curly quotation marks, and source-reconstruction postconditions; it is not active.

## S-036 Outcome

S-036 completed as `passed` on 2026-07-12 with prototype disposition `ready`, from human-owned evidence commit `d6e945d`. All eight fixed human steps passed on the documented Samsung Galaxy S23 Ultra / Android 16 / Firefox 152 setup. No acceptance-blocking defect or new issue was found. GitHub issue #19 remains an accepted, non-blocking deferred limitation. The generated local synthetic-report file was deleted; its intentionally synthetic transcript remains committed verbatim in [S-036 validation](../validation/s036_end_to_end_prototype_readiness.md).

## S-035B Outcome

S-035B completed as `passed` on 2026-07-12 from human-owned evidence commit `8b38905`. The human accepted the parser-sensitive and presentation/accessibility trace exercises, conditional-gate behavior, non-blocking defect deferral model, experiment authorization boundaries, and retained human control over rendered browser behavior. The disposition remains verbatim in [S-035B validation](../validation/s035b_qa_authority_validation.md). GitHub issue #22 is closed.

## S-035A Outcome

S-035A completed as `passed` on 2026-07-12 from human-owned evidence commit `d572760`. Clean Windows `standard` and `core` environments passed the corrected Python 3.12 contract, reported the expected parser-assisted and rule-based health identities, and fulfilled the configuration contract. The disposition remains verbatim in [S-035A validation](../validation/s035a_environment_contract_validation.md). GitHub issue #21 is closed.

## S-035 Outcome

S-035 completed as `passed` on 2026-07-12 from human-owned evidence commit `8f8a7a6` plus the committed automated standard-profile API follow-up. Human startup, `/health`, and browser sample checks passed in both `standard` and `core`. Parser CI now covers valid ingest/chunk/schedule POST contracts, bounded invalid defect rejection, POST-only `405` responses, expected fields, and JSON-native serialization under the real pinned parser environment. No further human gate is required.

## Issue #11 Maintenance Outcome

Issue #11 completed from human-owned evidence commit `a52e79f`. The enlarged coarse-seek touch target was accepted and issue #11 is closed. The low-priority, non-blocking phone-landscape obstruction by the `Defects Reported: #` display is tracked separately in GitHub issue #19; no follow-up correction was implemented during this transition.

## S-034 Outcome

S-034 completed as `passed` on 2026-07-12 from human-owned evidence commit `eafadbd`. All seven human steps passed, the four synthetic local reports were deleted, and no missing context or impractical protocol step was found. GitHub issue #8 is closed consistently.

## Implementation Guardrails

- Keep the parser-assisted path provisional for the current Flask prototype.
- Do not replace the rule-based chunker.
- Do not change S-023 code, weights, or configuration without a new authorized evaluation slice.
- Do not alter frozen evaluation manifests, hashes, baseline outputs, or annotation schemas unless a separate experiment-maintenance slice explicitly authorizes it.
- Do not broaden hand-written semantic or grammatical production rule families while the integrated parser-assisted path is being validated.
- Treat newly observed grammatical or semantic defects as evaluation cases first.
- Preserve the existing timing and schedule contract unless a separate approved slice changes it.

## Evidence And Entry Points

- [Parser-Assisted Chunking Experiment](../experiments/parser_assisted_chunking/README.md)
- [Experiment Contract](../experiments/parser_assisted_chunking/experiment_contract.md)
- [Future Implementation Interface](../experiments/parser_assisted_chunking/future_interface.md)
- [Baseline Freeze](../experiments/parser_assisted_chunking/baseline_freeze.md)
- [S-023 Implementation Freeze](../../evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json)
- [S-023 Blind Checksum Registry](../../evaluation/parser_assisted_chunking/freeze/blind_challenge_checksum_registry.json)
- [S-021 Human Summary](../validation/archive/s021_post_stabilization_human_summary.md)

## Next Actions

- Codex implements only the bounded S-038 scope authorized by GitHub issue #13.
- Keep the private A/B identity key out of Git.

## Active Risks

- Experimental parser dependencies may add installation weight, latency, or platform friction.
- Parser token alignment may fail or become unsafe; fallback to the baseline must remain available.
- Visible development/regression/generalization material can encourage overfitting if not handled carefully.
- Human-held blind material must remain outside Codex prompts until tuning is declared complete.
- Broad semantic-rule expansion remains frozen while the integrated parser-assisted path is being validated.

## Non-Goals

- No permanent production architecture commitment.
- No native/mobile provider decision.
- No playback, navigation, breakpoint, drift-recovery, or adaptation redesign.
- No broad handwritten semantic-rule expansion.
- No public performance claims.
