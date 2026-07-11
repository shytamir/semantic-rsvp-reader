# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-030: Semantic Output and Structural Integrity**
   - State: `AWAITING_HUMAN_VALIDATION`
   - Owner: Human
   - Scope: [S-030](s030_semantic_output_structural_integrity.md).
   - Handoff: [S-030 semantic/structural validation](../validation/s030_semantic_structural_validation.md).

## Next

1. **S-031: Playback and Adaptation** — `SCHEDULED`; [scope](s031_playback_adaptation.md).
2. **S-032: Navigation and Interaction** — `SCHEDULED`; [scope](s032_navigation_interaction.md).
3. **S-033: Mobile Presentation and Accessibility** — `SCHEDULED`; [scope](s033_mobile_presentation_accessibility.md).
4. **S-034: Evidence Capture and Reproducibility** — `SCHEDULED`; [scope](s034_evidence_capture_reproducibility.md).
5. **S-035: Service Surfaces and Fallback** — `SCHEDULED`; [scope](s035_service_surfaces_fallback.md).
6. **S-036: End-to-End Prototype Readiness** — `SCHEDULED`; [scope](s036_end_to_end_prototype_readiness.md).

These slices are ordered but not authorized for implementation until separately activated.

## Later

- Provider ablation or dependency reduction when a concrete platform need arises.
- Native/mobile provider evaluation.
- Application-service refinements only if validation exposes a need.
- Investigation of the S-024 rule-based coverage/mapping anomalies.
- Additional management-doc cleanup if the one-human/one-Codex workflow changes.

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
