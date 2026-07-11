# S-030 Semantic Output and Structural Integrity Validation

## Automated Characterization

The repeatable characterization command is:

```bash
python scripts/characterize_s030_semantic_integrity.py --check
```

The committed [machine-readable record](../../evaluation/semantic_integrity/s030_characterization.json) covers all 22 visible project-owned cases under parser-assisted and rule-based chunking plus a fixed H1/H2 structural fixture.

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
