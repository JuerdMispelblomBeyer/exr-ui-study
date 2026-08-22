# Visual Style v3 improvement plan

**Status:** Implemented in archive-safe Figma siblings; promotion pending user review  
**Date:** 2026-08-21  
**Scope:** Visual-system redesign of the existing Inspect → Diagnose → Change
storyboard. Product architecture and functional content remain the baseline.

## 1. Outcome

Visual Style v3 must make the engineering interface visibly belong to the
reference family while remaining truthful, accessible, and recognizably
ExRobotics.

The target is not a restyled dashboard. It is:

> A precisely framed, materially layered instrument chassis whose workbench is
> composed from heterogeneous live instruments, with ExRobotics yellow acting
> as a scarce optical signal.

The current v2 storyboard remains useful as a UX and content-flow prototype.
It does not meet the visual-reference fidelity threshold and must not be used
as the visual benchmark for further screens.

The plan was authorized and executed on 2026-08-21. V2 remains unchanged;
implementation evidence and node IDs are recorded in `FIGMA_IMPLEMENTATION.md`.

### Implementation record

- Foundations section: `49:4706`
- Component stage: `50:5179`
- Nine-screen engineering storyboard: `50:5617`
- Durable renders: `../renders/latest-v3-2026-08-21/`
- Graphite is the primary operational expression; Precision Light is validated
  as the paired identity expression in the foundations study.
- A separate dark semantic variable collection was intentionally deferred
  because FigWright cannot assign variable scopes. Existing scoped primitives
  and light semantics were reused instead of creating picker pollution.
- Visual QA and color-independent state encoding were completed. Full keyboard,
  reduced-motion, and production interaction validation remain product-phase
  work rather than claims of this static reference implementation.

## 2. Audit inputs

### Visually verified references

- `../reference/ref-001__dark-resource-overview__stacked-utilization-instrument.jpg`
- `../reference/ref-002__dark-contract-dashboard__tall-crop.jpg`
- `../reference/ref-004__light-health-dashboard__treatment-timeline-crop.jpg`
- `../reference/ref-005__light-frosted-workflow-dashboard__tall-navigation.jpg`
- `../reference/ref-003__dark-contract-dashboard__wide-workbench.jpg`
- `../reference/ref-006__dark-instrument-system__mixed-tile-grid.jpg`
- `../reference/presentation-only/pres-001__editorial-mobile-turbine-app__device-mockups.jpg`

Solar21 contributes verified page intent and flow principles, but its protected
case-study assets were not captured locally. Dribbble shot `27644169` remains a
queued source and contributes no visual claims.

### Current implementation reviewed

- foundations specimen `48:3030`;
- component stage `48:2129`;
- nine v2 storyboard frames `48:2171`, `48:2258`, `48:2346`, `48:2442`,
  `48:2574`, `48:2661`, `48:2751`, `48:2844`, and `48:2942`;
- durable exports under `../renders/latest-2026-08-21/`.

## 3. Reference-by-reference findings

### 3.1 Resource Overview — technical faceplate

#### What creates the identity

- A near-black field reads as one equipment face rather than a page.
- Sparse headline/totals and a dense chart create strong vertical tension.
- The chart, legend, filters, grid, axes, and values share one enclosure.
- Square markers and corner brackets provide a capture/scope motif.
- High-contrast data marks dominate; decoration is nearly absent.

#### ExRobotics translation

- Use a strict datum/grid inside diagnostic instruments.
- Join controls, scale, data, units, and legend into one instrument surface.
- Use brackets for the active probe or selected scope only.
- Create stronger sparse-to-dense transitions within one screen.
- Retain Space Grotesk/Roboto Mono rather than copying the segmented display
  face.

#### Current v2 gap

V2 uses large pale regions containing little data. Its comparison modules are
numbers over short bars, and the topology stage lacks a diagnostic grid,
scale, directional encoding, or data density. It resembles a clean diagram,
not an equipment faceplate.

### 3.2 Lunar dashboard — nested dark chassis

#### What creates the identity

- The navigation slab and content field form one inset product object.
- Several dark surface steps create depth without obvious shadows.
- Summary, trace, table, and object-library bands have different proportions
  and different information rhythms.
- Selected navigation is an inset plate; object cards have stable internal
  compartments and footer actions.
- The wide crop shows a tight bento field with almost no wasted gutters.

#### ExRobotics translation

- Introduce a real outer chassis and nested structural surfaces.
- Give each row a distinct diagnostic role and depth.
- Separate object identity, micro-instrument, metadata, and actions within a
  tile instead of placing all content in one undifferentiated rectangle.
- Use stepped graphite or warm-neutral surfaces for material hierarchy.

#### Current v2 gap

V2 is edge-to-edge, with a plain black rail beside a nearly uniform light
canvas. Header, lens bar, map, inspector, comparison, changes, and evidence are
all variations of the same white outlined panel. The interface has regions but
not material strata.

### 3.3 Connected medical timeline — continuous relationship field

#### What creates the identity

- A continuous datum/timeline organizes the composition.
- Capsules, cards, readings, and events are attached to the relationship line.
- Density gathers around consequential points and relaxes between them.
- The system feels spatial and navigable, not like a stack of sections.
- One bright anchor communicates current scope.

#### ExRobotics translation

- Treat LAN, CAN, VPN, time, and software paths as meaningful datums.
- Attach rates, latency, topic, error, and ownership chips directly to paths.
- Let one selected anchor interrupt the datum instead of outlining an entire
  region.
- Use space around causal paths to improve understanding.

#### Current v2 gap

The v2 LAN/CAN rails are thick grey lines with repeated white node cards. They
show attachment, but not direction, rate, traffic, uncertainty, causality, or
interaction. The map reads as a static architecture slide.

### 3.4 Layered light navigation — moulded structural chrome

#### What creates the identity

- A narrow dark utility rail, a translucent context rail, and the main content
  plane form neighboring physical layers.
- Large/medium/small radii create a legible nesting hierarchy.
- Fine outer strokes, inner highlights, soft blur, and local shadows make the
  shell feel manufactured.
- The selected navigation plate is luminous and inset rather than merely
  filled.

#### ExRobotics translation

- Use translucency and blur only on structural chrome and temporary controls.
- Give navigation genuine edge depth, internal highlights, and selected-state
  material change.
- Preserve crisp opaque surfaces for logs, traces, and telemetry.

#### Current v2 gap

The v2 rail is a flat black strip and the lens switcher is a row of ordinary
pills. Surface ownership is communicated mostly through borders. There is no
convincing structural chrome or light interaction.

### 3.5 Dark bento micro-instruments — active workbench

#### What creates the identity

- Large rounded tiles form a nearly continuous matrix with tight gutters.
- Every tile has a different internal instrument: node graph, orbit, trace,
  matrix, selection stage, or structured list.
- Values and labels float close to the mark they explain.
- Reticles, cursors, handles, plus controls, and annotation chips imply direct
  manipulation.
- A faint inner contour and local glow make each instrument tactile while the
  field remains calm.

#### ExRobotics translation

- Make the workbench a family of purpose-built engineering instruments.
- Add inspectable data marks, thresholds, paths, ranges, and current probes.
- Reveal only the controls that belong to the current selection.
- Use a continuous crop or expansion behavior where the workbench genuinely
  reveals more evidence.

#### Current v2 gap

The v2 storyboard repeats one large topology panel across almost every state.
Most nodes contain a letter, name, and one value. The lower cards repeat the
same number-and-bar anatomy. There is little visual evidence of interaction
beyond a yellow outline and a button.

### 3.6 Editorial mobile composition — focus and product storytelling

#### What creates the identity

- A selected product is isolated in deep negative space.
- Oblique hardware views, restrained lighting, and material reflections create
  physical presence.
- Small numbered explanation plates sit on separate depth planes.
- Fine dotted leader lines connect explanation to the product.
- The bright accent is extremely scarce.

#### ExRobotics translation

- Selected-subsystem and guided-diagnosis states may isolate one hardware or
  system object while retaining an escape back to the platform context.
- Use two or three anchored callout plates for cause, consequence, and next
  evidence—not for ordinary metadata.
- Introduce robot/hardware context in onboarding and subsystem explanation,
  not in routine dense monitoring.

#### Current v2 gap

Selection leaves every object at nearly the same weight and adds a strong box
outline. The inspector changes text, but the composition does not create a
focused depth state. No object becomes a visual subject.

## 4. Current v2 fidelity scorecard

| Gate | Result | Evidence |
|---|---|---|
| Chassis silhouette | Fail | Frames run edge-to-edge; the shell does not read as an inset designed object |
| Layer ownership | Partial | Rail, map, inspector, and drawer exist, but share nearly identical flat surface treatment |
| Bento rhythm | Fail | One repeated map dominates; lower modules are regular rectangles with repeated anatomy |
| Instrument content | Fail | Topology is mostly static; comparison cards are values plus short bars |
| Edge character | Partial | Fine borders exist, but the same edge treatment is applied almost everywhere |
| Interaction evidence | Partial | Selection/path color exists; direct-manipulation marks and anchored readouts are scarce |
| Density rhythm | Fail | Most areas use the same low-to-medium density; sparse and dense zones are not deliberately contrasted |
| Greyscale identity | Fail | Selection, health, and lens state depend heavily on yellow, green, blue, and orange |
| Yellow allocation | Fail | Selected rail item, lens, brackets, buttons, drawer edge, and chips compete simultaneously |

The current visual implementation therefore fails five gates and only
partially passes three. It should be described as **v2 UX/content baseline**,
not as the promoted visual identity.

## 5. Root causes of the mismatch

### 5.1 Layout rules were implemented as containers, not composition

The Figma frames contain the named regions from the UX plan, but the reference
rhythm was not translated. Region presence is not the same as chassis,
layering, bento proportion, or focus composition.

### 5.2 “Low relief” became “almost flat”

Borders were reduced correctly, but surface steps, inner contours, selected
depth, and structural chrome were also suppressed. The result is visually dry
rather than materially restrained.

### 5.3 “Visual first” became a node-and-line diagram

The platform topology is factually helpful, but its nodes do not contain live
instrumentation and its paths do not encode enough meaning. A schematic alone
does not satisfy the micro-instrument requirement.

### 5.4 The component model over-standardized content

One node component and one comparison-card anatomy dominate. The references
share external geometry while allowing radically different internal stages.
V2 shares both exterior and interior anatomy, producing repetition.

### 5.5 Color is carrying hierarchy that geometry should carry

Green strips, blue glyph fields, orange paths, yellow pills, and yellow borders
communicate most states. Removing color leaves a uniform set of white cards.

### 5.6 The light expression was treated as the safe default

The references include light work, but even their light examples use strong
material layering, unusual silhouettes, continuous datums, and controlled
blur. V2 uses lightness without those compensating identity devices, causing a
generic enterprise appearance.

## 6. Visual Style v3 target

### Direction remains Signal Instrumentation

The direction name and semantic foundations remain valid. V3 changes the
strength and consistency of their execution.

### Primary expression: Graphite Instrument Chassis

Start v3 in the dark/hybrid expression because it exposes silhouette, depth,
data contrast, and yellow scarcity most clearly.

- Near-black environmental canvas.
- Inset graphite application chassis with a clear outer radius.
- Dark structural navigation and command chrome.
- A stepped graphite workbench with crisp opaque instruments.
- Selected or explanatory plates may use warm light or signal-tinted surfaces.
- ExRobotics yellow is the brightest local mark and never an ambient wash.

### Paired expression: Precision Light

Translate the approved dark/hybrid grammar into light without changing
component anatomy or interaction semantics.

- Warm-neutral environmental canvas rather than pure white.
- A visibly bounded light chassis with a darker or smoked utility rail.
- Structural chrome may be translucent; data surfaces remain opaque.
- Instruments use stronger neutral separation than v2.
- The same yellow signal locations, focus marks, and data encodings are kept.

Neither expression is a theme skin. Both must share silhouette, spans,
instrument stages, edge hierarchy, and focus behavior.

## 7. System-level visual changes

### 7.1 Rebuild the outer silhouette

- Inset the 1,440 px application object by approximately 24–32 px when shown as
  a reference frame.
- Use one clearly readable chassis boundary and 28–32 px outer radius.
- Integrate global context, task navigation, lenses, workbench, attention, and
  evidence into the chassis instead of placing bands against the viewport.
- Use a quiet environmental field outside the chassis to make the application
  read as equipment.
- Keep the task rail inside the chassis with a narrow controlled gap from the
  workbench.

### 7.2 Establish a stronger layer ladder

The following layers must be distinguishable in greyscale:

1. environment;
2. chassis;
3. structural chrome/navigation;
4. workbench well;
5. persistent instrument;
6. selected/floating control;
7. blocking overlay.

Do not achieve this with seven shadows. Use neutral steps, outer strokes, inner
highlights, local blur, overlap, and only then elevation.

### 7.3 Convert the workbench into a real bento field

The platform overview should no longer be one map plus three subordinate
rectangles. Use a 12-column field with purposeful asymmetry:

- 8 columns: primary platform/topology instrument;
- 4 columns: adaptive focus/attention instrument;
- 4 columns: compute resource matrix;
- 4 columns: network/CAN pulse or distribution;
- 4 columns: consequential changes/state timeline;
- 8 columns or full width when evidence expands;
- 4 columns: scoped live-signal summary paired with evidence.

Edges align, but internal stages must differ. The field should feel continuous
through 10–14 px gutters, shared outer geometry, and aligned datums.

### 7.4 Turn topology into an instrument

Replace generic node cards with an instrumented platform map:

- LAN and CAN become fine bus spines with direction, traffic pulses, or rate
  ticks—not thick decorative rails.
- Compute nodes include a small resource matrix, thermal contour, runtime stack,
  or load trace according to the active lens.
- CAN subsystems use compact subsystem silhouettes or state matrices.
- Network paths expose interface, owner, latency, loss, and failover role in
  attached chips.
- Time paths expose source, offset, envelope, and confidence.
- Software paths expose container ownership and dependency direction.
- Unknown/TBD attachments remain visibly unknown rather than appearing as
  ordinary healthy pills.
- Normal state is optically quiet; exception and selected paths gain priority.

### 7.5 Replace repeated comparison cards with heterogeneous instruments

Use at least four internal instrument types across the critical screens:

- compute core/GPU matrix;
- synchronized mini-trace with shared time axis;
- CAN message-rate histogram or waterfall;
- network throughput/loss pulse;
- chrony offset/envelope plot;
- container distribution stack;
- subsystem state matrix;
- causal event timeline.

The same outer module may host different stages, but a value-plus-progress-bar
cannot remain the default for all comparisons.

### 7.6 Create a real focus state

When an object is selected:

- preserve the stable map geography;
- reduce unrelated content through contrast, detail, or depth—not heavy blur;
- elevate the selected object by one level;
- use two or four yellow focus brackets or one reticle, not a thick complete
  outline plus multiple yellow fills;
- attach one current-value chip or consequence callout to the selected mark;
- let the attention module visually connect to the selected object;
- reveal relevant controls locally.

For guided diagnosis or onboarding, allow an editorial focus layer with no
more than three numbered callouts.

### 7.7 Give navigation physical ownership

- Retain Inspect, Diagnose, and Change as the task rail.
- Replace the large pale selected tile with an inset plate, compact yellow
  signal, and trailing state mark.
- Make the lens control a structural strip or docked command capsule rather
  than an isolated row of generic pills.
- Integrate version, connectivity, environment, and settings into stable rail
  zones.
- Use technical outline icons or glyphs; remove generic letter-in-blue-square
  identity marks from system nodes.

### 7.8 Strengthen typography contrast

- Use fewer sizes but more deliberate contrast between them.
- Let one system state or value dominate each instrument.
- Use compact uppercase/mono eyebrows for instrument class, scope, and
  freshness.
- Place units and machine metadata on a strict baseline close to their values.
- Use tabular numerals for changing data.
- Reduce paragraph copy in the attention rail; replace it with consequence,
  evidence, and action blocks.
- Allow one larger editorial heading only in focus/onboarding compositions.

### 7.9 Reallocate yellow

Yellow must be scarce enough to function like an indicator lamp.

Priority:

1. selected/current path or live datum;
2. current task control or primary action;
3. focus bracket/reticle;
4. one attention cue.

Remove routine yellow from simultaneous lens fill, task tile fill, evidence
edge, large outline, action fill, and multiple chips. When an object is both
degraded and selected, orange keeps the state while yellow supplies only the
focus mark.

### 7.10 Reduce routine status color

- Healthy objects do not all need green rails.
- Use a small verified mark, text, or neutral state treatment for normal.
- Reserve strong green for confirmed recovery or a relevant healthy comparison.
- Keep blue for a selected comparison series or domain-specific instrument,
  not every compute-node glyph.
- Preserve orange/red for actual warning/critical semantics.
- Stale/unknown uses dashed geometry, pattern, timestamp, and reduced contrast
  rather than color alone.

### 7.11 Use atmosphere deliberately

- Permit subtle neutral radial/linear atmosphere at the environment or chassis
  level.
- Permit a local yellow signal bloom only behind the current active probe.
- Permit glass/blur on command chrome, search, floating inspectors, and selected
  controls.
- Keep traces, logs, tables, matrices, and persistent telemetry optically crisp.
- Do not restore different pastel gradients to every card.

## 8. Component redesign plan

### Chassis family

- application chassis / graphite and light;
- utility/task rail;
- global context strip;
- workbench well;
- docked lens/scope strip;
- compact evidence dock;
- expanded evidence plane.

### Instrument shell family

Variants describe ownership, not domain:

- persistent;
- selected;
- degraded;
- selected + degraded;
- floating;
- stale/unknown;
- dense evidence.

Each exposes slots for context, primary readout, instrument stage, attached
annotation, and compact controls.

### Platform object family

- compute object with interchangeable internal stage;
- subsystem object;
- integration/uplink object;
- camera/attachment object;
- unknown/TBD object;
- compact object token for dense maps;
- expanded selected-object instrument.

Normal, warning, critical, stale, selected, and selected-warning states must be
distinguishable without relying on fill hue.

### Path and annotation family

- bus spine;
- directional dependency edge;
- physical/logical/VPN/time/unknown edge;
- data pulse/rate tick;
- selected-path overlay;
- focus bracket and reticle;
- path-attached value chip;
- numbered explanation plate and leader line.

### Micro-instrument family

- trace with grid/threshold/current probe;
- resource matrix;
- state matrix;
- distribution/histogram;
- causal timeline;
- offset/envelope plot;
- runtime stack;
- port/interface diagram;
- dense evidence row/list.

Each component must state the diagnostic question it answers. Decorative chart
components are prohibited.

## 9. Critical screen recomposition

Do not restyle all nine screens at once. Establish the system using three
stress-test frames.

### Frame A — Inspect · Healthy

Purpose: prove the chassis, bento rhythm, normal-state restraint, and stable
platform geography.

Required visual evidence:

- clear inset chassis;
- one dominant topology instrument;
- at least three different supporting micro-instruments;
- quiet healthy objects without repeated green bars;
- current scope visible without multiple yellow surfaces;
- at least one dense and one sparse zone.

### Frame B — Inspect · Selected degraded motor drive

Purpose: prove simultaneous orange degradation and yellow focus, depth-based
selection, causal path emphasis, and selected-object explanation.

Required visual evidence:

- degraded path understood in under two seconds;
- selected object becomes the visual subject without moving geography;
- orange remains state; yellow remains selection;
- one anchored live-value chip;
- attention instrument connects visually to the selected object;
- normal objects remain locatable but subordinate.

### Frame C — Diagnose · Evidence expanded

Purpose: prove dense instrumentation, time correlation, and evidence expansion
without losing the platform mental map.

Required visual evidence:

- synchronized causal timeline;
- meaningful CAN rate/load/heartbeat instruments with scale and units;
- workbench compresses or overlays coherently;
- evidence uses crisp dense surfaces with smaller internal radii;
- selected path and time window remain visible.

Only after these three pass visual review should the Network, Software, Time,
Change, and stale/disconnected states inherit the system.

## 10. Figma implementation sequence

### Phase 0 — archive and audit

- Preserve v2 foundations, component stage, and storyboard unchanged.
- Prefix or document them as `Archive · UX baseline · Visual Style v2`.
- Create v3 sibling sections; never overwrite the current nodes.
- Add the reference images and this audit beside the v3 exploration area where
  helpful, without embedding copyrighted work into the product components.

**Exit gate:** v2 is recoverable and v3 has distinct target sections.

### Phase 1 — silhouette and greyscale material study

- Create dark/hybrid and light chassis studies with no semantic color.
- Build navigation, workbench well, instrument shell, selected plate, and
  evidence plane.
- Test the full 1,440 × 900 silhouette at thumbnail size.
- Establish the neutral surface ladder, border contrast, inner highlight, and
  elevation ownership.

**Exit gate:** chassis, layers, and focus remain legible in greyscale at 25%
scale.

### Phase 2 — instrument grammar study

- Build one specimen of each required micro-instrument.
- Place them in a compact bento field to test mixed density and spans.
- Validate scale, units, selection, threshold, stale, and empty states.
- Remove any instrument that cannot answer a real engineering question.

**Exit gate:** at least six distinct useful instrument stages share one outer
system without looking like duplicated cards.

### Phase 3 — topology as live instrument

- Rebuild platform nodes, LAN/CAN spines, edge types, and lens overlays.
- Add resource, rate, error, time, and runtime marks appropriate to each lens.
- Test normal, selected, degraded, selected-degraded, and stale states.
- Verify that the map still matches the platform source of truth.

**Exit gate:** the platform structure and dominant exception are understandable
without reading the inspector.

### Phase 4 — three critical stress-test frames

- Compose Frames A, B, and C.
- Add yellow only after greyscale hierarchy passes.
- Compare screenshots side-by-side with every verified reference.
- Run the v3 acceptance matrix below.

**Exit gate:** all visual gates pass on the critical path.

### Phase 5 — paired light expression

- Translate the approved dark/hybrid anatomy into Precision Light.
- Preserve spans, state hierarchy, and signal positions.
- Recalibrate borders, material separation, blur, and contrast.
- Avoid reverting to white outlined cards.

**Exit gate:** light and dark are recognizably the same system in greyscale.

### Phase 6 — propagate across the storyboard

- Apply the approved system to Network, Software, Time, Change, and stale
  states.
- Give each lens a domain-appropriate instrument rather than changing only
  labels and highlight colors.
- Update the component stage and foundations specimen from the approved
  components.

**Exit gate:** all nine frames share one system while remaining visually
distinct by diagnostic purpose.

### Phase 7 — interaction, accessibility, and promotion

- Prototype selected plate, local controls, evidence expansion, and focus-mode
  transitions.
- Test long IDs, dense logs, stale data, keyboard focus, reduced motion, and
  color-blind interpretation.
- Capture final screenshots and compare them with v2 at full size and thumbnail
  size.
- Promote only after user approval; retain v2 archive.

## 11. Acceptance matrix

### Silhouette

- The interface is recognizable as a bounded engineered object at thumbnail
  size.
- Removing all text still leaves a distinctive chassis and workbench rhythm.
- The utility rail, structural chrome, workbench, and floating selection layer
  have unambiguous ownership.

### Composition

- No critical screen is a sidebar plus a set of equal white cards.
- One dominant instrument is visible above the fold.
- At least three module proportions are used purposefully.
- Gaps are tight enough to create a continuous field but never compromise
  grouping.

### Instrumentation

- Every large tile answers a named diagnostic question.
- The three critical frames collectively include at least six distinct
  micro-instrument types.
- Charts expose scale/units and use non-color differentiation.
- The topology exposes direction, state, and at least one inspectable signal.

### Material and depth

- A minimum of four layer levels remain distinguishable in greyscale.
- Inner contour/border performs more work than drop shadow.
- Only selected or temporary surfaces receive obvious elevation.
- Glass never sits behind dense data.

### Interaction

- Current scope, selected object, and active path are visually connected.
- Controls appear near the object they affect.
- Focus brackets, reticles, chips, and leader lines correspond to real
  interaction or evidence.
- Selection does not depend on a full yellow fill.

### Color

- Yellow is the brightest local signal and has one clear owner per region.
- Orange degradation and yellow selection remain distinguishable together.
- Healthy state is understandable without a green stripe on every object.
- Stale/unknown is expressed through geometry, pattern, text, and time.

### Typography

- Primary values and states dominate supporting text.
- Machine values, units, IDs, rates, and time align consistently.
- Paragraphs do not occupy the central diagnostic stage.
- Dense evidence remains readable at 100% zoom.

### Reference fidelity

For each critical frame, reviewers must be able to identify concrete evidence
of at least four reference-derived principles without using source colors:

- equipment faceplate;
- nested chassis;
- continuous relationship datum;
- moulded structural chrome;
- heterogeneous bento instruments;
- editorial focus/callout layer.

If the evidence can only be described as “rounded,” “minimal,” or “uses
yellow,” the frame fails.

## 12. Explicit non-goals

- Do not copy source colors, logos, typography, content, or device mockups.
- Do not create fleet-management, mission, navigation, map, or autonomy views.
- Do not add decorative sci-fi HUD marks.
- Do not make every surface glass, glowing, floating, or dark.
- Do not trade operational legibility for cinematic presentation.
- Do not change the platform model or safety-control semantics in a visual pass.
- Do not rebuild all nine screens before the three critical frames are approved.

## 13. Delivered implementation

1. V3 foundations specimen with dark/hybrid and paired light expressions.
2. V3 component stage covering chassis, instruments, topology, focus, paths,
   annotations, and evidence.
3. Three approved critical stress-test frames.
4. Remaining six storyboard frames derived from the approved system.
5. Updated Figma tokens/styles only where the new system demonstrates repeated
   need.
6. Before/after screenshot set and reference-fidelity scorecard.
7. Updated `FIGMA_IMPLEMENTATION.md`, `DESIGN_GUIDELINES.md`, tokens, and
   decision log after implementation—not before visual validation.
