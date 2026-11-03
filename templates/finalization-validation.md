# LARA Finalization Validation

```yaml
gate: G3
status: passed | failed
checked_by: LEAD-01
checked_at: <timestamp or run-relative marker>
blockers: []
warnings: []
```

## G1 — Evidence Revalidation Gate

Status: passed | failed

System map status: evidence-revalidated | provisional

Checked by:

Notes:

## G2 — Review Discovery Verification Gate

Review-discovered items:

| Item | Discovered by | Verification status | Verified by | Verdict |
| --- | --- | --- | --- | --- |
| ANO-XXX | SKEP-01 | reviewed / lead-verified / unverified | SKEP-02 / LEAD-01 / — | ... |

Self-confirmation violations: 0

Notes:

## G3 — Finalization Consistency Gate

### Identity

- [ ] Evidence IDs are unique.
- [ ] Annotation IDs are unique.
- [ ] Namespaced IDs match creators.
- [ ] Architecture-item IDs are unique.

### Evidence lifecycle

- [ ] Evidence lifecycle metadata is complete.
- [ ] Annotated evidence has structured annotations.
- [ ] Superseded evidence points to valid replacement evidence.
- [ ] Final claims do not rely only on superseded evidence.

### System map

- [ ] G1 passed.
- [ ] System map is marked `evidence-revalidated`.
- [ ] Reconstruction-relevant map claims are evidence-backed.
- [ ] Provisional claims are excluded from current architectural truth.

### Architecture provenance and review

- [ ] Every architecture item records provenance.
- [ ] Reconstruction items completed required adversarial review.
- [ ] Review-discovered items satisfy G2.
- [ ] Completed reviews have exactly one v2 verdict.
- [ ] Unverified items remain visibly unverified.

### Run reproducibility

- [ ] `run.yaml` exists.
- [ ] `metrics.yaml` exists.
- [ ] Run IDs match.
- [ ] Target revision matches README, system map, and manifest.
- [ ] Execution mode matches the configured run.
- [ ] Phase and gate outcomes match actual state.
- [ ] Interruptions and resumes are recorded.
- [ ] Artifact counts match final files.
- [ ] Review counts match final review records.
- [ ] Unavailable cost/runtime values are `unknown`, not invented.

### Development navigation

- [ ] `manifest.yaml` exists.
- [ ] Manifest revision matches the analyzed revision.
- [ ] Every architecture item appears exactly once in the manifest item registry.
- [ ] Every manifest artifact path resolves.
- [ ] Confidence and review metadata match authoritative artifacts.
- [ ] Path-index references resolve.
- [ ] Module-index references resolve.
- [ ] Global-item references resolve and are truly cross-cutting.
- [ ] Manifest evidence references resolve.
- [ ] Manifest territories do not broaden evidence-backed scope.
- [ ] Unverified and contradicted items preserve their cautionary state.
- [ ] Unmappable items are surfaced as navigation warnings rather than given invented broad mappings.

### Cross-links

- [ ] Evidence references resolve.
- [ ] Related architecture-item references resolve or are explicitly deferred.
- [ ] Material evidence annotations are reflected by consuming items.
- [ ] Known contradictions remain visible.

### Scope integrity

- [ ] Final scope and exclusions are explicit.
- [ ] Out-of-scope counterexample evidence is labeled.
- [ ] Coverage gaps are explicit.
- [ ] No out-of-scope search is presented as complete analysis.

## Blockers

List every blocking inconsistency.

Use `None` only after completing all checks.

## Warnings

List non-blocking uncertainty that future consumers must see.

Use `None` only after actively checking.

## Gate decision

**PASSED | FAILED**

Reason:
