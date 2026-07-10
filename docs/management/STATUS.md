# Project Status

```yaml
current_slice: S-024
name: Baseline versus Experiment Comparison
state: READY_FOR_HUMAN_HANDOFF
owner: human
agent_action: none
blocked_on: sealed evaluation material and comparison authorization
started: 2026-07-10
evidence: evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json
previous_slice: S-023
```

## Current Slice

S-024 is the baseline-versus-experiment comparison slice. The parser-assisted implementation is frozen, but it has not been judged scientifically successful and has not been promoted.

S-024 is blocked until the human supplies or authorizes access to held-out comparison material, including the sealed blind package and any held-out annotations needed for a valid comparison.

The rule-based chunker remains the production default, regression baseline, fallback implementation, and comparison target.

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

- Human supplies or authorizes access to the sealed comparison material for S-024.
- Compare frozen rule-based baseline and frozen parser-assisted experiment without further tuning.
- Keep production behavior unchanged until comparison and promotion gates are satisfied.
- Leave production adoption decisions for the later disposition slice.

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
