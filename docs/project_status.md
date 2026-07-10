# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Chunker-dominant refinement.
> **Immediate Focus:** Validate Chunker Refinement Pass 2 while monitoring breakpoint, drift-recovery, and ghost-chunk navigability aids.

## Current Project Phase

Timing has improved enough that the current useful work is chunk quality. Chunker Refinement Pass 2 addressed repeated phrase-boundary issues around names, titles, articles, prepositions, and apostrophe tokenization while keeping timing/playback semantics stable. Conservative navigability work now includes current-stream breakpoint traversal, drift recovery lead-in, and a ghost previous chunk orientation aid; these should be validated without letting navigation mask chunking defects.

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

## Current Evidence

The latest timing passes reduced the strongest timing complaints, while remaining recurring defects increasingly describe chunk shape, phrase attachment, and display-state orientation. Chunker Refinement Pass 2 used the latest chunking report to address proper-name splits, honorific/title splits, article phrase splits, weak preposition-led chunks, and curly apostrophe suffix orphans. Defect reports now include quote, parenthetical, and optional navigation state so future reviews can separate visual context and orientation evidence from timing rhythm.

JavaScript syntax checking is now CI-backed through a lightweight `node --check` wrapper. Local environments without Node skip with a warning; CI installs Node and enforces the check.

The Passive Spatial Anchor is implemented as a subtle bottom progress bar with milestone-gated updates and coarse tap-to-seek. Breakpoint traversal is implemented with double-tap breakpoint toggles and swipe traversal between saved breakpoints. Drift recovery now starts breakpoint traversal up to three chunks before the target, pauses 500ms, and auto-resumes. The ghost previous chunk is implemented as a low-contrast orientation aid.

## Next 4 Planned Slices

1. Post-Chunker Refinement Pass 2 validation.
2. Post-navigation usability validation.
3. Chunking Regression Corpus Expansion or Chunker Refinement Pass 2 follow-up.
4. Structural Hierarchy Anchor after core RSVP/navigability validation is stable.

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
- No structural hierarchy headers before core RSVP/navigability validation is stable.
