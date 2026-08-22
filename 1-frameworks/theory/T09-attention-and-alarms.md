---
id: T09
title: Attention, Alerting, and Alarm Management
kind: theory
status: candidate
use_when: [status and attention design, notifications, safety states, deciding what may interrupt]
sources: [eemua191, isa182, endsley1995, rasmussen1983]
---

# Attention, Alerting, and Alarm Management

**There is a mature standards literature on how to decide what deserves an
operator's attention, built from decades of industrial accidents. It has
numbers. Your product is adjacent enough to borrow from it.**

## What it is

Process industries — including oil, gas, and chemical, which is exactly where
ExRobotics platforms are deployed — govern alerting through **EEMUA 191** and
**ANSI/ISA-18.2 / IEC 62682** `[eemua191, isa182]`.

The core ideas transfer well beyond alarms:

**An alarm lifecycle, not an alarm list.** Philosophy → identification →
**rationalisation** → detailed design → implementation → monitoring → periodic
review. Rationalisation is the key stage: every alarm must justify its
existence against stated criteria — is there a *specific operator action*, is
there *time* to take it, and what are the *consequences* of not acting? An
indicator that fails those tests should not be an alarm.

**Alarm flooding is the failure mode.** Systems that alert on everything train
operators to ignore everything, and this has contributed to real industrial
accidents. The standards therefore set explicit load targets — roughly **one
alarm per operator per ten minutes** in steady state, and **no more than ten in
the first ten minutes** of a major upset (EEMUA 191, 4th ed., 2024).

**Priority must be scarce to mean anything.** Priority distributions are
specified deliberately, with high-priority reserved for a small percentage.
If everything is critical, nothing is.

## Why it matters here

Your interface is not a control-room alarm system, and it should not pretend to
be. But it will show attention-demanding state — degraded subsystems, latched
protection states, stale observations, failed services — and the current
guidance handles this only as a *visual* problem.
`docs/DESIGN_GUIDELINES.md` covers how status looks. Nothing covers **which
states earn attention, on what basis, and with what budget.**

Three things worth borrowing:

**Apply the rationalisation test to every attention-demanding element.** For
each: is there a specific action an engineer would take? Is there time? What
happens if they do not? Anything that fails is information, not an alert.
Applied honestly this will substantially thin the design, and thinning is the
point.

**Set an explicit attention budget** and make it a design constraint, the way
`docs/INTERFACE_REDESIGN_PLAN.md` §5 sets an information budget. How many
things may compete for attention on one screen? What is the maximum in a
degraded state? Decide it, then hold the design to it.

**Drive Stall is the case that most needs this.** `docs/SAFETY_CONTROLS.md` and
D022 define a latched protection state. The standards' framing — a state
requiring a specific operator response, with defined presentation, priority,
and a documented path to acknowledgement and reset — maps directly, and its
concepts (shelving, suppression, acknowledgement, reset) are worth adopting as
vocabulary because they are precise and already understood by people in this
industry.

## How to use it

- **Rationalise, in writing.** One table: state, does it need action, is there
  time, consequence of inaction, priority. It doubles as design rationale.
- **Distinguish "needs attention now" from "is abnormal."** Most abnormal
  states in a returned platform need investigation, not interruption. Only the
  first class may interrupt.
- **Never rely on colour alone** — already in `AGENTS.md`, and reinforced by
  `T03`: at skill-based level colour is acted on before it is consciously read.
- **Count alerts per scenario in evaluation** (`M10`). If a realistic degraded
  scenario floods the screen, that is a finding, not a rendering issue.
- **Do not import alarm aesthetics.** Borrow the reasoning and the vocabulary,
  not the flashing banners of a 1990s DCS.

## Caveats

- **Scope mismatch, stated plainly.** These standards govern real-time process
  control where an operator must act within seconds. Your users are engineers
  doing introspection and retrospective diagnosis. The *lifecycle and
  rationalisation reasoning* transfers; the response-time assumptions and
  performance metrics largely do not. Do not cite EEMUA load figures as
  requirements for this interface.
- Marked `candidate`: adopt properly only once `docs/SAFETY_CONTROLS.md` §3
  resolves whether any safety classification applies. If it does, this stops
  being borrowed inspiration and starts being a compliance question — which is
  a conversation for ExRobotics' safety engineers, not a design decision.
- The standards are paid documents and have not been read here. Everything
  above is from secondary summaries.

## Sources

`[eemua191]`, `[isa182]` — **secondary summaries only**. See `SOURCES.md`.
