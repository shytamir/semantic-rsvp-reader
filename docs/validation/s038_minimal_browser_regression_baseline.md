# S-038 Minimal Browser Regression Baseline Validation

## Harness And Environment

The project uses one Node runner, `scripts/run_browser_smoke.mjs`, with pinned
Playwright `1.61.1` and one Chromium-family browser. The runner starts the Flask
app in explicit dependency-light `rule_based` mode on an isolated local port,
loads a deterministic in-script Markdown fixture, and closes its browser and
server after the checks. CI installs Playwright and Chromium transiently; the
repository adds no package manifest, lockfile, framework, bundler, transpiler,
or broad browser matrix.

## Protected Flows

- Paste deterministic text and prepare a nontrivial schedule.
- Start playback and pause it through the visible control state.
- Seek through the progress anchor and confirm movement to a later chunk.
- Create a breakpoint through the established double-tap interaction and
  confirm the visible breakpoint state.
- Reset to the first chunk with playback paused.
- At `320x568`, reject catastrophic horizontal document overflow or reader and
  critical-control bounds escaping the viewport.

## Deliberate Omissions

The smoke does not assert pixel-perfect rendering, screenshots, fonts, color,
animation timing, every responsive breakpoint, cross-browser parity, real
touch hardware, gesture ergonomics, accessibility quality, safe-area behavior,
orientation changes, background/foreground lifecycle, speed/adaptation quality,
defect reporting, semantic reading quality, pacing, fatigue, or comprehension.
It does not replace S-036 evidence or qualitative phone validation.

## Automated Results

On 2026-07-12 the exact runner passed locally on Windows using managed Python
`3.12.13`, managed Node `24.14.0`, bundled Playwright `1.61.1`, and Microsoft
Edge as the Chromium-family browser. A separate in-app browser confirmation
loaded the deterministic fixture and observed the play-to-pause-to-play control
transition. No product regression or minimal testability blocker was
reproduced, so product HTML, CSS, and JavaScript remain unchanged.

CI execution is the remote gate. Record its immediately available result for
the implementation commit without treating a pending run as passed.

## Fixed Human Confirmation Protocol

Use the intended phone/browser and the standard parser-default development
profile. Record the implementation commit - 3ff8cb2, device - samsung s23 ultra, android 16, firefox 152,
portrait, and each step as `passed`, `partially_passed`, `failed`,
`skipped`, or `inconclusive`.

1. Load one project validation sample and enter reader mode. Confirm the sample
   loads, the first chunk and progress are legible, and controls are available.
   `passed`
2. Start playback, pause, and resume. Confirm the visible state and timing feel
   stable enough for the existing prototype; automation proves only the state
   transition.
   `passed`
3. Perform one coarse progress seek and create one breakpoint with the existing
   double-tap gesture. Confirm both interactions are understandable and do not
   interfere with ordinary reader use.
   `passed`
4. Press Reset. Confirm the first chunk returns, playback is paused, and the
   state is understandable.
   `passed`
5. At a narrow portrait viewport, inspect the active chunk, progress, and
   critical controls. Confirm there is no catastrophic clipping or horizontal
   escape and record any non-blocking visual or touch-quality observation.
   `passed`
6. Review the deliberate omissions above and confirm the automated paths are a
   useful regression baseline without replacing qualitative phone validation.
   `passed` Human confirmed above automated paths are indeed a useful regression baseline. Not replacing qualitative phone validation is approved.

## Huamn Disposition
`passed`
all protocol steps passed. the regression baseline seems useful to me. we may proceed.

The human records the S-038 gate outcome and any blocking defect. Do not close
issue #13 or activate S-039 from automated evidence alone.
