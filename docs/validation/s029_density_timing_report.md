# S-029 Density and Timing Report

## Measurement

`scripts/measure_s029_density_timing.py` measures all 22 project-owned visible corpus cases under both chunkers on identical normalized text. Machine-readable records preserve per-case chunk counts, word and content-word density, character-length distributions, hint distributions, total duration, milliseconds per word/content word, and clamp incidence:

- [Before adjustment](../../evaluation/timing/s029_density_timing_before.json)
- [After adjustment](../../evaluation/timing/s029_density_timing_after.json)

Aggregate baseline results show that parser-assisted output uses 74 chunks versus 124 rule-based chunks (-40.3%). It contains 3.662 versus 2.185 words per chunk and 2.541 versus 1.516 content words per chunk, both +67.6%. The human “nearly doubled” description was directionally useful but is not the measured result.

Before recalibration, parser-assisted scheduling totaled 50,750 ms (187.269 ms/word), versus 69,440 ms (256.236 ms/word) for rule-based output: parser output was effectively 36.8% faster. After recalibration, parser scheduling totals 59,280 ms (218.745 ms/word), a 16.8% increase. Rule-based scheduling totals 72,640 ms (268.044 ms/word), a 4.6% increase. The remaining parser effective-rate difference is 22.5%. Neither mode hits the minimum or maximum clamp on this corpus.

## Deterministic Adjustment

For non-light, non-punctuation chunks, `density_dwell_bonus_ms` adds 50 ms per word beyond two plus 20 ms per content word beyond one, capped at 240 ms before the existing overall duration clamp. Existing hint multipliers, length, dense-settling, lexical dense, punctuation, sentence-final, quote, and strong-punctuation components retain their relative treatment. Light and punctuation chunks receive no density bonus.

## Human Validation Protocol

Use the current parser-default build on the same device/browser. Set speed to `1.0x`, disable adaptation, and reset session state before each passage. Read these project-owned cases in order without inspecting timing diagnostics during the pass:

1. Dense technical/nonfiction: `dev-source-0005`, `reg-dense-0002`, and `gen-synthetic-0004`.
2. Boundary-rich technical prose: `dev-quote-0007` and `gen-synthetic-0006`.
3. Lighter narrative: `gen-public-0001` and `gen-public-0002`.

Record one result for each criterion:

- dense chunks are understandable without routine rewinds;
- normal chunks do not feel systematically rushed;
- light and punctuation chunks do not feel sticky;
- sentence and quote boundaries retain natural rhythm;
- `1.0x` feels approximately as manageable as the prior build at `0.85x`;
- no timing change masks a chunking defect.

If useful, repeat one dense and one light passage at `0.85x` only after completing the fixed `1.0x` pass. Report `passed`, `partially_passed`, `failed`, or `inconclusive`, plus case IDs and any rewind/sticky/boundary observations. Do not treat a chunking defect as a timing success.

## Calibration Risk

The automated corpus supported the bounded adjustment but could not establish human comfort. Subsequent human validation passed all six corpus-sample validations and reported that default `1.0x` is as manageable as the prior build at `0.85x`; no acceptance-blocking timing issue was reported. Parser output remains faster per word than rule-based output, and clamp behavior is covered synthetically rather than exercised by the 22-case measurement corpus.
