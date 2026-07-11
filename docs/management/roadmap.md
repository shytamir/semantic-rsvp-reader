# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-026: Provisional parser-assisted prototype integration validation**
   - State: `AWAITING_HUMAN_VALIDATION`
   - Owner: Human
   - Goal: smoke-test the integrated parser-assisted Flask prototype default on representative phone-browser reading flows.
   - Constraint: validate the integrated frozen behavior without retuning S-023 optimizer behavior, changing timing/navigation semantics, or making a native/mobile provider decision.

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
