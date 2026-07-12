# Change-Validation Map

Select the smallest gate set covering the concrete risk. Run focused checks
before broader applicable checks as required by [AGENTS.md](../../AGENTS.md).

| Change category | Principal risk | Applicable gates | Profile | Human gate | Authority |
| --- | --- | --- | --- | --- | --- |
| Documentation | Broken or false guidance | Repository, Change-specific | None unless commands exercised | Procedural usability when required | AGENTS.md link/integrity rules |
| Management/evidence | False state, provenance, retention or hash drift | Repository, Change-specific, Disposition | Evidence-producing profile if needed | Required for human-owned disposition | [STATUS](../management/STATUS.md), archive policy in [testing](../development/testing.md) |
| Core Python behavior | Functional or fallback regression | Core, Change-specific | Core | If output needs judgment | [Verification matrix](verification_matrix.md), focused tests |
| Parser-sensitive behavior | Provider, alignment, optimizer, fallback | Core, Standard, Change-specific; experiment controls when relevant | Both | Often required for semantic quality | [Experiment contract](../experiments/parser_assisted_chunking/experiment_contract.md) |
| Timing/schedule logic | Pacing or duration-policy regression | Core, applicable Standard, Change-specific | Applicable | Required for perceptual pacing changes | [Timing](../features/timing.md) |
| Frontend/presentation | Rendered collision, overflow, lifecycle | Change-specific browser smoke, Human | Applicable | Normally mandatory | [S-038 browser baseline](../validation/s038_minimal_browser_regression_baseline.md), [manual testing](../development/manual_testing.md) |
| Accessibility/interaction | Target, focus, gesture, orientation | Change-specific, Human | Applicable | Mandatory for device-dependent claims | Existing accessibility/navigation protocols |
| Dependencies/profiles | Install inconsistency or provider identity | Repository, affected Core/Standard, Change-specific | Changed profiles | Remaining platform/setup usability only | [Environment contract](../development/environment_contract.md) |
| CI/workflows | Missing or misleading remote gate | Repository, affected gate, Change-specific | Workflow profile | Normally no; inspect actual remote evidence | Workflows and [testing](../development/testing.md) |
| Manifests/baselines/hashes/freeze records | Contamination or concealed scientific drift | Repository, applicable Core/Standard, Change-specific, Disposition | Registered environment | As experiment authority requires | Experiment controls and freeze records |

Gate applicability does not authorize correction, experiment modification, or
scope expansion. Record a newly exposed gap and obtain authority.
