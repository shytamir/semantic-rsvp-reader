# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Validation-driven stabilization.
> **Immediate Focus:** Post-stabilization validation focused on mobile layout, source boundaries, dates, and phrase cohesion.

## Current Project Phase

Timing has improved enough that the current useful work is validation-driven stability. The latest detailed validation file, `docs/validation/chunking_refinement_pass_3.md`, included 39 defects. Layout/visibility was a major mobile blocker, so Post-Validation Stabilization Pass 1 fixed ghost/active chunk layout first, then addressed source-boundary flattening, long-form date cohesion, and targeted phrase-cohesion cases while keeping timing/playback/navigation semantics stable.

## Completed Recent Slices

1. Backend defect reporting and security hardening.
2. Chunking Refinement Pass 1.
3. Timing-context instrumentation.
4. Evidence hygiene/display/tokenization cleanup.
5. Timing Calibration Pass 1.
6. Refreshed validation corpus.
7. Post-validation targeted calibration.
8. Quote/parenthetical state annotation and reporting prep.
9. Navigation Scaffolding Pass 1.
10. JavaScript syntax verification hardening.
11. Passive Spatial Anchor implementation.
12. Chunker Refinement Pass 2.
13. Breakpoint Bookmarking Traversal.
14. Ghost Previous Chunk.
15. Drift Recovery Logic.
16. Structural Hierarchy Anchor.
17. Post-Validation Stabilization Pass 1.

## Current Evidence

The latest timing passes reduced the strongest timing complaints, while remaining recurring defects increasingly describe chunk shape, phrase attachment, source structure, and mobile layout. Post-Validation Stabilization Pass 1 used the 39 included defects in `docs/validation/chunking_refinement_pass_3.md`: ghost previous chunk overlap and unexplained active-text shrinking were handled first, followed by source-title/date boundaries and focused phrase cohesion. Defect reports now include quote, parenthetical, navigation, structural, and layout context so future reviews can separate visual context and orientation evidence from timing rhythm.

JavaScript syntax checking is now CI-backed through a lightweight `node --check` wrapper. Local environments without Node skip with a warning; CI installs Node and enforces the check.

The Passive Spatial Anchor is implemented as a subtle bottom progress bar with milestone-gated updates and coarse tap-to-seek. Breakpoint traversal is implemented with double-tap breakpoint toggles and swipe traversal between saved breakpoints. Drift recovery now starts breakpoint traversal up to three chunks before the target, pauses 500ms, and auto-resumes. The ghost previous chunk is implemented as a low-contrast orientation aid that clips to one line with ellipsis and does not wrap into the active chunk. Simple Markdown H1/H2 headers now provide a static structural label and defect-report context.

## Next 4 Planned Slices

1. Post-Stabilization Validation Pass focused on mobile layout and source-boundary chunking.
2. Chunking Regression Corpus Expansion if stabilization validates well.
3. Post-navigation usability validation.
4. Demo/beta readiness cleanup.

## Known Risks

- Overfitting chunking rules to a small validation set.
- Misclassifying chunk shape defects as timing defects.
- Quote/parenthetical indicators being too subtle or too visually heavy.
- Proper-name heuristics improving one sample while harming ordinary prose.
- Proper-name grouping creating overlong or over-dense chunks in unseen text.
- Article/preposition cleanup improving observed cases while changing ordinary phrase rhythm.
- Adaptation or speed changes masking baseline schedule quality.
- Navigation UI causing peripheral distraction.
- Progress updates causing flicker/strobe effects.
- Bookmark traversal fighting existing swipe gestures.
- Ghost previous chunk turning RSVP into conventional two-line reading.
- Auto-resume after bookmark traversal surprising users.
- The 500ms recovery pause being too short or too long.
- Three lead-in chunks being insufficient for long or dense sentences.
- Stale recovery timers resuming playback if cancellation is incomplete.
- Structural label distracting from RSVP focus.
- Structure mapping being approximate around unusual Markdown or repeated heading text.
- Headings being both read as chunks and shown as labels.
- Navigability features masking chunking defects.
- Drift recovery becoming surprising if too automatic.
- CSS-only layout tests missing device-specific Android/Firefox issues.
- Preserving structure boundaries creating slightly more pauses.
- Phrase cohesion rules over-clumping edge cases.
- Date/name preservation creating dense chunks.
- Fixing ghost visibility reducing previous-chunk context usefulness.
- Remaining timing complaints being caused by chunk shape rather than duration formulas.

## Explicit Non-Goals

- No ML parser.
- No EPUB/PDF import.
- No accounts.
- No cloud analytics.
- No native app.
- No public performance claims.
- No broad timing redesign during chunker-dominant refinement.
- No full Markdown rendering, heading navigation, or table of contents.
