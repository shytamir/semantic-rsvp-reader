# Baseline Freeze

## Exact Baseline

- Git commit: `8b50a3049bb5d92a304a03527385c519194ce8da`
- Python version recorded by generator output.
- Dependency versions recorded by generator output where installed.
- Chunker: `semantic_rsvp.chunking.rules.RuleBasedChunker`
- Normalization: `semantic_rsvp.text.normalize.normalize_text`
- Segmentation: `semantic_rsvp.text.segment.split_sentences`
- Schedule generation: `semantic_rsvp.timing.schedule.schedule_text`
- Chunker defaults: `max_chars=32`, `max_content_words=2`
- Timing defaults: `base_beat_ms=400`, `min_duration_ms=150`, `max_duration_ms=1200`, `sentence_pause_ms=180`
- Fallback behavior: production scheduling uses `RuleBasedChunker()` when no chunker is supplied.

## Generated Artifacts

- Manifest hashes: `evaluation/parser_assisted_chunking/baseline/manifest_hashes.json`
- Baseline output: `evaluation/parser_assisted_chunking/baseline/rule_based_baseline.json`

## Commands

```bash
python scripts/validate_chunking_corpus.py
python scripts/freeze_chunking_baseline.py --write
python scripts/freeze_chunking_baseline.py --check
```

The generator records chunk text, character offset mappings when safely recoverable, sentence index, timing duration, display state, navigation metadata, and structure metadata.
