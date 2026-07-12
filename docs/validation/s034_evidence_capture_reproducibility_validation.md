# S-034 Evidence Capture and Reproducibility Validation

## Automated Preparation

The committed [S-034 characterization](../../evaluation/evidence_capture/s034_characterization.json) posts four bounded synthetic reports—chunking, timing, navigation, and layout—to a temporary report directory. It verifies generated filenames, readable gzip Markdown, HTML-sensitive-text escaping, required contextual sections, and review-tool ingestion, then deletes the temporary reports. No generated report or private blind material is committed.

Reproduce the record with:

```bash
python scripts/characterize_s034_evidence_capture.py --check
```

Focused tests cover capture validation, sanitization, request limits, contextual completeness, gzip storage, storage-encryption warnings, review filtering/export, repository integrity, registered hashes, management consistency, and private blind-identity exclusion. No defect was reproduced and no runtime stabilization was required.

## Fixed Human Protocol

Use only synthetic observations. Do not enter private text or blind identity material.

1. Start a fresh local reader session and load a project-owned validation sample. Open **Report Defect** during playback and confirm playback pauses. Close the panel and confirm normal reader controls return without submitting.
2. Submit a synthetic `bad_chunk_split` report with severity, notes, and preferred behavior. Confirm the UI reports a saved ID and the generated `.md.gz` file appears under `data/defect_reports/`.
3. Repeat with synthetic reports representing timing (`rushed_dense_chunk`), navigation (`gesture_interference`), and layout (`layout_or_visibility_issue`) context. Do not report an actual defect unless one is reproduced.
4. Run `python scripts/review_defects.py --report-dir data/defect_reports` and confirm all four new reports are readable and filterable.
5. Inspect the four reports and confirm they contain classification, chunk/sentence, timing, display/layout, navigation/breakpoint, structure, nearby context, session summary, and client/viewport information sufficient to reproduce the synthetic observation.
6. Confirm filenames contain generated IDs rather than user text, HTML-sensitive input is escaped, and the application documents or emits the local-storage encryption warning when encryption cannot be confirmed.
7. Run `python scripts/validate_repository_integrity.py` and confirm it passes. Verify `git status --short` does not show the generated reports and no private blind identity or per-case mapping is present.
8. Delete the four synthetic local reports after review. Record `passed`, `partially_passed`, `failed`, or `inconclusive`, plus any missing context or impractical protocol step.

## Human Disposition

Human records `passed` for all 7 steps after deleting the 4 synthetic local reports. No missing context or impractical protocol step detected.
