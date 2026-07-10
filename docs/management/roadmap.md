# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-021: Post-Stabilization Validation Pass**
   - State: `HUMAN_VALIDATION`
   - Owner: human
   - Goal: validate mobile layout, source boundaries, long-form dates, phrase cohesion, and quote/parenthetical display-state clarity under comparable baseline conditions.

## Next

1. **S-022: Evidence-based follow-up from S-021**
   - If S-021 passes, expand focused chunking regression coverage.
   - If S-021 partially passes, fails, or is inconclusive, summarize the new defects and run a targeted stabilization follow-up.
2. **S-023: Post-navigation usability validation**
   - Validate passive anchor, seek, breakpoints, ghost chunk, drift recovery, and structural label without letting navigation mask chunking defects.
3. **S-024: Demo/beta readiness cleanup**
   - Tighten documentation, validation workflow, and small ergonomics after core RSVP and navigability validation.

## Later

- Broader validation-corpus growth after the current stabilization gate is resolved.
- Additional management-doc cleanup if the one-human/one-Codex workflow changes.
- Optional CI or release hygiene only when the repo already has a clear need for it.

## Parked

- Native app, EPUB/PDF import, cloud sync, accounts, analytics, service workers, and deployment infrastructure.
- Frontend framework migration, npm toolchain, and browser automation tooling.
- Full Markdown rendering, heading navigation, and table of contents.
- Public performance claims.

Quote/parenthetical validation is not parked as a standalone queue item. It is folded into S-021 as a display-state clarity check.
