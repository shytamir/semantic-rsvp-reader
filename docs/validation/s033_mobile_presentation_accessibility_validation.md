# S-033 Mobile Presentation and Accessibility Validation

## Automated Preparation

The committed [characterization record](../../evaluation/mobile_presentation_accessibility/s033_characterization.json) inventories the shipped responsive shell and the fixed viewport/content matrix. Reproduce it with:

```bash
python scripts/characterize_s033_mobile_presentation_accessibility.py --check
```

The source checks cover visible keyboard focus, dynamic viewport and safe-area handling, long-content sizing, subordinate ghost/structure cues, quote/parenthetical cues, reachable controls, and bounded speed/report overlays. All checks pass. No presentation defect was reproduced during automated characterization, so no CSS, HTML, JavaScript, navigation, or reader behavior changed.

## Fixed Human Phone-Browser Protocol

Record the phone/browser and orientation used, then run these checks against the pushed commit. Use the existing prepare-screen sample collections; the linked structural stream is directly copyable.

1. Load any General long-form validation corpus sample. In phone portrait, enter reader mode and check the active chunk, ghost, progress, and all controls at the beginning, middle, and end. Confirm no clipping, horizontal scrolling, overlap, or unexpected size shift.
2. Copy the raw [S-032 structural stream](../../evaluation/navigation_interaction/s032_structural_stream.txt), paste it into the prepare screen, and enter reader mode in phone landscape. Step through both headings and confirm the structure label, ghost, active chunk, footer, and safe-area edges stay in separate readable lanes.
3. Load `dev-width-0006` from **S-030 semantic and structural cases**. Check it in the narrowest practical portrait and landscape viewports. Confirm long chunks and the extra-long token remain legible without page-level horizontal overflow or hidden controls.
4. Repeat an ordinary long-form sample in a wide browser viewport. Confirm the reader remains centered, the active chunk dominates, and ghost/structure/progress/breakpoint cues remain visually subordinate.
5. Open the speed overlay in portrait and landscape. Confirm all speed controls and Close remain visible, reachable, and do not cover essential reader controls.
6. Open the report panel in portrait and landscape. Confirm labels, fields, context preview, Save, and Cancel remain readable and reachable; close it without submitting unless recording a real defect.
7. Load `dev-quote-0007`, then `dev-parenthetical-0008`. Step through each and confirm their cues remain distinguishable without making the active text hard to read.
8. Where a hardware keyboard or desktop narrow viewport is available, use Tab through prepare and reader controls. Confirm the focus outline is always visible, the order is usable, and focused controls are not clipped.

For every step, record `pass` or `fail` and a concise observation. A failure must name the viewport/orientation, sample, state, and affected element. Do not disposition S-033 from static checks alone.

## Human Disposition
I used the same Samsung Galaxy S23 Ultra Android 16 Mozilla Firefox 152 device. I changed orientations according to the instructions starting with portrait and ending on a desktop device with a narrow viewport.

All tests have passed with no defects detected. Create a non-blocking high priotiy issue to make the coarse seek bar more than 2px, that's not something a human finger can reliably aim at. Slice is complete and can be closed.
