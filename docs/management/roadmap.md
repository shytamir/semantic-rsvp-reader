# 4-Week Calibration Roadmap

The goal of the next 4 weeks is to refine the reading experience using observed defects rather than speculative feature additions.

### Week 1: Instrumented Defect Collection
**Goal:** Make mobile validation practical and turn reports into usable evidence.
* **[ ] Slice 1: In-App Backend Defect Reporting**
  * *Gate:* Can read on phone, tap "Report Defect", submit, and find a compressed Markdown report on the backend.
  * *Details:* Adds UI reporting form capturing current/surrounding chunks, speed, adaptation state, and device info via `POST /api/defects`.
* **[ ] Slice 2: Defect Report Review Utility**
  * *Gate:* One local command (`python scripts/review_defects.py`) produces a readable defect summary aggregated by category and severity.
* **Human Workload:** 1-2 hours of pure phone reading across 2-4 samples to collect initial defects.

### Week 2: Chunking Refinement Cycle 1
**Goal:** Fix observed chunk boundary problems and prevent rule regressions.
* **[ ] Slice 3: Chunking Refinement from Reports**
  * *Gate:* Top recurring chunking defects are fixed via test-driven minimal rule changes (e.g., addressing negation, auxiliary chains, punctuation attachment).
* **[ ] Slice 4: Chunking Regression Corpus**
  * *Gate:* A stable test file exists containing representative validation sentences and known tricky cases to protect against backsliding.
* **Human Workload:** 30-60 minutes evaluating before/after outputs to ensure cognitive improvement over technical cleverness.

### Week 3: Timing Calibration Cycle 1
**Goal:** Separate timing defects from chunking defects and improve rhythm/dwell behavior.
* **[ ] Slice 5: Timing Defect Collection / Review**
  * *Gate:* Clear distinction achieved between "bad timing" (rushed/overpaused/fatigue) and "bad chunking" via report payloads.
* **[ ] Slice 6: Timing Engine Calibration**
  * *Gate:* A 10-15 minute reading session feels calmer.
  * *Details:* Formulaic, inspectable refinements to comma/semicolon pauses, sentence-ending pauses, and capping very short light chunks.
* **Human Workload:** 1 hour reading 2-3 samples to purely judge rhythm and speed.

### Week 4: Validation, Demo, and Decision Point
**Goal:** Evaluate real reading sessions and prepare for external testing.
* **[ ] Slice 7: Controlled Validation Pass**
  * *Gate:* Can run a full 15-30 minute validation session producing usable notes against documented decision criteria.
* **[ ] Slice 8: Demo/Beta Readiness Pass**
  * *Gate:* An external tester can run or use the app with minimal explanation. Includes simple run instructions, sample texts, and removal of debug clutter.
* **Human Workload:** 2-3 hours for one personal serious validation session, plus observing 1-2 external testers to identify friction points.