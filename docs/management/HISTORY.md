# Completed Slice History

This file records completed work. It does not define current priorities.

## Recent Completed Slices

| Slice | Outcome | Evidence |
| --- | --- | --- |
| Issue #11: Coarse-Seek Accessibility Maintenance | Completed. Human accepted the enlarged touch target and authorized closure. A low-priority phone-landscape obstruction remains separately tracked without changing seek semantics. | Human evidence commit `a52e79f`; [validation](../validation/issue_11_coarse_seek_accessibility_validation.md); GitHub issues #11 and #19 |
| S-034: Evidence Capture and Reproducibility | Completed as `passed`. All seven human steps passed; four synthetic local reports were deleted; no missing context or impractical protocol step was found. | Human evidence commit `eafadbd`; [S-034 validation](../validation/s034_evidence_capture_reproducibility_validation.md); GitHub issue #8 |
| S-033: Mobile Presentation and Accessibility | Completed as `passed`. All eight human checks passed on Samsung Galaxy S23 Ultra / Android 16 / Mozilla Firefox 152 with no acceptance-blocking defect; the non-blocking coarse-seek touch-target observation is tracked separately. | Human evidence commit `3488946`; [S-033 validation](../validation/s033_mobile_presentation_accessibility_validation.md); GitHub issue #11 |
| S-032: Navigation and Interaction | Completed as `passed`. All seven fixed phone-browser protocol steps passed with no reported defects, including direction consistency, drift recovery, cancellation, seeking, reset/new-stream state, ghost context, and structural orientation. | Human evidence commit `3293d8f`; [navigation validation](../validation/navigation_validation.md#s-032-human-validation-outcome) |
| S-031: Playback and Adaptation | Completed as `passed`. Both fixed human scenarios passed with zero reported defects; session reset, playback lifecycle, visibility behavior, controls, and conservative adaptation behaved as intended. | Human evidence commit `f39dc15`; [S-031 validation](../validation/archive/s031_playback_adaptation_validation.md) |
| S-030: Semantic Output and Structural Integrity | Completed as `passed`. Human validation accepted parser-default and fallback output with non-blocking observations. A narrow CSS-only stabilization separated the structural orientation cue from the ghost chunk; semantic observations remain evaluation evidence. | Human evidence commit `c632b71`; [S-030 validation](../validation/archive/s030_semantic_structural_validation.md); [observed defects](../validation/archive/s030_observed_semantic_structural_defects.md) |
| S-029: Density-Aware Dwell-Time Recalibration | Completed as `passed`. Measurement found a 67.6% parser-assisted density increase per chunk; the bounded density dwell component increased parser passage timing by 16.8%. Human validation passed all six corpus samples and found default `1.0x` as manageable as the prior build at `0.85x`. | Commits `3c09437` and `b7e59cb`; [S-029 density and timing report](../validation/archive/s029_density_timing_report.md) |
| S-028: Compact CI and Evidence Integrity | Completed as `passed`. Added compact integrity, dependency-light core, and pinned parser-default GitHub Actions coverage; finalized the S-026 integration identity and registered hashes; and resolved GitHub issue #3. | Commits `95e88a7` and `dd07093`; [S-028 scope](archive/s028_compact_ci_evidence_integrity.md); [integration record](../../evaluation/parser_assisted_chunking/freeze/provisional_integration_record.json) |
| S-027: Post-Navigation Usability Validation | Completed as `passed`. Navigation behavior already exercised against the same integrated build during S-026 showed no acceptance-blocking regression, so no redundant complete rerun was required. Separate Markdown H1/H2 testing confirmed that the structural hierarchy anchor showed the active H1 or deepest active H2, updated through sections, and remained unobtrusive. | [Navigation validation](../validation/navigation_validation.md) |
| S-026: Provisional Parser-Assisted Prototype Integration | Completed as `passed`. Human validation reported a smooth protocol, expected implementation behavior, and no acceptance-blocking regressions. The frozen S-023 parser-assisted behavior remains the current Flask prototype default, with `RuleBasedChunker` preserved as mandatory fallback. | [S-026 validation record](../validation/archive/s026_parser_integration_validation.md); [provisional integration record](../../evaluation/parser_assisted_chunking/freeze/provisional_integration_record.json) |
| S-025: Post-experiment Disposition | Completed as `provisional_adoption_authorized`. The experimental hypothesis was supported; parser-assisted output won all 12 decisive blinded preferences. The current Flask prototype will adopt the frozen parser-assisted behavior, while spaCy remains provisional and nonexclusive under D-008 and rule-based fallback remains mandatory. | [D-009](DECISIONS.md); [S-024 human preference summary](../validation/archive/s024_human_ab_preference_summary.md) |
| S-024: Baseline versus Experiment Comparison | Completed as evidence gathered, not promoted. Ran redacted objective comparison against the authorized sealed blind challenge and scored the completed human A/B responses without committing the private identity key or per-case system mappings. | [S-024 objective comparison](../experiments/parser_assisted_chunking/s024_objective_comparison.md); [S-024 human preference summary](../validation/archive/s024_human_ab_preference_summary.md) |
| S-023: Parser-assisted Chunking Spike | Implemented as an isolated optional experiment, not promoted. Added pinned spaCy adapter, project-owned linguistic records, deterministic global optimizer, diagnostics, runner, visible development/regression results, and freeze records. | Commits `b010851` and freeze record commit; [S-023 freeze manifest](../../evaluation/parser_assisted_chunking/freeze/parser_assisted_implementation_freeze.json) |
| S-022: Landscape Ghost-Chunk Collision Stabilization | Completed as passed. Human validation confirmed GitHub issue #1 is resolved; the previous-chunk ghost now has a distinct visual lane from the active chunk in the targeted phone/orientation validation. | Commit `31f3d59`; GitHub issue #1 |
| S-021: Post-Stabilization Validation Pass | Completed as partially passed. Human validation found no major or parser-experiment-blocking regression; one narrow phone-landscape ghost/current chunk collision was promoted into S-022. Detailed in-app reports were accidentally deleted, so no report counts or reconstructed defect details are recorded. | [S-021 human summary](../validation/archive/s021_post_stabilization_human_summary.md); GitHub issue #1 |
| Repository Licensing Pass | Added Apache License 2.0 and documented it in project docs. | Commit `1cc1c66`; [LICENSE](../../LICENSE) |
| Quick Development Security Validation Pass 1 | Added a standard-library security validation runner that skips optional missing tools cleanly. | Commit `387abb8`; [Security validation pass 1](../security/security_validation_pass_1.md) |
| Repository Maintenance Pass 1 | Organized the first canonical management-doc set and compatibility pointers. | Commit `734eba5`; [Repository Maintenance Pass 1](repo_maintenance_pass_1.md) |
| Post-Validation Stabilization Pass 1 | Addressed 39 reported chunking/layout defects with focused layout, source-boundary, date, and phrase-cohesion fixes. | Commit `8203a3e`; [Post-Validation Stabilization Pass 1](../validation/post_validation_stabilization_pass_1.md) |
| Structural Hierarchy Anchor | Added static H1/H2 orientation metadata and defect-report context without full Markdown rendering. | Commit `fc223dd`; [Navigation & Navigability](../features/navigation.md) |
| Drift Recovery Logic | Added breakpoint-traversal lead-in behavior with pause and auto-resume cancellation rules. | Commit `50c2caa`; [Navigation Validation](../validation/navigation_validation.md) |
| Ghost Previous Chunk | Displayed previous chunk context above the active chunk and included it in defect reports. | Commit `50c2caa`; [Navigation & Navigability](../features/navigation.md) |
| Breakpoint Bookmarking Traversal | Added session-only breakpoint toggling and traversal while preserving swipe fallback. | Commit `be2075b`; [Navigation Validation](../validation/navigation_validation.md) |
| Chunker Refinement Pass 2 | Refined observed phrase-boundary issues while preserving deterministic chunking. | Commit `f682a73`; [Chunking Refinement Pass 2](../validation/chunking_refinement_pass_2.md) |

## Earlier Completed Work

- Backend defect reporting.
- Defect report security hardening.
- Chunking Refinement Pass 1.
- Timing-context instrumentation.
- Evidence hygiene, display cleanup, and tokenization cleanup.
- Timing Calibration Pass 1.
- Post-calibration timing validation.
- Post-validation targeted calibration.
- Quote/parenthetical display-state annotation and defect taxonomy preparation.
- Navigation Scaffolding Pass 1.
- JavaScript syntax verification hardening.
- Passive Spatial Anchor implementation.

Earlier entries are intentionally compact. Use the validation and feature docs for detailed evidence when needed.
