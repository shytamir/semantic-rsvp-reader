# Calibration Roadmap

The near-term goal is to refine the reading experience using observed defects rather than speculative feature additions.

## Current Phase: Evidence Hygiene Before Timing Calibration

**Goal:** Make timing evidence trustworthy by separating pure timing defects from layout, wrapping, tokenization, and chunking defects.

- **Done:** In-app backend defect reporting.
- **Done:** Defect report security hardening.
- **Done:** Timing-context defect instrumentation.
- **Done:** Chunking Refinement Pass 1 from observed reports.
- **Current:** Display/tokenization noise cleanup and timing-only review filtering.

**Gate:** A timing-only review export can exclude reports without Timing Context, and phone validation no longer produces false rushed-chunk reports from word hyphenation or obvious tokenization splits.

## Next Slice 1: Clean Timing Validation Pass

**Goal:** Collect timing/rhythm evidence from cleaner chunks and display behavior.

**Gate:** A short phone-reading pass produces timing-context reports focused on dense chunks at default and elevated speeds.

## Next Slice 2: Timing Calibration Pass 1

**Goal:** Adjust deterministic timing rules only after evidence quality improves.

**Gate:** A 10-15 minute reading session feels calmer without changing adaptation semantics or adding opaque timing behavior.

## Next Slice 3: Post-Calibration Validation Review

**Goal:** Compare post-calibration reports against the cleaned baseline.

**Gate:** The review utility shows fewer repeated dense-chunk timing complaints without new rhythm regressions.

## Next Slice 4: Demo/Beta Readiness Pass

**Goal:** Prepare a small external-testable demo.

**Gate:** An external tester can run or use the app with minimal explanation, sample text is easy to load, and debug detail is controlled.

## Explicit Non-Goals For The Current Phase

- No timing calibration before the clean timing validation pass.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
