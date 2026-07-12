# Issue #11 Coarse-Seek Accessibility Validation

## Implemented Maintenance

The coarse-seek control now has a transparent 44px-high hit area while its visible progress fill remains 2px high and visually subordinate. Matching footer space prevents the hit area from intercepting reader-control taps. The existing click handler and horizontal milestone-seeking semantics are unchanged.

## Fixed Human Protocol

Use the Samsung Galaxy S23 Ultra running Android 16 with Mozilla Firefox 152 recorded by S-033, then repeat the viewport checks in a narrow desktop viewport and a normal desktop viewport.

1. Load a long-form validation sample and enter reader mode on the phone in portrait. Tap the transparent lane immediately above and around the visible 2px bar at approximately 25%, 50%, and 75% width. Confirm each tap reliably seeks to the nearest expected coarse milestone.
2. Repeat in phone landscape. Confirm the hit lane remains reliably aimable and the 2px visible bar remains unobtrusive.
3. Tap the lowest reader controls near their center and edges. Confirm the seek lane does not intercept those taps and all controls remain reachable.
4. Repeat the 25%, 50%, and 75% seeks in a narrow desktop viewport, then in a normal desktop viewport. Confirm horizontal seek mapping remains correct.
5. Exercise playback, pause/resume, an existing breakpoint, and one ordinary previous/next navigation step. Confirm seeking still pauses as before and no navigation behavior changed.

Record `passed`, `partially_passed`, `failed`, or `inconclusive`, including device/viewport and the approximate tap position for any miss. Issue #11 remains open until this human gate passes.

## Human Disposition

Pending. Issue #11 remains `AWAITING_HUMAN_VALIDATION`, owned by the human.
