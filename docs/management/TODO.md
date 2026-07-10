# TODO.md

## Development Tooling

- [x] **JavaScript Syntax Verification Hardening**
  - Added a lightweight `node --check` wrapper.
  - GitHub Actions installs Node and enforces the check.
  - No npm or frontend toolchain added.

## Chunker-Dominant Refinement
*Goal: Improve phrase-boundary quality while keeping timing, speed, adaptation, and playback semantics stable.*

- [x] **Chunker Refinement Pass 2**
  - Focus on honorific/name, title/name, proper-name, article/noun, preposition/pronoun bookend, and weak-boundary defects.
  - Requirement: Use observed reports and focused tests before changing chunking rules.
  - Completed with focused regressions for observed named entities, honorific/title phrases, article modifier/head phrases, preposition-led phrases, and curly apostrophe tokenization.

- [ ] **Post-Chunker Refinement Pass 2 Validation**
  - Validate on fresh text containing repeated named entities, institutions, titles, article phrases, and weak preposition/function-word boundaries.
  - Requirement: Watch for overlong chunks, over-clumped ordinary prose, and timing complaints caused by denser chunk shapes.

- [ ] **Quote/Parenthetical Validation**
  - Validate the new quote and parenthetical display-state indicators on mobile.
  - Requirement: Classify visual context defects separately from punctuation rhythm defects.

## Navigation & Navigability
*Goal: Address user orientation and state recovery without introducing UI clutter or peripheral distraction.*

- [x] **Navigation Scaffolding Pass 1**
  - Added schedule-level navigation metadata.
  - Added paragraph/progress milestone scaffolding.
  - Added dormant frontend helpers and hidden UI placeholders.
  - No user-visible navigation behavior enabled yet.

- [x] **Spatial Anchor (Passive Progress Bar)**
  - Implement a 2px-high, low-opacity (#333) progress bar at the bottom of the viewport.
  - Requirement: Update only at significant logical boundaries (paragraph breaks or every 5% character count) to avoid flicker/strobe effects.
  - Interaction: Single-tap to seek (coarse navigation).
  - Implemented as a milestone-gated passive anchor with coarse tap-to-seek.

- [x] **Breakpoint Bookmarking Traversal**
  - Implement gesture-based bookmarking (e.g., Double-tap or Long-press) to set persistent breakpoints in the stream.
  - Implement gesture-based traversal (Swipe Left/Right) to jump between saved breakpoints.
  - Visual Feedback: Subtle, 1-frame background shade shift (no animations/borders).
  - Implemented with double-tap toggle, current-stream/session-only breakpoints, swipe traversal when breakpoints exist, chunk-step swipe fallback when none exist, and subtle reader-surface flash feedback.

- [x] **Ghost Previous Chunk**
  - Displays the immediately previous chunk above the current chunk at reduced contrast.
  - Adds previous displayed chunk context to defect reports.

- [x] **Drift Recovery Logic (The 3-Chunk Lead-in)**
  - Implement a state-recovery mechanic for when the user jumps to a bookmark.
  - Logic: Upon jumping to breakpoint `n`, the engine should automatically pause at `n-3` for 500ms before resuming, providing the brain a "buffer" to re-orient to the sentence structure.
  - Implemented for breakpoint traversal only; progress seek, reset, manual previous/next, and ordinary swipe fallback do not use drift recovery.

## Backlog / Post-Validation
- [x] **Structural Hierarchy Anchor**
  - Detect Markdown headers (#, ##) during ingestion and display as a static label at the top of the viewport.
  - Requirement: Maintain static positioning; no movement.
  - Implemented simple `#`/`##` detection, schedule structure metadata, a static top label, and structural context in defect reports.
