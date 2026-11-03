# Workflow

LARA uses a phased workflow to reduce speculation and confirmation bias.

All phases obey the shared identity, lifecycle, provenance, execution, and checkpoint rules defined under `methodology/`.

The configured execution mode is recorded for the entire run:

- `strict` — fresh Phase 2 specialist contexts,
- `economical` — continued Phase 1 specialist contexts behind an explicit phase barrier.

Working state lives under `docs/architecture-working/` and is not final architectural memory.

## Before Phase 1 — Run identity and durable state

The Lead:

- assigns a stable run ID,
- records the target revision,
- selects/records execution mode,
- assigns stable agent instance identities using `id-namespaces.md`,
- initializes `docs/architecture-working/phase-state.yaml`.

Parallel agents create evidence and annotations only inside their assigned namespaces.

## Phase 1 — Discovery

Build a map of the system without reconstructing decisions yet.

Discovery output is provisional and is not itself architectural evidence.

Specialty Discovery notes live under `docs/architecture-working/discovery/` and are quarantined from normal development use.

Before Phase 2, Discovery must be checkpointed and the Lead must issue an explicit **BEGIN EVIDENCE** transition.

## Phase 2 — Evidence collection

Capture concrete architectural evidence as independent records.

Evidence receives:

- deterministic identity,
- lifecycle status,
- creator provenance,
- source traceability.

Do not synthesize ADRs yet.

Phase 2 ends only when **G1 — Evidence Revalidation Gate** passes and the system map is marked `evidence-revalidated`.

## Phase 3 — Reconstruction

The dedicated **Reconstruction Archaeologist** owns synthesis and must be independent from the Skeptic role.

Cluster current and correctly annotated evidence into:

- recovered ADRs,
- constraints,
- anomalies,
- open questions.

Architecture items receive explicit provenance and begin pending adversarial review.

## Phase 4 — Adversarial review

The **Architecture Skeptic** attempts to falsify reconstructed claims by searching for counterexamples, contradictions, alternative explanations, historical layering, and scope errors.

The Skeptic has a read-only out-of-scope counterexample license when evidence outside the configured scope is necessary to test a claim. This does not expand the analyzed scope.

Every completed review uses the canonical v0.2 verdict taxonomy from `review-model.md`.

Review may:

- create new evidence,
- annotate evidence,
- supersede evidence,
- discover new architecture items.

A review-discovered item cannot self-confirm.

Every review-discovered item must satisfy **G2 — Review Discovery Verification Gate** through independent review, Lead verification, or explicit UNVERIFIED status.

For infrastructure-heavy systems, an optional **Operations & Deployment Archaeologist** may own detailed runtime/deployment evidence while the Architecture Cartographer retains the overall structural map.

## Phase 5 — Finalization

Publish a navigable architecture memory with confidence levels, lifecycle-consistent evidence, provenance, cross-links, code references, unresolved questions, a system map, and a machine-readable development navigation manifest.

The manifest is generated from evidence-backed Affected territory metadata and must not introduce new architectural scope.

Finalization completes only when **G3 — Finalization Consistency Gate** passes.

G3 validates identity, lifecycle, system-map state, provenance, review completeness, development navigation, cross-links, scope integrity, and run metadata consistency.

Finalization also produces standardized `run.yaml` and `metrics.yaml` for cross-run comparison.

Non-blocking warnings remain visible in the final architecture memory.

## Incremental use

LARA does not need to analyze an entire system at once.

A scope may target one domain, service, integration, risky feature area, or planned refactor.
