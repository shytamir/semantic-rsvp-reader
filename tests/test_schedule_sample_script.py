import subprocess
import sys


def test_schedule_sample_script_generates_readable_schedule():
    result = subprocess.run(
        [sys.executable, "scripts/schedule_sample.py"],
        input="The system learns from the reader.",
        text=True,
        capture_output=True,
        check=True,
    )

    assert "3 chunk(s) generated." in result.stdout
    assert "The system" in result.stdout
    assert "the reader." in result.stdout
