# Corpus Provenance

Committed inputs are recorded in JSONL manifests under `evaluation/parser_assisted_chunking/manifests/`.

Every case records:

- Stable `case_id`.
- Corpus category.
- Exact source text.
- Document role.
- Language.
- Source ID.
- Provenance category.
- Whether it came from an existing project defect.
- Normalization status.
- Character count.
- Related validation report or test reference.
- Licensing or reuse status.

## Provenance Categories

- `synthetic_project_fixture`: text written specifically for this repository.
- `existing_regression_test`: text already represented in repository tests.
- `project_validation_evidence`: short text derived from existing project validation reports or defect descriptions.
- `public_domain_short_excerpt`: short public-domain excerpt used as fixed generalization material.

## Licensing Guidance

Do not commit full copyrighted articles or unnecessary personal data.

Prefer repository-owned synthetic examples, existing project fixtures, public-domain text, very short excerpts where legally appropriate, or text supplied directly as project test material.

Do not silently alter source text to make annotation easier. Record any normalization applied.

## Current Frozen Manifests

Manifest hashes are recorded in `evaluation/parser_assisted_chunking/baseline/manifest_hashes.json`.
