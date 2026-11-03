# Architecture artifact provenance

Every reconstructed architecture item records how it entered LARA's architectural memory.

This applies to:

- recovered ADRs,
- constraints,
- anomalies,
- open questions.

## Required provenance

Normal reconstruction output begins with:

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: <agent instance>
  source_item: null
review_status: pending-adversarial-review
reviewed_by: null
```

Items discovered during adversarial review begin with:

```yaml
provenance:
  discovered_during: adversarial-review
  discovered_by: SKEP-01
  source_item: ADR-R004
review_status: pending-independent-review
reviewed_by: null
```

`source_item` is optional and should identify the item whose review led to the new discovery.

## Review status and verdict

Review status answers whether required review has happened.

Review verdict answers what that review concluded.

The canonical verdict taxonomy lives in `methodology/review-model.md`.

Do not encode verdict meaning into `review_status`.

## Review status values

Allowed values:

- `pending-adversarial-review`
- `pending-independent-review`
- `reviewed`
- `lead-verified`
- `unverified`

### pending-adversarial-review

Normal state for an item produced during Reconstruction before Phase 4.

### pending-independent-review

Required initial state for an item first discovered by a Skeptic during Phase 4.

### reviewed

An appropriate independent reviewer completed the required review.

Set `reviewed_by` and record exactly one review verdict using `methodology/review-model.md`.

### lead-verified

The Lead independently verified a review-discovered item when another Skeptic instance was not available or appropriate.

Set `reviewed_by` to the Lead instance and record the verification conclusion using the same canonical verdict taxonomy when a verdict is applicable.

### unverified

The item is retained because it is useful or important, but independent verification was not completed.

UNVERIFIED must remain visible to future consumers and must not be presented as settled architecture.

## G2 verification requirement

Every item with `discovered_during: adversarial-review` is governed by **G2 — Review Discovery Verification Gate** in `methodology/workflow-gates.md`.

Changing `review_status` from `pending-independent-review` requires an independent primary-source check.

A different agent name alone does not satisfy G2.

## No self-confirmation

An agent that discovers an architecture item cannot provide the independent review required for that same item's acceptance.

In particular:

- `SKEP-01` may discover `ANO-012`,
- `SKEP-01` may provide evidence for it,
- `SKEP-01` may not mark it independently reviewed.

A different Skeptic instance or the Lead must perform the independent verification.

The verifier must inspect primary evidence and perform at least one fresh confirmation or counterexample search.

If this does not happen, preserve the item as `unverified`.

## Review verdict

A completed adversarial review records exactly one primary verdict:

- CONFIRMED
- STRENGTHENED
- NARROWED
- RECLASSIFIED
- CONFIDENCE DOWNGRADED
- CONTRADICTED
- UNRESOLVED CHALLENGE

Use `methodology/review-model.md` for definitions and boundary cases.

A completed `review_status: reviewed` without a verdict is incomplete.

An `unverified` item has no completed verdict.

## Reclassification

When adversarial review concludes that an architecture item was classified incorrectly, preserve its existing ID.

Record the review outcome and change the item's interpretation/type only through explicit review notes and provenance.

Do not silently delete the old identity and create a cosmetically clean replacement.

## Relationship to evidence provenance

Architecture-item provenance and evidence provenance answer different questions:

- evidence provenance: **who observed this fact, and when?**
- architecture-item provenance: **who synthesized this architectural interpretation, and when?**

Neither one proves correctness. Correctness still depends on evidence quality and review.
