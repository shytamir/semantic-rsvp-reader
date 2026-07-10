# Chunking Refinement Pass 2 Results

Date: 2026-07-10

Source report: `docs/validation/chunking_refinement_pass_2.md`

## Summary

Top recurring issues addressed:
1. Proper names and named entities split awkwardly, especially repeated `Air Force One` / `Air Force` phrases.
2. Honorifics and titles separated from the names they identify.
3. Definite and indefinite article phrases separated from their noun heads.
4. Weak function-word and preposition-led chunks created low-value beats.
5. Curly apostrophe contractions and possessives could create orphan suffix chunks.

Out of scope for this pass:
- `quote_state_confusion` around quote display state.
- `parenthetical_state_confusion` around bracket/reference display state.
- Timing formulas, speed/adaptation behavior, playback behavior, navigation behavior, and frontend API shape.

## Implemented Rules

- Preserved compact observed named entities such as `Air Force One`, `Air Force officials`, `Dartmouth College`, `New Hampshire Legislature`, `Bandar Abbas`, `Iran's Revolutionary Guards Navy`, and `Strait of Hormuz` when they fit the existing mobile-width limit.
- Preserved observed honorific/name and title/name pairs such as `Mr. Trump`, `Dr. Kudrenko`, `President Trump`, and `Ayatollah Ali Khamenei`.
- Extended tokenization to keep common honorifics, curly apostrophe contractions, possessives, and simple hyphenated words intact.
- Narrowed article/modifier/head preservation to observed modifier-like phrases, avoiding broad over-clumping such as `The system learns`.
- Split before known phrase starts when they were attached to weak lead-ins, while preserving longer known-phrase prefixes already in progress.
- Allowed short preposition-led noun phrases such as `of funeral processions` to avoid weak two-word chunks.

## Regression Examples

- `an Air Force One.` no longer becomes `an Air Force` / `One.`
- `former Air Force officials` keeps `Air Force officials` recognizable.
- `Mr. Trump`, `Dr. Kudrenko`, and `President Trump` stay attached.
- `Iran's Revolutionary Guards Navy` stays in one chunk within the 32-character limit.
- `Strait of Hormuz` stays recognizable even at sentence end.
- `didn't` and `Trump's` do not produce orphan `t` or `s` chunks.
- `the current model` stays together without changing the legacy `The system` / `learns from` / `the reader.` split.

## Tests

Added `tests/test_chunking_refinement_pass_2.py` with focused regressions for:
- repeated `Air Force` / `Air Force One` entities;
- compact proper names and institutions;
- honorific/title-name combinations;
- military/media/place names;
- curly contraction and possessive tokenization;
- preposition-led noun phrases;
- definite article modifier/head phrases.

Verification:
- `python -m pytest` passed: 167 tests.

## Remaining Risks

- The known-phrase list is intentionally small and report-driven, so unseen proper names can still split poorly.
- Broader proper-noun inference could improve recall but risks over-clumping ordinary titlecase prose.
- Grouping named entities can produce denser chunks; the existing `max_chars` check remains the hard mobile-display guard.
- Quote and parenthetical state confusion should continue to be classified separately from chunk shape.

## Next Validation Focus

Run a post-pass chunking validation focused on:
1. repeated named entities and organization names;
2. honorific/title-name attachment;
3. article/modifier/head phrases;
4. weak preposition and function-word boundaries;
5. overlong chunks introduced by proper-name grouping.
