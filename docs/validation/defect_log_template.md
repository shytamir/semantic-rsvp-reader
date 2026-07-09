# Defect Log Template

Copy this block for each issue found during validation.

```markdown
Date:
Tester:
Device/browser:
Sample ID:
Reading mode:
Speed:
Adaptation enabled:
Defect category:
Severity:
Original sentence or passage:
Observed chunks/timing:
What felt wrong:
Expected behavior:
Suggested fix:
Repro steps:
Notes:
```

## Filled Example

Date: 2026-07-09

Tester: Shy

Device/browser: Android / Firefox

Sample ID: DN-001

Reading mode: RSVP reader

Speed: 1.00x

Adaptation enabled: yes

Defect category: rushed_dense_chunk

Severity: 3

Original sentence or passage: "A phrase such as \"not because the evidence is weak, but because the explanation is incomplete\" asks the reader to hold a contrast in working memory."

Observed chunks/timing: The contrast appeared across several chunks, and the second half arrived before the first half felt settled.

What felt wrong: The sentence was understandable in normal reading, but the RSVP pass made the contrast feel flatter and harder to retain.

Expected behavior: The contrast should feel like one connected thought, with enough dwell time around the negated phrase and the second "because" clause.

Suggested fix: Inspect whether negation and contrast markers should influence either chunk grouping or timing.

Repro steps: Load DN-001, start at default speed, read until the final paragraph, and note the phrase beginning with "not because."

Notes: This may be a timing issue more than a chunking issue.
