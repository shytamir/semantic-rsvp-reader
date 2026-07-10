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
- **Current:** Prepare Chunker Refinement Pass 2 using clearer defect categories.

**Gate:** Collect enough clean chunking/display-state evidence to identify repeated phrase-boundary patterns without treating every discomfort as timing.

## Next Slice 1: Proper Noun / Honorific / Article / Function-Word Chunking Refinement Pass

**Goal:** Address recurring name/title/honorific, article-noun, preposition/pronoun bookend, and weak-boundary chunk defects.

**Gate:** Changes are deterministic, covered by focused tests, and do not alter timing formulas.

## Next Slice 2: Passive Spatial Anchor Implementation

**Goal:** Turn existing paragraph/progress metadata into a subtle 2px passive progress anchor.

**Gate:** Updates occur only at paragraph breaks or 5% progress milestones, with no flicker or peripheral distraction.

## Next Slice 3: Breakpoint Bookmarking Traversal

**Goal:** Add breakpoint setting and traversal without fighting existing swipe and long-press gestures.

**Gate:** Gesture behavior is explicit, tested manually on mobile, and does not destabilize current chunk navigation.

## Next Slice 4: Drift Recovery Logic

**Goal:** Add the 3-chunk lead-in behavior for bookmark jumps.

**Gate:** Recovery feels predictable, avoids surprise autoplay, and can be validated without masking chunking defects.

## Explicit Non-Goals For The Current Phase

- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
- No broad timing redesign during chunker-dominant refinement.
- No active navigation behavior before its dedicated implementation slice.
