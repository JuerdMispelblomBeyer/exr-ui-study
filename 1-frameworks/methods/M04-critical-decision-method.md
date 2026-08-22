---
id: M04
title: Critical Decision Method
kind: method
status: adopted
use_when: [eliciting expert diagnostic reasoning, finding the cues experts use, deriving information requirements]
cost: low–medium — 4–6 interviews of ~90 min plus analysis
sources: [klein1989, hoffman1998, cdm-eng2021, endsley1995]
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
  Remote video calls are fine and are how the published engineering-domain
  application ran it `[cdm-eng2021]`.
- **Have them bring the actual material, and get it in advance.** Make it a
  recruitment criterion: they have access to the logs, tickets, screenshots or
  notes from that incident, and are willing to walk through them. Then read it
  *before* the interview. The engineering-domain team's main stated regret was
  requesting only enough material to screen participants, and then having to
  understand unfamiliar cases live — a mental load they say they
  underestimated. You will be in the same position with ROS 2 graphs and CAN
  traces you did not debug.
- **Screen-capture the walkthrough**, with consent. The artefacts they open,
  and the order they open them in, are data.
- **Let them tell it once, uninterrupted**, before you start structuring. The
  first telling is the story; the value is in passes 2–4.
- **Walk their own material in sequential order** on pass 2 rather than
  reconstructing from memory. This is also the standard answer to the standard
  critique of retrospective methods — memory degradation — because the files
  carry the recollection.
- **Draw the timeline visibly** and let them correct it. Corrections are data.
- **Verify the timeline back with them**, in-session or as a short follow-up.
  The engineering-domain team flags skipping this as their second regret.
- **Push on the Aiding probe.** "At 14:20 you still thought it was the
  network. What would have had to be on screen for you to have doubted that?"
  That sentence is a requirement.
- Record and transcribe (`0-meta/ETHICS.md`); analyse with `M05`.

## What it produces

CDM has two named output artefacts. Build both — they are the deliverable, not
the transcript.

1. **A situation-assessment timeline** — the incident as a series of decision
   points, each annotated with the *goals*, *cues*, *knowledge*, *experience*
   and *actions* in play at that moment.
2. **A decision requirement table** — per decision point: what was decided,
   *how* it was decided, **why it was difficult**, and what supporting
   information was used. The "why difficult" column is where interface
   requirements come from.

Plus, across participants: a **cue inventory** (the observable signals experts
key on), **novice/expert deltas**, **timing requirements** (not just *what*
information but *when* it would have changed the outcome), and concrete
**diagnostic scenarios** reusable as evaluation tasks in `M10`.

One framing worth carrying into design: the goals and expectations extracted at
each decision point tell you what engineers want **to do**, not what they want
**to see**. `docs/UI_FUNCTIONAL_REQUIREMENTS.md` is currently written almost
entirely in "expose X" form. This is the method that converts it.

## Traps

- **Accepting a typical incident.** Routine cases have no decision points and
  teach you nothing. Insist on the hard one.
- **Stopping after pass 2.** The timeline alone is just a story. Depth comes
  from probing each decision point.
- **Taking the rationalised account at face value.** Experts confabulate tidy
  reasoning. The "what would a novice have missed" probe is your check.
- **Leading with your design.** Do not show the Figma file. This runs before,
  not during.
- **Solo analysis.** The published applications have two or three analysts code
  independently and then reconcile. You are one person. Mitigate by verifying
  timelines with participants (above) and by writing your reading down before
  you look at the next transcript, so later cases cannot quietly reshape
  earlier ones.

## Sources

`[klein1989]` is the origin; `[hoffman1998]` the standard procedural account —
**both are paywalled and neither has been read in the original.** The
procedural detail above comes from `[cdm-eng2021]`, an open applied study that
follows Hoffman et al. in an engineering-design domain, which is close to this
one. Obtain `[hoffman1998]` before relying on this card for anything load-
bearing. See `SOURCES.md`.
