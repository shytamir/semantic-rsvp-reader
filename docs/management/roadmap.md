# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-028: Compact CI and Evidence Integrity**
   - State: `READY_FOR_IMPLEMENTATION`
   - Owner: Codex
   - Goal: protect core/fallback operation, parser-default operation, management consistency, and experimental evidence with a compact automation layer.
   - Scope: [S-028 planning document](s028_compact_ci_evidence_integrity.md).
   - Included maintenance: open GitHub issue #3.

## Next

- No separately scheduled slice. Complete S-028 before selecting another slice.

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
