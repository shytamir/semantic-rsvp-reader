# S-042 EPUB Ingestion and Long-Document Navigation

## Status

S-042 is split into bounded lettered scopes under open umbrella issue #17. Only S-042A is active at `READY_FOR_IMPLEMENTATION`, owned by Codex. S-042B and S-042C are provisional, inactive, and unauthorized.

## Objective

Add EPUB ingestion and lightweight structural navigation after ingestion and continuity foundations are stable.

## Dependency And Initiating Reason

Depends on S-040 ingestion contracts and S-041 continuity. EPUB introduces ordered multipart content and long-document orientation needs.

## In Scope

- Bounded EPUB import with ordered readable content, metadata, headings, and supported structure.
- Heading navigation and a lightweight contents view.
- Resume behavior and deterministic handling of unsupported or malformed features.

## Lettered Scope Sequence

### S-042A: EPUB Ingestion Foundation

`READY_FOR_IMPLEMENTATION`, active, and owned by Codex. Define a deliberately limited EPUB subset; safely validate the ZIP container and required EPUB metadata; extract readable spine content deterministically; preserve supported headings and bounded provenance; produce stable `SourceDocument` identity; and prove scheduling and continuity compatibility. This objectively verifiable foundation has no human gate.

### S-042B: Contents And Heading Navigation

`PROVISIONAL`, inactive, and unauthorized. Own a lightweight contents view and heading navigation using S-042A structure. It does not activate automatically.

### S-042C: Long-Document Reading And Resume Validation

`PROVISIONAL`, inactive, and unauthorized. Own rendered long-document behavior, qualitative orientation, and resume validation after navigation exists. It does not activate automatically.

## Codex Preparation

For S-042A only, define the supported subset, prepare licensed/project-owned fixtures, characterize spine/heading mapping, and test identity, scheduling, and continuity integration.

## Human Handoff

No human gate applies to S-042A. Human reading and navigation review belongs to a separately activated successor.

## Permissible Narrow Work

Fix reproduced ordering, extraction, metadata, navigation, continuity, or bounded presentation defects.

## Non-Goals

S-042A adds no contents UI, heading navigation, new resume controls, rendered ebook behavior, DRM handling, full CSS fidelity, PDF support, application surface, annotation platform, library service, or native packaging.

## Completion Boundary

The supported EPUB subset is readable and navigable with explicit limitations and stable continuity. No successor activates automatically.
