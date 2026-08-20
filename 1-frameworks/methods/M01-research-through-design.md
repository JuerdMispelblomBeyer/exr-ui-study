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

Four claim types `[zimmerman2007]`, all four of which you should be able to
answer at the end:

| Criterion | The question it asks |
|---|---|
| **Process** | Could someone else follow how you got here and get comparably useful results? |
| **Invention** | What is genuinely new here, given what already exists? |
| **Relevance** | Why is this preferred state the right one to aim at? |
| **Extensibility** | Can the next person build on this, or does it die with the file? |

Extensibility is the one design projects fail. It is why `M07` exists.

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
