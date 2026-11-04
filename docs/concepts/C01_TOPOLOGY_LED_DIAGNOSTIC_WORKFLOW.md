# C01 — Topology-led diagnostic workflow

**Status:** Exploratory concept; not the sole or approved direction  
**Origin:** Workflow idea retained from Visual Style v4  
**Scope:** Internal robot-platform inspection, diagnosis, controlled change, and
verification  
**Not in scope:** Fleet management, missions, autonomy, SLAM, navigation, or
teleoperation

## 1. Core proposition

Use one stable visual model of the robot's connectivity and dependencies as the
engineer's persistent mental map. The interface carries the engineer through a
causal investigation without forcing them to navigate between disconnected
category dashboards.

The canonical sequence for this concept is:

```text
Orient → Notice → Locate → Understand → Prove → Change → Verify
```

The topology is the continuity mechanism. It is not merely an illustration and
it is not a network-configuration wizard.

## 2. Why it can feel like “network setup”

The first view begins with the platform's connection backbone because it
explains how the onboard system is assembled:

```text
Wi-Fi / 4G–5G
        ↓
VRRP / keepalived ownership
        ↓
Onboard LAN
   ┌────┼────────┐
 Intel  Jetson 1  Jetson 2
   ↓
  CAN
   ├─ Charging
   ├─ Battery
   ├─ Motor drive
   └─ GPIO / ADC
```

This is an orientation model, not a required setup sequence. It answers:

- what is connected to what;
- which route or owner is current;
- where a degraded signal first appears;
- which dependencies may be affected;
- where the engineer should inspect next.

A later concept may explore commissioning or guided network configuration, but
that should remain distinct from this diagnostic topology.

## 3. Stable geography, changing lenses

Intel, Jetson 1, Jetson 2, the onboard LAN, Intel-to-CAN boundary, and CAN
subsystems retain stable positions. Switching context changes emphasis and
annotation without rearranging the platform.

Potential lenses:

- **Physical:** computers, cameras, CAN, power-controlled hardware, and physical
  subsystems;
- **Network:** Wi-Fi, cellular, VRRP/keepalived, LAN, CAN, Tailscale, interfaces,
  peers, paths, latency, errors, and throughput;
- **Software:** Docker containers, runtime ownership, service dependencies,
  partner runtimes, ROS 2/DDS, and diagnostics;
- **Time:** chrony sources, participants, offsets, uncertainty, and correlation
  confidence;
- **Integration:** fleet-manager API or onboard-agent boundary and the selected
  data path, without exposing fleet-management workflows.

An engineer can therefore move from a motor-drive CAN problem to an Intel
container restart and then to clock confidence without losing the selected
object or causal path.

## 4. Task modes, not domain pages

The primary modes are verbs:

1. **Inspect** — understand present platform structure and state.
2. **Diagnose** — investigate a condition across synchronized evidence.
3. **Change** — review and perform an allowed platform action.

Compute, Network, Software, Time, and Integration are lenses or evidence
domains inside the task. They are not isolated top-level dashboards.

## 5. Conceptual user flow

1. Open one robot platform.
2. Verify robot identity, connection freshness, permissions, and safety state.
3. Read the stable platform topology.
4. Enter by selecting a visible abnormal object/path, searching for a known
   object, or applying a lens that answers a domain question.
5. Transform the attention area into an inspector for the selected object.
6. Read the state reason, impact, immediate dependencies, source, and
   freshness.
7. If proof is required, expand synchronized evidence while preserving the
   selection, path, filters, and time window.
8. If a permitted action is required, enter Change with the diagnosis and
   evidence still attached.
9. Review target, scope, preconditions, consequences, expected result,
   acknowledgement, rollback, and audit implications.
10. Observe the result, verify recovery, and return to the same platform map.

## 6. Progressive disclosure

| Level | Purpose | Typical content |
| --- | --- | --- |
| Glance | Orient and notice | topology, object/path state, freshness, one dominant condition |
| Focus | Understand a selected object | identity, reason, impact, dependencies, explanatory values |
| Evidence | Prove or disprove a hypothesis | synchronized traces, logs, events, messages, configuration, timestamps, source confidence |
| Change | Act deliberately | intended change, authority, preconditions, consequences, acknowledgement, observed result, audit record |

The default overview should not expose every CPU percentage, port, version,
timestamp, or trace. Precision appears when it supports the current question.

## 7. Flow invariants

- Selecting any representation of an object opens the same object context.
- Switching lenses never clears the selection.
- Opening evidence never clears the selected object, path, filters, or time
  window.
- Entering Change preserves the diagnosis that motivated the action.
- Returning to Inspect restores the same platform geography and focused path.
- Safety state remains visible throughout the workflow.
- Normal objects recede; one current or abnormal path may dominate attention.
- Status never relies on color alone.

## 8. State semantics

The concept separates workflow semantics from decoration:

- ExRobotics yellow: current selection, active path, present sample, or decisive
  deliberate action;
- orange: degraded condition or caution;
- red: fault or approved stop semantics only;
- geometry, labels, patterns, and line treatments reinforce every state.

The exact visual treatment remains open to future art direction.

## 9. Strengths worth retaining

- Preserves spatial orientation across a multi-domain investigation.
- Represents causes and dependencies rather than unrelated KPI categories.
- Supports dense engineering information through progressive disclosure.
- Makes overview, evidence, and action stages feel like one continuous task.
- Maps naturally to the actual three-computer, LAN, CAN, container, uplink, and
  time-synchronization architecture.
- Allows visual-first fault localization: an orange path or subsystem can
  communicate more quickly than a paragraph or alert list.

## 10. Risks and open questions

- A large topology can become visually noisy as the system model grows.
- The stable geography must still support small screens and different service
  contexts.
- Engineers may need list, search, and table entry points in addition to the
  spatial map.
- A network-like drawing may incorrectly imply that every relationship is a
  physical connection; relationship types require an explicit grammar.
- Root-cause confidence and unknown states must not be overstated visually.
- Safety actions and Drive Stall recovery require their own validated lifecycle;
  topology context does not make an action safe.
- The correct balance between persistent context and temporary evidence needs
  testing with real incidents.

## 11. Evaluation criteria

When this concept is compared with future concepts, test whether an engineer
can:

1. identify the robot, freshness, and safety posture immediately;
2. explain the physical and logical route to a selected subsystem;
3. locate a dominant degraded object or path without scanning every item;
4. move between network, software, time, and hardware evidence without losing
   context;
5. distinguish observed facts, inferred causes, and unavailable data;
6. reach detailed evidence without overloading the overview;
7. perform a permitted change with motivation, scope, consequences, and result
   preserved;
8. return to the overview and verify the new state.

## 12. Relationship to future concepts

C01 is one candidate direction. Future concepts may use a different organizing
model—for example an incident timeline, task queue, subsystem workbench,
commissioning sequence, search-first console, or direct hardware representation.
They should be documented beside C01 rather than overwritten by it.

