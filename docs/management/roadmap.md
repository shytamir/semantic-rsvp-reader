# Calibration Roadmap

The near-term goal is to refine the reading experience using observed defects rather than speculative feature additions.

## Current Phase: Validation-Driven Timing Calibration

**Goal:** Validate Timing Calibration Pass 1 against real phone reading at 1.0x and 1.15x.

- **Done:** In-app backend defect reporting.
- **Done:** Defect report security hardening.
- **Done:** Timing-context defect instrumentation.
- **Done:** Chunking Refinement Pass 1 from observed reports.
- **Done:** Display/tokenization noise cleanup and timing-only review filtering.
- **Done:** Timing Calibration Pass 1.
- **Current:** Post-calibration timing validation.

**Gate:** A timing-only validation pass produces clean reports showing whether dense chunks, extra-dense chunks, and quote/punctuation rhythm improved without introducing overpaused light chunks.

## Next Slice 1: Post-Calibration Timing Validation Pass

**Goal:** Collect timing/rhythm evidence after Timing Calibration Pass 1.

**Gate:** 8-12 clean reports, collected with adaptation disabled for at least one pass, focus on dense chunks at 1.0x and 1.15x.

## Next Slice 2: Timing Calibration Pass 1 Follow-Up

**Goal:** Make a small follow-up only if the post-calibration reports show recurring timing defects.

**Gate:** Any formula adjustment is backed by repeated timing-context evidence rather than isolated discomfort.

## Next Slice 3: Completion/Session Summary Polish

**Goal:** Improve demo validation ergonomics without changing timing semantics.

**Gate:** A tester can finish a session and understand what happened without reading raw debug output.

## Next Slice 4: Demo/Beta Readiness Pass

**Goal:** Prepare a small external-testable demo.

**Gate:** An external tester can run or use the app with minimal explanation, sample text is easy to load, and debug detail is controlled.

## Explicit Non-Goals For The Current Phase

- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
