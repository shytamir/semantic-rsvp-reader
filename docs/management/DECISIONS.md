# Project Decisions

This file records durable decisions, not every implementation detail.

## D-001: Deterministic Chunking Over Opaque Parsing

The reader uses inspectable Python chunking rules instead of an ML parser. This keeps validation evidence traceable and avoids adding NLP dependencies before the prototype has stronger qualitative evidence.

Consequence: chunking improvements should stay tied to observed defects and focused regression tests.

## D-002: Validation-driven Refinement

The project advances through observed validation evidence rather than speculative feature expansion.

Consequence: STATUS names one active slice, the roadmap orders near-term work, and completed slices move to HISTORY.

## D-003: Human-owned Qualitative Gates

Codex can implement, test, and maintain docs, but the human owner is the acceptance authority for usability and reading-comfort gates.

Consequence: Codex must not declare a validation gate passed without human evidence.

## D-004: Baseline And Exploratory Validation Stay Separate

Comparable validation uses fixed conditions: same device/browser where practical, fixed recorded speed, adaptation disabled, fixed corpus subset, predetermined exposure, and comparable reports.

Consequence: exploratory reading remains useful but should not be treated as baseline evidence.

## D-005: Navigation Is Session-only And Low-distraction

Navigation aids are designed for orientation without adding persistence, accounts, or heavy UI.

Consequence: passive anchor, breakpoints, ghost chunk, drift recovery, and structural labels should stay lightweight unless validation evidence says otherwise.

## D-006: Source-boundary Preservation Before Full Document Rendering

The reader preserves simple source, title, byline, date, and heading boundaries without becoming a full Markdown/article renderer.

Consequence: full Markdown rendering, heading navigation, and table of contents remain parked.

## D-007: Optional Parser-assisted Chunking Experiment

Status: provisional / experimental.

The project authorizes a reversible, optional parser-assisted chunking experiment while retaining the current deterministic rule-based implementation as the production default and fallback.

Context: the existing system uses hand-written rules for both linguistic cohesion and RSVP presentation. Rule interactions and corpus-specific exceptions are increasing maintenance cost. Generic RAG or document chunkers do not solve the RSVP presentation problem. Conventional NLP may provide useful sentence-structure evidence without controlling final presentation.

Decision: a future spike may use an optional local parser-assisted path, but the production baseline stays dependency-free from NLP tooling during the experiment. The experiment must use project-owned intermediate feature records, deterministic RSVP boundary selection after feature extraction, and held-out comparison before any default replacement.

Consequences: future experimental dependencies must remain isolated initially, library and model versions must eventually be pinned, parser failure or unsafe token alignment must fall back to the baseline, linguistic spans are normally soft constraints, display width and structural boundaries remain hard project constraints, and installation weight, latency, and fallback rate become evaluation concerns.

References: [Parser-Assisted Chunking Experiment](../experiments/parser_assisted_chunking/README.md), [Experiment Contract](../experiments/parser_assisted_chunking/experiment_contract.md), and [Future Implementation Interface](../experiments/parser_assisted_chunking/future_interface.md).
