# Browser-Local Reading Continuity

S-041 stores a minimal versioned continuity record in browser `localStorage`.
It is local to the current browser profile and is never sent to the Flask
application.

## Stored Records

Two keys keep preferences separate from document state:

- `semantic-rsvp-reader.preferences.v1`: speed level and whether adaptation is
  enabled.
- `semantic-rsvp-reader.documents.v1`: up to 12 recent document references,
  retained for at most 90 days.

Each document entry contains only the stable S-039 document identity, source
type, a short display name, current chunk position, at most 64 breakpoint
indices, and update time. Position and breakpoints are clamped to the current
schedule during restoration.

## Restoration And Removal

The reader never stores source text, so reopening the page stays on the input
screen and remains paused. Preparing text with the same stable identity restores
its position and breakpoints, still paused. The user explicitly starts playback.

`Reset` returns the current document to the first chunk and persists that
position. `Remove current saved state` deletes the current document reference,
position, and breakpoints. `Clear all local reading data` deletes document
records and preferences and resets the active preference controls to defaults.

Corrupt JSON, obsolete versions, invalid shapes, future timestamps, and records
older than 90 days are removed. Missing-document references retain no source and
can only be matched by preparing the same content or removed through the clear
control.

## Privacy And Deliberate Exclusions

Continuity does not store source text, defect reports or notes, session events,
telemetry, elapsed time, active timers, playback/running state, drift recovery,
parser data, schedules, or chunk text. There is no account, cloud sync, remote
transfer, database, service worker, or cross-device identity.
