# S-028 Compact CI and Evidence Integrity

## Status

Scheduled immediately after S-027. S-027 remains the sole active slice.

## Objective

Add a compact automation layer that verifies the supported prototype modes and protects management and experimental evidence without introducing deployment infrastructure or an oversized CI platform.

This slice includes resolution of [GitHub issue #3: Finalize provisional integration record with S-026 commit identity](https://github.com/shytamir/semantic-rsvp-reader/issues/3).

## Planned CI Jobs

### Integrity

Add an explicit, repository-specific validator and CI job that verifies:

- committed JSON and JSONL syntax;
- targeted structure and schema expectations for stable freeze, evaluation, response, and integration records;
- exactly one active slice;
- agreement between `docs/management/STATUS.md` and roadmap `Now`;
- completed previous slices appear in `docs/management/HISTORY.md`;
- referenced evidence paths exist;
- Markdown links and validation-corpus integrity pass;
- frozen baselines and registered hashes remain valid;
- private blind identity material is absent;
- committed placeholders such as `pending_until_commit` are rejected;
- the integration-record work tracked by issue #3 is resolved.

Keep these checks direct and reviewable. Do not design a generalized management workflow engine or state machine.

### Core

Add a dependency-light job that:

- installs `requirements-core.txt`;
- runs the applicable dependency-light tests;
- runs JavaScript syntax validation;
- starts Flask in explicit `rule_based` mode;
- smoke-tests `/health`, `/api/chunk`, and `/api/schedule`.

### Parser

Add a pinned parser-default job that:

- installs the standard prototype environment;
- verifies spaCy `3.7.5` and `en-core-web-sm` `3.7.1`;
- runs parser integration and frozen-reference parity checks;
- starts Flask in parser-assisted default mode;
- smoke-tests `/health`, `/api/chunk`, and `/api/schedule`;
- exercises automatic rule-based fallback;
- confirms fallback logs exclude source text;
- confirms startup does not download a model at runtime.

## Workflow Hardening

The workflow should use:

- read-only workflow permissions;
- concurrency cancellation for superseded runs;
- reasonable job timeouts;
- pip caching;
- concise job summaries;
- safe path filtering for the heavier parser job.

Dependency reproducibility should use the existing readable requirement files, their existing pins, and Python 3.12 constraints where needed. Do not schedule a package-manager migration or an elaborate multi-platform lock system.

## Non-Goals

S-028 does not include:

- deployment or release automation;
- containers or hosted infrastructure;
- browser automation or frontend build tooling;
- a coverage threshold;
- automatic experiment-result regeneration;
- private blind data in GitHub Actions;
- qualitative experiment interpretation;
- optimizer tuning or provider ablation;
- native/mobile work;
- a broad overlapping security-scanner stack.

A later security pass may separately consider `pip-audit`, one secret scanner, `actionlint`, optional CodeQL, and grouped dependency updates.

## Completion Boundary

S-028 is planning-only until it becomes the active authorized slice. This document does not add workflows, validators, requirements, tests, or runtime behavior.
