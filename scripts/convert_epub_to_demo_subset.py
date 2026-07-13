import argparse
import os
import sys
import tempfile
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semantic_rsvp.application.epub_preparation import EpubPreparationError, prepare_epub


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Prepare a local EPUB for the reader's bounded demo-safe subset.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    source = args.input.resolve()
    output = args.output.resolve()
    if source == output:
        parser.error("input and output paths must differ")
    if not source.is_file():
        parser.error("input must be an existing local file")
    if source.suffix.lower() != ".epub" or output.suffix.lower() != ".epub":
        parser.error("input and output paths must end with .epub")
    if output.exists() and not args.overwrite:
        parser.error("output exists; pass --overwrite to replace it")
    if not output.parent.is_dir():
        parser.error("output parent directory must exist")

    temporary = None
    try:
        result = prepare_epub(source.read_bytes(), source_name=source.name)
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=f".{output.name}.", suffix=".tmp", dir=output.parent, delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(result.data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output)
        temporary = None
    except (OSError, EpubPreparationError) as error:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        print(f"EPUB preparation failed: {error}", file=sys.stderr)
        return 1

    print(
        f"EPUB preparation {result.mode}: version={result.epub_version} "
        f"spine_items={result.spine_items} discarded_resources={result.discarded_resources} "
        f"output_bytes={result.output_size} characters={result.extracted_characters} "
        f"headings={result.heading_count} sha256={result.sha256}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
