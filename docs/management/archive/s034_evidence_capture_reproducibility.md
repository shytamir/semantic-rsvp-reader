# S-034 Evidence Capture and Reproducibility

## Status

Completed as `passed` from human-owned evidence commit `eafadbd`. All seven human steps passed, the four synthetic local reports were deleted, and no missing context or impractical protocol step was found.

## Objective

Validate that defect reports and management/evaluation records capture complete, private, reviewable, and reproducible evidence.

## Initiating Reason

The prototype depends on local compressed reports and committed evidence; prior report loss and later integrity work make an end-to-end evidence-capture pass necessary.

## In Scope

- Report panel pause/close/submit flow, category/severity/notes, contextual chunk/sentence/timing/display/navigation/structure/session/layout fields.
- Bounded sanitization, generated filenames, gzip Markdown storage, request limits, encryption warnings, and review/export tooling.
- Comparable exposure protocols, repository-integrity validation, management consistency, registered hashes, and private blind-identity exclusion.

## Codex Preparation

Run defect API/storage/review and integrity checks; prepare synthetic bounded reports and a reproducibility checklist without committing private or generated local reports.

## Human Handoff

Submit and review representative chunking, timing, navigation, and layout reports; confirm context is sufficient and the fixed exposure protocol is practical.

## Permissible Stabilization

Fix only a reproduced capture, sanitization, compression, context, review-tool, or record-consistency defect with focused tests.

## Non-Goals

No accounts, analytics, database, cloud sync, telemetry, private blind material, generalized workflow engine, or experiment reinterpretation.

## Completion Boundary

Capture-to-review and repository-record reproducibility are demonstrated, human context sufficiency is recorded, and narrow defects are stabilized. Do not activate S-035 automatically.
