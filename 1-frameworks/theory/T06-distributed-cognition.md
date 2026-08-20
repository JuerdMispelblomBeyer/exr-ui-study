---
id: T06
title: Distributed Cognition and Joint Cognitive Systems
kind: theory
status: candidate
use_when: [thinking about handover, multi-person diagnosis, what the tool should remember]
sources: [hutchins1995, hollnagel2005]
---

# Distributed Cognition and Joint Cognitive Systems

**The unit that does the diagnosing is not one engineer. It is the engineer
plus their tools, notes, colleagues, and the record of what happened last
time.**

## What it is

Hutchins' distributed cognition `[hutchins1995]`: cognitive work is carried out
across people, artefacts, and representations, not inside a single head.
Understanding is propagated through representational states — a marked-up
diagram, a log excerpt pasted into a thread, a checklist — and those external
representations are part of the cognitive system, not aids to it.

Hollnagel & Woods' **joint cognitive systems** `[hollnagel2005]` push the same
idea into safety-critical work: analyse the human–machine ensemble as one
system that maintains control, rather than as a person operating a tool. The
design question shifts from *what should the interface display* to *how does
this ensemble stay in control of the situation*.

## Why it matters here

Every current document assumes one engineer, at one workstation, in one
session. `docs/UX_ARCHITECTURE.md` §3 states the viewport assumption and the
single-active-platform assumption; §8 describes a single continuous flow. That
may be right — but it is an assumption nobody has checked, and it is the kind
that quietly determines the whole information architecture.

The distributed reading suggests three things worth testing in fieldwork rather
than assuming:

**Diagnosis is probably a relay, not a session.** A platform returns from site,
one engineer forms a partial hypothesis, another continues the next morning.
If so, the highest-value feature is not a better live view — it is a durable,
transferable representation of *what has been established and what is still
open*. `M09` names this the "handover frame," and it would be a substantially
different product.

**The tool ecology is part of the system.** `M03` will surface the terminals,
dashboards, and threads engineers already use. Designing as though the new
interface is the whole cognitive system, when it is one participant in it, is a
reliable way to build something that gets bypassed.

**Some of the reasoning is already externalised.** Where engineers currently
draw, annotate, paste, or write things down, they are compensating for
something the tooling does not hold. Those workarounds are direct requirement
evidence.

## How to use it

- **Add explicit probes to `M03`/`M04`:** Who else touched this? What did you
  write down, and where did it go? What did you have to reconstruct that
  someone already knew? What did you tell a colleague that the system could
  have told them?
- **Treat the record as a design object.** If diagnosis is distributed over
  time, then annotation, provenance, and "what has already been ruled out"
  become primary interface concerns rather than nice-to-haves.
- **Check the single-user assumption early** and update
  `docs/UX_ARCHITECTURE.md` §3 with an answer instead of an assumption.

## Caveats

- This is a *lens*, not a procedure — it reframes what you look for, it does
  not tell you what to build. Marked `candidate` because it should be adopted
  only if fieldwork shows diagnosis is genuinely distributed here. A small team
  co-located around one workbench may not be.
- Full joint-cognitive-systems analysis is heavy and aimed at control-room
  scale. Take the framing, not the apparatus.

## Sources

`[hutchins1995]` for distributed cognition; `[hollnagel2005]` for the
safety-critical framing. See `SOURCES.md`.
