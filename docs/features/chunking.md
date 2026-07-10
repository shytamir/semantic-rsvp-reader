# Chunking

## Purpose

The chunker converts normalized sentences into short semantic units suitable for RSVP playback. It is deterministic, inspectable, and implemented in pure Python.

## Current Behavior

- Tokenizes words, punctuation, honorifics, common initialisms, contractions, and possessives.
- Preserves known observed entities and compact phrases.
- Keeps long-form dates coherent.
- Respects source/title/byline/date boundaries prepared by segmentation.
- Applies conservative repairs for selected underdense and overlong observed cases.

## Constraints

- No spaCy, transformers, or ML parser.
- No broad document parser.
- No global chunk-size retuning without validation evidence.
- Mobile width constraints matter when preserving names, dates, and phrases.
- While the parser-assisted experiment is pending, newly observed grammatical or semantic defects should become evaluation cases first rather than automatic new production rules.

## Experimental Direction

An optional parser-assisted experiment is frozen in [Parser-Assisted Chunking Experiment](../experiments/parser_assisted_chunking/README.md). It does not change the production chunker. The rule-based implementation remains the default, fallback, and regression baseline.

## Validation Notes

Recent validation-driven refinements are documented in:

- [Chunking Refinement Pass 1](../validation/chunking_refinement_pass_1.md)
- [Chunking Refinement Pass 2](../validation/chunking_refinement_pass_2.md)
- [Post-Validation Stabilization Pass 1](../validation/post_validation_stabilization_pass_1.md)

## Known Limitations

- Rules can overfit observed text.
- Name/date preservation can create dense chunks.
- Source-boundary preservation can add pauses around metadata lines.
