# Validation Docs

## Active Validation Focus

- [Post-Validation Stabilization Pass 1](post_validation_stabilization_pass_1.md)
- [Navigation Validation](navigation_validation.md)
- [Validation Corpus](corpus.md)

Current focus:

1. Confirm ghost previous chunk never overlaps active text.
2. Confirm active chunk font size remains stable.
3. Validate title/byline/date/source boundaries.
4. Watch for over-clumping from phrase preservation.

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
