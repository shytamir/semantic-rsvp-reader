# S-031 Playback and Adaptation Validation

## Automated Characterization

The repeatable characterization command is:

```bash
python scripts/characterize_s031_playback_adaptation.py --check
```

The committed [machine-readable record](../../evaluation/playback_adaptation/s031_characterization.json) checks the shipped JavaScript source for the playback lifecycle, timer replacement and cancellation, visibility pause, fixed speed levels, session reset, conservative adaptation thresholds and suppression, progress seeking, and observable session-summary fields.

No S-031 defect was reproduced during automated preparation. No playback, timing, or adaptation behavior was changed, and the passed S-029 dwell calibration remains intact. This source characterization supplements the existing Python and JavaScript checks; it is not a substitute for the phone-browser gate below.

## Fixed Human Validation Protocol

Use the pushed build on one phone browser. Record device, operating system, browser/version, orientation, build commit, and whether battery-saving or reduced-motion settings are active. Use the same long-form validation sample for both scenarios and start at `1.0x`.

### Scenario A: fixed baseline with adaptation off

1. Load a long-form validation sample, disable adaptation, and reset its adaptation window.
2. Play, pause, resume, use previous/next once, then use the slower, faster, and reset controls. Confirm the current chunk remains current and the displayed speed stays within the existing choices.
3. While playing, send the browser to the background for at least two expected chunk dwell periods. Return to it and confirm playback is paused, no hidden progress occurred, and playback does not resume until explicitly requested.
4. Resume and allow the sample to complete. Confirm the final chunk and completion state remain stable without a later timer advance. Reset, return to edit, and load new text; confirm each action leaves playback stopped and the new session starts at `1.0x`.
5. Record the visible session summary after the lifecycle checks: events, rewinds, pauses, speed changes, completion, adaptations, current speed, and adaptation state.

### Scenario B: adaptation enabled

1. Reload the same sample, confirm `1.0x`, enable adaptation, and reset its window.
2. Perform two previous-chunk actions with at least three recorded events in the window. Confirm any adaptation is a single bounded slower step and its summary count increments.
3. Make a manual speed change, then perform one immediate rewind or pause. Confirm there is no immediate counteracting adaptation during the three-event suppression window.
4. Reset the adaptation window and play forward without intervention for at least 12 automatic chunk advances. Confirm any smooth-run adaptation is a single bounded faster step and playback continues normally.
5. Use the progress seek control while playing. Confirm seeking pauses, selects a valid chunk, and does not immediately trigger adaptation. Disable adaptation and confirm further rewind/pause activity does not change speed automatically.
6. Record the same visible session-summary fields and the action that preceded each observed adaptation.

### Disposition

Report `passed`, `partially_passed`, `failed`, or `inconclusive`. For any defect, include the exact step, expected and observed state, visible summary values, whether playback was active, and whether the page had just moved between background and foreground. Do not pass S-031 solely from the automated record.

Record each scenario's final summary as: `events / rewinds / pauses / speed changes / completed / adaptations / current speed / adaptation on-or-off`. Add the build and device details above it, then give the disposition and any step-specific observations.

## Human Validation Report

### Scenario A

Reporting passed on all tests. 0 defects reported. Debug window values:
- Events: 23
  Rewinds: 1
  Pauses: 3
  Speed changes: 4
  Completed: Yes
  Adaptations: 0
  Current speed: 1.00x
  Adaptation: off

These were correctly reset on preparing a new sample as intended.

### Scenario B

Reporting passed on all tests. 0 defects reported. Debug window values:
- Events: 47
  Rewinds: 6
  Pauses: 7
  Speed changes: 4
  Completed: Yes
  Adaptations: 7
  Current speed: 1.50x
  Adaptation: On

Android 16
Firefox 152
Portrait-Oriented

No additional notes. I'm disposed to close the slice and activate the next one.