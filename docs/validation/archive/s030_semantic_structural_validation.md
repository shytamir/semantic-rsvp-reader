# S-030 Semantic Output and Structural Integrity Validation

## Final Outcome

Human-owned evidence commit `c632b71` dispositioned S-030 as `passed`. The structural fixture passed with one authorized non-blocking CSS stabilization: the visible structure anchor now reserves a separate top lane from the ghost chunk. Long-word, quote-closure, and parenthetical-closure observations remain evaluation evidence and did not trigger semantic implementation changes.

## Automated Characterization

The repeatable characterization command is:

```bash
python scripts/characterize_s030_semantic_integrity.py --check
```

The committed [machine-readable record](../../../evaluation/semantic_integrity/s030_characterization.json) covers all 22 visible project-owned cases under parser-assisted and rule-based chunking plus a fixed H1/H2 structural fixture.

Results:

- parser fallback: 0 cases;
- parser width violations: 0;
- parser splits across 16 selected protected spans: 0;
- structural fixture failures: 0;
- rule-based splits across selected spans: 2.

The two rule-based findings are already represented by visible evaluation cases, so no new case or rule change was needed:

- `dev-names-0001`: rule-based output splits `Dr. Mira Patel`;
- `dev-negation-0003`: rule-based output splits `back down`.

They remain fallback-quality observations for the human pass, not parser-retuning evidence. No semantic implementation was changed in S-030 automated preparation.

## Fixed Human Validation Protocol

Use the pushed parser-default build on the same phone/browser where practical. Keep speed at `1.0x`, disable adaptation, and do not tune or edit cases during the pass.

### Parser-default semantic cases

In the prepare screen, use the **S-030 semantic and structural cases** collection. Its buttons are generated directly from the visible experiment manifests and appear in this protocol order:

1. `dev-names-0001` — names and entities.
2. `dev-date-0002` — date and source boundary.
3. `dev-negation-0003` — negation and phrasal verb.
4. `dev-source-0005` — title, byline, date, and body transition.
5. `dev-width-0006` — long-token width pressure.
6. `dev-quote-0007` — quote and core-claim span.
7. `dev-parenthetical-0008` — parenthetical span and display state.
8. `reg-air-force-0003` — `Air Force One` entity.
9. `reg-khamenei-0004` — proper names and geographic entity.
10. `reg-phrasal-0005` — `built up`.
11. `reg-qualifier-0006` — `far less`.
12. `reg-coordinated-0007` — coordinated phrase.
13. `gen-synthetic-0003` — unseen clause and `ruled out`.
14. `gen-synthetic-0005` — byline/date plus prose.

For each case, record whether chunks preserve the named/protected material, remain understandable without routine rewind, avoid harmful source-boundary merging, and avoid unjustified overlong/underdense output. Record any new semantic defect as an evaluation-case candidate before proposing a fix.

### Structural fixture

Load:

```text
# Main Title

Intro text.

## First Section

Section body.

## Second Section

Closing body.
```

Confirm the active label progresses from `Main Title` to `First Section` to `Second Section`, the active path retains the H1 under each H2, header chunks are identifiable, and the orientation cue does not mask a chunk defect.

### Mandatory fallback

Restart with `RSVP_CHUNKER_MODE=rule_based` and repeat `dev-names-0001`, `dev-negation-0003`, `dev-source-0005`, and `dev-width-0006`. Confirm output remains deterministic, ordered, readable, and width-safe. Specifically judge whether the two characterized splits are acceptable fallback limitations or acceptance-blocking defects.

Report `passed`, `partially_passed`, `failed`, or `inconclusive`, with case IDs and exact chunk text for every defect. S-031 must remain inactive until S-030 is dispositioned and separately closed.

## Human Validation Record

### Session Information

* **Validator:the human**
* **Date:11/07/2026**
* **Build/commit:490f689**
* **Device:phone**
* **Operating system:android 16**
* **Browser and version:firefox152.0.5**
* **Viewport/orientation:mixed, mostly portrait. switch sometimes for anecdotal regression validation**
* **Speed:1.0x** `1.0x`
* **Adaptation disabled:Yes** Yes / No
* **Parser-default mode confirmed:Yes** Yes / No
* **General session notes:human operator - fallible and prone to data entry errors**

### Rating Key

* `P` — passed
* `O` — non-blocking observation
* `D` — defect
* `N/A` — criterion not applicable
* `NT` — not tested

For every `D`, add a corresponding entry to the **Defect and Evaluation-Case Candidate Log** with the exact chunk text.

## Parser-Default Semantic Cases

| Case                     | Protected material preserved | Understandable without routine rewind | Source boundaries safe | Chunk length/density acceptable | Overall | Brief notes |
| ------------------------ | ---------------------------: | ------------------------------------: | ---------------------: | ------------------------------: | ------: | ----------- |
| `dev-names-0001`         | P                            | P                                     |                    N/A | P                               | P       |             |
| `dev-date-0002`          | P                            | P                                     | P                      | P                               | P       |             |
| `dev-negation-0003`      | P                            | P                                     |                    N/A | P                               | P       |             |
| `dev-source-0005`        | P                            | P                                     | P                      | P                               | P       |             |
| `dev-width-0006`         | D                            | D                                     |                    N/A | P                               | D       |             |
| `dev-quote-0007`         | D                            | P                                     |                    N/A | P                               | O       |             |
| `dev-parenthetical-0008` | D                            | P                                     |                    N/A | P                               | O       |             |
| `reg-air-force-0003`     | P                            | P                                     |                    N/A | P                               | P       |             |
| `reg-khamenei-0004`      | P                            | P                                     |                    N/A | P                               | P       |             |
| `reg-phrasal-0005`       | P                            | P                                     |                    N/A | P                               | P       |             |
| `reg-qualifier-0006`     | P                            | P                                     |                    N/A | P                               | P       |             |
| `reg-coordinated-0007`   | P                            | P                                     |                    N/A | P                               | P       |             |
| `gen-synthetic-0003`     | P                            | P                                     |                    N/A | P                               | P       |             |
| `gen-synthetic-0005`     | P                            | P                                     | P                      | P                               | P       |             |

### Parser-Default Summary

* **Cases passed:11**
* **Cases with non-blocking observations:2**
* **Cases with defects:1**
* **Cases not tested:0**
* **Routine rewind needed anywhere:No** Yes / No
* **Any harmful source-boundary merging:No** Yes / No
* **Any unjustified overlong chunks:No** Yes / No
* **Any unjustified underdense chunks:No** Yes / No
* **Parser-default summary:Stellar**

## Structural Fixture

Test text:

```text
# Main Title

Intro text.

## First Section

Section body.

## Second Section

Closing body.
```

| Check                                                                            | Result | Notes                                                                       |
| -------------------------------------------------------------------------------- | -----: | --------------------------------------------------------------------------- |
| Active label progresses from `Main Title` to `First Section` to `Second Section` |   P    |                                                                             |
| Active path retains `Main Title` under both H2 sections                          |   P    |                                                                             |
| Header chunks are identifiable as headers                                        |   P    |                                                                             |
| Orientation cue does not conceal or mask a chunk defect                          |   O    | It's being concealed by the ghost chunk sometimes instead, css work implied |
| Structural metadata remains synchronized during navigation/playback              |   P    |                                                                             |

* **Structural fixture overall:** `P` / `O` / `D` / `NT`
* **Structural fixture notes:small technical debt for validation purposes, since it's a simple fix better not postpone it**

## Mandatory Rule-Based Fallback

* **Application restarted with `RSVP_CHUNKER_MODE=rule_based`:Yes** Yes / No
* **Fallback mode visibly confirmed:** Yes / No

| Case                | Deterministic | Ordered | Readable | Width-safe | Known split judgment                                                     | Overall | Notes |
| ------------------- | ------------: | ------: | -------: | ---------: | ------------------------------------------------------------------------ | ------: | ----- |
| `dev-names-0001`    |       P       |    P    |    P     |     P      | `Dr. Mira Patel`: acceptable limitation                                  |    P    |       |
| `dev-negation-0003` |       P       |    P    |    P     |     P      | `back down`: acceptable limitation                                       |    P    |       |
| `dev-source-0005`   |       P       |    P    |    P     |     P      | N/A                                                                      |    P    |       |
| `dev-width-0006`    |       P       |    P    |    P     |     P      | N/A                                                                      |    P    |       |

### Fallback Summary

* **Output was repeatably deterministic:Yes** Yes / No / Inconclusive
* **The two characterized splits are acceptable fallback limitations:Yes** Yes / No / Mixed
* **Any acceptance-blocking fallback defect:No** Yes / No
* **Fallback remains usable:Yes** Yes / No / Inconclusive
* **Fallback summary:Acceptable**

## Defect List
Pushed separately to docs/validation/s030_observed_semantic_structural_defects.md


## Final Disposition

* **Disposition:passed** `passed` / `partially_passed` / `failed` / `inconclusive`
* **Parser-default result:passed**
* **Structural fixture result:passed**
* **Rule-based fallback result:passed**
* **Acceptance-blocking defects:passed**
* **Non-blocking observations:passed**
* **New evaluation-case candidates:passed**
* **Cases not completed or evidence missing:passed**
* **Rationale for disposition:only acceptable and non-blocking defects encountered****

### Management Handoff

* **S-030 recommended next state:close the slice and prepare s31**
* **Human follow-up required:none**
* **Narrow stabilization authorized:Yes** Yes / No
* **S-031 remains inactive:depends on the prompt wording** Yes
* **Additional notes:**
