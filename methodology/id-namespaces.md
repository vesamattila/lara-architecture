# ID namespaces

LARA assigns deterministic namespaces before parallel work begins.

The goal is to let agents create artifacts independently without coordinating every identifier through the Lead.

## Agent instance identity

Each agent instance receives:

```text
<ROLE>-<INSTANCE>
```

Examples:

```text
ARCH-01
DOM-01
DATA-01
TEST-01
HIST-01
SKEP-01
SKEP-02
```

Instance numbers are two digits and start at `01` within each role.

## Reserved role codes

| Role | Code |
| --- | --- |
| Lead Archaeologist | `LEAD` |
| Architecture Cartographer | `ARCH` |
| Domain Archaeologist | `DOM` |
| Data & Integration Archaeologist | `DATA` |
| Test Archaeologist | `TEST` |
| History Archaeologist | `HIST` |
| Reconstruction Archaeologist | `RECON` |
| Architecture Skeptic | `SKEP` |
| Operations & Deployment Archaeologist | `OPS` |

`RECON` and `OPS` are reserved even when a run does not use those roles.

Custom specialist roles must receive a unique uppercase code before the run starts.

## Evidence IDs

Evidence IDs use:

```text
E-<ROLE>-<INSTANCE>-<NNN>
```

Examples:

```text
E-ARCH-01-001
E-DOM-01-004
E-TEST-02-011
E-SKEP-01-003
```

Rules:

- `NNN` is a three-digit sequence local to that agent instance,
- each instance starts at `001`,
- IDs are never renumbered,
- deleted or abandoned numbers are not reused,
- the creator owns its namespace for the duration of the run.

This makes parallel creation collision-free without a central counter.

## Annotation IDs

Evidence annotations use:

```text
A-<ROLE>-<INSTANCE>-<NNN>
```

Examples:

```text
A-SKEP-01-001
A-LEAD-01-002
```

Annotation numbering is independent from evidence numbering.

## Architecture-item IDs

Architecture items remain globally numbered after evidence collection:

```text
ADR-R001
CON-001
ANO-001
AQ-001
```

These IDs are assigned during Reconstruction because architecture items are synthesis artifacts rather than independent specialist observations.

Once assigned, architecture-item IDs are never renumbered.

If an item is later reclassified, preserve its original ID and record the reclassification in provenance/review metadata rather than silently creating a new history.

## Lead responsibilities before Phase 1

The Lead must publish the run's agent allocation before parallel work begins.

Example:

```yaml
agents:
  lead:
    - LEAD-01
  discovery:
    - ARCH-01
    - DOM-01
    - DATA-01
    - TEST-01
    - HIST-01
  review:
    - SKEP-01
    - SKEP-02
    - SKEP-03
```

If an agent is restarted as a continuation of the same assigned work, it keeps the same instance identity and resumes the next unused local number.

If a genuinely new parallel instance is created, assign the next instance number.

## Cross-agent references

Agents may reference artifacts from another namespace but must never create IDs in that namespace.

For example:

- `TEST-01` may reference `E-DOM-01-004`,
- `TEST-01` must not create `E-DOM-01-005`.

## Late evidence

Evidence discovered during Reconstruction, Review, or Finalization uses the namespace of the agent that observed and verified it.

Examples:

```text
E-RECON-01-001
E-SKEP-02-006
E-LEAD-01-001
```

The artifact's `created_phase` records when it entered the evidence base.

## Stability rule

IDs identify historical artifacts, not current truth.

When evidence changes:

- annotate it,
- supersede it,
- or create replacement evidence.

Never reuse the old ID for a rewritten claim.
