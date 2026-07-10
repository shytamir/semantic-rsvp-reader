# Annotation Guide

Use character offsets in the normalized source string. Do not use spaCy token indexes, current-chunker token indexes, or visual line wrapping.

Evaluate text as RSVP display units: short sequential chunks shown in one place over time.

## Boundary Types

- `required`: a boundary is structurally or semantically necessary.
- `forbidden`: a boundary is clearly harmful.
- `preferred`: a boundary is better than nearby alternatives but not mandatory.
- `acceptable`: a boundary is neutral and should not be penalized.
- `required_structural`: a boundary required by document structure.

Unannotated boundaries are not automatically wrong. More than one complete segmentation may be acceptable.

## Protected Spans

Use protected spans for text that should normally stay together, such as:

- Names and named entities.
- Dates, numbers, and monetary expressions.
- Compact noun phrases.
- Auxiliary plus main verb.
- Negation plus predicate.
- Phrasal verbs.
- Source/title/byline/date lines.

Protected spans are soft unless paired with required or forbidden boundaries.

## Harmful Splits

Mark a forbidden boundary when the split damages comprehension, recognition, or rhythm enough that it should be penalized.

Common examples:

- `not` separated from what it negates.
- `built` separated from `up`.
- `July 4,` separated from `2026`.
- A title separated from the name it identifies.
- A preposition stranded from its object.

## Over-clumping

Annotate over-clumping when a chunk is too dense, too wide, or combines ideas that should arrive separately. Use rationale notes rather than forcing one perfect replacement segmentation.

## Punctuation

Punctuation is evidence, not an automatic answer. Strong punctuation often supports a boundary; commas may be a light rhythm cue or simply part of a date, list, title, or quotation.

## Ambiguity

When two segmentations both feel acceptable, mark both with acceptable or preferred boundaries and record uncertainty. Do not convert uncertainty into a fake gold answer.

## Adjudication

If a case is revisited later, record:

- Original annotator ID.
- Adjudicator ID.
- Annotation version.
- What changed.
- Why it changed.
- Whether implementation exposure may have influenced the revision.

## Blind Material

Keep blind-set source text and annotations outside the active repository and outside future Codex prompts until the implementation is declared ready for evaluation.

## Worked Synthetic Example

Normalized text:

```text
Dr. Mira Patel did not back down.
```

Character offsets:

```text
0 D
4 M
15 d
19 n
23 b
28 d
33 .
```

Possible annotations:

```json
{
  "case_id": "example-negation",
  "annotation_version": "0.1",
  "annotator_id": "human-1",
  "boundaries": [
    {"offset": 15, "type": "preferred", "rationale": "Name/title can stand apart from predicate."},
    {"offset": 23, "type": "forbidden", "rationale": "Separates negation from predicate."}
  ],
  "protected_spans": [
    {"start": 0, "end": 14, "label": "person_title_name", "rationale": "Title and name should normally stay recognizable."},
    {"start": 19, "end": 32, "label": "negated_phrasal_verb", "rationale": "Negation and phrasal verb belong together."}
  ],
  "whole_sentence_segmentations": [
    ["Dr. Mira Patel", "did not back down."]
  ],
  "adjudication_status": "draft"
}
```
