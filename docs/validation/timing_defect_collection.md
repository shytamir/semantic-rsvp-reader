# Timing Defect Collection

This guide is for collecting timing and rhythm evidence after Chunking Refinement Pass 1. Do not use this pass to request chunking fixes unless the chunk itself is otherwise acceptable and the remaining discomfort is about dwell time or rhythm.

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
- nearby previous/next chunk timing
- session elapsed time and average effective duration
- recent adaptation reason/direction when available

## What Not to Report as Timing

If the chunk itself is badly split, classify it as chunking first. For example, a rushed feeling caused by `a quiet | room` or `may not | know` is still primarily a chunking defect. Timing calibration should focus on chunks that are basically well-formed but feel too fast, too slow, or rhythmically wrong.

## Suggested Timing Validation Pass

1. Load a validation sample after chunking refinement.
2. Read at default speed.
3. Keep adaptation enabled for one pass, disabled for another if useful.
4. Report only timing/rhythm discomfort.
5. Submit 8-12 timing defects.
6. Use the review utility to aggregate reports.

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

The script reads `.md.gz` files from `data/defect_reports/` by default. It does not require Flask to be running, does not delete reports, and does not write into the report directory.
