# Navigation Validation

Navigation features are being added conservatively so orientation aids do not distract from reading or mask chunking defects.

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
- breakpoint jumps pause playback and do not auto-resume
- breakpoint jumps do not use drift recovery or a 3-chunk lead-in yet
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
- defect report captures previous displayed chunk metadata

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
- the progress bar blocks controls or creates horizontal scroll
- adaptation behaves unexpectedly after seek

Drift recovery applies only to breakpoint traversal. Coarse seek, manual previous/next, reset, and normal playback should not trigger it.
