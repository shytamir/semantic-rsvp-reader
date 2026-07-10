# Adaptation

## Purpose

Session-only adaptation provides a conservative feedback loop for reading speed without persistence or accounts.

## Current Behavior

- Adaptation is enabled by default for a loaded session.
- Repeated rewinds or pauses can slow playback within bounded speed levels.
- Smooth runs can increase speed conservatively.
- Manual speed changes suppress immediate automatic override.
- Loading new text resets adaptation state.

## Constraints

- No persistent user model.
- No analytics backend.
- No adaptive timing formula rewrite.
- Adaptation should not hide baseline chunking or timing defects during validation.

## Validation Notes

When isolating timing or chunking defects, run at least one pass with adaptation disabled.

## Known Limitations

- Adaptation can mask schedule quality if testers rely on it during baseline validation.
