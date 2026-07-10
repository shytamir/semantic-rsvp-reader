# Quote and Parenthetical State Indicators

This slice adds deterministic display-state annotations for quote and parenthetical spans without changing chunking or timing rules.

## Purpose

The reader now carries lightweight metadata for each scheduled chunk:

- `in_quote`
- `quote_boundary`
- `in_parenthetical`
- `parenthetical_depth`

The frontend uses that metadata to apply subtle visual state changes so a reader can tell when a chunk belongs to a quotation or parenthetical aside. The goal is orientation, not emphasis.

## Current Behavior

- Quote chunks receive a reserved left rule so entering or continuing a quote has a stable visual signal.
- Parenthetical chunks receive a slightly quieter text color.
- The left spacing is always reserved, so quote state does not shift the anchored text position.
- Defect reports include the current chunk state and nearby chunk state.

## Validation Guidance

Use `quote_state_confusion` when quote entry, quote exit, or continuing quoted text is hard to follow.

Use `parenthetical_state_confusion` when a parenthetical aside or return to main text is visually unclear.

Use `punctuation_rhythm_issue` only when the visual state is clear and the remaining issue is timing, dwell, or pause rhythm.

## Non-Goals

- No timing formula changes.
- No speed or adaptation changes.
- No chunking rule changes.
- No semantic parser or ML dependency.
