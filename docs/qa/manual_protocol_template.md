# Manual Validation Protocol Template

Copy this structure for new human protocols. Reference an authoritative
environment identity rather than retranscribing it when possible. Historical
protocols are not rewritten to match this template.

```markdown
# <Protocol title>

## Objective
<Bounded human judgment this protocol establishes.>

## Target And Environment
- Target commit:
- Environment/profile or authoritative environment-record link:
- Configured chunker mode:
- Active chunker mode/provider state:
- Device / operating system / browser / viewport, when applicable:
- Validation sample or corpus identifier:

## Fixed Procedure
| Step | Action | Expected result | Outcome |
| --- | --- | --- | --- |
| 1 | | | `passed` / `partially_passed` / `failed` / `skipped` / `inconclusive` |

## Observations And Issues
- Observation, classification, blocking status, and issue/follow-up link:

## Final Human Disposition
- Execution outcome:
- Disposition: `accepted` / `deferred` / `rejected` / `returned_for_stabilization`
- Task-specific decision:
- Acceptance-blocking defects:
- Authorized follow-up:

## Evidence Handling
- Retained committed evidence:
- Private/generated evidence deleted or retained outside Git:
```

Only the human records human acceptance. A prepared template or automated pass
is not an executed human gate.
