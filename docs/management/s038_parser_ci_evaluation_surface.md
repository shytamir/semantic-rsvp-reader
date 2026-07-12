# S-038A Parser CI Evaluation-Surface Coverage

## Status

`PROVISIONAL`, inactive, and unauthorized. S-038 must be separately dispositioned before S-038A may be activated. GitHub issue #25 is detailed authority; GitHub issue #23 is the bounded implementation work governed by this slice.

## Objective

Close the pinned standard-profile Parser CI coverage gap for the S-024/S-037 evaluation surface before S-039 application-service and document-contract work begins.

## Dependency And Initiating Reason

S-038A is the intended immediate successor to S-038 and predecessor to S-039. S-037 changed and characterized parser-sensitive evaluation tooling, but the current Parser CI workflow does not trigger on or execute that surface under the pinned `standard` environment. Incidental Core CI coverage is not the authoritative parser-sensitive gate.

This is CI and evidence-integrity maintenance, not evidence of a parser regression or authority to change parser behavior, evaluation policy, or frozen results.

## In Scope

- Implement the existing acceptance criteria in GitHub issue #23.
- Add the specified S-024/S-037 workflow path triggers and manual dispatch.
- Run the two affected evaluation test files under the pinned Python 3.12 standard profile.
- Reproduce the committed S-037 characterization through its existing check command.
- Preserve existing Parser CI dependency assertions, integration tests, S-030 characterization, and parser-default smoke coverage.
- Update only directly affected CI/testing documentation.

## Required Evidence

- Repository and workflow validation.
- The affected tests passing under the pinned standard profile.
- The committed S-037 characterization reproducing successfully.
- An immediately available remote Parser CI result, or accurate pending status without waiting.

## Human Handoff

Review the implementation evidence and choose the S-038A disposition. This is a management acceptance step, not a rendered-behavior judgment.

## Permissible Narrow Work

Modify only the existing Parser CI workflow and directly required documentation or focused tests needed to preserve the recorded contracts.

## Non-Goals

No new workflow job or dependency; no parser, optimizer, fallback, application, or browser behavior change; no evaluation-logic, substantive assertion, characterization-result, frozen-evidence, manifest, hash, annotation, or private A/B change; no broad CI redesign; no issue #24 implementation; and no S-039 or later activation or implementation.

## Completion Boundary

Issue #23's acceptance criteria pass under the pinned standard-profile Parser CI gate, the committed S-037 characterization is reproducible, and the human records a disposition. Issue #23 closes only after implementation commits and required evidence are recorded. S-039 does not activate automatically.
