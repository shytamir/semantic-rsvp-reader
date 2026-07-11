# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-026: Provisional parser-assisted prototype integration**
   - State: `READY_FOR_IMPLEMENTATION`
   - Owner: Codex
   - Goal: integrate the frozen parser-assisted behavior as the current Flask prototype default while preserving rule-based fallback.
   - Constraint: do not retune S-023 optimizer behavior, change timing/navigation semantics, or make a native/mobile provider decision.

## Next

1. **S-027: Post-navigation usability validation**
   - Resume navigation usability validation after the parser-assisted experiment sequence no longer risks masking chunking comparison results.

## Later

- Demo/beta readiness cleanup.
- Provider ablation or dependency reduction when a concrete platform need arises.
- Native/mobile provider evaluation.
- Application-service refinements only if validation exposes a need.
- Investigation of the S-024 rule-based coverage/mapping anomalies.
- Additional management-doc cleanup if the one-human/one-Codex workflow changes.
- Optional CI or release hygiene only when the repo already has a clear need for it.

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
