# Manual Validation

Use this guide for phone-browser validation after code changes. Detailed historical pass protocols remain in `docs/validation/`.

## Core Playback

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load a short paragraph.
4. Confirm the first chunk appears and controls are reachable.
5. Play, pause, step previous, step next, reset, and return to edit mode.
6. Confirm no timer continues after pause, reset, completion, or edit mode.

## Gestures And Controls

1. Tap reader area to play/pause.
2. Swipe left/right for chunk navigation when no breakpoints exist.
3. Hold and swipe left/right for five-chunk navigation.
4. Long press to open speed controls.
5. Confirm speed changes do not reset the current chunk.
6. Confirm browser gestures do not take over the reader surface.

## Defect Reporting

1. Pause on an awkward chunk.
2. Open Report Defect.
3. Confirm current chunk, sentence, previous/next chunks, timing, display, navigation, and structure context appear where available.
4. Submit a report.
5. Confirm a `.md.gz` report is written under `data/defect_reports/`.

## Navigation And Orientation

1. Confirm passive progress anchor appears only in reader mode.
2. Confirm progress updates are milestone-gated, not per chunk.
3. Set and remove breakpoints with double tap.
4. Traverse breakpoints with swipe when breakpoints exist.
5. Confirm drift recovery lands before the target and auto-resumes unless cancelled.
6. Confirm ghost previous chunk is subordinate and does not overlap active text.
7. Confirm structural hierarchy anchor appears only when simple `#` / `##` headers are active.

## Post-Stabilization Focus

1. Confirm ghost previous chunk never overlaps the active chunk.
2. Confirm active chunk font size remains stable.
3. Test text with title, byline, blank lines, and long-form dates.
4. Confirm source lines do not merge into body prose.
5. Watch for new overlong chunks caused by phrase preservation.
