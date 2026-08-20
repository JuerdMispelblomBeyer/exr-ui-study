---
id: T02
title: Situation Awareness
kind: theory
status: adopted
use_when: [deciding information hierarchy, designing overview screens, writing evaluation probes]
sources: [endsley1995, endsley2000]
---

# Situation Awareness (SA)

**Three levels: what is happening, what it means, what happens next. Most
interfaces serve the first and abandon the operator at the second.**

## What it is

Endsley's model `[endsley1995]`:

| Level | Name | The engineer's question |
|---|---|---|
| **1** | **Perception** | What is the state of the elements? *Is the CAN bus reporting? What is the Jetson temperature?* |
| **2** | **Comprehension** | What does it mean, together? *Is this platform fit to redeploy?* |
| **3** | **Projection** | What follows? *Will this degrade mid-mission? What fails next?* |

Level 2 is synthesis against goals. Level 3 is forecasting. Both are where
expertise lives, and both are where interfaces typically stop, dumping the
integration cost on the operator's working memory.

Design proceeds in three phases: analyse SA **requirements**, apply SA-oriented
design **principles**, then **measure** SA during evaluation `[endsley2000]`.

## Why it matters here

Run the current design intent through the three levels and the gap is stark.
`docs/UI_FUNCTIONAL_REQUIREMENTS.md` is overwhelmingly Level 1 — expose
participants, expose reachability, expose discovery, expose QoS. Those are
perception requirements. `docs/DECISION_LOG.md` D017 ("Overview prioritizes
causality and freshness") reaches toward Level 2. Almost nothing addresses
Level 3.

For a platform that is deployed unattended into a Zone 1 hazardous area, Level
3 is arguably the highest-value question the interface could answer: *given
what I can see, what is likely to fail during the next deployment?* Nothing in
the current requirement set attempts it.

This also sharpens an existing decision. `docs/UX_ARCHITECTURE.md` §6 states
health can be `unknown` or `stale`, and that absence of fault is not health —
that is a Level 2 commitment, and a good one. It should propagate: every
aggregate reading needs its confidence and freshness visible, or Level 2 is
built on sand.

## How to use it

- **Classify every proposed element.** If a screen is all Level 1, it is a
  readout, not a diagnostic instrument.
- **Design Level 2 explicitly.** Aggregate states must show *what they are
  computed from* and *how fresh the inputs are*. An unexplainable summary is
  worse than no summary, because it invites misplaced confidence (`T05`).
- **Attempt Level 3 where evidence supports it** — trend, projection to a
  threshold, "what depends on this if it fails." Where evidence does not
  support it, say so rather than implying it.
- **Write evaluation probes from the levels** (`M10`). Freeze the prototype,
  cover the screen, ask one question per level. A participant who reads the
  screen fluently but answers Level 2 wrong has found you a real defect.
- **Derive SA requirements from `M04`.** The cue inventory maps to Level 1; the
  decision points map to Level 2; the "what would have happened next" probes
  map to Level 3.

## Caveats

- SA is a well-established but contested construct; there is a long-running
  critique that it describes a product rather than a process, and the
  distributed-cognition reading (`T06`) is a useful counterweight.
- SAGAT proper requires simulation freezes. The Figma adaptation in `M10` is a
  reasonable approximation, not the validated instrument. Do not report it as
  SAGAT scores.
- More information does not produce more SA. Level 1 saturation actively
  degrades Levels 2 and 3 — which is the human-factors argument behind the
  information budget in `docs/INTERFACE_REDESIGN_PLAN.md` §5.

## Sources

`[endsley1995]` for the model; `[endsley2000]` for measurement. See
`SOURCES.md`.
