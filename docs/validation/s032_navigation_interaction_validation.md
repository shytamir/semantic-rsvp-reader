# S-032 Navigation and Interaction Validation

## Automated Characterization

Run:

```bash
python scripts/characterize_s032_navigation_interaction.py --check
```

The committed [machine-readable record](../../evaluation/navigation_interaction/s032_characterization.json) contains two deterministic streams and an interaction matrix for ordinary traversal, breakpoints, coarse seeking, reset/new-stream boundaries, drift recovery, cancellation, ghost context, and H1/H2 orientation.

Automated preparation reproduced and stabilized one functional defect: left/right swipe direction changed meaning when breakpoints existed. Ordinary and breakpoint traversal now consistently use left for previous and right for next. No timing, adaptation, presentation, or new navigation behavior changed. No presentation-only finding was recorded for S-033 during automated preparation.

## Fixed Phone-Browser Protocol

Use the pushed build on one phone browser. Record build, device, operating system, browser/version, viewport/orientation, and adaptation state. The exact source text for both streams is stored under `streams.<name>.source_text` in the committed JSON. Paste the `ordinary` source for steps 1–6 and the `structural` source for step 7.

1. **Ordinary traversal:** With no breakpoints, tap to play/pause. Swipe left and confirm one previous-chunk move; swipe right and confirm one next-chunk move. Long-press without moving opens the speed overlay. Long-press then swipe left/right moves five chunks without also toggling playback or a breakpoint.
2. **Breakpoints:** At three separated chunks, double-tap to add breakpoints; double-tap one again to remove and restore it. Confirm no play/pause side effect. From between markers, swipe left to the previous breakpoint and right to the next breakpoint, matching ordinary direction.
3. **Drift recovery:** On a breakpoint swipe, confirm a lead-in up to three chunks before the target appears, the recovery status is shown, and playback resumes after about 500 ms through the target context. Confirm the progress anchor and ghost chunk follow the lead-in/current position.
4. **Cancellation:** Start another breakpoint recovery and immediately tap, reset, seek, open the speed overlay, or use a reader control before the delay ends. Confirm delayed playback does not resume. Repeat once with a different cancellation action.
5. **Coarse seek:** While playing, tap near the beginning, middle, and end of the progress anchor. Confirm playback pauses, a nearby milestone is selected, the ghost becomes the preceding chunk, and subsequent tap/swipe controls still work.
6. **Reset and new stream:** Reset and confirm index zero, empty ghost, and same-stream breakpoints remain available. Load new text and confirm breakpoints, progress, ghost, and pending recovery state are cleared.
7. **Structural orientation:** Load the committed structural stream. Traverse normally, seek, and use breakpoints across both H2 sections. Confirm the orientation label progresses from `Main Route` to `First Turn` to `Second Turn` and stays synchronized with the current chunk.

Report `passed`, `partially_passed`, `failed`, or `inconclusive`. For each defect, record the step, starting/current/target chunk indices, gesture direction, breakpoint indices, whether recovery was pending, expected and observed state, and whether playback resumed unexpectedly. Presentation-only observations belong to S-033 unless they prevent these functional checks.
