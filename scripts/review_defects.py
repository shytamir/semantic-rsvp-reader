from __future__ import annotations

import argparse
import gzip
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_REPORT_DIR = Path("data") / "defect_reports"


@dataclass(frozen=True)
class DefectReport:
    filename: str
    text: str
    category: str
    has_timing_context: bool


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
        "--timing-only",
        action="store_true",
        help="Only include reports that contain a Timing Context section.",
    )
    parser.add_argument(
        "--out",
        help="Write combined Markdown to this file instead of stdout.",
    )
    return parser.parse_args(argv)


def load_reports(
    report_dir: Path,
    category: str | None = None,
    timing_only: bool = False,
) -> list[DefectReport]:
    if not report_dir.exists():
        return []

    reports = []
    for path in sorted(report_dir.glob("*.md.gz")):
        text = gzip.open(path, "rt", encoding="utf-8").read()
        report = DefectReport(
            filename=path.name,
            text=text,
            category=_extract_category(text),
            has_timing_context="## Timing Context" in text,
        )
        if category and report.category != category:
            continue
        if timing_only and not report.has_timing_context:
            continue
        reports.append(report)
    return reports


def render_review(
    reports: list[DefectReport],
    category: str | None = None,
    timing_only: bool = False,
    total_report_count: int | None = None,
) -> str:
    title = "Observed Defects Review"
    if category:
        title += f" - {category}"
    if timing_only:
        title += " - timing context only"
    lines = [f"# {title}", ""]
    lines.extend(_render_summary(reports, total_report_count))
    if not reports:
        lines.append("No defect reports found.")
        lines.append("")
        return "\n".join(lines)

    for report in reports:
        lines.extend(
            [
                "---",
                "",
                f"<!-- Source: {report.filename} -->",
                "",
                report.text.strip(),
                "",
            ]
        )
    return "\n".join(lines)


def _extract_category(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("Category:"):
            return line.replace("Category:", "", 1).strip()
    return "unknown"


def _render_summary(
    reports: list[DefectReport],
    total_report_count: int | None = None,
) -> list[str]:
    total = len(reports) if total_report_count is None else total_report_count
    with_timing = sum(1 for report in reports if report.has_timing_context)
    without_timing = len(reports) - with_timing
    category_counts: dict[str, int] = {}
    for report in reports:
        category_counts[report.category] = category_counts.get(report.category, 0) + 1

    lines = [
        "## Summary",
        "",
        f"- Total reports: {total}",
        f"- Included reports: {len(reports)}",
        f"- Reports with timing context: {with_timing}",
        f"- Reports without timing context: {without_timing}",
        "- Reports by category:",
    ]
    if category_counts:
        for category in sorted(category_counts):
            lines.append(f"  - {category}: {category_counts[category]}")
    else:
        lines.append("  - none: 0")
    lines.append("")
    return lines


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report_dir = Path(args.report_dir)
    all_reports = load_reports(report_dir)
    reports = load_reports(
        report_dir,
        category=args.category,
        timing_only=args.timing_only,
    )
    review = render_review(
        reports,
        category=args.category,
        timing_only=args.timing_only,
        total_report_count=len(all_reports),
    )
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(review, encoding="utf-8")
    else:
        print(review)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
