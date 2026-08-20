# Engineering interface functional requirements

**Status:** Evolving baseline  
**Version:** 0.1  
**Date:** 2026-08-20  
**Scope:** One connected robot's platform layer  
**Design basis:** Implemented Figma flow `Inspect → Diagnose → Change`

## 1. Purpose

This document is the durable functional overview for the ExRobotics internal
engineering interface. It defines what engineers must be able to observe,
understand and deliberately change. It is intentionally extensible: new
platform capabilities should be added here before they become screen-specific
content.

The interface covers compute, storage, networks, CAN, hardware subsystems,
software runtimes, middleware, diagnostics, evidence and authorized platform
actions. It does not cover fleet operations, missions, autonomy, SLAM,
navigation or dispatch.

The words **must**, **should** and **may** indicate required, recommended and
optional behaviour. A requirement marked **pending source** still describes a
UI need, but its authoritative data source, threshold or action path has not
yet been established.

## 2. Requirement and truth model

Each functional requirement must eventually identify:

- the platform object and stable ID;
- the authoritative observation or command source;
- health logic and thresholds;
- expected update cadence and stale window;
- dependency and impact relationships;
- permission and action authority;
- evidence available for diagnosis;
- request, acknowledgement and observed-result semantics for actions.

Facts supplied by a platform owner are **stated**. Values confirmed against a
runtime, manifest or implementation are **verified**. Missing details remain
**unknown** and must not be filled in merely to complete a screen.

## 3. Implemented component baseline

The requirements use the new Figma layout as their presentation grammar.

| Component or pattern | Figma reference | Functional role |
| --- | --- | --- |
| Global header | implemented screen pattern | Active robot, freshness, user authority and provisional Safety Stop |
| Task Rail Item | `46:479` | Move through Inspect, Diagnose and Change without changing platform scope |
| Lens Chip | `46:484` | Apply Physical, Network, Software, Time or Integration emphasis to the stable map |
| System Node | `46:467` | Name, health, object kind and one glance signal |
| Platform map | implemented screen pattern | Stable physical and logical geography plus highlighted dependency paths |
| Attention Rail | `46:485` | Highest-priority condition, impact, confidence and one next action |
| Comparison strip | implemented screen pattern | Aligned comparison across compute nodes, subsystems or software objects |
| Recent changes | implemented screen pattern | Relevant deployments, restarts, state changes and operator actions |
| Evidence Strip | `46:495` | Compact indication of evidence availability, freshness and gaps |
| Evidence Drawer | `47:1023` reference state | Causal chain, synchronized metrics, events, logs and raw evidence |
| Change review | `47:1771` reference state | Scope, preconditions, impact, acknowledgement, result and rollback |
| Stale encoding | `47:1957` reference state | Last-seen time, reduced confidence, muted object and dashed unknown boundary |

### Disclosure contract

1. **Glance:** every visible object gets its name, health and one useful signal.
2. **Focus:** selection adds exact state, key telemetry, dependencies and
   available actions in the Attention Rail.
3. **Evidence:** the drawer reveals synchronized metrics, logs, events,
   diagnostic payloads and causal hypotheses.
4. **Change:** the UI shows eligibility, scope, preconditions, request,
   acknowledgement, observed result, audit and rollback as distinct facts.

The map does not rearrange when a lens or state changes. Yellow marks selection
or deliberate action. Orange marks degraded or caution state. Red marks a
confirmed fault. Grey/dashed treatment marks unknown, stale or disconnected
state. State must also be stated in text.

## 4. Cross-cutting functional requirements

### Context, identity and freshness

- **FR-CTX-001 — Active platform:** the header must identify the active robot
  and preserve that identity through Inspect, Diagnose and Change.
- **FR-CTX-002 — Object identity:** every inspectable object must expose a
  human name, stable ID, type, parent scope and responsible owner when known.
- **FR-CTX-003 — Source:** every derived state must expose its authoritative
  source or clearly state that the conclusion is inferred.
- **FR-FRESH-001 — Observation time:** every health-bearing observation must
  carry an observation time and expected cadence.
- **FR-FRESH-002 — Stale state:** an observation older than its validity
  window must become `Stale`; the previous value must not remain visually
  current.
- **FR-FRESH-003 — Missing data:** missing data must name the missing source and
  which conclusions or dependents are affected.
- **FR-TIME-001 — Correlation confidence:** cross-source evidence must expose
  chrony/clock confidence when ordering events depends on synchronized time.

### Health, impact and attention

- **FR-HEALTH-001 — Common vocabulary:** objects must use Healthy, Degraded,
  Fault, Unknown, Offline or Stale with a textual explanation.
- **FR-HEALTH-002 — Fact versus inference:** raw facts, computed health and
  working hypotheses must remain distinguishable.
- **FR-HEALTH-003 — No false healthy:** `no reported faults` must not be
  presented as Healthy unless required observations are present and current.
- **FR-IMPACT-001 — Dependency impact:** abnormal state must identify affected
  downstream objects and functions, not only the source alarm.
- **FR-IMPACT-002 — Causal grouping:** repeated symptoms should roll up under
  one causal object when supported by evidence.
- **FR-ATTN-001 — One attention owner:** the Attention Rail must show the most
  consequential current issue, selected object or unresolved action.
- **FR-ATTN-002 — Priority:** ranking should consider platform impact,
  operational urgency, confidence, freshness and recency.

### Evidence and navigation

- **FR-EVID-001 — Preserved scope:** opening evidence must preserve the active
  platform, object, lens, time range and filters.
- **FR-EVID-002 — Synchronized evidence:** related metrics, diagnostics, logs
  and events should share one time range and correlation marker.
- **FR-EVID-003 — Gaps:** the Evidence Strip must show unavailable, stale or
  discontinuous sources before the drawer is opened.
- **FR-EVID-004 — Provenance:** raw observations must retain source object,
  timestamp, units and parsing/validity state.
- **FR-NAV-001 — Stable selection:** selecting the same object in a node,
  comparison, event or trace must produce the same focused context.
- **FR-NAV-002 — Deep link:** platform, object, lens, time range and relevant
  filters should be linkable for handoff between engineers.

### Actions, permissions and audit

- **FR-ACT-001 — Eligibility:** a control must expose support, permission,
  connection, current state and blocking preconditions before execution.
- **FR-ACT-002 — Explicit scope:** every consequential action must name the
  affected robot and object or power domain.
- **FR-ACT-003 — Lifecycle:** requested, acknowledged, observed, rejected,
  timed out and unconfirmed are separate states.
- **FR-ACT-004 — No optimistic success:** command transmission alone must not
  be shown as a successful physical or runtime result.
- **FR-ACT-005 — Concurrency:** an unresolved action must remain visible when
  the user changes lens or evidence view; conflicting actions must be blocked
  or explicitly reconciled.
- **FR-ACT-006 — Rollback:** reversible changes should state the rollback path
  and whether rollback is currently available.
- **FR-AUTH-001 — Permissions:** read, diagnose, change, recovery and safety
  authority may differ and must be displayed when relevant.
- **FR-AUDIT-001 — Audit record:** actions must retain requester, role, client,
  platform, scope, request ID, starting state, request time, acknowledgement,
  observed result and failure reason.

## 5. Motor drive and Drive Stall

### Stated behaviour

`Drive Stall` is activated after a motor overload and remains active until it
is manually deactivated. It is a latched motor-protection condition. Its exact
controller, authority, clearing mechanism and safety classification are still
unknown.

Drive Stall must remain separate from the provisional `Safety Stop` function.
Clearing Drive Stall must not imply release, reset or restart of any safety
function, and it must not automatically command motion.

### Required object state

- **FR-STALL-001 — Visibility:** Drive Stall must be visible on the motor-drive
  System Node and in the global attention hierarchy whenever active.
- **FR-STALL-002 — Latched state:** the UI must show that Drive Stall remains
  active after the overload observation has ended.
- **FR-STALL-003 — Trigger evidence:** focus/evidence must show the overload
  source, affected motor/channel if available, trigger time and peak/threshold
  evidence when supplied by the controller.
- **FR-STALL-004 — Current condition:** the UI must distinguish `overload still
  present` from `overload no longer present; stall remains latched`.
- **FR-STALL-005 — Impact:** the UI must state whether drive output is
  inhibited, reduced or unavailable and which dependents are affected.
- **FR-STALL-006 — Freshness:** stall state and recovery eligibility must carry
  source and age; stale state cannot be used to imply that recovery is safe.

### Manual deactivation

- **FR-STALL-007 — Manual recovery:** Drive Stall must never clear
  automatically in the UI merely because current falls or the page reloads.
- **FR-STALL-008 — Mechanism pending:** until confirmed, `manual deactivation`
  means an intentional authorized action; it does not prove that remote UI
  deactivation is permitted.
- **FR-STALL-009 — Eligibility:** a deactivation control, if supported, must
  show authority, controller reachability, overload-cleared status and other
  authoritative prerequisites.
- **FR-STALL-010 — Review:** the Change view must name the motor-drive scope,
  current latched state, expected effect, unavailable functions and whether a
  separate enable/restart step will still be required.
- **FR-STALL-011 — Result:** after a request, the UI must wait for an
  authoritative `Drive Stall inactive` observation before declaring success.
- **FR-STALL-012 — Failure:** rejection, timeout, lost connection or a
  reappearing overload must leave a prominent unresolved state and evidence.
- **FR-STALL-013 — Audit:** activation and every deactivation attempt must be
  separately recorded.
- **FR-STALL-014 — No implicit restart:** deactivation must not restart or
  enable motion unless a separately specified, permitted and acknowledged
  action explicitly does so.
- **FR-STALL-015 — Safety distinction:** Safety Stop state and Drive Stall state
  must be simultaneously representable without ambiguous `Stopped` copy.

### Component mapping

- System Node: `Drive Stall active` as the one glance signal.
- Platform map: orange motor-drive state and highlighted Intel → CAN → motor
  dependency path.
- Attention Rail: trigger, current overload condition, impact and recovery
  entry point.
- Evidence Drawer: overload/current trace, controller diagnostic, CAN events,
  activation time and related changes.
- Change review: manual-deactivation eligibility, acknowledgement, observed
  inactive state and any separate enable step.

## 6. Common software-subsystem requirements

Every software subsystem—POI Capture, CAN, API Agent, Cybersecurity and
ROS 2/DDS middleware—must use one consistent object contract.

- **FR-SW-001 — Identity:** subsystem name, stable ID, owner and purpose.
- **FR-SW-002 — Placement:** compute node, container/process, image/build and
  runtime version.
- **FR-SW-003 — Lifecycle:** expected, starting, healthy, degraded, failed,
  stopped, restart-loop, unknown and stale states as applicable.
- **FR-SW-004 — Resource context:** CPU, memory, GPU, network and storage
  contribution where available.
- **FR-SW-005 — Dependencies:** upstream inputs, downstream consumers,
  middleware, databases, devices and external integrations.
- **FR-SW-006 — ROS diagnostics:** each software subsystem must expose its ROS
  2 diagnostics roll-up and individual diagnostic entries when available.
- **FR-SW-007 — Diagnostics contract:** diagnostic name, level, message,
  hardware ID, key/value fields, source node and timestamp must be retained.
- **FR-SW-008 — Evidence:** recent state transitions, restarts, diagnostic
  changes, logs and relevant traces.
- **FR-SW-009 — Actions:** only supported actions are shown; restart, reset,
  reload or reconfigure must each use the standard action lifecycle.
- **FR-SW-010 — Aggregation:** top-level health must name the child component
  responsible for degradation and cannot hide unknown children.

## 7. POI Capture System

### Object model

POI Capture is a top-level software subsystem containing or depending on:

- the drive and inspection cameras;
- microphone input;
- POI manager nodes;
- the top-level POI component;
- data used to construct or enrich POIs;
- the POI database.

Exact manager-node names, microphone attachment, data schema, storage engine,
host placement and pipeline stages remain unknown.

### Functional requirements

- **FR-POI-001 — Top-level posture:** the Software lens must show one POI
  Capture System Node with rolled-up state, last successful capture and the
  responsible degraded child when applicable.
- **FR-POI-002 — Pipeline topology:** focus must visualize capture inputs →
  manager nodes → top-level POI component → database/consumers.
- **FR-POI-003 — Input state:** every camera and microphone input must show
  expected/present, connection, freshness and current data validity.
- **FR-POI-004 — Capture health:** expose capture attempts, successes,
  failures, last success, in-progress work and backlog/queue depth when those
  concepts exist.
- **FR-POI-005 — Data used by POIs:** the UI must list the input datasets or
  streams used by a selected POI, their source, freshness and availability.
- **FR-POI-006 — Data gaps:** missing input must name affected POI outputs and
  whether capture can continue in a degraded mode.
- **FR-POI-007 — Manager nodes:** expose expected versus discovered manager
  nodes, host/container, lifecycle, diagnostics and dependencies.
- **FR-POI-008 — Database health:** expose reachability, read/write health,
  error state, last successful operation and storage pressure.
- **FR-POI-009 — Database errors:** focus/evidence must show error class,
  affected operation, count/rate, first/last occurrence and correlated logs
  without exposing credentials or sensitive content.
- **FR-POI-010 — Record posture:** show counts or age distributions only when
  they answer an engineering question; do not turn this into POI content
  management.
- **FR-POI-011 — Media evidence:** diagnostic previews may be shown for capture
  verification, but the interface must not become a teleoperation or mission
  view.
- **FR-POI-012 — Correlation:** POI capture evidence must warn when camera,
  microphone, manager and database timestamps cannot be reliably correlated.

### Recommended visual instruments

- top-level POI System Node on the Software lens;
- compact pipeline/dependency stage after selection;
- input presence matrix for both cameras and microphone;
- capture-success/backlog trace;
- database operation/error instrument;
- ROS diagnostics list grouped by child node;
- synchronized evidence drawer for a selected failed capture.

## 8. CAN software subsystem

The CAN view must combine physical bus health, expected message behaviour and
subsystem responsiveness. A healthy interface alone does not prove that all
required messages are present at the correct rate.

- **FR-CAN-001 — Message inventory:** expose expected CAN messages using stable
  identifiers and human labels when definitions exist.
- **FR-CAN-002 — Availability:** show expected versus observed messages and
  explicitly identify missing or unexpected messages.
- **FR-CAN-003 — Proper rate:** compare observed message rate with the expected
  rate or accepted range for every expected message.
- **FR-CAN-004 — Rate confidence:** rate conclusions must show observation
  window, sample count and freshness in evidence.
- **FR-CAN-005 — Message matrix:** Glance/Focus should use an aligned matrix for
  availability and cadence rather than one card per message.
- **FR-CAN-006 — Bus state:** expose controller/interface state, bus load,
  error frames, dropped frames, error-passive/bus-off state and recovery when
  available.
- **FR-CAN-007 — Subsystem response time:** show response time per Charging,
  Battery, Motor Drive, Power GPIO and Gas ADC subsystem.
- **FR-CAN-008 — Response expectation:** compare response time with a named
  expected limit and distinguish timeout, late response and unknown cadence.
- **FR-CAN-009 — Gateway dependency:** show that CAN observations report
  through the Intel computer and name lost conclusions if that gateway is
  unavailable.
- **FR-CAN-010 — Child impact:** message or response degradation must name the
  affected physical subsystem and function.
- **FR-CAN-011 — Evidence:** allow synchronized inspection of message rate,
  response latency, bus errors, controller diagnostics and relevant logs.
- **FR-CAN-012 — Definitions:** bitrate, node IDs, expected messages/rates and
  response limits remain pending authoritative configuration.

## 9. API Agent

- **FR-API-001 — Identity and placement:** show API Agent version, host,
  container/process and ownership.
- **FR-API-002 — Connection:** expose reachability to its external endpoint,
  authentication state without secrets, last successful exchange and current
  connection mode.
- **FR-API-003 — Traffic posture:** show request/response rate, in-flight or
  queued work, response latency and error/timeout rate where available.
- **FR-API-004 — Contract health:** expose incompatible version/schema or
  rejected request conditions separately from network failures.
- **FR-API-005 — Dependencies:** show compute, container, DNS/network,
  Tailscale/uplink and external-integration dependencies.
- **FR-API-006 — Boundary:** the UI may inspect the on-board agent/API path but
  must not expose fleet inventory, dispatch or mission workflows.
- **FR-API-007 — Evidence:** correlate connection transitions, API errors,
  restarts and network path changes.

## 10. Cybersecurity monitoring

- **FR-CYBER-001 — Unauthorized attempts:** expose unauthorized login attempts
  as security observations with count, rate, first/last time, target service,
  outcome and source identity/address when policy permits.
- **FR-CYBER-002 — Current posture:** distinguish a rejected attempt from a
  successful unauthorized login or an unverified anomaly.
- **FR-CYBER-003 — Aggregation:** repeated attempts should be grouped by
  relevant source/target/time window while retaining access to individual
  evidence.
- **FR-CYBER-004 — Correlation:** correlate attempts with API Agent, SSH or
  other authentication service health, network path and relevant container.
- **FR-CYBER-005 — Sensitive data:** never expose passwords, tokens, session
  secrets or unnecessary personal data in tiles, logs or exports.
- **FR-CYBER-006 — Attention:** security observations enter the Attention Rail
  according to verified consequence, confidence and recency; attempt count
  alone must not automatically imply platform compromise.
- **FR-CYBER-007 — Actions:** block, revoke or isolate controls must not be
  invented. Show them only after authority, scope, side effects and rollback
  are specified.
- **FR-CYBER-008 — Evidence:** preserve source, target, auth method, decision,
  timestamp, correlation ID and log provenance where available.

## 11. ROS 2 and DDS middleware

- **FR-MW-001 — Graph:** expose expected and discovered ROS 2 nodes,
  publishers, subscribers, services/actions and their compute/container
  placement.
- **FR-MW-002 — DDS participants:** expose participant discovery, reachability
  and domain identity without conflating DDS participants with containers.
- **FR-MW-003 — Topic health:** show expected versus observed publishers and
  subscribers, message rate, freshness and last message.
- **FR-MW-004 — QoS:** identify incompatible or unexpected reliability,
  durability, history, deadline and liveliness settings when observable.
- **FR-MW-005 — Delivery quality:** expose deadline misses, liveliness loss,
  dropped samples and latency where the middleware provides them.
- **FR-MW-006 — Discovery:** distinguish discovery failure from an application
  node that was never expected or is intentionally stopped.
- **FR-MW-007 — Per-subsystem diagnostics:** group ROS diagnostics under their
  owning software subsystem while retaining the source ROS node.
- **FR-MW-008 — Cross-layer path:** allow an engineer to follow software
  subsystem → ROS node/topic → DDS participant → container → compute → LAN.
- **FR-MW-009 — Scale:** use matrices, filtered graphs and ranked exceptions;
  do not render an unreadable complete ROS graph at Glance.
- **FR-MW-010 — Evidence:** synchronize diagnostics transitions, topic-rate
  traces, DDS discovery events and container/network changes.

## 12. Compute, network and storage observability

### Compute

- **FR-SYS-001 — CPU:** show overall and per-node CPU utilization; per-core,
  load, frequency, temperature and throttling belong in Focus/Evidence when
  available.
- **FR-SYS-002 — GPU:** show utilization, memory use, temperature, power and
  throttling for each Jetson/NVIDIA accelerator when available.
- **FR-SYS-003 — Attribution:** correlate sustained CPU/GPU pressure with the
  responsible containers/processes and affected software subsystems.
- **FR-SYS-004 — Comparison:** compare Intel, Jetson 1 and Jetson 2 on aligned
  time windows and units.

### Network throughput

- **FR-NET-001 — Throughput:** show receive/transmit throughput per relevant
  interface and aggregate node throughput.
- **FR-NET-002 — Quality:** pair throughput with link state, negotiated speed,
  errors, drops, loss and latency where available.
- **FR-NET-003 — Path:** relate interface traffic to LAN, WiFi, 4G/5G,
  Tailscale and VRRP ownership without claiming packet attribution that is not
  observed.
- **FR-NET-004 — Expected range:** thresholds must be source-specific; high
  throughput alone is not necessarily degraded.

### System storage

- **FR-STOR-001 — Inventory:** show filesystems/volumes, mount point, capacity,
  used, free and reserved space per compute node.
- **FR-STOR-002 — Pressure:** show warning/fault thresholds, projected
  exhaustion only if a valid model exists, and which services are affected.
- **FR-STOR-003 — I/O health:** expose read/write throughput, latency, errors,
  read-only remount and device/SMART health when available.
- **FR-STOR-004 — Ownership:** identify major container, log, database or POI
  data consumers when attribution exists.
- **FR-STOR-005 — Database relation:** POI database storage pressure must roll
  up into POI Capture health without duplicating the same causal issue.
- **FR-STOR-006 — Actions:** cleanup, pruning or remount controls require
  explicit scope, preview, permissions, acknowledgement and audit; none are
  assumed today.

## 13. View composition by task

### Inspect

- The stable map shows hardware, network and selected software-domain nodes.
- Lens selection changes edge and object emphasis, not object position.
- The comparison strip adapts to compute resources, link throughput, CAN
  response, container distribution or clock offset.
- Healthy domains collapse to one quiet signal. Abnormal, stale and unknown
  domains receive area according to impact.

### Diagnose

- Selecting Drive Stall, a failed POI capture, a CAN message-rate problem, an
  API error or a ROS diagnostic opens the same object context.
- The Attention Rail states the fact, impact, confidence and next evidence
  step.
- The Evidence Drawer aligns relevant telemetry, diagnostics, events, logs and
  recent changes on one time axis.
- Working hypotheses are labelled and never replace raw observations.

### Change

- Only an eligible, supported action enters Change.
- The review identifies exact platform/object scope, current state,
  preconditions, expected temporary unavailability and downstream impact.
- Request, acknowledgement and observed result remain visible until resolved.
- Recovery or deactivation must not implicitly restart motion or services.

## 14. Initial acceptance scenarios

1. An engineer can see `Drive Stall active` and the affected motor-drive/CAN
   path without opening logs.
2. The interface continues to show Drive Stall after overload current returns
   to normal and identifies that manual deactivation is required.
3. A deactivation attempt cannot appear successful until the authoritative
   stall state becomes inactive.
4. A POI capture failure identifies whether camera, microphone, manager node,
   input data or database is the responsible child.
5. A POI database error exposes operation, time, rate and storage context
   without exposing credentials or POI content unnecessarily.
6. The CAN matrix shows whether all expected messages are present and at their
   proper rates, and compares subsystem response times.
7. An API Agent failure can be separated into runtime, authentication,
   contract, VPN/uplink and external-endpoint causes.
8. Unauthorized login attempts are visible without presenting rejected
   attempts as a confirmed compromise.
9. A ROS 2 subsystem degradation can be followed through diagnostics, topic,
   DDS participant, container, compute node and LAN.
10. CPU/GPU pressure can be attributed to a runtime and related to a degraded
    software subsystem.
11. Network throughput can be compared with link quality and current VRRP
    ownership.
12. Storage pressure identifies affected compute node, filesystem and major
    consumer, including a POI database dependency where relevant.
13. Stale diagnostics reduce health confidence rather than leaving the last
    green state visible.
14. Safety Stop and Drive Stall can be simultaneously represented with
    distinct state and recovery language.

## 15. Priority unknowns

1. Which controller and signal authoritatively activate and clear Drive Stall?
2. Does `manually deactivated` mean a local physical action, an authorized UI
   command, or either under defined conditions?
3. What prerequisites block Drive Stall deactivation, and is a separate drive
   enable/restart action required afterward?
4. What are the exact POI manager nodes, top-level component, data inputs,
   microphone path, database technology and host placement?
5. Which CAN definition source supplies expected messages, rates, IDs,
   response limits and bus thresholds?
6. Where does the API Agent run, which endpoint/contract does it implement and
   what authentication state is safely observable?
7. Which services produce unauthorized-login observations and what retention,
   privacy and response policy applies?
8. Which ROS 2 distribution, DDS implementation/domain and diagnostics
   conventions are used?
9. Which metric sources and thresholds apply to CPU, GPU, network and storage?
10. Which actions are supported, reversible and permitted for each software
    subsystem?

## 16. Extension template

For each future capability, add:

```text
Capability / stable ID:
Purpose and owner:
Objects and dependencies:
Required glance signal:
Health states and thresholds:
Source, cadence and stale window:
Focus metrics and diagnostics:
Evidence and correlation needs:
Supported actions and permissions:
Acknowledgement / observed result:
Audit and retention:
Unknowns:
Acceptance scenario:
```

Update `data/platform-system.yaml` when the addition changes the factual
inventory or relationships. Update this document when it changes what the UI
must do. Update the visualization or design guides only when it establishes a
new reusable presentation rule.
