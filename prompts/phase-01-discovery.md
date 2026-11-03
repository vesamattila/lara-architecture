# Phase 01 — Discovery

## Goal

Build a shared map of the target system before attempting to reconstruct architectural decisions.

## Execution mode

Read `methodology/execution-modes.md`.

Both `strict` and `economical` modes use the same Discovery rules.

In economical mode, specialist contexts may continue into Phase 2 **only after the explicit phase barrier below**.

Retained context does not turn Discovery observations into evidence.

## Lead instructions

Delegate independent exploration to the specialist agents.

Ask each agent to identify:

- important structural areas,
- likely architectural boundaries,
- unusual patterns,
- inconsistencies,
- high-risk areas,
- candidate sources of architectural evidence.

The Lead should combine these findings into a provisional system map without turning them into architectural decisions.

## Restrictions

Do not create ADRs.

Do not create evidence records or evidence IDs.

Do not infer original rationale.

Do not resolve inconsistencies into a single story.

Do not treat unfamiliar code as technical debt merely because it looks unusual.

## Working output

Discovery is provisional working state.

Create/update under the configured working directory, normally:

```text
docs/architecture-working/
├── phase-state.yaml
├── discovery/
│   ├── architecture.md
│   ├── domain.md
│   ├── data-integration.md
│   ├── tests.md
│   ├── history.md
│   └── operations.md        # when OPS is used
└── notes/
```

The provisional system map may be created at its final path if desired, but it must remain:

```yaml
map_status: provisional
```

until G1 passes.

Discovery specialty notes must **not** be stored among final decisions, constraints, anomalies, questions, or evidence.

Future coding agents should not consume `docs/architecture-working/` by default.

## Coverage review

Before closing Discovery ask:

- What important parts of the configured scope remain unexplored?
- Which areas deserve deeper evidence collection?
- Which apparent patterns already have known counterexamples?
- Which Discovery claims most need primary-source verification?

## Phase checkpoint

Before Phase 1 closes:

1. persist all Discovery working notes,
2. update `phase-state.yaml`,
3. record each agent's completed and pending territory,
4. record namespace cursors even though no evidence IDs should yet have been created,
5. set Discovery status to `checkpointed`,
6. have the Lead explicitly close Discovery.

## Discovery → Evidence barrier

Evidence Collection may begin only after the Lead issues an explicit:

> **BEGIN EVIDENCE**

transition.

### strict mode

End Discovery specialist sessions.

Start fresh Phase 2 specialist contexts as configured.

### economical mode

The same specialist contexts may continue, but they must:

- re-read the Phase 2 evidence rules,
- verify every observation from primary repository sources,
- create evidence only after the barrier,
- never copy Discovery prose into evidence without verification.

## Exit criterion

Only proceed when:

- the team has enough system orientation to collect evidence intentionally,
- Discovery working state is checkpointed,
- the Lead has closed Phase 1,
- the execution-mode transition is recorded in `phase-state.yaml`.
