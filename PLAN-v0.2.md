# LARA v0.2 Implementation Plan

**Legacy Architecture Reconstruction & Archaeology**

This plan focuses on making LARA more reproducible, scalable, reviewable, and useful during real development work.

The goal of v0.2 is **not** to add heavy tooling. It is to address methodology gaps that can make an archaeology run inconsistent or difficult to reproduce.

---

## 1. v0.2 goal

LARA v0.2 should let a team run the methodology with minimal process improvisation.

The key improvements are:

- explicit evidence lifecycle,
- stable parallel-agent ID allocation,
- a defined reconstruction role,
- a protocol for items discovered during review,
- clearer skeptic authority,
- stronger finalization and revalidation gates,
- machine-readable navigation for development agents,
- better cost guidance,
- documented checkpoint/resume behavior.

The v0.2 research question is:

> Can LARA become reproducible enough that different agent teams produce comparable, traceable architectural memory from the same scoped system?

---

## 2. Design principles carried forward

v0.2 must preserve all v0.1 epistemic rules:

1. Implementation is evidence of a decision, not proof of its rationale.
2. Never invent historical rationale.
3. Separate OBSERVED, INFERRED, and UNKNOWN.
4. Every architectural claim must be traceable to evidence.
5. Every inference must carry confidence.
6. Preserve competing explanations.
7. Prefer UNKNOWN over plausible speculation.
8. Historical inconsistency is not automatically a defect.
9. Evidence precedes reconstruction.
10. Adversarial review is mandatory.
11. Current architectural consequence must be separated from historical rationale.
12. The objective is trustworthy architectural memory, not consensus.

v0.2 adds one new operational principle:

> **Every artifact must have an explicit lifecycle and provenance.**

---

# MUST CHANGE

## 3. Evidence lifecycle protocol

### Problem

Evidence may need correction after it has already been consumed by later phases. Without a defined correction mechanism, agents may improvise incompatible caveats or silently edit the original observation.

Without a formal lifecycle, future agents may:

- silently rewrite evidence,
- act on stale evidence,
- lose the history of corrections,
- produce inconsistent references.

### v0.2 design

Every evidence record gets explicit lifecycle metadata.

Required fields:

```yaml
id: E-XXXX
status: current | annotated | superseded
created_by: <role/agent instance>
created_phase: discovery | evidence | reconstruction | review
superseded_by: null | E-XXXX
annotations:
  - id: A-XXXX
    reason: correction | clarification | scope-narrowing | contradiction
    created_by: ...
```

Rules:

- evidence records are append-only after creation,
- factual corrections are added as structured annotations,
- superseded evidence remains available for traceability,
- reconstructed items must prefer current evidence,
- finalization must detect references to superseded evidence.

### Deliverables

- ✅ update `templates/evidence.md`,
- ✅ add `methodology/evidence-lifecycle.md`,
- ✅ update Phase 2 and Phase 4 prompts,
- ✅ update Reconstruction and finalization checks.

---

## 4. Parallel-agent ID namespace

### Problem

Parallel agents can generate colliding artifact IDs unless allocation is deterministic.

### v0.2 design

IDs must be deterministic per run.

Recommended format:

```text
E-<ROLE>-<INSTANCE>-<NNN>

Examples:
E-ARCH-01-001
E-DOM-01-004
E-TEST-02-011
E-SKEP-01-003
```

Architecture items remain globally numbered after reconstruction:

```text
ADR-R001
CON-001
ANO-001
AQ-001
```

The Lead assigns role-instance identifiers before work begins.

### Deliverables

- ✅ add `methodology/id-namespaces.md`,
- ✅ update Lead role,
- ✅ update bootstrap prompt,
- ✅ update templates with namespaced evidence examples.

---

## 5. Define the Reconstruction Archaeologist role

### Problem

Phase 3 was executed successfully by a generic agent, but the methodology does not define who owns synthesis.

### v0.2 design

Add a dedicated **Reconstruction Archaeologist** role.

Responsibilities:

- consume evidence, not discovery prose,
- cluster evidence by architectural significance,
- distinguish decisions, constraints, anomalies, and open questions,
- preserve competing explanations,
- avoid architecture inflation,
- identify cross-cutting relationships,
- avoid turning local evidence into global claims,
- explicitly record rejected candidate items.

The Reconstruction Archaeologist must not be the Architecture Skeptic.

### Deliverables

- ✅ add `agents/reconstruction-archaeologist.md`,
- ✅ update Lead role and bootstrap team definition,
- ✅ update Phase 3 prompt.

---

## 6. Protocol for review-discovered items

### Problem

Adversarial review can discover new architecture items, but an item must not be confirmed solely by the agent that discovered it.

### v0.2 design

Any new architecture item discovered during Phase 4 must include:

```yaml
provenance:
  discovered_during: adversarial-review
  discovered_by: <skeptic instance>
  source_item: <optional>
review_status: pending-independent-review
```

A review-discovered item must receive one of:

- review by a different Skeptic instance,
- Lead-mediated independent verification,
- explicit deferral to final output as UNVERIFIED.

It must never be marked CONFIRMED solely by the agent that created it.

### Deliverables

- ✅ add `methodology/artifact-provenance.md`,
- ✅ update Phase 4 prompt,
- ✅ update all architecture-item templates,
- ✅ update finalization gate.

---

## 7. Explicit Skeptic out-of-scope license

### Problem

Evidence needed to verify or refute a claim may exist outside the configured analysis scope.

Examples include:

- deployment configuration,
- downstream consumers,
- adjacent stacks,
- external integration wrappers.

### v0.2 design

The Architecture Skeptic may search outside the configured scope when necessary to test a claim.

Rules:

- access remains read-only,
- out-of-scope evidence must be clearly labeled,
- out-of-scope files do not become part of the analyzed scope automatically,
- findings must explain why the external evidence matters,
- the Lead must distinguish "scope evidence" from "counterexample evidence".

### Deliverables

- ✅ update Architecture Skeptic role,
- ✅ update Phase 4 prompt,
- ✅ update scope documentation.

---

# SHOULD CHANGE

## 8. System-map revalidation gate

### Problem

The provisional system map inherited several discovery-phase errors.

### v0.2 design

At the end of Phase 2:

- every architectural claim in `system-map.md` must reference evidence,
- unsupported claims must be demoted to provisional notes or removed,
- corrected discovery claims must be updated,
- known counterexamples must be recorded.

The system map used by Reconstruction must be evidence-backed.

### Deliverables

- ✅ update Phase 2 exit criteria,
- ✅ update `templates/system-map.md`,
- ✅ add canonical G1 pass/fail rules,
- ✅ update finalization consistency checks.

---

## 9. Review verdict taxonomy v2

### Problem

A useful review taxonomy must distinguish changes in evidence strength, scope, classification, confidence, and validity.

### v0.2 taxonomy

Use:

- **CONFIRMED** — claim stands materially unchanged.
- **STRENGTHENED** — claim remains valid and new evidence increases scope, consequence, or confidence.
- **NARROWED** — claim remains valid but scope or consequence is reduced.
- **RECLASSIFIED** — evidence is valid but the architecture-item type or interpretation changes.
- **CONFIDENCE DOWNGRADED** — claim remains but certainty is reduced.
- **CONTRADICTED** — evidence invalidates the claim.
- **UNRESOLVED CHALLENGE** — meaningful challenge remains without sufficient evidence to resolve it.

### Deliverables

- ✅ add canonical `methodology/review-model.md`,
- ✅ update Skeptic role,
- ✅ update Phase 4 prompt,
- ✅ update architecture templates,
- ✅ define canonical verdict fields for future metrics.

---

## 10. Machine-readable architecture manifest

### Problem

An architecture index without code-location mapping forces development agents to scan the full artifact set.

### v0.2 design

Generate:

```text
docs/architecture/manifest.yaml
```

Minimum model:

```yaml
revision: <git revision>

items:
  ADR-R001:
    type: decision
    confidence: high
    paths:
      - src/example/**
    evidence:
      - E-ARCH-01-001
    related:
      - CON-002
      - ANO-004

path_index:
  src/example/**:
    - ADR-R001
    - CON-002
    - ANO-004
```

The manifest is a navigation aid, not a replacement for Markdown artifacts.

### Deliverables

- ✅ add `methodology/development-navigation.md`,
- ✅ add `templates/manifest.yaml`,
- ✅ update Phase 5 prompt,
- ✅ update development-context prompt,
- ✅ validate manifest consistency in G3.

---

## 11. Path/module → architecture navigation

### Goal

A coding agent should be able to ask:

> I am changing these files. Which architectural items matter?

Without scanning the entire architecture memory.

### v0.2 design

The finalization phase builds path/module mappings from architecture items.

The mappings should support:

- exact paths,
- directory scopes,
- glob-like territory descriptors,
- subsystem names where paths are unstable.

### Deliverables

- ✅ integrate path/module/global navigation with `manifest.yaml`,
- ✅ add evidence-backed Affected territory metadata to architecture-item templates,
- ✅ update architecture README,
- ✅ update `prompts/use-architecture-memory.md`,
- ✅ define safe fallback behavior for index misses.

---

## 12. Operations / deployment evidence

### Problem

Deployment configuration can contain decisive architectural evidence without being naturally owned by an existing specialist.

### v0.2 design

Two supported modes:

### Default

The Architecture Cartographer explicitly inspects runtime/deployment configuration.

### Optional specialist

For infrastructure-heavy systems, add:

**Operations & Deployment Archaeologist**

Focus:

- deployment topology,
- worker counts and partitioning,
- environment overrides,
- runtime feature flags,
- scheduling,
- process ownership,
- operational constraints.

### Deliverables

- ✅ expand Cartographer role,
- ✅ add optional Operations & Deployment Archaeologist role,
- ✅ update bootstrap guidance and scope configuration.

---

## 13. Discovery + Evidence cost optimization

### Problem

Discovery and Evidence Collection can repeat much of the same repository reading, increasing context and execution cost without improving evidentiary quality.

### v0.2 design

Keep Discovery and Evidence as separate methodological phases, but allow one specialist session to continue across both.

Recommended flow:

```text
Specialist context
    ↓
Discovery
    ↓
explicit phase checkpoint
    ↓
Evidence extraction
```

The agent must not generate evidence records until Discovery is explicitly closed.

### Modes

```text
strict:
  separate agent execution per phase

economical:
  continued specialist context across Phases 1–2
```

### Deliverables

- ✅ add `methodology/execution-modes.md`,
- ✅ support strict and economical Phase 1–2 execution,
- ✅ enforce explicit Discovery → Evidence barrier,
- ✅ update Lead guidance,
- ✅ record execution mode in run metadata.

---

# NICE TO HAVE

## 14. Checkpoint / resume protocol

### Problem

Agent interruptions are safely recoverable only when meaningful state is durable and the resume procedure is explicit.

### v0.2 design

✅ Implemented in `methodology/checkpoint-resume.md` and `templates/phase-state.yaml`.

The protocol records agent namespace cursors, pending/completed territory, partial artifacts, interruptions, gates, and target revision so a run can resume from durable files rather than agent memory.



Durable working state lives outside final architecture memory:

```text
docs/architecture-working/
├── phase-state.yaml
├── discovery/
└── notes/
```

Example:

```yaml
phase: evidence
status: in-progress
completed_agents:
  - domain-01
  - test-01
pending_agents:
  - history-01
last_verified_artifact: E-TEST-01-014
```

Document safe restart behavior:

- reload methodology,
- read current phase state,
- do not recreate completed artifacts,
- resume only pending work,
- run consistency check after recovery.

No executable tooling is required yet.

### Deliverables

- ✅ add `methodology/checkpoint-resume.md`,
- ✅ add `templates/phase-state.yaml`,
- ✅ persist namespace cursors for safe resume,
- ✅ define target-revision mismatch handling,
- ✅ define interrupted/partial artifact behavior,
- ✅ quarantine working state from normal development consumption.

---

## 15. Standardized run metadata

Every run should capture:

- target revision,
- run date,
- scope file,
- execution mode,
- agent roles,
- agent instance count,
- phases completed,
- model/runtime details where available,
- external orchestration mode,
- interruptions / resumes.

Store in:

```text
docs/architecture/run.yaml
```

### Deliverables

- ✅ add `templates/run.yaml`,
- ✅ record stable run ID and target revision,
- ✅ record execution mode, agent allocation, phases, gates, interruptions, and resumes,
- ✅ preserve unavailable runtime/model/cost metadata as `unknown` rather than guessing.

---

## 16. Standardized post-run metrics

Every run should report:

```yaml
run:
  scope: small | medium | large
  phases_completed: 5

artifacts:
  evidence: N
  recovered_adrs: N
  constraints: N
  anomalies: N
  open_questions: N

review:
  confirmed: N
  strengthened: N
  narrowed: N
  reclassified: N
  confidence_downgraded: N
  contradicted: N
  unresolved_challenge: N

quality:
  evidence_traceability: low | medium | high
  inference_discipline: low | medium | high
  rationale_hallucination_risk: low | medium | high
  adversarial_effectiveness: low | medium | high
  output_usability: low | medium | high
  duplication_level: low | medium | high

cost:
  approximate_tokens: N | unknown
  wall_clock: <duration> | unknown

recommendation:
  run_another_pilot: yes | no
```

This enables run-to-run comparison.

### Deliverables

- ✅ add `methodology/run-metrics.md`,
- ✅ add `templates/metrics.yaml`,
- ✅ standardize artifact, evidence-lifecycle, review, correction, navigation, quality, and cost metrics,
- ✅ require qualifiers such as scope size and execution mode for comparison,
- ✅ support sanitized external methodology reporting.

---

## 17. Discovery-note quarantine

### Problem

Discovery notes are provisional but visually resemble authoritative architecture documentation.

### v0.2 design

✅ Implemented.

Working notes live outside final architecture memory:

```text
docs/architecture-working/
├── phase-state.yaml
├── discovery/
└── notes/
```

The system map may exist at its final path during Discovery only while explicitly marked `map_status: provisional`.

Final coding agents must not consume Discovery working notes by default.

---

# 18. Proposed v0.2 repository changes

```text
LARA/
├── PLAN-v0.2.md
├── methodology/
│   ├── evidence-lifecycle.md
│   ├── id-namespaces.md
│   └── ...
├── agents/
│   ├── reconstruction-archaeologist.md
│   ├── operations-deployment-archaeologist.md   # optional role
│   └── ...
├── prompts/
│   └── ...
├── templates/
│   ├── manifest.yaml
│   ├── run.yaml
│   ├── metrics.yaml
│   ├── phase-state.yaml
│   └── ...
└── examples/
    └── ...
```

---

# 19. Implementation sequence

Implement v0.2 in this order:

## Step 1 — Lifecycle and identity ✅ IMPLEMENTED

Implemented in v0.2 work:

- evidence lifecycle with immutable original observations and explicit state transitions,
- deterministic parallel-agent ID namespaces,
- architecture-item provenance fields,
- review-discovered item independent-review protocol,
- lifecycle-aware Phase 2, Reconstruction, Review, and Finalization prompts,
- finalization consistency checks for IDs, annotations, supersession, and provenance.

These rules now form the identity and lifecycle foundation for every later v0.2 artifact.

## Step 2 — Roles and review model ✅ IMPLEMENTED

Implemented in v0.2 work:

- dedicated Reconstruction Archaeologist owns Phase 3 synthesis,
- optional Operations & Deployment Archaeologist for infrastructure-heavy systems,
- Architecture Cartographer retains default runtime/deployment mapping responsibility,
- Skeptic has an explicit read-only out-of-scope counterexample license,
- review status is separated from review verdict,
- verdict taxonomy v2 adds STRENGTHENED and RECLASSIFIED and clarifies nearby outcomes,
- bootstrap, Lead role, Phase 3/4 prompts, scope configuration, provenance rules, and architecture templates are aligned to the new model.

## Step 3 — Workflow gates ✅ IMPLEMENTED

Implemented in v0.2 work:

- canonical `methodology/workflow-gates.md` with explicit pass/fail semantics,
- G1 Evidence Revalidation Gate between Evidence and Reconstruction,
- `system-map.md` now transitions from `provisional` to `evidence-revalidated`,
- Reconstruction is blocked unless G1 passes,
- G2 Review Discovery Verification Gate requires independent primary-source verification rather than a second-agent rubber stamp,
- review-discovered items must end reviewed, Lead-verified, or explicitly UNVERIFIED,
- G3 Finalization Consistency Gate validates identity, lifecycle, map state, provenance, review completeness, cross-links, and scope integrity,
- G3 distinguishes blockers from non-blocking warnings,
- Finalization now produces `docs/architecture/validation.md` using a standard template,
- final architecture README surfaces gate status, warnings, and unverified items.

## Step 4 — Development usability ✅ IMPLEMENTED

Implemented in v0.2 work:

- canonical `methodology/development-navigation.md`,
- machine-readable `docs/architecture/manifest.yaml` generated during Finalization,
- manifest item registry preserves artifact path, confidence, review state, evidence, relations, and affected territory,
- architecture-item templates now capture evidence-backed Affected territory during Reconstruction rather than inventing scope during Finalization,
- reverse `path_index` and `module_index` plus evidence-backed `global_items`,
- cross-cutting items remain discoverable even when no changed path matches,
- index misses explicitly fall back to system-map/module inspection rather than implying architecture-neutrality,
- `use-architecture-memory.md` now starts from changed paths/modules and builds a bounded architecture context set,
- unverified, contradicted, unresolved, and reclassified review states are handled explicitly during development,
- G3 validates manifest completeness, references, revision, review metadata, and scope integrity,
- final architecture README exposes navigation coverage and gaps.

## Step 5 — Execution efficiency ✅ IMPLEMENTED

Implemented in v0.2 work:

- canonical `methodology/execution-modes.md`,
- `strict` mode with fresh Phase 2 specialist contexts,
- `economical` mode with continued specialist context behind a hard Discovery → Evidence checkpoint/barrier,
- Discovery cannot create evidence records in either mode,
- canonical `methodology/checkpoint-resume.md`,
- durable `docs/architecture-working/phase-state.yaml` state,
- namespace cursors preserved across interruption/resume,
- target revision mismatches explicitly block silent resume,
- Discovery notes quarantined under `docs/architecture-working/`,
- standardized final `docs/architecture/run.yaml`,
- standardized final `docs/architecture/metrics.yaml`,
- artifact, review, correction, navigation, quality, and cost metrics for run-to-run comparison,
- unknown runtime/token values remain `unknown` rather than being fabricated,
- G3 validates run IDs, revisions, execution mode, run state, and final metric counts.

---

# 20. v0.2 acceptance criteria

LARA v0.2 is complete when:

- evidence records have explicit lifecycle status,
- parallel agents can generate collision-free IDs without Lead improvisation,
- Phase 3 has a defined Reconstruction Archaeologist role,
- review-discovered items cannot self-confirm,
- Skeptics are explicitly allowed to search outside scope for counterevidence,
- the system map is evidence-revalidated before reconstruction,
- the review taxonomy captures strengthened and reclassified outcomes,
- final architecture memory includes a machine-readable manifest,
- a coding agent can map changed paths to relevant architecture items,
- discovery notes are clearly quarantined from final memory,
- interrupted runs have a documented safe-resume procedure,
- post-run metrics are standardized,
- the methodology supports a lower-cost continued-context mode for Phases 1–2.

---

# 21. Validation plan

A future evaluation should test whether v0.2 improves reproducibility and development usefulness.

Prefer one of:

### Option A — Known-ground-truth subsystem

Use a subsystem where trusted architectural documentation already exists.

Compare reconstructed LARA memory against known decisions.

Measure:

- true positives,
- missed decisions,
- false positives,
- invented rationale,
- scope errors,
- confidence calibration.

### Option B — Comparable bounded subsystem

Use a bounded subsystem with comparable size and evidence types.

Compare:

- token cost,
- coordination friction,
- evidence correction rate,
- review outcome distribution,
- architecture-memory usability.

### Option C — Development A/B experiment

Give two coding agents the same non-trivial legacy change:

#### Agent A

Repository only.

#### Agent B

Repository + LARA architectural memory.

Compare:

- constraints identified,
- invariants preserved,
- risky assumptions,
- architecture impacts noticed,
- regressions,
- need for human correction.

The A/B experiment is the strongest test of LARA's core value.

---

# 22. Explicitly out of scope for v0.2

Still do not build:

- graph database,
- vector database,
- full CLI product,
- autonomous repository mutation,
- automatic architecture scoring,
- CI enforcement,
- IDE plugin,
- continuous background archaeology service.

If validation shows that manifest generation, ID management, lifecycle checks, or cross-link validation are too error-prone manually, those become candidates for a minimal v0.3 CLI.

---

# 23. v0.2 implementation status

All five planned v0.2 implementation steps are now implemented:

1. Lifecycle and identity ✅
2. Roles and review model ✅
3. Workflow gates ✅
4. Development usability ✅
5. Execution efficiency ✅

The remaining work is empirical validation.

The acceptance criteria are represented in the methodology, prompts, templates, and gates. Future validation must test whether the added rigor improves reproducibility and usability without unacceptable cost or process weight.

---

# 24. Success condition

v0.2 succeeds if the next archaeology run requires significantly less Lead improvisation while preserving or improving:

- evidence traceability,
- inference discipline,
- adversarial effectiveness,
- architectural usefulness,
- development-context usability.

The methodology should become more reproducible **without becoming heavier than the legacy system it is trying to understand**.
