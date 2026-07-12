# QA Strategy

## Purpose And Limits

The framework connects existing verification assets into a traceable,
risk-based quality system. It selects evidence; it does not create parallel
management authority, duplicate setup or test procedures, or authorize fixes.

Authority order for QA work is:

1. [STATUS](../management/STATUS.md) for active scope, state, and ownership.
2. The active slice document and tracked GitHub issue for acceptance scope.
3. Root [AGENTS.md](../../AGENTS.md) for execution and narrow-before-broad validation discipline.
4. The [environment contract](../development/environment_contract.md) for runtime, profile, setup, and identity.
5. This QA layer for risks, gate applicability, evidence requirements, and terminology.
6. Tests, characterizations, protocols, and experiment records as evidence authorities.

Principal quality dimensions are functional correctness, deterministic and
safe fallback, semantic and timing integrity, interaction and accessibility,
service and privacy boundaries, reproducibility, environment consistency,
scientific integrity, and truthful management state.

## Conditional Gates

Gates are conditional; the [verification matrix](verification_matrix.md) and
[change map](change_validation_map.md) identify the applicable subset.

1. **Repository gate** — repository integrity, Markdown links, evidence structure, management/archive consistency, and applicable frozen-artifact consistency.
2. **Core gate** — dependency-light tests, rule-based behavior, applicable baseline and JavaScript checks, and core-profile smoke evidence.
3. **Standard gate** — standard dependency consistency, applicable parser integration/parity/freeze checks, parser-default smoke evidence, and pinned provider state.
4. **Change-specific gate** — focused tests, characterizations, or checks directly associated with the change.
5. **Human gate** — rendered behavior, device interaction, accessibility, comprehension, pacing, qualitative chunking, or other judgment automation cannot establish.
6. **Disposition gate** — recorded evidence is accepted, rejected, deferred, inconclusive, or returned for stabilization by the authorized owner.

S-038 adds one bounded Playwright/Chromium-family smoke runner to the change-specific gate. It protects named critical flows and one catastrophic narrow-layout invariant; it supplements rather than replaces the human gate for rendered quality, touch behavior, accessibility, pacing, comprehension, and device/browser judgment.

S-038A makes the pinned standard-profile Parser CI gate authoritative for the S-024/S-037 evaluation surface. Changes to that surface must schedule Parser CI, execute its focused tests, and reproduce the committed S-037 characterization without changing evaluation policy or frozen evidence.

## Entry, Exit, And Evidence States

Generic entry requires an authorized active scope, initiating evidence, known
boundaries, and identified applicable gates. Generic exit requires the scoped
artifact, executed applicable checks, retained evidence, truthful unresolved
items, and an authorized disposition. Slice-specific criteria always control.

Applicability/readiness terms:

- `required`: the gate applies.
- `prepared`: tooling, scaffolding, or a protocol exists.
- `executed`: the check or protocol was run.

Execution outcomes are `passed`, `partially_passed`, `failed`, `skipped`, and
`inconclusive`. Disposition outcomes are `accepted`, `deferred`, `rejected`, and
`returned_for_stabilization`. Execution outcome and final disposition are
separate fields. Prepared is not executed; automated preparation cannot pass a
human gate; only the human records human acceptance; an automated pass cannot
supersede required human judgment.

## Experimental-Governance Overlay

Parser experiments and frozen evaluation artifacts carry stronger controls than
ordinary product checks. Preserve registered hashes and manifests, blind-data
exclusions, project-owned linguistic records, mandatory rule-based fallback,
and separate authorization for scientific changes. Never retune without
authorization or regenerate a baseline to conceal behavior changes. The
[experiment contract](../experiments/parser_assisted_chunking/experiment_contract.md),
[contamination policy](../experiments/parser_assisted_chunking/contamination_policy.md),
[baseline freeze](../experiments/parser_assisted_chunking/baseline_freeze.md),
[decision D-009](../management/DECISIONS.md), and freeze records under
`evaluation/parser_assisted_chunking/freeze/` remain authoritative.

Validating the adopted parser-default path does not authorize modifying the
experiment, parser operating policy, weights, corpus, or frozen artifacts.
