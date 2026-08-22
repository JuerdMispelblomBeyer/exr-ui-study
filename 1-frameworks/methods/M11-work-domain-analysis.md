---
id: M11
title: Work Domain Analysis (and the rest of CWA)
kind: method
status: adopted
use_when: [building the abstraction hierarchy T01 requires, structuring the platform model, deciding what the interface must represent]
cost: medium — 1–2 weeks for a first-pass ADS, longer to validate
sources: [vicente1999, lintern-cwa, inl-wda, vicente1992, naikar2006]
---

# Work Domain Analysis

**`T01` says the interface should externalise the work domain's constraint
structure. This is how you actually build that structure. It is the single
biggest analytical gap in the project right now.**

## What it is

Cognitive Work Analysis is a five-stage framework `[vicente1999]`. Each stage
has a named output artefact, which is what makes it usable rather than
philosophical `[lintern-cwa]`:

| Stage | Question | Artefact |
|---|---|---|
| **1. Work domain analysis** | What are the activity-independent constraints? | **Abstraction–decomposition space (ADS)** |
| **2. Work organisation** | Which tasks arise, in which situations? | **Contextual activity matrix** (work task docket) |
| **3. Work/control task analysis** | What cognitive states and transitions does a task involve? | **Decision ladder** |
| **4. Cognitive strategies** | What different routes could achieve the same thing? | Strategy set per process |
| **5. Social organisation & competencies** | Who does what, at which SRK level? | Allocation across actors |

You do not need all five. Stages 1 and 2 carry most of the value here.

### Stage 1 — the abstraction–decomposition space

A two-dimensional matrix. Vertically, five levels of **abstraction**; each cell
is a complete description of the whole system in a different language. Lintern
names the levels *system purpose, domain values, domain functions, technical
functions, physical objects*; Rasmussen's original naming is *functional
purpose, abstract function, generalised function, physical function, physical
form*. Same ladder.

Horizontally, **decomposition** — whole to part. Crucially, decomposition is
performed independently at each level of abstraction; you are not just zooming
in.

The defining property: it is **activity-independent**. You describe what the
domain *is and can do*, not what anyone does with it. That is what makes it
support unanticipated faults — the ones a task analysis never enumerated.

### Stage 2 — work situations

Work does not happen in one undifferentiated context. A process plant has
startup, routine operation, shutdown, maintenance, emergency `[lintern-cwa]`.
The contextual activity matrix maps which tasks are live in which situation
`[naikar2006]`.

## Why it fits this project

**Stage 1 fills the specific hole `T01` identified.** `data/platform-system.yaml`
is a decomposition at essentially one abstraction level — physical function.
There is no abstract-function row, so questions of the form "is this platform
fit to deploy" have nothing to render. WDA is the procedure that produces the
missing rows, and its output is directly a data-model change:
`data/platform-system.yaml` gains entities like *power budget*, *thermal
budget*, *data flow integrity*, *observation freshness*, each related to the
physical objects that realise it.

**Stage 2 may be the more important finding.** The current docs assume one
continuous flow (`docs/UX_ARCHITECTURE.md` §8). But this platform plausibly has
several genuinely different work situations:

> pre-deployment check · autonomous run in progress · returned from site ·
> active fault investigation · post-repair verification · software or
> firmware update

If the task sets differ across those — and they almost certainly do — then
"good flow" does not mean one excellent flow. It means the interface fits each
situation, and the contextual activity matrix is what tells you where they
diverge. This is a cheap analysis with a potentially large structural payoff.

## How to run it here

Do a **first-pass ADS from existing material in a day**, then correct it with
engineers rather than trying to get it right alone.

1. **Write the functional purpose in one sentence.** Not the interface's
   purpose — the *platform's*. Something near: *deliver reliable inspection
   data from hazardous areas without human entry.* Everything hangs off this,
   so get it agreed with ExRobotics.
2. **Fill the physical rows from what exists** — `data/platform-system.yaml`
   and `docs/PLATFORM_SYSTEM_MODEL.md` already cover these well.
3. **Work upward, which is the hard and valuable part.** For each physical
   object ask *why does this exist?* until you reach purpose. The recurring
   answers are your abstract functions. Expect: energy, thermal, data flow,
   time/freshness, information integrity, mobility, communication.
4. **Check both directions.** Every cell should read upward as *why* and
   downward as *how*. Gaps in the middle rows are usually real gaps in
   observability, and worth noting as findings.
5. **Validate with engineers.** A whiteboard walk of the ADS is a good use of
   30 minutes at the end of an `M03` or `M04` session. Ask what is wrong.
6. **Then stage 2:** list work situations, and for each, the tasks that are
   live. A one-page matrix.

Defer stages 3–5 unless a specific question demands them. Decision ladders are
detailed and slow; `M04` timelines give you much of the same insight faster.

## What it produces

An ADS and a contextual activity matrix — both feeding `4-design/system/` and
directly amending `data/platform-system.yaml`. Also, reliably, a list of things
the platform cannot currently observe, which is requirements evidence.

## Traps

- **Sliding into task analysis.** If a cell describes what someone *does*, it
  belongs in stage 2. Stage 1 describes the domain, not the work.
- **Confusing decomposition with abstraction.** "Jetson → CPU → core" is
  decomposition at one level. Moving up means changing the *language*, from
  components to functions to purposes.
- **Perfectionism.** A validated ADS is a research project in itself
  `[inl-wda]`. A rough one that engineers have corrected beats an elegant one
  you built alone.
- **Treating it as documentation.** Its value is the design consequences it
  forces. If the ADS does not change a screen, you filed it instead of using
  it.

## Sources

`[lintern-cwa]` is a compact practical tutorial and **read in the original** —
start there. `[inl-wda]` is a long applied methodology report, also obtained.
`[vicente1999]` is the canonical book, not obtained. See `SOURCES.md`.
