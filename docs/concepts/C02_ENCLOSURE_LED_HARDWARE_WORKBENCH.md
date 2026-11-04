# C02 — Enclosure-led hardware workbench

**Status:** Exploratory concept; not approved product architecture
**Scope:** Internal robot-platform inspection, as-built reconciliation,
hardware diagnosis, controlled change, and verification
**Not in scope:** Fleet management, missions, autonomy, navigation,
teleoperation, a mechanical CAD viewer, or a replacement for service manuals

## 1. Core proposition

Use the robot's physical containment hierarchy as the engineer's primary entry
point:

```text
Robot → enclosure → board/controller → connector/power domain → module/device
```

The interface begins by answering **what is physically expected and present**,
then exposes the electrical, data, software, and evidence paths needed to
explain whether that hardware is functioning.

The canonical sequence is:

```text
Identify → Reconcile → Locate → Trace → Prove → Change → Observe
```

This direction is especially suited to service, commissioning, hardware
revision differences, optional equipment, and failures where `not installed`,
`not powered`, `not detected`, and `faulted` must not be conflated.

## 2. Problem this concept solves

The ExR-2 references describe several nested physical structures:

- an electronics box containing the Intel computer, motherboard STM, BOTP,
  USB peripherals, audio path, power injector, and revision-dependent options;
- a communication box containing a Xavier NX, WiFi, 4G/LTE, power control, and
  a status indicator;
- standard, optional, special, replacement, and incompatible camera and sensor
  variants;
- switchable 12 V, 36 V, USB3, camera, gas-sensor, motor-drive, and optional
  zippermast domains;
- measurements that look related but have different provenance, such as BOTP
  pack state and motherboard input voltage/current.

A connection topology can show dependencies, but it is less direct when the
engineer's first question is:

- Which enclosure should I open?
- Is this device supposed to be fitted on this hardware revision?
- Which controller and switch channel feed it?
- Which connector, board, or power domain sits between the device and host?
- Is the failure electrical, attachment-level, communication-level, or
  functional?

## 3. Organizing and spatial model

The primary instrument is a **source-qualified equipment map**, not a generic
dashboard and not a photorealistic digital twin.

At the robot level, it shows approximate physical zones for:

- electronics box;
- communication box;
- battery pack and BOTP;
- drive module;
- induction charger receiver;
- LiDAR, inspection, drive, front/rear, THK PTZ, and IR/thermal variants;
- microphone, speaker, gas detectors, acoustic analyser, mast, and zippermast
  when configured or reference-documented.

Selecting a zone opens an exploded containment stage. Children remain grouped
by enclosure and interface rather than becoming unrelated cards. A compact
robot silhouette remains visible as a locator while the selected enclosure is
expanded.

The selected device receives a vertical readiness chain:

```text
Expected → Installed → Detected → Powered → Communicating → Healthy
```

Each transition names its source and freshness. The chain may stop at
`Unknown`; later states are not inferred from earlier ones.

## 4. Conceptual user flow

1. Open one robot platform and verify immutable identity, connection,
   freshness, permissions, and persistent safety state.
2. Compare the selected robot's intended/as-built configuration with the
   minimal, standard, optional, special, and revision-dependent reference
   model.
3. Enter through a highlighted physical zone, a search result, an abnormal
   device, or a configuration mismatch.
4. Expand the relevant enclosure or module while retaining a locator on the
   complete robot.
5. Select the child board, controller, connector, power domain, or device.
6. Read its readiness chain and the first unproven or failing transition.
7. Trace outward from that transition:
   - toward power, switch, controller, or host when attachment is suspect;
   - toward CAN, analog, USB, Ethernet, FTDI, stream, or software consumer
     when communication or function is suspect.
8. Open evidence for the selected transition, preserving the physical target,
   path, time range, and hardware revision.
9. If an allowed change is required, review exact switch channel or runtime
   target, shared dependencies, expected interruption, acknowledgement,
   observed electrical state, device recovery, rollback, and audit.
10. Verify every affected readiness transition and return to the same expanded
    enclosure.

## 5. What is visible when

| Moment | Always visible | Newly visible | Deliberately hidden or collapsed |
| --- | --- | --- | --- |
| Robot landing | Robot identity, connection/freshness, permission, persistent safety state, compact equipment map, highest-impact abnormal zone, configuration coverage | Minimal/standard/optional/special legend; count of expected, detected, unknown, and mismatched modules | Raw metrics, every connector, logs, detailed dependencies, controls |
| Configuration reconciliation | Robot locator, selected reference revision, freshness | Intended versus detected equipment list; replacement and incompatibility constraints; unknown as-built facts; SD-card/board-revision and special-option notes | Health conclusions for objects whose installation is unresolved |
| Enclosure focus | Robot locator, selected enclosure breadcrumb, global safety/freshness | Exploded boards/controllers/modules; power rails, buses, USB paths and connector groups; quiet state on each child | Other enclosure internals; unrelated software and network detail |
| Device focus | Selected containment path and enclosure stage | Identity, stable ID, readiness chain, source/freshness per transition, upstream controller/host, downstream dependents, current measurements, permitted next steps | Raw payloads and full histories |
| Path trace | Physical target and readiness chain | One selected power, attachment, communication, or telemetry path; relation type on every edge; shared switch/domain warnings | Competing edge layers and unrelated normal paths |
| Evidence | Selected object/path, time range, source confidence, clock-correlation confidence | Synchronized measurements, commands, acknowledgements, observed power, messages/streams, events, logs, configuration, evidence gaps | Unrelated logs and unbounded platform telemetry |
| Change review | Platform/object identity, motivating fault, evidence summary, permission and safety state | Exact GPIO/runtime target, starting state, preconditions, dependents, expected interruption, request/acknowledgement/observation lifecycle, rollback and audit | Execution control until eligibility is proven; optimistic success |
| Verification | Same expanded enclosure, selected path, action state | Before/after readiness chain, expected-result checks, observed dependent recovery, remaining unknowns or faults | Resolved evidence detail unless reopened |

## 6. Information-disclosure model

### Glance: equipment posture

Show enclosure and module presence, one dominant abnormal zone, configuration
confidence, and freshness. Normal internals remain quiet.

### Focus: physical and functional readiness

Show the selected containment path, first failing or unknown transition,
relevant power/data attachments, and immediate dependents.

### Evidence: transition proof

Evidence is attached to a specific transition. Examples:

- `Powered`: switch request, controller acknowledgement, voltage/current, and
  device load;
- `Detected`: USB enumeration, CAN response, Ethernet link, ADC validity, or
  device identity;
- `Communicating`: message cadence, stream state, servo/FTDI response, or
  diagnostics;
- `Healthy`: thresholds, faults, temperature, calibration, and functional
  consumer state.

### Change: targeted intervention

The UI names the exact physical target and every shared dependency. GPIO 7,
for example, cannot be presented as an isolated motor-drive switch while its
reference mapping may also include the optional zippermast.

## 7. Platform-specific examples

### Camera that is powered but has no stream

The drive-camera module may show:

```text
Expected ✓  Installed ✓  Detected ✓  Powered ✓  Communicating ✕  Healthy —
```

The next disclosure follows Intel → switched USB3 → power injector → module
USB hub/PZIR/FTDI → camera. LED state remains a separate child path.

### Battery reading disagreement

Selecting the battery region separates BOTP cell-group voltages,
temperatures, and capacity estimate from motherboard input voltage/current and
charger power. The UI does not collapse these into one “battery current” value.

### Optional module absent

An unconfigured THK PTZ or zippermast appears as `Not expected`, not Offline or
Fault. If the configuration source is missing, it appears as `Expectation
unknown`, and downstream health is withheld.

### Gas detector problem

The focus path is detector → 4–20 mA channel → motherboard ADC/STM → Intel. It
shows installed detector identity and calibration only when authoritative data
exists; the reference list of possible detector models is not treated as the
installed inventory.

## 8. Flow invariants

- The active robot, safety state, freshness, permission, and hardware revision
  remain visible throughout.
- Zooming into an enclosure never loses the robot-level locator.
- `Expected`, `Installed`, `Detected`, `Powered`, `Communicating`, and `Healthy`
  are independent facts.
- Configuration mismatches are not automatically faults.
- A command request never changes the displayed physical state without an
  observation.
- Replacement and incompatibility constraints remain visible in configuration
  and change contexts.
- Selecting the same object from the equipment map, search, event, or evidence
  opens the same canonical identity.
- Evidence and Change preserve enclosure, object, transition, path, time range,
  and revision context.

## 9. Strengths

- Maps directly to the newly documented electrical enclosures, boards,
  controllers, switch channels, and configuration variants.
- Helps service engineers locate hardware and isolate the first failed
  readiness transition.
- Prevents absent optional hardware from appearing unhealthy.
- Makes measurement provenance and shared power domains difficult to overlook.
- Gives controlled actions precise physical scope and an observable result.
- Scales from robot to enclosure to connector without requiring every edge on
  one platform-wide topology.

## 10. Risks

- Approximate physical placement can be mistaken for mechanical or wiring
  precision; every view needs source/revision qualification.
- Maintaining enclosure geometry and option variants has a higher modelling
  cost than a list or abstract graph.
- Software, time, and external-integration causes may feel secondary unless
  the outward trace is strong.
- Deep containment may create excessive navigation if breadcrumbs, search, and
  cross-links are weak.
- The readiness chain depends on authoritative configuration and detection
  sources that are currently incomplete.
- A hardware-focused flow may be less efficient for cross-node performance or
  intermittent software incidents.

## 11. Unresolved questions

1. What source defines the current as-built configuration and hardware
   revision?
2. Which physical regions can be represented accurately without mechanical
   CAD or service-manual authority?
3. Which signals prove `Installed`, `Detected`, `Powered`, and
   `Communicating` for each object type?
4. Which switched domains expose observed voltage/current rather than only a
   command or acknowledgement?
5. How should connector aliases and board revisions retain stable identity?
6. Which optional-module combinations are valid beyond the documented THK
   PTZ/IR/FLIR constraints?
7. How much of the equipment map remains useful on a service tablet?

## 12. Evaluation criteria

Test whether an engineer can:

1. distinguish `not expected`, `not installed`, `not detected`, `not powered`,
   `not communicating`, and `faulted` without reading raw logs;
2. locate the electronics box, communication box, power injector, BOTP, motor
   drive, charger, and configured sensor/camera modules;
3. trace a selected device to its controller, switch channel, host, and
   software consumer;
4. explain the provenance of a battery, charger, power, or gas value;
5. see replacement, incompatibility, and shared-switch consequences before a
   change;
6. open transition-specific evidence without losing physical context;
7. verify an action through acknowledgement, electrical observation, device
   communication, and dependent recovery.

## 13. Relationship to other concepts

C01 preserves platform-wide causal continuity through stable dependency
geography. C02 instead preserves **physical containment and readiness
continuity** while zooming from robot to device. A later synthesis could use
C02 as a hardware-focused lens inside C01, but neither concept assumes that
merge.

