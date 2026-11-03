# Architectural Memory

Generated using LARA — Legacy Architecture Reconstruction & Archaeology.

## Analysis scope

Target repository:
Revision analyzed:
Date:
Focus areas:

### Included

- ...

### Excluded

- ...

## Run metadata

Execution metadata: `run.yaml`

Comparable run metrics: `metrics.yaml`

Development navigation: `manifest.yaml`

Validation audit trail: `validation.md`

## Validation status

G1 — Evidence Revalidation Gate: PASSED | FAILED

G2 — Review Discovery Verification Gate: PASSED | FAILED | NOT APPLICABLE

G3 — Finalization Consistency Gate: PASSED | FAILED

Link to the finalization validation report.

## Finalization warnings

List every non-blocking G3 warning future consumers should see.

Examples include low-confidence areas, stale operational evidence, unresolved review challenges, production-only unknowns, or significant coverage gaps.

Use `None` only when G3 recorded no warnings.

## Coverage

Summarize what was inspected and what remains outside the investigation.

## Development navigation

Machine-readable index: `manifest.yaml`

Use the manifest to map changed paths or modules to relevant architecture items.

Important:

- the manifest is navigation metadata, not authoritative architectural truth,
- always read the referenced Markdown artifact before relying on an item,
- path misses do not prove that no architecture applies,
- `global_items` must always be considered,
- unverified or contradicted items retain their cautionary review state.

### Navigation coverage gaps

List items or areas that could not be mapped safely to stable paths/modules.

These are G3 warnings, not reasons to invent broad mappings.

## System overview

Link to `system-map.md` and summarize the major architectural boundaries.

## Recovered decisions

| ID | Decision | Confidence | Review |
| --- | --- | --- | --- |
| ADR-RXXX | ... | High / Medium / Low | CONFIRMED / STRENGTHENED / ... |

## Constraints

| ID | Constraint | Confidence | Review |
| --- | --- | --- | --- |
| CON-XXX | ... | High / Medium / Low | CONFIRMED / STRENGTHENED / ... |

## Architectural anomalies

| ID | Anomaly | Confidence | Review |
| --- | --- | --- | --- |
| ANO-XXX | ... | High / Medium / Low | CONFIRMED / NARROWED / ... |

## Open questions

| ID | Question |
| --- | --- |
| AQ-XXX | ... |

## Low-confidence areas

Call out architectural areas where the available evidence is incomplete, contradictory, or weak.

## Using this memory during development

Before changing the system, use `prompts/use-architecture-memory.md` from LARA.

A change plan should identify:

- PRESERVED
- AFFECTED
- SUPERSEDED
- RISKS

## Unverified items

List review-discovered items retained with `review_status: unverified`.

These are not settled architectural truth.

## Evidence caveat

This architecture memory is a reconstruction from available evidence.

Recovered decisions are not proof of undocumented historical rationale.

When current implementation contradicts this memory, the contradiction must be investigated rather than hidden.
