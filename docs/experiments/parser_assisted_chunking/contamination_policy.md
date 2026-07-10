# Contamination Policy

This project cannot claim perfect scientific blindness for every set, because some frozen inputs are committed to the repository. It can still preserve useful separation between visible development material, frozen generalization inputs, and human-held blind material.

## Visibility Rules

- Development cases and annotations may be inspected during implementation.
- Regression cases may be inspected, but they cannot demonstrate generalization.
- Frozen generalization inputs may be visible, but their human annotations must remain unavailable during tuning.
- Human-held blind source text and annotations must remain unavailable until tuning is declared complete.
- Evaluation reports must state which sets were visible during implementation.

## Reclassification Rules

- Newly discovered held-out defects must not be moved into the development corpus before the comparison is recorded.
- If a generalization annotation is accidentally exposed during tuning, reclassify that case as visible generalization evidence.
- If blind source text or annotations are accidentally exposed, remove those cases from blind scoring and replace them if possible.
- Record accidental exposure in the evaluation report.

## Checksum Procedure

For human-held files kept outside the active repository, record a SHA-256 checksum without revealing source text.

PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 path\to\sealed-blind-set.jsonl
```

Python:

```bash
python -c "import hashlib, pathlib; p=pathlib.Path('sealed-blind-set.jsonl'); print(hashlib.sha256(p.read_bytes()).hexdigest())"
```

The repository may store a checksum and minimal sealed-package metadata, but not blind source text or gold annotations.
