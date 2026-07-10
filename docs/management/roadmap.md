# Refinement Roadmap

The near-term goal is to refine the reading experience using observed defects rather than speculative feature additions.

## Current Phase: Validation-Driven Stabilization

**Goal:** Stabilize the mobile reading surface and refine observed chunk/source-boundary defects while keeping timing, speed, adaptation, navigation, and playback semantics stable.

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
- **Done:** Chunker Refinement Pass 2.
- **Done:** Breakpoint Bookmarking Traversal.
- **Done:** Ghost Previous Chunk.
- **Done:** Drift Recovery Logic.
- **Done:** Structural Hierarchy Anchor.
- **Done:** Post-Validation Stabilization Pass 1.
- **Current:** Validate ghost/active chunk layout, source boundaries, long-form dates, and targeted phrase-cohesion repairs against fresh mobile evidence.

**Gate:** Confirm the pass resolves mobile layout/visibility blockers and reduces source-boundary and phrase-cohesion defects without creating overlong chunks, over-clumped ordinary prose, or timing-masked discomfort.

## Done Slice: Post-Validation Stabilization Pass 1

**Goal:** Address the 39-defect third chunking validation pass.

**Status:** Implemented mobile ghost/active chunk layout stabilization first, then source-boundary preservation, long-form date cohesion, and targeted phrasal verb, qualifier-pair, coordinated-form, noun-preposition, proper-name, title, underdense, and overlong repairs.

## Next Slice 1: Post-Stabilization Validation Pass

**Goal:** Validate mobile ghost layout and source-boundary chunking on Android/Firefox and desktop.

**Gate:** Confirm active font size remains stable, ghost text never overlaps the active chunk, headings/bylines/dates do not merge into prose, and remaining issues are classified cleanly as chunking, timing, display state, layout, or navigation defects.

## Done Slice: Breakpoint Bookmarking Traversal

**Goal:** Add current-stream breakpoint setting and traversal without fighting long-press speed controls.

**Status:** Implemented with double-tap toggle, swipe traversal when breakpoints exist, chunk-step swipe fallback when none exist, and subtle flash feedback. Drift recovery is intentionally not included.

## Done Slice: Drift Recovery Logic

**Goal:** Add the 3-chunk lead-in behavior for bookmark jumps.

**Status:** Implemented for breakpoint traversal only. Jumps land at `max(0, n - 3)`, pause 500ms, and auto-resume unless cancelled by explicit user action.

## Next Slice 2: Chunking Regression Corpus Expansion

**Goal:** Expand focused regression coverage if stabilization validates well.

**Gate:** New chunker changes remain report-driven and do not alter timing formulas.

## Next Slice 3: Post-Navigation Usability Validation

**Goal:** Validate the passive anchor, coarse seek, and later navigation behavior without letting navigation mask chunking defects.

**Gate:** Remaining issues are classified cleanly as navigation, chunking, timing, or layout defects.

## Done Slice: Structural Hierarchy Anchor

**Goal:** Provide a static orientation label from simple Markdown `#` and `##` headers.

**Status:** Implemented as schedule structure metadata, a fixed low-distraction reader label, and structural context in defect reports. This is not a full Markdown renderer.

## Next Slice 4: Demo/Beta Readiness Cleanup

**Goal:** Clean up documentation, validation workflow, and small ergonomics after core RSVP/navigability validation.

**Gate:** No new major feature surface is introduced.

## Explicit Non-Goals For The Current Phase

- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
- No broad timing redesign during chunker-dominant refinement.
- No full Markdown rendering, heading navigation, or table of contents.
