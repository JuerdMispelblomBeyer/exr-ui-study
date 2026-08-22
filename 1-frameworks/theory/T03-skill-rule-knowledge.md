---
id: T03
title: Skill–Rule–Knowledge and Human Error
kind: theory
status: adopted
use_when: [designing for expertise range, safety interactions, deciding automation vs manual, error prevention]
sources: [rasmussen1983, vicente1992]
---

# Skill–Rule–Knowledge (SRK)

**People operate at three cognitive levels depending on familiarity. Each fails
differently. Design has to support all three and protect against each failure
mode.**

## What it is

Rasmussen's taxonomy of cognitive control `[rasmussen1983]`, a hierarchy from
automatic to deliberate:

| Level | How it works | Example here | Its failure mode |
|---|---|---|---|
| **Skill-based** | Automatic, perceptual-motor, no conscious attention | Glancing at the platform overview and knowing it is normal | **Slips** — right intention, wrong execution. Fast and confident. |
| **Rule-based** | Learned if-then patterns from experience | "Inspection frames missing → check the capture service before the camera" | **Procedural traps** — a novel situation where the normal rule set is applied and silently stops working. See `T01`; the Three Mile Island case is the canonical example. |
| **Knowledge-based** | Effortful reasoning from first principles | A fault pattern nobody has seen; reasoning over the platform's actual structure | Slow, error-prone, high workload. Fails under time pressure. |

Experts operate at the lowest level a situation permits and only escalate when
the situation stops matching. The escalation itself is a design-relevant
moment — the interface should make it *obvious* that the familiar reading no
longer applies, or the engineer will keep applying a rule that has stopped
fitting.

## Why it matters here

The current design guidance implicitly targets a single expert user at a single
level. Three consequences worth designing around:

**Consistency is a safety property, not a preference.** Rule-based behaviour
depends on stable cue→meaning mappings. If a status colour, an icon, or a
position means one thing on one screen and something else on another, learned
rules misfire — silently, and with confidence. `docs/DESIGN_GUIDELINES.md` §7
and the tokens file already enforce consistency; SRK is why it matters beyond
tidiness.

**Status must never rely on colour alone** — already a rule in `AGENTS.md`.
SRK sharpens the reason: at skill-based level, colour is processed
pre-attentively and *acted on* before it is consciously read. A colour-only
cue that is wrong will be acted on before it is checked.

**Latched safety states must force level escalation.** Drive Stall
(`docs/DECISION_LOG.md` D022, `docs/SAFETY_CONTROLS.md`) is precisely a state
where routine skill-based scanning must be interrupted and the engineer moved
into deliberate reasoning. That is a legitimate use of the strongest available
presentation — and the argument for why it must look unlike anything in the
routine vocabulary, not merely louder.

**The novice/expert delta is the design opportunity, and there is a mechanism
for closing it.** `M04`'s "what would a less experienced engineer have missed"
probe maps directly: what an expert handles rule-based, a novice must handle
knowledge-based. Vicente & Rasmussen give the lever — where the interface
provides a true one-to-one mapping between the domain's constraints and its
displayed signs, an operator "can exhibit what looks like KBB by merely relying
on RBB" `[vicente1992]`. Making the expert's rule perceptible is how you close
the gap without training.

## How to use it

- **Ask of each element: which level is this serving?** A screen serving only
  knowledge-based reasoning is exhausting for routine work. A screen serving
  only skill-based scanning collapses when something novel happens.
- **Design the escalation cue.** When the situation stops matching known
  patterns — conflicting evidence, unknown state, stale data — say so
  explicitly. "Unknown" is a genuinely useful display state (`T02`).
- **Protect against slips on consequential actions.** Confirmation, delay, or
  physical separation for anything with real effect, per
  `docs/SAFETY_CONTROLS.md` §8.
- **Never reuse a routine visual pattern for an exceptional state.**

## Caveats

- SRK is a description of cognitive control, not a user segmentation. The same
  engineer moves between all three levels within one diagnosis.
- Level cannot be observed directly; infer it from `M04` and `M10` data with
  appropriate tentativeness.

## Sources

`[rasmussen1983]` is the origin; `[vicente1992]` operationalises it into
interface principles (`T01`). See `SOURCES.md`.
