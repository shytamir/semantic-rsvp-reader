# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

# Project Status

> **Status:** GREEN
> **Last Updated:** 2026-07-10
> **Current Phase:** Chunker-dominant refinement
> **Immediate Focus:** Post-Chunker Refinement Pass 2 validation focused on named entities, titles, articles, and weak boundaries

## Current State: Prototype Complete
The stable development base is finished. Text can enter the system cleanly, normalize into stable sentence units, and process through a rule-based chunking and deterministic timing engine. The mobile-first RSVP playback loop is fully operational with gesture interactions, speed controls, local behavioral telemetry, backend defect reports, display-state annotations for quoted and parenthetical spans, and dormant navigation metadata scaffolding.

## Current Validation Flow
The app can generate `.md.gz` backend defect report files directly from the mobile reading session. Reports carry explicit timing context, display metadata, quote state, parenthetical state, and optional navigation metadata so validation can separate timing rhythm, chunk shape, layout, visual-context, and future orientation defects.

## Completed Capabilities
| Area | Status | Notes |
|---|---|---|
| Flask + CI scaffold | Done | Stable development base |
| Mobile-first Flask/HTML5 prototype | Done | App is phone-browser-first |
| Text ingestion | Done | Text can enter the system cleanly |
| Text normalization | Done | Raw input is cleaned before scheduling |
| Sentence segmentation | Done | Common abbreviations, times, and initialisms are protected |
| Pure-Python rule-based semantic chunking | Done | Inspectable semantic chunker exists |
| Chunking refinement pass 1 from observed defects | Done | Observed modifier/head, verb-support, and punctuation-boundary defects addressed |
| Chunking refinement pass 2 from observed defects | Done | Proper-name, honorific/title, article, preposition, and curly apostrophe defects addressed |
| Deterministic timing engine | Done | Chunks receive deterministic durations |
| Timing Calibration Pass 1 from clean timing-context defect reports | Done | Dense, extra-dense, punctuation, and quote rhythm are conservatively adjusted |
| Dense chunk dwell calibration | Done | Dense chunks get a modest baseline dwell increase |
| Extra-dense chunk dwell bonus | Done | Long/reflective dense chunks get a bounded additional bonus |
| Punctuation/quote-aware timing adjustment | Done | Quote boundaries, strong punctuation, and dense sentence endings get bounded settling time |
| Post-validation targeted calibration | Done | Third-pass report drove narrow timing, chunking, and text-cleanliness fixes |
| Extreme semantic-density timing bonus | Done | Extreme dense/proper-noun/abstract chunks get bounded extra dwell |
| Punctuation/quote rhythm follow-up | Done | Semicolon, colon, quote, and comma-list emphasis timing refined |
| Chunking cleanup for `as` and `should` | Done | Short `as` phrases and modal/auxiliary attachment are less likely to pollute timing reports |
| Quote-spacing/text-cleanliness cleanup | Done | Closing quote followed by a word is normalized into readable spacing |
| Quote/parenthetical display-state indicators | Done | Schedule metadata and frontend styling identify quote and parenthetical spans |
| Navigation metadata scaffolding | Done | Schedule items include character span, paragraph, and coarse progress metadata |
| Paragraph/progress milestone metadata | Done | Paragraph starts and 5% progress crossings are computed for future navigability |
| Dormant navigability UI scaffolding | Done | Hidden progress/breakpoint placeholders and inactive JS helpers exist |
| Passive bottom progress anchor | Done | Subtle 2px bottom bar provides spatial orientation in reader mode |
| Milestone-gated progress updates | Done | Visible progress advances only at paragraph starts, 5% milestones, and forced navigation events |
| Coarse tap-to-seek navigation | Done | Progress-bar taps pause playback and jump to a nearby progress milestone |
| JavaScript syntax check | Done | Lightweight `node --check` wrapper runs locally when Node exists and is enforced in CI |
| `/api/schedule` | Done | Backend emits frontend-ready schedule |
| Mobile RSVP playback loop | Done | Reader advances scheduled chunks |
| Touch gestures | Done | Tap/swipe/long-press interaction exists |
| Session-only speed controls | Done | User can adjust runtime speed without persistence |
| Session-only event tracking/debug summary | Done | Local behavioral telemetry exists for the current session |
| Session-only conservative adaptation | Done | Conservative feedback loop exists without accounts or persistence |
| Mobile hardening | Done | Timer, loading, visibility, layout issues addressed |
| In-app backend-stored compressed defect reports | Done | Reports save as `.md.gz` files on the Flask backend |
| Defect report security hardening | Done | Bounded escaped fields, generated filenames, request limits, and storage-encryption warning |
| Timing-context defect instrumentation | Done | Reports include base/effective duration, speed, chunk metadata, and session summary |
| Validation corpus and defect taxonomy | Done | We have samples and a way to classify defects |
| Defect review workflow | Done | `scripts/review_defects.py` aggregates, filters, and exports reports |
| Display/tokenization noise cleanup from timing-review findings | Done | Chunk display avoids browser word splitting; time abbreviations, initialisms, and `whether` modal patterns are cleaner |

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the App

```bash
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Open `http://127.0.0.1:5000` on the host machine, or use the host machine's LAN IP address from a phone or another device on the same network.

## Run Tests

```bash
pytest
```

The repository includes `pyproject.toml` so pytest can import the local `semantic_rsvp` package directly from a fresh clone.

## JavaScript Syntax Check

```bash
python scripts/check_js_syntax.py
```

The script checks `static/js/app.js` with `node --check` or `nodejs --check` when either runtime is available. If Node is missing locally, it prints a warning and skips without failing. GitHub Actions installs Node and enforces this check in CI. No npm packages, frontend framework, bundler, or transpiler are used.

## Validation Workflow

The validation corpus lives in `docs/validation/corpus.md`. Start the app, load one sample from the prepare screen, and use `docs/demo_validation.md` for the 15-minute or 30-minute manual validation loop.

The app supports in-app defect reporting during reader playback. Reports are saved by the local Flask backend as compressed Markdown files under `data/defect_reports/`; see `docs/validation/in_app_defect_reporting.md` for the report format and decompression commands.

Defect report storage uses generated filenames, bounded/escaped Markdown fields, a request size limit, and a best-effort local storage encryption check. If encrypted storage cannot be confirmed, the app logs a warning and continues.

Chunking refinement pass 1 is documented in `docs/validation/chunking_refinement_pass_1.md`. It addresses the first observed modifier/head, verb-support, and punctuation-boundary defects. Chunking refinement pass 2 is documented in `docs/validation/chunking_refinement_pass_2.md`, with implementation results in `docs/validation/chunking_refinement_pass_2_results.md`; it addresses observed proper-name, honorific/title, article, preposition, and curly apostrophe defects while keeping timing/playback behavior stable. A follow-up evidence-hygiene cleanup reduces display wrapping, `a.m.`/`p.m.` initialism, and `whether ... would` noise before calibration. Timing Calibration Pass 1 is documented in `docs/validation/timing_calibration_pass_1.md`, and the targeted third-pass follow-up is documented in `docs/validation/post_validation_targeted_calibration.md`.

Quote and parenthetical state indicators are documented in `docs/validation/quote_parenthetical_state_indicators.md`. Use `quote_state_confusion` and `parenthetical_state_confusion` when the issue is visual context, not timing.

Defect reports now include timing context such as base duration, effective duration, playback speed, syntactic hint, content word count, character length, quote state, parenthetical state, nearby chunk timing, session timing summary, optional navigation metadata, and display metadata. See `docs/validation/timing_defect_collection.md` for the timing defect collection workflow and `scripts/review_defects.py` for local report review/export.

Navigation metadata is available in schedule items for future orientation and recovery features. The passive spatial anchor uses that metadata for a low-distraction bottom progress bar. Updates are intentionally milestone-gated rather than per-chunk, and progress-bar tap seeking is coarse. Bookmark traversal and drift recovery are not implemented yet.

Log defects with the in-app `Report Defect` button, or use `docs/validation/defect_log_template.md` when working outside the app. Choose categories from `docs/validation/defect_taxonomy.md`. Interpret severity as:

- 1: minor annoyance
- 2: noticeable friction
- 3: comprehension-impacting
- 4: session-breaking

To inspect the backend schedule without using the UI, run:

```bash
python scripts/schedule_sample.py sample.txt
```

or pipe text through stdin:

```bash
python scripts/schedule_sample.py --json < sample.txt
```

## Next Milestones

1. Post-Chunker Refinement Pass 2 validation
2. Breakpoint Bookmarking Traversal
3. Drift Recovery Logic
4. Post-navigation usability validation

## Manual Test Checklist

Mobile playback manual test:

1. Open app on a phone browser.
2. Paste a short paragraph.
3. Tap Load/Prepare.
4. Confirm first chunk appears centered.
5. Tap Play.
6. Confirm chunks advance automatically.
7. Tap Pause.
8. Confirm playback stops immediately.
9. Tap Previous.
10. Confirm it moves back one chunk and remains paused.
11. Tap Next.
12. Confirm it moves forward one chunk and remains paused.
13. Tap Reset.
14. Confirm it returns to first chunk and remains paused.
15. Let playback reach the end.
16. Confirm it stops cleanly.
17. Tap Back/Edit Text.
18. Confirm input mode returns and no timer keeps running.

Touch gesture manual test:

1. Open app on a phone browser.
2. Paste a short paragraph and load it.
3. Confirm first chunk appears centered and paused.
4. Tap reader area.
5. Confirm playback starts.
6. Tap reader area again.
7. Confirm playback pauses.
8. Swipe left.
9. Confirm reader moves back one chunk and pauses.
10. Swipe right.
11. Confirm reader moves forward one chunk and pauses.
12. Swipe left at the first chunk.
13. Confirm it stays on the first chunk and remains paused.
14. Swipe right at the final chunk.
15. Confirm it stays on the final chunk and remains paused.
16. Long press reader area.
17. Confirm speed overlay appears.
18. Long press again or close overlay.
19. Confirm overlay disappears.
20. Confirm swipes do not accidentally toggle play/pause.
21. Confirm long press does not accidentally toggle play/pause.
22. Hold reader area, then swipe left.
23. Confirm reader moves back five chunks or stops at the first chunk and remains paused.
24. Hold reader area, then swipe right.
25. Confirm reader moves forward five chunks or stops at the final chunk and remains paused.
26. Confirm the -5 and +5 buttons match the hold-swipe behavior.
27. Confirm buttons still work.
28. Confirm Back/Edit Text stops playback and returns to input mode.

Speed control manual test:

1. Open app on a phone browser.
2. Paste a paragraph and load it.
3. Confirm first chunk appears centered and paused.
4. Long press reader area.
5. Confirm speed overlay opens.
6. Confirm current speed shows 1.00x.
7. Tap Faster.
8. Confirm speed label increases.
9. Tap Slower.
10. Confirm speed label decreases.
11. Tap Reset.
12. Confirm speed returns to 1.00x.
13. Close overlay.
14. Tap Play.
15. Confirm playback works.
16. While playing, open speed overlay and increase speed.
17. Confirm upcoming chunks advance faster.
18. Decrease speed while playing.
19. Confirm upcoming chunks advance slower.
20. Confirm changing speed does not reset current chunk index.
21. Confirm Back/Edit Text stops playback.
22. Load new text.
23. Confirm speed resets to 1.00x.
24. Confirm gestures and buttons still work.

Session event tracking manual test:

1. Open app on a phone browser.
2. Paste a paragraph and load it.
3. Confirm event count starts at 1 or otherwise records schedule_loaded.
4. Confirm debug panel shows current event counts.
5. Tap Play.
6. Confirm play event count is reflected.
7. Tap Pause.
8. Confirm pause count increases.
9. Tap Previous or swipe left.
10. Confirm rewind count increases.
11. Tap Next or swipe right.
12. Confirm manual next event is recorded if visible in summary.
13. Open speed overlay.
14. Change speed.
15. Confirm speed change count increases.
16. Tap Reset.
17. Confirm reset event is recorded if visible in event count.
18. Play until final chunk.
19. Confirm completed becomes yes/true.
20. Tap Back/Edit Text.
21. Load new text.
22. Confirm previous session events are cleared.
23. Confirm playback behavior still matches the previous slice.
24. Confirm no data is sent to backend except schedule requests.

Session adaptation manual test:

1. Open app on a phone browser.
2. Paste a paragraph long enough for at least 30 chunks.
3. Load the schedule.
4. Confirm adaptation status is enabled.
5. Confirm current speed starts at 1.00x.
6. Tap Play.
7. Let playback advance smoothly for enough chunks to trigger a smooth-run speedup.
8. Confirm speed increases by one level only.
9. Confirm adaptation count increases.
10. Confirm playback continues normally.
11. Rewind several times.
12. Confirm speed decreases by one level only after threshold is reached.
13. Pause repeatedly.
14. Confirm speed decreases conservatively after threshold is reached.
15. Manually change speed using speed controls.
16. Confirm adaptation does not immediately override the manual change.
17. Disable adaptation.
18. Rewind/pause repeatedly.
19. Confirm speed does not change automatically.
20. Re-enable adaptation.
21. Tap reset adaptation.
22. Confirm adaptation counters/window reset but session event log remains.
23. Let playback reach the end.
24. Confirm completion still works.
25. Load new text.
26. Confirm adaptation state resets cleanly.
27. Confirm no events are sent to backend except schedule requests.

Mobile hardening manual test:

1. Open app on a phone browser.
2. Paste a paragraph and load it.
3. Rapidly tap Load/Prepare several times.
4. Confirm only one schedule is loaded and no duplicate playback begins.
5. Tap Play.
6. Confirm chunks advance normally.
7. Tap Pause.
8. Confirm playback stops immediately.
9. Tap Play again.
10. While playing, press Back/Edit Text.
11. Confirm playback stops and input mode returns.
12. Load new text.
13. Confirm old playback does not continue.
14. While playing, lock phone or switch apps.
15. Return to browser.
16. Confirm reader is paused on the same chunk.
17. Confirm it does not auto-resume.
18. Rotate phone portrait/landscape.
19. Confirm chunk remains visible and centered.
20. Confirm controls remain reachable.
21. Open speed overlay.
22. Rotate phone again.
23. Confirm overlay remains usable.
24. Use gestures after rotation.
25. Confirm tap/swipe/long press still behave correctly.
26. Trigger an API error if possible.
27. Confirm a visible error appears and stale playback does not continue.
28. Complete a 15-30 minute reading session.
29. Confirm no obvious timer drift, duplicate advancement, layout breakage, or stuck controls.

In-app backend defect reporting manual test:

1. Start the Flask app locally.
2. Open app on a phone browser pointed at the local server.
3. Load demo text or a validation sample.
4. Start playback.
5. Pause on a chunk that feels awkward.
6. Tap Report Defect.
7. Confirm playback pauses.
8. Confirm defect panel opens.
9. Confirm current chunk is shown.
10. Confirm original sentence is shown if available.
11. Confirm previous/next chunks are shown.
12. Choose category and severity.
13. Add notes.
14. Add preferred behavior.
15. Submit the report.
16. Confirm saved status appears with report ID or filename.
17. Confirm defect count increases.
18. Check backend report directory.
19. Confirm a `.md.gz` file was created.
20. Decompress it.
21. Confirm the Markdown includes the report details and context.
22. Report a second defect.
23. Confirm a second `.md.gz` file is created.
24. Confirm existing playback controls still work.
25. Load new text.
26. Confirm defect count resets.

Timing instrumentation manual test:

1. Start the Flask app locally.
2. Open the app on a phone browser.
3. Load demo text or a validation sample.
4. Start playback.
5. Pause on any chunk.
6. Tap Report Defect.
7. Confirm context preview shows current chunk.
8. Confirm context preview shows base duration.
9. Confirm context preview shows effective duration.
10. Confirm context preview shows playback speed.
11. Choose category rushed_dense_chunk.
12. Add notes.
13. Submit the report.
14. Confirm saved status appears.
15. Decompress the generated `.md.gz` file.
16. Confirm Markdown includes Timing Context.
17. Confirm previous/next chunks include timing metadata where available.
18. Confirm existing playback, speed controls, gestures, adaptation, and defect reporting still work.

Evidence hygiene manual test:

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load demo text or a validation sample.
4. Find a longer/dense chunk.
5. Confirm the displayed chunk does not hyphenate or split words awkwardly.
6. Confirm no horizontal page scroll appears.
7. Submit a defect report for any layout issue if seen.
8. Confirm the saved report includes timing context.
9. Confirm display metadata is included.
10. Load text containing "9 a.m." and "6 p.m."
11. Confirm sentence splitting remains correct.
12. Load text containing "U.S." or "E.U."
13. Confirm no ugly punctuation chunks appear.
14. Run the defect review utility with timing-only filtering.
15. Confirm older reports without Timing Context are excluded.
16. Confirm existing playback, gestures, speed controls, adaptation, and reporting still work.

Timing Calibration Pass 1 manual test:

1. Start Flask locally.
2. Open app on a phone browser.
3. Load a validation sample with dense prose.
4. Read at 1.0x with adaptation disabled.
5. Watch dense chunks and sentence-ending chunks.
6. Confirm they feel less rushed than before.
7. Switch to 1.15x.
8. Confirm dense chunks remain readable more often.
9. Find quote/punctuation-heavy sentences.
10. Confirm quote and punctuation rhythm feels less abrupt.
11. Submit defect reports only for remaining genuine timing problems.
12. Confirm layout/tokenization/chunking defects are classified separately.
13. Run pytest.

Post-validation targeted calibration manual test:

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load a dense validation sample.
4. Disable adaptation.
5. Read at 1.0x.
6. Watch for extreme semantic-density chunks.
7. Switch to 1.15x.
8. Confirm dense proper nouns and abstract chunks feel less rushed.
9. Optionally test 1.3x.
10. Find semicolon/comma/quote-heavy sentences.
11. Confirm punctuation rhythm feels less abrupt.
12. Watch for orphaned `as` and awkward `should` chunks.
13. Confirm quote-spacing defects like `intuition"cannot` no longer appear.
14. Submit defect reports only for remaining genuine defects.
15. Run pytest.

Quote/parenthetical state indicator manual test:

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load text containing a quoted sentence that spans several chunks.
4. Confirm quote chunks have a subtle left-side state indicator.
5. Confirm the first displayed character does not shift when entering or leaving the quote.
6. Load text containing a parenthetical aside.
7. Confirm parenthetical chunks are visually quieter than mainline chunks.
8. Pause on a quoted chunk and tap Report Defect.
9. Confirm context preview includes quote state and quote boundary.
10. Pause on a parenthetical chunk and tap Report Defect.
11. Confirm context preview includes parenthetical state and depth.
12. Submit `quote_state_confusion` or `parenthetical_state_confusion` only when the visual state is unclear.
13. Use `punctuation_rhythm_issue` only when visual state is clear and rhythm still feels wrong.
14. Confirm playback speed, adaptation, gestures, and timing behavior are unchanged.
15. Run pytest.

Passive Spatial Anchor manual test:

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load a medium or long validation sample.
4. Confirm no progress bar appears in input mode.
5. Enter reader mode.
6. Confirm a subtle 2px progress bar appears at the bottom.
7. Start playback.
8. Confirm the bar updates only occasionally, not every chunk.
9. Confirm progress does not flicker or strobe.
10. Pause playback.
11. Tap near the middle of the progress bar.
12. Confirm playback remains paused.
13. Confirm the reader jumps to a roughly middle location.
14. Confirm progress bar updates to the resolved location.
15. Tap near the beginning.
16. Confirm reader jumps near the beginning and remains paused.
17. Tap near the end.
18. Confirm reader jumps near the end and remains paused.
19. Confirm reader-area tap/play/pause still works.
20. Confirm swipe previous/next still works.
21. Confirm speed controls still work.
22. Confirm adaptation does not behave unexpectedly after seek.
23. Confirm defect reporting still works after seek.
24. Tap Edit Text.
25. Confirm progress bar hides or resets.
26. Load new text.
27. Confirm progress starts at 0%.
28. Run pytest.
