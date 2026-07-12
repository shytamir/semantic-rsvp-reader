# S-041 Local Reading Continuity Validation

## Automated Evidence

Focused contract checks cover versioned and separate preference/document keys,
stable source identity, bounded retention, breakpoint limits, clamping, corrupt
and obsolete records, stale eviction, removal, clearing, and excluded fields.
The final implementation report records the exact local and remote results.

Executed evidence:

- focused shell and continuity checks: 26 passed, 1 Node-dependent check
  skipped because Node was unavailable;
- full managed standard-profile suite: 317 passed, the same 1 check skipped;
- S-032 navigation/interaction and S-033 presentation characterizations were
  refreshed only for authorized source hashes and then reproduced with all
  invariants passing and no hard failures;
- the 22-case corpus, frozen rule-based baseline, S-037 characterization,
  parser-default Flask smoke, repository integrity, Markdown links, and diff
  whitespace checks passed;
- the repository JavaScript syntax command reported its documented Node-missing
  skip; the updated scripts loaded and ran without browser console errors in the
  managed in-app browser.

Browser inspection additionally confirmed that a document restored to chunk 3
of 9 while paused, its breakpoint was restored, reset returned to chunk 1, the
per-document removal survived reload, and a missing source was not restored or
stored automatically.

## Fixed Human Protocol

Use one browser profile and this exact text:

> First continuity sentence provides several chunks for restoration. Second
> continuity sentence verifies paused reopen behavior and breakpoint retention.

1. Select `Clear all local reading data`. Confirm the status reports clearing
   document references and preferences.
2. Prepare the fixed text, advance at least two chunks, set a breakpoint, change
   speed through the long-press speed controls, and disable adaptation. Note the
   current chunk, then select `Edit`.
3. Reload the page. Confirm no source text or reader screen is reconstructed,
   playback is not active, and the status reports one saved document reference.
4. Paste and prepare the same fixed text. Confirm the noted chunk and breakpoint
   restore, the reader remains paused with a `Play` control, and the speed and
   adaptation preferences remain selected. Press `Play` once and confirm reading
   resumes from the restored chunk, then pause.
5. Select `Reset`, reload, and prepare the same text again. Confirm restoration
   is paused at the first chunk.
6. Select `Remove current saved state`, reload, and prepare the same text again.
   Confirm it opens as a new document at the first chunk with no breakpoint.
7. Advance once, select `Edit`, reload without pasting the text, and confirm the
   saved reference cannot reconstruct the missing document. Select `Clear all
   local reading data` and confirm the saved-reference count returns to zero.

Record exactly one outcome: `passed`, `partially_passed`, `failed`, or
`inconclusive`. Report incorrect restoration, automatic playback, retained
source text, preference mixing, unclamped navigation, ineffective reset/removal,
or missing-document reconstruction. Do not assess S-042 or any EPUB behavior.
