# S-042 EPUB Ingestion and Long-Document Navigation

## Status

Provisional post-S-041 scope. Not active or authorized.

## Objective

Add EPUB ingestion and lightweight structural navigation after ingestion and continuity foundations are stable.

## Dependency And Initiating Reason

Depends on S-040 ingestion contracts and S-041 continuity. EPUB introduces ordered multipart content and long-document orientation needs.

## In Scope

- Bounded EPUB import with ordered readable content, metadata, headings, and supported structure.
- Heading navigation and a lightweight contents view.
- Resume behavior and deterministic handling of unsupported or malformed features.

## Codex Preparation

Define the supported EPUB subset, prepare licensed/project-owned fixtures, characterize spine/heading mapping, and test identity/continuity integration.

## Human Handoff

Read and navigate representative EPUBs and validate contents orientation, resume behavior, and limitations.

## Permissible Narrow Work

Fix reproduced ordering, extraction, metadata, navigation, continuity, or bounded presentation defects.

## Non-Goals

No PDF, DRM bypass, full ebook renderer, full CSS fidelity, full Markdown rendering, annotation platform, library service, or native packaging.

## Completion Boundary

The supported EPUB subset is readable and navigable with explicit limitations and stable continuity. No successor activates automatically.
