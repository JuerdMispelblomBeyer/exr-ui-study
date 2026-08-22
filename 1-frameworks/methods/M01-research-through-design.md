---
id: M01
title: Research through Design
kind: method
status: adopted
use_when: [framing the whole project, justifying the approach, deciding what counts as a result]
cost: structural — shapes everything, costs nothing extra on its own
sources: [stappers2017, zimmerman2007, gaver2012, frayling1993, koskinen2011]
---

# Research through Design

**Designing is the instrument of inquiry, not just the output of it. The
prototype is how you find things out.**

## What it is

Frayling's three-way split `[frayling1993]`:

- **Research *into* design** — studying how designers work. Not this project.
- **Research *for* design** — gathering input to inform a design. Interviews,
  benchmarking, requirements. This project has done a lot of this already.
- **Research *through* design** — the act of designing generates the knowledge.
  Making a thing forces you to confront what you don't know.

Stappers & Giaccardi define RtD as design activity playing a *formative* role
in generating knowledge, through "gaining actionable understanding of a complex
situation, framing and reframing it, and iteratively developing prototypes"
`[stappers2017]`. Making provokes a particular kind of cognition: you cannot
draw the screen without deciding what an engineer needs to see first, and that
decision exposes an assumption you can then go and test.

## Why it fits this project

The existing `docs/` set is almost entirely research *for* design that was
never actually grounded — `docs/UX_ARCHITECTURE.md` §3 lists eight "operating
assumptions to validate," §19 lists open product questions, and
`docs/UI_FUNCTIONAL_REQUIREMENTS.md` §15 lists priority unknowns. Meanwhile the
Figma file already contains screens. That is the RtD situation exactly: the
artefact is ahead of the knowledge, and the artefact is the best tool available
for closing the gap.

The alternative — pause designing, do six weeks of interviews, then resume — is
worse here. Platform-introspection work is hard to talk about in the abstract.
An engineer shown a concrete dependency view will tell you in ninety seconds
what an hour of open questioning would not surface.

## How to run it here

Each cycle:

1. **Frame** — state what you currently believe and what you are unsure of.
   One open question, written down before you design.
2. **Make** — build the smallest Figma artefact that would make you wrong if
   you are wrong. See `M06` for choosing what to build.
3. **Confront** — put it in front of an ExRobotics engineer inside a real
   diagnostic scenario (`M10`). Not "do you like this" — "show me how you'd
   find the fault."
4. **Learn** — what did the artefact teach you that the doc could not? Record
   as an insight, not as a to-do.
5. **Reframe** — update the belief, and the design guidance that depended on
   it. If nothing changed, the artefact was not risky enough.

The cycle is the unit of progress in this project. Tag each one.

## What it produces

Zimmerman, Forlizzi & Evenson's model: the designer integrates **true**
knowledge (models and theories from behavioural science), **how** knowledge
(what is technically possible), and **real** knowledge (what is actually the
case, from fieldwork) in order to make **the right thing** `[zimmerman2007]`.
Through ideating, iterating and critiquing, the problem is continually
reframed. The stated output is *"a concrete problem framing and articulation of
the preferred state, and a series of artifacts — models, prototypes, products,
and documentation of the design process."*

That maps onto this workspace directly, which is why the lanes are shaped as
they are:

| Their term | Where it lives here |
|---|---|
| **true** | `1-frameworks/theory/` |
| **how** | `docs/PLATFORM_SYSTEM_MODEL.md`, `data/platform-system.yaml` |
| **real** | `2-research/` — currently the empty one |
| **the right thing** | `4-design/`, `5-prototypes/` |

### The four criteria

Four lenses for judging the contribution `[zimmerman2007]`:

| Criterion | What it actually requires |
|---|---|
| **Process** | Not reproducible *results* — explicitly not. What is judged is the **rigour applied to the methods** and **the rationale for selecting those methods**, documented in enough detail to be followed. |
| **Invention** | A novel integration of subject matters, situated by **an extensive literature review** showing how it advances the state of the art. Not a refinement of something that already exists. |
| **Relevance** | A shift from *what is true* to *what is real*. You must articulate the **preferred state** the design aims at **and argue why it should be considered preferred**. Work that skips this "appears to be a self-indulgent, personal exploration." |
| **Extensibility** | That others can build on it — either reusing the process, or leveraging the knowledge the artefacts carry. Requires deliberate documentation. |

Extensibility is the one design projects fail. It is why `M07` exists.

## One honest caveat about this project

Zimmerman et al. draw a sharp line between research artefacts and practice
artefacts: in RtD "the intent going into the research is to produce knowledge
for the research and practice communities, not to make a commercially viable
product," and RtD projects are expected to **de-emphasise** commercial framing
`[zimmerman2007]`.

This project does not sit cleanly on that side of the line. It is
industry-internal, and ExRobotics wants a usable interface, not a knowledge
contribution to HCI. That is fine — but it means:

- **The criteria still apply and are still useful.** Process, relevance and
  extensibility are exactly what makes design work survive its author.
- **Invention, in their strict sense, is not the goal.** Do not stretch to
  claim novelty against the literature. The honest claim here is relevance and
  extensibility, evidenced.
- Zimmerman et al. also note why industry design research rarely gets shared:
  it is a competitive advantage. Assume the output stays internal, and design
  the documentation for the **next ExRobotics engineer**, not for a conference.

## Traps

- **Doing RtD and reporting it as research-for-design.** If the prototype
  taught you something, say the prototype taught you it. Don't retro-fit the
  finding to an interview.
- **Prototypes that cannot fail.** A screen that everyone nods at generated no
  knowledge. Build the version that might be rejected.
- **Over-formalising.** Gaver argues RtD produces theory that is "provisional,
  contingent, and aspirational" and warns against standardising the practice
  into something that stifles designing `[gaver2012]`. Hold conclusions
  loosely; state confidence explicitly.
- **Losing the middle versions.** The rejected iteration is evidence. Keep it
  (`M07`, and the tagged snapshots in `6-log/`).

## Positioning this project

Koskinen et al. distinguish three constructive design research settings
`[koskinen2011]`: **Lab** (controlled comparison), **Field** (studying use in
its real context), **Showroom** (the artefact as argument/provocation). This
project is primarily **Field** — real engineers, real robots, real faults —
with occasional Lab moments when comparing two layouts head to head. Say which
one a given study is; the standards of evidence differ.

## Sources

`[stappers2017]` is the anchor — read it first. `[zimmerman2007]` for the four
criteria. `[gaver2012]` for why not to over-systematise. See `SOURCES.md`.
