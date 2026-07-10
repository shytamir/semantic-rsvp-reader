# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Chunker-dominant refinement.
> **Immediate Focus:** Collect and address chunk quality defects without further timing calibration unless clean evidence justifies it.

## Current Project Phase

Timing has improved enough that the next useful work is chunk quality. Recent validation evidence points to phrase-boundary issues around names, titles, articles, prepositions, pronouns, quotes, and parentheticals. This phase keeps timing stable while improving report quality and preparing targeted chunker changes.

## Completed Recent Slices

1. Backend defect reporting and security hardening.
2. Chunking Refinement Pass 1.
3. Timing-context instrumentation.
4. Evidence hygiene/display/tokenization cleanup.
5. Timing Calibration Pass 1.
6. Refreshed validation corpus.
7. Post-validation targeted calibration.
8. Quote/parenthetical state annotation and reporting prep.

## Current Evidence

The latest timing passes reduced the strongest timing complaints, while remaining recurring defects increasingly describe chunk shape, phrase attachment, and display-state orientation. Defect reports now include quote and parenthetical state so future reviews can separate visual context confusion from timing rhythm.

## Next 4 Planned Slices

1. Chunker Refinement Pass 2 for names, titles, honorifics, articles, prepositions, and weak boundaries.
2. Quote/parenthetical validation pass using the new display-state categories.
3. Timing Calibration Pass 2 only if clean timing-context reports show repeated timing-only defects.
4. Session summary / validation UX polish.

## Known Risks

- Overfitting chunking rules to a small validation set.
- Misclassifying chunk shape defects as timing defects.
- Quote/parenthetical indicators being too subtle or too visually heavy.
- Proper-name heuristics improving one sample while harming ordinary prose.
- Adaptation or speed changes masking baseline schedule quality.

## Explicit Non-Goals

- No ML parser.
- No EPUB/PDF import.
- No accounts.
- No cloud analytics.
- No native app.
- No public performance claims.
- No broad timing redesign during chunker-dominant refinement.
