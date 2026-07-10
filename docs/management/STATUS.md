# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Chunker-dominant refinement.
> **Immediate Focus:** Post-Chunker Refinement Pass 2 validation; navigation additions remain conservative.

## Current Project Phase

The prototype has completed Chunker Refinement Pass 2 after a chunker-dominant validation report. Timing remains stable; the latest pass focused on phrase attachment, proper names, titles, articles, prepositions, and apostrophe tokenization. The Passive Spatial Anchor adds a subtle bottom progress bar and coarse tap-to-seek while leaving bookmarking and drift recovery for future slices.

## Completed Recent Slices

1. Backend defect reporting.
2. Security hardening.
3. Chunking Refinement Pass 1.
4. Timing-context instrumentation.
5. Evidence hygiene/display/tokenization cleanup.
6. Timing Calibration Pass 1.
7. Post-calibration timing validation.
8. Post-validation targeted calibration.
9. Quote/parenthetical display-state annotation and defect taxonomy prep.
10. Navigation Scaffolding Pass 1.
11. JavaScript syntax verification hardening.
12. Passive Spatial Anchor implementation.
13. Chunker Refinement Pass 2.

## Current Evidence

`docs/validation/chunking_refinement_pass_2.md` drove the latest targeted chunker slice. The pass addressed repeated `Air Force` / `Air Force One` splits, honorific/title-name splits, article modifier/head grouping, preposition-led weak chunks, and curly apostrophe tokenization. New quote, parenthetical, and navigation metadata supports cleaner classification while active navigability features remain future work.

JavaScript syntax checking is now CI-backed through a lightweight `node --check` wrapper. No npm toolchain or frontend framework was added.

The progress anchor is milestone-gated to reduce flicker and peripheral distraction. Active bookmarking and drift recovery remain future work.

## Next 4 Planned Slices

1. Post-Chunker Refinement Pass 2 validation.
2. Breakpoint Bookmarking Traversal.
3. Drift Recovery Logic.
4. Post-navigation usability validation.

## Known Risks

- Overfitting chunking rules to a small report count.
- Known-phrase rules improving observed named entities while missing unseen entities.
- Proper-name grouping creating overlong or over-dense chunks.
- Article/preposition cleanup changing ordinary phrase rhythm.
- Speed multipliers masking timing formula quality.
- Chunking defects being misclassified as timing defects.
- Quote/parenthetical visual indicators being too subtle or too heavy.
- Adaptation masking baseline timing defects.
- Progress bar becoming distracting.
- Seek interaction conflicting with reader gestures.
- Coarse seek causing disorientation without drift recovery.
- Bookmark traversal fighting existing swipe gestures.
- Navigability features masking chunking defects.
- Drift recovery becoming surprising if too automatic.

## Explicit Non-Goals

- No ML parser.
- No EPUB/PDF import.
- No accounts.
- No cloud analytics.
- No native app.
- No public performance claims.
- No broad timing redesign during chunker-dominant refinement.
- No active navigation behavior in the scaffolding slice.
