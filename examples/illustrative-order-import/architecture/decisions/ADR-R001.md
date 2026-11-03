# ADR-R001 — Use `order_id` as the sequential materialization key

```yaml
provenance:
  discovered_during: reconstruction
  discovered_by: RECON-01
  source_item: null
review_status: reviewed
reviewed_by: SKEP-01
```

- Status: Recovered
- Decision confidence: Medium
- Rationale confidence: Unknown

## Recovered decision

Within the demonstrated sequential, single-process path, use `order_id` as the filename key and treat an existing output file as an already materialized order.

## Evidence

- E-TEST-01-001

## Observed context

The synthetic importer derives one JSON destination from `order_id`, checks whether it exists, and skips the write when it does. The test demonstrates two sequential calls in one process.

## Original rationale

**Unknown.** No history or design record exists for this synthetic fixture.

## Current consequences

Sequential re-imports with the same identifier preserve the first payload. Identifier collisions also suppress later payloads, even if their other fields differ.

## Competing interpretations

- The behavior could model intentional idempotency.
- It could instead be a minimal overwrite guard with no broader architectural intent.

## Change implications

Code relying on sequential duplicate suppression should not silently change to overwrite existing output. Parallelism or multiple identity namespaces require a new decision because this fixture provides no atomicity or namespace evidence.

## Affected territory

Paths:

- `source/import_orders.py`
- `tests/test_import_orders.py`

Modules:

- `illustrative-order-import`

Cross-cutting: false

## Related items

- AQ-001

## Adversarial review

- Review status: reviewed
- Verdict: NARROWED
- Reviewer: SKEP-01
- Reviewer notes: The core sequential behavior stands, but the initial candidate claim was narrowed because neither concurrency safety nor global identifier uniqueness is evidenced. See `architecture/reviews/ADR-R001-review.md`.
