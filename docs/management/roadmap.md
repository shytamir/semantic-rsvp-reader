# Roadmap

This roadmap is the priority-order view. [STATUS](STATUS.md) is the authority for the current active slice.

## Now

1. **S-022: Landscape Ghost-Chunk Collision Stabilization**
   - State: `HUMAN_VALIDATION`
   - Owner: human
   - Goal: validate the targeted phone landscape layout correction for GitHub issue #1.

## Next

1. **S-023: Parser-assisted chunking spike**
   - Implement an isolated experimental parser-assisted path using the frozen design in [Parser-Assisted Chunking Experiment](../experiments/parser_assisted_chunking/README.md).
   - Keep the rule-based chunker as the production default and fallback.
2. **S-024: Baseline versus experiment comparison**
   - Compare rule-based and parser-assisted outputs using frozen regression, frozen generalization, and human-held blind challenge material when available.
3. **S-025: Post-experiment disposition**
   - Decide whether to abandon, revise, or consider promoting the parser-assisted approach after held-out evaluation.

## Later

- Post-navigation usability validation.
- Demo/beta readiness cleanup.
- Consider production adoption only after held-out evaluation and the documented promotion gate.
- Additional management-doc cleanup if the one-human/one-Codex workflow changes.
- Optional CI or release hygiene only when the repo already has a clear need for it.

## Parked

- Native app, EPUB/PDF import, cloud sync, accounts, analytics, service workers, and deployment infrastructure.
- Frontend framework migration, npm toolchain, and browser automation tooling.
- Full Markdown rendering, heading navigation, and table of contents.
- Public performance claims.
- Broad expansion of hand-written semantic and grammatical exception families while the parser-assisted experiment is pending.

Quote/parenthetical validation is not parked as a standalone queue item. It is folded into S-021 as a display-state clarity check.

Newly observed grammatical or semantic defects should become evaluation cases first. They do not automatically become new production rules while the parser-assisted experiment is pending.
