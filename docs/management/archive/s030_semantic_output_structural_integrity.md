# S-030 Semantic Output and Structural Integrity

## Status

Completed as `passed` from human-owned evidence commit `c632b71`. The authorized structural/ghost lane CSS fix was completed without semantic or parser changes. Long-word, quote, and parenthetical observations remain evaluation evidence.

## Objective

Validate that the shipped parser-default path produces coherent, deterministic semantic chunks and correct H1/H2 structural metadata while mandatory rule-based fallback remains safe.

## Initiating Reason

Parser-assisted output is now the provisional Flask default and S-029 changed dwell timing, but the frozen parser behavior still needs a focused shipped-build integrity pass across representative difficult text and structural transitions.

## In Scope

- Parser-default chunks, sentence/source boundaries, headings, active H1/H2 labels, and navigation-attached structure metadata.
- Protected names, dates, quotes, parentheticals, coordinated phrases, phrasal verbs, qualifier pairs, long tokens, and visible development/regression/generalization cases.
- Explicit rule-based operation and automatic fallback output on the same representative material.

## Codex Preparation

Run existing corpus, freeze, parser-parity, fallback, API, and structural-metadata checks; prepare a concise comparison/checklist from project-owned cases; record concrete defects without qualitative retuning.

## Human Handoff

Read a fixed difficult-case subset in the shipped parser-default build and judge semantic coherence, structural orientation, overlong/underdense chunks, and whether fallback remains usable.

## Permissible Stabilization

Only a narrow fix for a reproduced defect may follow validation. A new semantic defect must first become a recorded evaluation case. Do not retune or modify the frozen parser merely to improve qualitative output.

## Non-Goals

No optimizer tuning, provider ablation, broad handwritten rule expansion, timing/playback changes, new document parser, or production-provider commitment.

## Completion Boundary

Automated characterization and required human evidence are recorded; any authorized narrow fix is validated. Transition to `AWAITING_HUMAN_VALIDATION` when qualitative review is pending, then to the human-determined gate result. Do not activate S-031 automatically.
