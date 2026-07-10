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

## D-008: Backend-neutral Linguistic Evidence

Status: accepted architectural direction; implementation deferred pending experiment disposition.

The RSVP boundary optimizer must remain independent of any particular NLP library, model, runtime, operating system, or vendor service.

Context: the parser-assisted experiment currently uses spaCy as a practical scientific reference implementation. This allows the project to test whether linguistic evidence improves chunking, but it does not establish spaCy, Python, or the current English model as suitable production dependencies for every target platform.

Directly embedding the experimental spaCy stack in a future mobile application may impose unacceptable package size, memory use, initialization latency, build complexity, platform compatibility work, and long-term dependency maintenance. Native platforms may instead provide some relevant linguistic capabilities through operating-system frameworks, managed on-device models, or hardware-accelerated inference services.

Decision: linguistic analysis and RSVP boundary selection will remain separate architectural responsibilities.

NLP backends must convert their results into a project-owned, backend-neutral representation before those results reach the RSVP optimizer. The optimizer must not depend directly on spaCy objects, Apple framework types, Android service objects, model-specific token identifiers, or vendor-specific grammatical labels.

The neutral representation should expose only evidence that the RSVP system has demonstrated a need for, potentially including:

* tokens and source-character offsets;
* sentence boundaries;
* named entities;
* dates, quantities, and numerical spans;
* parts of speech;
* noun-phrase or protected spans;
* grammatical relationships;
* confidence or alignment information;
* declared backend capabilities.

Different providers are not required to expose identical features. Each provider should declare its capabilities explicitly, and the optimizer must degrade safely when evidence is unavailable.

Possible future providers may include:

* the current spaCy adapter for experimentation, desktop use, or server-side processing;
* Apple Natural Language or related native iOS services;
* Android platform or managed on-device NLP services;
* a compact project-specific mobile model;
* a server-backed linguistic-analysis service;
* a no-NLP provider that preserves the deterministic rule-based fallback.

Consequences:

* spaCy remains an experimental evidence provider, not the universal production architecture.
* A positive S-024 result would establish the value of parser-derived evidence, not automatically justify shipping spaCy on mobile.
* Production adoption must separately evaluate provider footprint, latency, memory use, privacy, offline availability, platform coverage, determinism, model lifecycle, and fallback behavior.
* The project should avoid building a general-purpose NLP abstraction. Only capabilities demonstrated to improve RSVP segmentation should enter the stable interface.
* Provider failure, missing capabilities, unsafe alignment, or unsupported platforms must not prevent access to the existing deterministic fallback.
* Platform-specific providers may produce different evidence, but final width limits, source preservation, structural boundaries, timing compatibility, and deterministic RSVP policy remain project-owned.
* Formalizing or integrating additional providers is deferred until the parser-assisted experiment reaches its post-experiment disposition.
* A later feature-ablation study should determine which linguistic signals account for any observed improvement before native or compact production replacements are designed.

This decision does not promote the parser-assisted chunker, change the production default, modify the frozen experiment, or authorize immediate mobile implementation.
