# S-041 Local Reading Continuity

## Status

`READY_FOR_IMPLEMENTATION`, active, and owned by Codex. GitHub issue #16 is detailed authority. S-042 and S-043 remain provisional, inactive, and unauthorized.

## Objective

Preserve local reading position, recent documents, reader preferences, and appropriate session state using stable document identities.

## Dependency And Initiating Reason

Depends on S-040 delivering stable document records. Continuity must follow rather than invent the ingestion contract.

## In Scope

- Local persistence of position, recent-document references, preferences, and explicitly selected session state.
- Safe restoration, stale/missing-document behavior, reset/removal controls, and bounded retention.
- Privacy documentation for locally retained state.

## Codex Preparation

Characterize transient state, define minimal versioned local records, and prepare deterministic restore/reset/migration tests without unnecessarily storing text.

## Human Handoff

Validate reopen, resume, reset, missing-document, and preference continuity across local sessions.

## Permissible Narrow Work

Fix reproduced local persistence, restoration, migration, privacy, or stale-state defects.

## Non-Goals

No accounts, cloud sync, analytics, backend database, cross-device identity, service worker, or offline application platform.

## Completion Boundary

Bounded local state restores predictably, can be cleared, and has documented privacy/retention behavior. No successor activates automatically.
