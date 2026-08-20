---
id: M10
title: Scenario-Based Evaluation with Experts
kind: method
status: adopted
use_when: [testing any prototype, closing an iteration, checking a design change actually helps]
cost: low — 3–5 sessions of 60–90 min per iteration
sources: [endsley2000, endsley1995, buchenau2000, braun2022]
---

# Scenario-Based Evaluation with Experts

**Give an engineer a real fault and a prototype, and watch them try to find it.
Do not ask whether they like it.**

## What it is

Task-based evaluation with domain experts, using scenarios drawn from real
incidents. Three components worth combining here:

**Think-aloud on a real diagnostic task.** The participant works a scenario and
narrates. You are watching for where they look first, what they misread, what
they cannot find, and where they stop trusting the display.

**SA probes.** Endsley's SAGAT technique freezes the scenario at unpredictable
points, blanks the display, and asks what the participant currently believes
`[endsley2000]`. You probe all three SA levels (`T02`): *what is the state of
the CAN bus?* (perception) · *is this platform safe to redeploy?*
(comprehension) · *what will fail next if this is not addressed?* (projection).

A full SAGAT needs a running simulation, which Figma is not. The adapted form
for this project: at 2–3 points, cover the screen and ask three questions. It
is cruder, and it still catches the failure mode that matters most — a display
the engineer can read fluently but which leaves them holding a wrong model.

**Condition simulation** `[buchenau2000]`. Add what makes real diagnosis hard:
a time constraint, an incomplete observation, a stale value, one plausible-but-
wrong lead. Evaluating a fault interface under calm conditions tests the wrong
thing.

## Why it fits this project

The users are a small population of experts, so classic usability metrics on
small n are close to meaningless — but expert judgement on a realistic task is
extremely informative. Three engineers working a real scenario will find the
structural problems.

The scenarios come free: `M04` produces real incidents as a by-product, and
`docs/UI_FUNCTIONAL_REQUIREMENTS.md` §14 already contains initial acceptance
scenarios that can be converted into evaluation tasks.

This also closes the RtD loop from `M01`. An iteration without this step is a
design change, not a research cycle.

## How to run it here

- **3–5 engineers per iteration.** Rotate so the same person is not always
  seeing the prototype fresh; keep at least one repeat participant to hear
  what changed for them.
- **Scenario, not tour.** Open with: *"This platform came back from site
  yesterday. Inspection footage is missing for the last two runs. Find out
  why."* Then be quiet.
- **Prompt, do not rescue.** "What are you thinking?" · "What would you do
  next?" · "What did you expect to happen?" Never "did you see the panel on the
  right?"
- **Record where they look first.** The first fixation on an unfamiliar screen
  is the strongest signal you get about whether the hierarchy works.
- **Probe SA at 2–3 freezes**, per above.
- **Close with a comparison, not a rating.** "Against the version you saw last
  time, what is better and what is worse?" — this feeds `M07` annotations.
- **Analyse with `M05`.** Log the session under
  `2-research/studies/S0n/sessions/`, per `0-meta/ETHICS.md`.

## What it produces

- Breakdowns, ranked by how badly they derail the task.
- SA failures — the dangerous class: fluent reading, wrong model.
- Comparative judgements that become `M07` annotations.
- Evidence to close or revise entries in `2-research/questions.yaml`.

## Traps

- **Asking for opinions.** "What do you think of this screen?" produces
  politeness and art direction. Task performance produces findings.
- **Explaining the prototype first.** Whatever you explain, you can no longer
  test. Say only what the scenario says.
- **Treating a Figma flow as a system test.** Clicking a predefined path proves
  the path exists, not that they would have found it. Leave dead ends in.
- **Only testing the happy path.** The value of this interface is concentrated
  in degraded, stale, partial, and unknown states —
  `docs/UX_ARCHITECTURE.md` §14. Evaluate those specifically.
- **Fixing everything you hear.** Experts propose solutions fluently. Take the
  breakdown as data; the solution stays your call.

## Sources

`[endsley2000]` for SAGAT; `[endsley1995]` for the SA levels behind the probes;
`[buchenau2000]` for condition simulation. See `SOURCES.md`.
