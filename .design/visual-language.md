# ExRobotics platform interface — visual language

**Direction:** Signal Instrumentation  
**Product:** internal robot-platform engineering interface  
**Scope:** compute, software runtimes, LAN/CAN, onboard subsystems, connectivity,
time synchronization, evidence, configuration, and controlled safety actions  
**Out of scope:** fleet management, missions, autonomy, SLAM, navigation,
teleoperation, and geographic tracking

> **Status note, 2026-08-23.** This document remains the direction for the
> system as a whole, but the dark expression has moved ahead of it in three
> places. Semantic state (§5.2–5.3), surface hierarchy (§7) and instrument
> grammar (§2.5, §8.4) are now governed for dark by decisions D030–D034 and by
> `docs/DESIGN_GUIDELINES.md` sections 18a, 19a, 20a and 6.2a. Where they
> disagree, the decisions win for dark; this document still governs light.

## 1. Design thesis

The ExRobotics interface is a **living technical chassis**: a stable visual model
of the robot platform with evidence attached to real objects and paths.

It should feel:

- calm enough for long engineering sessions;
- exact enough to be trusted during diagnosis;
- spatial enough that the user can see where a problem lives and how it
  propagates;
- dense enough to answer the first question without opening five pages;
- consequential when an action or fault matters;
- unmistakably ExRobotics without looking theatrical or “sci-fi.”

It should look like modern engineering equipment translated into software: a
bounded chassis, joined low-relief work surfaces, precise internal instruments,
truthful system imagery, and a scarce yellow current signal.

The desired impression is **refinery instrument, not command-center fantasy;
working product, not portfolio mockup; system model, not card catalog**.

## 2. What makes the language distinctive

Every primary screen must express at least four of the following five
signatures. A technically correct screen that does not express them is not
visually complete.

### 2.1 Stable platform field

The main visual object is the robot’s stable platform geography—not a row of
summary cards. Intel, Jetson 1, Jetson 2, LAN, the Intel-attached CAN branch,
CAN-side subsystems, cameras, uplinks, VPN overlay, and external integration
retain consistent locations across related views.

The field is both overview and navigation. Health appears on the represented
object or path. Selecting an issue focuses the responsible object without
destroying the surrounding mental map.

### 2.2 Yellow current probe

ExRobotics yellow behaves like an optical current or measurement probe. It
marks one coherent current context:

- selected object or route;
- active signal path;
- current sample or time position;
- primary deliberate action;
- current navigation scope.

Small yellow marks may repeat when they refer to that same context. They must
not become unrelated decorative accents.

### 2.3 Attached diagnostic lens

Selected detail does not appear as an arbitrary floating card. It is an
**attached lens**: an inspector, tooltip, callout, or expanded instrument with a
visible spatial or logical relationship to the selected node, path, event, or
sample.

The lens may float one level above the chassis, but its connector, alignment,
focus bracket, or shared datum must make ownership explicit.

### 2.4 Evidence datum

Time, causality, and evidence share a continuous datum. A visible probe can
synchronize traces, logs, CAN messages, container events, chrony confidence,
and configuration changes. Dense evidence gathers around the selected moment;
unselected history remains compressed.

### 2.5 Calibrated instrument grammar

Values, paths, marks, and surfaces use a recognizable technical grammar:

- fine shared dividers rather than repeated card shadows;
- inset plots and matrices;
- exact ticks, units, thresholds, source, and freshness;
- monospaced machine identity;
- small focus brackets or reticles only where real interaction exists;
- soft outer enclosure with harder internal measurement geometry.

This grammar—not yellow alone—must make the product recognizable in greyscale.

## 3. Composition operating system

### 3.1 Begin with the engineering question

Before composing a screen, write its dominant question in one sentence. Examples:

- “Which platform object is causing the current degradation?”
- “Is message availability and rate healthy across the CAN subsystem?”
- “Which compute node or container is driving resource pressure?”
- “Which uplink owns the route, and did failover occur cleanly?”
- “What caused Drive Stall, and is manual deactivation permitted?”

The largest visual region must answer that question. If the largest region is a
page title, generic KPI row, or decorative illustration, the composition is
wrong.

### 3.2 Application chassis

At the 1,440 px reference width:

- viewport inset: 24–40 px when the host environment permits;
- outer chassis radius: 28 px;
- compact global header: 56–64 px;
- optional utility rail: 56–72 px, only for genuine global tool modes;
- context navigation: 208–248 px when hierarchy depth warrants it;
- workbench: remaining width on a 12-column grid;
- workbench padding: 24–32 px;
- workbench gutter: 12–16 px.

Rail, navigation, workbench, inspector, and evidence drawer must read as joined
pieces of one manufactured object. Avoid the appearance of a website sidebar
next to unrelated cards.

### 3.3 Default platform composition

The default Inspect view uses:

1. a compact context strip with robot ID, build, connection, freshness, clock
   confidence, and at most one primary action;
2. an 8-column platform field, 420–560 px deep;
3. a 4-column issue/selection lens attached to the field;
4. a lower evidence datum/drawer for compute comparison, uplink state, recent
   changes, traces, logs, or correlated events.

Do not start with four equal KPI cards. Summary values belong at the edge of the
platform field, inside the relevant object, or in a compact aligned strip.

```text
┌────────────────────────────── EXR CHASSIS ──────────────────────────────┐
│ Robot / build / connection / freshness / clock         primary action │
├──────────────┬───────────────────────────────────────┬─────────────────┤
│ Context      │                                       │ Attached        │
│ navigation   │       STABLE PLATFORM FIELD           │ diagnostic lens │
│              │       LAN / compute / CAN / paths     │ cause / impact  │
│ 208–248 px   │       8-column dominant instrument    │ action / why    │
│              │                                       │ 4 columns       │
├──────────────┴───────────────────────────────────────┴─────────────────┤
│ Evidence datum: chrony confidence / traces / events / logs / changes   │
└─────────────────────────────────────────────────────────────────────────┘
```

This is a relationship template, not a fixed component arrangement. A focused
view may enlarge the platform field or evidence band, but must preserve scope,
attachment, and the selected path.

### 3.4 Focus without losing geography

Selection changes emphasis, not object position.

- Keep the selected object fixed in the stable platform field.
- Quiet unrelated nodes using luminance and detail reduction, not disappearance.
- Highlight the selected path in yellow.
- Retain degraded/fault color underneath the yellow selection bracket; selection
  and health are separate meanings.
- Open the attached diagnostic lens on the nearest viable side.
- Preserve filters, active layer, time window, and evidence probe during drill-in.

For deep diagnosis, the selected object may expand into 6–8 columns while its
neighbors remain as compact comparison anchors. Do not replace the whole screen
with an unrelated detail template.

### 3.5 Density rhythm

Use three densities deliberately:

| Density | Use | Visual behavior |
|---|---|---|
| Sparse | threshold, safety confirmation, selected-object explanation | One subject, one state, one action, short evidence chain |
| Standard | platform overview and normal inspection | Dominant system field plus attached summary/evidence |
| Dense | traces, logs, CAN matrices, container/resource comparison | Compact type, shared axes, minimal container chrome |

Alternate density by role. A sparse orientation strip may sit beside a dense
instrument; a calm platform field may lead into a compact evidence drawer.
Uniform emptiness feels dry. Uniform density makes every element compete.

### 3.6 Asymmetry and visual weight

Use a strict grid but do not make a symmetric tile wall. Visual mass should
respond to system state:

- the dominant object or path receives the largest span;
- supporting evidence is narrower, quieter, or inset;
- a real anomaly may pull the focal point off-center;
- two equally large focal regions are permitted only for an explicit comparison;
- repeated objects such as the three compute nodes align for comparison, while
  the selected node may expand without losing the row.

Use these as art-direction guardrails, not automatic layout formulas:

- the dominant system instrument should usually occupy 45–65% of visible
  workbench area;
- the attached lens should usually occupy 20–30%;
- supporting comparison and evidence use the remainder or a lower drawer;
- at least 60% of persistent workbench area should read as joined or inset
  chassis, not standalone floating cards;
- more than two equally sized/equally contrasted major regions is a hierarchy
  warning;
- more than two persistent raised/floating surfaces visible at once is a
  material-hierarchy warning.

Break a guardrail only when the screen’s stated question provides a stronger
reason—for example, a deliberate three-node comparison.

### 3.7 Composition decision rule

Choose the primary visual form by question:

| Question | Primary form |
|---|---|
| Where is the problem and what is affected? | Stable topology with highlighted causal path |
| What changed over time? | Shared timeline/trace with current probe |
| Are many channels/messages healthy? | Matrix with aligned thresholds and direct labels |
| Which comparable node differs? | Aligned lanes or small multiples |
| What exact evidence supports the state? | Inset trace/log/table attached to selected object |
| What must the user decide or confirm? | Sparse threshold composition with one primary action |

Never choose a radial, map, bento, or floating tile because it looks fashionable.

## 4. Typography

### 4.1 Type roles

- **Space Grotesk:** product identity, screen orientation, selected system/fault,
  and instrument titles.
- **Inter:** navigation, controls, explanations, labels, tables, and body copy.
- **Roboto Mono:** values, units, timestamps, hostnames, ports, paths, message
  rates, versions, hashes, IDs, clock offsets, and code-like content.

Do not introduce a segmented display face. Technical identity comes from role,
alignment, and measurement grammar rather than a novelty font.

### 4.2 Operational hierarchy

| Role | Style | Use constraint |
|---|---|---|
| Exceptional orientation | Space Grotesk Bold 40/48 or 56/64 | Login, onboarding, reconnect, or a single major incident only |
| Screen/system heading | Space Grotesk Medium 32/40 | One per screen; name the real scope, never “Dashboard” |
| Major instrument | Space Grotesk Medium 24/32 | Dominant topology, selected system, or fault narrative |
| Instrument title | Space Grotesk Medium 20/28 | Important modules only |
| Interface body | Inter Regular 14/20 or 16/24 | Explanation and normal reading |
| Compact UI | Inter Regular 12/18; Medium 12/16 | Dense labels, rows, and controls |
| Data display | Roboto Mono Medium 32/40 | One decisive reading per local region |
| Data value | Roboto Mono Medium 16/24 | Comparable values |
| Data metadata | Roboto Mono Regular 12/18 | Units, timestamps, source, path, freshness |

### 4.3 Type behavior

- One dominant type object per screen or state.
- Large type names the actual system, selected fault, or required decision.
- Do not use oversized greetings, slogans, or page-category labels in the
  operational product.
- Align comparable values by digits or decimal point.
- Keep units immediately adjacent but visually subordinate.
- Put values near the mark, node, sample, or path they explain.
- Use uppercase 12 px eyebrows sparingly for instrument categories.
- Truncate human descriptions before machine identifiers. Hostnames, paths, and
  fault codes need copy access and a full-value disclosure.
- Minimum-size and contrast must be verified at intended viewport, not judged
  from a zoomed Figma canvas.

## 5. Color

### 5.1 Neutral foundation

The reference palettes are not source colors. Use the established ExRobotics
tokens:

| Role | Light | Dark |
|---|---:|---:|
| Canvas | `#F8F9F7` | `#090B0A` |
| Surface | `#FFFFFF` | `#141715` |
| Subtle surface | `#F1F3EF` | `#242925` |
| Border | `#CDD2CA` | `#394039` |
| Primary text | `#141715` | `#F8F9F7` |
| Secondary text | `#515A51` | `#CDD2CA` |
| Muted text | `#8C958B` | `#8C958B` |

Light and dark are paired expressions of one language. Light is a warm
precision workbench; dark is a graphite diagnostic chassis. Do not redesign the
composition or meaning when switching theme.

### 5.2 ExRobotics yellow

| Token/role | Value |
|---|---:|
| Signal soft | `#FFF8D6` |
| Selected surface | `#FFF0A3` |
| Signal bright | `#FFDA4D` |
| Lead signal | `#F5C400` |
| Focus/pressed | `#D9AA00` |
| Dark selected field | `#A57E00` |

Yellow priority is:

1. active path, selected node, current sample, or time probe;
2. primary deliberate action;
3. current navigation scope;
4. focus border or reticle;
5. one exceptional attention surface.

Use no more than one dominant yellow surface per local region. Multiple small
yellow marks are allowed only when they describe the same selection. Yellow is
not warning.

### 5.3 Semantic state

> **Dark supersedes this, see D032 and D034.** Green and blue are removed from
> the dark expression. Healthy is a neutral grey check; information and time
> sync are carried by line style. Caution is `#FF8A3D` and critical `#FF5765`,
> fully saturated so they separate from signal yellow by hue rather than
> lightness. The table below governs light only.


| State role | Soft | Strong | Required redundancy |
|---|---:|---:|---|
| Verified healthy | `#DDF6E9` | `#177A4D` | check/healthy label |
| Information/compute | `#E3EEFF` | `#2968C8` | domain label or line style |
| Caution/degraded | `#FFF0D9` | `#C66B0A` | warning glyph + reason |
| Critical/fault | `#FCE4E2` | `#B93A36` | critical glyph + consequence |

Unknown, stale, offline, and inferred require their own neutral/dashed/hatched
treatments and explicit text. “No detected fault” must not be rendered as
verified healthy.

Selection and status stack rather than replace one another: an orange degraded
node may receive a yellow focus bracket; it must not become yellow and lose its
degraded meaning.

### 5.4 Gradient rule

Gradients may provide quiet atmosphere or localized signal depth, never page
identity.

- Canvas/shell gradients span a large area and move no more than two neutral
  steps.
- Signal gradients belong only to a selected instrument or active route region.
- Dense plots, tables, logs, and persistent telemetry stay opaque.
- Do not place a different pastel or spectral gradient on every module.
- Do not use vivid diagonal portfolio backdrops inside the product.
- The screen must remain coherent with gradients disabled.

## 6. Spacing and geometry

### 6.1 Spacing scale

Use only: `0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64`.

Operational rules:

- 4–8 px: internal mark/label separation;
- 8–12 px: compact rows, control groups, and diagram internals;
- 12–16 px: workbench gutters and instrument internals;
- 20–24 px: standard instrument padding;
- 24–32 px: large topology/trace padding and workbench edge;
- 40–64 px: only major composition intervals, threshold screens, or editorial
  explanation.

At dense settings, compress padding and repeated headings before reducing
label legibility or target size. Minimum pointer target remains 44 px even when
the visible glyph is smaller.

### 6.2 Radius hierarchy

| Token | Value | Role |
|---|---:|---|
| none | 0 | tables, axes, shared dividers, paths |
| small | 4 | diagram nodes, tags, chart marks |
| control | 8 | controls and selected rows |
| card | 12 | dense evidence panels |
| expressive | 16 | selected compact panels/floating controls |
| panel | 20 | standard instruments |
| instrument | 24 | signature instruments and context panels |
| chassis | 28 | outer application object |
| full | 999 | short status/filter tokens only |

The radius decreases inward. Outer softness contains harder technical geometry.
Do not give every object 20–24 px rounding. Tables, plots, buses, matrices, and
internal nodes should be materially sharper than the chassis.

### 6.3 Alignment and borders

- Share left edges, axes, baselines, and dividers across related instruments.
- Use one-pixel outer borders and a subtle inner contour before adding shadow.
- Put healthy/normal structure on neutral hairlines.
- Use dash, double-outline, or clock marks to distinguish logical, VPN, unknown,
  and synchronization relationships.
- Maintain 16 px clearance between data marks and instrument edges.
- A connector must encode a real relationship; decorative dotted lines are
  prohibited inside the operational product.

## 7. Surface hierarchy

> **Dark supersedes the edge rules below, see D034 and guideline P12.** In dark,
> light does the separating — plane gradient, 1 px inner top highlight, soft
> inner glow, bottom floor — and the border is calibrated to sit below notice.
> The layer model and elevation-ownership rules are unchanged.


| Layer | Role | Treatment |
|---|---|---|
| L0 Canvas | environment behind product | quiet neutral atmosphere |
| L1 Chassis | complete application object | bounded silhouette, broad low-opacity depth |
| L2 Structural plane | rail, context nav, workbench | fine edge + subtle inner contour |
| L3 Instrument | topology, trace, matrix, list | crisp, flat or inset, little/no shadow |
| L4 Floating lens | selected detail, tooltip, palette | stronger edge and one elevation step |
| L5 Overlay | blocking dialog/confirmation | strongest elevation, explicit modal ownership |

Surface rules:

- Persistent surfaces are joined or inset; temporary context may float.
- The border and inner contour do more work than the shadow.
- Related instruments may share one structural plane and dividers.
- Elevation expresses interaction ownership, not importance alone.
- Glass/blur is permitted for utility rails, temporary inspectors, palettes,
  and overlays. It is prohibited for long tables, code, logs, dense charts, and
  persistent telemetry.
- A selected object may gain a focus edge, one level of elevation, or a signal
  wash. Do not enlarge, glow, shadow, and recolor it simultaneously.

## 8. Imagery and visualization

### 8.1 Imagery priority

Use imagery in this order:

1. accurate platform topology and dependency paths;
2. truthful live data instruments—traces, matrices, event timelines, resource
   bars, message-rate fields;
3. real drive/inspection camera frames when they answer a diagnostic question;
4. accurate robot or subsystem renders for onboarding, explanation, and empty
   states;
5. abstract illustration only when no truthful visual model exists.

Do not use generic 3D servers, floating cubes, fake circuit boards, world maps,
or device mockups as operational decoration.

### 8.2 Platform visual grammar

Maintain this geography across views:

- top/outer boundary: fleet-manager integration, Tailscale, Wi-Fi, cellular;
- upper middle: uplink ownership and VRRP/keepalived state;
- center: strong horizontal onboard LAN spine;
- center row: Intel, Jetson 1, Jetson 2 as comparable compute objects;
- lower Intel branch: CAN spine;
- CAN attachments: charging, battery, motor drive, 8-channel power GPIO, gas
  ADCs;
- side zone: drive and inspection cameras until their actual attachment is
  known;
- inside host lanes/overlay: Docker containers;
- cross-cutting overlay: chrony relationships, offset, uncertainty.

Unknown attachment is a dashed edge ending in `TBD`, never an invented
connection.

### 8.3 Relationship styles

| Relationship | Visual encoding |
|---|---|
| Physical cable/bus | solid line/spine |
| Network path | solid, directional only where meaningful |
| Logical dependency | dashed line |
| Tailscale/VPN | dotted or double-outline tunnel |
| Chrony synchronization | thin clock-marked line |
| Measured current traffic | live/current trace over a known path |
| Unknown association | dashed neutral line + question/TBD marker |

Do not animate flow without a live measurement. Do not conflate physical,
logical, observed-traffic, and overlay relationships.

### 8.4 Instrument selection

- **Topology:** location, attachment, dependency, propagation.
- **Aligned lanes:** compute-node or host comparison.
- **Matrix:** CAN availability/rate, GPIO channels, container health, message
  distribution.
- **Trace:** resource pressure, timing, throughput, signal value over time.
- **Timeline:** correlated events, restarts, configuration changes, stall cause.
- **Table/log:** exact evidence after the visual summary, not as the only
  overview.
- **Radial/direct manipulation:** only for genuinely circular or bounded
  adjustment/relationship models; never for novelty.

Every large instrument must expose its question, unit, source, time range,
freshness, and selected state. Decorative charts fail.

## 9. Component language

### 9.1 Instrument anatomy

A major instrument contains up to four zones:

1. context—category, object, or question;
2. readout—primary value/state/selection;
3. stage—topology, trace, matrix, diagram, list, or direct manipulation;
4. control/metadata—time range, source, units, freshness, filter, or action.

The stage is mandatory for signature analytic modules. Do not repeat the same
title/value/bar anatomy across every module.

### 9.2 Summary treatment

A compact summary should include at least one meaningful visual:

- short trace with a threshold;
- range marker;
- component silhouette;
- stacked distribution;
- live delta and time window;
- compact state distribution.

If a summary contains only a title, number, and explanatory sentence, place it
in a shared summary strip or table rather than giving it a large card.

### 9.3 Status and selection

- Status always has label + icon/shape/pattern + color.
- Freshness is shown beside the observation, not only in a global footer.
- Current scope receives the yellow probe or bracket.
- A selected node exposes relevant controls; dormant controls stay hidden.
- Dangerous or permission-controlled actions are visually separated from
  navigation and routine filters.

### 9.4 Data grammar

Every machine reading should answer, as applicable:

- value and unit;
- source/object;
- expected range or threshold;
- time window or timestamp;
- freshness/uncertainty;
- comparison or previous value;
- reason for health roll-up.

This grammar is part of the visual identity. Accurate metadata must not be
treated as optional polish.

### 9.5 Realistic content contract

Concept screens must use the known platform model, not generic dashboard filler.

- Name the three onboard computers as Intel, Jetson 1, and Jetson 2 unless a
  more authoritative hostname is available.
- Show LAN, Intel-attached CAN, charging, battery, motor drive, 8 GPIO power
  channels, gas ADCs, two cameras, Docker runtimes, chrony, Tailscale,
  Wi-Fi/cellular, VRRP/keepalived, and fleet-manager integration only where the
  view requires them.
- Use plausible units and formats: `%`, `°C`, `GB`, `MB/s`, `Mbit/s`, `ms`,
  message rate, clock offset, packet loss, restart count, version, and timestamp.
- Mark invented demonstration values as `Illustrative`, `Demo`, or `Sample` in
  the frame/documentation. Do not present synthetic health as a current robot
  fact.
- Represent unresolved camera hosts, routes, VRRP roles, or other unknowns as
  `TBD` with dashed geometry.
- Use failure copy that states cause, consequence, evidence freshness, and the
  next safe inspection step. Avoid “Something went wrong.”
- Do not add uptime percentages, user counts, revenue, tasks, team activity,
  avatars, or geographic regions to make the screen look populated.

Realistic content changes composition. It exposes label length, comparison
needs, unknown state, unit alignment, and evidence density that placeholder
copy hides.

## 10. Interaction and motion

- Selecting any visual object opens the same canonical inspector model.
- Selection persists across topology, traces, logs, tables, and time.
- Hover may preview neighbors or values but cannot contain essential facts.
- A visible “why?” disclosure explains which measurements created a health
  state.
- Zoom and layer changes preserve stable node positions and selected context.
- Motion duration uses 120 ms fast, 200 ms normal, and 320 ms slow only for
  major spatial transitions.
- Prefer short continuity transitions: probe relocation, lens attachment,
  trace reveal, panel expansion.
- Do not use ambient pulsing, parallax, elastic nav movement, flowing particles,
  or animated network traffic without semantic state.
- Provide reduced-motion behavior; motion cannot be the only evidence of change.

## 11. Product-specific composition recipes

### 11.1 Platform overview

- Dominant 8-column stable platform field.
- 4-column causal issue/selection lens.
- Highest-impact fault or unknown shown in place.
- Compact lower band: three-node resource comparison, uplink ownership, recent
  correlated changes.
- No fleet map, mission queue, autonomy state, or giant KPI row.

### 11.2 Compute

- Three aligned host lanes remain visible.
- Selected host expands; other hosts remain comparison anchors.
- CPU/GPU, memory, storage, thermal, chrony, and container placement appear
  inside or immediately beside their host.
- Container owner and dependency are encoded with label/line style, not color
  alone.

### 11.3 Connectivity

- Primary path: Wi-Fi/cellular → VRRP/keepalived ownership → onboard LAN → host
  → CAN or service.
- Tailscale is a distinct overlay, not a physical cable.
- Show active/standby, last transition, rate, latency, loss, errors, and
  freshness on the affected path.

### 11.4 CAN and physical subsystems

- CAN spine is the main instrument.
- Charging, battery, motor drive, GPIO, and gas ADCs stay at stable attachment
  points.
- Message availability/rate may use a matrix attached to the spine.
- Subsystem response time uses directly labeled traces or aligned small
  multiples.
- GPIO is an eight-channel requested/observed/interlock matrix, never one
  generic on/off card.

### 11.5 Software and middleware

- Use three host lanes with container groups.
- Show ROS 2/DDS, API agent, POI capture nodes, partner runtimes, ports, and
  selected dependencies in place.
- ROS diagnostics, unauthorized login attempts, POI database health, and data
  capture evidence attach to the responsible runtime/object.
- Avoid an undifferentiated container table as the primary view.

### 11.6 Drive Stall and controlled actions

- Treat Drive Stall as a sparse consequential state, not a dashboard badge.
- Show motor-drive object and affected CAN/power path in context.
- State the overload cause/evidence, current physical state, permission,
  interlock, and freshness.
- Manual deactivation is one explicit primary action with request,
  acknowledgement, and observed-result states separated.
- Never imply that browser UI or visual styling makes the control safety-rated.

## 12. Principles combined into this original language

The synthesis deliberately combines complementary principles, not source
layouts:

- **spatial system focus** from map/workbench references + the real ExR platform
  topology;
- **continuous current/evidence path** from flow and timeline references + ExR
  yellow’s existing brand role;
- **joined chassis and inversion** from structural-grid references + ExR’s warm
  neutral/graphite token system;
- **selective material depth** from dimensional/frosted references + a strict
  ownership rule for floating surfaces;
- **expert evidence density** from operations/analytics references + stable
  scope, units, freshness, and source grammar;
- **editorial focus** from presentation/login references only for onboarding,
  threshold, recovery, and selected-object explanation.

These principles reinforce one another: the stable platform field answers
where; yellow shows current scope; the attached lens explains what/why; the
evidence datum proves when; the instrument grammar supplies exact machine
truth.

## 13. Conflicts resolved

- **Cinematic whitespace vs engineering density:** cinematic spacing is limited
  to threshold, onboarding, and recovery states. Monitoring uses role-based
  density.
- **Soft consumer geometry vs technical precision:** softness belongs to the
  outer chassis and temporary lens; instruments, paths, grids, and tables stay
  exact.
- **Bright multicolor analytics vs ExR signal discipline:** yellow identifies
  current context; a minimal labeled semantic set handles health; other series
  default to neutral or blue comparison.
- **Floating tiles vs causal continuity:** tiles may float only when selected,
  movable, temporary, or attached to a referent. Persistent evidence remains
  joined or inset.
- **Symmetric comparability vs dynamic focus:** comparable compute nodes align,
  but current system state determines which span or path dominates.
- **Light premium atmosphere vs dark diagnostic depth:** both themes share the
  same hierarchy and interaction semantics; neither imports reference colors.

## 14. Reference-specific details not to copy

Do not reproduce:

- segmented display fonts or exact bracket glyphs;
- blue hexagonal noise maps, point-cloud world maps, geographic heat maps, or
  cartographic incident fields when onboard topology is the real subject;
- coral matrices, lime project cards, violet atmospheres, green navigation
  ribbons, acid-yellow phone styling, or multicolor radial palettes;
- phone/device mockups inside the operational application;
- healthcare timelines, sales taxonomies, logistics tracking, facility cards,
  contract folders, household scenes, or file-browser metaphors as product
  content;
- exact bento arrangements, dashboard card grids, navigation dimensions, font
  choices, shadows, radii, or gradients from any source;
- decorative 3D controls whose geometry does not correspond to an interaction;
- presumed motion, hover, cross-filtering, or causal relationships that a static
  screenshot does not prove;
- low-resolution artifacts, crop-specific whitespace, or presentation backdrops.

Borrow the decision behind a move, then rebuild it from the ExR product model,
tokens, content, and interaction contract.

## 15. Consistent anti-patterns

Reject a design when any of these dominates:

- sidebar + greeting + four KPI cards + generic chart grid;
- a screen organized by categories instead of detect → locate → explain → act;
- one rounded rectangle per fact;
- equal module spans or uniform visual weight;
- a “topology” view that is actually a table or set of cards;
- gradients, blur, glow, or 3D objects supplying identity without meaning;
- yellow used as warning, decoration, and selection simultaneously;
- color-only health, freshness, or selection;
- a different accent color for every chart or subsystem;
- large empty premium spacing around trivial information;
- multiple unrelated focal objects;
- world maps, fleet concepts, mission state, autonomy, or navigation content;
- generic avatars, productivity metrics, business analytics, or welcome copy;
- controls, handles, reticles, dotted connectors, or animated flow without real
  behavior;
- exact telemetry without units, source, time window, freshness, or uncertainty;
- invented host assignments, routes, health, or system relationships;
- a technically consistent interface whose composition remains aesthetically
  anonymous.

## 16. Instructions for an AI design agent

Before building:

1. Name the user, task, dominant question, current scope, and consequence.
2. Inspect existing Figma components, variables, text styles, and stable system
   geography; reuse them where semantically correct.
3. Select one primary visual form using the composition decision rule.
4. Sketch the full-screen massing in greyscale before styling components.
5. Mark the focal path, attached lens, evidence region, and deliberate action.
6. Use realistic ExR system objects and plausible content; label unknown facts
   as unknown/TBD rather than inventing them.

While building:

1. Establish the chassis and large-span composition first.
2. Build the dominant system instrument before summaries.
3. Add only evidence that explains state, comparison, or action.
4. Apply typography roles, then neutral surface hierarchy, then semantic state,
   then yellow current signal.
5. Reuse existing tokens and components. Create a new component only when its
   behavior or visual role is genuinely different.
6. Verify that floating surfaces are temporary/selected and attached.
7. Keep exact machine metadata near the evidence it qualifies.

Before completion:

1. Render the actual viewport at 100%.
2. Inspect it in color and greyscale.
3. Blur/squint the render: the platform field, current issue, and action must
   still be obvious.
4. Verify that a degraded subsystem can be located in under two seconds.
5. Verify that selection and health remain different without hue.
6. Check minimum text contrast, target sizes, alignment, overflow, units,
   timestamps, source, and freshness.
7. Identify the five highest-impact visual problems and fix them in impact
   order: composition → hierarchy → density → typography → surface/color →
   craft.
8. Render again and repeat. Successful rendering proves implementation only;
   it does not prove design quality.

### Genericity breaker tests

Run these before declaring the art direction successful:

1. **Silhouette test:** remove text, icons, color, and logo. The joined chassis,
   dominant platform field, attached lens, and evidence datum should still be
   identifiable.
2. **Yellow-off test:** turn all yellow neutral. Hierarchy and current ownership
   must remain understandable through scale, position, line, bracket, and tone.
3. **Swap test:** imagine replacing ExR nouns with finance or sales nouns. If the
   composition still works unchanged, it is probably a generic dashboard and
   must be rebuilt around real platform relationships.
4. **Card test:** count major standalone rectangles. If most facts have their own
   container, consolidate them into a schematic, matrix, lane, shared plot, or
   aligned evidence surface.
5. **Instrument test:** the dominant visual must answer an engineering question
   more quickly than a list. If it does not, choose a better encoding.
6. **Reference test:** no individual source should be recognizable through an
   exact layout, palette, motif, or object. The result should express the
   combined ExR grammar instead.
7. **Anonymity test:** ask what remains memorable after five minutes. “Dark
   cards with yellow accents” is a failure; “stable robot field with a yellow
   probe and attached diagnostic lens” is a pass.

### Three-distance reading test

- **Five seconds:** robot context, overall safety/health, highest-impact anomaly,
  and active path are apparent.
- **Thirty seconds:** the responsible object, affected dependencies, freshness,
  and first evidence are understandable.
- **Two minutes:** the engineer can correlate time, inspect exact data, explain
  the health roll-up, and locate the permitted next action without losing scope.

## 17. Acceptance gate

A design passes only when all statements are true:

- The screen’s dominant engineering question is obvious without reading a
  paragraph.
- The stable platform/system context remains visible during drill-in.
- One primary visual object clearly dominates; supporting evidence is attached
  or subordinate.
- The user can follow symptom → object/path → evidence → permitted action.
- Information density is high where comparison/evidence requires it and calm
  where orientation/decision requires it.
- Typography separates human explanation from machine truth.
- Yellow describes one coherent current scope and does not replace warning.
- Status, freshness, selection, and edge type remain distinguishable in
  greyscale.
- Surface elevation corresponds to ownership and temporariness.
- Every decorative-looking mark has a real informational or interactive role.
- Real platform objects and believable engineering content replace generic
  SaaS placeholders.
- The screen remains free of fleet, mission, autonomy, SLAM, navigation, and
  teleoperation concepts.
- The composition is recognizable as ExRobotics without relying on logo or
  color alone.
- A fresh render has been visually critiqued and the highest-impact problems
  have been corrected.

Failure on composition, causal clarity, signal semantics, truthful content, or
greyscale state is an automatic **ITERATE**. Consistency and rendering accuracy
cannot override those failures.
