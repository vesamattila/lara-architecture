# AQ-XXX — <open architectural question>

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: <agent instance>
  source_item: null
review_status: pending-adversarial-review
reviewed_by: null
```

Status: Open

## Question

State the unresolved architectural question.

## Why it matters

Explain what future decision or risk depends on the answer.

## Evidence

- E-<ROLE>-<INSTANCE>-<NNN>

Do not cite superseded evidence as current support.

When citing annotated evidence, account for the annotation explicitly.

## Plausible explanations

1. ...
2. ...

## Missing evidence

What information would help resolve the question?

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
- ANO-XXX

## Review

Review status: reviewed | lead-verified | unverified
Verdict: CONFIRMED | STRENGTHENED | NARROWED | RECLASSIFIED | CONFIDENCE DOWNGRADED | CONTRADICTED | UNRESOLVED CHALLENGE

Reviewer:
Reviewer notes:

For review-discovered questions, independent review or explicit UNVERIFIED status is mandatory.

Update `review_status` and `reviewed_by` according to `methodology/artifact-provenance.md`.

Use `methodology/review-model.md` for any completed review verdict.
