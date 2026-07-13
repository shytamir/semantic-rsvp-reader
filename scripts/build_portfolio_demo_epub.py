import argparse
import io
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tests" / "fixtures" / "epub"
DEFAULT_OUTPUT = ROOT / "samples" / "portfolio-demo.epub"
ENTRIES = (
    ("mimetype", b"application/epub+zip", zipfile.ZIP_STORED),
    ("META-INF/container.xml", (SOURCE / "container.xml").read_bytes(), zipfile.ZIP_DEFLATED),
    ("EPUB/package.opf", (SOURCE / "package.opf").read_bytes(), zipfile.ZIP_DEFLATED),
    ("EPUB/chapter-1.xhtml", (SOURCE / "chapter-1.xhtml").read_bytes(), zipfile.ZIP_DEFLATED),
    ("EPUB/chapter-2.xhtml", (SOURCE / "chapter-2.xhtml").read_bytes(), zipfile.ZIP_DEFLATED),
)


def build_epub() -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        for name, data, compression in ENTRIES:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = compression
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or verify the project-owned portfolio EPUB.")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="write the deterministic EPUB")
    action.add_argument("--check", action="store_true", help="verify the committed EPUB")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    expected = build_epub()
    if args.check:
        if not args.output.is_file() or args.output.read_bytes() != expected:
            print(f"Portfolio EPUB is absent or stale: {args.output}", file=sys.stderr)
            return 1
        print(f"Portfolio EPUB is reproducible: {args.output.relative_to(ROOT)}")
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(expected)
    print(f"Wrote deterministic portfolio EPUB: {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
