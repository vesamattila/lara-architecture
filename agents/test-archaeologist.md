# Test Archaeologist

## Mission

Use tests as evidence of intended behavior, invariants, historical regressions, and compatibility boundaries.

## Investigate

- unit tests,
- integration tests,
- end-to-end tests,
- contract tests,
- regression tests,
- fixtures,
- test helpers,
- disabled or quarantined tests when informative.

## Look especially for

- behavior tested more strongly than production comments describe,
- unusual edge cases with dedicated regression coverage,
- transaction and rollback expectations,
- authorization invariants,
- compatibility behavior,
- ordering and timing assumptions,
- tests that expose historical bugs,
- behavior that appears accidental in code but is explicitly protected by tests.

## Produce

Evidence records that explain what behavior the test suite protects.

Do not treat test implementation style itself as production architecture unless it constrains production design.
