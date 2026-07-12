# Verification Matrix

Gate names refer to the [QA strategy](strategy.md). Commands and profile setup
remain governed by [AGENTS.md](../../AGENTS.md) and the
[environment contract](../development/environment_contract.md).

| Product area | Principal risks and triggers | Gates | Profile | Automated evidence | Human evidence | Authority/evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Normalization and segmentation | Text loss, offsets, sentence boundaries; normalization/segmentation changes | Repository, Core, Change-specific | Core | `tests/test_normalize.py`, `tests/test_segment.py`, corpus validator | When meaning or difficult structure requires judgment | [Chunking](../features/chunking.md), [corpus](../validation/corpus.md) |
| Rule-based chunking | Boundary or fallback drift; rules/config changes | Repository, Core, Change-specific | Core | rule chunker tests, visible corpus, frozen baseline check | Qualitative output when scoped | [Baseline freeze](../experiments/parser_assisted_chunking/baseline_freeze.md) |
| Parser-assisted chunking | Provider, alignment, optimizer, fallback; adapter/record/optimizer changes | Repository, Core, Standard, Change-specific; Human when qualitative | Standard plus Core fallback | parser optimizer/integration/freeze tests and experiment runner | Fixed semantic protocol when required | [Experiment README](../experiments/parser_assisted_chunking/README.md), freeze records |
| Timing and schedule | Dwell, duration, serialization; timing/config/schedule changes | Core, applicable Standard, Change-specific; Human for pacing | Applicable | schedule, timing, API, calibration tests/characterizations | Fixed pacing protocol | [Timing](../features/timing.md), timing validation records |
| Playback and adaptation | Lifecycle, timer, reset, visibility, session adaptation | Change-specific, Human | Applicable | S-031 characterization and applicable static tests | Phone-browser lifecycle and pacing | [S-031 validation](../validation/archive/s031_playback_adaptation_validation.md) |
| Navigation and structural metadata | Direction, seek, breakpoints, drift, hierarchy | Change-specific, Human | Applicable | navigation tests and S-032 characterization | Fixed interaction protocol | [Navigation](../features/navigation.md), [validation](../validation/navigation_validation.md) |
| Presentation and responsive layout | Collision, overflow, hierarchy; HTML/CSS changes | Change-specific, Human | Applicable | mobile shell and S-033 characterization | Required rendered viewport review | [S-033 validation](../validation/archive/s033_mobile_presentation_accessibility_validation.md) |
| Accessibility and touch interaction | Aimability, focus, cues, gestures | Change-specific, Human | Applicable | focused static assertions where meaningful | Device, viewport, keyboard/touch judgment | [Issue #11 protocol](../validation/issue_11_coarse_seek_accessibility_validation.md) |
| Defect capture and evidence | Context, privacy, retention, reproducibility | Repository, Change-specific; Human for usability | Applicable | defect API/storage/review tests and S-034 characterization | Capture/review practicality | [Defect reporting](../features/defect_reporting.md), [S-034 validation](../validation/s034_evidence_capture_reproducibility_validation.md) |
| Flask service contracts | Method, schema, JSON, health | Core, applicable Standard, Change-specific | Both as applicable | API/web/service tests and S-035 characterization | Startup/browser checks when scoped | [S-035 validation](../validation/s035_service_surfaces_fallback_validation.md) |
| Provider availability and fallback | Startup failure, health state, unsafe fallback | Core, Standard, Change-specific | Both | selection, integration, web, smoke, parser CI | Operational startup evidence when required | [Environment contract](../development/environment_contract.md), [Chunking](../features/chunking.md) |
| Dependency and environment integrity | Unreproducible install, wrong profile/provider | Repository, affected profile, Change-specific | Core and/or Standard | dependency/CI identity and environment-contract tests | Remaining platform/setup usability | [Environment contract](../development/environment_contract.md) |
| Experimental and frozen artifacts | Contamination, stale hashes, unauthorized scientific change | Repository, applicable Core/Standard, Change-specific, Disposition | Registered environment | integrity/freeze/hash/comparison validators | Blind or qualitative authority when required | [Experiment contract](../experiments/parser_assisted_chunking/experiment_contract.md), [freeze directory](../../evaluation/parser_assisted_chunking/freeze/) |

Rendered layout, touch targeting, gestures, viewport interaction, and browser
lifecycle currently depend on controlled human validation; static assertions do
not replace it. The minimal browser regression baseline belongs to S-038.
