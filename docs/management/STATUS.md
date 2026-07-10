# Project Status

```yaml
current_slice: S-023
name: Parser-assisted Chunking Spike
state: READY_FOR_IMPLEMENTATION
owner: codex
agent_action: implement isolated experimental spike
started: 2026-07-10
evidence: docs/experiments/parser_assisted_chunking/README.md
previous_slice: S-022
```

## Current Slice

S-023 is the parser-assisted chunking spike defined by the frozen experiment design. The goal is to implement an isolated experimental path that can be compared against the current deterministic rule-based baseline.

The rule-based chunker remains the production default, regression baseline, fallback implementation, and comparison target.

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
- Do not alter frozen evaluation manifests, hashes, baseline outputs, or annotation schemas unless a separate experiment-maintenance slice explicitly authorizes it.
- Do not broaden hand-written semantic or grammatical production rule families while the parser-assisted experiment is pending.
- Treat newly observed grammatical or semantic defects as evaluation cases first.
- Preserve the existing timing and schedule contract unless a separate approved slice changes it.

## Evidence And Entry Points

- [Parser-Assisted Chunking Experiment](../experiments/parser_assisted_chunking/README.md)
- [Experiment Contract](../experiments/parser_assisted_chunking/experiment_contract.md)
- [Future Implementation Interface](../experiments/parser_assisted_chunking/future_interface.md)
- [Baseline Freeze](../experiments/parser_assisted_chunking/baseline_freeze.md)
- [S-021 Human Summary](../validation/s021_post_stabilization_human_summary.md)

## Next Actions

- Implement the isolated parser-assisted experimental path.
- Keep production behavior unchanged until comparison and promotion gates are satisfied.
- Run baseline/evaluation checks to verify the frozen rule-based baseline remains reproducible.
- Leave production adoption decisions for the later comparison and disposition slices.

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
