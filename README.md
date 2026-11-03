# LARA

**Legacy Architecture Reconstruction & Archaeology**

LARA is an experimental, repository-driven methodology for recovering architectural knowledge from legacy software. It helps AI agent teams separate what a codebase directly shows from what can only be inferred—and from what remains unknown—before future agents change the system.

## The problem

Legacy repositories preserve implementation but often lose the decisions, constraints, migrations, and tradeoffs that shaped it. A coding agent can read the code and still mistake a compatibility boundary for accidental complexity or invent a plausible rationale that the evidence does not support.

## The approach

LARA gives a Claude Code agent team a five-phase investigation process:

1. map the system without prematurely creating decisions;
2. collect traceable repository evidence;
3. reconstruct candidate decisions, constraints, anomalies, and open questions;
4. challenge those conclusions independently; and
5. publish only claims that pass explicit consistency gates.

Every claim is classified as:

- **OBSERVED** — directly supported by repository evidence;
- **INFERRED** — a reasoned interpretation with an explicit confidence level; or
- **UNKNOWN** — important context that the available evidence cannot establish.

The key differentiator is adversarial traceability: implementation is treated as evidence of a decision, not proof of its original rationale. Evidence corrections are append-only, reconstruction and skepticism are independently owned, and unresolved challenges remain visible.

## Current status

LARA v0.2 is an **experimental methodology and prompt set**, not an installed application, CLI, hosted service, or autonomous analysis product. Its current functionality consists of:

- Markdown methodology and role definitions;
- prompts for Claude Code agent teams;
- YAML and Markdown artifact templates;
- workflow gates, evidence lifecycle rules, and review taxonomy; and
- a manifest-based convention for using recovered architecture during development.

The methodology has not yet been established as generally effective. Empirical validation, automation, integrations, and executable tooling are future research—not current features. See [PLAN-v0.2.md](PLAN-v0.2.md) for the implementation history and proposed validation work.

## Minimal quick start

LARA currently assumes access to Claude Code with Agent Teams support.

1. Clone this repository and the target repository.
2. Copy [scope.example.yaml](scope.example.yaml) to the target repository as `scope.yaml`, then bound the included paths and exclusions.
3. Give Claude Code [prompts/run-archaeology.md](prompts/run-archaeology.md), the target repository path, and the scope file.
4. Choose `economical` or `strict` execution mode and let the five phases run in order.
5. Review the generated `docs/architecture/validation.md` before treating any recovered artifact as usable.

Start with a small subsystem. LARA defaults to read-only analysis and should not modify target application code unless explicitly authorized.

For a safe walkthrough, see the [clearly illustrative order-import example](examples/illustrative-order-import/README.md). It demonstrates source evidence, OBSERVED/INFERRED/UNKNOWN distinctions, a recovered decision, and a narrowing review. It is not presented as output from an actual LARA run.

## What a run produces

A finalized run normally creates:

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

The four primary architecture artifact types are:

- **recovered ADRs** — decisions supported by current evidence;
- **constraints** — invariants and limitations relevant to future changes;
- **anomalies** — architectural tensions, divergence, and risky historical layers; and
- **open questions** — important uncertainties the evidence cannot resolve.

The manifest is a navigation aid, not architectural truth. A path-index miss must fall back to system-map or module inspection.

## Methodology map

The detailed methodology remains the authoritative reference:

- [principles](methodology/principles.md) — epistemic rules;
- [workflow](methodology/workflow.md) and [workflow gates](methodology/workflow-gates.md) — phase order and pass/fail criteria;
- [evidence model](methodology/evidence-model.md) and [evidence lifecycle](methodology/evidence-lifecycle.md) — traceability and correction;
- [confidence model](methodology/confidence-model.md) — calibration;
- [artifact provenance](methodology/artifact-provenance.md) and [review model](methodology/review-model.md) — independent review;
- [ID namespaces](methodology/id-namespaces.md) — collision-free parallel work;
- [execution modes](methodology/execution-modes.md) and [checkpoint/resume](methodology/checkpoint-resume.md) — reproducible operation;
- [development navigation](methodology/development-navigation.md) — using architecture memory during code changes; and
- [run metrics](methodology/run-metrics.md) — comparable, sanitized reporting.

Role definitions live under [`agents/`](agents/), phase prompts under [`prompts/`](prompts/), and source-controlled artifact templates under [`templates/`](templates/).

## Agent team

The baseline investigation separates responsibilities across:

- Lead Archaeologist;
- Architecture Cartographer;
- Domain Archaeologist;
- Data & Integration Archaeologist;
- Test Archaeologist;
- History Archaeologist;
- Reconstruction Archaeologist; and
- Architecture Skeptic.

An Operations & Deployment Archaeologist is optional for infrastructure-heavy scopes. The Reconstruction Archaeologist must remain independent from the Architecture Skeptic.

## Using recovered architecture during development

For a later feature, refactor, or bug fix, use [prompts/use-architecture-memory.md](prompts/use-architecture-memory.md). A coding agent starts from changed paths or modules, resolves relevant items through `docs/architecture/manifest.yaml`, reads the authoritative Markdown artifacts, and states what the change:

- **PRESERVES**;
- **AFFECTS**;
- **SUPERSEDES**; and
- **RISKS**.

Transient discovery and checkpoint state belongs under `docs/architecture-working/` and is not normal development input.

## Safety and validation

LARA output can contain sensitive facts from a target repository. Keep generated output isolated, review it before sharing, and never assume that generated architecture memory is safe to publish.

Repository validation commands are documented in [VALIDATION.md](VALIDATION.md).

## License

LARA is licensed under the [MIT License](LICENSE).
