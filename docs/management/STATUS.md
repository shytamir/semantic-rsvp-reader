# Project Status

```yaml
current_slice: S-022
name: Landscape Ghost-Chunk Collision Stabilization
state: HUMAN_VALIDATION
owner: human
agent_action: none
started: 2026-07-10
evidence: docs/validation/s021_post_stabilization_human_summary.md
issue: https://github.com/shytamir/semantic-rsvp-reader/issues/1
```

## Current Slice

S-022 is a narrow responsive-layout stabilization for GitHub issue #1: in phone landscape orientation, the previous-chunk ghost can occupy the same visual lane as the active chunk. Portrait orientation remains correct.

The implementation has been completed and is awaiting targeted human phone/orientation validation. This is a presentation fix only; it does not change chunking, timing, playback, navigation, adaptation, parser experiment artifacts, or semantic-rule behavior.

## S-021 Outcome

S-021 completed as `partially_passed`: human validation found no major or parser-experiment-blocking regression. The stabilized reader looked approximately the same overall, and no semantic, timing, playback, navigation, source-boundary, or general usability defect was considered acceptance-blocking for the parser-assisted experiment.

One minor but reproducible layout regression remained: in phone landscape orientation, the previous-chunk ghost collides with or occupies the same visual lane as the active chunk. That defect is tracked as GitHub issue #1 and promoted into S-022.

Detailed in-app defect reports from the S-021 validation session were accidentally deleted. No report counts or individual defect details are reconstructed from memory.

## Validation Required

Validate on the affected phone/browser combination:

- Portrait layout.
- Landscape layout after advancing beyond the first chunk.
- Portrait to landscape while paused.
- Portrait to landscape while playing.
- Landscape back to portrait.
- First chunk with empty ghost.
- Short and long previous chunks.
- Ellipsized ghost chunks.
- Active chunks in normal, long-token, quote, and parenthetical display states.

## Acceptance Gate

The human owner records the S-022 gate result as `passed`, `partially_passed`, `failed`, or `inconclusive`.

S-022 passes only if the previous-chunk ghost has a distinct visual lane and does not overlap or appear on the same line as the active chunk across the targeted phone/orientation checks.

Codex must not close GitHub issue #1 or declare the visual gate passed without human evidence.

## Next Actions

- If S-022 passes, proceed to the parser-assisted chunking spike defined by the roadmap.
- If S-022 fails or is inconclusive, summarize the observed layout behavior and keep the fix constrained to issue #1.
- Other minor S-021 observations, if any, remain deferred until after the parser-assisted experiment rather than becoming new production rules.

## Active Risks

- CSS-only automated tests may miss Android/Firefox rendering differences.
- Very short landscape viewports may still require human judgment about comfort even if lanes no longer overlap.
- Orientation changes can expose browser viewport-unit behavior that static tests cannot prove.
- Navigation aids may hide chunking defects during unrelated validation.
- Broad hand-written semantic exception expansion remains frozen while the parser-assisted experiment is pending.

## Non-Goals

- No chunking rule changes.
- No timing, playback, navigation, breakpoint, drift-recovery, or adaptation changes.
- No parser, NLP, or dependency changes.
- No parser-assisted experiment artifact changes.
- No broad reader redesign.
- No full Markdown rendering, heading navigation, or table of contents.
