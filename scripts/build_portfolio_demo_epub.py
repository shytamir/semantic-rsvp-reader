import argparse
import io
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tests" / "fixtures" / "epub"
DEFAULT_OUTPUT = ROOT / "samples" / "portfolio-demo.epub"
NORMALIZED_NAME = "portfolio-demo-normalization-required.epub"
REJECTED_NAME = "portfolio-demo-encrypted-rejected.epub"
ENTRIES = (
    ("mimetype", b"application/epub+zip", zipfile.ZIP_STORED),
    ("META-INF/container.xml", (SOURCE / "container.xml").read_bytes(), zipfile.ZIP_DEFLATED),
    ("EPUB/package.opf", (SOURCE / "package.opf").read_bytes(), zipfile.ZIP_DEFLATED),
    ("EPUB/chapter-1.xhtml", (SOURCE / "chapter-1.xhtml").read_bytes(), zipfile.ZIP_DEFLATED),
    ("EPUB/chapter-2.xhtml", (SOURCE / "chapter-2.xhtml").read_bytes(), zipfile.ZIP_DEFLATED),
)


def _archive(entries) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        for name, data, compression in entries:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = compression
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return stream.getvalue()


def build_epub() -> bytes:
    return _archive(ENTRIES)


def build_normalization_required_epub() -> bytes:
    chapter_one = b'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"><html><head><meta charset="utf-8"><link rel="stylesheet" href="book.css"></head><body style="margin: 1em"><article><h1>Opening</h1><p>Preparation removes presentation markup while preserving this readable text.</p></article></body></html>'''
    chapter_two = b'''<html><head><meta name="generator" content="synthetic"></head><body><section><h2>Continuation</h2><p style="color: black">The normalized path preserves supported structure and deterministic identity.</p></section></body></html>'''
    return _archive((
        ENTRIES[0],
        ENTRIES[1],
        ENTRIES[2],
        ("EPUB/chapter-1.xhtml", chapter_one, zipfile.ZIP_DEFLATED),
        ("EPUB/chapter-2.xhtml", chapter_two, zipfile.ZIP_DEFLATED),
        ("EPUB/book.css", b"body { margin: 1em; }", zipfile.ZIP_DEFLATED),
    ))


def build_rejected_epub() -> bytes:
    return _archive((*ENTRIES, ("META-INF/encryption.xml", b"<encryption/>", zipfile.ZIP_DEFLATED)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or verify the project-owned portfolio EPUB.")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="write the deterministic EPUB")
    action.add_argument("--check", action="store_true", help="verify the committed EPUB")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    outputs = {
        args.output: build_epub(),
        args.output.with_name(NORMALIZED_NAME): build_normalization_required_epub(),
        args.output.with_name(REJECTED_NAME): build_rejected_epub(),
    }
    if args.check:
        for output, expected in outputs.items():
            if not output.is_file() or output.read_bytes() != expected:
                print(f"Portfolio EPUB is absent or stale: {output}", file=sys.stderr)
                return 1
        print("Portfolio EPUB paths are reproducible: " + ", ".join(path.relative_to(ROOT).as_posix() for path in outputs))
        return 0

    for output, expected in outputs.items():
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(expected)
    print("Wrote deterministic portfolio EPUB paths: " + ", ".join(path.relative_to(ROOT).as_posix() for path in outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
