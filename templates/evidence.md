# E-<ROLE>-<INSTANCE>-<NNN> — <short observation>

```yaml
id: E-<ROLE>-<INSTANCE>-<NNN>
status: current
created_by: <ROLE>-<INSTANCE>
created_phase: evidence
superseded_by: null
```

## Classification

OBSERVED | INFERRED | UNKNOWN

## Sources

- `path/to/file.ext:line-line`
- related test, migration, commit, issue, PR, or document

## Observation

State exactly what the repository evidence shows.

Avoid causal or historical explanation unless directly evidenced.

This section is append-only after creation.

## Architectural significance

Explain why this observation may matter architecturally.

Clearly mark interpretation as inference when applicable.

## Confidence

High | Medium | Low

## Counterevidence

List known counterexamples or contradictory sources.

Use `None found` only after actively checking.

## Caveats

What limits this evidence?

## Related evidence

- E-<ROLE>-<INSTANCE>-<NNN>

## Annotations

Use this section only when later phases qualify, correct, narrow, contradict, or change confidence in the original record.

Do not rewrite the original Observation.

Example:

```yaml
- id: A-SKEP-01-001
  reason: scope-narrowing
  created_by: SKEP-01
  created_phase: review
  related_evidence:
    - E-SKEP-01-004
```

### A-SKEP-01-001 — <annotation summary>

Explain:

- what changed,
- why,
- which evidence supports the change,
- whether this record remains usable.

When an annotation exists, change the top-level `status` to `annotated`.

When the record is fully replaced, change `status` to `superseded` and set `superseded_by` to the replacement evidence ID.
