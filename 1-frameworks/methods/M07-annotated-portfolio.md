---
id: M07
title: Annotated Portfolio
kind: method
status: adopted
use_when: [recording iterations, making in-between versions count as knowledge, final handover]
cost: low — ~30 min per iteration, if done at the time
sources: [gaver2012ap, lowgren2013, hook2012, gaver2012, dalsgaard2012]
---

# Annotated Portfolio

**A set of designs, side by side, with short annotations naming the dimensions
along which they differ. This is how a folder of versions becomes knowledge.**

## What it is

Gaver & Bowers' proposal for communicating design research without forcing it
into theory `[gaver2012ap]`. You select a collection of related designs,
represent them in a suitable medium, and attach **brief textual annotations**
that name what varies across them.

The annotations do the work. They sit deliberately between the artefact (too
particular to transfer) and theory (too abstract to guide making) — what Löwgren
calls **intermediate-level knowledge** `[lowgren2013]`, alongside strong
concepts `[hook2012]` and patterns. See `T04`.

Gaver's argument for this over theory-building: RtD produces knowledge that is
"provisional, contingent, and aspirational," and portfolios of related pieces
are a more honest carrier for it than premature generalisation `[gaver2012]`.

## Why it fits this project

You explicitly asked for progress tracking *including in-between versions*.
This is the method that makes those versions pay off rather than accumulate.

Concretely: the current Figma file contains `Style Direction · Signal
Instrumentation` (`36:56`), which `README.md` already describes as predating a
stricter identity revision — a superseded version being kept because someone
sensed it was worth keeping. Nothing says *what changed and why*, so the
knowledge in that comparison is currently inaccessible. That is the exact gap
an annotated portfolio closes.

It also directly answers the **extensibility** criterion in `M01` — the one
design projects usually fail. And at handover it gives ExRobotics something far
more useful than a final file: the reasoning, in a form they can apply to
screens you never drew.

## How to run it here

At the close of every iteration, ~30 minutes:

1. **Capture** the state — screenshot every materially changed screen. Commit
   under `5-prototypes/P0n/`, and tag the repo (`6-log/iterations.md`).
2. **Annotate**, 3–6 short lines. Each names a *dimension of variation*, not a
   changelog entry:

   > *Density:* single scrollable field, no tabs — tests whether an engineer
   > will accept ~40 values on one screen rather than paying navigation cost.
   >
   > *Causality:* dependency path is always visible, not disclosed on demand —
   > against P01, which hid it behind selection.
   >
   > *Colour:* greyscale only. Structure is being tested, not identity.

3. **Compare explicitly.** An annotation that does not reference another
   version in the portfolio is a note, not an annotation. "Against P01…" is the
   move that generates knowledge.
4. **Keep the rejects.** A portfolio of only successes has no contrast and
   therefore no dimensions.

Promote a recurring dimension that proves generative into `4-design/` as a rule,
and log it in `6-log/decisions.md`. That is the escalation path from
observation → intermediate-level knowledge → project canon.

## What it produces

- A navigable visual history where each step states what it was testing.
- Named dimensions of the design space — the transferable output.
- Candidate **strong concepts** (`T04`) once a dimension recurs across several
  iterations and holds up.
- The handover artefact.

## Traps

- **Annotating retrospectively.** Six weeks later you will write a changelog,
  not an annotation, because the alternatives you rejected are gone from memory.
  Do it at the time.
- **Describing instead of differentiating.** "Added a topology panel" is a
  changelog. "Topology always visible, against P01's on-demand" is an
  annotation.
- **Too many dimensions.** Three to six per iteration. More means you changed
  too much at once and cannot attribute anything.
- **Screenshots without annotation.** That is just a folder.

## Sources

`[gaver2012ap]` is the original; `[lowgren2013]` situates it among other
intermediate-level forms; `[dalsgaard2012]` on reflective documentation. See
`SOURCES.md`.
