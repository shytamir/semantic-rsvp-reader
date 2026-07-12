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

Pulled latest commit: b38e2d5. Performed clean venv install per standard profile instructions in envirionment contract successfully with all tests green and no errors or warnings.
Python v3.12.10:0cc8128
pip list json result:
```json
[{"name": "annotated-doc", "version": "0.0.4"}, {"name": "annotated-types", "version": "0.7.0"}, {"name": "blinker", "version": "1.9.0"}, {"name": "blis", "version": "0.7.11"}, {"name": "catalogue", "version": "2.0.10"}, {"name": "certifi", "version": "2026.6.17"}, {"name": "charset-normalizer", "version": "3.4.9"}, {"name": "click", "version": "8.1.8"}, {"name": "cloudpathlib", "version": "0.24.0"}, {"name": "colorama", "version": "0.4.6"}, {"name": "confection", "version": "0.1.5"}, {"name": "cymem", "version": "2.0.13"}, {"name": "en-core-web-sm", "version": "3.7.1"}, {"name": "Flask", "version": "3.1.3"}, {"name": "idna", "version": "3.18"}, {"name": "iniconfig", "version": "2.3.0"}, {"name": "itsdangerous", "version": "2.2.0"}, {"name": "Jinja2", "version": "3.1.6"}, {"name": "langcodes", "version": "3.5.1"}, {"name": "markdown-it-py", "version": "4.2.0"}, {"name": "MarkupSafe", "version": "3.0.3"}, {"name": "mdurl", "version": "0.1.2"}, {"name": "murmurhash", "version": "1.0.15"}, {"name": "numpy", "version": "1.26.4"}, {"name": "packaging", "version": "26.2"}, {"name": "pip", "version": "25.0.1"}, {"name": "pluggy", "version": "1.6.0"}, {"name": "preshed", "version": "3.0.13"}, {"name": "pydantic", "version": "2.13.4"}, {"name": "pydantic_core", "version": "2.46.4"}, {"name": "Pygments", "version": "2.20.0"}, {"name": "pytest", "version": "9.1.1"}, {"name": "requests", "version": "2.34.2"}, {"name": "rich", "version": "15.0.0"}, {"name": "setuptools", "version": "83.0.0"}, {"name": "shellingham", "version": "1.5.4"}, {"name": "smart_open", "version": "7.7.1"}, {"name": "spacy", "version": "3.7.5"}, {"name": "spacy-legacy", "version": "3.0.12"}, {"name": "spacy-loggers", "version": "1.0.5"}, {"name": "srsly", "version": "2.5.3"}, {"name": "thinc", "version": "8.2.5"}, {"name": "tqdm", "version": "4.68.4"}, {"name": "typer", "version": "0.26.8"}, {"name": "typer-slim", "version": "0.24.0"}, {"name": "typing_extensions", "version": "4.16.0"}, {"name": "typing-inspection", "version": "0.4.2"}, {"name": "urllib3", "version": "2.7.0"}, {"name": "wasabi", "version": "1.1.3"}, {"name": "weasel", "version": "0.4.3"}, {"name": "Werkzeug", "version": "3.1.8"}, {"name": "wrapt", "version": "2.2.2"}]
```
Samsung S23 Ultra
Android 16
Firefox 152
portrait
default chunker state (parser assisted fallback, no configured state)

1. Start the app in parser-default mode. Confirm `/health` reports configured and active `parser_assisted`, the pinned spaCy/model identity, and `rule_based` fallback.
human records `passed`
result: {"chunking":{"active_mode":"parser_assisted","configured_mode":"parser_assisted","fallback":"rule_based","provider":"spacy:3.7.5/en_core_web_sm:3.7.1","provider_available":true,"provider_reason":"available"},"status":"ok"}

2. Load one general long-form validation sample and one S-030 semantic/structural case. Read at default `1.0x`; confirm representative chunks, headings/structure, protected spans, and the passed S-029 pacing remain practical.
human records `passed`
Confirmed listed features remain practical.

3. Exercise play, pause/resume, speed change, background/foreground return, completion/reset, and a fresh session. Confirm lifecycle and conservative adaptation remain understandable and stable.
human records `passed`
Confirmed listed features remain understandable and stable.

4. Exercise previous/next gestures, coarse progress seeking, breakpoint creation/traversal, drift recovery/cancellation, ghost context, and structural orientation.
human records `passed`
Confirmed listed features displayed no observable regressions.

5. Check portrait and landscape presentation, a narrow viewport, long chunks/tokens, quote/parenthetical cues, focus visibility, overlays, and safe-area behavior. Specifically observe whether issue #19 prevents the readiness session; do not fix it in this gate.
human records `passed`
Confirmed listed features displayed no observable regressions. Issue #19 doesn't prevent the readiness session. Fix can remain in its current deferred state.

6. Submit one synthetic defect report. Confirm useful context and session state are captured without private text, review it locally, then delete the generated report and record deletion.
human records `passed`
Following synthetic report was recorded and deleted. It was confirmed to preserve displayed ID from the UI and the local review was observed as retaining useful context and session state successfully.
```markdown
# Semantic RSVP Defect Report

Report ID: defect_20260712_160324_52173a
Created at: 2026-07-12T16:03:24.445491Z

## Classification

Category: layout_or_visibility_issue
Severity: 2
Notes:
Synthetic

Preferred behavior:
Synthetic

## Reader State

Current index: 13
Sentence index: 2
Playback speed: 1x
Adaptation enabled: false

Current chunk:
without changing timing policy.

## Timing Context

Base duration ms: 1020
Effective duration ms: 1020
Playback speed: 1x
Duration source: schedule
Current syntactic hint: dense
Current content word count: 4
Character length: 31
In quote: false
Quote boundary: none
In parenthetical: false
Parenthetical depth: 0
Navigation progress percent: 100
Navigation paragraph index: 2

## Structural Context

- Active H1: 
- Active H2: 
- Active label: 
- Active path: none
- Is header chunk: false
- Header level: unknown

## Navigability Context

Previous displayed chunk:
- Index: 12
- Text: cancellation can be checked
- Duration ms: 870
- Progress percent: 91
- Paragraph index: 2

Breakpoints:
- Count: 1
- Current is breakpoint: false
- Previous breakpoint: 5
- Next breakpoint: unknown
- Indices: 5

## Drift Recovery Context

- Active: false
- Pending: false
- Target breakpoint: unknown
- Lead-in index: unknown
- Delay ms: 500
- Direction: 

Original sentence:
Third paragraph closes the stream so reset, end boundaries, and cancellation can be checked without changing timing policy.

Previous chunks:
- [10] "closes the stream" - 670ms base / 670ms effective - dense - 2 content word(s) - 17 chars - quote=false/none - parenthetical=false/0 - navigation=75%/p2
- [11] "so reset, end boundaries, and" - 900ms base / 900ms effective - dense - 4 content word(s) - 29 chars - quote=false/none - parenthetical=false/0 - navigation=83%/p2
- [12] "cancellation can be checked" - 870ms base / 870ms effective - dense - 2 content word(s) - 27 chars - quote=false/none - parenthetical=false/0 - navigation=91%/p2

Next chunks:
- none

## Session Summary

Event count: 35
Rewind count: 0
Pause count: 3
Speed change count: 3
Adaptation count: 1
Completed: true
Elapsed session ms: 333181
Estimated remaining chunks: 0
Average effective duration ms: 834
Last adaptation reason: smooth_run
Last adaptation direction: faster

## Client

User agent:
Mozilla/5.0 (Android 16; Mobile; rv:152.0) Gecko/152.0 Firefox/152.0

Viewport:
384x742

Display:
Reader width px: 368
Chunk scroll width px: 340
Chunk client width px: 340
Chunk may overflow: false
Layout context:
- Previous chunk visible: true
- Previous chunk text length: 27
- Active chunk text length: 31
- Viewport: 384x742
```

7. Stop the standard app. Start the clean `core` profile with explicit `RSVP_CHUNKER_MODE=rule_based`; confirm `/health` and smoke behavior demonstrate dependency-light fallback, then read a representative sample.
human records `passed`
New health state confirms fallback behavior after starting the clean core profile:
```json
{"chunking":{"active_mode":"rule_based","configured_mode":"rule_based","fallback":"rule_based","provider":null,"provider_available":false,"provider_reason":"not_configured"},"status":"ok"}
```
I was able to read a representative sample (first structural stream from S-030) without trouble.

8. Review the known limitations above and confirm setup, indexes, QA links, and demo instructions are sufficient for the intended bounded prototype demonstration.
human records `passed`
Known limitations reviewed. setup, indexes, QA links and demo instructions are sufficient for the intended bounded prototype demonstration.

For each step record `passed`, `partially_passed`, `failed`, `skipped`, or
`inconclusive`, plus any observation, blocking status, and issue reference.

## Final Human Disposition

Choose exactly one:

- `ready`
recorded `passed` on all human protocols, limitations accepted, no blocking defects, no new issues, synthetic defect record deletion confirmed, although it is preserved in this document for reference and automated validation purposes. I'm disposed to close the slice as successful for the purpose of advancing the prototype demo.