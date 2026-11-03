# Confidence model

Confidence describes how strongly the available evidence supports an architectural claim.

It does **not** describe how reasonable or elegant the claim sounds.

## High confidence

Use when multiple independent evidence sources agree, behavior is enforced, counterexamples were actively searched for, and scope is clearly bounded.

## Medium confidence

Use when evidence is consistent but incomplete, the claim relies on repeated patterns, or plausible alternatives remain.

## Low confidence

Use when evidence is sparse, important areas remain uninspected, or competing explanations are equally plausible.

## Confidence can differ by statement

A recovered ADR may have:

- high confidence that a decision currently exists,
- low confidence about its original rationale.

Do not collapse these into one misleading certainty.

## Downgrading confidence

Adversarial review should downgrade confidence when a counterexample is found, scope is narrower than first believed, or an alternative explanation fits equally well.

Prefer a narrower high-confidence statement to a broad low-evidence claim.
