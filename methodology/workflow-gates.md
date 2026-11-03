# Workflow gates

LARA phases are separated by explicit gates.

A gate is not a summary or recommendation. It is a **pass/fail condition** that controls whether the next phase may begin or whether architectural memory may be finalized.

v0.2 defines three canonical gates:

- **G1 — Evidence Revalidation Gate** between Phase 2 and Phase 3,
- **G2 — Review Discovery Verification Gate** inside Phase 4,
- **G3 — Finalization Consistency Gate** before Phase 5 completes.

## Gate result model

Every gate records:

```yaml
gate: G1
status: passed | failed
checked_by: LEAD-01
blockers: []
warnings: []
```

A gate with one or more blockers is `failed`.

Warnings do not block progress, but must remain visible to later phases.

The Lead owns gate completion unless a phase-specific instruction assigns a verifier.

---

# G1 — Evidence Revalidation Gate

## Purpose

Prevent provisional Discovery claims from silently becoming Reconstruction input.

Discovery maps are provisional and may misstate scope or topology until checked against evidence.

Phase 3 must therefore consume an **evidence-revalidated system map**, not raw Discovery prose.

## Required checks

Before Phase 3 begins:

1. every reconstruction-relevant claim in `system-map.md` must cite one or more current or correctly annotated evidence IDs,
2. every annotated evidence record used by the map must have its qualification reflected in the map,
3. superseded evidence must not support a current system-map claim,
4. known counterexamples must be represented,
5. Discovery claims corrected by Phase 2 must be updated,
6. unsupported claims must be:
   - removed,
   - moved to Coverage gaps / Open questions,
   - or explicitly marked `PROVISIONAL — NOT RECONSTRUCTION INPUT`,
7. scope and exclusions must still match the configured run scope,
8. describe-only and out-of-scope observations must remain labeled as such.

## System-map state

Before revalidation:

```yaml
map_status: provisional
```

After a successful gate:

```yaml
map_status: evidence-revalidated
revalidation:
  gate: G1
  status: passed
  checked_by: LEAD-01
  excluded_provisional_claims: <N>
```

If unresolved provisional claims remain, they must be counted as `excluded_provisional_claims` and explicitly excluded from Reconstruction input.

A map may still pass with known uncertainty when the uncertain content is clearly labeled and excluded from factual architectural claims.

## G1 blockers

Examples:

- a topology claim used for Reconstruction has no evidence,
- a map claim still relies on superseded evidence,
- a known contradiction is hidden,
- a Discovery correction was not propagated,
- scope labels are inconsistent with the configured scope.

## G1 warnings

Examples:

- a map section is evidence-backed but low confidence,
- runtime/deployment evidence may be stale,
- an important area has sparse evidence but is clearly labeled.

---

# G2 — Review Discovery Verification Gate

## Purpose

Prevent an Architecture Skeptic from creating and effectively approving a new architecture item in the same reasoning context.

Every architecture item first discovered during adversarial review must receive independent treatment.

## Applies to

Any ADR, constraint, anomaly, or open question with:

```yaml
provenance:
  discovered_during: adversarial-review
```

## Valid completion paths

A review-discovered item must end Phase 4 in exactly one of these states:

### Independently reviewed

```yaml
review_status: reviewed
reviewed_by: SKEP-02
```

Requirements:

- reviewer differs from `discovered_by`,
- reviewer independently inspects the cited evidence,
- reviewer performs at least one fresh counterexample or confirmation search,
- reviewer records one canonical v2 verdict.

### Lead-verified

```yaml
review_status: lead-verified
reviewed_by: LEAD-01
```

Requirements:

- Lead independently checks primary sources,
- Lead does not merely approve the creating Skeptic's prose,
- Lead records what was independently verified,
- a canonical verdict is recorded when applicable.

### Unverified

```yaml
review_status: unverified
reviewed_by: null
```

Requirements:

- the item remains visible because it may matter,
- it is clearly excluded from settled architectural memory,
- no completed verdict is recorded,
- README/index surfaces its unverified state.

## G2 blockers

Examples:

- `discovered_by == reviewed_by`,
- item is marked reviewed with no verifier,
- reviewed item has no verdict,
- verifier did not inspect primary evidence,
- item is presented as settled while status is pending or unverified.

## G2 warnings

Examples:

- Lead verification was used because only one Skeptic instance was available,
- verification evidence is strong but current-production applicability remains uncertain.

---

# G3 — Finalization Consistency Gate

## Purpose

Ensure the final architecture memory is internally coherent, traceable, and honest about uncertainty.

Phase 5 may not complete until G3 passes.

## Blocker checks

### Identity

- every evidence ID is unique,
- every annotation ID is unique,
- namespaced IDs match their creator,
- architecture-item IDs are unique and stable.

### Evidence lifecycle

- every evidence record has valid lifecycle metadata,
- every annotated record contains at least one structured annotation,
- every superseded record has a valid replacement,
- replacement targets exist,
- final claims do not rely only on superseded evidence.

### System map

- G1 passed,
- `map_status: evidence-revalidated`,
- reconstruction-relevant map claims are evidence-backed,
- provisional claims are visibly excluded from Reconstruction truth.

### Architecture provenance

- every architecture item records provenance,
- normal Reconstruction items completed required adversarial review,
- review-discovered items satisfy G2,
- unverified items remain explicitly unverified.

### Review model

- every completed review has reviewer identity,
- every completed adversarial review has exactly one canonical v2 verdict,
- review status and verdict are not conflated,
- RECLASSIFIED items preserve historical identity.

### Run reproducibility

- `run.yaml` exists,
- `metrics.yaml` exists,
- both use the same stable run ID,
- target revision matches the final architecture memory and manifest,
- execution mode matches the configured run mode,
- phase and gate outcomes match the actual completed workflow,
- interruptions/resumes are recorded,
- metrics artifact/review counts match final artifacts,
- unavailable token/runtime information is `unknown`, not fabricated.

A mismatched run ID or revision is a blocker.

A missing cost figure is not a blocker when the runtime did not provide one.

### Development navigation

- `manifest.yaml` exists,
- manifest revision matches the architecture-memory revision,
- every architecture item appears exactly once in the manifest item registry,
- every manifest artifact path resolves,
- item confidence, review status, and verdict match the authoritative Markdown artifact,
- every `path_index`, `module_index`, and `global_items` reference resolves,
- every manifest evidence reference resolves,
- every global item is evidence-backed as cross-cutting,
- manifest path/module territory does not broaden the item's evidence-backed scope,
- unverified and contradicted items preserve their review state.

Missing path coverage for an honestly unmappable item is a warning, not permission to invent a broad mapping.

A manifest/index reference to a nonexistent item or an incorrectly broadened territory is a blocker.

### Cross-links

- cited evidence IDs exist,
- related architecture-item IDs exist or are explicitly marked external/deferred,
- material evidence annotations are reflected in consuming architecture items,
- contradictions are not silently normalized away.

### Scope integrity

- final README states analyzed scope and exclusions,
- out-of-scope counterexample evidence is labeled,
- no out-of-scope search is presented as comprehensive analysis,
- coverage gaps remain visible.

## Warnings

Warnings do not fail G3 but must be published in the final architecture README.

Examples:

- low-confidence but useful item,
- stale deployment/configuration evidence,
- unresolved challenge,
- production truth requiring external verification,
- important uninspected area,
- high reliance on negative-space evidence.

## Gate report

Phase 5 produces a gate report using `templates/finalization-validation.md`.

Minimum output:

```yaml
gate: G3
status: passed
checked_by: LEAD-01
blockers: []
warnings:
  - "Production runtime topology is inferred from possibly stale deployment configuration."
```

The report is part of the architectural memory audit trail.

## Failure behavior

If G3 fails:

- do not claim Finalization is complete,
- do not hide blockers by converting them into warnings,
- return the affected item to the appropriate earlier phase,
- preserve already valid artifacts,
- rerun only the necessary gate checks after correction.

The objective is not a green gate.

The objective is architecture memory that deserves a green gate.
