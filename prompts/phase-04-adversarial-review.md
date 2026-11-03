# Phase 04 — Adversarial Review

## Goal

Attempt to falsify every reconstructed architecture item.

Read:

- `agents/architecture-skeptic.md`
- `methodology/review-model.md`
- `methodology/evidence-lifecycle.md`
- `methodology/artifact-provenance.md`

before review begins.

## Skeptic identity

Each Skeptic instance has a stable identity such as `SKEP-01`.

New evidence uses that instance's namespace:

```text
E-SKEP-01-001
```

Evidence annotations use:

```text
A-SKEP-01-001
```

## Out-of-scope counterexample license

The Skeptic may inspect repository areas outside the configured analysis scope when necessary to test a claim.

This is a read-only verification/falsification license.

It does not expand the analysis scope.

For each out-of-scope source used:

- label it as `out-of-scope counterexample evidence`,
- explain why it matters to the reviewed item,
- do not imply that the surrounding subsystem was fully analyzed,
- preserve uncertainty about runtime/current-production applicability.

## Skeptic instructions

For each item:

1. inspect its evidence,
2. check lifecycle status of every cited record,
3. read annotations on annotated evidence,
4. search for counterexamples,
5. inspect adjacent modules,
6. look for conflicting tests,
7. inspect relevant history,
8. use the out-of-scope license when needed,
9. propose plausible alternative explanations,
10. verify the claimed scope,
11. challenge any asserted rationale.

When review discovers a new fact:

- create a new evidence record in your own namespace,
- do not rewrite prior evidence,
- annotate or supersede prior evidence according to `methodology/evidence-lifecycle.md`.

## Required review result

Record exactly one primary verdict from taxonomy v2:

- **CONFIRMED**
- **STRENGTHENED**
- **NARROWED**
- **RECLASSIFIED**
- **CONFIDENCE DOWNGRADED**
- **CONTRADICTED**
- **UNRESOLVED CHALLENGE**

Use `methodology/review-model.md` to distinguish nearby outcomes.

For example:

- do not use CONFIRMED when review materially increases consequence or confidence; use STRENGTHENED,
- do not use DOWNGRADED when the claim is still well supported but applies to less territory; use NARROWED,
- use RECLASSIFIED when the evidence remains useful but the architectural interpretation changes.

Explain the evidence behind the verdict.

## Review-discovered architecture items

If adversarial review discovers a new ADR, constraint, anomaly, or open question, create it with explicit provenance:

```yaml
provenance:
  discovered_during: adversarial-review
  discovered_by: SKEP-01
  source_item: ADR-R004 | null
review_status: pending-independent-review
reviewed_by: null
```

The creating Skeptic must not review its own newly discovered item.

The Lead must arrange one of:

1. review by a different Skeptic instance,
2. Lead-mediated independent verification,
3. finalization with `review_status: unverified`.

If independently reviewed, record:

```yaml
review_status: reviewed
reviewed_by: SKEP-02
```

and record the independent review verdict separately.

## G2 — Review Discovery Verification Gate

Every architecture item first discovered during Phase 4 must pass **G2** from `methodology/workflow-gates.md` before it may be treated as reviewed architectural memory.

A different reviewer identity alone is not sufficient.

For `review_status: reviewed`, the independent reviewer must:

1. differ from `discovered_by`,
2. inspect the primary cited evidence directly,
3. inspect lifecycle state and annotations of that evidence,
4. perform at least one fresh confirmation or counterexample search,
5. record exactly one canonical v2 verdict,
6. explain what was independently verified.

For `review_status: lead-verified`, the Lead must perform the same primary-source check rather than merely accepting the discovering Skeptic's notes.

If independent verification cannot be completed:

```yaml
review_status: unverified
reviewed_by: null
```

The item may remain useful, but it must not be presented as settled architectural memory and has no completed review verdict.

G2 fails if:

- the discoverer and reviewer are the same agent,
- the verifier did not inspect primary evidence,
- a reviewed item has no verdict,
- a pending/unverified item is presented as settled.

## Lead instructions

Do not defend the original reconstruction.

Update, strengthen, narrow, downgrade, reclassify, contradict, or preserve architecture items when evidence requires it.

Preserve unresolved disagreement when evidence remains ambiguous.

Ensure review-created evidence follows normal lifecycle rules.

Ensure review-discovered architecture items do not self-confirm.

Ensure out-of-scope evidence remains labeled and does not silently expand scope.

A clean-looking architecture memory is less important than an honest one.

## Exit criterion

No recovered ADR, constraint, or anomaly created before Phase 4 should reach finalization without:

- completed review status,
- exactly one primary v2 review verdict,
- reviewer identity,
- review notes.

Every architecture item discovered during Phase 4 must satisfy G2 and end in exactly one valid state:

- independently reviewed,
- Lead-verified,
- or explicitly UNVERIFIED.

Phase 4 is not complete while any review-discovered item remains `pending-independent-review`.
