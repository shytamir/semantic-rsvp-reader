# TODO.md

## Development Tooling

- [x] **JavaScript Syntax Verification Hardening**
  - Added a lightweight `node --check` wrapper.
  - GitHub Actions installs Node and enforces the check.
  - No npm or frontend toolchain added.

## Chunker-Dominant Refinement
*Goal: Improve phrase-boundary quality while keeping timing, speed, adaptation, and playback semantics stable.*

- [ ] **Chunker Refinement Pass 2**
  - Focus on honorific/name, title/name, proper-name, article/noun, preposition/pronoun bookend, and weak-boundary defects.
  - Requirement: Use observed reports and focused tests before changing chunking rules.

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

- [ ] **Spatial Anchor (Passive Progress Bar)**
  - Implement a 2px-high, low-opacity (#333) progress bar at the bottom of the viewport.
  - Requirement: Update only at significant logical boundaries (paragraph breaks or every 5% character count) to avoid flicker/strobe effects.
  - Interaction: Single-tap to seek (coarse navigation).

- [ ] **Breakpoint Bookmarking Traversal**
  - Implement gesture-based bookmarking (e.g., Double-tap or Long-press) to set persistent breakpoints in the stream.
  - Implement gesture-based traversal (Swipe Left/Right) to jump between saved breakpoints.
  - Visual Feedback: Subtle, 1-frame background shade shift (no animations/borders).

- [ ] **Drift Recovery Logic (The 3-Chunk Lead-in)**
  - Implement a state-recovery mechanic for when the user jumps to a bookmark.
  - Logic: Upon jumping to breakpoint `n`, the engine should automatically pause at `n-3` for 500ms before resuming, providing the brain a "buffer" to re-orient to the sentence structure.

## Backlog / Post-Validation
- [ ] **Structural Hierarchy Anchor**
  - Detect Markdown headers (#, ##) during ingestion and display as a static label at the top of the viewport.
  - Requirement: Maintain static positioning; no movement.
