# Calibration Roadmap

The near-term goal is to refine the reading experience using observed defects rather than speculative feature additions.

## Current Phase: Post-Targeted-Calibration Validation

**Goal:** Validate the narrow third-pass follow-up without overfitting or masking baseline timing with adaptation.

- **Done:** In-app backend defect reporting.
- **Done:** Defect report security hardening.
- **Done:** Timing-context defect instrumentation.
- **Done:** Chunking Refinement Pass 1 from observed reports.
- **Done:** Display/tokenization noise cleanup and timing-only review filtering.
- **Done:** Timing Calibration Pass 1.
- **Done:** Refreshed validation corpus to reduce overfitting.
- **Done:** Third-pass post-calibration timing report review.
- **Done:** Post-validation targeted calibration.
- **Current:** Focused validation at 1.0x, 1.15x, and optionally 1.3x.

**Gate:** Collect 8-12 clean timing-context reports with adaptation disabled for at least one pass. Only consider Timing Calibration Pass 2 if recurring defects remain after separating timing from chunking/normalization issues.

## Next Slice 1: Focused Post-Targeted-Calibration Validation Pass

**Goal:** Retest extreme semantic density, punctuation/quote rhythm, dense proper nouns, and modal-heavy dense chunks.

**Gate:** A clean report set shows whether targeted fixes reduced repeated friction without making light text sluggish.

## Next Slice 2: Timing Calibration Pass 2, If Justified

**Goal:** Make another timing formula change only if clean reports show repeated pure timing defects.

**Gate:** Any adjustment is narrow, test-covered, and backed by timing-context evidence.

## Next Slice 3: Session Summary / Validation UX Polish

**Goal:** Improve demo validation ergonomics without changing timing semantics.

**Gate:** A tester can finish a session and understand what happened without reading raw debug output.

## Next Slice 4: Demo/Beta Readiness Pass

**Goal:** Prepare a small external-testable demo.

**Gate:** An external tester can run or use the app with minimal explanation, sample text is easy to load, and debug detail is controlled.

## Explicit Non-Goals For The Current Phase

- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
- No broad timing redesign without another clean validation pass.
