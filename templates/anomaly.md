# ANO-XXX — <architectural anomaly>

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: <agent instance>
  source_item: null
review_status: pending-adversarial-review
reviewed_by: null
```

Status: Observed | Suspected | Transitional
Confidence: High | Medium | Low

## Observation

Describe the architectural tension, inconsistency, duplication, unfinished migration, or divergence.

## Evidence

- E-<ROLE>-<INSTANCE>-<NNN>

Do not cite superseded evidence as current support.

When citing annotated evidence, account for the annotation explicitly.

## Why it matters

Explain the maintenance, correctness, operability, or change risk.

Do not label the anomaly a defect unless evidence supports that conclusion.

## Possible explanations

List alternatives without forcing a conclusion.

## Known impact

Describe demonstrated impact separately from hypothetical risk.

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
- CON-XXX
- AQ-XXX

## Adversarial review

Review status: reviewed | lead-verified | unverified
Verdict: CONFIRMED | STRENGTHENED | NARROWED | RECLASSIFIED | CONFIDENCE DOWNGRADED | CONTRADICTED | UNRESOLVED CHALLENGE

Reviewer:
Reviewer notes:

After required review, update `review_status` and `reviewed_by` according to `methodology/artifact-provenance.md`.

Use `methodology/review-model.md` to select exactly one primary verdict.
