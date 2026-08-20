---
id: M08
title: Interaction Vision
kind: method
status: candidate
use_when: [setting a qualitative target for how the interface should feel, resolving style arguments, briefing yourself]
cost: low — a day, plus the research it rests on
sources: [hekkert2011, pasman2011, ei-course, vanboeijen2020]
---

# Interaction Vision

**A short, deliberately non-literal statement of the *quality* of interaction
you are designing for. Not what the interface shows — how it behaves toward
the person using it.**

## What it is

The signature move of TU Delft's Design for Interaction programme. In the
`ID4250 Exploring Interactions` sequence, students formulate a design goal,
analyse current interactions, **develop an interaction vision**, generate
starting points, then develop and test concepts `[ei-course]`.

The vision is a few carefully chosen words — typically an adjective/adverb
phrase, often carried by a metaphor from outside the product domain
`[pasman2011]`. The metaphor is the point: "like a *good diagnostic
conversation*" or "like *a well-lit workshop*" is generative in a way that
"clear and efficient" is not, because the first has properties you can keep
interrogating and the second is just approval.

It descends from ViP `[hekkert2011]`, where you deliberately choose context
factors, build them into a **leitmotiv**, and design the *interaction* before
the product — because the appropriateness of an interaction is determined by
the context it is designed for, not by the artefact.

The vision is then made concrete through **storyboards of the intended
interaction** — a sequence showing the interaction quality in use, before any
UI is designed.

## Why it fits this project

This project has a strong *visual* direction — "Signal Instrumentation," fully
specified across `docs/DESIGN_GUIDELINES.md` — and no stated *interaction*
quality. Every existing rule describes how the interface should look and how
it is composed. None says how it should behave toward an engineer who is
stuck, wrong, or under time pressure.

That gap has consequences. `docs/DECISION_LOG.md` D017 ("Overview prioritizes
causality and freshness") and D020 ("Stable visual topology precedes text
summaries") are both really interaction-quality decisions, argued as layout
decisions. An interaction vision would give them a shared parent and make the
next such call fall out rather than need re-litigating.

It is also the natural home for a genuine tension in this product: the
interface must be **calm** enough for routine introspection and **urgent**
enough for a latched safety state (`docs/SAFETY_CONTROLS.md` D022, Drive
Stall). A single vision that holds both is worth the day it takes to write.

## How to run it here

Do this **after** `M03`/`M04`, not before — a vision invented from the armchair
is just a slogan. The DfI ordering is deliberate.

1. **Analyse current interaction.** From the fieldwork: how does diagnosis feel
   *now*? Likely candidates from the existing docs — fragmented, distrustful,
   reconstructive, tab-heavy. Name it honestly.
2. **Choose context factors.** What is true about this situation that should
   drive the design? ATEX Zone 1 deployment, high consequence of a wrong call,
   partial and stale observability, engineers who already hold a deep mental
   model of the platform.
3. **Write the vision.** One phrase, plus a metaphor from elsewhere. Test it:
   does it *exclude* anything? A vision that forbids nothing is decoration.
4. **Storyboard it.** Six to eight frames of an engineer diagnosing a real
   `M04` incident under the intended quality. Still no UI.
5. **Derive starting points** — concrete interaction properties the design must
   have — and carry them into `4-design/` as first-class rules.

## What it produces

A stated interaction quality, a storyboard, and a set of starting points. In
this workspace it becomes the parent decision that D017/D020 and their
successors hang from.

## Traps

- **Adjectives that nobody would oppose.** "Intuitive, clear, powerful" is not
  a vision. If the opposite is absurd, the statement is empty.
- **A metaphor you then take literally.** The vision guides the quality of
  interaction; it does not mean the UI should look like a workshop.
- **Writing it before the research.** Then it encodes your assumptions, which
  is precisely what this project already has too much of.
- **Filing it and never using it.** Its job is to settle later arguments. Cite
  it in decisions or it is dead weight.

## Sources

`[hekkert2011]` for ViP; `[pasman2011]` on expressing interaction qualities;
`[ei-course]` for the DfI sequence; `[vanboeijen2020]` has a two-pager. See
`SOURCES.md`.
