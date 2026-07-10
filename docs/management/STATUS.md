# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Validation-driven stabilization.
> **Immediate Focus:** Post-stabilization validation focused on mobile layout, source boundaries, dates, and phrase cohesion.

## Current Project Phase

The prototype has completed Post-Validation Stabilization Pass 1 after `docs/validation/chunking_refinement_pass_3.md` reported 39 included defects. Timing remains stable; the latest pass fixed layout/visibility first, then addressed source-boundary flattening, long-form date cohesion, targeted phrase attachment, proper names, titles, underdense chunks, and overlong subject/verb cases. Navigability still includes the Passive Spatial Anchor, double-tap current-stream breakpoints with swipe traversal, drift recovery lead-in, a ghost previous chunk, and a static structural hierarchy anchor.

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
14. Breakpoint Bookmarking Traversal.
15. Ghost Previous Chunk.
16. Drift Recovery Logic.
17. Structural Hierarchy Anchor.
18. Post-Validation Stabilization Pass 1.

## Current Evidence

`docs/validation/chunking_refinement_pass_3.md` drove the latest stabilization slice. The report had 39 included defects: 17 bad chunk splits, 12 layout/visibility issues, 5 underdense chunks, 2 overlong chunks, 2 title-name splits, and 1 proper-name split. The pass addressed ghost previous chunk overlap and active font-size instability first, then source/title/byline/date flattening and observed phrase-cohesion cases. New quote, parenthetical, navigation, structure, and layout metadata support cleaner classification.

JavaScript syntax checking is now CI-backed through a lightweight `node --check` wrapper. No npm toolchain or frontend framework was added.

The progress anchor is milestone-gated to reduce flicker and peripheral distraction. Breakpoint traversal is current-stream/session-only and uses existing swipe gestures only after at least one breakpoint exists; otherwise chunk-step swipes remain unchanged. Drift recovery applies only to breakpoint traversal: it lands at `max(0, n - 3)`, pauses 500ms, then auto-resumes. The ghost previous chunk is visible above the current chunk at reduced contrast, clipped to one line with ellipsis, and included in defect report context. Simple Markdown H1/H2 headers now produce a static top label and structural defect-report context.

## Next 4 Planned Slices

1. Post-Stabilization Validation Pass focused on mobile layout and source-boundary chunking.
2. Chunking Regression Corpus Expansion if stabilization validates well.
3. Post-navigation usability validation.
4. Demo/beta readiness cleanup.

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
- Bookmark traversal fighting existing swipe gestures.
- Ghost previous chunk becoming too visually dominant.
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
- No broad timing redesign during validation-driven refinement.
- No full Markdown rendering, heading navigation, or table of contents.
