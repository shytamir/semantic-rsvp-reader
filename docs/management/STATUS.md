# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Validation-driven refinement: cleaning evidence quality before timing calibration.
> **Immediate Focus:** Evidence hygiene plus display/tokenization noise cleanup.

## Current Project Phase

The prototype is in validation-driven refinement. The current goal is to reduce false timing evidence caused by layout, tokenization, and chunking noise before changing timing formulas.

## Completed Slices

1. Flask + CI scaffold.
2. Mobile-first Flask/HTML5 reading shell.
3. Text ingestion, normalization, sentence segmentation, semantic chunking, and deterministic scheduling.
4. Mobile playback loop with controls, gestures, session-only speed controls, event tracking, and conservative adaptation.
5. Mobile hardening for timers, visibility changes, loading, local network use, and compact phone layouts.
6. Backend-stored compressed defect reports with bounded/escaped fields, generated filenames, request limits, and storage-encryption warnings.
7. Timing-context defect instrumentation and defect review export.
8. Chunking Refinement Pass 1 from observed validation defects.

## Current Slice

Evidence Hygiene + Display/Tokenization Noise Cleanup:

- prevent chunk display hyphenation and within-word browser splitting;
- record display width/overflow metadata in defect reports;
- protect `a.m.`, `p.m.`, `U.S.`, and `E.U.` from sentence/tokenization noise;
- conservatively improve `whether ... would` chunking;
- add timing-only review filtering so older reports without Timing Context can be excluded.

## Next 4 Planned Slices

1. Clean timing validation pass.
2. Timing Calibration Pass 1.
3. Post-calibration validation review.
4. Demo/beta readiness pass.

## Known Risks

- Timing reports can still be polluted if layout defects are reported under timing categories.
- Rule-based chunking remains conservative and may need more observed examples before broader grammar handling.
- Mobile browser rendering differences may still affect very long unbroken tokens.
- The project intentionally uses session-only telemetry, so long-term user modeling is out of scope.

## Explicit Non-Goals

- No timing multiplier/formula calibration in the current slice.
- No adaptation behavior changes.
- No persistence model, accounts, analytics, offline mode, service workers, or deployment infrastructure.
- No NLP dependency additions such as spaCy, transformers, or ML chunking.
- No frontend framework, browser automation, EPUB/PDF import, or packaging work.
