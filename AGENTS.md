# AGENTS.md
This file defines how coding agents should work in this repository.

## 1. Core rule
Complete the requested task with the smallest coherent change that satisfies its acceptance criteria.
Do not turn a bounded task into a repository-wide review.
Do not search for additional work after the task is complete.
Optimize for correctness, maintainability, and reviewability—not activity.

## 2. Instruction order
Follow, in order:
1. The current user prompt.
2. This `AGENTS.md`.
3. Repository documentation and conventions.
4. Existing implementation patterns.
5. General engineering judgment.
A specific instruction overrides a general one.

## 3. Scope
Inspect and modify only:
- files named in the task;
- files directly required to implement it;
- directly affected tests;
- directly affected documentation.
Do not:
- fix unrelated defects;
- modernize nearby code;
- reorganize files without necessity;
- upgrade unrelated dependencies;
- perform broad cleanup;
- rewrite working code for style alone;
- expand the task because more work is visible.
Mention unrelated findings briefly in the final report. Do not fix them unless they block the task.

## 4. Before editing
1. Run `git status --short`.
2. Inspect the directly relevant source, tests, and docs.
3. Identify existing behavior and local conventions.
4. Determine the smallest viable implementation.
5. Identify the narrowest relevant validation.
6. Start editing once the task is sufficiently understood.
Do not repeatedly inspect the same files without a concrete unresolved question.
Stop investigating once enough evidence exists to implement safely.
Resolve minor ambiguity from repository evidence. Ask only when a missing decision materially changes the outcome.

## 5. Plan versus implementation
Treat requests to inspect, review, analyze, explain, or plan as non-mutating unless they explicitly ask for changes.
Otherwise, unless the prompt says `PLAN ONLY`, treat the task as implementation.
Implementation workflow:
1. inspect;
2. implement;
3. validate;
4. repair failures caused by the change;
5. review the final diff;
6. commit only when requested or required by the completion language;
7. push only when explicitly required;
8. report after required Git operations succeed.
For non-mutating or `PLAN ONLY` tasks:
- do not modify files;
- do not commit or push;
- return the requested review, analysis, or bounded plan.
“Report after implementation is committed and pushed” means implement, validate, commit, push successfully, then report.

## 6. Implementation discipline
Prefer:
- minimal local patches;
- existing abstractions and conventions;
- direct, readable code;
- deterministic behavior;
- focused tests;
- documentation that matches behavior.
Avoid:
- speculative abstractions;
- premature generalization;
- broad refactors hidden inside feature work;
- duplicate implementations;
- unnecessary compatibility layers;
- hypothetical production hardening;
- comments that restate code;
- generated output without a documented reason.
Preserve public interfaces unless the task explicitly changes them.
Do not alter unrelated behavior.

## 7. Repository constraints
This is a Flask + plain HTML/CSS/JavaScript project.
Do not add a frontend framework, npm dependencies, bundler, transpiler, browser automation, accounts, analytics, databases, cloud sync, or deployment infrastructure unless explicitly required.
Parser-assisted chunking currently uses spaCy for the prototype.
Maintain D-008:
- pass linguistic evidence through project-owned, backend-neutral records;
- keep the RSVP optimizer independent of spaCy objects;
- keep final RSVP policy deterministic and project-owned;
- preserve the rule-based chunker as the deterministic fallback when linguistic evidence is unavailable or unsafe.
Keep provider-specific NLP dependencies isolated from the core optimizer unless explicitly instructed otherwise.
Do not add dependencies without a clear need.

### Codex Windows workspace constraints
In this managed workspace:
- the shell is PowerShell; use PowerShell-safe argument passing and avoid fragile nested quoting;
- for scoped diff review, pass paths as separate arguments: `git diff -- path1 path2 ...`;
- `python` is not on `PATH`, and the repository `.venv` is unusable because its host interpreter target is unavailable;
- when an authorized environment repair needs temporary files, use an untracked repository-local temporary directory, remove it before final diff review, and proceed without pausing to justify the temporary workspace.
- run repository Python scripts with `& 'C:\Users\Usuario\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' <script-and-arguments>`; do not retry `python` or `.venv` first;
- read-only Git commands run normally, but staging, committing, and other `.git` writes require elevated sandbox permission; request it before the first Git write;
- when remote synchronization is required, perform at most one check immediately before the commit/push sequence.

## 8. Validation commands
Use actual repository commands.

### Focused tests
Run the narrowest relevant test first, for example:
```bash
python -m pytest tests/test_rule_based_chunker.py
python -m pytest tests/test_schedule.py
python -m pytest tests/test_web.py
python -m pytest tests/test_defect_api.py
python -m pytest tests/test_navigation_metadata.py
python -m pytest tests/test_parser_assisted_optimizer.py
```
A known individual test may be targeted:
```bash
python -m pytest path/to/test_file.py::test_name
```
Do not repeatedly guess test node IDs.

### Full Python suite
```bash
python -m pytest
```

### JavaScript syntax
For JavaScript or frontend behavior:
```bash
python scripts/check_js_syntax.py
```
If Node is unavailable, report the check as skipped, not passed.

### Markdown links
For Markdown or documentation structure:
```bash
python scripts/check_markdown_links.py
```

### Rule-based fallback and baseline
For fallback, normalization, segmentation, corpus, or baseline-sensitive changes:
```bash
python scripts/validate_chunking_corpus.py
python scripts/freeze_chunking_baseline.py --check
```
Do not use `--write` unless explicitly authorized.

### Parser-assisted integration
Only when the task requires the optional NLP environment:
```bash
python -m pip install -r requirements-nlp-spike.txt
python -m pytest tests/test_parser_assisted_spacy_integration.py
```
Do not install optional NLP dependencies for unrelated work.

### Security
Only when explicitly requested or required:
```bash
python scripts/run_security_checks.py
```
Missing optional validators are skips, not passes.

### No lint or type-check command
The repository has no configured Python linter, formatter gate, static type checker, or consolidated verification command.
Do not:
- invent lint or type-check commands;
- claim checks that were not run;
- add Ruff, Black, mypy, Pyright, or similar tools merely to validate unrelated work.

### No Waiting for Git Actions Verification of Pushed Code
The agent has access to the CI reports and can track their results only when explicity authorized.
Do not:
- wait for CI reports after a git push
- delay your report for CI related reasons

## 9. Validation discipline
Use this sequence:
1. run the narrowest relevant check;
2. fix failures caused by the change;
3. rerun the failed check;
4. run broader validation only when justified;
5. review the final diff once.
Do not:
- rerun successful commands after no relevant changes;
- run the full suite repeatedly while editing;
- use overlapping validators for reassurance;
- treat unrelated warnings as blockers;
- continue after required checks pass;
- regenerate a baseline to hide an unintended change.
Allow at most two repair cycles for the same failure unless explicitly authorized.
If unresolved, stop and report the blocker with evidence.

## 10. Tests and docs
Identify applicable conditional gates using docs/qa/strategy.md and docs/qa/change_validation_map.md; do not apply gates unrelated to the scoped risk.Add or update tests when behavior changes.
Tests should be focused, deterministic, proportionate, and avoid real external services.
Do not add broad test infrastructure for a small change.
Do not weaken assertions merely to obtain a pass.
Documentation must match actual behavior.
Keep `README.md` focused on purpose, setup, common commands, and navigation.
Move detail into focused files under `docs/`.
Do not duplicate explanations or rewrite docs solely to change voice.
Run the Markdown-link checker once after documentation changes settle.

## 11. Dependencies and generated files
Before adding a dependency, consider existing alternatives, maintenance, license compatibility, transitive weight, security, runtime, and packaging impact.
Do not perform unrelated dependency upgrades.
Do not commit:
- virtual environments;
- caches or `__pycache__`;
- temporary diagnostics;
- local benchmark output;
- downloaded models;
- editor or OS noise.
Inspect generated diffs before committing.

## 12. Git discipline
Before editing:
```bash
git status --short
```
Do not overwrite, revert, reformat, or include unexplained user changes.
Before committing:
1. inspect `git status --short`;
2. inspect the final diff;
3. confirm only intended files changed;
4. run required validation;
5. check for secrets, temporary files, and generated noise.
Create one coherent commit per requested slice unless instructed otherwise.
Use a concise commit message describing the completed change.
Do not amend, rebase, reset, clean, stash, force-push, or rewrite history unless explicitly instructed.
Push only when explicitly requested or required before reporting.
When push is not required, do not push.

## 13. Anti-churn
Do not:
- repeatedly reopen the same files;
- repeat successful commands;
- perform equivalent searches;
- reconsider settled decisions without new evidence;
- edit, revert, and recreate substantially the same change;
- restart from first principles after implementation begins;
- continue after acceptance criteria and checks pass;
- search for more work after completion.
A tool call must answer a specific unresolved question or advance the task.
If it does neither, do not make it.

## 14. Iteration limits
Unless explicitly authorized:
- one relevant inspection pass;
- one implementation pass;
- at most two repair cycles for the same failure;
- one final diff review;
- each successful validation command once.
A materially new failure may justify more work, but the reason must be concrete.

## 15. Stop conditions
Stop and report when:
- completion requires changes outside scope;
- the task conflicts with architecture or explicit instructions;
- required credentials, services, dependencies, or data are unavailable;
- user changes prevent safe modification;
- validation reveals an unrelated repository-wide failure;
- two repair cycles fail to resolve the same blocker;
- the outcome requires a major design decision not covered by the prompt;
- committing or pushing would include unrelated work.
Do not hide blockers by broadening scope.
Do not claim completion while acceptance criteria remain unmet.

## 16. Definition of done
A task is complete when:
- the requested behavior or artifact exists;
- the change stays within scope;
- relevant checks pass or skips are reported accurately;
- documentation is updated when required;
- the final diff contains only intentional changes;
- no known defect introduced by the change remains;
- the work is committed when requested or required;
- the commit is pushed when required;
- the final report is accurate.
Once complete, stop.

## 17. Final report
Report:
### Completed
A concise description of the result.
### Changed
- files created, modified, or removed;
- significant behavioral changes.
### Validation
List each command actually run and its result.
Do not claim checks that were not run.
### Git
- branch;
- commit hash, or `Not committed — explicitly not requested`;
- commit message, when committed;
- push result: successful, failed, or not requested.
### Residual issues
List only known limitations, blockers, or relevant follow-up deliberately left out of scope.
If none, say:
`None known within the requested scope.`
Keep the report factual and concise.
