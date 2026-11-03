# Development navigation

LARA architectural memory must be usable from a development task without requiring a coding agent to read the entire documentation tree first.

v0.2 adds a machine-readable navigation layer:

```text
docs/architecture/manifest.yaml
```

The manifest is an **index**, not a second source of architectural truth.

The Markdown architecture items remain authoritative.

## Design goals

A coding agent starting with changed or planned files should be able to answer:

- Which recovered decisions may apply?
- Which constraints may apply?
- Which anomalies make this area risky?
- Which open questions create uncertainty?
- Which cross-cutting items should always be considered?

The manifest must optimize discovery of relevant memory without pretending that path matching proves architectural applicability.

## Canonical sources

Authority order:

1. architecture item Markdown,
2. cited evidence,
3. evidence annotations and lifecycle state,
4. `manifest.yaml` as navigation metadata.

If manifest metadata conflicts with an architecture item, the architecture item and evidence win.

The conflict should be treated as stale navigation metadata and corrected.

## Manifest identity

A manifest records:

```yaml
schema_version: "0.2"
generated_from_revision: <target git revision>
architecture_root: docs/architecture
```

The revision must match the revision described by the final architectural memory.

## Item model

Every finalized architecture item receives one manifest entry.

Minimum fields:

```yaml
items:
  ADR-R001:
    type: decision
    title: "<short title>"
    artifact: decisions/ADR-R001.md
    confidence: high
    review_status: reviewed
    verdict: CONFIRMED
    territories:
      paths:
        - src/example/**
      modules:
        - example-module
      cross_cutting: false
    evidence:
      - E-ARCH-01-001
    related:
      - CON-002
      - ANO-004
```

### type

Allowed values:

- `decision`
- `constraint`
- `anomaly`
- `question`

### artifact

Relative path from `docs/architecture/` to the authoritative Markdown item.

### confidence

Use the item's current confidence when that artifact type carries confidence.

For an open question without a normal confidence field, use:

```yaml
confidence: unknown
```

### review_status and verdict

Mirror the authoritative item.

For `review_status: unverified`:

```yaml
verdict: null
```

### territories

Territories are navigation hints supported by the architecture item's scope.

They do not independently establish scope.

#### paths

May contain:

- exact repository-relative files,
- repository-relative directories,
- glob-like patterns.

Examples:

```yaml
paths:
  - src/core/service.py
  - src/core/**
  - migrations/**
```

Prefer the narrowest useful stable territory.

Do not add broad paths merely because evidence was found there.

#### modules

Use stable logical subsystem or module identifiers when path structure is insufficient or unstable.

Example:

```yaml
modules:
  - signing-workflow
  - background-processing
```

Module names should come from the system map or architecture memory, not be invented only for the manifest.

#### cross_cutting

Set `true` when an item can affect changes across many unrelated paths and cannot be safely discovered through path matching alone.

Examples may include:

- system-wide identity semantics,
- global wire compatibility,
- universal transaction policy,
- deployment-wide concurrency assumptions.

Cross-cutting status must be justified by the item's evidence-backed scope.

## Path index

The manifest contains a reverse index:

```yaml
path_index:
  - pattern: src/core/**
    items:
      - ADR-R001
      - CON-002
```

Use a list rather than YAML keys so metadata can later be extended without changing the shape.

Each entry may optionally include:

```yaml
  - pattern: src/core/**
    modules:
      - core-workflow
    items:
      - ADR-R001
      - CON-002
```

Every ID in the path index must exist in `items`.

## Module index

The manifest also contains:

```yaml
module_index:
  core-workflow:
    - ADR-R001
    - CON-002
    - ANO-004
```

Every module should correspond to terminology present in the evidence-revalidated system map or architecture items.

## Global items

Cross-cutting architecture must not disappear because no path pattern matched.

The manifest includes:

```yaml
global_items:
  - CON-010
  - ADR-R012
```

Every ID in `global_items` must have:

```yaml
territories:
  cross_cutting: true
```

Do not abuse `global_items` as a place for uncertain scope.

Uncertain scope belongs in the architecture item and should remain explicit.

## Navigation algorithm for coding agents

Given planned or changed files:

1. read `manifest.yaml`,
2. collect all matching `path_index` entries,
3. map known modules when applicable and collect `module_index` entries,
4. add every `global_items` entry,
5. de-duplicate IDs,
6. read the authoritative Markdown artifact for every selected ID,
7. follow related items when they materially affect the planned change,
8. inspect cited evidence when:
   - confidence is low,
   - review verdict is UNRESOLVED CHALLENGE,
   - the item is unverified,
   - the proposed change may supersede the item,
   - manifest applicability is ambiguous.

## No-match behavior

A path-index miss does **not** mean "no architecture applies."

If changed files have no match:

1. inspect the nearest module/system-map boundary,
2. search architecture item territories,
3. include global items,
4. state that manifest coverage is incomplete,
5. do not silently conclude that the change is architecture-neutral.

## Planned changes without files

When implementation files are not yet known:

- start from module names,
- system-map boundaries,
- planned behavior,
- related APIs/data/integrations.

Use `module_index` first and refine with paths later.

## Manifest generation

Phase 5 generates the manifest from finalized architecture items.

Do not infer new architectural scope while generating the manifest.

If an item lacks enough territory information to index safely:

- leave `paths: []`,
- use supported module mappings if available,
- mark `cross_cutting: true` only when justified,
- otherwise add a Finalization warning for incomplete navigation coverage.

## Consistency requirements

G3 must verify:

- every finalized architecture item appears exactly once under `items`,
- every manifest artifact path exists,
- every path/module/global index reference resolves to a manifest item,
- every manifest evidence reference exists,
- manifest review metadata matches the authoritative artifact,
- unverified items remain unverified,
- global items are actually marked cross-cutting,
- path/module territories do not silently broaden the item's evidence-backed scope,
- generated revision matches architectural memory revision.

## Principle

> **The manifest should reduce search cost, not reduce epistemic caution.**
