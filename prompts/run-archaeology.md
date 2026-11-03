# Bootstrap prompt

Use this prompt from the LARA repository to start an archaeology run.

---

Use the methodology defined in this repository to analyze the target repository at:

`<TARGET_PATH>`

Scope configuration:

`<SCOPE_FILE or scope description>`

Create an Architecture Archaeology Agent Team.

## Required roles

- Lead Archaeologist
- Architecture Cartographer
- Domain Archaeologist
- Data & Integration Archaeologist
- Test Archaeologist
- History Archaeologist
- Reconstruction Archaeologist
- Architecture Skeptic

## Optional role

Add **Operations & Deployment Archaeologist** when runtime/deployment configuration is large, environment-specific, or appears to enforce load-bearing invariants.

Read the methodology and role definitions before starting.

Before parallel work begins:

1. read `methodology/id-namespaces.md`,
2. assign every agent instance a stable role-instance ID,
3. publish the run's agent allocation,
4. assign clear investigation territory,
5. require each agent to create evidence and annotations only in its own namespace.

Read:

- `methodology/evidence-lifecycle.md`
- `methodology/artifact-provenance.md`
- `methodology/review-model.md`
- `methodology/execution-modes.md`
- `methodology/checkpoint-resume.md`
- `methodology/run-metrics.md`

before starting the run.

## Initialize durable run state

Before Phase 1:

1. determine the configured execution mode: `strict` or `economical`,
2. create a stable run ID,
3. record the target repository revision,
4. create the configured working directory, normally `docs/architecture-working/`,
5. initialize `phase-state.yaml` using `templates/phase-state.yaml`,
6. record agent identities and namespace cursors,
7. prepare final `run.yaml` metadata using `templates/run.yaml`.

If an existing checkpoint for the same run is present, follow `methodology/checkpoint-resume.md` instead of restarting completed work.

Follow the phases under `prompts/` in order.

## Critical rules

- do not modify target application code,
- do not create recovered ADRs or evidence records during discovery,
- keep Discovery notes under the working directory, not final architectural memory,
- enforce an explicit Discovery -> Evidence barrier even in economical mode,
- collect evidence before reconstruction,
- Reconstruction Archaeologist owns Phase 3 synthesis,
- Reconstruction Archaeologist and Architecture Skeptic must be independent roles,
- treat implementation as evidence, not historical explanation,
- distinguish OBSERVED, INFERRED, and UNKNOWN,
- cite concrete repository evidence,
- assign confidence to inferences,
- preserve competing explanations,
- optimize for trustworthy claims rather than consensus,
- never silently rewrite evidence,
- never use superseded evidence as current support,
- allow Skeptics read-only out-of-scope searches when needed to test claims,
- label out-of-scope counterexample evidence explicitly,
- use review verdict taxonomy v2,
- run adversarial review before finalizing.

Write provisional/working state to the configured working directory.

Write finalized architecture memory to the configured output directory.

At Finalization, produce standardized `run.yaml` and `metrics.yaml`.

At the end, summarize:

- analyzed scope,
- agent namespace allocation,
- optional roles used,
- major recovered decisions,
- important constraints,
- high-risk anomalies,
- unresolved questions,
- review verdict distribution,
- low-confidence areas,
- annotated or superseded evidence,
- out-of-scope counterexample evidence used,
- areas not inspected.
