import gzip
import subprocess
import sys


def write_report(path, category):
    text = "\n".join(
        [
            "# Semantic RSVP Defect Report",
            "",
            "## Classification",
            "",
            f"Category: {category}",
            "Severity: 2",
            "",
        ]
    )
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
