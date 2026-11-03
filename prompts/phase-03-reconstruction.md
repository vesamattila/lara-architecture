# Phase 03 — Reconstruction

## Goal

Cluster evidence into useful architectural memory.

## Owner

Phase 3 is owned by the **Reconstruction Archaeologist**, normally `RECON-01`.

The Reconstruction Archaeologist must not serve as an Architecture Skeptic for the same run.

Read `agents/reconstruction-archaeologist.md` before starting.

## G1 prerequisite

Do not begin Reconstruction unless **G1 — Evidence Revalidation Gate** has passed.

Verify that:

- `system-map.md` has `map_status: evidence-revalidated`,
- its revalidation status is `passed`,
- provisional claims are explicitly excluded from Reconstruction truth.

If G1 is failed or missing, stop Phase 3 and return the map to Phase 2 revalidation.

## Evidence input gate

Reconstruction consumes **evidence records**, not unverified discovery prose.

Before synthesis:

1. inspect the lifecycle state of every candidate evidence record,
2. read all annotations on `annotated` evidence,
3. exclude `superseded` evidence from current support,
4. retain superseded records only as historical traceability,
5. inspect explicit evidence conflicts and gaps,
6. flag missing or inconsistent lifecycle metadata before continuing.

## Artifact provenance

Every architecture item created in this phase must begin with provenance defined in `methodology/artifact-provenance.md`:

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: RECON-01
  source_item: null
review_status: pending-adversarial-review
reviewed_by: null
```

## Artifact types

### Recovered ADR

Use when evidence supports a durable architectural decision or policy that future changes may need to preserve or explicitly supersede.

### Constraint

Use when the system imposes a limitation, invariant, compatibility requirement, or consistency boundary that materially affects design choices.

### Anomaly

Use when evidence reveals architectural tension, inconsistency, duplication, unfinished migration, or risky divergence.

An anomaly is not automatically a defect.

### Open question

Use when an important architectural issue cannot be resolved reliably from available evidence.

Open questions are first-class output.

## Rules

Every reconstructed item must reference namespaced evidence IDs.

Do not cite superseded evidence as current support.

When using annotated evidence, incorporate the annotation into the interpretation.

Do not invent original rationale.

A recovered decision may be high confidence while its original rationale remains UNKNOWN.

Preserve competing interpretations when evidence supports more than one explanation.

Avoid creating ADRs for trivial implementation details.

Prefer fewer useful architecture items over exhaustive noise.

Do not use raw discovery prose to fill evidence gaps.

## Late evidence

If reconstruction uncovers a genuinely new verifiable fact:

- create it in the `RECON-<INSTANCE>` evidence namespace,
- set `created_phase: reconstruction`,
- explain why it was discovered late,
- do not manufacture evidence merely to rescue a candidate architecture item.

## Rejected candidates

Maintain a short working note of candidate items deliberately not promoted.

Record a reason such as:

- insufficient evidence,
- implementation trivia,
- duplicate,
- scope too narrow,
- no meaningful change implication,
- unresolved classification.

These notes are not final architectural memory.

## Development navigation metadata

For every architecture item, populate its **Affected territory** section while the evidence and scope reasoning are still in context.

Record:

- repository-relative paths or glob-like territories when justified,
- stable module/subsystem names from the evidence-revalidated system map,
- whether the item is genuinely cross-cutting.

Do not invent broad path mappings for convenience.

If scope cannot be mapped safely:

- leave paths empty,
- use a supported module mapping when possible,
- set cross-cutting only when evidence establishes broad applicability,
- otherwise preserve the navigation gap for Finalization warning.

This metadata is later used to build `manifest.yaml`; Finalization must not infer new architectural scope.

## Reconstruction checks

For every candidate item ask:

- Would a future coding agent need to know this before changing the area?
- Does the current evidence establish the claimed scope?
- Is any supporting evidence annotated, and has that qualification been carried forward?
- Is this a decision, constraint, anomaly, or unanswered question?
- What would be lost if this item were omitted?
- Is any historical rationale explicitly evidenced, or merely plausible?
- What evidence would falsify this item?
