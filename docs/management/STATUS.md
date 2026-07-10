# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Chunker-dominant refinement.
> **Immediate Focus:** Proper-name, title, article, preposition, quote, and parenthetical chunk quality; navigation additions remain conservative.

## Current Project Phase

The prototype has completed a narrow follow-up to Timing Calibration Pass 1. Timing is improved enough that the main blocker is now chunk quality: phrase attachment, proper names, titles, articles, prepositions, pronoun/preposition bookends, and context around quotes or parentheticals. The Passive Spatial Anchor adds a subtle bottom progress bar and coarse tap-to-seek while leaving bookmarking and drift recovery for future slices.

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

## Current Evidence

`docs/validation/observed_timing_defects_third_pass.md` drove the prior targeted slice. After that work, remaining recurring issues are more likely to be chunk shape or visual-context problems than pure timing. New quote, parenthetical, and navigation metadata supports cleaner classification while active navigability features remain future work.

JavaScript syntax checking is now CI-backed through a lightweight `node --check` wrapper. No npm toolchain or frontend framework was added.

The progress anchor is milestone-gated to reduce flicker and peripheral distraction. Active bookmarking and drift recovery remain future work.

## Next 4 Planned Slices

1. Proper Noun / Honorific / Article / Function-Word Chunking Refinement Pass.
2. Breakpoint Bookmarking Traversal.
3. Drift Recovery Logic.
4. Post-navigation usability validation.

## Known Risks

- Overfitting chunking rules to a small report count.
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
