# S-040 Plain Text, Markdown, and Bounded Clean-HTML Ingestion

## Status

Provisional post-S-039 scope. Not active or authorized.

## Objective

Add local ingestion for plain text, Markdown, and a bounded clean-HTML subset through the source-document contract.

## Dependency And Initiating Reason

Depends on S-039 so format adapters do not couple directly to Flask or schedule policy.

## In Scope

- Plain-text and Markdown import with source metadata and supported heading structure.
- Bounded clean HTML/article ingestion when normalization is safe and deterministic.
- Explicit format limits, validation, failure messages, and representative fixtures.

## Codex Preparation

Define accepted encodings and limits, characterize normalization, prepare fixtures, and verify records feed the existing reader path.

## Human Handoff

Open representative files and judge whether text, headings, provenance, and failure messages support the intended workflow.

## Permissible Narrow Work

Fix reproduced parsing, metadata, structure, safety, or compatibility defects within bounded formats.

## Non-Goals

No PDF, EPUB, full Markdown rendering, arbitrary web scraping, rich-document renderer, remote URL fetch, or parser retuning.

## Completion Boundary

Supported files produce validated source-document records and remain readable with limitations documented. No successor activates automatically.
