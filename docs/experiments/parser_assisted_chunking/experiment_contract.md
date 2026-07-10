# Experiment Contract

## Hypothesis

A parser-assisted global boundary optimizer will reduce harmful grammatical and semantic splits on held-out text without violating RSVP display constraints or materially increasing over-clumping and operational cost.

## Null Outcome

If the experimental system does not demonstrate a clear held-out advantage, the existing rule-based chunker remains the production default and the experiment may be abandoned or revised.

## Baseline

The baseline is the production implementation at commit `8b50a3049bb5d92a304a03527385c519194ce8da`.

Observed pipeline:

1. `normalize_text(raw_text)`
2. `split_sentences(normalized_text)`
3. `RuleBasedChunker(max_chars=32, max_content_words=2).chunk_sentence(sentence)`
4. `schedule_text(raw_text)` attaches timing, navigation, display-state, and structure metadata.

Timing defaults are `base_beat_ms=400`, `min_duration_ms=150`, `max_duration_ms=1200`, and `sentence_pause_ms=180`.

## Experiment Permission

This contract permits a future optional parser-assisted spike only. It does not authorize replacing or extending the production chunker.

Future experimental dependencies must be isolated at first. Library and model versions must be pinned before any comparison run is treated as evidence.

## Production Freeze Rule

Newly observed grammatical or semantic defects become evaluation cases first. They do not automatically become new production rules while the parser-assisted experiment is pending.

Small safety fixes and clear regressions may still be considered separately, but broad expansion of hand-written semantic and grammatical exception families is frozen during the experiment.

## Hard Constraints

- Exact source-text coverage.
- Source ordering.
- No dropped or duplicated text.
- Safe token-to-character alignment.
- Required document-structure boundaries.
- Maximum display width, except explicitly documented unsplittable-token exceptions.
- Existing schedule contract unless a separate approved slice changes it.

## Soft Evidence

- Named-entity spans.
- Date, number, and money spans.
- Noun-phrase spans.
- Auxiliary/main-verb relationships.
- Negation/predicate relationships.
- Phrasal-verb particles.
- Strong dependency relationships.
- Clause boundaries.
- Punctuation boundaries.
- Visual underfilling and over-clumping signals.

Future weights are intentionally unspecified in this pass.

## Promotion Gate

The experimental implementation cannot become the production default merely because its architecture appears cleaner.

Promotion requires:

1. No regression in exact source coverage.
2. No regression in structural-boundary compliance.
3. No unacceptable maximum-width regressions.
4. A clear reduction in harmful splits on held-out material.
5. No material increase in over-clumping.
6. Acceptable latency and installation cost.
7. Acceptable alignment and fallback rates.
8. A meaningful blinded human-preference advantage.
9. Preservation of the existing timing and schedule contract.
10. A documented production fallback.

Numerical thresholds are a later human decision after baseline metrics and annotations exist.

## Benchmark-construction Rules

- Do not define metrics using outputs that only one algorithm can produce.
- Do not assume dependency parsing will always be available.
- Do not encode expected spaCy labels into the gold schema.
- Do not use model token indexes as canonical references.
- Do not select only cases that favor parser-assisted techniques.
- Include simple prose where the current baseline is already strong.
- Include cases testing over-clumping as well as harmful splitting.
- Preserve known baseline successes, not only failures.
