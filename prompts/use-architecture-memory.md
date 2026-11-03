# Use Architectural Memory During Development

Use this prompt when planning or implementing a change in a repository that already contains LARA architectural memory.

---

## Goal

Use LARA memory to reduce unsafe assumptions before changing legacy code.

Start from the change territory rather than reading the entire architecture tree blindly.

The navigation layer is:

`docs/architecture/manifest.yaml`

The manifest is an index only.

The authoritative architectural meaning remains in the referenced Markdown items and their evidence.

## Step 1 — Identify change territory

Before implementation, identify one or both of:

- planned or changed repository-relative file paths,
- affected modules/subsystems when file paths are not yet known.

Examples:

```text
src/core/service.py
src/workers/**
```

or:

```text
core-workflow
background-processing
```

## Step 2 — Resolve relevant architecture items

Read `docs/architecture/manifest.yaml`.

Collect architecture IDs from:

1. matching `path_index` entries,
2. matching `module_index` entries,
3. all `global_items`.

De-duplicate the IDs.

Then read the authoritative Markdown artifact for every selected item.

Do not reason from manifest titles alone.

## Step 3 — Handle index misses safely

A manifest miss does **not** mean no architecture applies.

If a changed/planned path matches no index entry:

1. inspect the nearest relevant boundary in `system-map.md`,
2. inspect module mappings,
3. search architecture item Affected territory sections,
4. include all global items,
5. record a navigation coverage gap if applicability remains uncertain.

Never conclude "architecture-neutral change" solely from an index miss.

## Step 4 — Interpret review state

Treat review metadata explicitly.

### reviewed / lead-verified

Use the item according to its current content, confidence, and verdict.

### unverified

Treat as a risk signal, not settled architecture.

Verify important claims from evidence/code before relying on them.

### CONTRADICTED

Do not use the contradicted claim as current architectural truth.

It may remain useful as historical/provenance context.

### UNRESOLVED CHALLENGE

Treat the unresolved challenge as part of the change risk.

### RECLASSIFIED

Use the current authoritative interpretation while preserving awareness of the historical identity.

## Step 5 — Trace evidence when needed

Trace architecture claims back to evidence when:

- confidence is Low,
- review status is unverified,
- verdict is UNRESOLVED CHALLENGE,
- the proposed change may supersede the item,
- current code appears to contradict the memory,
- manifest applicability is ambiguous,
- the item is operationally or security critical.

Do not assume an architecture item is correct merely because it is indexed.

## Step 6 — Expand related items deliberately

Follow `related` architecture-item links when they materially affect the planned change.

Do not recursively read every related item without a reason.

Prefer a bounded context set:

- directly matched items,
- global items,
- materially relevant related items.

## Architecture impact report

Before implementation, produce an architecture impact section with exactly these categories:

## PRESERVED

Existing architectural decisions and constraints that the proposed approach preserves.

For each important item, cite its LARA ID.

## AFFECTED

Existing architecture items whose scope or consequences are touched by the change.

Include decisions, constraints, anomalies, and open questions where relevant.

## SUPERSEDED

Recovered decisions the change intentionally replaces.

If none, state `None`.

Do not silently violate or replace a recovered decision.

When a recovered decision must change:

- explain why,
- identify the existing item,
- propose a new ADR that explicitly supersedes it.

## RISKS

Relevant:

- anomalies,
- unresolved questions,
- low-confidence assumptions,
- unverified items,
- unresolved review challenges,
- evidence gaps,
- manifest/navigation coverage gaps.

## Implementation rules

- Treat LARA output as evidence-backed context, not unquestionable truth.
- Respect confidence levels and review state.
- Re-check code when an architecture item is stale, ambiguous, or critical.
- Do not convert an anomaly into a defect without evidence.
- Do not invent rationale for existing decisions.
- If implementation evidence contradicts the architecture memory, stop relying on the stale claim and surface the contradiction.
- Do not edit architecture memory merely to make the proposed implementation look compliant.

## After implementation

State whether the change:

- preserved documented architecture,
- affected existing architectural assumptions,
- superseded an existing decision,
- introduced a new architectural decision,
- revealed new evidence,
- revealed a new anomaly,
- revealed a new constraint,
- resolved or created an open question,
- exposed stale or incomplete manifest navigation.

When architectural memory materially changes, update it explicitly rather than letting it drift from the system.

## Minimal workflow

```text
changed paths / modules
        ↓
manifest.yaml
        ↓
matched items + global items
        ↓
authoritative Markdown artifacts
        ↓
evidence where needed
        ↓
PRESERVED / AFFECTED / SUPERSEDED / RISKS
        ↓
implementation
        ↓
architecture-memory update when warranted
```
