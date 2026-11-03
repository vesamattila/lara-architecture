# CON-XXX — <constraint>

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: <agent instance>
  source_item: null
review_status: pending-adversarial-review
reviewed_by: null
```

Status: Active | Scope-limited | Historical | Uncertain
Confidence: High | Medium | Low

## Constraint

State the limitation, invariant, compatibility requirement, or consistency boundary.

## Evidence

- E-<ROLE>-<INSTANCE>-<NNN>

Do not cite superseded evidence as current support.

When citing annotated evidence, account for the annotation explicitly.

## Scope

Where does this constraint apply?

## Consequences

What design choices does it restrict or shape?

## Failure mode

What is known or expected to happen if the constraint is violated?

Separate demonstrated behavior from inferred risk.

## Affected territory

Navigation metadata for future coding agents.

Paths:

- `path/or/glob/**`

Modules:

- `stable-module-name`

Cross-cutting: true | false

Rules:

- paths and modules must reflect evidence-backed scope,
- prefer the narrowest stable useful territory,
- do not broaden scope merely to improve manifest coverage,
- use `Cross-cutting: true` only when path matching alone would be unsafe,
- leave paths empty when scope cannot be represented honestly by repository paths.

## Related items

- ADR-RXXX
- ANO-XXX
- AQ-XXX

## Adversarial review

Review status: reviewed | lead-verified | unverified
Verdict: CONFIRMED | STRENGTHENED | NARROWED | RECLASSIFIED | CONFIDENCE DOWNGRADED | CONTRADICTED | UNRESOLVED CHALLENGE

Reviewer:
Reviewer notes:

After required review, update `review_status` and `reviewed_by` according to `methodology/artifact-provenance.md`.

Use `methodology/review-model.md` to select exactly one primary verdict.
