# S-044 Deferred Correctness and Landscape Maintenance

## Status and Authority

S-044 is a provisional post-S-043 maintenance slice. It is not active or authorized until:

1. S-043 receives a Human-owned rehearsal disposition;
2. the S-043 management state and issue #18 are reconciled; and
3. a separate management transition explicitly activates S-044A.

S-044 contains two ordered passes:

1. **S-044A: Rule-Based Fallback Source Fidelity** — detailed authority: GitHub issue #24.
2. **S-044B: Landscape Coarse-Seek Lane Clearance** — detailed authority: GitHub issue #19.

The passes must execute in that order. S-044B must not activate automatically after S-044A.

The post-S-043 product-direction and market-discovery planning spike remains governed by GitHub issue #26. It must remain inactive until S-044 completes and receives a separate activation.

## Objective

Resolve the two accepted non-blocking defects remaining from the stabilization and productization programs before strategic product planning begins:

* preserve normalized source characters and enforce source-reconstruction postconditions in the rule-based fallback;
* prevent the defect-count display from obstructing the accepted coarse-seek interaction lane in phone landscape.

This is a bounded maintenance slice. It must not introduce new product direction, parser policy, navigation semantics, presentation redesign, or experimental tuning.

## Initiating Reason

Issues #19 and #24 were deliberately deferred because neither blocked their originating validation gates.

They should now be resolved before the planning spike so that:

* known correctness debt does not become an implicit assumption in future architecture or packaging decisions;
* the mandatory fallback has an explicit source-fidelity invariant;
* the accepted mobile navigation surface no longer carries a known layout obstruction;
* the planning spike evaluates a clean stabilized baseline rather than mixing maintenance implementation with strategic deliberation.

## S-044A: Rule-Based Fallback Source Fidelity

### Scope

Implement the narrow correction authorized by issue #24.

The pass must:

* characterize the reproduced loss or alteration of normalized source characters in rule-based fallback output;
* preserve curly quotation marks and other affected normalized source characters;
* define deterministic source-reconstruction postconditions for fallback chunk output;
* enforce those postconditions at the narrowest appropriate boundary;
* add focused regression coverage for reproduced failures;
* retain deterministic fallback behavior when parser evidence is unavailable or unsafe.

### Boundaries

S-044A must not:

* change the parser-assisted default;
* alter parser selection or fallback activation policy;
* retune the optimizer;
* expand broad handwritten semantic or grammatical rule families;
* reinterpret frozen evaluation evidence;
* modify frozen manifests, registered hashes, blind material, or historical outputs merely to accommodate new behavior;
* treat previously accepted unsafe mapping or unscorable cases as newly passed without separate authority.

Any required registered source-code hash update must reflect only the authorized implementation change and must preserve the meaning of frozen evidence.

### Validation and Completion

S-044A completes objectively when:

* the reproduced character-preservation defect is covered by focused regression tests;
* documented source-reconstruction postconditions pass for supported fallback output;
* fallback remains deterministic;
* parser-assisted behavior and mandatory fallback policy remain unchanged;
* applicable unit, characterization, frozen-baseline, repository-integrity, CI, and CodeQL checks pass;
* objective evidence is recorded;
* issue #24 is reconciled and closed as completed.

No qualitative Human acceptance gate is required for S-044A.

After completion, S-044B remains inactive until a separate management transition.

## S-044B: Landscape Coarse-Seek Lane Clearance

### Scope

Implement the narrow landscape presentation correction authorized by issue #19.

The pass must prevent the `Defects Reported: #` display from obstructing the transparent coarse-seek interaction lane in the established phone-landscape presentation.

Preserve:

* the accepted 2px visible progress bar;
* the enlarged coarse-seek touch target;
* horizontal seek mapping;
* milestone resolution;
* pause behavior;
* focus behavior;
* existing portrait presentation;
* all other navigation and defect-reporting semantics.

Prefer a landscape-specific layout or stacking correction over removing information or changing interaction policy.

### Boundaries

S-044B must not:

* redesign navigation;
* change seek calculations or thresholds;
* move responsibility for seek behavior between components;
* remove the defect count outside the affected landscape presentation;
* alter defect-report storage or reporting behavior;
* redesign the reader layout;
* introduce a new responsive framework or frontend toolchain;
* expand browser automation beyond the smallest useful regression surface.

### Validation and Completion

Codex must provide objective evidence covering:

* preservation of the progress bar and coarse-seek hit area;
* absence of overlap between the defect-count display and the intended seek lane at the targeted landscape dimensions;
* unchanged horizontal seek mapping, milestone selection, and pause behavior;
* no portrait regression;
* applicable JavaScript syntax, browser smoke, Python suite, repository-integrity, CI, and CodeQL results.

Final acceptance requires one fixed Human check using the established Samsung Galaxy S23 Ultra / Android 16 / Firefox environment:

1. rotate to phone landscape;
2. confirm the defect-count display does not obstruct the coarse-seek lane near the previously affected midpoint;
3. exercise the lane across representative left, midpoint, and right positions;
4. confirm seeking remains usable and playback remains paused as documented;
5. record any remaining obstruction or presentation regression.

Record exactly one disposition:

* `passed`
* `partially_passed`
* `failed`
* `inconclusive`

Issue #19 closes only after the required Human evidence supports completion.

## Shared Evidence Boundary

Use only repository-owned fixtures, deterministic automated evidence, and the established Human device/browser environment.

Do not modify S-043’s immutable demonstration package or reinterpret its completed rehearsal evidence. S-044 occurs after S-043 and creates a later maintenance baseline; it does not retroactively replace the S-043 demonstration identity.

Do not commit private evaluation material, sensitive source text, generated local residue, credentials, or unsupported qualitative claims.

## S-044 Completion Boundary

S-044 completes when:

* S-044A is recorded as objectively passed and issue #24 is closed;
* S-044B implementation and automated validation pass;
* the fixed Human landscape check receives a permitted passing disposition;
* issue #19 is reconciled and closed;
* management records identify both passes as completed;
* no successor scope is active;
* issue #26 remains open but inactive pending explicit activation.

No product-direction decision, planning-spike result, or successor implementation program is part of S-044.
