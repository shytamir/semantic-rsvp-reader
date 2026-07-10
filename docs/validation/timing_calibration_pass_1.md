# Timing Calibration Pass 1

Date: 2026-07-10

## Source Report

Calibration used `docs/validation/observed_timing_defects_second_pass.md`, the timing-context-only second-pass export headed `# Observed Defects Review - timing context only`.

Timing evidence categories used:

- `rushed_dense_chunk`
- `punctuation_rhythm_issue`
- the single `overpaused_light_chunk` only as a guardrail against globally slowing light chunks

Historical noise excluded from timing formula decisions:

- end-of-line hyphenation and display wrapping
- `a.m.` / `p.m.` splitting
- `U.S.` / `E.U.` tokenization issues
- `whether leaving would` connector/modal chunking
- reports without Timing Context
- chunking defects mislabeled as timing

## Evidence Summary

Dense chunks were the dominant timing complaint. The clearest clean reports clustered around effective dwell of roughly 470-504ms at 1.15x. Later reports also pointed to extra cognitive load from long or reflective content words, closing/opening quote boundaries, short priming punctuation chunks, and dense sentence-ending chunks.

## Timing Rules Changed

- Dense multiplier increased from `1.25` to `1.30`.
- Dense chunks receive a fixed `40ms` settling bonus.
- Extra-dense dense chunks receive a bounded `50ms` bonus when they include a long content word or a small set of reflective/abstract words.
- Dense sentence-ending chunks receive an additional `40ms` settling bonus beyond the existing sentence pause.
- Quote-boundary chunks receive a `60ms` bonus.
- Colon/semicolon chunks receive a `40ms` bonus.
- Opening quote comma priming chunks receive an additional `30ms` bonus.

The existing min/max clamps still apply.

## Before/After Examples

| Chunk | Evidence | Before | After | Effect at 1.15x |
|---|---|---:|---:|---:|
| `pages can punish` | Dense chunk felt rushed at 470ms effective | 540ms | 600ms | 470ms -> 522ms |
| `be allowed to hesitate` | Dense reflective verb needed more time | 580ms | 690ms | 504ms -> 600ms |
| `"however,` | Opening quote/comma priming chunk felt too abrupt | 240ms | 330ms | 209ms -> 287ms |
| `and return a response.` | Dense sentence-ending chunk needed settling time | 760ms | 860ms | 661ms -> 748ms |

## Expected Effect

At 1.0x, dense chunks should feel slightly calmer without turning every chunk into a pause. At 1.15x, representative dense chunks should be less likely to land in the 470-504ms effective-duration band that dominated the clean report.

Light and normal chunks are not globally slowed. Comma-only light chunks do not receive new punctuation bonuses.

## Tests Added

- dense chunks remain slower than normal chunks
- representative dense chunks clear a conservative 1.15x effective dwell threshold
- extra-dense dense chunks receive a bounded bonus
- sentence-ending dense chunks receive added settling time
- quote-boundary chunks receive bounded dwell
- colon/semicolon chunks receive bounded dwell
- light comma chunks are not overpaused
- timing explanation output remains deterministic and inspectable

## Known Remaining Timing Issues

- The extra-dense heuristic is intentionally simple and may miss some cognitively dense phrases.
- The calibration is based on a small personal validation sample and may need another pass.
- Adaptation can mask timing defects, so at least one validation pass should disable adaptation.
- Chunking defects can still feel like timing defects and should continue to be classified separately.

## Next Validation Pass

Run a post-calibration timing validation pass focused on dense chunks at 1.0x and 1.15x. Keep adaptation disabled for at least one pass, report only genuine timing defects, and collect 8-12 clean reports before deciding whether a follow-up calibration is justified.
