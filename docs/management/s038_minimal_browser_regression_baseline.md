# S-038 Minimal Browser Regression Baseline

## Status

`AWAITING_HUMAN_VALIDATION`, active, and owned by the human. The bounded automated baseline passes locally; GitHub issue #13 remains open as detailed authority. Use the fixed [S-038 confirmation protocol](../validation/s038_minimal_browser_regression_baseline.md). [S-038A](s038_parser_ci_evaluation_surface.md) is the provisional immediate successor; S-038A and S-039 through S-043 remain inactive and unauthorized.

## Objective

Add a deliberately small browser regression baseline for the stabilized interaction model before architectural or ingestion work.

## Dependency And Initiating Reason

Depends on S-037 preserving or explicitly updating parser operating policy. Later productization work needs protection against critical interaction regressions.

## In Scope

- Smoke coverage for text loading, playback, pause/resume, progress seeking, breakpoints, and critical reset behavior.
- One bounded check for catastrophic narrow/mobile layout failure.
- Deterministic fixtures and proportionate local/CI execution.

## Codex Preparation

Maintain one Playwright/Chromium-family smoke runner with a deterministic local fixture and explicit assertions for the protected flows. Keep browser automation supplementary to qualitative phone validation.

## Human Handoff

Confirm the smoke paths represent the stabilized interaction model and do not replace qualitative phone validation.

## Permissible Narrow Work

Fix only a reproduced regression or minimal testability blocker in protected flows.

## Non-Goals

No broad browser matrix, exhaustive visual testing, frontend framework, general npm migration, interaction redesign, or replacement of human usability gates.

## Completion Boundary

The bounded smoke suite passes locally and remotely with documented limits. No successor activates automatically.
