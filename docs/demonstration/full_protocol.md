# Full Technical Portfolio Demonstration

Target: approximately ten minutes. Use only the pinned checkout and committed inputs.

1. Show the immutable SHA, Python 3.12 standard profile, dependency identity, and the documented startup command.
2. Start the Flask development server and show `/health`, including configured mode, active mode, provider, and fallback state.
3. Paste [portfolio-demo.md](../../samples/portfolio-demo.md), prepare it, and identify the canonical source-document/schedule boundary.
4. Demonstrate play/pause, timing, forward/back navigation, coarse seek, and one breakpoint traversal without changing settings solely for presentation effect.
5. Pause, reload, and restore position; show preferences separately. Explain that application-owned continuity stores IDs, positions, preferences, breakpoints, and recent references—not source text or active timers.
6. Reset or remove that document record and show the bounded local control.
7. Select [portfolio-demo.epub](../../samples/portfolio-demo.epub); identify the server-provided canonical EPUB identity and the dedicated raw-byte request boundary.
8. Open contents, jump to `Continuation`, retain focus, and confirm playback remains paused. Reload or reselect the same EPUB to show identity-based continuity.
9. Demonstrate one bounded failure by selecting a plain text file renamed with `.epub`; report the displayed validation error without treating it as an application crash.
10. Summarize the [architecture/evidence map](repository_orientation.md) and [claims/limitations](supported_claims_and_limitations.md): local prototype, deterministic policy and fallback, bounded ingestion, no source-text persistence, and no production or reading-performance claim.

Use the [fallback sequence](fallback_package.md) if live execution fails. Do not use network content, private evaluation material, arbitrary ebooks, or undocumented recovery steps.
