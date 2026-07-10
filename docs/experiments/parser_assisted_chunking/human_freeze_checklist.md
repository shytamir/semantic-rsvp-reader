# Human-only Freeze Checklist

Complete this before parser implementation or tuning begins.

1. Review the proposed frozen generalization inputs.
2. Select the human-held blind challenge text.
3. Store blind inputs and annotations outside the active repository.
4. Complete annotations before parser tuning begins.
5. Compute and record a checksum using the procedure in [Contamination Policy](contamination_policy.md).
6. Do not paste blind material into Codex prompts.
7. Record the date and annotator ID.
8. Reveal the blind set only after implementation weights and rules are frozen.

The repository may contain a checksum and minimal metadata for a sealed package, but not the source text or gold annotations.
