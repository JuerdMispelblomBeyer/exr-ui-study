---
id: M09
title: Frame Creation and Reframing
kind: method
status: reference
use_when: [the problem as stated is not producing good answers, stakeholder brief feels wrong, stuck]
cost: low as a check, high as a full workshop process
sources: [dorst2015, dorst2011, dorst2001]
---

# Frame Creation and Reframing

**A frame is the proposition: *if we treat this situation as X, then it
follows that…*. Changing X is often more productive than solving harder within
the current X.**

## What it is

Dorst's account of design reasoning `[dorst2011]`: designers work
**abductively**, and specifically they propose a *frame* — a way of looking at
a problem situation — from which working principles and then solutions follow.
Framing is the core creative act, not ideation.

Related: **problem–solution co-evolution** `[dorst2001]`. Designers do not
solve a fixed problem; the problem and the solution develop together, each
reshaping the other. A solution attempt that reveals the problem was
mis-stated is a success, not a detour.

`Frame Innovation` `[dorst2015]` sets out a nine-step process (archaeology,
paradox, context, field, themes, frames, futures, transformation, integration)
for doing this deliberately on stubborn problems. The full process is heavy;
the useful everyday residue is the habit of asking *what are we treating this
as, and what else could it be?*

## Why it fits this project

The project has already reframed once, and it worked. `docs/DECISION_LOG.md`
D021 — "Task-led redesign replaces category-led dashboards" — is a textbook
frame shift: from *this is a monitoring dashboard with categories* to *this is
a task performed on a platform graph*. D014 ("Platform graph as the primary
mental model") is the working principle that followed from it.

That is worth noticing, because it means the productive move in this project
has historically been reframing, not refining. Two frames are still live and
worth testing rather than assuming:

- **Currently framed as** an *introspection* tool — you look at the platform
  and it shows you its state.
- **Could be framed as** a *diagnostic argument* tool — the system proposes
  what it thinks is wrong and shows its evidence, and the engineer's job is to
  confirm or refute it. `T05` (trust and transparency) would then become
  central rather than peripheral.
- **Or as** a *handover* tool — the real user need is transferring
  understanding of a platform's state between people and across time, not any
  single person's live inspection.

Fieldwork (`M03`, `M04`) will indicate which frame the actual work fits. Do not
settle this from the desk.

## How to run it here

The cheap version, as a standing check at the start of each iteration:

1. **Name the current frame** in one sentence: *"We are treating this as…"*
2. **Find the paradox.** Where do the requirements genuinely conflict? A real
   one here: the interface must be trustworthy for safety-adjacent decisions
   (`docs/SAFETY_CONTROLS.md`) while sitting on observability that is
   admittedly partial (`data/platform-system.yaml` `status: partial`). Design
   that treats the paradox as a bug will keep failing.
3. **Propose one alternative frame** and ask what would follow from it.
4. **Test cheaply** — one prototype under the alternative frame (`M06`), rather
   than an argument about it.

Run the full nine-step process only if the project stalls badly.

## What it produces

Frame statements, and their consequences made explicit. Record any frame shift
in `6-log/decisions.md` as a decision — D021 is the model to follow.

## Traps

- **Reframing as procrastination.** At some point you must design under a
  frame. Timebox this.
- **Frames with no consequences.** If nothing about the design changes, it was
  a rewording.
- **Reframing away a real constraint.** Safety classification
  (`docs/SAFETY_CONTROLS.md` §3) is not a frame you can choose out of.

## Sources

`[dorst2011]` is the compact statement; `[dorst2015]` for the full process.
See `SOURCES.md`.
