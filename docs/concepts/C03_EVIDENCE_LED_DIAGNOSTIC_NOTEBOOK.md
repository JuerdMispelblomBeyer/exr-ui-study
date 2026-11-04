# C03 — Evidence-led diagnostic notebook

**Status:** Exploratory concept; not approved product architecture
**Scope:** Internal robot-platform investigation, correlation, controlled
change, and verification for one robot
**Not in scope:** Fleet incident management, work queues, ticketing, missions,
autonomy, navigation, dispatch, or operator tasking

## 1. Core proposition

Start from an engineering question or observed symptom, not from a complete
system map. Build a time-scoped diagnostic notebook that keeps facts,
unknowns, evidence, hypotheses, changes, and verification criteria together.

The canonical sequence is:

```text
Notice → Frame → Correlate → Hypothesize → Prove → Change → Compare → Close
```

The continuity mechanism is the **investigation scope**:

- active robot;
- selected object or symptom;
- time range;
- relevant sources and filters;
- clock-correlation confidence;
- pinned facts and evidence gaps;
- action and expected result.

The notebook may be session-local. It is not automatically a persistent
incident or organizational workflow.

## 2. Problem this concept solves

Many engineering failures are intermittent, cross-domain, or ambiguous:

- a camera has power acknowledgement but no stream;
- motor commands remain high-frequency while feedback or odometry drops;
- BOTP capacity, motherboard input current, and charger power appear to
  disagree because they measure different things;
- CAN message rate changes near a container restart or clock-confidence loss;
- an optional module appears absent, but the expected configuration is unknown;
- symptoms appear on several dependents while one upstream source is stale.

A topology gives orientation, but an engineer testing a hypothesis often needs
time alignment, provenance, before/after comparison, and explicit evidence
gaps more than a persistent overview of every object.

## 3. Organizing and spatial model

The primary instrument is a **diagnostic notebook canvas** with four stable
strata:

1. **Question header** — robot, symptom/object, time range, freshness,
   correlation confidence, authority, and current investigation state.
2. **Fact and gap rail** — confirmed observations, unavailable/stale sources,
   affected objects, and recent changes.
3. **Synchronized evidence field** — aligned lanes for metrics, state changes,
   messages, diagnostics, events, logs, configuration, and action output.
4. **Hypothesis and verification rail** — candidate explanations, supporting
   or contradicting evidence, next test, expected result, and completion
   criteria.

A compact dependency mini-map appears only for the selected causal path. The
full platform topology is available as context, but it is not the default
canvas.

## 4. Conceptual user flow

1. Open one robot and verify identity, connection, freshness, permission, and
   persistent safety state.
2. Enter through a current abnormal observation, a recent change, a search
   result, or a plain-language/object-ID engineering question.
3. Frame the investigation by confirming object scope and time range. The UI
   states which evidence sources can be correlated and which are stale,
   missing, or unsynchronized.
4. Assemble suggested evidence lanes from the selected object's relationships
   without claiming a root cause.
5. Read confirmed facts and gaps before creating or accepting a hypothesis.
6. Add, edit, or reject candidate explanations. Each hypothesis names the
   observation that would support or contradict it.
7. Pin relevant trace intervals, messages, events, logs, configuration values,
   and dependency paths. Raw evidence keeps source, timestamp, units, validity,
   and parser state.
8. If an allowed change or diagnostic test is justified, carry the motivating
   evidence, expected result, preconditions, consequences, rollback, and audit
   into Change.
9. Keep request, acknowledgement, observed electrical/runtime result, and
   downstream recovery on the same time field.
10. Compare before and after against the declared verification criteria.
11. Close with one of three outcomes: proven cause, disproven hypothesis, or
    unresolved because named evidence is unavailable.

## 5. What is visible when

| Moment | Always visible | Newly visible | Deliberately hidden or collapsed |
| --- | --- | --- | --- |
| Notebook landing | Robot identity, connection/freshness, persistent safety state, search/question entry, current clock confidence | Highest-impact observations, stale/missing-source summary, recent platform changes, resumable local investigations if supported | Full topology, every metric, unfiltered logs, change controls |
| Investigation framing | Robot, safety, selected symptom/object | Time range, affected object set, relevant dependency mini-path, available evidence sources, expected cadences, correlation confidence, known gaps | Root-cause assertions and irrelevant domains |
| Evidence assembly | Question header, time range, source confidence | Suggested synchronized lanes; facts/gaps rail; recent changes; raw-versus-derived labels | Sources outside scope; misleading event ordering when clocks are unreliable |
| Hypothesis work | Facts, gaps, mini-path and evidence field | Candidate explanation, confidence owner, supporting/contradicting pins, next test, falsification condition | Automatic promotion of a hypothesis to fact |
| Raw proof | Selected hypothesis/question and synchronized time cursor | Exact CAN frames/rates, GPIO request/ack/observation, power values, USB/stream state, BOTP/charger data, diagnostics, logs, configuration, units and timestamps | Decorative summaries and unrelated raw volume |
| Change or diagnostic test | Motivating evidence, hypothesis, object scope, time window, permission and safety state | Eligibility, target, preconditions, expected disruption, expected measurement change, request/acknowledgement/observation lifecycle, rollback and audit | Execution until scope and success criteria are explicit |
| Verification comparison | Same question, evidence lanes, action marker | Before/after windows, expected versus observed result, dependent recovery, regressions, remaining gaps | A success label based only on command transmission |
| Close or handoff | Robot/object/time scope and conclusion status | Proven/disproven/unresolved result, cited evidence pins, missing-source list, deep link if supported | Unbounded narrative, credentials, or unrelated platform data |

## 6. Evidence-lane grammar

Lanes are assembled from the functional path under investigation. Possible
lanes include:

- **Power and battery:** BOTP cell-group voltage/temperature/capacity,
  motherboard input voltage/current, charger transmitter/receiver states and
  transmitted power;
- **Switch lifecycle:** requested GPIO state, controller acknowledgement,
  observed voltage/current, device detection, communication, and health;
- **CAN:** expected message presence/rate, response time, errors/load, motor
  settings/speed, feedback and odometry;
- **Camera and peripheral:** USB enumeration, power-injector state, FTDI/LED,
  servo response, stream state, and consuming software;
- **Compute and software:** CPU/GPU/memory/storage, containers, restarts,
  diagnostics, ROS 2/DDS graph, and service dependencies;
- **Connectivity:** WiFi/cellular, VRRP ownership, LAN interfaces, Tailscale,
  latency, errors, drops, and external integration;
- **Time:** chrony state, offset, uncertainty, and source reachability;
- **Change:** deployment, configuration, power command, restart, recovery, and
  audit events.

The notebook does not show every lane at once. It begins with the smallest set
that can answer the framed question and makes omitted evidence discoverable.

## 7. Fact, inference, and hypothesis model

The notebook uses three visibly different statement types:

- **Fact:** a current or historical observation with source, time, units, and
  validity;
- **Derived state:** a rule-backed health or impact conclusion with the inputs
  that produced it;
- **Hypothesis:** an engineer- or system-proposed explanation that remains
  provisional until its support and contradiction criteria are evaluated.

Confidence never substitutes for missing evidence. A hypothesis may be marked
`unsupported`, `consistent`, `contradicted`, or `proven under defined
criteria`; it may not overwrite the underlying facts.

## 8. Platform-specific examples

### Camera power acknowledged, stream absent

The notebook aligns:

```text
GPIO request → acknowledgement → observed power → USB detection → FTDI state
→ camera stream → consuming service
```

Possible hypotheses such as `USB3 path disabled`, `camera not enumerated`, or
`consumer unhealthy` remain separate until evidence supports one.

### Motor feedback dropout

The evidence field places high-frequency speed commands, motor feedback and
odometry, CAN errors/load, motor-drive protection state, Intel load, container
events, and chrony confidence on one time axis. Drive Stall remains visible as
a distinct latched state rather than being inferred from current overload.

### Battery and charger discrepancy

The question header names the measurement being tested. Separate lanes prevent
BOTP capacity, motherboard input current, receiver current, transmitter
current, and transmitted power from being treated as equivalent values.

### Absent optional hardware

The notebook adds configuration expectation as an evidence lane. If the
as-built source is missing, the conclusion is `installation expectation
unknown`, not `device offline`.

## 9. Flow invariants

- Robot identity, safety state, freshness, permission, time range, and clock
  confidence remain visible throughout.
- Every evidence item retains source, timestamp, units, validity, and parsing
  state.
- Stale or unsynchronized data visibly weakens causal ordering.
- Facts, derived state, and hypotheses never share the same presentation.
- Opening raw evidence does not reset the question, object, path, filters, or
  time cursor.
- Entering Change preserves the motivating evidence and explicit expected
  result.
- Request, acknowledgement, observed result, and dependent recovery are
  separate events on the same time field.
- An unresolved investigation names the missing evidence rather than forcing a
  conclusion.
- Handoff links, if supported, remain scoped to one robot and contain no
  credentials or sensitive payloads.

## 10. Strengths

- Excellent for intermittent, multi-domain, and before/after investigations.
- Makes time quality, evidence provenance, and missing sources impossible to
  treat as footnotes.
- Supports rigorous falsification instead of a premature “root cause” label.
- Keeps change motivation, action lifecycle, and verification in one record.
- Adapts to hardware, CAN, compute, software, network, and time questions
  without requiring a different dashboard for each domain.
- Can produce a precise handoff between engineers without becoming fleet or
  ticket management.

## 11. Risks

- Requires mature timestamps, source identity, cadence contracts, and clock
  health; several are currently unknown.
- A blank question-first canvas may be intimidating without strong issue,
  object, and search entry points.
- Too many suggested lanes or hypotheses can increase cognitive load.
- The notebook metaphor can drift into incident management, collaboration, or
  persistent task tracking outside the product boundary.
- Engineers may lose physical orientation unless the selected dependency
  mini-map and object identity remain clear.
- Storing notebooks or evidence pins introduces retention, privacy, and audit
  questions.
- Automated hypothesis suggestions risk overclaiming causality.

## 12. Unresolved questions

1. Are investigations session-local, shareable deep links, or persisted
   diagnostic records?
2. Which metric, event, log, CAN, GPIO, camera, and configuration sources have
   authoritative timestamps and expected cadences?
3. What chrony-confidence threshold permits causal ordering?
4. How are evidence pins retained without copying credentials or sensitive
   payloads?
5. Who may add, approve, or close a hypothesis and conclusion?
6. Which diagnostic tests are read-only, which are consequential changes, and
   which require recovery or safety authority?
7. How many simultaneous lanes remain usable at reference desktop and service
   tablet sizes?
8. What minimum evidence qualifies a cause as proven rather than merely
   consistent?

## 13. Evaluation criteria

Test whether an engineer can:

1. frame a specific question in one robot/object/time scope;
2. see stale, missing, and unsynchronized evidence before reading a causal
   story;
3. distinguish facts, derived health, and hypotheses;
4. align a physical measurement, CAN/USB event, software change, and dependent
   symptom without reconstructing filters;
5. prove or reject a camera, motor, battery, network, or software hypothesis;
6. execute an eligible test/change with explicit expected evidence;
7. compare before and after without treating acknowledgement as recovery;
8. close or hand off an unresolved investigation with its evidence gaps intact.

## 14. Relationship to other concepts

C01 uses stable platform topology as the continuity mechanism. C02 uses
physical containment and readiness. C03 uses a **time-scoped engineering
question and its evidence set**. A later product could link between these
views, but C03 remains a complete alternative flow for evaluation rather than
an assumed drawer inside C01.

