# Execution modes

LARA keeps Discovery and Evidence Collection as separate **methodological phases**.

v0.2 supports two execution modes for how specialist agent contexts cross the Phase 1 → Phase 2 boundary:

- `strict`
- `economical`

The mode changes execution cost and context reuse.

It does **not** change the epistemic rules.

## Why modes exist

A specialist may reacquire the same repository context during both Discovery and Evidence Collection.

The goal of `economical` mode is to reduce repeated context acquisition while preserving the rule:

> Discovery orients. Evidence verifies. Reconstruction synthesizes.

## strict mode

```yaml
execution:
  mode: strict
```

In strict mode:

- Discovery specialist sessions end at the Phase 1 boundary,
- Phase 2 starts fresh specialist sessions,
- the new sessions consume Discovery outputs only as orientation,
- Phase 2 independently inspects primary repository sources before creating evidence.

### Advantages

- strongest context separation,
- lower risk that a Discovery hypothesis is unconsciously promoted into evidence,
- useful for benchmark runs and high-scrutiny validation.

### Costs

- repeated codebase reading,
- higher token/context cost,
- more startup coordination.

## economical mode

```yaml
execution:
  mode: economical
```

In economical mode, the same specialist agent instance/context may continue from Discovery into Evidence Collection.

The phase boundary is still mandatory.

### Economical phase barrier

Before the specialist may create any evidence record:

1. Phase 1 must be explicitly closed by the Lead,
2. Discovery working notes must be persisted,
3. a Phase 1 checkpoint must be written,
4. the Lead must issue an explicit **BEGIN EVIDENCE** transition,
5. the specialist must switch from exploratory language to evidence-verification rules,
6. every evidence observation must still be re-verified against primary repository sources.

Discovery prose is not evidence merely because it remains in context.

### Forbidden behavior

Economical mode must not:

- create evidence IDs during Discovery,
- copy Discovery conclusions directly into evidence without source verification,
- skip G1,
- merge Discovery and Evidence into one undifferentiated output,
- treat retained agent context as proof.

## Agent identity

In economical mode, a continuing specialist keeps the same identity.

Example:

```text
DOM-01 Discovery
   ↓ explicit phase barrier
DOM-01 Evidence
```

The namespace therefore remains stable.

In strict mode, the Lead may either:

- reuse the same logical identity for a fresh session continuing the assigned territory, or
- allocate a new instance identity when it is genuinely a new parallel worker.

The checkpoint must make the choice explicit.

## Recommended use

Use `strict` when:

- comparing LARA accuracy across runs,
- evaluating methodology changes,
- the analyzed area is highly sensitive to confirmation bias,
- cost is secondary to independence.

Use `economical` when:

- repository-reading cost is significant,
- scope is bounded,
- specialist territory is stable,
- the Lead can enforce a hard phase checkpoint.

Every evaluation run should record the chosen mode so cost and quality can be compared across runs.

## Metrics

Every run records:

- execution mode,
- approximate token usage when available,
- wall-clock duration when available,
- interruptions/resumes,
- evidence correction rate,
- review outcome distribution.

The goal is not simply to minimize tokens.

The goal is to reduce repeated work **without weakening evidence discipline**.
