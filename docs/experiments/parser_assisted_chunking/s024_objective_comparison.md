# S-024 Objective Comparison

This report contains repository-safe, redacted objective evidence only. It does not include blind source text, annotations, raw chunks, parser traces, or the A/B identity key.

The blind challenge set was revealed only after the S-023 implementation freeze. The set is synthetic and model-authored; it is useful for held-out boundary checks but does not establish human preference or broad real-world superiority by itself.

## Frozen Identities

- S-023 implementation commit: `b01085193a36b664b6415686ff835426d0434c92`
- Configuration hash: `0e3266b6917b75da27896b382104ecf164457fee7f28d7e4d835ccb7251accab`
- ZIP SHA-256: `a8926e9dc9cd68399f2c9f6a8b63ee44ac0cdd5b4f4361a20460410617b1f71b`
- Canonical SHA-256: `a6647ba26a9e32cfc154bfb904579f57ebdfbef9bdd2b64b7253cfefaa026502`

## Corpus Summaries

### Regression

- Cases: 8
- Rule-based forbidden violations: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted forbidden violations: {'numerator': 0, 'denominator': 0, 'rate': None}
- Rule-based protected-span splits: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted protected-span splits: {'numerator': 0, 'denominator': 0, 'rate': None}
- Rule-based required-boundary recall: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted required-boundary recall: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser fallback: {'cases': 0, 'rate': 0.0}
- Rule-based hard compliance: {'source_coverage_failure': 0, 'dropped_text': 0, 'duplicated_text': 0, 'source_ordering_failure': 0, 'structural_boundary_violations': 0, 'max_width_violations': 0, 'unsafe_mapping_failure': 0}
- Parser-assisted hard compliance: {'source_coverage_failure': 0, 'dropped_text': 0, 'duplicated_text': 0, 'source_ordering_failure': 0, 'structural_boundary_violations': 0, 'max_width_violations': 0, 'unsafe_mapping_failure': 0}
- Rule-based distribution: {'total_chunks': 33, 'chunks_exceeding_density_target': 5, 'mean_chars_per_chunk': 12.84375, 'median_chars_per_chunk': 13.375, 'mean_words_per_chunk': 2.2875, 'median_words_per_chunk': 2.1875, 'single_word_chunk_rate': 0.05625, 'long_chunk_rate': 0.0, 'chunks_per_sentence': 4.125, 'chunks_per_1000_words': 440.724125, 'char_width_distribution': {'3': 1, '5': 1, '6': 3, '8': 2, '9': 3, '10': 2, '11': 3, '13': 4, '14': 1, '15': 2, '16': 2, '17': 1, '18': 2, '19': 3, '21': 1, '22': 2}}
- Parser-assisted distribution: {'total_chunks': 21, 'chunks_exceeding_density_target': 9, 'mean_chars_per_chunk': 20.91675, 'median_chars_per_chunk': 19.9375, 'mean_words_per_chunk': 3.625, 'median_words_per_chunk': 3.4375, 'single_word_chunk_rate': 0.0, 'long_chunk_rate': 0.135417, 'chunks_per_sentence': 2.625, 'chunks_per_1000_words': 282.241875, 'char_width_distribution': {'10': 1, '11': 1, '14': 1, '16': 1, '17': 4, '19': 1, '22': 2, '23': 3, '24': 1, '25': 1, '26': 2, '28': 2, '30': 1}}
- Paired chunk-count behavior: {'parser_fewer_chunks': 8, 'parser_more_chunks': 0, 'identical_chunk_count': 0}

### Generalization

- Cases: 6
- Rule-based forbidden violations: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted forbidden violations: {'numerator': 0, 'denominator': 0, 'rate': None}
- Rule-based protected-span splits: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted protected-span splits: {'numerator': 0, 'denominator': 0, 'rate': None}
- Rule-based required-boundary recall: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted required-boundary recall: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser fallback: {'cases': 0, 'rate': 0.0}
- Rule-based hard compliance: {'source_coverage_failure': 0, 'dropped_text': 0, 'duplicated_text': 0, 'source_ordering_failure': 0, 'structural_boundary_violations': 0, 'max_width_violations': 0, 'unsafe_mapping_failure': 0}
- Parser-assisted hard compliance: {'source_coverage_failure': 0, 'dropped_text': 0, 'duplicated_text': 0, 'source_ordering_failure': 0, 'structural_boundary_violations': 0, 'max_width_violations': 0, 'unsafe_mapping_failure': 0}
- Rule-based distribution: {'total_chunks': 43, 'chunks_exceeding_density_target': 1, 'mean_chars_per_chunk': 11.285167, 'median_chars_per_chunk': 11.75, 'mean_words_per_chunk': 2.049667, 'median_words_per_chunk': 2.166667, 'single_word_chunk_rate': 0.155844, 'long_chunk_rate': 0.0, 'chunks_per_sentence': 5.472167, 'chunks_per_1000_words': 494.639333, 'char_width_distribution': {'4': 2, '5': 2, '6': 3, '7': 1, '8': 5, '9': 8, '10': 5, '11': 1, '12': 5, '13': 1, '14': 1, '15': 1, '16': 1, '17': 2, '19': 3, '20': 1, '23': 1}}
- Parser-assisted distribution: {'total_chunks': 24, 'chunks_exceeding_density_target': 13, 'mean_chars_per_chunk': 21.427833, 'median_chars_per_chunk': 20.083333, 'mean_words_per_chunk': 3.927833, 'median_words_per_chunk': 3.75, 'single_word_chunk_rate': 0.033333, 'long_chunk_rate': 0.327778, 'chunks_per_sentence': 3.027833, 'chunks_per_1000_words': 284.6005, 'char_width_distribution': {'1': 1, '9': 1, '12': 2, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '21': 1, '22': 2, '24': 1, '26': 2, '28': 3, '29': 2, '30': 1, '32': 1}}
- Paired chunk-count behavior: {'parser_fewer_chunks': 5, 'parser_more_chunks': 0, 'identical_chunk_count': 1}

### Blind

- Cases: 16
- Rule-based forbidden violations: {'numerator': 14, 'denominator': 58, 'rate': 0.241379}
- Parser-assisted forbidden violations: {'numerator': 0, 'denominator': 60, 'rate': 0.0}
- Rule-based protected-span splits: {'numerator': 19, 'denominator': 40, 'rate': 0.475}
- Parser-assisted protected-span splits: {'numerator': 3, 'denominator': 42, 'rate': 0.071429}
- Rule-based required-boundary recall: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser-assisted required-boundary recall: {'numerator': 0, 'denominator': 0, 'rate': None}
- Parser fallback: {'cases': 0, 'rate': 0.0}
- Rule-based hard compliance: {'source_coverage_failure': 2, 'dropped_text': 2, 'duplicated_text': 0, 'source_ordering_failure': 1, 'structural_boundary_violations': 0, 'max_width_violations': 0, 'unsafe_mapping_failure': 1}
- Parser-assisted hard compliance: {'source_coverage_failure': 0, 'dropped_text': 0, 'duplicated_text': 0, 'source_ordering_failure': 0, 'structural_boundary_violations': 0, 'max_width_violations': 0, 'unsafe_mapping_failure': 0}
- Rule-based distribution: {'total_chunks': 70, 'chunks_exceeding_density_target': 1, 'mean_chars_per_chunk': 11.239625, 'median_chars_per_chunk': 10.9375, 'mean_words_per_chunk': 1.951, 'median_words_per_chunk': 2.0, 'single_word_chunk_rate': 0.174444, 'long_chunk_rate': 0.0, 'chunks_per_sentence': 4.208312, 'chunks_per_1000_words': 459.940875, 'char_width_distribution': {'3': 1, '4': 2, '5': 4, '6': 2, '7': 2, '8': 7, '9': 3, '10': 5, '11': 7, '12': 7, '13': 4, '14': 9, '15': 5, '16': 2, '17': 3, '18': 2, '20': 2, '21': 1, '22': 2}}
- Parser-assisted distribution: {'total_chunks': 42, 'chunks_exceeding_density_target': 25, 'mean_chars_per_chunk': 23.057313, 'median_chars_per_chunk': 24.3125, 'mean_words_per_chunk': 3.849063, 'median_words_per_chunk': 4.03125, 'single_word_chunk_rate': 0.041667, 'long_chunk_rate': 0.395833, 'chunks_per_sentence': 2.458312, 'chunks_per_1000_words': 273.333563, 'char_width_distribution': {'1': 1, '10': 2, '11': 2, '12': 2, '14': 1, '15': 2, '17': 1, '19': 2, '20': 2, '21': 2, '22': 2, '23': 2, '24': 2, '25': 1, '26': 3, '27': 2, '28': 3, '29': 2, '30': 4, '31': 3, '32': 1}}
- Paired chunk-count behavior: {'parser_fewer_chunks': 14, 'parser_more_chunks': 1, 'identical_chunk_count': 1}

## Interpretation Boundary

No production disposition is made here. S-024 remains pending human A/B review; S-025 owns any later promotion, revision, or abandonment decision.
