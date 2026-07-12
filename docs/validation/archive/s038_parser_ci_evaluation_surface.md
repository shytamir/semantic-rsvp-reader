# S-038A Parser CI Evaluation-Surface Coverage Validation

## Implemented Scope

The existing Parser CI job now supports manual dispatch and triggers when the
five S-024/S-037 evaluation-surface paths listed in GitHub issue #23 change.
Its existing pinned Python 3.12 standard profile, dependency assertions,
parser-integration tests, S-030 characterization, and parser-default Flask
smoke remain in place. The same parser validation step now also runs the S-024
comparison tests, S-037 anomaly-characterization tests, and the committed S-037
characterization through its existing `--check` command.

No job, dependency, parser behavior, evaluation logic, assertion, frozen
evidence, manifest, annotation, or private A/B material changed. The subsequent
stabilization is limited to normalizing S-037 text-file source-evidence identity
across LF and CRLF checkouts.

## Executed Evidence

- The focused S-037 characterization tests passed: 5 tests, including
  equivalent LF/CRLF source-evidence identity.
- The complete updated Parser CI validation command passed locally under the
  managed standard profile: dependency integrity and exact pins passed; all 38
  selected tests passed.
- The S-030 characterization check passed.
- The normalized S-037 characterization reproduced successfully with
  `--check`.
- The parser-default Flask smoke passed.
- The full repository suite passed: 297 tests.
- Markdown links and diff whitespace checks passed.

## Limitations And Remote Status

Parser CI run `29207917112` and General CI run `29207917075` are authoritative
failed evidence. Both failed the committed S-037 characterization
reproducibility test because its text-file source-evidence hashes were derived
from checkout bytes and therefore differed between Windows CRLF and Ubuntu LF
working trees. S-038A returned to Codex-owned stabilization for the localized
identity correction and remote revalidation.

Repair commit `723f620` passed Parser CI run `29208667633` and General CI run
`29208667636`. CodeQL run `29208667359` was still in progress at the immediate
post-validation snapshot and is not an S-038A acceptance gate.

This maintenance evidence does not establish parser quality, reinterpret
S-024/S-037 evidence, or authorize evaluation, parser, fallback, or product
changes.

## Human Disposition

Review the implemented trigger list, manual dispatch, focused standard-profile
test execution, S-037 characterization reproducibility, preservation of the
existing Parser CI checks, and the immediately available remote status.

Record exactly one outcome in GitHub issue #25:

- `passed`
- `partially_passed`
- `failed`
- `inconclusive`

The human disposition was initially `inconclusive` pending remote evidence.
After the localized correction, both required remote workflows passed. The
final S-038A outcome is `passed`. S-039 remains provisional, inactive, and
unauthorized.
