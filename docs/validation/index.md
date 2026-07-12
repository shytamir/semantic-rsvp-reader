# Validation Docs

Historical slice validation records are preserved in the [validation archive](archive/index.md).

## Active Validation Focus

- [Post-Validation Stabilization Pass 1](post_validation_stabilization_pass_1.md)
- [Navigation Validation](navigation_validation.md)
- [S-033 Mobile Presentation and Accessibility Validation](archive/s033_mobile_presentation_accessibility_validation.md)
- [S-034 Evidence Capture and Reproducibility Validation](s034_evidence_capture_reproducibility_validation.md)
- [Issue #11 Coarse-Seek Accessibility Validation](issue_11_coarse_seek_accessibility_validation.md)
- [S-035 Service Surfaces and Fallback Validation](s035_service_surfaces_fallback_validation.md)
- [S-035A Development Environment Contract Validation](s035a_environment_contract_validation.md)
- [S-035B QA Authority Validation](s035b_qa_authority_validation.md)
- [S-036 End-to-End Prototype Readiness Validation](s036_end_to_end_prototype_readiness.md)
- [Validation Corpus](corpus.md)

Current focus:

1. S-026 parser-assisted Flask prototype integration passed human validation with no acceptance-blocking regressions.
2. S-027 post-navigation usability validation completed as `passed`; the recorded evidence is in [Navigation Validation](navigation_validation.md).
3. S-029 Density-Aware Dwell-Time Recalibration completed as `passed`.
4. S-030 Semantic Output and Structural Integrity completed as `passed`; non-blocking semantic observations remain evaluation evidence.
5. S-031 Playback and Adaptation completed as `passed`; both fixed human scenarios reported zero defects.
6. S-032 Navigation and Interaction completed as `passed`; all seven fixed human protocol steps reported no defects.
7. S-033 Mobile Presentation and Accessibility completed as `passed`; all eight human checks passed with no acceptance-blocking defect.
8. S-034 Evidence Capture and Reproducibility completed as `passed`; all seven human steps passed with complete and practical report context.
9. Issue #11 coarse-seek accessibility maintenance completed; its low-priority landscape obstruction is tracked separately in issue #19.
10. S-035 Service Surfaces and Fallback completed as `passed`; human profile checks and automated standard-profile API coverage are complete.
11. S-035A and S-035B completed as `passed`; S-036 is active at `AWAITING_HUMAN_VALIDATION` with automated readiness evidence and a fixed human session.
12. Parser-assisted chunking remains frozen unless a new authorized evaluation slice changes it.

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
