# S-035 Service Surfaces and Fallback

## Objective

Validate Flask service contracts and both supported chunking modes under normal, unavailable-provider, and safe-fallback conditions.

## Initiating Reason

The prototype ships a parser-default standard environment plus a mandatory dependency-light rule-based path; their API, startup, logging, and dependency contracts need one focused service pass.

## In Scope

- `/health`, `/api/ingest`, `/api/chunk`, `/api/schedule`, validation samples, and bounded defect submission behavior.
- Parser-default startup, explicit `RSVP_CHUNKER_MODE=rule_based`, automatic fallback, state reporting, and response serialization without parser-native objects.
- Fallback reason-category logs without source text, pinned spaCy/model versions, no startup/runtime model download, and `requirements-core.txt` operation.

## Codex Preparation

Run compact CI-equivalent core/parser checks, focused API/fallback tests, dependency-pin verification, startup/smoke characterization, and log-privacy assertions.

## Human Handoff

Where useful, confirm normal parser-default and forced rule-based startup from documented commands and verify representative API-driven reading remains usable.

## Permissible Stabilization

Fix only a reproduced API contract, startup, configuration, fallback, serialization, logging-privacy, or dependency-documentation defect.

## Non-Goals

No deployment infrastructure, containers, hosted service, provider replacement, dependency migration, API redesign, accounts, or database.

## Completion Boundary

Both supported modes and fallback invariants pass automated checks, any required manual startup evidence is recorded, and narrow defects are stabilized. Do not activate S-036 automatically.
