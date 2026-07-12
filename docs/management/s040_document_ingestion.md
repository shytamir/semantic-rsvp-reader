# S-040 Plain Text, Markdown, and Bounded Clean-HTML Ingestion

## Status

`AWAITING_HUMAN_VALIDATION`, active, and owned by Human. GitHub issue #15 remains open as detailed authority. Automated evidence and the fixed representative-file protocol are recorded in [S-040 validation](../validation/s040_document_ingestion.md). S-041 through S-043 remain provisional, inactive, and unauthorized.

## Objective

Add local ingestion for plain text, Markdown, and a bounded clean-HTML subset through the source-document contract.

## Dependency And Initiating Reason

Depends on S-039 so format adapters do not couple directly to Flask or schedule policy.

## In Scope

- Plain-text and Markdown import with source metadata and supported heading structure.
- Bounded clean HTML/article ingestion when normalization is safe and deterministic.
- Explicit format limits, validation, failure messages, and representative fixtures.

## Codex Preparation

The bounded contract accepts `.txt`, `.md`, `.markdown`, `.html`, and `.htm` local byte payloads encoded as UTF-8 or UTF-8 with a BOM. Each source is limited to 1,000,000 bytes and 20,000 lines. Clean HTML is additionally limited to 10,000 elements and 32 nesting levels, rejects active/embedded content, event-handler attributes, mismatched markup, and elements outside the documented article subset, and extracts text plus H1/H2 headings without rendering HTML.

All adapters return the accepted immutable `SourceDocument` with source type, source text, deterministic normalized-text identity, supported H1/H2 structure, and four bounded provenance fields: adapter version, encoding, media type, and source name. They do not fetch URLs or import Flask, persistence, parser, or schedule policy.

## Human Handoff

Follow the fixed protocol in [S-040 validation](../validation/s040_document_ingestion.md). Judge only extracted text, supported headings, bounded provenance, reader-path readability, and the named failure messages.

## Permissible Narrow Work

Fix reproduced parsing, metadata, structure, safety, or compatibility defects within bounded formats.

## Non-Goals

No PDF, EPUB, full Markdown rendering, arbitrary web scraping, rich-document renderer, remote URL fetch, or parser retuning.

## Completion Boundary

Supported files produce validated source-document records and remain readable with limitations documented. No successor activates automatically.
