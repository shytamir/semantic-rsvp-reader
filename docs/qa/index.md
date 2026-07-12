# QA Authority

This directory is the compact authority for quality risks, conditional gates,
evidence requirements, and disposition terminology. It does not replace
[project status](../management/STATUS.md), active slice or issue scope, the
[agent execution rules](../../AGENTS.md), the
[environment contract](../development/environment_contract.md), executable
tests and characterizations, human protocols, or experiment freeze records.

- [Strategy](strategy.md): authority boundaries, quality dimensions, gates, and evidence states.
- [Verification matrix](verification_matrix.md): product risks mapped to profiles, evidence, and authorities.
- [Change-validation map](change_validation_map.md): risk-based gate selection by change category.
- [Defect lifecycle](defect_lifecycle.md): classification, authorization, correction, deferral, and closure.
- [Manual protocol template](manual_protocol_template.md): reusable human-evidence structure.

Apply only the gates required by the active scope and change risk. Prepared
evidence is never represented as executed evidence, and automation cannot
declare a required human gate passed.
