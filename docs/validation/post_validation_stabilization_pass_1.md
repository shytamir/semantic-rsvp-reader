# Post-Validation Stabilization Pass 1

Date: 2026-07-10

Source validation report used: `docs/validation/chunking_refinement_pass_3.md`

## Source Evidence

The source report included 39 defects:

- `bad_chunk_split`: 17
- `layout_or_visibility_issue`: 12
- `underdense_chunk`: 5
- `overlong_chunk`: 2
- `title_name_split`: 2
- `proper_name_split`: 1

## Top Defects Addressed

1. Ghost previous chunk overlap and unexplained active-text shrinking on mobile.
2. Source/title/byline/date lines flattening into body prose.
3. Long-form dates splitting the year from the rest of the date.
4. Observed phrasal verb, qualifier-pair, coordinated-form, noun-preposition, proper-name, and title phrase splits.
5. Focused underdense and overlong edge cases from the report.

## Layout Fixes

- Previous chunk is clipped to one line.
- Previous chunk uses hidden overflow and ellipsis.
- Previous chunk no longer receives active chunk long-token sizing classes.
- Active chunk keeps an explicit default font-size clamp.
- Extra-long active-token shrinking now applies only to substantially long tokens.
- Defect payloads include sanitized layout context when available.

## Chunking And Source-Boundary Fixes

- Structural lines are preserved as sentence-like units before chunking.
- Markdown H1/H2, title-like lines, bylines, blank-line paragraph breaks, and long-form date lines are kept separate from following prose.
- Month/day/year and day/month/year date forms are kept together.
- Small deterministic rules protect observed phrasal verbs, qualifier pairs, coordinated forms, noun-preposition phrases, obvious two-word names, and occupational/institutional title phrases.
- A conservative post-pass repairs selected underdense chunks and splits the observed subject/verb overlong case without touching timing formulas.

## Representative Before / After Examples

1. Source boundary:
   - Before: `Deterrence Alex`
   - After: `Built on Economic` / `Deterrence` / `Alex`

2. Long-form date:
   - Before: `July 4,` / `2026 Inherent`
   - After: `July 4, 2026` / `Inherent ...`

3. Phrasal verb:
   - Before: `had built` / `up his`
   - After: `built up` / `his office ...`

4. Qualifier pair:
   - Before: `He had far` / `less impressive`
   - After: `He had` / `far less impressive`

5. Coordinated form:
   - Before: `left` / `and right` / `wings`
   - After: `left and right wings`

6. Proper name and title:
   - Before: `said Ray` / `Takeyh,` / `a senior` / `fellow at`
   - After: `Ray Takeyh,` / `a senior fellow`

7. Noun-preposition phrase:
   - Before: `language of international` / `credibility`
   - After: `the primary language` / `of international credibility`

8. Overlong subject/verb:
   - Before: `The country will navigate`
   - After: `The country` / `will navigate`

## Tests Added Or Updated

- Added `tests/test_chunking_post_validation_stabilization.py`.
- Updated `tests/test_mobile_shell.py` for ghost clipping, ellipsis, stable active sizing, and layout context.
- Updated `tests/test_defect_api.py` for sanitized layout context.
- Preserved pass 1/pass 2 regression coverage for named entities, contractions, abbreviations, and `whether` modal patterns.

## Known Remaining Issues

- CSS-only tests may miss Android/Firefox rendering differences.
- Source-boundary preservation can create slightly more pauses around metadata lines.
- Phrase preservation can over-clump compact edge cases.
- Date/name preservation can create dense chunks.
- Clipping ghost text reduces previous-chunk context for very long chunks.
- Some remaining timing complaints may still be caused by chunk shape, not duration formulas.

## Next Validation Focus

1. Confirm ghost previous chunk never overlaps or visually competes with active chunk.
2. Confirm active chunk font size remains stable.
3. Test article/source text with title, byline, blank lines, and date.
4. Confirm long-form dates stay coherent.
5. Confirm headings/source lines do not merge into body prose.
6. Confirm phrasal verbs and qualifier pairs are less often split.
7. Confirm coordinated noun phrases remain coherent when compact.
8. Confirm noun-preposition phrases improve.
9. Watch for new overlong chunks from phrase preservation.
10. Watch for new underdense chunks caused by source-boundary splitting.
