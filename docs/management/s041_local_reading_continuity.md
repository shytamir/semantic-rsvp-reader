# S-041 Local Reading Continuity

## Status

`COMPLETED` as `passed` on 2026-07-13, pinned to human-evidence commit `a865f563b50b9fa62bc65cb8e618ddcac04b0c6f`. The human evidence remains verbatim in [S-041 validation](../validation/s041_local_reading_continuity.md), including the paste-box restoration observation. Application-owned continuity stores no source text; browser-managed form restoration does not authorize unrelated changes. GitHub issue #16 is closed. S-042 and S-043 remain provisional, inactive, and unauthorized.

## Objective

Preserve local reading position, recent documents, reader preferences, and appropriate session state using stable document identities.

## Dependency And Initiating Reason

Depends on S-040 delivering stable document records. Continuity must follow rather than invent the ingestion contract.

## In Scope

- Local persistence of position, recent-document references, preferences, and explicitly selected session state.
- Safe restoration, stale/missing-document behavior, reset/removal controls, and bounded retention.
- Privacy documentation for locally retained state.

## Codex Preparation

Characterization found schedule, position, breakpoints, speed, adaptation preference, session events, timers, drift recovery, and defect context were all transient. S-041 adds two separate version-1 browser-local stores: reader preferences, and per-document continuity keyed by the S-039 stable identity.

The preference record contains only speed level and adaptation enabled/disabled. Each document record contains identity, source type, a bounded display reference, clamped position, at most 64 breakpoints, and update time. Retention is limited to the 12 most recent documents for 90 days. Source text, defect contents, session events/telemetry, timers, drift-recovery state, playback state, and parser data are never stored.

Matching documents restore paused. Invalid positions and breakpoints clamp to the current schedule; corrupt, wrong-version, invalid, future-dated, and stale records are discarded deterministically. A missing source is never reconstructed from storage: the input screen remains paused and reports only the saved reference count until matching text is prepared or local data is removed.

## Human Handoff

Run the fixed protocol in [S-041 validation](../validation/s041_local_reading_continuity.md) for reopen, paused resume, preferences, reset, per-document removal, full clearing, and missing-document behavior.

## Permissible Narrow Work

Fix reproduced local persistence, restoration, migration, privacy, or stale-state defects.

## Non-Goals

No accounts, cloud sync, analytics, backend database, cross-device identity, service worker, or offline application platform.

## Completion Boundary

Bounded local state restores predictably, can be cleared, and has documented privacy/retention behavior. No successor activates automatically.
