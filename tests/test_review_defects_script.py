import gzip
import subprocess
import sys


def write_report(path, category, timing_context=False):
    lines = [
        "# Semantic RSVP Defect Report",
        "",
        "## Classification",
        "",
        f"Category: {category}",
        "Severity: 2",
        "",
    ]
    if timing_context:
        lines.extend(
            [
                "## Timing Context",
                "",
                "Base duration ms: 580",
                "Effective duration ms: 446",
                "",
            ]
        )
    text = "\n".join(lines)
    with gzip.open(path, "wt", encoding="utf-8") as file:
        file.write(text)


def test_review_defects_script_filters_by_category(tmp_path):
    report_dir = tmp_path / "reports"
    report_dir.mkdir()
    write_report(report_dir / "one.md.gz", "rushed_dense_chunk")
    write_report(report_dir / "two.md.gz", "bad_chunk_split")

    result = subprocess.run(
        [
            sys.executable,
            "scripts/review_defects.py",
            "--report-dir",
            str(report_dir),
            "--category",
            "rushed_dense_chunk",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "Observed Defects Review - rushed_dense_chunk" in result.stdout
    assert "one.md.gz" in result.stdout
    assert "two.md.gz" not in result.stdout
    assert "Reports by category:" in result.stdout
    assert "rushed_dense_chunk: 1" in result.stdout


def test_review_defects_script_handles_missing_directory(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            "scripts/review_defects.py",
            "--report-dir",
            str(tmp_path / "missing"),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "No defect reports found." in result.stdout


def test_review_defects_script_filters_timing_only(tmp_path):
    report_dir = tmp_path / "reports"
    report_dir.mkdir()
    write_report(report_dir / "old.md.gz", "rushed_dense_chunk")
    write_report(report_dir / "timed.md.gz", "rushed_dense_chunk", timing_context=True)

    result = subprocess.run(
        [
            sys.executable,
            "scripts/review_defects.py",
            "--report-dir",
            str(report_dir),
            "--timing-only",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "Observed Defects Review - timing context only" in result.stdout
    assert "Total reports: 2" in result.stdout
    assert "Included reports: 1" in result.stdout
    assert "Reports with timing context: 1" in result.stdout
    assert "Reports without timing context: 0" in result.stdout
    assert "timed.md.gz" in result.stdout
    assert "old.md.gz" not in result.stdout


def test_review_defects_script_combines_category_and_timing_filters(tmp_path):
    report_dir = tmp_path / "reports"
    report_dir.mkdir()
    write_report(report_dir / "timed_chunk.md.gz", "bad_chunk_split", timing_context=True)
    write_report(report_dir / "timed_rushed.md.gz", "rushed_dense_chunk", timing_context=True)
    write_report(report_dir / "old_rushed.md.gz", "rushed_dense_chunk")

    result = subprocess.run(
        [
            sys.executable,
            "scripts/review_defects.py",
            "--report-dir",
            str(report_dir),
            "--category",
            "rushed_dense_chunk",
            "--timing-only",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "timed_rushed.md.gz" in result.stdout
    assert "timed_chunk.md.gz" not in result.stdout
    assert "old_rushed.md.gz" not in result.stdout
    assert "rushed_dense_chunk: 1" in result.stdout


def test_review_defects_script_writes_output_file(tmp_path):
    report_dir = tmp_path / "reports"
    report_dir.mkdir()
    write_report(report_dir / "one.md.gz", "rushed_dense_chunk")
    output_path = tmp_path / "review" / "timing.md"

    subprocess.run(
        [
            sys.executable,
            "scripts/review_defects.py",
            "--report-dir",
            str(report_dir),
            "--out",
            str(output_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "one.md.gz" in output_path.read_text(encoding="utf-8")
