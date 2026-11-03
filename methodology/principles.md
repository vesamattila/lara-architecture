# Principles

## 1. Implementation is evidence, not rationale

A codebase can demonstrate that a behavior, boundary, dependency, or invariant exists. It usually cannot prove why the original authors chose it.

LARA may recover a decision from implementation evidence without inventing the original rationale.

## 2. Separate observation from interpretation

Every meaningful claim must be classified as one of:

- **OBSERVED** — directly supported by repository evidence.
- **INFERRED** — a reasoned architectural interpretation.
- **UNKNOWN** — relevant context that cannot be established reliably.

Do not blur these categories.

## 3. Evidence before ADRs

Architecture reconstruction starts with evidence records.

Do not begin by writing ADRs and then search for supporting evidence. That creates confirmation bias.

## 4. Preserve uncertainty

When multiple explanations fit the evidence:

- preserve the alternatives,
- state what evidence would discriminate between them,
- lower confidence,
- do not force consensus.

## 5. Current consequences matter more than guessed history

Historical rationale can be valuable when explicit evidence exists.

Always distinguish:

- historical rationale,
- current architectural consequence.

## 6. Inconsistency is evidence

Different patterns in different parts of a legacy system may indicate deliberate bounded differences, migrations in progress, organizational history, abandoned refactors, framework transitions, or technical debt.

Do not normalize these differences away.

## 7. Tests are architectural evidence

Tests often encode stronger intent than implementation details.

## 8. Negative space matters

Absence can be significant, but negative evidence should have lower confidence unless reinforced by other sources.

## 9. Challenge attractive explanations

The most dangerous reconstruction is a coherent story with weak evidence.

## 10. Architectural memory exists to support change

The output is useful only if future agents can answer:

- What must this change preserve?
- Which architectural decisions does it touch?
- Which constraints are accidental versus intentional?
- Which anomalies make this area risky?
- Does this change supersede an existing decision?
