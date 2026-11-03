# ADR-RXXX — <recovered decision>

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: <agent instance>
  source_item: null
review_status: pending-adversarial-review
reviewed_by: null
```

Status: Recovered
Decision confidence: High | Medium | Low
Rationale confidence: High | Medium | Low | Unknown

## Recovered decision

State the architectural decision supported by current evidence.

## Evidence

- E-<ROLE>-<INSTANCE>-<NNN>
- E-<ROLE>-<INSTANCE>-<NNN>

Do not cite superseded evidence as current support.

When citing annotated evidence, account for the annotation explicitly.

## Observed context

Describe only context supported by evidence.

## Original rationale

Document explicit historical rationale if available.

Otherwise:

**Unknown.**

## Current consequences

Describe what the present system relies upon because of this decision.

## Competing interpretations

List plausible alternatives when evidence is inconclusive.

## Change implications

What would a future implementation need to preserve, or explicitly supersede?

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

- CON-XXX
- ANO-XXX
- AQ-XXX

## Adversarial review

Review status: reviewed | lead-verified | unverified
Verdict: CONFIRMED | STRENGTHENED | NARROWED | RECLASSIFIED | CONFIDENCE DOWNGRADED | CONTRADICTED | UNRESOLVED CHALLENGE

Reviewer:
Reviewer notes:

After required review, update `review_status` and `reviewed_by` according to `methodology/artifact-provenance.md`.

Use `methodology/review-model.md` to select exactly one primary verdict.
