from __future__ import annotations

import argparse
import gzip
import sys
from pathlib import Path


DEFAULT_REPORT_DIR = Path("data") / "defect_reports"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Combine gzip Markdown defect reports into one review document."
    )
    parser.add_argument(
        "--report-dir",
        default=str(DEFAULT_REPORT_DIR),
        help="Directory containing .md.gz defect reports.",
    )
    parser.add_argument(
        "--category",
        help="Only include reports with this Category value.",
    )
    parser.add_argument(
        "--out",
        help="Write combined Markdown to this file instead of stdout.",
    )
    return parser.parse_args(argv)


def load_reports(report_dir: Path, category: str | None = None) -> list[tuple[str, str]]:
    if not report_dir.exists():
        return []

    reports = []
    for path in sorted(report_dir.glob("*.md.gz")):
        text = gzip.open(path, "rt", encoding="utf-8").read()
        if category and f"Category: {category}" not in text:
            continue
        reports.append((path.name, text))
    return reports


def render_review(reports: list[tuple[str, str]], category: str | None = None) -> str:
    title = "Observed Defects Review"
    if category:
        title += f" - {category}"
    lines = [f"# {title}", ""]
    if not reports:
        lines.append("No defect reports found.")
        lines.append("")
        return "\n".join(lines)

    for filename, text in reports:
        lines.extend(
            [
                "---",
                "",
                f"<!-- Source: {filename} -->",
                "",
                text.strip(),
                "",
            ]
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    reports = load_reports(Path(args.report_dir), category=args.category)
    review = render_review(reports, category=args.category)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(review, encoding="utf-8")
    else:
        print(review)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
