# Phase 05 — Finalize Architectural Memory

## Goal

Publish a coherent, navigable, evidence-backed architecture memory for future development agents.

## Preferred structure

```text
docs/architecture/
├── README.md
├── system-map.md
├── manifest.yaml
├── run.yaml
├── metrics.yaml
├── validation.md
├── evidence/
├── decisions/
├── constraints/
├── anomalies/
└── questions/
```

## Architecture index

The architecture README should summarize:

- analyzed scope,
- repository revision analyzed,
- important exclusions,
- major system boundaries,
- recovered decisions,
- important constraints,
- high-risk anomalies,
- unresolved questions,
- low-confidence areas,
- coverage gaps.

## Cross-linking

Architecture items should link to:

- evidence records,
- related architecture items,
- relevant code locations.

Evidence may support more than one architecture item.

## Development navigation manifest

Before running G3, generate:

`docs/architecture/manifest.yaml`

using:

- `methodology/development-navigation.md`
- `templates/manifest.yaml`

The manifest is a navigation index, not a source of architectural truth.

Build it from the **Affected territory** metadata already present in architecture items.

Do not infer new architecture scope during Finalization merely to improve path coverage.

For every architecture item, include:

- item type,
- title,
- authoritative artifact path,
- confidence,
- review status,
- review verdict when present,
- path territories,
- module territories,
- cross-cutting flag,
- evidence IDs,
- related architecture-item IDs.

Then build:

- `path_index`,
- `module_index`,
- `global_items`.

### Navigation rules

- every architecture item must appear under `items`,
- path mappings must be repository-relative,
- module names must use terminology already present in the evidence-revalidated system map or architecture items,
- `global_items` is only for evidence-backed cross-cutting items,
- do not use broad globs as a substitute for uncertain scope,
- if an item cannot be mapped safely, preserve empty paths and surface a navigation-coverage warning.

Items with `review_status: unverified` or verdict `CONTRADICTED` may remain indexed for provenance and caution, but the manifest must preserve those states exactly. The manifest must never make them appear settled or current by omission of review metadata.

## Run metadata and metrics

Before G3, create:

- `docs/architecture/run.yaml` from `templates/run.yaml`,
- `docs/architecture/metrics.yaml` from `templates/metrics.yaml`.

Follow `methodology/run-metrics.md`.

### run.yaml

Record the actual execution:

- stable run ID,
- target revision,
- scope reference/size,
- strict or economical execution mode,
- agent allocation,
- optional specialists,
- model/runtime identifiers when available,
- phase completion,
- gate outcomes,
- interruptions/resumes,
- wall-clock duration when available.

Use `unknown` rather than guessing unavailable values.

### metrics.yaml

Record:

- artifact counts,
- evidence lifecycle counts,
- v2 review verdict counts,
- review-discovered verification counts,
- correction counts,
- development-navigation coverage,
- qualitative run-level quality assessments,
- runtime cost only when available.

The quality labels are assessments and should be explained in the post-run report rather than presented as objective measurements.

Do not estimate token usage from document size or intuition.

## G3 — Finalization Consistency Gate

Before Finalization may complete, execute **G3** from `methodology/workflow-gates.md`.

Create:

`docs/architecture/validation.md`

using:

`templates/finalization-validation.md`

The report becomes part of the architectural memory audit trail and must be linked from the architecture README.

### Required prerequisite gates

Verify:

- G1 passed and the system map is `evidence-revalidated`,
- every review-discovered item satisfies G2,
- no item remains accidentally pending review.

### Blockers

G3 must fail if any blocker exists.

At minimum check:

#### Identity

- every evidence ID is unique,
- every annotation ID is unique,
- namespaced IDs match creators,
- architecture-item IDs are unique and stable.

#### Evidence lifecycle

- every evidence record has valid lifecycle metadata,
- every annotated record has structured annotations,
- every superseded record points to an existing replacement,
- no final architecture claim relies only on superseded evidence.

#### System map

- G1 passed,
- map status is `evidence-revalidated`,
- reconstruction-relevant map claims are evidence-backed,
- provisional claims are visibly excluded from architectural truth.

#### Provenance and review

- every architecture item has provenance,
- Reconstruction items completed required adversarial review,
- every completed review has reviewer identity,
- every completed adversarial review has exactly one v2 verdict,
- every review-discovered item satisfies G2,
- unverified items remain explicitly unverified,
- RECLASSIFIED items preserve historical identity.

#### Run reproducibility

- `run.yaml` exists,
- `metrics.yaml` exists,
- run IDs match each other,
- target revision matches the system map/manifest/architecture README,
- execution mode matches the configured run mode,
- phase/gate status matches actual run state,
- interruption/resume history is recorded,
- unknown cost/runtime values are represented as `unknown` rather than invented estimates,
- artifact and review counts in metrics match final files.

#### Development navigation

- `manifest.yaml` exists,
- manifest revision matches the architecture-memory revision,
- every architecture item appears exactly once under `items`,
- every manifest artifact path resolves,
- manifest confidence/review metadata matches the authoritative Markdown item,
- every path/module/global index ID resolves,
- every manifest evidence ID resolves,
- every global item is explicitly cross-cutting,
- manifest territories do not broaden evidence-backed item scope,
- unverified and contradicted items retain their cautionary review state.

#### Cross-links

- cited evidence IDs resolve,
- related architecture-item IDs resolve or are explicitly deferred,
- material evidence annotations are reflected in consuming items,
- contradictions remain visible.

#### Scope integrity

- analyzed scope and exclusions are explicit,
- out-of-scope counterexample evidence remains labeled,
- no out-of-scope search is presented as comprehensive analysis,
- coverage gaps are visible.

### Warnings

Warnings do not fail G3, but must be surfaced in both:

- the validation report,
- the final architecture README.

Examples:

- low-confidence but useful item,
- stale deployment/config evidence,
- unresolved challenge,
- production truth requiring external verification,
- important uninspected area,
- reliance on negative-space evidence.

Do not convert a blocker into a warning to finish the run.

### Failure behavior

If G3 fails:

- do not claim Finalization is complete,
- set Finalization state to `failed` in `docs/architecture-working/phase-state.yaml`,
- identify the owning earlier phase,
- correct only the necessary artifacts,
- rerun the affected gate checks,
- preserve valid work already completed.

If G3 passes:

- update `phase-state.yaml` with G3 passed,
- set Finalization and the run to `complete`,
- record the final namespace cursors,
- ensure `run.yaml` records any interruptions and resume count.

## Development-context section

Include guidance that future coding agents should identify, for each change:

- **PRESERVED**
- **AFFECTED**
- **SUPERSEDED**
- **RISKS**

A future agent must not silently violate a recovered decision.

## Final check

Ask:

- Can a future coding agent start from changed paths or modules and find relevant architecture items?
- Does a manifest miss correctly trigger fallback rather than "no architecture"?
- Can a future coding agent identify what it must preserve?
- Can it see where confidence is low?
- Can it trace claims back to current or correctly annotated evidence?
- Can it distinguish decisions from anomalies?
- Can it find unresolved architectural questions?
- Can it identify review-discovered items that remain unverified?
- Can it identify when a proposed change should supersede a recovered decision?

If not, the architecture memory is not finished.
