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
- **Done:** Navigation Scaffolding Pass 1.
- **Done:** JavaScript syntax verification hardening.
- **Done:** Passive Spatial Anchor implementation.
- **Current:** Prepare Chunker Refinement Pass 2 using clearer defect categories.

**Gate:** Collect enough clean chunking/display-state evidence to identify repeated phrase-boundary patterns without treating every discomfort as timing.

## Next Slice 1: Proper Noun / Honorific / Article / Function-Word Chunking Refinement Pass

**Goal:** Address recurring name/title/honorific, article-noun, preposition/pronoun bookend, and weak-boundary chunk defects.

**Gate:** Changes are deterministic, covered by focused tests, and do not alter timing formulas.

## Next Slice 2: Breakpoint Bookmarking Traversal

**Goal:** Add breakpoint setting and traversal without fighting existing swipe and long-press gestures.

**Gate:** Gesture behavior is explicit, tested manually on mobile, and does not destabilize current chunk navigation.

## Next Slice 3: Drift Recovery Logic

**Goal:** Add the 3-chunk lead-in behavior for bookmark jumps.

**Gate:** Recovery feels predictable, avoids surprise autoplay, and can be validated without masking chunking defects.

## Next Slice 4: Post-Navigation Usability Validation

**Goal:** Validate the passive anchor, coarse seek, and later navigation behavior without letting navigation mask chunking defects.

**Gate:** Remaining issues are classified cleanly as navigation, chunking, timing, or layout defects.

## Explicit Non-Goals For The Current Phase

- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
- No broad timing redesign during chunker-dominant refinement.
- No bookmark traversal or drift recovery before their dedicated implementation slices.
