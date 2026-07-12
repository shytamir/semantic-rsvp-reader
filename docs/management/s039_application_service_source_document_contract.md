# S-039 Application-Service Boundary and Source-Document Contract

## Status

`AWAITING_HUMAN_VALIDATION`, active, and owned by Human. The bounded S-039A implementation evidence is recorded in [S-039 validation](../validation/s039_application_service_source_document_contract.md). GitHub issue #2 is closed with pushed implementation evidence. S-040 through S-043 remain provisional, inactive, and unauthorized.

## Objective

Establish a project-owned application-service boundary for schedule generation and a minimal source-document contract for later ingestion and continuity work.

## Dependency And Initiating Reason

Depends on S-038A. Current Flask handling needs a narrow injectable seam before additional document sources are introduced.

## In Scope

- Define a backend-neutral source-document record with stable identity, source type, text, supported structure, and bounded provenance.
- Extract schedule generation behind an injectable application service while preserving API behavior and fallback policy.
- Record compatibility and failure contracts for later slices.
- Track GitHub issue #2, **S-039A Extract RSVP schedule generation into an injectable application service**, as the bounded service-extraction item within S-039.

## Codex Preparation

Characterization confirmed that `ScheduleService` already owns framework-independent schedule generation, performs normalization and segmentation once, accepts the existing `Chunker` protocol, and attaches timing, display-state, navigation, and structure metadata. `/api/ingest`, `/api/chunk`, and `/api/schedule` already delegate through the configured service. S-039 preserves those paths and the parser-assisted default with mandatory automatic rule-based fallback.

The missing contract delta is limited to an immutable `SourceDocument` record. The record preserves source text, derives deterministic identity from its versioned source type and normalized text, exposes the supported H1/H2 structure already recognized by the project, and stores at most eight sorted string provenance fields. Provenance does not alter document identity. The existing `app.config["SCHEDULE_SERVICE"]` seam already lets route tests substitute a service without altering the hash-registered S-026 integration files.

Compatibility and failure contracts:

- existing HTTP request and response shapes remain unchanged;
- source text follows the existing normalization contract before identity and scheduling;
- unsupported structure remains text rather than gaining new format semantics;
- invalid or oversized source type and provenance metadata fail before scheduling;
- injected services affect orchestration only and do not change configured chunking health identity.

## Human Handoff

In plain language, review only whether a stable identity derived from source type plus normalized text, together with supported headings and bounded provenance, is sufficient groundwork for S-040 ingestion and S-041 continuity. Do not judge new formats, persistence, parser quality, or rendered reading behavior in this gate.

## Permissible Narrow Work

Refactor only the schedule-generation seam and directly required source-document plumbing.

## Non-Goals

No new ingestion format, accounts, database, cloud service, parser redesign, public API redesign, issue #24 implementation, or S-040 activation.

## Completion Boundary

The injectable service and document contract preserve behavior and are ready for S-040/S-041 consumers. S-039A is dispositioned within S-039; no successor activates automatically.
