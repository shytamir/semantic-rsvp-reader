# Repository Orientation

The shortest useful review path is:

1. [README](../../README.md) for purpose, setup, test commands, and documentation navigation.
2. [Architecture](../development/architecture.md) for the Flask, plain HTML/CSS/JavaScript, scheduling, and project-owned chunking boundaries.
3. [Environment contract](../development/environment_contract.md) for Python 3.12 profiles, exact dependencies, startup, and `/health` identity.
4. [EPUB feature](../features/epub_ingestion.md) and [local continuity](../management/s041_local_reading_continuity.md) for bounded ingestion, canonical identity, navigation, retention, and privacy behavior.
5. [QA strategy](../qa/strategy.md), [verification matrix](../qa/verification_matrix.md), and [validation index](../validation/index.md) for automated, browser, and human evidence boundaries.
6. [Security](../security/index.md), [license](../../LICENSE), and [current status](../management/STATUS.md) for repository trust and authority.

The architecture remains intentionally small: Flask routes delegate to application services; immutable `SourceDocument` values carry normalized text, structure, identity, and bounded provenance; schedule generation owns presentation-neutral chunks and navigation metadata; the browser owns transient presentation and bounded local continuity. Parser-specific objects do not enter the optimizer, and unsafe parser evidence falls back automatically.
