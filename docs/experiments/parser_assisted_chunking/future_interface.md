# Future Implementation Interface

The parser-assisted path should separate linguistic evidence, RSVP boundary optimization, and the existing schedule layer.

## Linguistic Feature Extractor

Produces project-owned records. Do not expose parser-native objects outside the adapter.

Fields may include:

- Source text and character offsets.
- Sentence membership.
- Part of speech.
- Dependency relation.
- Head relationship by project-owned ID.
- Entity type.
- Named-entity spans.
- Noun-phrase spans.
- Clause-related indicators.
- Numerical or date-related spans.
- Alignment confidence.

Parser failure or unsafe token alignment must fall back to the production baseline.

## Boundary Optimizer

Consumes:

- Normalized source text.
- Project-owned linguistic features.
- Structural constraints.
- RSVP presentation constraints.

Produces:

- Selected chunks.
- Character boundary positions.
- Boundary scores.
- Human-readable reasons.
- Fallback status.

## Existing Timing And Schedule Layer

The existing timing and schedule layer remains downstream and unchanged. A future parser-assisted implementation must preserve the current schedule contract unless a separately approved slice changes it.
