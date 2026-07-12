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
