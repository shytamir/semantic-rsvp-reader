# S-039 Application-Service and Source-Document Contract Validation

## Existing Behavior Preserved

Before S-039 implementation, `ScheduleService` already provided the complete
framework-independent text-to-schedule pipeline. It normalized and segmented
once, accepted an injected `Chunker`, attached timing, display-state,
navigation, and H1/H2 structure metadata, and served all three text-processing
routes. Those behaviors and the public JSON shapes remain unchanged. The
parser-assisted default with mandatory automatic rule-based fallback remains
the operating policy.

## Implemented Delta

`SourceDocument` is an immutable project-owned record with deterministic
versioned identity, source type, preserved source text, supported H1/H2 structure,
and sorted provenance limited to eight string fields. Identity excludes
provenance so equivalent content and source type remain stable across rename or
re-import. Later adapters can pass the record's `text` through the
existing `ScheduleService.generate()` interface. Route tests can substitute a
service through the existing `app.config["SCHEDULE_SERVICE"]` seam. The
hash-registered S-026 service and web implementation files and all HTTP shapes
remain unchanged.

## Automated Evidence

- Focused source-document, route-injection, and repository-integrity tests
  passed: 12 tests.
- The full standard-profile repository suite passed: 301 tests.
- The visible chunking corpus passed: 22 cases.
- The frozen rule-based baseline remained reproducible.
- The parser-assisted-default Flask smoke passed.
- Markdown links and diff whitespace checks passed.

The final implementation report records immediately available GitHub Actions
status without waiting or polling.

## Deliberate Omissions

S-039 adds no file format, database, local persistence, public API field,
frontend behavior, parser change, fallback change, timing change, or issue #24
work. Unsupported structure remains source text. S-040 through S-043
remain inactive.

## Human Confirmation Protocol

Review only these two plain-language questions:

1. Is identity based on source type plus normalized text stable enough for
   S-041 to recognize the same document without using a filename or provenance?
2. Are supported H1/H2 headings and at most eight short provenance fields enough
   groundwork for S-040 adapters without storing arbitrary metadata?

Record `passed`, `partially_passed`, `failed`, or `inconclusive`. This gate does
not ask for browser, phone, parser-quality, ingestion-format, or persistence
validation.
