# S-032 Navigation and Interaction

## Status

Active and authorized for implementation at `READY_FOR_IMPLEMENTATION`, owned by Codex. S-033 remains scheduled and inactive.

## Objective

Validate functional navigation and recovery behavior across the shipped reader without conflating presentation polish with interaction correctness.

## Initiating Reason

Gestures, coarse seeking, breakpoint traversal, ghost context, drift recovery, and structural orientation share state and cancellation paths that require an integrated functional pass.

## In Scope

- Tap play/pause, swipe chunk traversal, hold-swipe jumps, long-press coexistence, and browser-gesture suppression.
- Milestone progress anchor and coarse seek.
- Breakpoint add/remove/reset/traversal, ghost previous chunk updates, drift lead-in/auto-resume/cancellation, and active H1/H2 orientation updates.

## Codex Preparation

Run navigation metadata, shell, syntax, and related integration checks; prepare deterministic streams and an interaction matrix covering ordinary, breakpoint, seek, reset, and cancellation paths.

## Human Handoff

Execute the focused gesture, seeking, breakpoint, ghost, drift-recovery, and structural-orientation protocol on representative phone-browser streams.

## Permissible Stabilization

Fix only a reproduced functional state, gesture arbitration, target, cancellation, or metadata defect. Presentation-only findings are recorded for S-033 unless they block functional validation.

## Non-Goals

No layout redesign, animation-heavy UI, persistent bookmarks, conventional scrolling reader, timing/adaptation redesign, or new navigation feature family.

## Completion Boundary

Functional paths are characterized, human interaction evidence is recorded, and blocking defects are narrowly stabilized. Do not activate S-033 automatically.
