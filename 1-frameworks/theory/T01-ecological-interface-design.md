---
id: T01
title: Ecological Interface Design and the Abstraction Hierarchy
kind: theory
status: adopted
use_when: [designing any diagnostic view, deciding what to show at which level, structuring the platform model]
sources: [vicente1992, vicente2002, vicente1999, rasmussen1983]
---

# Ecological Interface Design (EID)

**Show the structure of the system itself — including *why* each part exists —
so the operator can reason about faults nobody anticipated.**

## What it is

Vicente & Rasmussen's framework for interfaces to complex human–machine
systems `[vicente1992]`. Two goals, held together:

1. **Do not force cognition to a higher level than the task requires.** Routine
   checks should stay perceptual, not become puzzles.
2. **Support all three levels of cognitive control** (`T03`), including the
   effortful knowledge-based reasoning needed for unfamiliar faults.

The distinctive claim: an interface should externalise the **work domain's
constraint structure**, not just the designer's task model. Task-based designs
support anticipated tasks. Constraint-based designs also support the
*unanticipated* ones — which, in fault diagnosis, are the ones that matter.

### The Abstraction Hierarchy

The work domain is modelled at five levels, each a *why/what/how* chain:

| Level | For this platform |
|---|---|
| **Functional purpose** | Deliver reliable inspection data from ATEX Zone 1 without human entry |
| **Abstract function** | Power budget, thermal budget, data flow, time/freshness, information integrity |
| **Generalised function** | Sense → compute → decide → actuate → record → transmit |
| **Physical function** | Intel node, 2× Jetson, CAN bus, LAN, cameras, microphone, drive |
| **Physical form** | Enclosure, connectors, physical placement, indicator LEDs |

Any element can be read *upward* ("why does this exist?") and *downward* ("how
is it achieved?"). An interface that supports both directions lets an engineer
who finds an anomaly at one level trace its meaning at another — which is
exactly what diagnosis is.

### Design principles by control level

- **Skill-based** — make high-level information *directly perceptible* as
  aggregate visual form, so it can be read at a glance rather than computed.
- **Rule-based** — provide consistent one-to-one mappings between system
  constraints and displayed information, so learned cue→action rules stay
  reliable. Consistency is a correctness requirement, not a style preference.
- **Knowledge-based** — give the operator the abstraction hierarchy itself as
  an **external mental model** to reason over when no rule applies.

## Why it matters here

This is the closest thing to a native theory for this product, and the current
docs have arrived at parts of it independently without the underlying model.

`docs/DECISION_LOG.md` D014 ("Platform graph as the primary mental model") and
D015 ("Three disclosure layers") are EID-adjacent. But the graph in
`data/platform-system.yaml` is almost entirely at the **physical function**
level — nodes, buses, containers — with `docs/PLATFORM_SYSTEM_MODEL.md` §6
adding relationship paths at the same level. The abstract-function level, where
budgets and flows live, is largely missing. So is any explicit representation
of functional purpose.

That predicts a specific weakness: the interface will handle *"which component
is faulty"* well and *"is this platform still fit to deploy"* badly — because
the second is an abstract-function question and there is nothing to show.

Two concrete implications:

- **Extend the platform model upward.** Add abstract-function entities (power,
  thermal, data-flow, freshness) as first-class objects in
  `data/platform-system.yaml`, related to the physical objects that realise
  them. This is a documentation change with real design consequences.
- **Make means–ends traversal an interaction.** Selecting any object should
  afford "why does this exist / what depends on it" and "how is it realised."
  `docs/SYSTEM_VISUALIZATION_SPEC.md` covers spatial encoding; it does not
  currently cover this vertical movement.

## How to use it

- As a **checklist on any new view**: which abstraction level is this? Can the
  engineer move up and down from here?
- As **analysis structure** when processing `M04` data: at which level was the
  expert reasoning at each decision point? Level-shifting moments are where
  aiding pays off most.
- As an **argument** for resisting flat metric dashboards —
  `docs/DESIGN_GUIDELINES.md` §18 already forbids them; EID says *why*.

## Caveats

- EID is demanding and has mostly been validated in process control, aviation,
  and network management `[vicente2002]`. Do not over-claim transfer.
- Building a full Work Domain Analysis `[vicente1999]` is a project in itself.
  Use the abstraction hierarchy as a lens; commit to full CWA only if the
  fieldwork shows the design keeps failing on knowledge-based tasks.
- EID complements task analysis; it does not replace it.

## Sources

`[vicente1992]` for the foundations; `[vicente2002]` for a candid progress
review. See `SOURCES.md`.
