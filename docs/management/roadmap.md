# Calibration Roadmap

The near-term goal is to refine the reading experience using observed defects rather than speculative feature additions.

## Current Phase: Post-Calibration Refinement Planning

**Goal:** Convert the third-pass timing-context report into a narrow follow-up plan without overfitting or globally slowing dense chunks.

- **Done:** In-app backend defect reporting.
- **Done:** Defect report security hardening.
- **Done:** Timing-context defect instrumentation.
- **Done:** Chunking Refinement Pass 1 from observed reports.
- **Done:** Display/tokenization noise cleanup and timing-only review filtering.
- **Done:** Timing Calibration Pass 1.
- **Done:** Refreshed validation corpus to reduce overfitting.
- **Done:** Third-pass post-calibration timing report review.
- **Current:** Targeted follow-up planning for extreme density, punctuation rhythm, and chunk-shape noise.

**Gate:** The next implementation should address only repeated third-pass signals: extreme semantic density, semicolon/comma rhythm, quote-adjacent text cleanup, orphaned function words, and modal/auxiliary attachment. It should not apply a blanket dense-duration increase.

## Next Slice 1: Targeted Timing/Chunking Follow-Up Pass 1

**Goal:** Make narrow fixes for the third-pass defects.

**Candidate work:**

- detect extreme semantic density without slowing every dense chunk;
- improve semicolon and comma-list emphasis dwell;
- inspect quote-adjacent spacing cleanup such as `intuition"cannot.`;
- reduce orphaned function-word chunks such as `as`;
- inspect modal/auxiliary attachment around `should`.

**Gate:** Tests cover each recurring pattern, schedule/API shape remains stable, and light chunks are not globally overpaused.

## Next Slice 2: Clean Validation Pass After Targeted Follow-Up

**Goal:** Retest with the refreshed corpus and adaptation disabled for at least one pass.

**Gate:** 8-12 clean timing-context reports or a clear note that defects are no longer recurring enough to justify another timing change.

## Next Slice 3: Completion/Session Summary Polish

**Goal:** Improve demo validation ergonomics without changing timing semantics.

**Gate:** A tester can finish a session and understand what happened without reading raw debug output.

## Next Slice 4: Demo/Beta Readiness Pass

**Goal:** Prepare a small external-testable demo.

**Gate:** An external tester can run or use the app with minimal explanation, sample text is easy to load, and debug detail is controlled.

## Explicit Non-Goals For The Current Phase

- No blanket dense-duration increase based only on the third-pass report.
- No public performance claims.
- No ML/NLP dependency additions.
- No accounts, analytics, persistence model, service workers, or deployment work.
- No frontend framework migration or browser automation tooling.
- No native app, EPUB/PDF import, or cloud sync.
