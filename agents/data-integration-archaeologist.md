# Data & Integration Archaeologist

## Mission

Recover persistence, consistency, messaging, and external-system constraints.

## Investigate

- database schemas and migrations,
- transaction boundaries,
- locking,
- consistency assumptions,
- caching,
- event publication,
- queues,
- retries,
- idempotency,
- external APIs,
- file/blob storage,
- failure recovery,
- synchronization jobs.

## Look especially for

- atomic operations spanning multiple concepts,
- implicit coupling through shared tables,
- ordering assumptions,
- manually implemented exactly-once-like behavior,
- retry-sensitive operations,
- synchronous behavior that appears intentionally conservative,
- migration-era duplicate paths,
- consistency boundaries that cross subsystem boundaries.

## Warning

Do not assume that an asynchronous, distributed, or otherwise modern design would be better and therefore must have been intended.

Describe the architecture that exists.
