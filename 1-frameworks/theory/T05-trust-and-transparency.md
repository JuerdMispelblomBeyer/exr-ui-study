---
id: T05
title: Trust, Transparency, and Appropriate Reliance
kind: theory
status: adopted
use_when: [showing computed or inferred state, health aggregation, autonomy status, uncertainty]
sources: [lee2004, chen2014, vicente1992, hri-transparency2025]
---

# Trust, Transparency, and Appropriate Reliance

**The goal is not maximum trust. It is *calibrated* trust — reliance that
matches what the system can actually deliver.**

## What it is

Lee & See's framing `[lee2004]`: both over-trust (relying on an unreliable
output) and under-trust (ignoring a good one) are failures. The design target
is **appropriate reliance**, achieved by making the system's *basis*, *process*,
and *limits* legible rather than by making it look confident.

Their three bases of trust map cleanly onto display decisions:

| Basis | The user asks | Display implication |
|---|---|---|
| **Performance** | Does it work? | Show accuracy, coverage, and known failure cases |
| **Process** | How does it work? | Show what a computed state was derived from |
| **Purpose** | Why does it exist? | Show what it was designed to detect — and what it was not |

Chen et al.'s **SAT model** `[chen2014]` adds an agent-transparency structure
aligned to the SA levels (`T02`): show the agent's current state and intent,
its reasoning and constraints, and its projections with uncertainty.

Recent HRI work finds explanations reliably improve *understanding* even where
their effect on measured trust is inconsistent `[hri-transparency2025]` — which
is an argument for explaining on the grounds of comprehension, not persuasion.

## Why it matters here

This is the theory under one of the strongest decisions already in the project.
`docs/UX_ARCHITECTURE.md` §6 states health is computed from multiple
observations, can be `unknown` or `stale`, and that absence of fault is not
health. That is a calibration commitment. It needs to be enforced everywhere,
because a single unexplained green aggregate undoes it.

Three specific consequences:

**Every computed state owes its derivation.** If the interface says a subsystem
is healthy, the engineer must be able to reach *what was observed, when, and
what was not checked* in one step. An aggregate that cannot be decomposed is
asking for trust it has not earned — and in a platform deployed into ATEX Zone
1, misplaced confidence has physical consequences.

The strongest available argument for this is not a trust study but an accident.
At Three Mile Island, operators relied on pressurizer level as a proxy for
coolant inventory. The cue was valid in normal operation and they did not know
its boundary conditions; under saturation it inverted, and they acted on the
inverted reading `[vicente1992]`. A derived indicator that is right most of the
time, with its validity conditions hidden, is more dangerous than no indicator
— it earns reliance and then withdraws it silently. **Show the conditions under
which a derived value stops meaning what it appears to mean.** See `T01`.

**Freshness is part of the value.** A reading without a timestamp is an
implicit claim of currency. `AGENTS.md` already mandates monospaced timestamps;
the substantive rule is that stale and live values must be visually
distinguishable at a glance, not on inspection.

**Unknown must be a first-class state, not an empty cell.** The interface will
frequently not know — `data/platform-system.yaml` is `status: partial` and
observability across the CAN bus, ROS 2 graph, and containers is uneven. An
absent value rendered as blank reads as "nothing wrong." That is the specific
over-trust failure this domain is most exposed to.

There is also a scope note worth holding: ExRobotics platforms operate
autonomously with cloud-based control through a partner stack `[exr-product]`.
Where displayed state originates from an inference rather than a direct
observation, the distinction belongs on screen. Engineers calibrate very
differently against "measured" versus "concluded."

## How to use it

- **Three-question test on any computed indicator:** What is this derived from?
  How fresh is it? What would make it wrong? If the interface cannot answer all
  three, it is over-claiming.
- **Design the four states explicitly** — known-good, known-bad, stale, unknown
  — as distinct visual treatments, not as an afterthought
  (`docs/UX_ARCHITECTURE.md` §14).
- **Do not smooth over disagreement.** Where two observations conflict, showing
  the conflict is more useful than picking a winner silently.
- **Evaluate calibration, not satisfaction** (`M10`): ask participants how
  confident they are, then check whether that confidence tracked reality. A
  participant confidently wrong is the finding.

## Caveats

- Trust research is largely from automation and HRI contexts with operators
  under live control. These users are engineers doing retrospective and
  live introspection — related, not identical. Treat transfer as a hypothesis.
- More explanation is not monotonically better; verbose justification competes
  with the Level 1 reading (`T02`). Explanation should be reachable, not
  omnipresent.

## Sources

`[lee2004]` is the anchor; `[chen2014]` for agent transparency structure. See
`SOURCES.md`.
