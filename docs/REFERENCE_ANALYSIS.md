# Visual reference analysis

## Purpose and method

This document records the visual grammar extracted from the supplied and
visually verified references. Queued but inaccessible sources are listed
separately and do not contribute visual claims. It deliberately excludes source color palettes. Color for
ExRobotics comes from the established brand system, led by ExRobotics yellow;
the references contribute composition, geometry, hierarchy, depth, typography,
data treatment, and interaction character.

The references are not templates to copy. They are evidence for a coherent
interface identity. The analysis therefore asks five questions of each image:

1. What gives the interface its recognizable silhouette?
2. How are navigation, content, and temporary controls layered?
3. How do modules relate to one another in scale and spacing?
4. What makes a tile feel like an instrument rather than a generic card?
5. Which details should be retained, translated, or rejected for an internal
   engineering interface?

## Executive finding

The shared visual language is a **layered instrument chassis**.

It consists of a large, clearly bounded application shell containing nested
navigation strata and a field of mixed-span modules. Modules have substantial
corner radii, fine edge definition, and quiet depth. The most important modules
contain an internal diagram, trace, matrix, orbit, topology, or other
purpose-built micro-instrument. Small capsules, reticles, brackets, cursors,
and anchored annotations make the interface feel inspectable and live.

This is materially different from a conventional SaaS dashboard. A standard
sidebar beside equal metric cards is not enough. The reference character comes
from the whole spatial system:

- an inset chassis rather than an edge-to-edge webpage;
- two or more deliberate depth strata;
- mixed module sizes rather than a repeated card row;
- internal visual instruments rather than text-only summaries;
- fine technical framing rather than prominent drop shadows;
- selected objects that float, glow, bracket, or reveal controls;
- generous negative space inside modules despite high overall information
  density.

The two references added on 2026-08-20 extend this grammar with an
**editorial focus layer**: an isolated product or live instrument can be shown
in context, with a small number of anchored explanatory plates and a clear
visual sequence. This is useful for onboarding, guided inspection, focus mode,
and design-system presentation; it must not replace the dense operational
workbench.

The 2026-08-21 comparison against the rendered v2 Figma frames confirmed that
the written synthesis remains valid but has not yet been expressed strongly
enough in the implementation. The complete gap analysis and corrective plan
are recorded in `VISUAL_STYLE_V3_PLAN.md`.

## 2026-08-20 additions

### `../reference/presentation-only/pres-001__editorial-mobile-turbine-app__device-mockups.jpg`

#### Composition and silhouette

- A tall, near-black editorial field holds three oblique device views and
  three small floating feature plates.
- Product hardware is isolated by large regions of negative space rather than
  boxed into a conventional grid.
- The sequence moves from one primary instrument to a paired comparison,
  creating a simple top-to-bottom narrative.
- A mixed-weight headline, tiny category marker, and page number make the
  composition read like a designed technical case-study plate.

#### Geometry, material, and depth

- Devices and callouts occupy different depth planes; overlap establishes
  ownership without large shadows.
- Callout plates use low-contrast dark surfaces, small radii, and one bright
  square signal marker.
- Fine dotted leader lines connect explanation to context while remaining
  subordinate.
- Oblique hardware, restrained reflections, and local lighting create a
  physical instrument character.

#### Interface character

- The device interfaces combine compact labels, thin dials, radial readouts,
  direct values, and sparse navigation.
- The bright accent is scarce and therefore immediately identifies a current
  reading, selection, or primary action.
- Background detail is deliberately suppressed so the active instrument reads
  first.

#### Adopt for ExRobotics

- A focus/presentation mode that isolates one robot subsystem, path, or
  instrument and surrounds it with only the explanations required for the
  current task.
- Small numbered explanation plates with short titles and one-sentence
  consequences for onboarding, incident review, and design documentation.
- Anchored leader lines only when they encode a real relationship to a node,
  control, or state.
- Hardware-in-context views for explaining where a subsystem lives on the
  robot; ExRobotics yellow replaces the source accent semantics.
- Intentional alternation between a dense workbench and a spacious selected-
  object state.

#### Translate rather than copy

- Keep the operational desktop interface crisp and readable; use cinematic
  darkness primarily for focus mode, presentation, or a carefully calibrated
  dark expression.
- Replace phone mockups with robot, compute-node, network, CAN, camera, and
  subsystem objects.
- Use radial instruments only for values with meaningful thresholds, range,
  orientation, or cyclic structure. Prefer traces, matrices, and topology for
  ordinary telemetry.
- Scale explanatory text and contrast for engineering use rather than copying
  the source's very small editorial typography.

#### Reject

- Decorative device mockups inside daily platform screens.
- Low-contrast tiny labels, unexplained radial charts, or theatrical glow.
- Leader lines that merely decorate empty space.
- Replacing information density with presentation spectacle.

### Solar21 application case study

Source: [Solar21 App case study](https://www.webfelipe.com/solar21-app.html)

The source explicitly frames the work as a full interface redesign toward a
modern, technological, clean, minimalist UI and a simplified in-app flow. Its
value to ExRobotics is the combination of instrument-like monitoring with a
clear product narrative: individual views should each have one dominant job,
and a sequence of views should explain a workflow rather than repeat a generic
dashboard template.

Adopt the following principles:

- give each view one dominant engineering question;
- simplify task progression even when the underlying system is complex;
- show the monitored object and its primary reading together;
- reveal secondary controls and explanation in attached layers;
- use product-storytelling compositions for onboarding, handover, guided
  diagnosis, and visual-identity documentation.

The case study is not evidence for the ExRobotics palette. The brand's yellow,
neutral foundations, semantic colors, typography, and accessibility rules
remain authoritative.

## 2026-08-21 queued source

### Robotics Fleet Platform Dashboard & Brand System

Source: [Robotics Fleet Platform Dashboard & Brand System](https://dribbble.com/shots/27644169-Robotics-Fleet-Platform-Dashboard-Brand-System)

This Dribbble shot is intentionally **not yet analysed**. The protected live
viewer returned no visual content, direct retrieval was challenged, and no
indexed copy was available. Its title makes it relevant to the question of
brand-to-product continuity, but does not provide evidence for any particular
layout, palette, typography, component, or interaction choice.

Once a verified capture is available, review it with
`REFERENCE_INTAKE_METHOD.md`. Fleet-management subject matter remains outside
scope; only transferable visual grammar may be considered.

## 2026-08-22 screened reference library

The reference library now contains 33 direct, screen-like UI images plus one
device-mockup composition isolated under `reference/presentation-only/`.
The online batch covers topology, observability, industrial operations,
instrumentation, dense workbenches, editorial hierarchy, and restrained
floating/glass material studies. Exact names and provenance are recorded in
`../reference/CATALOG.md` and `../reference/SOURCES.tsv`.

Collection is not adoption. These new sources expand the comparison set but do
not change the identity rules in this document until a visual trait has been
analysed, translated to the ExRobotics platform-layer context, and explicitly
accepted. Source colors remain non-authoritative; ExRobotics yellow remains the
lead signal.

## 1. `ref-001__dark-resource-overview__stacked-utilization-instrument.jpg`

### Composition and silhouette

- The layout reads as a single equipment faceplate rather than a collection of
  cards.
- A sparse title-and-totals band occupies the upper half. A single framed
  analysis module occupies the lower half.
- The main chart is not floating independently; its filters, legend, grid, and
  data share one continuous enclosure.
- Small corner brackets at the outer edge and around values establish a visual
  language of capture, scope, and targeting.

### Geometry and spacing

- Rectilinear geometry dominates. Corners are mostly square or minimally
  rounded.
- Large voids around the title and resource totals create tension and clarity.
- The chart region uses tight internal spacing, thin divisions, and a regular
  horizontal/vertical grid.
- Repeated small square markers produce rhythm without relying on illustration.

### Typography and data

- Display lettering is treated as part of the instrument surface.
- Operational totals use strong alignment and large contrast between labels and
  values.
- The legend is compact, code-like, and directly associated with the graph.
- The chart is dense but legible because every data mark follows a strict grid.

### Interaction cues

- Brackets imply that a value, legend item, or region can be selected or scoped.
- Compact filter controls sit inside the chart enclosure rather than in a
  separate toolbar.
- The graph reads as a live diagnostic surface, not a passive report.

### Adopt for ExRobotics

- Focus brackets and corner reticles for live capture, selected topology nodes,
  trace scopes, and diagnostic regions.
- A single enclosure that joins filters, legend, visualization, and metadata.
- Strong separation between sparse summary zones and dense analysis zones.
- Hairline grids, strict alignment, compact legends, and machine-like labels.

### Translate rather than copy

- Use Space Grotesk for large hierarchy and Roboto Mono for machine values; do
  not reproduce the segmented display face as the default typography.
- Apply substantial rounding only where the broader ExRobotics system calls for
  a floating module; preserve the rectilinear discipline inside diagrams.
- Use ExRobotics yellow for the active scope, current sample, or selected series.

### Reject

- Terminal styling on every screen.
- Decorative brackets around every value.
- Unlabelled series or dramatic chart treatment without diagnostic meaning.

## 2. `ref-002__dark-contract-dashboard__tall-crop.jpg`

### Composition and silhouette

- A tall, persistent navigation slab forms one edge of a larger application
  chassis.
- The navigation itself contains distinct zones: workspace switcher, primary
  routes, object hierarchy, and a bottom utility/promotion module.
- The content is arranged in bands: heading, summary modules, a dominant chart,
  then a horizontally repeated object collection.
- The outer shell and inner modules share a coherent corner language.

### Geometry and spacing

- Fine strokes and small surface-value changes carry most separation.
- Drop shadows are nearly absent; depth comes from borders, nested frames, and
  subtle inset treatment.
- Module radii are generous enough to soften the dense grid without turning
  modules into pills.
- Summary cards use asymmetric internal divisions, allowing an icon or object
  silhouette to occupy a secondary compartment.

### Typography and data

- Large values are isolated with enough empty space to become visual anchors.
- Labels remain quiet and secondary.
- The chart uses a solid path, a secondary dashed path, and hatching, showing
  that series can differ through stroke and texture rather than hue.
- Object cards combine a large symbolic area, a title/description block, and a
  compact action row.

### Interaction cues

- Selected navigation is an inset plate, not merely bold text.
- Search and shortcut hints are embedded in the navigation.
- Card actions live in a stable footer region.
- Layered object silhouettes suggest history, multiplicity, or stacked assets.

### Adopt for ExRobotics

- The chassis-with-navigation silhouette.
- Navigation zones with clear ownership and a persistent bottom utility area.
- Summary modules with a secondary compartment for a microvisualization,
  topology glyph, or component silhouette.
- Mixed line styles and hatching for comparison data.
- Stable card anatomy: header, instrument stage, metadata, action/footer.

### Translate rather than copy

- Replace business objects with compute nodes, storage volumes, buses, services,
  and subsystem objects.
- Replace generic welcome content with context such as node name, platform
  state, build, and data freshness.
- Use ExRobotics yellow for selected navigation, active scope, or the current
  trace—not as a folder-decoration palette.

### Reject

- Generic dashboard greetings.
- Repeated cards when a table, trace view, or dependency map is more useful.
- Muted contrast so low that long diagnostic sessions become tiring.

## 3. `ref-004__light-health-dashboard__treatment-timeline-crop.jpg`

### Composition and silhouette

- The interface is organized as a continuous systems map rather than a stack of
  dashboard sections.
- A broad header ribbon contains navigation capsules and a compact summary row.
- A fine horizontal datum line, interrupted by a highlighted anchor, separates
  overview from the relationship field below.
- Cards and capsules become nodes connected by thin paths.

### Geometry and spacing

- The composition mixes a large continuous silhouette with small floating
  islands.
- Full pills are reserved for filters, tags, and compact objects.
- Larger information containers retain a softer rectangular shape rather than
  becoming capsules.
- Thin, mostly orthogonal or gently curved connectors provide continuity across
  generous empty space.

### Typography and data

- Labels are compact and arranged in short horizontal groups.
- Important readings are presented as small clusters rather than giant KPI
  cards.
- Content density rises around the relationship nodes and relaxes elsewhere.

### Interaction cues

- The highlighted anchor on the datum line reads as a current step, selected
  date, or active inspection point.
- Pills act as filters or object tokens that can be followed along connections.
- Connected nodes imply drill-in and causal/dependency navigation.

### Adopt for ExRobotics

- A relationship-first view for boot sequence, message flow, dependency chains,
  device buses, and data lineage.
- A continuous datum or timeline with one active anchor.
- Compact pill filters and interface/topic tokens attached to paths.
- Floating nodes with sufficient surrounding space to make the system legible.

### Translate rather than copy

- Replace the organic domain imagery with system nodes, ports, topics, buses,
  services, and sensors.
- Keep connectors directional and stateful. Every path should expose meaning,
  latency, throughput, or status.
- Retain ExRobotics geometry and typography rather than the source brand's
  organic identity.

### Reject

- Decorative connection lines without inspectable endpoints.
- Large ornamental curves that do not encode system structure.
- Pills used for paragraphs or complex content.

## 4. `ref-005__light-frosted-workflow-dashboard__tall-navigation.jpg`

### Composition and silhouette

- The most distinctive feature is a two-stage navigation system embedded in a
  large rounded application shell.
- A narrow utility rail floats beside a broader contextual navigation panel.
- The main content sits in a third, still larger framed plane.
- Navigation and content read as neighboring physical layers rather than a
  flat sidebar and page.

### Geometry and spacing

- Large outer radii, medium panel radii, and smaller control radii create a
  clear nesting hierarchy.
- Soft inner highlights and thin outer strokes make panels feel moulded or
  machined.
- Gaps between major panels are small and controlled, so the whole composition
  remains one chassis.
- Selected navigation is a luminous inset plate with a counter or trailing
  control.

### Typography and data

- The type hierarchy is plain and restrained, allowing material and structure
  to carry the identity.
- Section labels and counters are quiet.
- Large numbers occupy a dedicated instrument tile with very little supporting
  text.

### Interaction cues

- The utility rail suggests switching between broad tool modes.
- The contextual panel changes its contents within the selected tool mode.
- Search, counters, disclosure, and hierarchy are integrated into navigation
  rows.
- The selected row has depth and a trailing indicator, not just a color change.

### Adopt for ExRobotics

- Dual navigation only when the information architecture genuinely has global
  tools and contextual routes.
- A visible shell with nested material strata.
- Inner highlight plus outer hairline as a signature edge treatment.
- Selected navigation as an inset instrument plate.
- Counters and live-status indicators aligned to the trailing edge of rows.

### Translate rather than copy

- Glass belongs to structural chrome, floating command surfaces, and selected
  controls. Data tables, logs, and graphs remain optically crisp.
- Blur should soften what is behind a layer without reducing the foreground's
  legibility.
- Use yellow as the active optical signal within the selected plate.

### Reject

- Applying blur to every tile.
- Simulated material with no information hierarchy.
- Oversized soft shadows that make the interface feel like consumer hardware.

## 5. `ref-003__dark-contract-dashboard__wide-workbench.jpg`

This is the wide-system expression of reference 2 and provides better evidence
for proportion, scan order, and module behavior.

### Composition and silhouette

- The navigation slab occupies roughly one fifth of the usable width.
- The main work area begins with four compact summary instruments.
- The middle row splits into a wide trace module and a narrower structured-list
  module.
- The final row becomes a horizontal library of larger object modules.
- Every row has a distinct purpose and density; the page is not an undifferentiated
  grid.

### Geometry and spacing

- Gaps are narrow relative to tile dimensions, creating a continuous bento
  field.
- The largest module spans approximately twice the width of its neighbor.
- Summary modules are short and wide, analytic modules are deeper, and object
  modules are portrait-like.
- Tile edges align precisely across rows even when spans differ.

### Typography and data

- Summary values dominate their tiles.
- Analytic modules use small titles and reserve most space for actual data.
- Table rows are shallow, repetitive, and easy to scan.
- Object modules use a stable three-zone anatomy.

### Adopt for ExRobotics

- A 12-column bento field with purposeful 3-, 4-, 6-, 8-, and 12-column spans.
- Distinct module depths for summary, analysis, topology, and object inspection.
- A wide analytic module paired with a narrower event or subsystem list.
- Strict edge alignment across heterogeneous tiles.

### Translate rather than copy

- Summary row: processor, memory, accelerator, network or storage.
- Analytic row: utilization/thermal trace paired with events, logs, or interface
  state.
- Object row: comparable services, devices, volumes, or subsystem units only
  when a repeated-card view is genuinely useful.

### Reject

- A four-KPI row as the default for every page.
- Card repetition without comparison value.
- Headline greetings that consume space but add no engineering context.

## 6. `ref-006__dark-instrument-system__mixed-tile-grid.jpg`

### Composition and silhouette

- This reference offers the clearest expression of the desired module field.
- Large rounded tiles form an uninterrupted bento matrix with very small
  gutters.
- The crop continues beyond every edge, implying a larger navigable workbench
  rather than a finite report page.
- Each tile is visually autonomous but shares the same external dimensions,
  edge treatment, and internal restraint.

### Geometry and spacing

- Tile radii are substantial and consistent.
- Each tile has a low-relief outer edge and a faint inner contour.
- Internal diagrams use fine lines, small nodes, nested rectangles, arcs, and
  soft fields that remain subordinate to the tile boundary.
- Information rarely touches a tile edge; instrument stages have generous
  internal breathing room.

### Typography and data

- Text is sparse. A small label, one strong value, or one annotation is often
  enough.
- Numeric readouts and short labels float near the visualization rather than
  being forced into a conventional card header.
- The strongest hierarchy is created by scale and placement rather than by
  multiple type weights.

### Interaction cues

- Cursor arrows, focus points, plus controls, toggles, chips, and highlighted
  paths make the modules look actively manipulable.
- Annotation capsules are attached to data points or paths.
- Radial selectors and node graphs imply direct manipulation.
- Some modules expose only the currently relevant control; the rest remains
  visually quiet.

### Adopt for ExRobotics

- The bento workbench as the primary overview/inspection canvas.
- Every signature tile should contain a useful micro-instrument: trace, matrix,
  topology, orbit, distribution, comparison, or state map.
- Anchored annotation capsules for thresholds, deltas, interfaces, selected
  nodes, and current samples.
- Sparse, contextual controls revealed by selection or hover.
- Continuous workbench crops where appropriate, suggesting pan, scroll, or
  drill-in beyond the visible set.

### Translate rather than copy

- Keep labels and diagnostic lines brighter and more explicit than the source
  when accessibility requires it.
- Use ExRobotics yellow for the active path, focus node, current sample, or
  selected control.
- Use the larger tile radius as a signature on workbench modules while keeping
  dense tables and small controls more rectilinear.

### Reject

- Abstract graphs that cannot be explained in one sentence.
- Ambient glow that substitutes for state or hierarchy.
- A wall of identical square tiles when the underlying tasks need different
  spans.

## Cross-reference visual grammar

### A. The chassis

The application should read as a designed object. On large screens, inset the
primary shell from the viewport when space permits. Give the shell a clear
outer silhouette and contain the navigation and main workbench within it.

The chassis may be light or dark. Its identity comes from its geometry and
layering, not from the source references' colors.

### B. The navigation strata

Navigation is part of the chassis rather than an unrelated column. Use:

- a narrow utility rail for global tools only;
- a wider contextual panel for the selected tool or system domain;
- inset navigation plates for selection;
- trailing counters or live-state marks;
- a stable bottom utility or environment region.

Do not add a utility rail merely to imitate the references. It is appropriate
only when the product has two real levels of navigation.

### C. The bento field

The content area is a continuous matrix of heterogeneous instruments. Tile
spans and depths communicate purpose:

- compact and wide for summaries;
- large and wide for traces or topology;
- narrow and tall for ordered events or state lists;
- medium portrait modules for comparable objects;
- square modules for direct-manipulation instruments.

The grid should remain visually continuous through consistent gutters, aligned
edges, and shared external geometry.

### D. The micro-instrument

A signature tile is not a rounded rectangle containing three lines of text. It
has an internal stage that answers a diagnostic question. Appropriate stages
include:

- time-series traces and ranges;
- dependency or message-flow paths;
- node/link topology;
- resource matrices;
- radial selectors or distributions;
- state timelines;
- port/interface diagrams;
- compact tables with a selected row;
- comparison silhouettes or stacked layers.

Every visualization must expose its scale, state, or inspectable meaning.

### E. Edge treatment

The references consistently favor low-relief definition:

1. a fine outer stroke;
2. a subtle inner highlight or inset contour;
3. minimal, broad ambient shadow only where a surface genuinely floats;
4. a stronger focus ring, bracket, or glow for the selected object.

This edge stack is more important to the identity than strong gradients.

### F. Interaction marks

Use small, precise marks to make the interface feel live:

- focus brackets;
- reticles or active points;
- path-attached annotation chips;
- compact plus/minus or expand controls;
- cursor-proximate values;
- trailing counters;
- small command capsules;
- selected-path emphasis.

These marks must describe actual behavior. Decorative cursors, controls, or
graphs are prohibited.

### G. Density rhythm

The references alternate density rather than applying one density everywhere:

- shell and navigation: calm, structured, moderate density;
- summary instruments: sparse;
- traces, topology, and tables: dense;
- selected object detail: focused and spacious;
- supporting metadata: compact and monospaced.

This alternating rhythm prevents both sterile emptiness and dashboard clutter.

## Resolved tensions

### Hard instrument vs. soft material

Use hard, exact geometry inside the instrument stage and softer geometry for
the module and chassis silhouette. Data stays precise; the containing product
feels refined.

### Floating tiles vs. continuous system

Tiles share a continuous grid and edge language. Only selected, temporary, or
direct-manipulation surfaces receive additional elevation.

### Light glass vs. diagnostic clarity

Translucency belongs to structural chrome and temporary control layers. Dense
data remains on opaque surfaces with high-contrast marks.

### Large radii vs. engineering seriousness

Large radii are acceptable on the outer chassis and signature workbench
modules. Small controls, tables, brackets, grids, and diagrams stay exact. The
contrast between soft enclosure and hard instrument creates the identity.

## Reference fidelity test

Before calling an ExRobotics screen aligned with these references, verify that
it passes all of the following without relying on color:

1. **Silhouette:** the screen reads as an intentional chassis, not a generic
   webpage.
2. **Layering:** navigation, workbench, module, and control layers are visually
   distinct.
3. **Bento rhythm:** modules have purposeful mixed spans and aligned edges.
4. **Instrument content:** at least one primary module contains a meaningful,
   inspectable visualization or relationship view.
5. **Edge character:** hairlines and inner contours carry more structure than
   drop shadows.
6. **Interaction evidence:** selected scope, active path, or direct-manipulation
   cue is visible.
7. **Density rhythm:** sparse and dense zones alternate deliberately.
8. **Color independence:** removing yellow and semantic hues would still leave
   a recognizable ExRobotics composition.

## Final synthesis

The refined direction remains **Signal Instrumentation**, now defined more
strictly as:

> A layered systems chassis containing a continuous bento workbench of
> low-relief, directly inspectable engineering instruments.

ExRobotics yellow remains the lead optical signal for active scope, focus,
selection, current data, and decisive action. It is applied to this structural
language; it is not the source of the language itself.
