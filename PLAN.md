# LARA v0.1 Implementation Plan

**LARA — Legacy Architecture Reconstruction & Archaeology**

This plan captures the initial product and methodology ideas so the first implementation can be built without losing the reasoning behind the project.

## 1. Goal

Build a repository-based methodology and prompt framework that enables an AI agent team to reconstruct the architectural memory of a legacy software system.

The first version deliberately contains **no custom executable tooling**. The hypothesis should be tested with prompts, agent roles, structured evidence, and Markdown artifacts before adding automation.

## 2. Core research question

> Can a well-orchestrated AI agent team reconstruct architectural memory reliably enough to improve subsequent changes to legacy software?

A later validation experiment should compare AI-assisted changes:

- with reconstructed architectural memory,
- without reconstructed architectural memory.

Useful outcomes include better detection of hidden constraints, invariants, architectural side effects, and risky changes.

## 3. Core epistemic model

LARA must enforce these rules throughout the workflow:

1. **Implementation is evidence of a decision, not proof of its rationale.**
2. Never invent historical rationale.
3. Separate **OBSERVED**, **INFERRED**, and **UNKNOWN**.
4. Every architectural claim must link to concrete evidence.
5. Every inference must include a confidence level.
6. Preserve competing explanations when evidence is inconclusive.
7. Prefer UNKNOWN over plausible speculation.
8. Historical inconsistency is not automatically a defect.
9. Repetition does not automatically imply intentional architecture.
10. Tests, migrations, configuration, and history may reveal stronger intent than production code alone.
11. Distinguish historical rationale from current architectural consequence.
12. Optimize for trustworthy claims rather than artificial consensus.

## 4. Architecture memory model

LARA should produce four primary types of architectural memory.

### Recovered ADR

A durable architectural decision or policy supported by current evidence.

A recovered ADR may have high confidence that the decision exists while the original rationale remains unknown.

### Constraint

A limitation, invariant, compatibility requirement, consistency boundary, or other condition that materially shapes future implementation choices.

### Anomaly

An architectural tension, inconsistency, duplicate pattern, unfinished migration, or divergence that increases change risk.

An anomaly is not automatically a defect.

### Open question

An architecturally important uncertainty that cannot be resolved reliably from available evidence.

Open questions are first-class output, not failed ADRs.

## 5. Evidence model

Architecture reconstruction must begin with evidence, not ADR generation.

Evidence may come from:

- production code,
- tests,
- database migrations,
- configuration,
- API schemas,
- deployment manifests,
- feature flags,
- dependency definitions,
- comments and TODOs,
- Git history,
- issues and pull requests,
- existing documentation and ADRs.

Each evidence record should have:

- stable ID,
- classification,
- source references,
- direct observation,
- architectural significance,
- confidence,
- caveats,
- related evidence.

## 6. Agent Team

The baseline team should contain the following roles.

### Lead Archaeologist

Coordinates the investigation, enforces phase boundaries, manages scope, and prevents unsupported consensus.

### Architecture Cartographer

Maps modules, dependencies, runtime boundaries, processes, APIs, and structural inconsistencies.

### Domain Archaeologist

Recovers domain concepts, invariants, lifecycles, state transitions, and hidden coupling.

### Data & Integration Archaeologist

Investigates persistence, transactions, consistency, messaging, retries, idempotency, external integrations, and storage boundaries.

### Test Archaeologist

Uses tests as evidence of intended behavior, regression history, compatibility promises, and protected invariants.

### History Archaeologist

Uses version history and historical artifacts to recover explicit rationale where it actually exists.

### Architecture Skeptic

Attempts to falsify reconstructed claims, find counterexamples, challenge scope, and expose plausible but unsupported stories.

The skeptic is intentionally independent from the initial reconstruction.

## 7. Workflow

### Phase 1 — Discovery

Map the system before reconstructing decisions.

Outputs:

- system map,
- specialty discovery notes,
- high-risk areas,
- unexplored areas.

No ADRs should be created in this phase.

### Phase 2 — Evidence collection

Create stable evidence records from concrete repository sources.

Outputs:

- evidence records,
- source conflicts,
- evidence gaps.

No ADR synthesis yet.

### Phase 3 — Reconstruction

Cluster evidence into:

- recovered ADRs,
- constraints,
- anomalies,
- open questions.

Every reconstructed item must reference evidence IDs.

### Phase 4 — Adversarial review

The Architecture Skeptic attempts to disprove every reconstructed item.

Review outcomes:

- CONFIRMED
- NARROWED
- CONFIDENCE DOWNGRADED
- CONTRADICTED
- UNRESOLVED CHALLENGE

### Phase 5 — Finalization

Publish the architecture memory in a form future coding agents can navigate and use.

## 8. Target output structure

A normal LARA run should produce something equivalent to:

```text
docs/architecture/
├── README.md
├── system-map.md
├── evidence/
│   ├── E-0001.md
│   └── ...
├── decisions/
│   ├── ADR-R001.md
│   └── ...
├── constraints/
│   ├── CON-001.md
│   └── ...
├── anomalies/
│   ├── ANO-001.md
│   └── ...
└── questions/
    ├── AQ-001.md
    └── ...
```

## 9. Development-context integration

The architecture memory exists to improve future implementation work.

A coding agent working on a change should identify:

- **PRESERVED** — decisions and constraints the change preserves,
- **AFFECTED** — architecture items touched by the change,
- **SUPERSEDED** — existing decisions intentionally replaced,
- **RISKS** — relevant anomalies, unresolved questions, or low-confidence assumptions.

A coding agent should never silently violate a recovered architectural decision.

If a change establishes a new architectural decision, it should propose a new ADR.

LARA provides `prompts/use-architecture-memory.md` to operationalize this step during feature and refactoring work.

## 10. Scope configuration

LARA should support both full-system and focused archaeology.

A scope manifest should allow:

- include/exclude source paths,
- optional focus areas,
- Git history inspection,
- output location,
- target-code modification safety.

Focused archaeology should be encouraged for very large systems.

## 11. Repository deliverables for v0.1

The repository should contain:

```text
LARA/
├── README.md
├── CLAUDE.md
├── PLAN.md
├── scope.example.yaml
├── methodology/
│   ├── principles.md
│   ├── evidence-model.md
│   ├── confidence-model.md
│   └── workflow.md
├── agents/
│   ├── lead.md
│   ├── architecture-cartographer.md
│   ├── domain-archaeologist.md
│   ├── data-integration-archaeologist.md
│   ├── test-archaeologist.md
│   ├── history-archaeologist.md
│   └── architecture-skeptic.md
├── prompts/
│   ├── run-archaeology.md
│   ├── phase-01-discovery.md
│   ├── phase-02-evidence.md
│   ├── phase-03-reconstruction.md
│   ├── phase-04-adversarial-review.md
│   ├── phase-05-finalize.md
│   └── use-architecture-memory.md
└── templates/
    ├── architecture-readme.md
    ├── system-map.md
    ├── evidence.md
    ├── adr-recovered.md
    ├── constraint.md
    ├── anomaly.md
    └── question.md
```

## 12. v0.1 acceptance criteria

LARA v0.1 is complete when:

- the methodology is explicit and internally consistent,
- all baseline agent roles are defined,
- every workflow phase has an executable prompt,
- artifact templates preserve observation/inference/unknown distinctions,
- evidence precedes reconstruction,
- adversarial review is mandatory,
- scope can be configured,
- target source modification is disabled by default,
- the README contains a usable quick-start path,
- architecture memory can be consumed explicitly during future development work,
- a user can point Claude Code at LARA and a target repository and run the method without custom software.

## 13. Explicitly out of scope for v0.1

Do not build these until real archaeology runs demonstrate a need:

- CLI application,
- database or vector store,
- automatic evidence indexing,
- duplicate detection service,
- graph database,
- incremental code-to-ADR lookup engine,
- CI integration,
- IDE integration,
- automatic architecture scoring,
- autonomous modification of the target system.

## 14. Candidate v0.2 work

After the first real experiments, consider:

- machine-readable schemas for evidence and decisions,
- incremental archaeology,
- changed-files-to-architecture-context lookup,
- duplicate evidence detection,
- stale ADR detection,
- architecture memory diffing,
- automatic context packs for coding agents,
- validation metrics,
- experiment harness for comparing informed vs uninformed implementation agents.

## 15. First experiment

Choose a real legacy repository with:

- non-trivial history,
- tests,
- migrations or infrastructure evolution,
- visible architectural layering.

Run LARA against a bounded scope first.

Then give another AI agent the same non-trivial change twice:

1. repository only,
2. repository + LARA architectural memory.

Compare:

- constraints identified,
- invariants preserved,
- risky assumptions made,
- architecture impacts noticed,
- regressions introduced,
- need for human correction.

The experiment should test whether LARA improves development decisions rather than merely producing convincing documentation.
