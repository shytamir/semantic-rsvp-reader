# S-029 Density-Aware Dwell-Time Recalibration

## Status

Completed as `passed` on 2026-07-11. Human validation passed all six corpus-sample validations and found default `1.0x` as manageable as the prior build at `0.85x`. No successor slice is active.

## Initiating Evidence

Human observation: parser-assisted chunks appear substantially denser than earlier rule-based chunks; existing dwell times do not appear to scale with that density; default `1.0x` feels too fast; and `0.85x` is approximately comfortable. The claimed near-doubling of density is a hypothesis to measure, not an established repository metric.

## Objective

Make default `1.0x` comfortable for current parser-assisted output while retaining deterministic, inspectable timing. Measure identical project-owned corpus text under both chunkers before changing the formula. Use stable chunk metadata, preserve relative hint and punctuation treatment, clamps, speed values, interfaces, parser behavior, adaptation semantics, and rule-based support. Do not apply a blanket multiplier.

## Evidence and Validation

Commit a repeatable per-sample and aggregate density/timing comparison. Expose the new dwell component through `explain_duration`; test monotonicity, thresholds, clamps, light protection, dense and representative parser-sized chunks, and consolidation safety. After automated validation, hand off a concise human protocol and set the slice to `AWAITING_HUMAN_VALIDATION`.

## Non-Goals

No parser or optimizer changes, frozen S-023/S-024 evidence changes, lexical exception expansion, speed-control or adaptation changes, successor activation, or qualitative pass declaration.
