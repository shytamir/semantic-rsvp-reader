# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Chunker-dominant refinement.
> **Immediate Focus:** Validate Chunker Refinement Pass 2 while keeping navigation additions conservative and low-distraction.

## Current Project Phase

Timing has improved enough that the current useful work is chunk quality. Chunker Refinement Pass 2 addressed repeated phrase-boundary issues around names, titles, articles, prepositions, and apostrophe tokenization while keeping timing/playback semantics stable. This phase now needs post-pass validation and conservative navigability work that avoids peripheral distraction.

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

## Current Evidence

The latest timing passes reduced the strongest timing complaints, while remaining recurring defects increasingly describe chunk shape, phrase attachment, and display-state orientation. Chunker Refinement Pass 2 used the latest chunking report to address proper-name splits, honorific/title splits, article phrase splits, weak preposition-led chunks, and curly apostrophe suffix orphans. Defect reports now include quote, parenthetical, and optional navigation state so future reviews can separate visual context and orientation evidence from timing rhythm.

JavaScript syntax checking is now CI-backed through a lightweight `node --check` wrapper. Local environments without Node skip with a warning; CI installs Node and enforces the check.

The Passive Spatial Anchor is implemented as a subtle bottom progress bar with milestone-gated updates and coarse tap-to-seek. Active bookmark traversal and drift recovery remain future slices.

## Next 4 Planned Slices

1. Post-Chunker Refinement Pass 2 validation.
2. Breakpoint Bookmarking Traversal.
3. Drift Recovery Logic.
4. Post-navigation usability validation.

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
