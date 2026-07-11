# Prototype Validation and Stabilization Program

This program orders validation of the shipped prototype without authorizing multiple active slices. Only the slice named in [STATUS](STATUS.md) may be implemented.

1. **S-029: Density-Aware Dwell-Time Recalibration** — measure rule-based versus parser-assisted density, implement the smallest justified deterministic timing adjustment, and hand off human validation.
2. **Semantic output and structure** — validate semantic chunking, headings, structural metadata, parser-default behavior, and mandatory rule-based fallback without retuning the frozen parser.
3. **Playback behavior** — validate playback, speed controls, adaptation, pause/resume behavior, and rhythm across representative material.
4. **Navigation behavior** — validate gestures, progress seeking, breakpoints, ghost context, drift recovery, and structural orientation.
5. **Mobile presentation** — stabilize phone layouts, orientations, display-state cues, quote/parenthetical state, and accessibility-relevant visual behavior.
6. **Evidence capture** — validate defect reporting, privacy, reproducibility, and management/evidence integrity.
7. **Service surfaces** — validate Flask APIs, health reporting, parser startup, automatic fallback, and dependency-light operation.
8. **Prototype readiness** — validate setup instructions, automation, representative end-to-end use, and final shipped-prototype readiness.

Passes 2–8 are program-level sequence only. They are not active, authorized implementation slices, or promises of a particular slice numbering.
