# Semantic RSVP Reader

Semantic RSVP Reader is a mobile-first HTML5 reading prototype served by Flask. The prototype explores whether deterministic semantic chunking and rhythm control can improve reading throughput without harming comprehension.

## Current Scope

This repository currently contains the Week 4 adaptation foundation:

- Flask app factory and routes for `/`, `/health`, `/api/ingest`, and `/api/schedule`
- Optional `/api/chunk` endpoint for chunking one sentence
- Mobile-first HTML/CSS/vanilla JS playback loop
- Pure-Python text normalization
- Deterministic sentence segmentation
- Pure-Python rule-based semantic chunking v1
- Deterministic timing and full text-to-schedule generation
- Touch gestures for play/pause and chunk navigation
- Session-only speed controls
- Session-only event tracking and debug summary
- Session-only conservative adaptation
- Pytest coverage for the web app, normalization, segmentation, ingestion API, chunking, timing, and scheduling
- GitHub Actions CI that installs minimal dependencies and runs pytest

## Non-Goals

This version does not implement adaptive speed, persistence, accounts, databases, EPUB/PDF import, ML models, NLP services, spaCy, transformers, or a frontend framework.

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

## Next Milestones

1. Mobile hardening
2. Demo validation
3. UX cleanup
4. Optional chunking/timing refinements

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
17. Confirm speed overlay placeholder appears.
18. Long press again or close overlay.
19. Confirm overlay disappears.
20. Confirm swipes do not accidentally toggle play/pause.
21. Confirm long press does not accidentally toggle play/pause.
22. Confirm buttons still work.
23. Confirm Back/Edit Text stops playback and returns to input mode.

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
