---
id: D02
title: Observability Practice and the Robot Introspection Landscape
kind: domain
status: adopted
use_when: [before designing any view, deciding what data can exist, avoiding reinventing existing tools]
sources: [majors2022, opentelemetry, microservice-survey2025, foxglove-compare, ros2-docs]
---

# Observability Practice and the Robot Introspection Landscape

**There is a large engineering discipline and a mature tool ecosystem for
exactly this problem. Your engineers already use some of it. Study it before
designing, or you will redesign Foxglove with better typography.**

## Part 1 — Observability as an engineering discipline

The ExRobotics platform is, structurally, a **distributed system**: three
compute nodes, containers, a ROS 2 / DDS graph, a CAN bus, and a network,
producing partial and asynchronous evidence. That is the same shape as the
systems the observability field was built for, and its concepts transfer.

### The three pillars, and why they are contested

The conventional decomposition is **metrics, logs, traces**. Each answers a
different question — *is something wrong* (metrics), *what happened*
(logs), *where in the causal chain* (traces).

The influential critique `[majors2022]`: the three pillars are three *storage
silos*, and forcing an engineer to correlate across them by hand is the actual
cost of debugging. The counter-proposal is **arbitrarily wide structured
events** as the single source of truth, with metrics and traces derived as
views. The motivating distinction:

- **Monitoring** answers questions you knew to ask — *known unknowns*, encoded
  as dashboards and thresholds.
- **Observability** is the ability to answer questions you had not thought of
  in advance — *unknown unknowns* — without shipping new instrumentation.

**This maps precisely onto `T01`.** Rasmussen's rule-based level is the
known-unknown regime; knowledge-based reasoning about novel faults is the
unknown-unknown regime. Dashboards serve the first. A system that lets you ask
new questions of existing data serves the second. Your product's differentiated
value is almost certainly in the second, and that is a *data-model* claim
before it is a UI claim.

The practical constraint to respect: **high cardinality is what makes arbitrary
questions answerable, and it is expensive.** On a robot with constrained
storage and intermittent connectivity, that trade-off is real. Find out what is
actually retained, and where.

### Distributed tracing and causality

Tracing reconstructs a causal chain across components — the thing an engineer
manually reconstructs when they ask "the camera frames stopped; was it the
capture service, the container, the node, or the bus?" ROS 2 has no universal
trace context the way HTTP services do, which is itself worth investigating:
**is end-to-end causality across the ROS 2 graph even reconstructible today?**
If not, that is a finding with consequences well beyond the interface.

A 2025 survey of failure diagnosis in microservice systems (98 papers) reports
that combining **logs, metrics, traces, events and topology** yields
substantially better fault localisation than any subset
`[microservice-survey2025]`. Topology is the one most often missing — and it is
the one your design already centres (D014, "platform graph as the primary
mental model"). That is a point of genuine alignment between your design
instinct and the literature.

## Part 2 — The existing tool landscape

**Study these as prior art. Some of them are what your engineers use today.**

| Tool | What it is | Why it matters to you |
|---|---|---|
| **rqt / rqt_graph** | Standard ROS visualisation plugins; live node/topic graph | The default mental model of "the ROS graph as a picture" your engineers already hold |
| **`ros2 doctor`, `ros2 topic/node/param`** | CLI introspection | The baseline. What does an engineer type first, and why? |
| **`diagnostic_msgs` / diagnostic aggregator** | ROS's own convention for component health reporting | An existing, structured health model. Whether ExRobotics uses it is a key question |
| **RViz** | 3D robot state visualisation | Spatial/physical state — largely orthogonal to platform introspection |
| **Foxglove** | Web/desktop robotics observability; live and recorded; layered panels | The closest existing product to what you are designing. **Study it hardest.** |
| **Rerun** | Code-first visualiser, SDK-driven, time-aware | Different model: visualisation as instrumentation |
| **PlotJuggler** | Time-series analysis with derivatives, filters, expressions | Sets the bar for what engineers expect of signal analysis |
| **MCAP** | Recording format, rosbag2 default from Iron onward | The substrate for anything retrospective |
| **Grafana / Prometheus** | Metrics dashboarding | Likely already present on the infrastructure side |

## Why this matters here

**The most valuable thing you can learn early is what is already solved.** Your
differentiator will not be plotting a topic faster than PlotJuggler. It is far
more likely to be:

- **integration across evidence types** the existing tools keep separate —
  which is precisely the three-pillars critique, restated as a design
  opportunity;
- **the abstract-function layer** (`T01`, `M11`) that none of these tools
  represent at all, because they are built around physical components;
- **the diagnostic narrative** — what has been ruled out, by whom, on what
  evidence (`T06`, `T07`).

Note also that Foxglove, Rerun, and PlotJuggler are all evidence about
**conventions your users already know**. Departing from them costs learning;
`T03` says consistency is a correctness property. Deviate deliberately, not
accidentally.

## How to use it

- **Tool inventory before design.** In `M03`, record precisely which of these
  are in use, for what, and what engineers say each is bad at. The complaints
  are the brief.
- **Spend a day in Foxglove with real ExRobotics data.** Not to copy it — to
  find where it stops helping. That boundary is your product's territory.
- **Establish what data actually exists** before designing views that need it.
  `M06` warns that Figma will happily render data you cannot obtain; this is
  where you check. Feed answers back into `data/platform-system.yaml`.
- **Ask the retention and connectivity questions.** What is recorded on-robot,
  what survives to the ground, what is discarded, at what resolution, and for
  how long? This constrains everything retrospective — and per `D01`,
  retrospective is the dominant mode for an autonomous platform.

## Caveats

- Observability practice comes from cloud services with elastic storage and
  continuous connectivity. A robot in ATEX Zone 1 has neither. Transfer the
  *concepts*; verify every assumption about cost and availability.
- The tool table is from vendor and community comparisons, not hands-on use
  here. Verify current capabilities directly — this ecosystem moves fast.

## Sources

`[majors2022]` for the observability argument; `[microservice-survey2025]` for
diagnosis techniques; `[foxglove-compare]`, `[ros2-docs]` for tooling. All
secondary. See `SOURCES.md`.
