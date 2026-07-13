# S-042 EPUB Ingestion and Long-Document Navigation

## Status

S-042 is split into bounded lettered scopes under open umbrella issue #17. S-042A and S-042B completed as `passed` on 2026-07-13. S-042C is the sole active scope at `READY_FOR_IMPLEMENTATION`, owned by Codex. S-043 remains provisional, inactive, and unauthorized.

## Objective

Add bounded EPUB ingestion, minimal application integration, lightweight structural navigation, and stable local reading continuity after the document-ingestion and continuity foundations are established.

## Dependency And Initiating Reason

S-042 depends on the S-039 source-document contract, S-040 ingestion contracts, and S-041 browser-local continuity.

EPUB introduces:

* a bounded archive and package format;
* ordered multipart readable content;
* canonical document identity that must cross the server/browser boundary;
* long-document orientation and heading navigation;
* continuity behavior that must not reconstruct a missing local source.

## In Scope

* Bounded EPUB import with ordered readable content, required metadata, supported headings, and explicit limitations.
* Minimal application integration for selecting and preparing a supported local EPUB.
* Canonical `SourceDocument` identity and bounded source metadata propagated into the browser reader.
* Lightweight H1/H2 contents navigation derived from project-owned structure.
* Stable paused resume after the user reselects the same local EPUB.
* Deterministic handling of unsupported, malformed, missing, or changed sources.
* Human validation of representative long-document reading, navigation, resume behavior, and limitations.

## Lettered Scope Sequence

### S-042A: EPUB Ingestion Foundation

`COMPLETED` as `passed` on 2026-07-13.

S-042A added the deliberately limited framework-independent EPUB adapter. It safely validates the ZIP container and required EPUB metadata, extracts supported UTF-8 XHTML spine content deterministically, preserves supported H1/H2 structure and bounded provenance, produces stable `SourceDocument` identity, and proves schedule and continuity-contract compatibility.

Implementation and evidence are recorded in [S-042A validation](../validation/s042a_epub_ingestion_foundation.md). The supported subset and numeric limits are documented in [bounded EPUB ingestion](../features/epub_ingestion.md).

S-042A added no upload route, file-selection control, reader integration, contents interface, heading navigation, rendered ebook surface, or new resume control.

### S-042B: EPUB Reader Application Integration

`COMPLETED` as `passed` on 2026-07-13. Implementation and terminal stabilization evidence are recorded in [S-042B validation](../validation/s042b_epub_reader_application_integration.md).

S-042B owns the smallest application bridge required to read an S-042A-supported EPUB through the existing RSVP reader:

* add a minimal local EPUB file-selection control;
* add a dedicated bounded local file-transfer, ingestion, and scheduling path that passes EPUB bytes through the S-042A adapter;
* schedule the resulting `SourceDocument.text` through the existing application service;
* return the canonical document ID, source type, bounded display metadata, and existing schedule response data required by the browser;
* load the resulting schedule into the existing reader without changing playback semantics;
* use the server-provided EPUB identity for S-041 continuity rather than recomputing an `inline_text` identity;
* restore only after the user reselects an EPUB whose canonical document identity matches a saved reference;
* treat an EPUB whose extracted normalized text has changed as a different document, regardless of filename;
* expose explicit bounded failures for unsupported, malformed, encrypted, oversized, or unsafe EPUBs;
* provide focused route, integration, continuity, security, and browser-smoke evidence.

The dedicated EPUB path may use the S-042A twenty-megabyte container limit. It must not globally increase the existing request limit for unrelated JSON, text, defect, or schedule endpoints. Avoid encoding EPUB bytes into the existing JSON schedule contract.

S-042B has no human gate. It may complete as `passed` on objective evidence.

S-042B does not own:

* a contents panel or heading-jump interface;
* source-text or EPUB-byte persistence;
* automatic reconstruction of a missing source;
* filename-based continuity matching;
* recent-book or library-management UI;
* EPUB navigation-document or NCX interpretation;
* full ebook rendering;
* CSS, image, media, or layout fidelity;
* changes to chunking, timing, playback, drift recovery, adaptation, or breakpoint policy.

### S-042C: Lightweight Contents Navigation and Integrated EPUB Validation

`READY_FOR_IMPLEMENTATION`, active, and owned by Codex.

S-042C depends on completed S-042B application integration.

S-042C owns:

* a lightweight contents view derived only from supported project-owned H1/H2 structure;
* deterministic mapping from each displayed heading to its first corresponding scheduled chunk;
* heading jumps that cancel active playback or recovery activity and leave the reader paused at the destination;
* correct progress, structure-anchor, breakpoint, and continuity behavior after a jump;
* a clear empty state when no supported headings are present;
* keyboard and focus behavior required to operate the new contents control;
* preservation of the existing narrow-screen and accessibility baselines;
* integrated automated and browser validation;
* the fixed human EPUB reading, navigation, and resume protocol.

S-042C does not introduce a conventional ebook renderer, page view, chapter-text view, EPUB CSS rendering, images, media, EPUB navigation-document parsing, annotation platform, document library, or new playback semantics.

After implementation and automated validation, S-042C must stop at `AWAITING_HUMAN_VALIDATION`, owned by Human.

## Codex Preparation

### S-042B Preparation

Characterize the current pasted-text schedule path, browser continuity identity flow, request-size boundaries, and existing reader-state initialization before editing.

Reuse the S-039 application service, S-041 continuity contract, and S-042A adapter. Do not create a parallel scheduler, continuity store, source-document model, or generic document-upload framework.

The application integration must preserve the canonical EPUB `SourceDocument.document_id` and `source_type="epub"` across the server/browser boundary. Filename and provenance may support display, but must not replace canonical identity.

### S-042C Preparation

Use only S-042B’s supported browser response and the existing project-owned H1/H2 structure metadata.

Do not add a second EPUB parser or begin interpreting EPUB navigation documents merely to construct the contents view.

## Human Handoff

The human gate belongs only to S-042C.

Use fixed project-owned or otherwise permitted representative EPUBs and verify:

1. A supported EPUB can be selected and prepared through the documented local workflow.
2. Extracted chapter order and RSVP output are readable and consistent with the supported subset.
3. The lightweight contents view shows the expected supported H1/H2 headings in document order.
4. Forward and backward heading jumps land at the intended sections and remain paused.
5. Playback can begin normally after a heading jump.
6. Progress, active structure, and breakpoints remain coherent after navigation.
7. Leaving the reader and reselecting the same EPUB restores the saved position and breakpoints while remaining paused.
8. Renaming or recompressing an otherwise equivalent EPUB does not prevent identity-based restoration.
9. An EPUB with changed extracted text is treated as a different document.
10. A missing EPUB is not reconstructed from local continuity data.
11. An unsupported or malformed representative EPUB produces the documented bounded failure.
12. The contents control remains usable in the existing phone validation environment and the bounded browser-smoke environment.

Record exactly one disposition: `passed`, `partially_passed`, `failed`, or `inconclusive`.

Codex may prepare the protocol and automated evidence but may not declare this human gate passed.

## Permissible Narrow Work

* Fix reproduced EPUB application-integration defects within the S-042A supported subset.
* Fix reproduced document-identity, scheduling, heading mapping, continuity, navigation, focus, or bounded presentation defects.
* Adjust only the dedicated request handling required for the bounded EPUB path.
* Preserve existing text, Markdown, clean-HTML, parser, timing, playback, and continuity contracts.

## Non-Goals

* No PDF ingestion.
* No DRM bypass or encrypted-content handling.
* No full ebook renderer or conventional page-reading mode.
* No EPUB CSS, image, media, SVG, scripting, or layout fidelity.
* No EPUB navigation-document or NCX support unless separately authorized.
* No full Markdown rendering.
* No annotation platform, recent-document library, account, database, cloud sync, or library service.
* No generic upload framework.
* No native packaging or production hosting.
* No source-text or EPUB-byte persistence in browser-local continuity.
* No parser retuning, chunking-rule expansion, timing redesign, or playback redesign.
* No public performance, accessibility, educational, medical, or comprehension claims.

## Completion Boundary

S-042 completes only after:

* S-042A remains completed as `passed`;
* S-042B has objectively demonstrated bounded EPUB application integration using canonical document identity and stable continuity;
* S-042C has implemented lightweight supported-heading navigation;
* the fixed S-042C human protocol has received a recorded disposition;
* limitations and failure behavior are accurately documented;
* issue #17 is reconciled with the final S-042 evidence and disposition.

No S-043 scope activates automatically.
