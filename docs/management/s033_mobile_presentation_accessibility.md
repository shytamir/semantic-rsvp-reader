# S-033 Mobile Presentation and Accessibility

## Status

Active and authorized for implementation at `READY_FOR_IMPLEMENTATION`, owned by Codex. S-034 remains scheduled and inactive.

## Objective

Validate that the shipped mobile-first presentation remains readable, stable, accessible, and visually subordinate to the active RSVP chunk.

## Initiating Reason

Past phone-landscape overlap showed that static checks cannot establish device layout quality; the shipped overlays, context cues, and safe-area handling need targeted viewport validation.

## In Scope

- Portrait/landscape, narrow/wide viewports, safe-area insets, long chunks/tokens, and stable active-chunk sizing.
- Ghost context, hierarchy/progress/breakpoint cues, quote/parenthetical state, controls, speed/report overlays, and unobtrusive visual hierarchy.
- Keyboard focus visibility, control reachability, contrast/readability, overflow, and layout shifts.

## Codex Preparation

Inventory responsive CSS and static shell assertions, run syntax/tests, and prepare a viewport/content matrix including long-token and overlay states.

## Human Handoff

Inspect representative states on phone portrait and landscape plus narrow and wide browser viewports, using keyboard focus where available.

## Permissible Stabilization

Apply only narrow CSS/HTML/presentation corrections for reproduced overlap, clipping, focus, contrast, safe-area, or hierarchy defects.

## Non-Goals

No frontend framework, npm dependencies, build toolchain, browser automation, visual rebrand, navigation behavior change, or new accessibility platform.

## Completion Boundary

The viewport/state matrix and human visual judgment are recorded and concrete presentation defects are stabilized. Do not activate S-034 automatically.
