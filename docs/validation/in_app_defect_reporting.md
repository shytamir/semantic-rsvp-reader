# In-App Defect Reporting

The reader can save validation defects directly from the mobile UI. Reports are stored locally by the Flask backend as compressed Markdown files. This is prototype validation support, not analytics infrastructure.

## How to Report a Defect

1. Start the Flask app.
2. Open the reader on a phone browser.
3. Load text or a validation sample.
4. Start reading.
5. When a chunk, pause, gesture, layout, or comprehension issue appears, tap `Report Defect`.
6. Choose a category and severity.
7. Add notes describing what felt wrong.
8. Optionally add the preferred behavior.
9. Submit the report.

Opening the report panel pauses playback. Closing the panel returns to the normal reader controls.

## Automatic Fields

Each report captures the current reader context:

- current chunk index and sentence index
- current chunk text
- current duration, syntactic hint, and content word count
- original sentence when available from `/api/schedule`
- nearby previous and next chunks
- current playback speed
- adaptation enabled/disabled state
- session summary counts
- browser user agent
- viewport size

## Manual Fields

The tester fills:

- defect category
- severity from 1-4
- notes
- optional preferred behavior

Severity uses the project taxonomy:

- 1: minor annoyance
- 2: noticeable friction
- 3: comprehension-impacting
- 4: session-breaking

## Storage

Reports are written under:

```text
data/defect_reports/
```

The directory is created automatically if missing. Generated report files are ignored by git.

Filenames use UTC server time:

```text
defect_YYYYMMDD_HHMMSS_<shortid>.md.gz
```

Example:

```text
defect_20260709_183512_a8f3d2.md.gz
```

The API response returns only `status`, `report_id`, and `filename`. It does not expose absolute filesystem paths.

## Security Notes

The backend uses generated report IDs and filenames only; user-provided text is never used in paths. Report fields are size-limited, control characters are normalized, and Markdown content escapes HTML-sensitive characters before writing to disk.

Flask also applies a request size limit to reduce accidental or hostile oversized submissions.

On startup, the backend performs a best-effort local storage encryption check for the defect report path. It checks BitLocker on Windows, FileVault on macOS, and LUKS-style encrypted storage on Linux when those platform tools are available. If encrypted storage cannot be confirmed, the app logs a warning and continues running. This app does not attempt to enable disk or hardware encryption itself.

## Reading Reports

Decompress one report while keeping the original gzip file:

```bash
gzip -dk data/defect_reports/defect_20260709_183512_a8f3d2.md.gz
```

Print all saved reports:

```bash
python - <<'PY'
import gzip
from pathlib import Path

for path in Path("data/defect_reports").glob("*.md.gz"):
    print("\n---", path.name, "---")
    print(gzip.open(path, "rt", encoding="utf-8").read())
PY
```

On Windows PowerShell, the same Python snippet can be saved into a temporary `.py` file and run from the project root.

## Refinement Loop

Use saved reports to drive the next chunking/timing refinement cycle:

1. Group reports by category and severity.
2. Look for repeated failures on similar language patterns.
3. Prefer fixing high-severity, repeatable defects first.
4. Convert stable improvements into focused tests.
5. Keep subjective discomfort reports visible; repeated subjective friction is product data.
