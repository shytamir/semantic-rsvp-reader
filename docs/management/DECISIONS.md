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

## D-009: Provisional Parser-Assisted Adoption for the Flask Prototype

Status: accepted.

Disposition: `provisional_adoption_for_current_flask_prototype`.

Context: S-024 showed that the parser-assisted system substantially reduced annotated harmful boundaries and protected-span splits. In the sealed blind challenge, parser-assisted output had `0` forbidden-boundary violations versus `14` for the rule-based baseline, and `3` protected-span splits versus `19` for the rule-based baseline. The human blinded review preferred parser-assisted output in all 12 decisive comparisons, with 10 high-confidence and 2 medium-confidence parser-assisted preferences. Parser-assisted output also satisfied blind hard-compliance requirements without fallback.

The current project is a Python/Flask prototype delivered through a browser, not a native mobile package. The measured spaCy/model footprint and startup cost are acceptable for this prototype environment. Delaying integration for provider ablation or cross-platform optimization would reduce project velocity without addressing a current deployment blocker.

Decision: the frozen S-023 parser-assisted behavior is provisionally adopted as the default chunking path for the current Flask prototype. spaCy `3.7.5` and `en-core-web-sm` `3.7.1` are accepted as the provisional linguistic-evidence provider for this environment. `RuleBasedChunker` remains the mandatory deterministic fallback and explicit baseline.

The project will integrate the evaluated behavior without changing optimizer weights, feature interpretation, fallback rules, or model pins. D-008 continues to govern long-term architecture. This decision does not establish spaCy as the universal production provider, a native-mobile requirement, the only permissible implementation, or a permanent dependency for all future platforms. Future provider replacement, feature ablation, footprint reduction, or native integration may be considered when there is a concrete platform need. The current priority is validating the improved chunking behavior in normal prototype use.

Consequences:

* Production prototype requests prefer parser-assisted chunking.
* Missing or failed parser capability must degrade automatically to `RuleBasedChunker`.
* Flask route handlers must not depend on spaCy-native objects.
* The browser must not receive parser-native data.
* The application must not download models automatically at runtime.
* Fallback must be observable without exposing source text.
* The evaluated S-023 behavior remains frozen as the adoption reference.
* Optimizer retuning requires a separate future slice and new evaluation discipline.
* Broad hand-written semantic-rule expansion remains disallowed while the adopted path is being validated.
* Public superiority claims remain prohibited.

References: D-007, D-008, [S-024 objective comparison](../experiments/parser_assisted_chunking/s024_objective_comparison.md), and [S-024 human preference summary](../validation/archive/s024_human_ab_preference_summary.md).

Post-S-037 confirmation (2026-07-12): S-037 completed as `passed` at human-evidence commit `b95df256c0b26a8ff51e37e539f1a859bf31a56c` with disposition `retain_parser_default_with_mandatory_automatic_fallback`. The evaluator correction changes evidence classification; it does not establish a parser regression or reduced fallback safety. Unsafe mapping and unscorable output remain accepted limitations. GitHub issue #24 records an authorized non-blocking, inactive follow-up for normalized source-character preservation in rule-based fallback, particularly curly quotation marks, and source-reconstruction postconditions.

## D-010: Productization-entry Decision Brief

This brief aims to answer:

- Who is the first intended user?
  The first intended user is the human involved in the development of the product. He knows the product intimately and the product solves a real problem for him.
- What real reading problem should the next program solve?
  Ingest EPUB and local continuity features and retain featureset upon reading, but not before the product is ready for the feature. Human acknowledges D-008 correctly requires application service source document contract before ingest, continuity, and long navigation features can be implemented.
- Is the immediate objective a stronger local demo, a usable personal reader, or an external trial?
  It's twofold - A usable personal reader, and a strong local demo. The former takes precedence over the latter.
- What evidence would justify continuing through S-043?
  The question is vague, but if you mean requirements - then a workable demo with a rollback point, which we have now. If you mean readiness, the PM agent should advise we are ready. If you mean something else I missed your meaning.
- What would cause the program to pause, reorder, or stop?
  scope creep, overdevelopment, excessive human validation workloads, insufficiently clear human protocols, obvious conflicts that may arise during implementation or testing that point to a real need.
- What is the maximum scope you are willing to fund before external evidence?
  D-008 correctly dictates the implementation of the application service source contract before adding the EPUB ingest feature. A usable personal reader, with no observable feature regressions, and the EPUB ingest and local continuity features. It should be servicable as a stronger local demo.
  
In light of the above the project will progress to the beta program outlined in S-037 through S-043 as outlined, being careful not to overstep scope and improve human protocol authorship where possible.

The human records here that PM GPT advised 1-2 exploratory demos with other users at this stage, but this was deferred for after the next program by the human to have a stronger  prototype for the first exploratory demos.
