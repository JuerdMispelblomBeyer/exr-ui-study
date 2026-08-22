---
id: T08
title: Mental Models and Device Understanding
kind: theory
status: adopted
use_when: [what does "full picture" mean, deciding what structure to expose, onboarding, explaining behaviour]
sources: [gentner1983, norman1983, dekleer1981, endsley1995]
---

# Mental Models and Device Understanding

**"A full picture of the internal state" means the engineer can run the machine
in their head: predict what it will do, and explain why it did what it did.
That is the actual design target.**

## What it is

A mental model is an internal model of a system that lets its holder **explain**
and **predict** the system's behaviour `[gentner1983]`. The important
properties, from the classic literature:

- **Runnable.** The useful test is not "can they describe the architecture" but
  "can they simulate it." De Kleer & Brown's analysis of how someone reasons
  about a doorbell is the canonical demonstration: understanding is the ability
  to run the mechanism forward mentally `[dekleer1981]`.
- **Parsimonious and incomplete.** People hold simplified, partial, sometimes
  contradictory models — and this is functional, not a defect. They are not
  trying to hold the schematic.
- **Distinct from the conceptual model.** Norman separates the *target system*,
  the *conceptual model* a designer invents to teach it, and the user's *mental
  model* which is what they actually end up with `[norman1983]`. Your interface
  **is** the conceptual model. Whatever structure it makes visible is what
  engineers will end up believing about the platform — including the wrong
  parts.

Relation to `T02`: a mental model is what makes SA Level 3 (projection)
possible at all. You cannot forecast a system you cannot run.

## Why it matters here

Your goal statement — "help engineers get a full picture of the internal state
of the machine" — is a mental-model goal, and it is worth being precise about,
because two very different designs both satisfy a loose reading of it:

| Reading | Design consequence |
|---|---|
| **"Show all the state"** | Exhaustive readouts. Maximises Level 1 data, degrades comprehension (`T02`), and produces the flat metric dashboard `docs/DESIGN_GUIDELINES.md` §18 already forbids |
| **"Support a runnable model"** | Expose *structure, causality, and constraint* so the engineer can simulate and explain. Fewer values, better arranged |

The second is what you want, and it is a much sharper brief. It also tells you
what to prioritise when space runs out: **relationships over readings.**

Two specific implications:

**Your engineers already have strong mental models — the design job is
alignment, not education.** These are people who know the platform deeply.
Their models were formed from source code, wiring diagrams, ROS graphs, and
past faults. An interface organised around a structure that does not match
their existing model imposes a translation cost on every use. `M02` and `M04`
should explicitly elicit *how they carve the platform up* — that is the IA you
should be building toward, and it may not be the one in
`docs/UX_ARCHITECTURE.md` §5.

**Where the model is wrong is where the interface should intervene.** The
highest-value thing this product can do is not show more; it is correct a
specific, recurring misconception — a dependency people forget, a startup
ordering that is not what it appears, a subsystem that fails in a way its name
does not suggest. `M04`'s novice/expert probes will surface these directly.
Each one is a design opportunity with an evidence trail.

## How to use it

- **Test runnability, not recognition.** In `M10`, ask prediction questions:
  *"if this node dies now, what stops working?"* A participant who can read
  every value but cannot answer that does not have the picture, and your
  interface has not given it to them.
- **Elicit their carving.** Ask engineers to draw the platform before you show
  them anything. Compare the drawings to `data/platform-system.yaml`.
  Divergence is a finding about the IA.
- **Design the conceptual model deliberately.** Decide what simplified story
  the interface tells about the platform, write it down, and check it is
  *true enough* — since it is what people will internalise.
- **Support explanation, not just observation.** "Why is this in this state"
  needs to be answerable in the interface, or the model stays in people's heads
  and dies with them (`T06`).

## Caveats

- Mental models are hard to measure; drawings and predictions are proxies.
  Report them as such.
- Do not confuse a mental model with a persona or a user segment. It is a
  property of a person's understanding of *this machine*, and it changes as
  they learn.
- A simplified conceptual model that is subtly false is worse than a complex
  true one — it produces confident wrong predictions. Compare the procedural
  trap in `T01`.

## Sources

`[gentner1983]` is the foundational collection; `[norman1983]` for the
target/conceptual/mental distinction; `[dekleer1981]` for runnability. **None
read in the original** — see `SOURCES.md`.
