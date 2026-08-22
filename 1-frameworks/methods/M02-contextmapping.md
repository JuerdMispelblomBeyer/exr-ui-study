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
you diagnose a robot" and you get the tidy version.

**Five phases:** preparation → sensitizing → group sessions → analysis →
communication.

The mechanism is that participants **make a designerly artefact and then tell a
story about what they made**. Making is what gives access: people "reflect on,
re-live and to some degree re-feel their experiences" while constructing
something. The artefact is a vehicle — *"especially in their stories, there is
rich and useful information for designers."*

Conventional techniques (interviews, observation, focus groups) reach explicit
and observable knowledge, and give "little hold on the future." Generative
techniques reach two further levels: **tacit knowledge** — what people can act
on but cannot readily put into words — and **latent needs** — needs they are
not yet aware of. Diagnostic expertise is largely tacit, which is the whole
argument for using this here.

The experience domain spans **past memories → the present moment → future
dreams**; generative exercises walk participants through it in that order,
because aspiration is only reachable after recollection.

**Contextmapping produces a map, not a route.** The output should give the
design team *"roads, dangers, and opportunities to the traveller, not… a mere
route prescribing a fixed solution."* Insight that over-prescribes has failed —
it removes the designing.

## Why it fits this project

The unknowns in `docs/UI_FUNCTIONAL_REQUIREMENTS.md` §15 and
`docs/UX_ARCHITECTURE.md` §19 are mostly latent-level: not "which metric do you
want" but "what does it feel like when a robot comes back and you cannot tell
whether the CAN bus or the Jetson is at fault." That is a memory-and-values
question, not a feature question.

It is also the method your own faculty is known for, and the one the current
docs most conspicuously lack.

## How to run it here

**Start at least three weeks before the session** — that is the paper's own
figure, and it is mostly recruiting plus sensitizing lead time.

- **Write your preconceptions down first.** The paper's practice is to build a
  mindmap of what the team already assumes *before* the study, so new material
  can be recognised as new rather than absorbed into existing belief. You are
  unusually well set up for this: `docs/UX_ARCHITECTURE.md` §3, §19 and
  `docs/UI_FUNCTIONAL_REQUIREMENTS.md` §15 already *are* the preconception map.
  Freeze a copy before you start.
- **Group size: 4–6 per session, and run at least two sessions.** Four is
  enough for genuine group discussion; above six you cannot attend to
  individuals. Three works but yields fewer stories — participants need each
  other to react to. Multiple sessions stop one dominant voice defining the
  findings.
- **Sensitizing package sent 1–2 weeks ahead, 5–10 minutes of work per day.**
  Keep the subject **broader than the session topic** — the paper is explicit
  that over-specific exercises make participants arrive with prepared answers.
  So probe *how the working day goes, where attention goes, what gets checked
  and re-checked*, not "how do you diagnose CAN faults." Pilot it on one person
  first.
- **Session toolkit:** blank platform-topology cards (compute nodes, CAN, ROS 2
  nodes, cameras, network), timeline strips, friction stickers. Have them
  reconstruct a real recent fault as a path across the topology, then mark
  where confidence dropped.
- **Record video and audio**, and transcribe the verbal protocol — the stories,
  not the collages, carry the findings.
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
- **The problem-solvers trap — the big one for this project.** The paper warns
  that a group made up mainly of designers is difficult because they are
  *"problem-solution minded and therefore fail to make their own experiences
  explicit."* Your participants are **engineers**, who have exactly this
  disposition and more of it. They will jump to proposing features. Expect it,
  and structure exercises so that the first move is always *reconstruct what
  happened*, never *what should it do*. Consider including one participant from
  outside engineering.
- **A toolkit that leads.** If your cards already encode your intended IA, you
  will get your IA back. Use neutral primitives.

## Cheaper fallback

If 2–4 weeks is not available: run **`M04` (Critical Decision Method)**
instead. It reaches similar depth on *specific incidents* at roughly a fifth of
the cost, at the price of losing the values layer.

## Sources

`[sleeswijk2005]` is the canonical process description. `[sanders2012]` for the
toolkits and the path of expression. See `SOURCES.md`.
