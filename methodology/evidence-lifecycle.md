# Evidence lifecycle

LARA preserves the history of evidence while allowing its interpretation to evolve.

The **original evidence body is immutable after creation**. Lifecycle metadata may transition only through the rules below, and later corrections are appended as structured annotations or replacement evidence.

The purpose of the lifecycle protocol is to allow later phases to correct, narrow, contradict, or supersede earlier evidence without destroying the reasoning history that produced it.

## Lifecycle states

Every evidence record has exactly one status:

### `current`

The record remains valid as written and may be used directly during reconstruction.

### `annotated`

The original record remains part of the evidence history, but later information changes how it must be interpreted.

A coding or reconstruction agent must read the annotations before relying on the record.

Typical reasons:

- clarification,
- scope narrowing,
- partial correction,
- newly discovered counterevidence,
- a changed confidence assessment.

### `superseded`

The record must not be used as current architectural evidence.

It remains in the repository only for traceability.

A superseded record must identify the evidence record that replaces or invalidates it.

`superseded` is terminal.

## Allowed state transitions

Only these transitions are allowed:

```text
current ───────────────→ annotated
   │                       │
   └───────────────────────┴────→ superseded
```

Rules:

- `current → annotated` when the record remains usable with qualification,
- `current → superseded` when replacement evidence makes the original misleading,
- `annotated → superseded` when later evidence makes the qualified record unusable,
- additional annotations may be appended while status remains `annotated`,
- `superseded` never returns to `current` or `annotated`.

Do not use lifecycle transitions to hide reasoning mistakes. The historical record remains visible.

## Required metadata

Each evidence record begins with structured metadata:

```yaml
id: E-ARCH-01-001
status: current
created_by: ARCH-01
created_phase: evidence
superseded_by: null
```

Allowed `created_phase` values:

- discovery
- evidence
- reconstruction
- review

Normal Phase 2 evidence uses `evidence`.

Later phases may create evidence when new verifiable facts are discovered, but provenance must make this explicit.

## Immutable and mutable parts

### Immutable after creation

Do not rewrite:

- the original Observation,
- original cited Sources,
- original Architectural significance,
- original Confidence,
- original Counterevidence,
- original Caveats.

These fields describe what the creating agent concluded at that moment.

### Lifecycle-controlled metadata

The following may change only through this protocol:

- `status`,
- `superseded_by`.

### Append-only additions

The following may be appended:

- structured annotations,
- related evidence references created later,
- lifecycle history notes.

Formatting-only fixes that do not alter meaning are allowed, but should be rare.

## Annotations

Annotations are structured append-only additions.

Example:

```yaml
annotations:
  - id: A-SKEP-01-001
    reason: scope-narrowing
    created_by: SKEP-01
    created_phase: review
    related_evidence:
      - E-SKEP-01-004
```

Allowed reasons:

- `correction`
- `clarification`
- `scope-narrowing`
- `contradiction`
- `confidence-change`

The annotation body explains:

- what changed,
- why,
- which new evidence supports the change,
- whether the original record remains usable.

An annotation does not replace a missing evidence record.

If a correction depends on a newly observed fact, create new evidence for that fact and reference it from the annotation.

## When to annotate

Use `annotated` when the core observation is still useful but requires qualification.

Examples:

- "only caller" becomes "one of two callers",
- a system-wide pattern is narrowed to one subsystem,
- the original confidence is no longer appropriate,
- later evidence reveals an important exception.

The original Confidence field remains unchanged as historical provenance. The annotation states the updated confidence interpretation.

## When to supersede

Use `superseded` when the original observation would mislead a future agent if consumed as current evidence.

Examples:

- the cited behavior does not exist,
- the wrong file or mechanism was identified,
- the original claim is materially contradicted,
- a replacement evidence record states the corrected observation.

A superseded record must set:

```yaml
status: superseded
superseded_by: E-SKEP-02-007
```

The replacing record should link back using `Related evidence`.

## Consumer rules

### Reconstruction

The Reconstruction phase must:

- prefer `current` evidence,
- read all annotations on `annotated` evidence,
- never rely on `superseded` evidence as support for a current architecture claim,
- preserve superseded evidence only as historical traceability.

### Adversarial review

The Skeptic may:

- create new evidence,
- append annotations to existing evidence,
- transition evidence to `annotated` or `superseded` when independently verified counterevidence warrants it.

The Skeptic must not rewrite the immutable body of the original record.

### Finalization

Finalization must fail its consistency gate if:

- a final architecture item relies only on superseded evidence,
- a superseded record has no `superseded_by`,
- a `superseded_by` target does not exist,
- an annotation references missing evidence,
- an annotated record has no structured annotation,
- architecture memory ignores an annotation that materially changes a cited record.

## Provenance principle

Evidence provenance describes how LARA learned something.

It does not imply that evidence created later is automatically stronger.

A Phase 2 test assertion can be stronger evidence than a Phase 4 inference. Evidence strength continues to depend on source quality and verification, not chronology.

## Why records are retained

Superseded evidence is intentionally retained because the evolution of LARA's understanding is itself useful:

- it makes corrections auditable,
- exposes recurring reasoning failures,
- allows run-to-run methodology analysis,
- prevents silent historical rewriting by agents.
