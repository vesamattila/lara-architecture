# Run metadata and metrics

Every LARA run should be comparable with later runs without exposing proprietary repository content.

v0.2 standardizes two final machine-readable files:

```text
docs/architecture/run.yaml
docs/architecture/metrics.yaml
```

## run.yaml

`run.yaml` describes how the archaeology was executed.

Use `templates/run.yaml`.

Record:

- run ID,
- target revision,
- date/time when available,
- configured scope reference,
- execution mode,
- agents and roles,
- optional specialists,
- model/runtime identifiers when available,
- orchestration mode,
- phase completion,
- gate outcomes,
- interruptions and resumes.

Do not invent unavailable runtime metadata.

Use `unknown` when necessary.

## metrics.yaml

`metrics.yaml` records comparable results.

Use `templates/metrics.yaml`.

### Artifact counts

Count final artifacts:

- evidence,
- recovered ADRs,
- constraints,
- anomalies,
- open questions.

Evidence counts should also separate:

- current,
- annotated,
- superseded.

### Review counts

Count canonical v2 verdicts:

- confirmed,
- strengthened,
- narrowed,
- reclassified,
- confidence downgraded,
- contradicted,
- unresolved challenge.

Also count:

- review-discovered items,
- independently reviewed review-discovered items,
- Lead-verified items,
- unverified items.

### Quality assessments

Use:

- `low`
- `medium`
- `high`

for:

- evidence traceability,
- inference discipline,
- rationale hallucination risk,
- adversarial effectiveness,
- output usability,
- duplication level,
- navigation coverage.

These are run-level assessments, not objective scientific measurements.

The post-run report should explain the basis for each assessment.

### Cost

Record only what the runtime makes available.

Fields:

- approximate tokens,
- wall-clock duration,
- agent/session count.

If token usage is unavailable:

```yaml
approximate_tokens: unknown
```

Do not estimate token counts from prose length unless the runtime explicitly provides a defensible figure.

### Correction metrics

Record when practical:

- evidence records annotated,
- evidence records superseded,
- review items that materially changed during skepticism.

These help measure whether adversarial review is actually doing work.

### Navigation metrics

Record:

- architecture items with path mappings,
- items with module-only mappings,
- cross-cutting global items,
- items with navigation coverage warnings.

Do not inflate path coverage with unjustified broad globs.

## Comparability rule

Metrics are meaningful only when run metadata preserves differences such as:

- strict vs economical execution,
- scope size,
- optional specialist use,
- target revision,
- model/runtime differences.

Do not compare raw token counts across runs without those qualifiers.

## Sanitized reporting

A sanitized external evaluation report may report these metrics without:

- repository names,
- company names,
- proprietary identifiers,
- concrete paths,
- business-domain details.

This allows methodology evaluation without exporting target-system details.
