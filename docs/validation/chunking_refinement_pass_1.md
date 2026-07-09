# Chunking Refinement Pass 1

Date: 2026-07-10

Source: `docs/validation/observed_defects_first_pass.md`

## Top Recurring Chunking Issues

1. Modifier-head units were split awkwardly, especially `a/an` + modifier + noun phrases and short direct-object groupings.
2. Verb support structures were separated from the verb they govern, especially infinitives, modal-negation chains, and gerund/auxiliary neighbors.
3. Connectors and punctuation attached to the wrong side of a thought, especially `and`, `or`, `therefore`, quotes, colons, and semicolons.

## Rules Added or Changed

- Added light support words for modal verbs, negation, quantifiers, and transition terms so they do not count as dense content by default.
- Preserved compact `a/an` + modifier + noun units when they fit existing constraints.
- Split before clear boundary connectors after meaningful content, so connectors do not become tails of the previous idea.
- Allowed `or` to stand alone before `a/an` modifier-noun phrases when that preserves the denser phrase.
- Split before infinitive `to` when followed by an auxiliary such as `be`, preserving chunks like `to be noticed`.
- Split before modal verbs when followed by `not`, then preserved compact modal-negation-verb chains such as `may not know`.
- Improved quote handling so opening quotes attach to the enclosed phrase and closing quotes attach to the phrase end.

## Before and After Examples

Observed sentence:

```text
This is why a paragraph can feel easy when read in a quiet room and nearly impossible on a train.
```

Before:

```text
a quiet | room and nearly
```

After:

```text
a quiet room | and nearly
```

Observed sentence:

```text
If normalization removes too much punctuation, the segmenter may not know where the writer changed direction.
```

Before:

```text
removes too | much punctuation, | the segmenter | may not | know where the
```

After:

```text
removes | too much punctuation, | the segmenter | may not know | where the writer
```

Observed sentence:

```text
A reading tool therefore has to respect two different forms of effort.
```

Before:

```text
A reading | tool therefore has | to respect
```

After:

```text
A reading tool | therefore has to respect
```

Observed sentence:

```text
A phrase such as "not because the evidence is weak, but because the explanation is incomplete" asks the reader.
```

Before:

```text
such as " | not because the | ... | is incomplete " | asks the reader
```

After:

```text
as | "not because the evidence | ... | is incomplete" | asks the reader.
```

## Tests Added

Added `tests/test_chunking_refinement_observed.py` with observed-regression coverage for:

- `a quiet room`
- `A reading tool therefore`
- `asking to be noticed`
- `too much punctuation`
- `may not know`
- `not begin`
- opening and closing quote attachment
- `or` before `a dense definition`
- colon/semicolon boundaries

Existing chunking golden tests remain in `tests/test_rule_based_chunker.py`.

## Known Remaining Chunking Issues

- This is still a deterministic rule-based chunker, not a parser; it cannot reliably distinguish every adjective, noun, and verb role.
- Definite article phrases with `the` are not broadly preserved as modifier-head units yet because the first pass avoids over-clumping common phrases like `the system learns`.
- Some verb/direct-object cases remain heuristic and may need a later pass informed by more reports.
- Quote handling is intentionally simple and may not cover nested quotes or unusual typography.
- Timing defects are deferred to a later timing calibration pass.
