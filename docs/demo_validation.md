# Demo Validation

This validation loop is for prototype feedback, not a scientific study. Use it to find repeatable chunking, timing, gesture, adaptation, comprehension, and layout defects before refining the reader.

## 15-minute solo validation

1. Pick one sample from `docs/validation/corpus.md`.
2. Read it normally.
3. Summarize the main point in 3-5 bullets.
4. Load the same sample into the RSVP reader.
5. Read it using default speed/adaptation.
6. Use the in-app `Report Defect` button for every chunk/timing issue that causes friction.
7. Summarize again in 3-5 bullets.
8. Compare effort, comprehension, and irritation.

## 30-minute comparative validation

1. Pick two samples of similar difficulty.
2. Read one normally.
3. Read one with the RSVP reader.
4. Summarize both.
5. Rate perceived effort from 1-5.
6. Rate comprehension confidence from 1-5.
7. Count rewinds, pauses, and speed changes from the debug panel.
8. Record defects using the in-app workflow, or use the template if the app is not running.

## Validation questions

- Did chunking feel natural?
- Did timing feel calm or rushed?
- Were dense ideas given enough dwell time?
- Were light phrases over-emphasized?
- Did punctuation create useful rhythm?
- Did adaptation help, annoy, or go unnoticed?
- Were gestures reliable?
- Did the reader reduce eye movement fatigue?
- Could you summarize the passage afterward?
- What was the first thing that irritated you?
- Would you use this again for dense text?

## Logging defects

Use the reader's `Report Defect` button for each issue that causes friction. The app stores compressed Markdown reports under `data/defect_reports/` on the backend. If the app is not running, use `docs/validation/defect_log_template.md` instead.

Choose a category from `docs/validation/defect_taxonomy.md` and assign a severity:

- 1: minor annoyance
- 2: noticeable friction
- 3: comprehension-impacting
- 4: session-breaking

When possible, paste the original sentence and describe the observed chunks or timing. If the issue feels subjective, still log it; repeated subjective friction is useful prototype data.

See `docs/validation/in_app_defect_reporting.md` for the backend-stored report format and decompression commands.

## Generating schedules

Start the Flask app:

```bash
flask --app semantic_rsvp.web:create_app run --host 0.0.0.0
```

Then call the existing schedule API:

```bash
curl -X POST http://127.0.0.1:5000/api/schedule \
  -H "Content-Type: application/json" \
  -d '{"text":"The system learns from the reader. It adapts slowly."}'
```

You can also generate a readable schedule from a plain text file or stdin:

```bash
python scripts/schedule_sample.py sample.txt
python scripts/schedule_sample.py --json < sample.txt
```
