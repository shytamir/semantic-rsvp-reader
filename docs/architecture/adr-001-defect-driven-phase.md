# ADR 001: Transition to Defect-Driven Validation

**Date:** 2026-07-09  
**Status:** Accepted  

## Context
The RSVP mobile reader prototype roadmap has been completed. The core engine (Flask backend, chunking, timing, telemetry, mobile HTML5 shell) is fully operational. The standard software development instinct is to immediately build breadth: user accounts, database persistence, EPUB ingestion, or cloud deployment. 

However, the core risk of the project is no longer technical feasibility ("Can we build it?"), but cognitive friction ("Where does the reading experience fail?").

## Decision
We are freezing all speculative feature development. For the next 4 weeks, development will be strictly driven by **observed defects**. 

If a proposed change does not stem from a real defect report, make validation more reliable, or make testing easier, it will not be built. We will rely on local filesystem storage (compressed Markdown files) for defect capture rather than standing up a database infrastructure.

## Consequences
* **Positive:** Forces absolute focus on the quality of the rule-based chunker and timing engine. Collapses the feedback loop between reading on a phone and fixing the algorithm.
* **Negative:** The application remains a localized, single-user prototype without cloud persistence or automated document ingestion for another month.
* **Mitigation:** We will build a highly frictionless, in-app defect reporting tool to ensure that capturing reading errors does not interrupt the reading session itself.