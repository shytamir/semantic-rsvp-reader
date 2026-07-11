# Navigation Validation

Navigation features are being added conservatively so orientation aids do not distract from reading or mask chunking defects.

## S-032 Navigation and Interaction Validation

### Automated Characterization

Run:

```bash
python scripts/characterize_s032_navigation_interaction.py --check
```

The committed [machine-readable record](../../evaluation/navigation_interaction/s032_characterization.json) contains two deterministic streams and an interaction matrix for ordinary traversal, breakpoints, coarse seeking, reset/new-stream boundaries, drift recovery, cancellation, ghost context, and H1/H2 orientation.

Automated preparation reproduced and stabilized one functional defect: left/right swipe direction changed meaning when breakpoints existed. Ordinary and breakpoint traversal now consistently use left for previous and right for next. No timing, adaptation, presentation, or new navigation behavior changed. No presentation-only finding was recorded for S-033 during automated preparation.

### Fixed Phone-Browser Protocol

Use the pushed build on one phone browser. Record build, device, operating system, browser/version, viewport/orientation, and adaptation state. The exact source text for both streams is stored under `streams.<name>.source_text` in the committed JSON. Paste the `ordinary` source for steps 1–6 and the `structural` source for step 7.

1. **Ordinary traversal:** With no breakpoints, tap to play/pause. Swipe left and confirm one previous-chunk move; swipe right and confirm one next-chunk move. Long-press without moving opens the speed overlay. Long-press then swipe left/right moves five chunks without also toggling playback or a breakpoint.
2. **Breakpoints:** At three separated chunks, double-tap to add breakpoints; double-tap one again to remove and restore it. Confirm no play/pause side effect. From between markers, swipe left to the previous breakpoint and right to the next breakpoint, matching ordinary direction.
3. **Drift recovery:** On a breakpoint swipe, confirm a lead-in up to three chunks before the target appears, the recovery status is shown, and playback resumes after about 500 ms through the target context. Confirm the progress anchor and ghost chunk follow the lead-in/current position.
4. **Cancellation:** Start another breakpoint recovery and immediately tap, reset, seek, open the speed overlay, or use a reader control before the delay ends. Confirm delayed playback does not resume. Repeat once with a different cancellation action.
5. **Coarse seek:** While playing, tap near the beginning, middle, and end of the progress anchor. Confirm playback pauses, a nearby milestone is selected, the ghost becomes the preceding chunk, and subsequent tap/swipe controls still work.
6. **Reset and new stream:** Reset and confirm index zero, empty ghost, and same-stream breakpoints remain available. Load new text and confirm breakpoints, progress, ghost, and pending recovery state are cleared.
7. **Structural orientation:** Load the committed structural stream. Traverse normally, seek, and use breakpoints across both H2 sections. Confirm the orientation label progresses from `Main Route` to `First Turn` to `Second Turn` and stays synchronized with the current chunk.

Report `passed`, `partially_passed`, `failed`, or `inconclusive`. For each defect, record the step, starting/current/target chunk indices, gesture direction, breakpoint indices, whether recovery was pending, expected and observed state, and whether playback resumed unexpectedly. Presentation-only observations belong to S-033 unless they prevent these functional checks.

## S-027 Human Validation Outcome

S-027 completed as `passed` on 2026-07-11.

The navigation features covered by S-027 had already been exercised against the same integrated build during the immediately preceding S-026 validation. The reported result showed no acceptance-blocking regression in the progress anchor, seeking, breakpoints, ghost previous chunk, drift recovery, controls, or related navigation behavior. S-027 therefore did not require a redundant complete rerun; this record does not infer completion of each checklist item below.

The previously unvalidated structural hierarchy anchor was tested separately with Markdown H1/H2 content. The anchor displayed the active H1 or deepest active H2 correctly, updated correctly while moving through sections, was visually unobtrusive, and behaved as intended. No acceptance-blocking navigation or structural-anchor defect was observed.

## Passive Progress Anchor

Use a medium or long validation sample on a phone browser.

Check that:

- no progress bar appears in input mode
- a subtle 2px progress bar appears at the bottom in reader mode
- playback updates the bar only occasionally, not every chunk
- the bar does not flicker, pulse, animate, or strobe
- the bar does not block controls
- tapping the bar pauses playback and seeks coarsely
- reader-area tap, swipe, speed controls, and defect reporting still work after seeking

## Breakpoint Bookmarking Traversal Validation

Use a medium validation sample with enough chunks to create several breakpoint targets.

Check that:

- double-tap sets a breakpoint at the current chunk
- double-tap again removes that breakpoint
- visual feedback is a subtle background shade shift and does not distract
- breakpoint changes do not toggle play/pause as a side effect
- long-press speed overlay still works and does not set a breakpoint
- breakpoints persist during play, pause, and reset for the same loaded stream
- breakpoints clear when new text is loaded
- swipe left/right jumps between saved breakpoints when breakpoints exist
- swipe behavior remains old chunk-step behavior when no breakpoints exist
- breakpoint traversal uses drift recovery and auto-resumes after the lead-in pause
- progress anchor updates after a breakpoint jump
- defect report after breakpoint navigation includes current chunk, previous displayed chunk, and breakpoint context

## Ghost Previous Chunk Validation

Use any prepared schedule with at least three chunks.

Check that:

- previous chunk is hidden or empty at index 0
- previous chunk appears above the current chunk after advancing
- previous chunk is roughly half contrast and visually secondary
- current chunk remains the dominant focus
- previous chunk updates during automatic playback
- previous chunk updates after manual previous/next
- previous chunk updates after progress seek
- previous chunk updates after breakpoint jump
- previous chunk does not become interactive
- previous chunk does not cause layout jitter or crowd controls
- long previous chunks are clipped to one line with ellipsis
- previous chunk never wraps into or obscures the active chunk
- active chunk font size remains stable when the previous chunk is long
- defect report captures previous displayed chunk metadata
- defect report captures layout context when available

## Post-Stabilization Validation Focus

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

## Drift Recovery Validation

Use a medium validation sample with at least two saved breakpoints.

Check that:

1. Set at least two breakpoints.
2. Swipe to a breakpoint.
3. Confirm the reader lands at `max(0, breakpoint - 3)`, not directly on the breakpoint.
4. Confirm it pauses for about 500ms.
5. Confirm playback auto-resumes after the pause.
6. Confirm the breakpoint is reached naturally after up to three chunks.
7. Confirm ghost previous chunk updates during the lead-in.
8. Confirm progress anchor updates to the lead-in location.
9. Confirm ordinary chunk swipe still works when no breakpoints exist.
10. Confirm progress-bar seek does not trigger drift recovery.
11. Confirm manual previous/next does not trigger drift recovery.
12. Confirm tapping during the 500ms pause cancels pending auto-resume.
13. Confirm loading new text cancels pending auto-resume.
14. Confirm double-tap breakpoint toggle does not accidentally start drift recovery.
15. Confirm defect reports include drift recovery context.

## Structural Hierarchy Anchor Validation

Use one sample without Markdown headers and one sample with simple `#` / `##` headers.

Check that:

1. Load text with no Markdown headers.
2. Confirm no structure label appears.
3. Load text with one `# H1` header.
4. Confirm the label appears in reader mode.
5. Confirm the label is static and does not move.
6. Confirm the label is hidden in input mode.
7. Load text with `# H1` and `## H2` sections.
8. Confirm label updates when entering the H2 section.
9. Confirm label does not animate or shift layout.
10. Confirm current chunk remains visually dominant.
11. Confirm ghost previous chunk remains readable but subordinate.
12. Confirm progress anchor remains stable.
13. Confirm breakpoint/drift behavior remains stable.
14. Submit a defect report under an H2 section.
15. Confirm saved defect report includes structural context.

## Manual Test: Breakpoints + Ghost Previous Chunk

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load a medium validation text.
4. Enter reader mode.
5. Confirm previous chunk is hidden/empty at first chunk.
6. Advance a few chunks.
7. Confirm previous chunk appears above current chunk at reduced contrast.
8. Confirm current chunk remains dominant.
9. Double-tap reader area.
10. Confirm subtle background flash.
11. Confirm a breakpoint is set without toggling play/pause unexpectedly.
12. Move several chunks forward.
13. Double-tap again to set another breakpoint.
14. Swipe right.
15. Confirm reader jumps to previous breakpoint and pauses.
16. Swipe left.
17. Confirm reader jumps to next breakpoint and pauses.
18. Confirm progress bar updates after jump if passive anchor is implemented.
19. Double-tap an existing breakpoint.
20. Confirm breakpoint is removed.
21. Clear all breakpoints by loading new text.
22. Confirm swipe behavior falls back to normal chunk previous/next when no breakpoints exist.
23. Confirm long-press speed overlay still works if implemented.
24. Confirm tap play/pause still works.
25. Confirm progress-bar tap-to-seek still works if implemented.
26. Create a defect report.
27. Confirm saved defect report includes current chunk and previous displayed chunk context.
28. Run `python -m pytest`.
29. Run `python scripts/check_js_syntax.py`.

## Manual Test: Drift Recovery

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load a medium validation text.
4. Enter reader mode.
5. Advance to chunk 8 or later.
6. Double-tap to set a breakpoint.
7. Advance to chunk 20 or later.
8. Double-tap to set another breakpoint.
9. Swipe right to jump to the previous breakpoint.
10. Confirm the app lands three chunks before the breakpoint, or at 0 if near the beginning.
11. Confirm the app waits about 500ms.
12. Confirm playback resumes automatically.
13. Confirm the app reaches the saved breakpoint naturally after the lead-in.
14. During another drift recovery, tap the reader before 500ms expires.
15. Confirm auto-resume is cancelled.
16. During another drift recovery, tap progress seek before 500ms expires.
17. Confirm auto-resume is cancelled and seek wins.
18. Confirm ordinary swipe previous/next still works after loading new text with no breakpoints.
19. Confirm ghost previous chunk updates correctly throughout.
20. Submit a defect report after a drift recovery.
21. Confirm saved report includes drift recovery context.
22. Run `python -m pytest`.
23. Run `python scripts/check_js_syntax.py`.

## Manual Test: Structural Hierarchy Anchor

1. Start Flask locally.
2. Open the app on a phone browser.
3. Load a text with no Markdown headers.
4. Enter reader mode.
5. Confirm no structural label appears.
6. Return to input mode.
7. Load text containing one `# Main Title` and two `## Section` headings.
8. Enter reader mode.
9. Confirm the top label is visible but subtle.
10. Confirm the top label is static and does not move.
11. Confirm the top label does not animate.
12. Confirm current chunk remains the focus.
13. Advance from intro into the first H2 section.
14. Confirm the label updates appropriately.
15. Advance into the second H2 section.
16. Confirm the label updates appropriately.
17. Use manual previous/next.
18. Confirm the label updates correctly.
19. Use progress seek if implemented.
20. Confirm the label updates correctly.
21. Use breakpoint traversal if implemented.
22. Confirm the label updates correctly.
23. Use drift recovery if implemented.
24. Confirm the label updates correctly during lead-in.
25. Submit a defect report.
26. Confirm saved report includes Structural Context.
27. Run `python -m pytest`.
28. Run `python scripts/check_js_syntax.py`.

## Defects To Report

Report navigation defects when:

- progress flickers or moves distractingly
- peripheral motion pulls attention away from the chunk
- coarse seek lands in a confusing position
- progress-bar tap conflicts with reader tap or swipe
- breakpoint swipe traversal conflicts with expected chunk-step navigation
- ghost previous chunk distracts from the current RSVP chunk
- drift recovery auto-resume feels surprising
- the 500ms recovery pause feels too short or too long
- three lead-in chunks are insufficient for the surrounding sentence
- a cancelled drift recovery resumes playback anyway
- drift recovery lands at the wrong lead-in chunk
- structure anchor shows the wrong label
- structure anchor is missing when a simple H1/H2 header is active
- structure anchor distracts from RSVP focus
- structure anchor causes layout shift
- the progress bar blocks controls or creates horizontal scroll
- adaptation behaves unexpectedly after seek

Drift recovery applies only to breakpoint traversal. Coarse seek, manual previous/next, reset, and normal playback should not trigger it.
