# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

# Project Status

> **Status:** 🟢 GREEN  
> **Last Updated:** 2026-07-09  
> **Current Phase:** Week 1 — Instrumented Defect Collection  
> **Immediate Focus:** Collect validation defects for chunking/timing refinement  

## Current State: Prototype Complete
The stable development base is finished. Text can enter the system cleanly, normalize into stable sentence units, and process through a rule-based chunking and deterministic timing engine. The mobile-first RSVP playback loop is fully operational with gesture interactions, speed controls, and local behavioral telemetry.

## Current Validation Flow
The app can generate `.md.gz` backend defect report files directly from the mobile reading session. The next step is to use those reports to identify repeatable chunking and timing defects.

## Completed Capabilities
| Area | Status | Notes |
|---|---|---|
| Flask + CI scaffold | ✅ Done | Stable development base |
| Mobile-first HTML5 shell | ✅ Done | App is phone-browser-first |
| Text ingestion | ✅ Done | Text can enter the system cleanly |
| Normalization/segmentation | ✅ Done | Raw text becomes stable sentence units |
| Rule-based chunking | ✅ Done | First semantic chunker exists |
| Timing engine | ✅ Done | Chunks receive deterministic durations |
| Schedule API | ✅ Done | Backend emits frontend-ready schedule |
| Playback loop | ✅ Done | Mobile RSVP reader works |
| Gestures | ✅ Done | Tap/swipe/long-press interaction exists |
| Speed controls | ✅ Done | User can adjust runtime speed |
| Event tracking | ✅ Done | Local behavioral telemetry exists |
| Adaptation | ✅ Done | Conservative feedback loop exists |
| Mobile hardening | ✅ Done | Timer, loading, visibility, layout issues addressed |
| Demo validation docs | ✅ Done | Evaluation process exists |
| Validation corpus/taxonomy | ✅ Done | We have a way to classify defects |

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

## Validation Workflow

The validation corpus lives in `docs/validation/corpus.md`. Start the app, load one sample from the prepare screen, and use `docs/demo_validation.md` for the 15-minute or 30-minute manual validation loop.

The app supports in-app defect reporting during reader playback. Reports are saved by the local Flask backend as compressed Markdown files under `data/defect_reports/`; see `docs/validation/in_app_defect_reporting.md` for the report format and decompression commands.

Defect report storage uses generated filenames, bounded/escaped Markdown fields, a request size limit, and a best-effort local storage encryption check. If encrypted storage cannot be confirmed, the app logs a warning and continues.

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

1. Demo validation
2. UX cleanup
3. Chunking/timing refinement based on real reading samples
4. Optional packaging/deployment notes

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
