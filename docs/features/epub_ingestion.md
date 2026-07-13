# Bounded EPUB Ingestion

S-042A provides a framework-independent `ingest_epub_document` adapter. It
returns the S-039 immutable `SourceDocument`; it does not add an upload route,
reader UI, contents view, heading navigation, or rendered ebook surface.

## Supported Subset

- local `.epub` bytes using the standard ZIP container;
- the first, uncompressed `mimetype` entry with the exact EPUB media type;
- exactly one valid package rootfile declared by `META-INF/container.xml`;
- EPUB 2.x or 3.x packages with required unique identifier, title, and language;
- unencrypted UTF-8 XHTML linear spine items in declared order;
- the same deliberately limited clean-HTML/article elements supported by local
  ingestion, including `h1` and `h2`, converted to project-owned text structure.

ZIP paths must be relative and unique. Remote references, encrypted/DRM content,
non-XHTML spine items, unsafe paths, symbolic links, unsupported compression,
external XML declarations, scripts, styles, SVG, images, and unsupported HTML
elements fail explicitly. CSS, media, navigation documents, and non-linear
manifest resources are not rendered or interpreted.

## Limits And Identity

- 20,000,000 compressed input bytes;
- 1,000 ZIP entries;
- 50,000,000 total expanded bytes and 5,000,000 bytes per entry;
- 100:1 maximum per-entry compression ratio;
- 200 spine declarations and 5,000,000 extracted text characters.

Identity remains `SourceDocument` v1 identity over source type `epub` and
normalized extracted text. Container compression, source filename, and bounded
provenance do not change identity. Provenance records only adapter version,
source name/media type, required package metadata, and extracted spine count.

The synthetic files under `tests/fixtures/epub/` are project-owned and covered
by the repository license. Tests package them deterministically and verify
ordering, headings, metadata, safety failures, stable identity, scheduling, and
the identity used by browser-local continuity.

## Reader Application Boundary

S-042B adds a dedicated `POST /api/epub/schedule` request accepting raw
`application/epub+zip` bytes and a bounded `X-EPUB-Filename` display hint. It
does not encode EPUB bytes into JSON and does not alter the existing one-megabyte
limit for JSON, text, defect, or schedule requests. Only this route may accept
the S-042A twenty-megabyte EPUB container limit.

The response supplies the existing schedule representation plus a canonical
server-produced document ID, source type `epub`, and bounded display metadata.
The browser passes that identity directly into the existing reader and S-041
continuity store. It never hashes the filename or EPUB bytes and never persists
source text or archive bytes. Restoration therefore occurs only after the user
reselects an EPUB whose extracted normalized text yields the same canonical ID.

This application boundary completed S-042B as `passed` after terminal Core,
integrity, browser-smoke, and CodeQL evidence. Contents and heading navigation
remain outside this boundary and require separate S-042C activation.

## Lightweight Contents Navigation

S-042C uses only the H1/H2 structure already attached to scheduled chunks. For
each supported heading, the contents view maps to the first schedule item marked
as that header chunk. It does not inspect EPUB navigation documents or NCX.

Selecting a heading cancels pending playback or drift recovery, moves to that
existing schedule index, refreshes progress and the structure anchor, persists
the position through normal continuity, and remains paused. Contents buttons
retain keyboard focus. EPUBs without supported headings show an explicit empty
state; the list is height-bounded and scrollable on narrow screens.
