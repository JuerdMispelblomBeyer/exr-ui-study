---
id: M04
title: Critical Decision Method
kind: method
status: adopted
use_when: [eliciting expert diagnostic reasoning, finding the cues experts use, deriving information requirements]
cost: low–medium — 4–6 interviews of ~90 min plus analysis
sources: [klein1989, hoffman1998, endsley1995]
---

# Critical Decision Method (CDM)

**Pick one hard incident. Walk it four times, each pass deeper. What you are
after is the cue the expert noticed and the novice would not.**

## What it is

A cognitive task analysis interview built on **multiple-pass retrospection of a
single non-routine incident**, guided by cognitive probes `[klein1989]`. It
rests on the naturalistic-decision-making finding that experts do not evaluate
options — they recognise patterns of cues. CDM extracts those cues.

The four passes `[hoffman1998]`:

1. **Incident identification** — get a specific, real, difficult case. Not
   typical: *difficult*. "Tell me about a time you couldn't work out what was
   wrong with a platform."
2. **Timeline construction** — build the incident as an ordered sequence of
   events and decision points. Verify it back with them.
3. **Deepening** — walk the timeline again with probes at each decision point.
4. **"What if"** — counterfactuals that expose expertise: *What would a less
   experienced engineer have done here? What would have had to be different for
   you to have caught this an hour earlier?*

Core probes: **Cues** (what did you see/hear that mattered?) · **Knowledge**
(what did you know that let you read it that way?) · **Analogues** (had you
seen this before?) · **Goals** (what were you trying to achieve right then?) ·
**Options** (what else did you consider, and why did you drop it?) ·
**Experience** (what would a novice have missed?) · **Aiding** (what
information would have helped, and when?).

## Why it fits this project

This is the highest-yield method available for this specific product, and it is
the one I would run first if only one is possible.

The interface being designed is a **diagnostic** instrument. Its entire value
is helping an engineer move from "something is wrong" to "it is the CAN
subsystem, and here is why." CDM is purpose-built to extract exactly that
reasoning from people who already do it well.

It also produces the input that Ecological Interface Design (`T01`) and
Situation Awareness design (`T02`) need: an explicit inventory of **cues**, the
**relationships** between them, and the **projections** experts make. The
"Aiding" probe converts directly into functional requirements with real
provenance — replacing the currently-unsourced entries in
`docs/UI_FUNCTIONAL_REQUIREMENTS.md`.

And it is cheap. Four interviews, no fieldwork logistics, no sensitizing lead
time, no ATEX site access.

## How to run it here

- **4–6 ExRobotics engineers**, one incident each, ~90 min. Mix experience
  levels — the novice/expert delta is where the design opportunity lives.
- **Prime the incident request in advance** so they arrive with a case in mind.
  Ask for one where the answer was not obvious, or where they were wrong first.
- **Let them tell it once, uninterrupted**, before you start structuring. The
  first telling is the story; the value is in passes 2–4.
- **Draw the timeline visibly** and let them correct it. Corrections are data.
- **Push on the Aiding probe.** "At 14:20 you still thought it was the
  network. What would have had to be on screen for you to have doubted that?"
  That sentence is a requirement.
- Record and transcribe (`0-meta/ETHICS.md`); analyse with `M05`.

## What it produces

- A **cue inventory** — the observable signals experts actually key on.
- **Decision points** and what was ambiguous at each.
- **Novice/expert deltas** — what the interface should make visible so a less
  experienced engineer reaches the same conclusion.
- **Timing requirements** — not just *what* information, but *when* it would
  have changed the outcome.
- Concrete **diagnostic scenarios** reusable as evaluation tasks in `M10`.

## Traps

- **Accepting a typical incident.** Routine cases have no decision points and
  teach you nothing. Insist on the hard one.
- **Stopping after pass 2.** The timeline alone is just a story. Depth comes
  from probing each decision point.
- **Taking the rationalised account at face value.** Experts confabulate tidy
  reasoning. The "what would a novice have missed" probe is your check.
- **Leading with your design.** Do not show the Figma file. This runs before,
  not during.

## Sources

`[hoffman1998]` is the best procedural account. `[klein1989]` is the origin.
See `SOURCES.md`.
