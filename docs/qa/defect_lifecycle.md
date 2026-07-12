# Defect Lifecycle

```text
observation
→ reproduction or evidence capture
→ classification
→ severity and priority assignment
→ authorization for correction, experiment modification, or scope expansion where required
→ correction or deferral
→ regression protection
→ human validation where applicable
→ disposition
→ issue closure or follow-up
```

An observation may be recorded, classified, and deferred without implementation
authorization. Evidence collection does not itself authorize correction.

## Classes

- **Product defect:** runtime, API, presentation, interaction, accessibility, or service behavior violates an intended product contract.
- **Scientific/evaluation observation:** semantic, linguistic, timing, optimizer, parser, annotation, evaluation, or corpus evidence that must not automatically become a production change.
- **Process/evidence defect:** context, reproducibility, protocol, hash, management state, retention, or evidence integrity is missing or inconsistent.

## Independent Decisions

- **Severity** measures impact; **priority** orders work.
- **Blocking status** determines whether current acceptance can proceed; it is not severity or priority.
- **Verification outcome** reports an executed check; **disposition** records the authorized decision.
- **Correction** changes the scoped defect; **deferral** records it without correction.
- A **slice defect** may be corrected only within its authorization; separately tracked follow-up work remains outside the slice.

A slice or issue may close with a non-blocking observation retained in a
separate follow-up. Record the evidence and linkage without implying the
follow-up was implemented or accepted.
