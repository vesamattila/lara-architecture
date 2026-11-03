# Checkpoint and resume protocol

LARA treats files as the durable state of an archaeology run.

Agent context is disposable.

A run must be resumable without trusting an interrupted agent's memory.

## Working-state location

Transient run state lives under:

```text
docs/architecture-working/
├── phase-state.yaml
├── discovery/
└── notes/
```

This directory is working state, not final architectural memory.

Future coding agents should not consume it by default.

Final architecture memory lives under:

```text
docs/architecture/
```

## Phase state

The canonical checkpoint file is:

```text
docs/architecture-working/phase-state.yaml
```

Use `templates/phase-state.yaml`.

It records:

- run ID,
- target revision,
- execution mode,
- current phase,
- phase status,
- completed gates,
- agent status,
- artifact cursors,
- pending work,
- interruptions.

## Phase status values

Allowed values:

- `not-started`
- `in-progress`
- `checkpointed`
- `passed`
- `failed`
- `complete`

A phase transition must be persisted before new-phase work begins.

## Required checkpoints

Write a checkpoint:

1. after agent allocation,
2. at the end of Discovery,
3. after G1,
4. after Reconstruction,
5. after each material Review batch,
6. after G2 completion,
7. before G3,
8. after G3,
9. whenever an interruption or rate limit stops progress.

## Namespace cursors

For every agent instance, record the next unused local ID numbers.

Example:

```yaml
agents:
  TEST-01:
    status: completed
    next_evidence_number: 15
    next_annotation_number: 3
    last_artifact: E-TEST-01-014
```

On resume:

- continue from the recorded next number,
- never scan for a convenient free number and reuse a gap,
- never reset a namespace to `001`.

## Resume algorithm

When resuming a run:

1. read `CLAUDE.md`,
2. read the methodology files relevant to the current phase,
3. read `phase-state.yaml`,
4. verify that the target revision still matches the run revision,
5. verify completed gates,
6. verify that checkpointed artifacts actually exist,
7. restore agent identities and namespace cursors,
8. identify completed vs pending territory,
9. resume only pending work,
10. run a consistency check before the next phase transition.

## Target revision mismatch

If the target repository revision changed during an interrupted run:

- do not silently continue,
- record the new revision,
- identify changed files,
- determine whether existing evidence may be stale,
- either restore the original target revision or explicitly restart/revalidate affected work.

A run spanning multiple target revisions must not present itself as a single-revision reconstruction.

## Restarting an agent

If an agent process/context dies but its assigned work continues:

- keep the same agent identity when it is a continuation,
- reload its role,
- reload its completed artifacts,
- restore namespace cursors,
- resume pending territory only.

If the Lead intentionally introduces an additional independent worker, assign a new instance identity.

## Completed work

Do not regenerate completed artifacts merely because a new agent context lacks memory of creating them.

Read and verify them.

Regenerate only when:

- the artifact is missing,
- checkpoint consistency fails,
- lifecycle/provenance rules require correction,
- target revision changed materially.

## Interrupted writes

If an interruption leaves a partial artifact:

- do not treat it as completed,
- record it under `partial_artifacts`,
- verify whether it has a stable ID,
- either finish it without changing identity or explicitly abandon it,
- never silently reuse an abandoned ID.

## Finalization

Finalization records interruption/resume history in `docs/architecture/run.yaml`.

The working `phase-state.yaml` may remain for audit/debugging, but it is not required reading for normal development use.

## Principle

> **Resume from durable artifacts, not from remembered conversation state.**
