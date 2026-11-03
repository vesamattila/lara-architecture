# LARA — Claude Code instructions

LARA is a methodology for reconstructing architectural memory from legacy software.

## Objective

Do not merely describe a target repository. Recover the architectural decisions, constraints, invariants, tensions, and unresolved questions that future development agents need in order to change the system safely.

## Non-negotiable epistemic rules

1. Code is evidence, not explanation.
2. Never invent historical rationale.
3. Distinguish **OBSERVED**, **INFERRED**, and **UNKNOWN**.
4. Every architectural claim must cite concrete evidence.
5. Every inference must state a confidence level.
6. Preserve competing explanations when evidence is inconclusive.
7. Prefer UNKNOWN over plausible speculation.
8. Historical inconsistency is not automatically a defect.
9. Repetition does not prove intentional architecture.
10. Tests, migrations, configuration, and history may reveal stronger intent than implementation alone.
11. Original evidence observations are immutable after creation.
12. Evidence corrections use lifecycle transitions, replacement evidence, and append-only annotations.
13. Every artifact must have explicit lifecycle and provenance.
14. Never consume superseded evidence as current support.

## Workflow

Follow the phases in `prompts/` in order:

1. discovery
2. evidence collection
3. reconstruction
4. adversarial review
5. finalization

Do not create recovered ADRs during initial discovery.

Use the role definitions under `agents/` when creating an Agent Team.

Use the templates under `templates/` for generated artifacts.

Before parallel work begins, the Lead must assign agent instance identities using `methodology/id-namespaces.md`.

Evidence corrections must follow `methodology/evidence-lifecycle.md`.

Architecture-item provenance must follow `methodology/artifact-provenance.md`.

Adversarial review must follow `methodology/review-model.md`.

Phase 3 synthesis is owned by a dedicated Reconstruction Archaeologist that must be independent from the Architecture Skeptic.

The Skeptic may perform read-only out-of-scope counterexample searches when needed to test a claim; such evidence must be labeled and must not silently expand the analyzed scope.

Phase transitions and Finalization must obey `methodology/workflow-gates.md`:

- G1 before Reconstruction,
- G2 for every review-discovered architecture item,
- G3 before Finalization is declared complete.

A failed gate blocks progress. Do not downgrade blockers into warnings merely to complete the run.

Execution mode must follow `methodology/execution-modes.md`.

Checkpoint and resume behavior must follow `methodology/checkpoint-resume.md`.

Run metadata and metrics must follow `methodology/run-metrics.md`.

Discovery working notes and transient run state belong under `docs/architecture-working/` and must not be treated as final architectural memory.

Development navigation must follow `methodology/development-navigation.md`.

`manifest.yaml` is an index, not a source of architectural truth. A path-index miss never proves that no architecture applies.

## Target repository safety

Unless explicitly instructed otherwise:

- do not modify target application code,
- do not run destructive commands,
- do not change dependencies,
- do not rewrite history,
- keep LARA output isolated from production code.

## Architectural memory output

A target project should normally receive:

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

The goal is not documentation completeness.

The goal is **trustworthy architectural memory**.
