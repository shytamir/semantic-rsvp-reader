# Timing Defect Collection

This guide is for collecting timing and rhythm evidence after Chunking Refinement Pass 1. Do not use this pass to request chunking fixes unless the chunk itself is otherwise acceptable and the remaining discomfort is about dwell time or rhythm.

Reports without a `## Timing Context` section should not drive timing calibration. They can remain useful for chunking or UX review, but they do not include the base/effective duration evidence needed for calibration.

## Timing-Focused Defect Categories

- `rushed_dense_chunk`
- `overpaused_light_chunk`
- `punctuation_rhythm_issue`
- `fatigue_or_discomfort`

## What to Report

Use timing categories for issues like:

- This dense chunk disappeared too quickly.
- This light chunk lingered too long.
- The semicolon pause felt too short.
- The comma rhythm felt choppy.
- The sentence-ending pause felt too long.
- The rhythm felt tiring even when the chunks were semantically acceptable.

Each in-app defect report now captures timing evidence:

- base schedule duration
- effective duration after playback speed
- playback speed
- syntactic hint
- content word count
- character length
- quote state and quote boundary
- parenthetical state and depth
- nearby previous/next chunk timing
- session elapsed time and average effective duration
- recent adaptation reason/direction when available

## What Not to Report as Timing

If the chunk itself is badly split, classify it as chunking first. For example, a rushed feeling caused by `a quiet | room` or `may not | know` is still primarily a chunking defect. Timing calibration should focus on chunks that are basically well-formed but feel too fast, too slow, or rhythmically wrong.

If the chunk is hard to read because the browser visibly wraps, clips, hyphenates, or splits a word, classify it as `layout_or_visibility_issue`, not timing. Layout/hyphenation artifacts should be fixed before those reports are interpreted as timing failures.

If the issue is tokenization or segmentation noise, such as `a.m.` becoming a separate punctuation-like chunk, fix that before timing calibration. Dense-chunk timing should be retested after display and tokenization cleanup.

If the issue is source/title/byline/date structure being flattened into prose, classify it as `source_boundary_flattening` or `date_split`, not timing. If the issue is a split phrasal verb, qualifier pair, coordinated phrase, or noun-preposition phrase, use `phrasal_verb_split`, `qualifier_pair_split`, `coordinated_phrase_split`, or `noun_preposition_split` before interpreting the discomfort as a duration problem.

If the issue is that a quote or parenthetical aside is visually hard to track, classify it as `quote_state_confusion` or `parenthetical_state_confusion`, not timing. Use `punctuation_rhythm_issue` for quote-adjacent punctuation only when the visual quote/parenthetical state is already clear and the remaining problem is dwell, pause, or rhythm.

Navigation metadata is now available for future orientation and recovery features, but active navigability behavior is not enabled yet. Do not report progress bar, seeking, bookmark traversal, or drift recovery defects until those features are intentionally activated.

## Suggested Timing Validation Pass

1. Load a validation sample after chunking refinement.
2. Read at default speed.
3. Keep adaptation enabled for one pass, disabled for another if useful.
4. Report only timing/rhythm discomfort.
5. Submit 8-12 timing defects.
6. Use the review utility to aggregate reports.

## Post-Calibration Timing Validation Pass

Use this protocol after Timing Calibration Pass 1:

1. Load a validation sample with dense prose.
2. Test at `1.0x`.
3. Test at `1.15x`.
4. Keep adaptation disabled for at least one pass to isolate backend timing.
5. Report only timing defects.
6. Classify layout, tokenization, and chunking defects separately.
7. Target 8-12 clean timing reports.
8. Focus on dense chunks, punctuation/quote rhythm, and extra-dense semantic chunks.
9. Use `python scripts/review_defects.py --timing-only` to exclude older/no-context reports before reviewing results.

## Post-Targeted-Calibration Validation Pass

Use this protocol after the post-validation targeted calibration pass:

1. Test at `1.0x`.
2. Test at `1.15x`.
3. Optionally test at `1.3x`.
4. Disable adaptation for at least one pass.
5. Focus on extreme semantic density.
6. Focus on punctuation/quote rhythm.
7. Focus on dense proper nouns.
8. Focus on modal-heavy dense chunks.
9. Classify remaining `as`, `should`, or quote-spacing problems as chunking/normalization if they recur.
10. Target 8-12 clean timing reports before another timing formula change.

## Review Utility

Print all reports:

```bash
python scripts/review_defects.py
```

Filter timing categories:

```bash
python scripts/review_defects.py --category rushed_dense_chunk
```

Write a combined timing review document:

```bash
python scripts/review_defects.py --category rushed_dense_chunk --out docs/validation/observed_timing_defects_first_pass.md
```

Write only reports that include timing context:

```bash
python scripts/review_defects.py --timing-only --out docs/validation/observed_timing_defects_cleaned.md
```

Filter by timing category and require timing context:

```bash
python scripts/review_defects.py --category rushed_dense_chunk --timing-only
```

The script reads `.md.gz` files from `data/defect_reports/` by default. It prints summary counts for total reports, included reports, reports with Timing Context, reports without Timing Context, and reports by category. It does not require Flask to be running, does not delete reports, and does not write into the report directory.
