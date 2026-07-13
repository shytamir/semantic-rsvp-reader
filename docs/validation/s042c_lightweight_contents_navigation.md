# S-042C Lightweight Contents Navigation Validation

## Automated Evidence

S-042C maps only existing project-owned schedule structure. Each supported H1
or H2 header contributes its first `is_header_chunk` schedule index, in document
order. Jumps cancel pending recovery and playback, render and persist the target,
refresh progress and structure state, and remain paused.

Local focused contents, EPUB integration, continuity, and mobile-shell evidence
passed 31 tests with one documented Node-dependent skip. The full managed suite
then passed 332 tests with the same skip; its two expected registered source-hash
failures were resolved by refreshing only the S-032 and S-033 characterization
records, after which all 8 affected checks passed. The 22-case corpus, frozen
rule-based baseline, S-037 characterization, repository integrity, and all
behavioral characterization invariants remained passing. Local JavaScript syntax
and Playwright execution were unavailable because Node was not installed; CI is
the authoritative browser execution. Terminal remote evidence is recorded after
the implementation push.

Initial remote CI run `29214665717` passed browser smoke and integrity and ran
all 329 dependency-light tests successfully, then failed because the S-031
check-only characterization JSON still held the pre-S-042C `app.js` source hash.
This scope-caused evidence maintenance gap changes no playback or evaluation
meaning. CodeQL run `29214665388` passed all three analyses.

After refreshing only the S-031 `app.js` source identity, terminal evidence for
commit `5e04e54d50da47be1e2cab81f659ac1c864320bc` passed:

- CI run `29214755155`: Core, integrity, and browser-smoke jobs passed;
- CodeQL run `29214754680`: Actions, Python, and JavaScript/TypeScript analyses
  passed.

S-042C is therefore ready for the human gate below. Automated evidence does not
declare the human disposition.

The contents view is shown only for EPUB schedules. It has a bounded scroll area,
keyboard-operable buttons, retained focus after jumps, and an explicit empty
state. It adds no navigation-document parsing, ingestion path, source persistence,
ebook rendering, or playback semantics.

## Fixed Human Protocol

Use one browser profile, the project-owned representative EPUB fixture (or an
equivalent permitted EPUB within the documented subset), and the existing phone
validation environment. Record an observation after every numbered step; do not
infer unobserved details.

1. Select and prepare the supported EPUB through the local EPUB control. Confirm
   the reader opens paused.
   Evidence: _Human to record._
2. Read enough RSVP output to confirm extracted chapter order is readable and
   consistent with the supported subset.
   Evidence: _Human to record._
3. Open Contents. Confirm the expected supported H1/H2 headings appear once and
   in document order.
   Evidence: _Human to record._
4. Jump forward and backward between headings. Confirm each jump lands at the
   intended section and remains paused.
   Evidence: _Human to record._
5. After a heading jump, press Play once. Confirm normal playback begins, then
   pause it.
   Evidence: _Human to record._
6. Confirm progress, active structure label, and an existing breakpoint remain
   coherent after navigation.
   Evidence: _Human to record._
7. Select Edit, reselect the same EPUB, and confirm position and breakpoints
   restore while playback remains paused.
   Evidence: _Human to record._
8. Rename or recompress an otherwise equivalent EPUB, reselect it, and confirm
   identity-based restoration still occurs.
   Evidence: _Human to record._
9. Reselect an EPUB whose extracted text has changed. Confirm it opens as a
   different document rather than restoring the prior position.
   Evidence: _Human to record._
10. Reload without reselecting an EPUB. Confirm the saved reference does not
    reconstruct the missing source.
    Evidence: _Human to record._
11. Select an unsupported or malformed representative EPUB. Confirm the
    documented bounded failure is clear and the reader does not open.
    Evidence: _Human to record._
12. In the existing phone environment, confirm Contents remains keyboard/focus
    operable and does not create catastrophic narrow-screen overflow.
    Evidence: _Human to record._

Disposition: _Human must record exactly one of `passed`, `partially_passed`,
`failed`, or `inconclusive`._

Defects or limitations observed: _Human to record._

Authorization to complete S-042 or proceed: _Human to record._
