# S-037 Evaluation Anomaly and Parser Operating-Policy Decision

## Evidence Boundary

This packet uses only repository-safe, redacted S-023/S-024 and integration
evidence. It does not require, reconstruct, expose, or infer the private A/B
identity key, blind source text, annotations, raw chunks, or per-case system
mappings. Historical artifacts and reports remain unchanged.

Machine-readable evidence: [S-037 characterization](../../evaluation/evaluation_anomaly_policy/s037_characterization.json).

## Reproduced Classifications

| Evidence | Classification | Finding |
| --- | --- | --- |
| Eight visible regression and six visible generalization cases | Annotation/denominator coverage | Both systems have zero annotation denominators because these visible cases were supplied without annotations. Distribution and hard-compliance results remain usable; `0/0` is not evidence of zero violations. |
| Blind case identities and provenance | Integrity check passed | All 16 redacted case IDs and source hashes are unique; annotation validation reports no failure; implementation/config identities and visible manifest hashes match the registered freeze. |
| `blind-0004` rule-based record | Historical source-to-chunk mapping failure | Mapping failed and the output was unscorable. The historical runner could defensibly report unsafe mapping and remove annotation denominators, but could not infer dropped text, source-coverage failure, or ordering failure. |
| `blind-0011` rule-based record | Product behavior observed in the historical run | Mapping succeeded but non-whitespace source coverage differed. This is a separate historical rule-based coverage failure; its private source is neither needed nor reconstructed. |
| Blind hard-compliance summary | Reporting-only anomaly | Historical totals report two coverage/dropped-text failures and one ordering failure. Defensible classification is one confirmed coverage/dropped-text failure, zero confirmed ordering failures, and one separate unsafe/unscorable mapping failure. |
| Rule/parser blind denominator differences | Reporting-only consequence | Rule denominators are lower exactly by `blind-0004` parser denominators because rule annotations were removed after mapping became unscorable. This is expected, not case-identity drift. |
| Generic required-boundary recall `0/0` | Annotation coverage | The blind annotations contain no generic `required` boundaries. Two `required_structural` boundaries are separately reported and must not be conflated with generic recall. |
| Repository-owned `dev-quote-0007` in explicit rule mode | Public product-behavior analogue | Curly-quote source-character loss reproduces a rule-based coverage-failure class without mapping failure. It bounds the limitation but does not identify the private `blind-0011` source. |

## Narrow Plumbing Repair

Future `run_s024_comparison.py` executions now classify a mapping failure only as
unsafe and unscorable. They no longer automatically assert dropped text,
source-coverage failure, or ordering failure. Annotation denominators remain
removed for an unscorable system output. Focused tests protect both behaviors.

This repair changes evaluation reporting only. It does not change frozen S-024
evidence, rule-based or parser output, the optimizer, model pins, integration,
fallback behavior, or current policy.

## Policy Evidence

- D-009 and the integration record establish `parser_assisted` as the current Flask prototype default, `rule_based` as the explicit baseline mode, and `RuleBasedChunker` as mandatory fallback.
- S-024 parser-assisted output had no blind mapping or source-coverage failure, no fallback, and won all 12 decisive human comparisons. These are historical bounded results, not universal superiority claims.
- S-030 and S-036 accepted parser-default reading and explicit rule-based operation for the stabilized prototype.
- Rule-based operation remains deterministic and dependency-light, but the recorded blind and public coverage limitations show why it should not be treated as semantically equivalent to parser-default output.
- Automatic fallback is defensible when the provider/model is unavailable, parsing fails, alignment is unsafe, optimization has no complete path, or hard postconditions fail. Health and logs expose mode/reason without source text; fallback must not download a model at runtime.
- The S-037 reporting repair reduces historical rule hard-compliance counts but does not erase the confirmed `blind-0011` coverage failure or the parser-assisted qualitative evidence.

## Limitations And Inference

Evidence cannot establish the private causes of `blind-0004` or `blind-0011`
without prohibited source reconstruction. The public curly-quote analogue
supports a failure class, not identity equivalence. Visible unannotated corpora
support distribution and compliance comparisons but not annotated boundary-rate
claims. Automatic fallback quality depends on rule-based limitations already
accepted for availability, not on parity with parser-default output.

Inference: the current combined policy remains internally coherent after the
reporting correction, but a policy choice belongs to the human. Choosing a new
default would authorize a later management/implementation transition, not a
behavior change inside S-037.

## Fixed Human Decision Handoff

1. Confirm the classifications separate product behavior, historical runner behavior, annotation coverage, mapping failure, and reporting-only effects.
Human confirmed.
2. Confirm identities/provenance are sufficient without private A/B material and that the historical S-023/S-024 evidence remains unchanged.
Human confirmed sufficiency and unchanged status of evidence.
3. Confirm the plumbing repair no longer turns an unscorable mapping into unsupported product-failure claims while preserving unsafe-mapping and denominator handling.
Human confirmed the repair doesn't violate product-failure support while preserving original handling.
4. Review the three operating-policy options and record exactly one disposition:

   - `retain_parser_default_with_mandatory_automatic_fallback` — retain parser-default behavior, explicit rule mode, and automatic rule fallback under the existing safe triggers.
   - `prefer_explicit_rule_based_as_default` — choose dependency-light rule behavior as the future default while acknowledging the recorded coverage and qualitative limitations; implementation requires separate authorization.
   - `additional_evidence_required` — keep current behavior provisionally and specify the smallest missing evidence before deciding.
Human recorded disposition below.
5. Record rationale, accepted limitations, any required follow-up issue, and whether S-038 may be activated separately.

## Human Disposition

`retain_parser_default_with_mandatory_automatic_fallback`
We're seeing acceptable behavio from the new parser default, and the reapir won't hurt the fallback. The only violation is of arbitrary limit on number of acceptable expected S-023/S-024 failing tests. Human accepts the recorded limitations of unsafe mapping and unscorable output. No required follow-up issue. S-038 may be activated after this slice concludes, which it should considering the positive, non-blocking human dispostion recorded.