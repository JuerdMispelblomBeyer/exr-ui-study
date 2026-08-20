---
id: D01
title: ExRobotics Operating Context
kind: domain
status: partial — needs verification with the company
use_when: [grounding any design decision in the real deployment situation, recruiting participants, writing scenarios]
sources: [exr-product]
---

# ExRobotics Operating Context

**What the robots do, where they go, and who this interface is actually for.**

> ⚠️ **Assembled from public product material and press coverage, not from
> ExRobotics itself.** Every claim below is a candidate for correction in the
> first conversation with the company. Do not treat it as verified project
> input; verify and then move confirmed facts into
> `docs/PLATFORM_SYSTEM_MODEL.md`, which is the project's source of truth.

## The platforms

ExRobotics builds tracked inspection robots (ExR-1, ExR-2) for **potentially
explosive atmospheres** `[exr-product]`:

- **ATEX / IECEx Zone 1 certified** — one of very few robots qualified for
  areas where a flammable atmosphere may be present in normal operation.
- **IP67**, tracked chassis, payload capacity around 30 kg.
- Payloads: PTZ camera, IR thermal, LiDAR, gas sensors, microphone.
- Applications: audio-visual inspection, heat-pattern detection, gas and
  emissions detection (methane, benzene), predictive maintenance data capture.
- Deployed in **oil and gas, petrochemical, and chemical** facilities.
- ExR-2 is designed to operate **autonomously**, with cloud-based control
  available through a partner stack (Energy Robotics).

## Why the context shapes the design

**The robot goes where people should not.** That is the entire value
proposition, and it inverts the usual diagnostic situation: you cannot walk
over and look at it. Remote introspection is not a convenience feature — it is
the only channel. Anything the interface fails to expose is genuinely
unobservable until the platform is recovered.

**Deployment decisions carry physical consequence.** Sending a platform into
Zone 1 with an undiagnosed fault risks the platform, the mission, and
potentially the site. This is the substantive argument behind
`docs/SAFETY_CONTROLS.md` and behind `T05` — the interface participates in a
decision whose cost of error is not a bad user experience.

**Autonomy raises the observability bar.** A teleoperated robot has a human
continuously in the loop who notices things. An autonomous one accumulates
state unobserved, and the engineer meets it afterwards. That makes history,
provenance, and freshness (`T05`) more important than live telemetry, and it
supports the "handover" reading in `T06`.

**Harsh conditions produce ambiguous data.** Dust, temperature, vibration, and
EM environment mean sensors degrade and drop out. Distinguishing *the sensor is
broken* from *the sensor is reporting something bad* is a genuine and recurring
diagnostic problem, and a good candidate for `M04` incident elicitation.

## Who the user is — the distinction that matters most

There are two populations, and this project serves the second:

| | **Field / mission operators** | **Platform engineers** ← *this project* |
|---|---|---|
| Concern | Where does the robot go, what does it inspect, is the run complete | Is the platform itself sound: compute, buses, services, sensors |
| Tooling | Fleet and mission control, largely via the partner stack | Direct platform introspection |
| Question | "Did we get the data?" | "Why did that node stop publishing?" |

`AGENTS.md` already draws this boundary and excludes fleet, missions, routes,
and tasking. Grounding it in the real organisation: **that other interface
largely already exists**, supplied through the partner control stack. The gap
this project fills is the engineering layer beneath it.

Two consequences: the interface must be legible to people who already hold a
deep mental model of the platform — so it should *externalise structure* (`T01`)
rather than simplify it — and there is a real boundary object where mission
symptoms ("inspection frames missing") must be traceable to platform causes.
Where that handoff happens is worth mapping explicitly.

## What to verify first

Priority questions for the first ExRobotics conversation:

1. Who actually diagnoses platform faults — a dedicated team, field service, or
   whoever is free? How many people?
2. Does diagnosis happen with the platform present, remotely, or both? What
   proportion?
3. What is the real tool ecology today? (`M03` will answer this properly.)
4. How often is a platform genuinely hard to diagnose — and what does that
   currently cost in time and in deployment delay?
5. Where is the boundary with the partner control stack, and what does it
   already expose?
6. What is the actual fleet size and deployment cadence? This sets whether
   diagnosis is a daily activity or an occasional one, which changes the design
   considerably.
7. Is there any safety classification already assigned to platform-state
   displays? (`docs/SAFETY_CONTROLS.md` §3 flags this as unresolved and
   blocking.)

## Sources

`[exr-product]` — public product and press material. Nothing here is
first-party project input yet. See `SOURCES.md`.
