# Post-Validation Targeted Calibration

Date: 2026-07-10

## Source Report

This pass used `docs/validation/observed_timing_defects_third_pass.md`, the post-calibration timing-context report headed `# Observed Defects Review - timing context only`.

## Evidence Summary

The third-pass report contained 13 timing-context reports:

- `rushed_dense_chunk`: 6
- `punctuation_rhythm_issue`: 4
- `orphan_function_word`: 3

The timing evidence no longer supported a broad dense-duration increase. The repeated timing signal was narrower: extreme semantic density, dense proper nouns, long abstract words, semicolon/comma emphasis, and quote-adjacent rhythm.

## Timing Defects Addressed

- Extreme semantic density in chunks such as `a parenthetical may quietly`.
- Dense proper-noun chunks such as `Department of Transportation`.
- Long abstract chunks such as `the duration is mathematically`.
- Semicolon/colon settling in chunks such as `may rescue it;`.
- Comma-list emphasis in chunks such as `failures,`.
- Quote-boundary rhythm.

## Chunking/Text-Cleanliness Defects Separated

The report also included defects that should not drive timing formulas directly:

- orphaned `as`;
- modal/auxiliary attachment around `should`;
- missing space after a closing quote, as in `intuition"cannot.`;
- any remaining chunking or source-text cleanliness issue mislabeled as timing.

## Timing Rules Changed

- Added a bounded `60ms` bonus for extreme semantic density.
- Increased quote-boundary settling from `60ms` to `70ms`.
- Increased colon/semicolon settling from `40ms` to `70ms`.
- Added a narrow `20ms` comma-list emphasis bonus for single long comma-ended items.

Ordinary dense chunks do not receive the new extreme-density bonus.

## Chunking/Normalization Rules Changed

- Short `as ...` phrases are preserved when they fit, reducing standalone `as` chunks.
- `should` now splits before the modal only when it would otherwise trail an already dense two-content-word chunk.
- Normalization inserts a space after a closing quote followed immediately by a word, avoiding joins such as `intuition"cannot`.

## Before/After Examples

| Case | Before | After | Notes |
|---|---:|---:|---|
| `a parenthetical may quietly` | 690ms | 750ms | extreme semantic density bonus |
| `Department of Transportation` | 690ms | 750ms | dense proper-noun bonus |
| `may rescue it;` | 480ms | 510ms | stronger semicolon settling |
| `failures,` | 440ms | 460ms | narrow comma-list emphasis |
| `intuition"cannot proceed` | joined text | `intuition" cannot proceed` | normalization cleanup |

## Known Remaining Issues

- Extreme-density detection is intentionally heuristic and may miss some difficult chunks.
- Comma-list emphasis is narrow to avoid overpausing ordinary comma chunks.
- Some `should` cases may still be better solved by future chunking refinements.
- Reports collected with adaptation enabled can still obscure baseline timing behavior.

## Next Validation Recommendation

Run a focused post-targeted-calibration validation pass at `1.0x`, `1.15x`, and optionally `1.3x`, with adaptation disabled for at least one pass. Target 8-12 clean reports before making another timing formula change.
