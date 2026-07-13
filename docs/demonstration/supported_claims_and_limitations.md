# Supported Claims And Limitations

## Supported Claims

- This is a local-first Flask and plain-browser prototype with deterministic project-owned chunking, scheduling, timing, navigation, and fallback policy.
- The standard profile uses parser-assisted chunking by default and automatically retains the deterministic rule-based fallback when linguistic evidence is unavailable or unsafe.
- Project-owned source-document identity connects supported ingestion, scheduling, EPUB navigation, and bounded paused continuity.
- Application-owned browser continuity does not store source text or EPUB bytes; records are versioned, bounded, resettable, and removable.
- The committed text plus unchanged, normalized, and rejected EPUB examples are synthetic, project-owned, reproducible, and covered by focused tests plus applicable CI evidence.

## Limitations And Deliberately Unproven Claims

- EPUB support is a deliberately limited clean XHTML subset, not general ebook rendering. During S-042 human validation, three ordinary EPUBs were rejected for `<link>`, a non-HTML5 doctype, and `<meta>` before preparation existed. S-043A can now remove those representative constructs when readable order and meaning remain safe; the historical observation remains valid evidence of the former direct-ingestion boundary.
- Preparation is deliberately lossy: styling, images, media, fonts, scripts, annotations, and unsupported presentation are discarded. The original local file is untouched; the web app neither saves nor returns prepared bytes. The offline CLI may write a prepared artifact only when explicitly invoked.
- EPUB navigation uses extracted H1/H2 schedule structure, not EPUB navigation documents or NCX. CSS fidelity, media, images, DRM, and arbitrary HTML are unsupported.
- Browser-managed form restoration can retain paste-box content independently of application-owned continuity; the application does not claim control over browser form behavior.
- The Flask development server is for local demonstration and development, not public hosting, deployment, reliability, security certification, or production readiness.
- Evidence does not establish comprehension, reading-speed improvement, accessibility conformance, medical or educational benefit, universal parser quality, market demand, or broad device/browser support.
- No account, analytics, telemetry, database, cloud synchronization, PDF ingestion, native application, installer, or external beta is included.

If behavior exceeds these claims, describe it as an observation—not as validated project capability.
