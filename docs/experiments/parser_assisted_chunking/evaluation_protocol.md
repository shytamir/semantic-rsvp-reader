# Evaluation Protocol

## Corpus Categories

### Development Corpus

Visible during future implementation. Use it for debugging, feature design, and weight tuning. It may include known defect examples and existing regression cases. It does not measure generalization.

Representative cases include names, dates, numbers, auxiliary verbs, negation, phrasal verbs, noun phrases, clause boundaries, punctuation, titles/bylines/source lines, over-clumping, width pressure, and source-boundary defects.

### Frozen Regression Corpus

Visible during development, but frozen before parser implementation begins. It preserves existing known behavior, previously reported defects, and current regression fixtures so recurrence and regressions can be measured.

### Frozen Generalization Corpus

Committed source text visible to Codex, but not used to create current semantic-rule families. It is frozen before implementation and has no committed gold boundary annotations. Human annotations for this set should remain unavailable during tuning.

This is not a perfectly blind set because the inputs are in the repository. Treat it as a frozen generalization set.

### Human-held Blind Challenge Set

The strongest available check against overfitting. Its source text and annotations remain outside the active repository and outside Codex prompts until tuning is declared complete.

## Metrics

Raw defect counts must always be reported with a denominator: per sentence, per candidate boundary, per fixed corpus, or per 1,000 words.

### Hard Compliance

- Maximum-width violations per fixed corpus.
- Required structural-boundary violations per required structural boundary.
- Dropped or duplicated source text per case.
- Unsafe alignment failures per case.
- Fallback rate: `fallback_cases / evaluated_cases`.

### Linguistic Quality

- Forbidden-boundary violation rate: `violated_forbidden_boundaries / annotated_forbidden_boundaries`.
- Protected-span violation rate: `split_protected_spans / annotated_protected_spans`.
- Required-boundary recall: `satisfied_required_boundaries / annotated_required_boundaries`.
- Preferred-boundary agreement: `satisfied_preferred_boundaries / annotated_preferred_boundaries`.
- Recurrence of known defects by case and defect class.
- New regression count by case and defect class.
- Over-clumping rate: `overclumped_chunks / evaluated_chunks` or `overclumped_cases / evaluated_cases`.

### Distributional Behavior

- Mean and median words per chunk.
- Character-width distribution.
- Single-word chunk rate.
- Long-chunk rate.
- Chunks per sentence and chunks per 1,000 words.

### Operational Cost

- Processing latency per case and per 1,000 characters.
- Parser initialization cost, once implemented.
- Dependency and model footprint, once implemented.
- Percentage of cases using fallback.

### Human A/B Comparison

Later comparison should:

- Hide implementation identity.
- Randomize A/B assignment.
- Permit `A`, `B`, `equivalent`, and `both poor`.
- Record confidence.
- Measure preference by sentence and by full passage.
- Keep known-defect, generalization, and blind-set results separate.

## Contamination Rules

- Development cases and annotations may be inspected during implementation.
- Regression cases may be inspected but cannot demonstrate generalization.
- Frozen generalization inputs may be visible, but annotations must remain unavailable during tuning.
- Human-held blind source text and annotations must remain unavailable until tuning is declared complete.
- Newly discovered held-out defects must not be moved into development before the comparison is recorded.
- Accidental exposure must be recorded and affected cases reclassified.
- Evaluation reports must identify which sets were visible during implementation.
