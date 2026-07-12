# S-040 Bounded Document Ingestion Validation

## Automated Scope

Project-owned fixtures cover plain text, Markdown, clean HTML, an unsafe HTML
document, and an unsupported extension. Automated checks cover accepted
encoding identity, source type, H1/H2 structure, bounded provenance, unchanged
reader-service compatibility, size and nesting limits, and stable failure
messages. The final implementation report records broader repository, frozen
evidence, and immediately available remote results.

Executed evidence:

- all 14 focused ingestion and inspection tests passed;
- all 315 repository tests passed under the managed standard profile;
- the 22-case visible corpus and frozen rule-based baseline passed;
- the committed S-037 characterization reproduced;
- parser-assisted-default Flask smoke, repository integrity, Markdown links,
  and diff whitespace checks passed.

## Fixed Human Protocol

Use the repository fixtures under `tests/fixtures/ingestion/`. Do not substitute
private or downloaded documents for this gate.

For each filename below, run:

```bash
python scripts/inspect_document_ingestion.py tests/fixtures/ingestion/<filename>
```

1. Open `representative.txt`. Confirm both paragraphs appear in order in the
   extracted source text, provenance names the fixture with `text/plain` and
   UTF-8, and the result remains readable through the existing reader path.
2. Open `representative.md`. Confirm `Field Notes` and `Details` are recorded as
   H1/H2 structure, Markdown remains source text rather than rendered markup,
   provenance is bounded to the four documented fields, and reader output is
   readable.
3. Open `representative.html`. Confirm the browser-only `<title>` is omitted,
   `Local Article` and `Details` become supported H1/H2 structure, inline
   emphasis becomes plain text, provenance reports `text/html`, and reader
   output is readable.
4. Open `unsafe.html`. Confirm ingestion fails with `Unsupported HTML element:
   <script>.` and no partial document is returned.
5. Open `unsupported.pdf`. Confirm ingestion fails with `Unsupported document
   type. Expected .txt, .md, .markdown, .html, or .htm.` and its contents are
   not interpreted.

Record one outcome: `passed`, `partially_passed`, `failed`, or `inconclusive`.
Report only incorrect text order/content, missing or incorrect H1/H2 structure,
unbounded/incorrect provenance, unreadable existing-reader output, or a failure
that does not match the two fixed messages. This protocol does not validate PDF,
EPUB, arbitrary HTML, persistence, uploads, remote content, or rendered markup.
