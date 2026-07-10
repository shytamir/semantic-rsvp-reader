# Navigation & Navigability

## Purpose

Navigation features provide orientation and recovery without turning the reader into a conventional scrolling interface.

## Implemented Features

- Passive Spatial Anchor: subtle bottom progress bar with milestone-gated updates.
- Coarse tap-to-seek on the progress anchor.
- Breakpoint Bookmarking Traversal: double-tap current-stream breakpoints and swipe traversal when breakpoints exist.
- Ghost Previous Chunk: a low-contrast previous chunk above the active chunk, clipped to one line.
- Drift Recovery: breakpoint traversal can land up to three chunks before the target, pause briefly, then auto-resume.
- Structural Hierarchy Anchor: simple Markdown H1/H2 labels as a static top orientation aid.

## Constraints

- Low peripheral distraction.
- No animation-heavy navigation UI.
- No persistent accounts or cross-session bookmarks.
- Progress seek and ordinary manual previous/next do not use drift recovery.

## Validation Notes

Use [navigation_validation.md](../validation/navigation_validation.md) for current validation focus and manual checks.

## Known Limitations

- Orientation aids can mask chunking defects.
- Drift recovery may feel surprising if validation shows the auto-resume is too aggressive.
- CSS-only tests may miss device-specific layout issues.
