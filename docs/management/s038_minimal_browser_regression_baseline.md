# S-038 Minimal Browser Regression Baseline

## Status

Provisional post-S-037 scope. Not active or authorized.

## Objective

Add a deliberately small browser regression baseline for the stabilized interaction model before architectural or ingestion work.

## Dependency And Initiating Reason

Depends on S-037 preserving or explicitly updating parser operating policy. Later productization work needs protection against critical interaction regressions.

## In Scope

- Smoke coverage for text loading, playback, pause/resume, progress seeking, breakpoints, and critical reset behavior.
- One bounded check for catastrophic narrow/mobile layout failure.
- Deterministic fixtures and proportionate local/CI execution.

## Codex Preparation

Characterize stable DOM and interaction contracts, select the smallest maintainable harness, and document protected flows and omissions.

## Human Handoff

Confirm the smoke paths represent the stabilized interaction model and do not replace qualitative phone validation.

## Permissible Narrow Work

Fix only a reproduced regression or minimal testability blocker in protected flows.

## Non-Goals

No broad browser matrix, exhaustive visual testing, frontend framework, general npm migration, interaction redesign, or replacement of human usability gates.

## Completion Boundary

The bounded smoke suite passes locally and remotely with documented limits. No successor activates automatically.
