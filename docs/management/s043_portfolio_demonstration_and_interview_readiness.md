# S-043 Portfolio Demonstration and Interview Readiness

## Status

S-043 remains the current parent slice under open GitHub issue #18, but its Human-owned rehearsal is suspended while the ordered [S-043A1 → S-043A2 → S-043A3 blocking chain](s043a_epub_preparation_chain.md) completes. Only S-043A1 is active at `READY_FOR_IMPLEMENTATION`, owned by Codex under issue #27. No rehearsal or readiness disposition has been performed.

The original repository-owned demonstration package remains immutable historical evidence at commit `2d16a91fdfc95c384094de5f6cf0d59f666dcd8c`. It is not the active rehearsal target during suspension and has not been replaced. No release tag was created.

Prepared materials are indexed by the [portfolio demonstration package](../demonstration/README.md); the fixed gate is the [S-043 rehearsal record](../validation/s043_portfolio_demonstration_rehearsal.md).

## Objective

Prepare one reproducible, accurately documented portfolio demonstration of the validated local-first RSVP reader, together with a bounded fallback package and a fixed human rehearsal protocol, without expanding into external beta distribution or production deployment.

## Dependency And Initiating Reason

Depends on successful S-037 through S-042 evidence and the S-036 readiness disposition.

The intended audience is a technical interviewer or repository reviewer. The sole operator and tester remains the project owner using the established validated environments:

* the documented Windows development environment;
* the existing mobile device, operating system, and browser combination used for prior qualitative validation.

No external tester cohort, hosted public service, participant evidence collection, or beta recruitment is planned.

## In Scope

* Pin one reproducible portfolio-demonstration release identity using an immutable commit SHA or tag.
* Verify that the documented Windows setup and startup path work without undocumented local state.
* Prepare a deterministic short demonstration suitable for a constrained interview slot.
* Prepare a fuller technical demonstration covering the product, architecture, validation discipline, privacy boundaries, and known limitations.
* Demonstrate supported pasted-text and EPUB reading through the existing application.
* Demonstrate playback, navigation, breakpoints, contents navigation, and paused local continuity where supported.
* Demonstrate at least one representative bounded failure without exposing sensitive or third-party source material.
* Prepare a minimal fallback package for use if the live demonstration cannot be completed.
* Ensure repository-facing claims are supported by committed evidence and do not overstate maturity or validation.
* Prepare a fixed human rehearsal protocol and record one final portfolio-readiness disposition.

## Demonstration Release Identity

The demonstration must be tied to one immutable commit SHA or repository tag.

Record:

* the exact release identity;
* supported Python and dependency profile;
* startup command;
* tested Windows environment;
* tested mobile/browser environment;
* expected CI state;
* supported source formats;
* known limitations;
* rollback or withdrawal procedure if the demonstration build is later found unreliable.

Once declared ready for rehearsal, the pinned demonstration identity must not change except to repair a reproduced demonstration blocker.

## Demonstration Protocol

Prepare two deterministic variants.

### Short Demonstration

Target duration: approximately three to five minutes.

The short path should:

1. Introduce the problem and product objective.
2. Start or present the running local application.
3. Load a prepared text sample.
4. Demonstrate RSVP playback and semantic chunk presentation.
5. Show one navigation or continuity feature.
6. Load or briefly demonstrate a supported EPUB.
7. Close with the project’s architecture, validation discipline, and principal limitation.

### Full Technical Demonstration

Target duration: approximately ten minutes.

The full path should:

1. Identify the pinned release and validated environment.
2. Start the Flask application using the documented procedure.
3. Show the application health and configured chunking identity.
4. Load a prepared plain-text or Markdown sample.
5. Demonstrate playback, timing, manual navigation, and breakpoints.
6. Demonstrate local paused continuity without source-text persistence.
7. Load a project-owned representative EPUB.
8. Demonstrate canonical EPUB identity, contents navigation, heading jumps, and paused resume.
9. Demonstrate one documented unsupported or malformed-input failure.
10. Summarize the source-document contract, parser-assisted path, deterministic fallback, testing model, privacy boundary, and known limitations.

The protocol must not depend on private evaluation material, undocumented shell history, external network services, or sensitive source documents.

## Portfolio Narrative

Prepare or verify concise repository material covering:

* the user problem and intended reading workflow;
* why semantic chunking and RSVP presentation are technically significant;
* the Flask, HTML, CSS, and JavaScript application architecture;
* the project-owned `SourceDocument` and schedule-service boundaries;
* parser-assisted chunking and mandatory deterministic fallback;
* local continuity and source non-persistence;
* EPUB ingestion and bounded structural navigation;
* automated, browser, and human validation;
* security and privacy constraints;
* known limitations and deliberately unproven claims.

Prefer links to existing authoritative documentation over duplicated explanations.

## Fallback Package

Prepare a bounded fallback package containing only project-owned or otherwise permitted material:

* one known-good text sample;
* one representative EPUB fixture;
* screenshots of key application states;
* concise architecture or repository-orientation material;
* terminal CI evidence or links to committed validation records;
* optionally, a short prerecorded demonstration.

Fallback materials supplement the live demonstration. They do not create a new application surface or distribution mechanism.

## Repository Presentation Checks

Verify only interview-relevant repository surfaces:

* README setup and capability statements are current;
* management status is understandable;
* license and security policy are visible;
* no credentials, private evaluation material, sensitive source text, or local artifacts are committed;
* known limitations are explicit;
* issue and validation history support the claims made during the demonstration;
* stale prototype language does not materially contradict the demonstrated state.

This scope does not authorize broad documentation restructuring, repository beautification, or unrelated maintenance.

## Evidence Boundary

Evidence is limited to:

* reproducible setup and startup results;
* automated test and GitHub Actions results;
* successful execution of the fixed demonstration protocols;
* screenshots or fallback artifacts;
* observed demonstration blockers or presentation friction;
* the human rehearsal disposition.

No telemetry, analytics, participant data, reading-history collection, source-content collection, or external user research is included.

## Human Handoff

The project owner performs the final rehearsal.

Verify:

1. The pinned release can be checked out or opened in the intended Windows environment.
2. Setup and startup succeed using only committed instructions.
3. The short demonstration can be completed within its intended duration.
4. The full technical demonstration can be completed without undocumented recovery steps.
5. The representative text and EPUB paths behave as documented.
6. Contents navigation, heading jumps, and paused continuity remain coherent.
7. The established mobile/browser path still supports the critical EPUB reading workflow.
8. Every spoken or displayed technical claim is supported by committed evidence.
9. The fallback package can replace a failed live demonstration without exposing private material.
10. No hidden dependency, sensitive source, credential, or private evaluation asset is required.
11. Known limitations can be explained clearly without undermining the demonstrated value.
12. Any observed blocker or presentation friction is recorded before disposition.

Record exactly one disposition:

* `portfolio_demo_ready`
* `ready_with_known_limitations`
* `rehearsal_blocked`
* `documentation_blocked`
* `inconclusive`

Codex may prepare the demonstration materials, protocol, and objective evidence but may not declare the human rehearsal gate passed.

## Permissible Narrow Work

* Fix reproduced defects that block the approved demonstration protocol.
* Correct setup, startup, validation, or documentation defects that make the demonstration non-reproducible.
* Correct misleading or stale claims directly relevant to the demonstration.
* Adjust fallback materials when required to match the pinned release.
* Preserve existing product, parser, timing, playback, navigation, continuity, ingestion, and privacy contracts unless a reproduced demonstration blocker requires a narrowly authorized correction.

## Non-Goals

* No external beta recruitment or participant trial.
* No public hosted demonstration.
* No production deployment or production-readiness claim.
* No accounts, authentication, analytics, telemetry, database, cloud sync, or scaling architecture.
* No native packaging, installer, desktop wrapper, or mobile application.
* No new distribution mechanism.
* No broad UI redesign or speculative interview feature.
* No repository-wide cleanup.
* No parser retuning, chunking-rule expansion, timing redesign, or playback redesign.
* No public performance, comprehension, educational, medical, accessibility, or market claims beyond committed evidence.
* No private evaluation material in Git.
* No automatic activation of a successor phase.

## Completion Boundary

S-043 completes only after:

* one immutable demonstration release identity is recorded;
* setup and startup are reproducible in the intended Windows environment;
* the short and full demonstration protocols are prepared;
* the fallback package is complete and matches the pinned release;
* relevant automated and remote validation evidence is recorded;
* the human rehearsal has received one permitted disposition;
* any remaining limitations are documented accurately;
* repository management state and the S-043 issue reflect the final result.

No further phase activates automatically.
