# Timing

## Purpose

The timing engine assigns deterministic display durations to chunks based on chunk shape and context.

## Current Behavior

- Computes bounded durations from syntactic hint, content-word count, character length, punctuation, quote state, and density.
- Preserves timing formulas during chunker-dominant and stabilization passes unless a pass explicitly targets timing.
- Exposes base and effective duration context in defect reports.

## Constraints

- No adaptive timing persistence.
- No public performance claims.
- No timing changes should be made to compensate for badly shaped chunks.

## Validation Notes

Timing work is documented in:

- [Timing Defect Collection](../validation/timing_defect_collection.md)
- [Timing Calibration Pass 1](../validation/timing_calibration_pass_1.md)
- [Post-Validation Targeted Calibration](../validation/post_validation_targeted_calibration.md)

## Known Limitations

- Some timing complaints are actually chunk-shape problems.
- Speed/adaptation can mask baseline timing issues during manual validation.
