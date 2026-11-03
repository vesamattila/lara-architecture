# Evidence model

LARA treats repository artifacts as evidence with different strengths and failure modes.

The evidence model is governed by:

- `methodology/evidence-lifecycle.md`
- `methodology/id-namespaces.md`

## Evidence sources

Typical sources include:

- production code,
- tests,
- database migrations,
- infrastructure configuration,
- API schemas,
- deployment manifests,
- feature flags,
- dependency configuration,
- comments and TODOs,
- Git history,
- issues and pull requests when available,
- existing documentation and ADRs.

## Evidence record

Each evidence record should contain:

- stable namespaced ID,
- lifecycle status,
- creator and phase provenance,
- observation classification,
- source locations,
- direct observation,
- architectural significance,
- confidence,
- counterevidence,
- caveats,
- related evidence,
- structured annotations when later correction is required.

## Evidence identity

Parallel agents must use deterministic IDs:

```text
E-<ROLE>-<INSTANCE>-<NNN>
```

Example:

```text
E-TEST-01-004
```

IDs are historical identities and are never reused or renumbered.

## Evidence lifecycle

Evidence is append-only after creation.

Allowed states:

- `current`
- `annotated`
- `superseded`

Do not silently rewrite an observation when later evidence changes the conclusion.

Use structured annotations for qualification and replacement evidence plus `superseded_by` when the original record should no longer support current architecture claims.

## Evidence strength

### High

Direct, repeated, behaviorally enforced evidence.

### Medium

Strongly suggested but not fully enforced.

### Low

Plausible interpretation with limited support.

## Source disagreement

When sources conflict, record the conflict.

Do not silently choose one source as truth.

Such conflicts often become anomalies or open questions.

## Evidence created after Phase 2

Later phases may discover new verifiable evidence.

Such records must:

- use the discovering agent's namespace,
- record the actual creation phase,
- explain why the evidence was discovered late,
- participate in the same lifecycle rules as Phase 2 evidence.

Chronologically later evidence is not automatically stronger evidence.
