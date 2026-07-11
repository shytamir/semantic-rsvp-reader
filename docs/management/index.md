# Management Docs

These files are the project-management source of truth for the solo human/Codex workflow.

## Canonical Hierarchy

1. [STATUS](STATUS.md): the sole authority for the current operational slice.
2. [Roadmap](roadmap.md): ordered Now / Next / Later / Parked priorities.
3. [HISTORY](HISTORY.md): compact completed-slice history.
4. [DECISIONS](DECISIONS.md): durable ADR-lite project decisions.
5. [TODO](TODO.md): parked and unscheduled inventory only.

## Active Slice

- S-030 is the sole active slice, with state `AWAITING_HUMAN_VALIDATION` and owner Human.
- The [Prototype Validation and Stabilization Program](prototype_validation_stabilization_program.md) schedules S-030 through S-036 in strict order.
- Scope documents: [S-030](s030_semantic_output_structural_integrity.md), [S-031](s031_playback_adaptation.md), [S-032](s032_navigation_interaction.md), [S-033](s033_mobile_presentation_accessibility.md), [S-034](s034_evidence_capture_reproducibility.md), [S-035](s035_service_surfaces_fallback.md), [S-036](s036_end_to_end_prototype_readiness.md).
- S-031 through S-036 are scheduled only and are not authorized for implementation.

Compatibility pointers:

- [Root TODO](../../TODO.md): short pointer to this hierarchy.
- [Legacy project status path](../project_status.md): compatibility stub pointing here.
- [Repository Maintenance Pass 1](repo_maintenance_pass_1.md): historical record of the first docs cleanup.

## Human And Codex Roles

Human owner:

- Product owner.
- Usability tester.
- Evidence author.
- Priority authority.
- Sole acceptance authority for qualitative gates.

Codex:

- Implementer.
- Automated-test author.
- Mechanical documentation maintainer.
- Repo hygiene executor.

Codex must not:

- Declare a qualitative gate passed without human evidence.
- Promote its own work into the next slice.
- Interpret low raw defect counts as success without comparable exposure.
- Expand scope beyond the active slice.
- Rewrite the meaning of human evidence.

## Repository Sync Protocol

1. Fetch and confirm the expected starting commit before implementation.
2. Avoid concurrent manual uploads while an implementation pass is active.
3. Rerun relevant checks and inspect the complete diff before commit.
4. Rebase or fast-forward from remote before push.
5. Never resolve an unexpected conflict by guessing.
6. Stop and report if the remote changed in a way that makes the next action unsafe.

## Validation Terms

Baseline validation uses the same device/browser where practical, a fixed recorded speed, adaptation disabled, a fixed corpus subset, predetermined exposure completed even when few defects appear, and comparable in-app defect reporting.

Exploratory validation may use natural speed changes, adaptation, additional texts, and free-form observations. Label it exploratory so it is not mistaken for comparable baseline evidence.

Use severity-weighted defects per fixed sample, recurrence of fixed defects, new regressions, session-breaking defects, and a human gate result: `passed`, `partially_passed`, `failed`, or `inconclusive`.
