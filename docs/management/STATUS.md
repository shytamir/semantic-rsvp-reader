# Project Status

```yaml
current_slice: S-025
name: Post-experiment Disposition
state: READY_FOR_HUMAN_DECISION
owner: human
agent_action: none
blocked_on: product disposition decision for parser-assisted chunking
started: 2026-07-11
evidence: docs/validation/s024_human_ab_preference_summary.md
previous_slice: S-024
```

## Current Slice

S-025 is the post-experiment disposition slice. S-024 objective comparison and human A/B scoring are complete, but the parser-assisted implementation has not been promoted.

The next decision is whether to abandon, revise, continue evaluating, or consider promoting the parser-assisted approach. That product decision is intentionally separate from the evidence-gathering comparison.

The rule-based chunker remains the production default, regression baseline, fallback implementation, and comparison target.

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

Human preference results are scored. Do not make a production-disposition decision without an explicit S-025 decision.

## S-023 Outcome

S-023 completed as `implemented_not_promoted`.

The repository now contains an isolated optional parser-assisted chunking spike using pinned spaCy `3.7.5` and `en-core-web-sm` `3.7.1`, project-owned linguistic records, deterministic dynamic-programming boundary optimization, diagnostic traces, fallback to the rule-based chunker, and a visible development/regression runner.

The implementation freeze target is commit `b010851`. The freeze manifest is [parser_assisted_implementation_freeze.json](../../evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json), and the blind checksum registry is [blind_challenge_checksum_registry.json](../../evaluation/parser_assisted_chunking/freeze/blind_challenge_checksum_registry.json).

No blind source text or annotations were accessed. No qualitative generalization-output tuning was performed. Production still uses `RuleBasedChunker`.

## S-022 Outcome

S-022 completed as `passed`.

Human validation confirmed that GitHub issue #1, "Landscape Orientation Layout Collision Between Ghost and Current Chunk," is resolved. The previous-chunk ghost now has a distinct visual lane from the active chunk in the targeted phone/orientation validation.

Issue #1 may be closed as completed. The fix was a responsive presentation correction only; it did not change chunking, timing, playback, navigation, adaptation, parser experiment artifacts, or semantic-rule behavior.

## S-021 Evidence Note

S-021 completed as `partially_passed`: human validation found no major or parser-experiment-blocking regression, with one narrow landscape layout defect promoted into S-022.

Detailed in-app defect reports from the S-021 validation session were accidentally deleted. No report counts or individual defect details are reconstructed from memory.

## Implementation Guardrails

- Keep the parser-assisted path isolated from the production default.
- Do not replace the rule-based chunker.
- Do not change S-023 code, weights, or configuration during S-024 unless the comparison slice is deliberately invalidated and restarted.
- Do not alter frozen evaluation manifests, hashes, baseline outputs, or annotation schemas unless a separate experiment-maintenance slice explicitly authorizes it.
- Do not broaden hand-written semantic or grammatical production rule families while the parser-assisted experiment is pending.
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

- Human reviews the completed S-024 evidence packet.
- Decide whether the parser-assisted approach should be abandoned, revised, evaluated further, or considered for promotion planning.
- Keep production behavior unchanged until comparison and promotion gates are satisfied.
- Keep the private A/B identity key out of Git.

## Active Risks

- Experimental parser dependencies may add installation weight, latency, or platform friction.
- Parser token alignment may fail or become unsafe; fallback to the baseline must remain available.
- Visible development/regression/generalization material can encourage overfitting if not handled carefully.
- Human-held blind material must remain outside Codex prompts until tuning is declared complete.
- Broad semantic-rule expansion remains frozen while the experiment is pending.

## Non-Goals

- No production default replacement in S-023.
- No production promotion decision in S-023.
- No timing, playback, navigation, breakpoint, drift-recovery, or adaptation redesign.
- No broad handwritten semantic-rule expansion.
- No public performance claims.
