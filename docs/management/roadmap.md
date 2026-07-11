# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-029: Density-Aware Dwell-Time Recalibration**
   - State: `IN_IMPLEMENTATION`
   - Owner: Codex
   - Goal: measure the parser density shift and make default `1.0x` timing comfortable through a bounded, inspectable adjustment.
   - Scope: [S-029](s029_density_aware_dwell_time_recalibration.md).

## Next

- Follow the ordered [Prototype Validation and Stabilization Program](prototype_validation_stabilization_program.md). Later passes are not active or authorized for implementation.

## Later

- Provider ablation or dependency reduction when a concrete platform need arises.
- Native/mobile provider evaluation.
- Application-service refinements only if validation exposes a need.
- Investigation of the S-024 rule-based coverage/mapping anomalies.
- Additional management-doc cleanup if the one-human/one-Codex workflow changes.
- Demo/beta readiness cleanup.

## Parked

- Native app, EPUB/PDF import, cloud sync, accounts, analytics, service workers, and deployment infrastructure.
- Frontend framework migration, npm toolchain, and browser automation tooling.
- Full Markdown rendering, heading navigation, and table of contents.
- Permanent universal commitment to spaCy.
- Immediate native packaging.
- Public performance claims.
- Broad expansion of hand-written semantic and grammatical exception families.
- Optimizer retuning without a new experimental slice.

Quote/parenthetical validation is not parked as a standalone queue item. It is folded into S-021 as a display-state clarity check.

Newly observed grammatical or semantic defects should become evaluation cases first. They do not automatically become new production rules while the parser-assisted experiment is pending.
