# Refinement Roadmap

The near-term goal is to refine the reading experience using observed defects rather than speculative feature additions.

## Current Phase: Chunker-Dominant Refinement

**Goal:** Improve phrase-level chunk quality while keeping timing, speed, adaptation, and playback semantics stable.

- **Done:** In-app backend defect reporting.
- **Done:** Defect report security hardening.
- **Done:** Timing-context defect instrumentation.
- **Done:** Chunking Refinement Pass 1 from observed reports.
- **Done:** Display/tokenization noise cleanup and timing-only review filtering.
- **Done:** Timing Calibration Pass 1.
- **Done:** Refreshed validation corpus to reduce overfitting.
- **Done:** Third-pass post-calibration timing report review.
- **Done:** Post-validation targeted calibration.
- **Done:** Quote/parenthetical display-state annotation and defect taxonomy prep.
- **Current:** Prepare Chunker Refinement Pass 2 using clearer defect categories.

**Gate:** Collect enough clean chunking/display-state evidence to identify repeated phrase-boundary patterns without treating every discomfort as timing.

## Next Slice 1: Chunker Refinement Pass 2

**Goal:** Address recurring name/title/honorific, article-noun, preposition/pronoun bookend, and weak-boundary chunk defects.

**Gate:** Changes are deterministic, covered by focused tests, and do not alter timing formulas.

## Next Slice 2: Quote/Parenthetical Validation Pass

**Goal:** Check whether quote and parenthetical state indicators help orientation without moving the anchored text or adding visual clutter.

**Gate:** Defects classify visual context with `quote_state_confusion` or `parenthetical_state_confusion`, and rhythm with `punctuation_rhythm_issue` only when visual state is clear.

## Next Slice 3: Timing Calibration Pass 2, If Justified

**Goal:** Make another timing formula change only if clean reports show repeated pure timing defects.

**Gate:** Any adjustment is narrow, test-covered, and backed by timing-context evidence.

## Next Slice 4: Session Summary / Validation UX Polish

**Goal:** Improve demo validation ergonomics without changing timing semantics.

**Gate:** A tester can finish a session and understand what happened without reading raw debug output.

## Explicit Non-Goals For The Current Phase

- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
- No broad timing redesign during chunker-dominant refinement.
