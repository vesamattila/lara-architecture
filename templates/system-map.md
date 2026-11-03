# System Map

```yaml
map_status: provisional | evidence-revalidated
revalidation:
  gate: G1
  status: pending | passed | failed
  checked_by: null
  excluded_provisional_claims: 0
```

## Evidence convention

This map begins as provisional Discovery output.

Before Reconstruction, it must pass **G1 — Evidence Revalidation Gate**.

Every reconstruction-relevant architectural claim must cite one or more evidence IDs, either inline or in the nearest `Relevant evidence` section.

Use only current or correctly annotated evidence as present support.

Unsupported Discovery observations must be marked:

> **PROVISIONAL — NOT RECONSTRUCTION INPUT**

or moved to Coverage gaps / Open questions.

## Scope

Describe the part of the system represented by this map.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Runtime topology

Describe:

- runtime processes,
- deployment units,
- background workers,
- queues,
- scheduled jobs,
- external services.

Use a diagram when useful, but keep the textual description authoritative and reviewable.

Distinguish repository-configured topology from known current runtime topology.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Major modules and boundaries

For each major area:

### <module / subsystem>

Responsibilities:

Dependencies:

Inbound interfaces:

Outbound interfaces:

Persistence:

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

Known counterexamples / exceptions:

## Domain boundaries

Describe the major domain areas and known cross-domain dependencies.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Persistence and consistency boundaries

Describe databases, storage systems, transactions, caches, and important consistency relationships.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Integration boundaries

Describe external APIs, messaging, identity systems, file storage, or other external dependencies.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Test topology

Describe where unit, integration, contract, and end-to-end tests provide architectural evidence.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Historical layers

List visible framework generations, parallel implementations, migrations, or compatibility layers without assuming why they exist.

Relevant evidence:

- E-<ROLE>-<INSTANCE>-<NNN>

## Known architectural tensions

Link to relevant anomaly IDs where available.

Before Reconstruction, Discovery-only tensions must either gain evidence or remain provisional.

## Coverage gaps

List important areas that were not inspected or remain poorly understood.

List any provisional claims deliberately excluded from Reconstruction input.

## Known contradictions

Record source disagreements or counterexamples that materially qualify the map.

Do not normalize them away.

## Notes on certainty

Clearly distinguish direct structural observations from inferred architectural boundaries.

## G1 revalidation record

Checked by:

Status: PASSED | FAILED

Corrections made since Discovery:

Provisional claims excluded from Reconstruction:

Warnings carried forward:
