---
id: M06
title: Prototyping Strategy
kind: method
status: adopted
use_when: [before building any prototype, deciding fidelity, scoping what an iteration tests]
cost: none — it is a decision, not an activity
sources: [houde1997, lim2008, buchenau2000, stappers2017]
---

# Prototyping Strategy

**Decide what the prototype is a question about before you build it. Then build
the smallest thing that asks it.**

## What it is

Three frameworks that together answer "what should I make next?"

**Houde & Hill — what does it prototype?** `[houde1997]` Every prototype sits
somewhere in a triangle:

| Dimension | The question it asks |
|---|---|
| **Role** | What will this do for the user? Where does it fit in their work? |
| **Look and feel** | What is the concrete sensory experience of it? |
| **Implementation** | Can this actually be built and fed with real data? |

Most failed prototypes are failures of declaration: built to test *role*,
critiqued on *look and feel*.

**Lim, Stolterman & Tenenberg — filters and manifestations** `[lim2008]`. A
prototype is a **filter**: it deliberately passes some dimensions of the design
idea and blocks others. It is also a **manifestation**: the medium you choose
shapes what you can think. Their principle — *the best prototype is the minimal
one that makes the possibilities and limitations of a design idea measurable*.
Anything beyond minimal is decoration that will attract the wrong critique.

**Buchenau & Suri — experience prototyping** `[buchenau2000]`. To learn about
an experience you must let someone *have* it, including the context: time
pressure, interruption, ambiguity, consequence.

Stappers & Giaccardi add the RtD reading: the prototype is where theory meets
reality and loses. It embodies your judgement, and confronting it with the
world is the knowledge-generating act `[stappers2017]`.

## Why it fits this project

Prototypes here are Figma. Figma is very good at *look and feel* and structurally
bad at *implementation* — it will render a beautiful dependency graph fed by
data that may not exist. `docs/PLATFORM_SYSTEM_MODEL.md` §8 and
`data/platform-system.yaml` (`status: partial`) both say the platform model is
incomplete. So a Figma prototype in this project **cannot** answer
implementation questions and must never be read as evidence that it can.

That is the single most useful thing this card enforces: state the dimension,
and stop treating a polished screen as proof that the data exists.

## How to run it here

Before building, write three lines into the iteration's `intent.md`:

```
Question:  What am I actually unsure about?
Dimension: role | look-and-feel | implementation  (pick one, primarily)
Falsifier: What would I see that tells me I'm wrong?
```

Then choose the minimum:

| If the question is about… | Build |
|---|---|
| Whether the diagnostic path makes sense | Paper or greyscale wireframe. No tokens, no yellow. |
| Whether an engineer can read the topology | One instrument, real-ish data, no chassis around it |
| Whether density is bearable | One full screen at true 1440 px with realistic value counts |
| Whether the visual identity holds | A composed screen with tokens applied |
| Whether the data can feed it | **Not Figma.** A query against a real platform, or a stubbed YAML extension |

**Withhold the identity layer early.** `docs/DESIGN_GUIDELINES.md` §20 already
requires a colour-independent fidelity gate. Extend the logic to research: a
greyscale prototype gets you feedback about structure; the same screen in
ExRobotics yellow gets you feedback about yellow.

**Simulate the conditions.** An engineer evaluating a fault screen calmly at a
desk is not the condition. Give a scenario from `M04`, a time constraint, and
incomplete information — that is experience prototyping applied here.

## What it produces

Prototypes whose findings are interpretable, because the question was declared
first. Feeds `5-prototypes/` and, via `M07`, the annotated portfolio.

## Traps

- **Fidelity creep.** Polishing past the minimum costs time and biases the
  critique toward surface.
- **One prototype, many questions.** It will answer none cleanly. Split it.
- **Confusing "they liked it" with a result.** Liking is not a dimension.
- **Discarding rejected versions.** They are the comparison set `M07` needs.

## Sources

`[houde1997]`, `[lim2008]`, `[buchenau2000]`. See `SOURCES.md`.
