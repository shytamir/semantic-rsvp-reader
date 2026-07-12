# Validation Docs

Historical slice validation records are preserved in the [validation archive](archive/index.md).

## Active Validation Focus

- [S-031 Playback and Adaptation Validation](s031_playback_adaptation_validation.md)
- [Post-Validation Stabilization Pass 1](post_validation_stabilization_pass_1.md)
- [Navigation Validation](navigation_validation.md)
- [S-033 Mobile Presentation and Accessibility Validation](s033_mobile_presentation_accessibility_validation.md)
- [Validation Corpus](corpus.md)

Current focus:

1. S-026 parser-assisted Flask prototype integration passed human validation with no acceptance-blocking regressions.
2. S-027 post-navigation usability validation completed as `passed`; the recorded evidence is in [Navigation Validation](navigation_validation.md).
3. S-029 Density-Aware Dwell-Time Recalibration completed as `passed`.
4. S-030 Semantic Output and Structural Integrity completed as `passed`; non-blocking semantic observations remain evaluation evidence.
5. S-031 Playback and Adaptation completed as `passed`; both fixed human scenarios reported zero defects.
6. S-032 Navigation and Interaction completed as `passed`; all seven fixed human protocol steps reported no defects.
7. S-033 Mobile Presentation and Accessibility is the sole active slice at `AWAITING_HUMAN_VALIDATION`; the fixed phone-browser protocol is ready.
8. Parser-assisted chunking remains frozen unless a new authorized evaluation slice changes it.

## Defect Reporting Workflow

- [In-app defect reporting](in_app_defect_reporting.md)
- [Defect log template](defect_log_template.md)
- [Defect taxonomy](defect_taxonomy.md)
- Review utility: `scripts/review_defects.py`

## Chunking Validation History

- [Observed defects first pass](observed_defects_first_pass.md) historical
- [Chunking Refinement Pass 1](chunking_refinement_pass_1.md)
- [Chunking Refinement Pass 2](chunking_refinement_pass_2.md)
- [Chunking Refinement Pass 2 Results](chunking_refinement_pass_2_results.md)
- [Chunking Refinement Pass 3](chunking_refinement_pass_3.md)
- [Post-Validation Stabilization Pass 1](post_validation_stabilization_pass_1.md)

## Timing Validation History

- [Timing defect collection](timing_defect_collection.md)
- [Observed timing defects first pass](observed_timing_defects_first_pass.md) historical
- [Observed timing defects second pass](observed_timing_defects_second_pass.md) historical
- [Observed timing defects third pass](observed_timing_defects_third_pass.md) historical
- [Timing Calibration Pass 1](timing_calibration_pass_1.md)
- [Post-validation targeted calibration](post_validation_targeted_calibration.md)

## Display State And Navigation

- [Quote/parenthetical state indicators](quote_parenthetical_state_indicators.md)
- [Navigation validation](navigation_validation.md)

## Review Utilities

- `scripts/review_defects.py`: aggregate, filter, and export backend defect reports.
- `scripts/schedule_sample.py`: inspect schedule output from a file or stdin.
