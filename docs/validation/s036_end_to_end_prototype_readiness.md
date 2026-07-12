# S-036 End-to-End Prototype Readiness Validation

## Gate Selection

S-036 applies all six conditional gates from the [QA strategy](../qa/strategy.md):
repository, core, standard, change-specific, human, and disposition. Automated
preparation establishes the first four. The human and disposition gates remain
pending and cannot be passed by this record's preparation.

Automated preparation ran against source checkout `9329776395047463b02048eee31506d65e679bcf` on Windows. The committed handoff adds documentation and management state only; the human must record the final target commit.

## Clean Environment Identities

Both disposable environments were created explicitly with the managed Python
3.12 runtime. The sandbox account did not expose the Windows `py` launcher, so
the documented `py -3.12` command was not re-exercised by automation; it already
passed human validation in S-035A.

| Profile | Python and dependencies | `/health` identity | Consistency and smoke |
| --- | --- | --- | --- |
| `standard` | Python `3.12.13`; Flask `3.1.3`; pytest `9.1.1`; Click `8.1.8`; spaCy `3.7.5`; `en-core-web-sm` `3.7.1` | configured/active `parser_assisted`; provider `spacy:3.7.5/en_core_web_sm:3.7.1`; provider available; fallback `rule_based` | `pip check` passed; parser-assisted smoke passed |
| `core` | Python `3.12.13`; Flask `3.1.3`; pytest `9.1.1`; parser packages absent | configured/active `rule_based`; provider absent with reason `not_configured`; fallback `rule_based` | `pip check` passed; explicit rule-based smoke passed |

The first core test invocation incorrectly set `RSVP_CHUNKER_MODE=rule_based`
before the suite and produced two expected default-mode assertion failures. It
was discarded as operator error. The corrected invocation followed the
environment contract: run the dependency-light suite without the override,
then set the override for health and smoke evidence.

## Automated Readiness Evidence

| Gate/evidence | Result |
| --- | --- |
| Clean standard suite | `292 passed` |
| Clean core suite | `286 passed`; parser-only integration and standard-profile API files excluded as specified by the environment contract |
| S-030 semantic/structural characterization | Reproducible; hard invariants passed |
| S-031 playback/adaptation characterization | Reproducible; invariants passed |
| S-032 navigation/interaction characterization | Reproducible; invariants passed |
| S-033 presentation/accessibility characterization | Reproducible; invariants passed |
| S-034 synthetic evidence-capture characterization | Reproducible and complete |
| S-035 service/fallback characterization | Reproducible and complete |
| Visible chunking corpus | 22 cases passed |
| Frozen rule-based baseline | Reproducible |
| Repository integrity | Passed |
| Markdown links | Passed |
| Slice-age archive policy | Passed; no pending work |
| JavaScript syntax | Local execution skipped because Node/nodejs is unavailable; the checker reported the skip. Node-backed syntax remains an enforced Ubuntu CI core-job check and is not claimed as a local pass. |
| Compact GitHub Actions | CI run [29198184766](https://github.com/shytamir/semantic-rsvp-reader/actions/runs/29198184766) passed for preparation-base commit `9329776`; observed `integrity` and `core` jobs both succeeded, including Node-backed JavaScript syntax in `core`. Path filtering did not schedule a parser job for that documentation/archive commit; clean local standard evidence above covers the pinned parser path. |

Completed S-030 through S-035B human dispositions remain their own evidence
authorities. This readiness record does not reinterpret checklist details or
reopen the frozen S-023/S-024 scientific work.

## Known Prototype Limitations

- The Flask development server and source checkout are for local prototype demonstration, not production hosting or a production-readiness claim.
- spaCy remains a provisional, pinned provider with installation/platform weight; the deterministic rule-based path remains mandatory fallback.
- The accepted rule-based fallback may split `Dr. Mira Patel` and `back down`; S-030 classified these as readable, non-blocking fallback limitations.
- Long-word, quote-closure, and parenthetical-closure observations remain recorded semantic evaluation evidence, not authorization for parser retuning or new rules.
- Open issue #19 tracks a low-priority phone-landscape obstruction where the defect count can overlap the coarse-seek hit lane near 50%; accepted seek semantics are unchanged.
- Rendered browser behavior remains human-controlled. Minimal browser regression automation is planned for inactive S-038 and is not part of S-036 preparation.
- Accounts, persistence/cloud sync, analytics, broad document ingestion, native packaging, production infrastructure, and public performance claims remain outside the stabilized prototype.

## Fixed Human Readiness Session

Use the clean `standard` profile and an intended demo phone/browser. Record the
target commit, Python/dependency identity, device, operating system, browser,
viewport, configured/active chunker state, and each step outcome.

1. Start the app in parser-default mode. Confirm `/health` reports configured and active `parser_assisted`, the pinned spaCy/model identity, and `rule_based` fallback.
2. Load one general long-form validation sample and one S-030 semantic/structural case. Read at default `1.0x`; confirm representative chunks, headings/structure, protected spans, and the passed S-029 pacing remain practical.
3. Exercise play, pause/resume, speed change, background/foreground return, completion/reset, and a fresh session. Confirm lifecycle and conservative adaptation remain understandable and stable.
4. Exercise previous/next gestures, coarse progress seeking, breakpoint creation/traversal, drift recovery/cancellation, ghost context, and structural orientation.
5. Check portrait and landscape presentation, a narrow viewport, long chunks/tokens, quote/parenthetical cues, focus visibility, overlays, and safe-area behavior. Specifically observe whether issue #19 prevents the readiness session; do not fix it in this gate.
6. Submit one synthetic defect report. Confirm useful context and session state are captured without private text, review it locally, then delete the generated report and record deletion.
7. Stop the standard app. Start the clean `core` profile with explicit `RSVP_CHUNKER_MODE=rule_based`; confirm `/health` and smoke behavior demonstrate dependency-light fallback, then read a representative sample.
8. Review the known limitations above and confirm setup, indexes, QA links, and demo instructions are sufficient for the intended bounded prototype demonstration.

For each step record `passed`, `partially_passed`, `failed`, `skipped`, or
`inconclusive`, plus any observation, blocking status, and issue reference.

## Final Human Disposition

Choose exactly one:

- `ready`
- `ready_with_limitations`
- `not_ready`
- `inconclusive`

Record the rationale, acceptance-blocking defects, accepted limitations, issue
links, and confirmation that generated/private defect evidence was deleted or
retained outside Git. This is a prototype demo/beta disposition, not a
production-readiness or public-performance claim.
