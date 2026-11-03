# Adversarial review model

LARA separates **review status** from **review verdict**.

These answer different questions:

- review status: **has the required independent review happened?**
- review verdict: **what did the review conclude about the architecture claim?**

Do not use one as a substitute for the other.

## Review status

Review status is defined by `methodology/artifact-provenance.md`.

Typical values:

- `pending-adversarial-review`
- `pending-independent-review`
- `reviewed`
- `lead-verified`
- `unverified`

A status of `reviewed` does not mean the claim was confirmed. It means the required review occurred.

## Review verdict taxonomy v2

Every completed adversarial review records exactly one primary verdict.

### CONFIRMED

The claim stands materially unchanged.

Use when:

- scope remains substantially the same,
- interpretation remains substantially the same,
- confidence remains substantially the same,
- review adds no material consequence that changes how a future agent should reason about the item.

Additional citations alone do not require STRENGTHENED.

### STRENGTHENED

The core claim remains valid and review materially increases one or more of:

- evidentiary support,
- confidence,
- known scope,
- known consequence,
- change risk.

Use this instead of CONFIRMED when the reviewed item becomes meaningfully stronger or more consequential.

### NARROWED

The core claim remains valid, but review reduces:

- scope,
- affected territory,
- consequence,
- blast radius,
- applicability.

Use when the item still represents the same architectural concept after narrowing.

### RECLASSIFIED

The underlying evidence remains useful, but the architectural interpretation or artifact type changes materially.

Examples:

- anomaly → constraint,
- recovered decision → historical compatibility layer,
- "live routing rule" → backfill/replay mechanism.

Preserve the original item ID and record the reclassification explicitly.

### CONFIDENCE DOWNGRADED

The claim remains in architectural memory, but review reduces confidence because:

- counterevidence exists,
- evidence is weaker than reconstructed,
- competing explanations become equally plausible,
- current-production applicability is uncertain.

Use this when scope and artifact type remain substantially intact but certainty falls.

### CONTRADICTED

Review evidence invalidates the architecture claim as stated.

The item should not remain presented as current architectural truth.

Preserve it for provenance according to the artifact lifecycle/provenance rules.

### UNRESOLVED CHALLENGE

Review raises a material challenge that cannot be resolved from available evidence.

The item may remain useful, but its unresolved challenge must be visible to future consumers.

Do not force CONFIRMED or CONTRADICTED when evidence cannot decide.

## Choosing between nearby verdicts

### STRENGTHENED vs CONFIRMED

Ask:

> Would a future coding agent reason differently because of what review added?

If yes, prefer STRENGTHENED.

### NARROWED vs CONFIDENCE DOWNGRADED

Use NARROWED when the claim is still well supported but applies to less territory or fewer cases.

Use CONFIDENCE DOWNGRADED when applicability may be unchanged but certainty in the claim is lower.

Both may be true, but record one primary verdict and describe the secondary effect in review notes.

### RECLASSIFIED vs CONTRADICTED

Use RECLASSIFIED when the evidence remains architecturally meaningful but the original interpretation was wrong.

Use CONTRADICTED when the claim itself no longer has a defensible current interpretation.

## Review record

Each architecture item should record:

```yaml
review:
  status: reviewed
  verdict: STRENGTHENED
  reviewed_by: SKEP-02
```

The Markdown review section should explain:

- challenge attempted,
- counterevidence searched,
- new evidence created,
- lifecycle changes to cited evidence,
- verdict rationale,
- resulting changes to the item.

## Review-discovered items

Review-discovered items are governed by **G2 — Review Discovery Verification Gate**.

An item discovered by a Skeptic starts:

```yaml
review_status: pending-independent-review
reviewed_by: null
```

The discovering agent cannot provide the independent review verdict for that item.

A different Skeptic or the Lead must review it.

Independent review requires:

- direct inspection of primary cited evidence,
- lifecycle/annotation checks,
- at least one fresh confirmation or counterexample search,
- an explicit statement of what was independently verified.

A second agent merely reading the creator's conclusion does not satisfy G2.

If independent review cannot happen, preserve the item as:

```yaml
review_status: unverified
reviewed_by: null
```

An UNVERIFIED item has no completed review verdict.

## Metrics

Post-run metrics must count the v2 verdicts separately:

- confirmed,
- strengthened,
- narrowed,
- reclassified,
- confidence_downgraded,
- contradicted,
- unresolved_challenge.

This taxonomy is canonical for all future metrics and run comparisons.
