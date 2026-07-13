# A Local-First Reading Session

The Semantic RSVP Reader turns a source document into deterministic semantic chunks and presents them one at a time. The reader can pause, move through the schedule, and retain bounded local continuity without storing source text in application-owned browser storage.

## Inspectable Boundaries

The Flask application delegates scheduling to a project-owned service. Parser evidence is translated into backend-neutral records, while final chunking and timing policy remain deterministic and project-owned. If parser evidence is missing or unsafe, the rule-based fallback remains mandatory.

## Document Continuity

Stable document identity connects ingestion, scheduling, EPUB contents navigation, and paused restoration. Preferences are stored separately from per-document position. Removing a recent document removes its application-owned continuity record.

## Evidence Before Claims

Automated tests protect focused contracts, browser smoke covers critical flows, and fixed human protocols cover qualitative behavior. The project is a validated local prototype, not a production service or a claim about reading performance.
