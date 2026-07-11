# S-031 Playback and Adaptation

## Status

Active and authorized for implementation at `READY_FOR_IMPLEMENTATION`. S-032 remains scheduled and inactive.

## Objective

Validate the shipped reader lifecycle, speed controls, visibility behavior, and conservative session-only adaptation without disturbing the passed S-029 dwell calibration.

## Initiating Reason

Playback combines timers, manual controls, document visibility, session events, and adaptation suppression; these interactions need a focused integrated pass after timing stabilization.

## In Scope

- Play, pause, resume, manual previous/next, completion, reset, return-to-edit, and loading new text.
- Speed overlay, bounded speed levels, reset, current-chunk continuity, visibility pause behavior, and timer cancellation.
- Adaptation enable/disable/reset, rewind/pause and smooth-run signals, manual-change suppression, session reset, and interaction with seeking.

## Codex Preparation

Characterize existing state transitions and static/test coverage, run relevant Python and JavaScript checks, and prepare fixed baseline and adaptation-enabled scenarios with observable session summaries.

## Human Handoff

Exercise lifecycle and controls on a phone browser, including background/foreground transitions, completion, speed changes, and comparable adaptation-off/on passages.

## Permissible Stabilization

Fix only a reproduced lifecycle, timer, control, visibility, or conservative-adaptation defect with focused regression coverage.

## Non-Goals

No S-029 recalibration change without specific regression evidence, persistent profiles, analytics, new speed values, adaptation redesign, navigation work, or layout polish.

## Completion Boundary

Lifecycle and adaptation evidence is recorded and any narrow authorized defect is stabilized. Transition through `AWAITING_HUMAN_VALIDATION` where qualitative rhythm/control judgment is required; do not activate S-032 automatically.
