# Defect Reporting

## Purpose

In-app defect reporting captures validation evidence while the reader is in the problematic state.

## Current Behavior

- Reports are submitted from the reader UI.
- Playback pauses when reporting.
- Backend writes compressed Markdown reports under `data/defect_reports/`.
- Fields are bounded and escaped.
- Filenames are generated server-side.
- Local storage encryption support is checked best-effort; missing confirmation logs a warning without failing.

## Captured Context

- Current chunk and original sentence.
- Previous/next chunk context.
- Base and effective duration.
- Playback speed and session summary.
- Quote and parenthetical state.
- Navigation, breakpoint, drift recovery, and structure context.
- Display and layout context.

## Related Docs

- [In-app defect reporting](../validation/in_app_defect_reporting.md)
- [Defect taxonomy](../validation/defect_taxonomy.md)
- [Timing defect collection](../validation/timing_defect_collection.md)

## Known Limitations

- Reports are local files, not cloud analytics.
- Classification still depends on the tester choosing the best category.
