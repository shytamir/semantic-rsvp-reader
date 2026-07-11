# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-032: Navigation and Interaction**
   - State: `AWAITING_HUMAN_VALIDATION`
   - Owner: Human
   - Scope: [S-032](s032_navigation_interaction.md).
   - Handoff: [fixed navigation and interaction protocol](../validation/navigation_validation.md#s-032-navigation-and-interaction-validation).

## Next

1. **S-033: Mobile Presentation and Accessibility** — `SCHEDULED`; [scope](s033_mobile_presentation_accessibility.md).
2. **S-034: Evidence Capture and Reproducibility** — `SCHEDULED`; [scope](s034_evidence_capture_reproducibility.md).
3. **S-035: Service Surfaces and Fallback** — `SCHEDULED`; [scope](s035_service_surfaces_fallback.md).
4. **S-036: End-to-End Prototype Readiness** — `SCHEDULED`; [scope](s036_end_to_end_prototype_readiness.md).

These slices are ordered but not authorized for implementation until separately activated.

## Post-Stabilization Sequence

After S-036, the approved roadmap destinations are:

1. **S-037: S-024 Coverage and Mapping Anomaly Investigation** — `PLANNED`. Investigate remaining rule-based coverage and evaluation-mapping anomalies as scientific/evaluation debt. This does not authorize automatic parser retuning or promotion.
2. **S-038: Document Ingestion Foundation** — `PLANNED`. Add plain-text and Markdown file import while preserving source metadata and supported structure; clean HTML/article ingestion may be included where it fits naturally. PDF and a full rich-document rendering system are excluded.
3. **S-039: Local Reading Continuity** — `PLANNED`. Preserve local reading position, recent documents, reader preferences, and appropriate session state without accounts, cloud sync, analytics, or a backend database.
4. **S-040: Minimal Browser Regression Coverage** — `PLANNED`. Add a deliberately small smoke suite for text loading, playback, pause/resume, progress seeking, breakpoints, and catastrophic mobile-layout regressions. This does not authorize a frontend-framework or general npm-toolchain migration.
5. **S-041: EPUB and Long-Document Navigation** — `PLANNED`. Add EPUB ingestion after S-038 is stable, with appropriate heading navigation and a lightweight contents view. Full Markdown rendering and PDF are excluded.
6. **S-042: Beta Distribution and External Trial** — `PLANNED`. Prepare a deliberately limited beta or hosted demonstration with clear privacy, limitation, and prototype-status documentation, without accounts, analytics, scaling architecture, or production-grade deployment infrastructure.

These destinations are ordered but have no detailed implementation scopes and are not authorized until separately activated. EPUB therefore precedes beta distribution.

## Later

- Provider ablation or dependency reduction when a concrete platform need arises.
- Native/mobile provider evaluation when native distribution becomes a real objective.
- Application-service refinements only if validation exposes a need.
- Management-document cleanup if the solo human/Codex workflow materially changes.
- PDF ingestion evaluation after S-042 as a distinct research and validation problem covering extraction quality, reading order, columns, headers, footers, captions, and hyphenation.

## Parked

- Native app, cloud sync, accounts, analytics, service workers, and production-grade deployment infrastructure.
- PDF ingestion pending its dedicated post-S-042 evaluation.
- Frontend framework migration, a general npm toolchain, and browser-automation expansion beyond the deliberately small S-040 smoke suite.
- Full Markdown rendering and rich-document rendering.
- Permanent universal commitment to spaCy.
- Immediate native packaging.
- Public performance claims.
- Broad expansion of hand-written semantic and grammatical exception families.
- Optimizer retuning without a new experimental slice.

Quote/parenthetical validation is not parked as a standalone queue item. It is folded into S-021 as a display-state clarity check.

Newly observed grammatical or semantic defects should become evaluation cases first. They do not automatically become new production rules while the parser-assisted experiment is pending.
