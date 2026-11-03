# Phase 02 — Evidence Collection

## Goal

Turn discovery findings into concrete, traceable evidence records.

## Phase entry

Do not begin until Discovery is checkpointed and the Lead has explicitly issued **BEGIN EVIDENCE**.

Read `methodology/execution-modes.md`.

### strict mode

Phase 2 uses fresh specialist contexts.

Discovery notes are orientation only. Inspect primary sources before creating evidence.

### economical mode

The same specialist contexts may continue from Discovery.

Retained context is not evidence.

Before writing the first evidence record, each continuing specialist must explicitly switch to evidence-verification rules and re-check the observation against primary repository sources.

## Instructions

Each specialist agent should create evidence records using `templates/evidence.md`.

Before writing evidence, verify your assigned agent identity and namespace.

Evidence IDs must follow:

```text
E-<ROLE>-<INSTANCE>-<NNN>
```

Only create IDs in your own namespace.

Evidence should point to concrete sources such as:

- files and line ranges where practical,
- tests,
- migrations,
- configuration,
- API schemas,
- commit identifiers,
- issue or PR references,
- existing documentation.

## Lifecycle initialization

Every new Phase 2 record starts with:

```yaml
status: current
created_by: <your agent identity>
created_phase: evidence
superseded_by: null
```

Evidence becomes append-only once created.

Do not rewrite an existing record to make later findings fit.

Follow `methodology/evidence-lifecycle.md` for corrections.

## Rules

One evidence record should express one primary observation.

Separate direct observation from interpretation.

Architectural significance may be inferred, but must be labeled accordingly.

Record contradictory evidence rather than normalizing it away.

Do not yet create recovered ADRs, constraints, anomalies, or open questions.

## Evidence quality checks

Ask for each record:

- Is the observation directly supported?
- Is the source precise enough for another agent to verify?
- Is the claimed significance broader than the evidence?
- Are there known counterexamples?
- Is confidence appropriate?
- Is the lifecycle metadata complete?
- Does the ID belong to my assigned namespace?

## Corrections during Phase 2

If another evidence record is incomplete or wrong:

- do not edit its original observation,
- create new evidence for newly observed facts,
- add a structured annotation if authorized by the Lead,
- supersede only when the original record would mislead as current evidence.

## System-map revalidation

Before Phase 2 may complete, run **G1 — Evidence Revalidation Gate** from `methodology/workflow-gates.md`.

The provisional `system-map.md` from Discovery must be revalidated against the Phase 2 evidence base.

For every reconstruction-relevant map claim:

- cite current or correctly annotated evidence IDs,
- propagate material evidence annotations,
- remove reliance on superseded evidence,
- preserve known counterexamples,
- correct Discovery overclaims,
- label unsupported claims as `PROVISIONAL — NOT RECONSTRUCTION INPUT` or move them to coverage gaps / open questions.

After a successful gate, update the map metadata to:

```yaml
map_status: evidence-revalidated
revalidation:
  gate: G1
  status: passed
  checked_by: LEAD-01
  excluded_provisional_claims: <N>
```

A map may contain known uncertainty and still pass only when that uncertainty is explicit and is not consumed as established architectural truth.

## Checkpoint

During Phase 2, update `docs/architecture-working/phase-state.yaml` after material evidence batches.

Record:

- completed/pending territory,
- each agent's next evidence and annotation numbers,
- last completed artifact,
- interruptions and partial artifacts.

On interruption, follow `methodology/checkpoint-resume.md`.

## Exit criterion

Before reconstruction begins:

- important claims have evidence,
- duplicate records are linked rather than silently merged,
- contradictory evidence remains visible,
- annotations and supersessions are internally consistent,
- no two artifacts share an ID,
- major evidence gaps are listed,
- the configured scope has adequate coverage,
- **G1 has passed**,
- `system-map.md` is marked `evidence-revalidated`,
- unresolved provisional map claims are explicitly excluded from Reconstruction input.

If G1 fails, Phase 3 must not begin.
