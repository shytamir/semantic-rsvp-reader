# Project Status

```yaml
current_slice: S-026
name: Provisional Parser-Assisted Prototype Integration
state: AWAITING_HUMAN_VALIDATION
owner: human
agent_action: none
blocked_on: focused parser-integration smoke validation
started: 2026-07-11
evidence: docs/management/DECISIONS.md
previous_slice: S-025
```

## Current Slice

S-026 is the provisional parser-assisted prototype integration slice.

The frozen S-023 parser-assisted behavior is now integrated as the normal chunking path in the current Flask prototype while preserving `RuleBasedChunker` as the mandatory fallback. This slice did not retune optimizer weights, change feature interpretation, alter fallback rules, change timing/navigation/display-state behavior, or make a native/mobile provider decision.

The rule-based chunker remains the explicit baseline and required fallback implementation.

Human validation is now required before S-026 can be closed. See [S-026 parser integration validation](../validation/s026_parser_integration_validation.md).

## S-025 Outcome

S-025 completed as `provisional_adoption_authorized`.

Human disposition decision: `provisional_adoption_for_current_flask_prototype`.

The experimental hypothesis was supported by S-024 evidence: parser-assisted output reduced annotated harmful boundaries and protected-span splits, won all 12 decisive blinded human preferences, and preserved blind hard-compliance requirements without fallback. The current Flask prototype will adopt the frozen parser-assisted behavior as its preferred/default chunking path. spaCy remains provisional and nonexclusive under D-008, and `RuleBasedChunker` remains mandatory fallback.

Decision record: [D-009: Provisional Parser-Assisted Adoption for the Flask Prototype](DECISIONS.md).

## S-024 Outcome

S-024 completed as `evidence_gathered_not_promoted`.

The objective comparison was run against the authorized sealed blind challenge package, and the human blinded A/B response packet was scored without committing the private identity key or per-case system mappings.

- Redacted objective report: [s024_objective_comparison.md](../experiments/parser_assisted_chunking/s024_objective_comparison.md)
- Redacted objective JSON: [s024_objective_comparison.json](../../evaluation/parser_assisted_chunking/results/s024_objective_comparison.json)
- Human A/B preference summary: [s024_human_ab_preference_summary.md](../validation/s024_human_ab_preference_summary.md)
- Human A/B preference JSON: [s024_human_ab_preference.json](../../evaluation/parser_assisted_chunking/results/s024_human_ab_preference.json)

Human A/B scoring result: parser-assisted preferred in 12 decisive cases, rule-based preferred in 0, with 3 equivalent and 1 both-poor responses.

## S-024 Objective Comparison Status

The sealed material was revealed only after the S-023 implementation freeze.

- ZIP SHA-256: `a8926e9dc9cd68399f2c9f6a8b63ee44ac0cdd5b4f4361a20460410617b1f71b`
- Canonical sealed file SHA-256: `a6647ba26a9e32cfc154bfb904579f57ebdfbef9bdd2b64b7253cfefaa026502`
- Redacted objective JSON: [s024_objective_comparison.json](../../evaluation/parser_assisted_chunking/results/s024_objective_comparison.json)
- Redacted objective report: [s024_objective_comparison.md](../experiments/parser_assisted_chunking/s024_objective_comparison.md)
- Objective run record: [s024_objective_run_record.json](../../evaluation/parser_assisted_chunking/freeze/s024_objective_run_record.json)

Human preference results are scored, and S-025 recorded the provisional Flask-prototype adoption decision in D-009.

## S-023 Outcome

S-023 completed as `implemented_not_promoted`.

The repository now contains an isolated optional parser-assisted chunking spike using pinned spaCy `3.7.5` and `en-core-web-sm` `3.7.1`, project-owned linguistic records, deterministic dynamic-programming boundary optimization, diagnostic traces, fallback to the rule-based chunker, and a visible development/regression runner.

The implementation freeze target is commit `b010851`. The freeze manifest is [parser_assisted_implementation_freeze.json](../../evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json), and the blind checksum registry is [blind_challenge_checksum_registry.json](../../evaluation/parser_assisted_chunking/freeze/blind_challenge_checksum_registry.json).

No blind source text or annotations were accessed. No qualitative generalization-output tuning was performed. The frozen S-023 behavior is now the provisional Flask prototype default under D-009, with `RuleBasedChunker` still mandatory fallback.

## S-022 Outcome

S-022 completed as `passed`.

Human validation confirmed that GitHub issue #1, "Landscape Orientation Layout Collision Between Ghost and Current Chunk," is resolved. The previous-chunk ghost now has a distinct visual lane from the active chunk in the targeted phone/orientation validation.

Issue #1 may be closed as completed. The fix was a responsive presentation correction only; it did not change chunking, timing, playback, navigation, adaptation, parser experiment artifacts, or semantic-rule behavior.

## S-021 Evidence Note

S-021 completed as `partially_passed`: human validation found no major or parser-experiment-blocking regression, with one narrow landscape layout defect promoted into S-022.

Detailed in-app defect reports from the S-021 validation session were accidentally deleted. No report counts or individual defect details are reconstructed from memory.

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
- [S-021 Human Summary](../validation/s021_post_stabilization_human_summary.md)

## Next Actions

- Perform focused human validation of the integrated parser-assisted default.
- Confirm rule-based fallback remains available and observable.
- Record any parser-integration smoke validation regressions before closing S-026.
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
- No timing, playback, navigation, breakpoint, drift-recovery, or adaptation redesign.
- No broad handwritten semantic-rule expansion.
- No public performance claims.
