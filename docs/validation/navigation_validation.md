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

## Defects To Report

Report navigation defects when:

- progress flickers or moves distractingly
- peripheral motion pulls attention away from the chunk
- coarse seek lands in a confusing position
- progress-bar tap conflicts with reader tap or swipe
- the progress bar blocks controls or creates horizontal scroll
- adaptation behaves unexpectedly after seek

Drift recovery is not implemented yet, so coarse seek may feel abrupt. Classify that as a navigation limitation unless the seek target itself is incorrect or the interaction conflicts with existing controls.
