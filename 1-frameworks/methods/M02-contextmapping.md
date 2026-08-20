---
id: M02
title: Contextmapping
kind: method
status: candidate
use_when: [understanding how engineers experience diagnostic work, surfacing tacit and latent needs, front-end framing]
cost: high — 2–4 weeks including sensitizing, sessions, and analysis
sources: [sleeswijk2005, sanders2012, sleeswijk2009]
---

# Contextmapping

**Give people a week to notice their own practice before you ask them about
it. Then have them make something rather than answer questions.**

## What it is

The TU Delft generative-research method `[sleeswijk2005]`. Its premise: people
are not reliable reporters of their own routine work. Ask an engineer "how do
you diagnose a robot" and you get the tidy version. Contextmapping gets past
that with two moves:

1. **Sensitizing** — participants receive a small booklet or set of tasks days
   before the session. They observe and record their own practice: annotate a
   fault they hit, photograph their screen setup, log what they checked and in
   what order. This primes memory and shifts them from answering to noticing.
2. **Generative session** — participants *make* something (a collage, a map, a
   timeline) using a provided toolkit, then explain it. The artefact is a
   vehicle for talking, not a deliverable.

Sanders & Stappers call the underlying structure the **path of expression**:
four steps from **facts** → **feelings** → **memories** → **values**
`[sanders2012]`. Present first, past second, future last — you can only design
for what someone aspires to once they have retrieved what they have lived.

Three levels of knowledge come out, and only contextmapping reliably reaches
the third: what people **say** (explicit), what they **do** (observable), and
what they **dream or know tacitly** (latent).

## Why it fits this project

The unknowns in `docs/UI_FUNCTIONAL_REQUIREMENTS.md` §15 and
`docs/UX_ARCHITECTURE.md` §19 are mostly latent-level: not "which metric do you
want" but "what does it feel like when a robot comes back and you cannot tell
whether the CAN bus or the Jetson is at fault." That is a memory-and-values
question, not a feature question.

It is also the method your own faculty is known for, and the one the current
docs most conspicuously lack.

## How to run it here

- **Recruit 4–6 ExRobotics engineers** who actually diagnose returned or
  misbehaving platforms. Small n is correct — this is depth, not incidence.
- **Sensitizing booklet, 5–7 days.** Daily prompts: *Draw where you looked
  first today. What did you have open at once? Where did you get stuck? What
  did you wish the system had just told you?* Keep it to five minutes a day.
- **Sessions of 2–4 people, ~2 hours.** Toolkit: blank platform-topology cards
  (compute nodes, CAN, ROS 2 nodes, cameras, network), timeline strips,
  friction stickers. Have them reconstruct a real recent fault as a path across
  the topology, then mark where confidence dropped.
- **Analyse** with `M05`. **Communicate** via `3-insights/` — Sleeswijk Visser
  is explicit that the communication phase is where contextmapping usually
  fails `[sleeswijk2009]`.

## What it produces

Tacit-level insight into diagnostic experience: where confidence breaks, what
engineers reconstruct mentally that the tooling should hold for them, and what
"understanding the platform" actually means to them. Feeds `3-insights/models/`
(mental models, the journey of a diagnosis).

## Traps

- **Skipping sensitizing.** Without it a generative session is just a workshop
  and yields the tidy version anyway. This is the step people cut, and cutting
  it removes most of the value.
- **Treating the collage as the finding.** The artefact is a prompt. The
  finding is in what they *said* while making it — record audio (see
  `0-meta/ETHICS.md`).
- **Recruiting managers instead of practitioners.** You want the people whose
  hands are on the diagnosis.
- **A toolkit that leads.** If your cards already encode your intended IA, you
  will get your IA back. Use neutral primitives.

## Cheaper fallback

If 2–4 weeks is not available: run **`M04` (Critical Decision Method)**
instead. It reaches similar depth on *specific incidents* at roughly a fifth of
the cost, at the price of losing the values layer.

## Sources

`[sleeswijk2005]` is the canonical process description. `[sanders2012]` for the
toolkits and the path of expression. See `SOURCES.md`.
