# S-039 Application-Service Boundary and Source-Document Contract

## Status

Provisional post-S-038 scope. Not active or authorized.

## Objective

Establish a project-owned application-service boundary for schedule generation and a minimal source-document contract for later ingestion and continuity work.

## Dependency And Initiating Reason

Depends on S-038. Current Flask handling needs a narrow injectable seam before additional document sources are introduced.

## In Scope

- Define a backend-neutral source-document record with stable identity, source type, text, supported structure, and bounded provenance.
- Extract schedule generation behind an injectable application service while preserving API behavior and fallback policy.
- Record compatibility and failure contracts for later slices.
- Track GitHub issue #2, **S-039A Extract RSVP schedule generation into an injectable application service**, as the bounded service-extraction item within S-039.

## Codex Preparation

Characterize current service paths and serialization, propose the smallest contract, and add focused compatibility evidence.

## Human Handoff

Review whether identity and provenance are sufficient for local reading without precommitting to unsupported formats or storage.

## Permissible Narrow Work

Refactor only the schedule-generation seam and directly required source-document plumbing.

## Non-Goals

No new ingestion format, accounts, database, cloud service, parser redesign, public API redesign, or issue #2 implementation before S-039 activation.

## Completion Boundary

The injectable service and document contract preserve behavior and are ready for S-040/S-041 consumers. S-039A is dispositioned within S-039; no successor activates automatically.
