# Project Decisions

This file records durable decisions, not every implementation detail.

## D-001: Deterministic Chunking Over Opaque Parsing

The reader uses inspectable Python chunking rules instead of an ML parser. This keeps validation evidence traceable and avoids adding NLP dependencies before the prototype has stronger qualitative evidence.

Consequence: chunking improvements should stay tied to observed defects and focused regression tests.

## D-002: Validation-driven Refinement

The project advances through observed validation evidence rather than speculative feature expansion.

Consequence: STATUS names one active slice, the roadmap orders near-term work, and completed slices move to HISTORY.

## D-003: Human-owned Qualitative Gates

Codex can implement, test, and maintain docs, but the human owner is the acceptance authority for usability and reading-comfort gates.

Consequence: Codex must not declare a validation gate passed without human evidence.

## D-004: Baseline And Exploratory Validation Stay Separate

Comparable validation uses fixed conditions: same device/browser where practical, fixed recorded speed, adaptation disabled, fixed corpus subset, predetermined exposure, and comparable reports.

Consequence: exploratory reading remains useful but should not be treated as baseline evidence.

## D-005: Navigation Is Session-only And Low-distraction

Navigation aids are designed for orientation without adding persistence, accounts, or heavy UI.

Consequence: passive anchor, breakpoints, ghost chunk, drift recovery, and structural labels should stay lightweight unless validation evidence says otherwise.

## D-006: Source-boundary Preservation Before Full Document Rendering

The reader preserves simple source, title, byline, date, and heading boundaries without becoming a full Markdown/article renderer.

Consequence: full Markdown rendering, heading navigation, and table of contents remain parked.
