# Bounded Local Document Ingestion

S-040 provides framework-independent adapters that turn local byte payloads
into the project-owned `SourceDocument` contract. It does not add an upload
route, renderer, persistence layer, or remote fetcher.

## Accepted Sources

| Extensions | Source type | Encoding | Structure |
| --- | --- | --- | --- |
| `.txt` | `plain_text` | UTF-8 or UTF-8 BOM | Text only |
| `.md`, `.markdown` | `markdown` | UTF-8 or UTF-8 BOM | Existing Markdown H1/H2 detection; no rendering |
| `.html`, `.htm` | `clean_html` | UTF-8 or UTF-8 BOM | Extracted article text and H1/H2 headings |

The adapter records exactly four provenance fields: `adapter`, `encoding`,
`media_type`, and `name`. Source identity remains the S-039 versioned hash of
source type plus normalized text; provenance and filenames do not affect it.

## Limits And Failures

- Maximum encoded size: 1,000,000 bytes.
- Maximum source lines: 20,000.
- Maximum HTML elements: 10,000.
- Maximum HTML nesting: 32 levels.
- Empty, invalid UTF-8, NUL-containing, unsupported-extension, mismatched HTML,
  and over-limit inputs fail with `DocumentIngestionError`.

The clean-HTML subset accepts article-oriented block elements (`article`,
`main`, `section`, `div`, `p`, `h1`, `h2`, lists, and block quotes), simple
inline text elements, HTML5 doctype, and line breaks. It rejects scripts,
styles, frames, SVG, templates, event-handler attributes, and all unlisted
elements. Attributes are never fetched or rendered.

## Deliberate Omissions

No PDF, EPUB, remote URL, arbitrary scraping, full Markdown/HTML rendering,
embedded media, persistence, parser adjustment, or API change is included.

EPUB remains a separate bounded adapter and contract. The S-043A1 offline preparation engine may simplify local EPUB bytes before that final adapter, but it does not broaden this local-document adapter, persist source content, fetch remote resources, or add an application route.

## Local Inspection

Inspect a project-owned fixture through the adapter and existing reader service:

```bash
python scripts/inspect_document_ingestion.py tests/fixtures/ingestion/representative.md
```

The JSON output contains extracted text, H1/H2 structure, bounded provenance,
and scheduled reader chunks. Rejected inputs print the documented failure and
exit nonzero.
