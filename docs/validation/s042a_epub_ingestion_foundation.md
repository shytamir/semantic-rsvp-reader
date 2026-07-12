# S-042A EPUB Ingestion Foundation Validation

## Scope

S-042A is an objectively verifiable framework-independent foundation. It adds
bounded EPUB container/package validation and deterministic text extraction into
the existing `SourceDocument` contract. It adds no application surface and has
no human gate.

## Executed Evidence

Executed local evidence:

- focused ingestion, source-document, schedule, and continuity compatibility:
  30 passed, 1 documented Node-dependent skip;
- full managed suite with a repository-local temporary base: 325 passed, 1
  documented Node-dependent skip;
- repository integrity: 2 passed;
- the 22-case corpus, frozen rule-based baseline, and S-037 characterization
  reproduced exactly;
- Markdown links and diff whitespace passed;
- JavaScript syntax reported its documented Node-unavailable skip;
- the optional security runner reported Bandit, pip-audit, Semgrep, Gitleaks,
  and detect-secrets unavailable and skipped. Focused EPUB security cases passed.

The first full-suite invocation completed all tests but the managed Windows
account was denied access while pytest cleaned its inherited global temporary
symlink. Re-running once with a repository-local `--basetemp` produced the clean
325-pass result; the temporary directory was removed and no project state was
changed by that environment repair.

Resolved remote evidence for commit
`e30cc5c7c858ad2d363290693f8ac6c9ba7ff058`:

- CI run `29212449552`: integrity and browser-smoke jobs passed. The Core job
  ran 320 dependency-light tests successfully, then failed on the pre-existing
  S-031 playback/adaptation characterization check. That evaluation-surface
  regression is unrelated to the bounded EPUB implementation.
- CodeQL run `29212449396`: Actions, Python, and JavaScript/TypeScript analyses
  all passed.

The human reviewed this remote evidence and accepts the isolated CI Core
regression as non-blocking for S-042A. It is neither repaired nor reinterpreted
here and does not authorize evaluation work. Together with the clean local
evidence, S-042A is dispositioned `passed` on 2026-07-13. Issue #17 remains open
as S-042 umbrella authority; no successor is active.

The project-owned synthetic fixture covers required EPUB 3 metadata, two UTF-8
XHTML spine items in deterministic order, `h1`/`h2` structure, stable identity,
and existing schedule/continuity compatibility. Focused negative cases cover an
invalid ZIP, encryption marker, unsafe path, missing metadata, missing spine
content, unsupported XHTML, and invalid UTF-8.

## Limitations

The deliberately limited subset and numeric limits are documented in [bounded
EPUB ingestion](../features/epub_ingestion.md). Contents UI, heading navigation,
new resume controls, rendered ebook behavior, DRM, full CSS fidelity, PDF, and
new application surfaces remain outside S-042A and unauthorized.
