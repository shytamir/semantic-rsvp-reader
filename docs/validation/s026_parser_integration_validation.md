# S-026 Parser Integration Validation

Use this checklist to validate the provisional parser-assisted Flask prototype default after integration.

Do not close S-026 until this validation is performed and any acceptance-blocking regressions are recorded.

## Human Validation Result

Date recorded: 2026-07-11

S-026 completed as `passed`.

The human validator reported that the protocol went smoothly, the implementation behaved as expected, and no acceptance-blocking regressions were observed.

This result records the human acceptance disposition without inventing checklist-level observations or unreported minor defects.

## Checklist

1. Install the standard prototype environment with `pip install -r requirements.txt`.
2. Start the app normally and confirm it starts without downloading a model at runtime.
3. Open `/health` and confirm it reports `status: ok`, `configured_mode: parser_assisted`, and parser-provider availability when the pinned provider is installed.
4. Read representative validation samples on a phone browser.
5. Confirm known semantic improvements from S-024 remain visible in normal use.
6. Check whether denser parser-assisted chunks remain comfortable during timed playback.
7. Confirm controls, navigation, timing, ghost chunk, breakpoints, structural labels, and defect reporting still behave normally.
8. Force `RSVP_CHUNKER_MODE=rule_based` and confirm the application still starts and schedules text.
9. Simulate or temporarily remove the parser/model and confirm automatic fallback still returns schedules.
10. Confirm fallback warnings identify reason categories without exposing source text in logs.
11. Record any acceptance-blocking regressions before closing S-026.

## Scope Notes

- This validates the current Python/Flask browser prototype only.
- spaCy remains provisional and nonexclusive under D-008 and D-009.
- `RuleBasedChunker` remains the mandatory fallback and explicit baseline.
- Optimizer retuning, provider ablation, native/mobile provider decisions, and public performance claims are out of scope for this validation.
