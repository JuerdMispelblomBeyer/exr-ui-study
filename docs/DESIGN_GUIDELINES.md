# ExRobotics engineering interface visual identity

## 1. Status, scope, and authority

This is the canonical visual-identity specification for the ExRobotics internal
engineering interface. It governs foundations, components, reference screens,
and future product views.

The product covers platform introspection and diagnostics: compute, memory,
accelerators, storage, services, containers, subsystems, buses, network links,
telemetry, logs, events, configuration, health, and dependencies.

Fleet management, mission planning or execution, routing, checkpoints,
dispatch, and autonomy controls remain outside scope.

The supplied references define visual grammar, not color. Their source palettes
must not be sampled or imported. ExRobotics brand colors remain authoritative,
with yellow as the lead optical signal.

Existing Figma screens are implementation drafts. When they conflict with this
document or the reference analysis, this document wins.

The 2026-08-21 audit found that Visual Style v2 does not pass the
reference-fidelity gates. Treat it as the preserved UX/content baseline.
Visual Style v3 is now implemented as archive-safe sibling sections following
`VISUAL_STYLE_V3_PLAN.md`; it is the current visual-reference candidate pending
user promotion. Its validated Figma nodes and exports are recorded in
`FIGMA_IMPLEMENTATION.md`.

Product structure, navigation, user flows, layout regions, and screen intent
are defined in `UX_ARCHITECTURE.md`. Safety-state and stop-control interactions
are provisional in `SAFETY_CONTROLS.md` and require safety-engineering review.
This document supplies their visual expression; it does not replace them.

## 2. Identity definition

### Direction name: Signal Instrumentation

Signal Instrumentation is:

> A layered systems chassis containing a continuous bento workbench of
> low-relief, directly inspectable engineering instruments.

It should feel like a precise piece of modern engineering equipment translated
into software—not a generic enterprise dashboard and not a theatrical command
center.

### The five signatures

A screen is recognizably ExRobotics only when most of these signatures are
present:

1. **Chassis silhouette** — navigation and content belong to one bounded,
   layered application object.
2. **Instrument bento** — heterogeneous modules share tight gutters and aligned
   edges; size expresses diagnostic purpose.
3. **Low-relief edges** — fine outer stroke, subtle inner contour, and minimal
   ambient elevation create physical definition.
4. **Micro-instruments** — primary tiles contain meaningful traces, topology,
   matrices, diagrams, or direct-manipulation stages.
5. **Yellow optical signal** — ExRobotics yellow marks the active scope,
   selected path, current datum, decisive action, or focus point.

The system must remain recognizable in greyscale. Yellow strengthens the
identity; it does not compensate for generic structure.

## 3. Core principles

### P1. Build a chassis, not a webpage

On large screens, compose the product as a coherent shell with nested
navigation and work surfaces. Avoid an unrelated sidebar placed beside a field
of ordinary cards.

### P2. Every major tile is an instrument

A major tile must answer a diagnostic question. A title, value, and sentence
inside a rounded rectangle is a summary card, not a signature instrument.

### P3. Structure before color

Hierarchy must survive with all semantic colors removed. Establish it through
silhouette, scale, grouping, edge treatment, typography, and density first.

### P4. Yellow means active signal

Yellow identifies current scope, focus, selection, live data, or the primary
action. Scarcity is mandatory so the signal remains legible.

### P5. Depth expresses interaction ownership

Persistent work surfaces sit in the chassis. Selected, temporary, or
direct-manipulation surfaces may float above it. Do not elevate every card.

### P6. Soft enclosure, hard instrument

Outer shells and signature modules may be generously rounded. Internal grids,
tables, chart axes, brackets, paths, and data marks stay exact and technical.

### P7. Dense and sparse zones alternate

Use sparse summaries and selected-object views beside denser traces, tables,
and topology. Uniform density makes the interface either empty or exhausting.

### P8. Relationships are first-class

When causality, flow, or dependency matters, show it spatially. Do not replace
a topology or sequence with unrelated cards. The current robot's stable spatial
grammar, object shapes, edge semantics, and degraded-path treatment are defined
in `SYSTEM_VISUALIZATION_SPEC.md`.

### P9. Machine truth is visually distinct

IDs, timestamps, ports, paths, rates, units, and version strings use the data
type system. Human explanation remains visibly different.

### P10. Details imply real behavior

Brackets, cursors, chips, reticles, handles, and plus/minus controls may appear
only when they correspond to an actual selectable, inspectable, or manipulable
state.

### P11. Brand and product share one formal language

Carry a small set of devices—yellow signal, chassis framing, hairline/inset
edges, monospaced machine metadata, focus brackets, and mixed instrument
spans—across product UI, system diagrams, onboarding, and presentation. Their
meaning must remain compatible in every context. Do not create a decorative
brand skin that contradicts operational behavior.

## 4. Spatial system

### 4.1 Application chassis

Desktop and large engineering displays should use a visible application shell
when the host environment allows it.

- Reference desktop viewport: 1440 px wide.
- Recommended viewport inset: 24–40 px.
- Chassis radius: 28 px.
- Major internal panel radius: 24 px.
- Workbench module radius: 20–24 px.
- Dense card radius: 12–16 px.
- Control radius: 8–12 px.
- Pills/status tokens: full radius.
- Chassis-to-panel gap: 8–12 px.

The shell may extend edge to edge in constrained embedded environments. Even
then, retain the nested strata through edges, spacing, and material treatment.

### 4.2 Navigation strata

Use one or two navigation layers according to the information architecture:

- **Utility rail:** 56–72 px wide. Global tool modes only.
- **Context navigation:** 208–248 px wide. Routes and hierarchy within the
  selected tool or system domain.
- **Main workbench:** remaining width.

If there is no genuine global/context distinction, omit the utility rail.
Imitating a two-rail reference without a two-level product model is prohibited.

The rail, context panel, and main workbench must read as neighboring pieces of
one chassis. Keep the gap narrow and the outer silhouette continuous.

### 4.3 Workbench grid

Use a 12-column desktop grid for instrument composition.

- Outer workbench padding: 24–32 px.
- Standard gutter: 12–16 px.
- Preferred spans: 3, 4, 6, 8, and 12 columns.
- Avoid one-off spans that break edge alignment.
- Align tile edges across rows even when tile heights differ.

Purposeful module proportions:

| Module purpose | Typical span | Typical depth |
|---|---:|---:|
| Compact summary | 3–4 columns | 136–176 px |
| Trace or resource history | 6–8 columns | 280–360 px |
| Events or subsystem list | 4–6 columns | 280–360 px |
| Topology/dependency stage | 8–12 columns | 360–560 px |
| Direct-manipulation instrument | 4–6 columns | 280–400 px |
| Comparable object tile | 3–4 columns | 240–320 px |

Do not use a four-summary-card row as a universal opening. The first row should
reflect the page's actual diagnostic priorities.

### 4.4 Continuous field behavior

The bento grid should feel like a continuous workbench rather than a collection
of isolated cards:

- use consistent external geometry and gutters;
- repeat the same edge stack;
- let related tiles share a baseline or axis;
- allow a larger tile to dominate a row;
- crop or continue the field beyond the viewport when the view genuinely pans,
  scrolls, or expands;
- avoid large empty bands between module rows.

## 5. Shape and radius hierarchy

Radius communicates scale and function.

| Token | Value | Use |
|---|---:|---|
| radius/small | 4 px | tiny marks, chart tags, internal nodes |
| radius/control | 8 px | compact controls, table selection |
| radius/card | 12 px | dense cards, logs, small panels |
| radius/expressive | 16 px | floating controls, selected dense panels |
| radius/panel | 20 px | standard workbench instruments |
| radius/instrument | 24 px | signature bento instruments, context panels |
| radius/chassis | 28 px | outer application shell |
| radius/full | 999 px | pills, status, compact filters |

Rules:

- Never give all objects the same radius.
- Full pills are for short controls and tokens, not content containers.
- Internal diagram geometry is usually 0–8 px even inside a 24 px module.
- Nested surfaces must step down in radius as they step inward.
- Avoid excessively soft 32+ px “pillow cards” unless the viewport and object
  scale justify them.

## 6. Surface and material system

### 6.1 Layer model

| Layer | Purpose | Typical treatment |
|---|---|---|
| L0 Canvas | environment behind product | quiet neutral field or atmosphere |
| L1 Chassis | complete application object | clear silhouette, broad ambient depth |
| L2 Structural panel | rail, context nav, workbench | fine border, subtle inner contour |
| L3 Instrument | trace, topology, metric, list | crisp surface, low-relief edge |
| L4 Floating control | palette, selected tool, tooltip | stronger edge/elevation, compact |
| L5 Overlay | dialog or blocking inspector | overlay elevation only |

### 6.2 Signature edge stack

The preferred surface definition is:

1. one-pixel outer border;
2. a subtle inner highlight or inset contour;
3. optional broad, low-opacity ambient shadow;
4. selected-state focus border, bracket, or glow.

The border and inner contour should do more visual work than the shadow.

### 6.3 Elevation

- **Inset:** inner highlight or inner shadow for selected navigation plates and
  moulded structural chrome.
- **Raised:** `0 2 6 0`, neutral/950 at 8%. Selected compact cards and controls.
- **Floating:** `0 6 16 -2`, neutral/950 at 12%. Featured instruments,
  popovers, and temporary panels.
- **Overlay:** `0 16 40 -8`, neutral/950 at 18%. Dialogs only.

Persistent tables, logs, and most instruments use borders without shadows.

### 6.4 Glass and blur

Instrument Glass is a limited structural material.

Use it for:

- utility rails;
- context navigation when layered over an atmospheric canvas;
- command palettes and floating search;
- temporary inspectors;
- selected floating controls.

Do not use it for:

- long tables;
- code/log surfaces;
- dense charts;
- persistent telemetry;
- every workbench tile.

Foreground content on glass remains opaque and high contrast. Blur describes
layer separation; it must not become the identity by itself.

## 7. Color identity

### 7.1 Source rule

The reference images do not contribute colors. Use the established ExRobotics
palette only.

### 7.2 Core neutrals

| Role | Light | Dark |
|---|---:|---:|
| Canvas | `#F8F9F7` | `#090B0A` |
| Surface | `#FFFFFF` | `#141715` |
| Subtle surface | `#F1F3EF` | `#242925` |
| Border | `#CDD2CA` | `#394039` |
| Primary text | `#141715` | `#F8F9F7` |
| Secondary text | `#515A51` | `#CDD2CA` |
| Muted text | `#8C958B` | `#8C958B` |

### 7.3 ExRobotics signal yellow

| Role | Value |
|---|---:|
| Signal soft | `#FFF8D6` |
| Selected surface | `#FFF0A3` |
| Signal bright | `#FFDA4D` |
| Lead signal | `#F5C400` |
| Focus/pressed | `#D9AA00` |
| Dark selected field | `#A57E00` |

Yellow usage priority:

1. selected path, node, sample, or active probe;
2. primary action;
3. selected navigation plate or utility tool;
4. focus border or reticle;
5. one attention module when necessary.

Use no more than one dominant yellow surface per local region. A screen may
contain several small yellow signals when they all describe the same active
scope.

Yellow is not the generic warning color. Warnings and critical states keep
their established semantic colors.

### 7.4 Supporting semantics

| Purpose | Soft | Strong |
|---|---:|---:|
| Healthy | `#DDF6E9` | `#177A4D` |
| Information/compute | `#E3EEFF` | `#2968C8` |
| Caution | `#FFF0D9` | `#C66B0A` |
| Critical | `#FCE4E2` | `#B93A36` |

Blue may describe comparison, compute, or network. Green is verified health.
Orange and red remain caution and critical. Status never depends on hue alone.

### 7.5 Gradients

Gradients are secondary atmospheric tools, not a substitute for the reference
geometry.

- Atmosphere: large canvas or shell only.
- Signal: selected/active instrument only.
- Compute: compute/network instrument where it aids domain recognition.
- Healthy: verified subsystem instrument.
- Dark gradients move no more than two neutral steps.
- Avoid putting a different pastel gradient on every card.
- Avoid strong diagonal transitions behind dense data.

## 8. Typography

### 8.1 Families

- **Space Grotesk:** product identity, page hierarchy, section and instrument
  titles.
- **Inter:** navigation, controls, body copy, descriptions, table labels.
- **Roboto Mono:** values, units, timestamps, IDs, ports, paths, rates, hashes,
  versions, and code-like metadata.

### 8.2 Established styles

| Style | Typeface | Size / line |
|---|---|---:|
| Display/XL | Space Grotesk Bold | 56 / 64 |
| Display/L | Space Grotesk Bold | 40 / 48 |
| Heading/H1 | Space Grotesk Medium | 32 / 40 |
| Heading/H2 | Space Grotesk Medium | 24 / 32 |
| Heading/H3 | Space Grotesk Medium | 20 / 28 |
| UI Body/L | Inter Regular | 16 / 24 |
| UI Body/M | Inter Regular | 14 / 20 |
| UI Body/S | Inter Regular | 12 / 18 |
| UI Label/M | Inter Medium | 14 / 18 |
| UI Label/S | Inter Medium | 12 / 16 |
| Data/Display | Roboto Mono Medium | 32 / 40 |
| Data/Value | Roboto Mono Medium | 16 / 24 |
| Data/Meta | Roboto Mono Regular | 12 / 18 |

### 8.3 Reference-inspired hierarchy

- Use one strong numeric or state readout per summary instrument.
- Keep supporting labels small and quiet.
- Reserve large headings for page context; do not fill every tile with a large
  title.
- Values may float near the relevant graph point or instrument stage rather
  than always sitting in a fixed top-left card header.
- Use uppercase 12 px labels sparingly for instrument categories and panel
  eyebrows.
- Do not introduce decorative segmented typography into the core system.

## 9. Navigation identity

### Utility rail

- 56–72 px wide.
- Icon target: 44–48 px.
- Consistent 20–24 px technical outline icons.
- Selected tool sits on an inset or raised plate.
- The selected icon may use the yellow signal; inactive icons remain neutral.
- Stable environment/settings utility belongs at the bottom.

### Context navigation

- 208–248 px wide.
- Divide into labeled zones such as Platform, Inspect, History, and
  Configuration only when they reflect the product model.
- Row height: 44–52 px.
- Selected row uses an inset plate, focus edge, and optional trailing counter.
- Search, hierarchy, disclosure, and live counts may be integrated into rows.
- Avoid a large brand mark or marketing block competing with engineering work.

### Main workbench header

Use a compact, context-rich header:

- node/system name;
- page purpose;
- freshness or connection status;
- active scope/filter;
- one primary action when needed.

Avoid generic greetings and large empty hero headers.

## 10. Instrument module grammar

### 10.1 Standard anatomy

A workbench instrument contains up to four zones:

1. **Context:** small category, title, or object identity.
2. **Readout:** one primary value, state, or selection.
3. **Instrument stage:** trace, topology, matrix, diagram, list, or relationship
   view.
4. **Control/metadata:** compact filter, time range, units, freshness, or action.

Not every tile needs all four. The instrument stage is mandatory for signature
analytic modules and optional for compact summaries.

### 10.2 Internal layout

- Standard instrument padding: 20–24 px.
- Large topology/trace padding: 24–32 px.
- Internal gap: 12–16 px.
- Instrument header height: 32–48 px.
- Compact footer/control band: 32–44 px.
- Data marks remain at least 16 px from the module edge.

### 10.3 Summary instruments

A summary instrument may be text-led, but should include at least one of:

- a small trace;
- a range or threshold mark;
- a component silhouette;
- a stacked layer indicator;
- a live delta chip;
- a compact state distribution.

Do not make all summary modules structurally identical.

### 10.4 Featured and selected instruments

Selection may add:

- yellow focus border or corner brackets;
- a subtle signal gradient;
- one level of elevation;
- revealed controls;
- an anchored annotation chip;
- a selected-path highlight within the instrument.

Do not enlarge, glow, shadow, and recolor the same tile simultaneously. Use the
minimum cues needed to establish ownership and focus.

## 11. Diagnostic visualization language

### 11.1 Trace instruments

- Use thin gridlines and clear units.
- Current/live series uses yellow.
- Comparison series uses blue or a neutral dashed line.
- Verified target band may use green.
- Thresholds use caution/critical semantics.
- Hatching or dash patterns distinguish overlapping data without relying on
  color.
- Direct labels are preferred over distant legends.
- A selected point may expose a compact anchored chip.

### 11.2 Resource bars and matrices

- Align marks to a visible grid.
- Keep bar width and spacing consistent.
- Use stacked values only when the parts explain the whole.
- Label time or sequence explicitly.
- Current interval or selected category receives the yellow signal.

### 11.3 Topology and dependency instruments

- Nodes inherit the module's surface/radius language at a smaller scale.
- Connectors show direction and state.
- Selected paths use yellow.
- Interfaces, ports, topics, rates, and latencies use Roboto Mono.
- Provide zoom, filter, inspect, and path-focus controls where the view is
  interactive.
- Preserve empty space around important paths.

### 11.4 Direct-manipulation instruments

Appropriate forms include radial selectors, state or resource matrices, node
graphs, range handles, trace scrubbers, and port maps.

- Show only the relevant controls until hover, focus, or selection.
- Place labels near the controlled object.
- Use reticles, cursor-proximate values, or handles only for real interaction.
- Maintain 44 px minimum targets even when the visible mark is smaller.

### 11.5 Event and log instruments

- Use dense, crisp, opaque surfaces.
- Reserve large radii for the outer module; rows remain more rectilinear.
- Selected rows use a quiet inset plate or focus border.
- Severity uses icon/text plus semantic color.
- Time, source, identifier, and key payload fields use Roboto Mono.

## 12. Micro-controls and annotations

### Command capsules

Use short floating capsules for time range, trace selection, interface filters,
zoom, view mode, and selected-object actions.

- Height: 32–40 px.
- Horizontal padding: 12–16 px.
- Radius: full or 12 px depending on content.
- Keep labels short.
- Attach the capsule to the relevant instrument rather than creating a global
  toolbar for every control.

### Annotation chips

Use for current value, delta, threshold, selected node, interface, or trace
label.

- Keep to one short line when possible.
- Anchor visually to the mark or path it describes.
- Use yellow for the current selection or active probe.
- Use semantic colors only for actual health/severity.

### Focus brackets and reticles

- Use around a selected node, live capture region, or diagnostic scope.
- Two or four corner marks are sufficient.
- Do not frame every card or value.
- Brackets supplement, rather than replace, accessible focus indicators.

## 13. Density system

Use three densities deliberately:

### Sparse

For primary readouts, selected-object focus, and direct-manipulation stages.
Large empty regions are acceptable when they clarify one state or relationship.

### Standard

For navigation, summaries, object cards, and most subsystem panels.

### Dense

For traces, event streams, logs, matrices, and configuration tables. Dense
content requires stricter alignment, smaller radii internally, and strong
contrast.

A good workbench alternates these densities. Do not apply the dense mode to all
surfaces or use sparse mode as an excuse to remove useful engineering data.

## 14. Light and dark expressions

### Signal Instrumentation / Light

- Warm-neutral canvas.
- Clear white or near-white instruments.
- Structural chrome may use restrained translucency.
- Fine grey borders and inner highlights define depth.
- Yellow remains the primary active signal.

### Night Console / Dark

- Same chassis, spans, radii, typography, and component API.
- Depth comes from stepped neutral surfaces and edge treatment.
- Borders and labels must remain visible during long use.
- Ambient glow is restrained and local.
- Yellow retains the same semantic meaning.

Dark is not a separate cyberpunk theme. Light is not a generic pastel
dashboard. Both expressions must pass the same color-independent identity test.

### Editorial focus layer

The 2026-08-20 references add a presentation grammar that may be used for
onboarding, guided diagnosis, incident explanation, hardware-context views,
and design-system demonstrations.

- Isolate one subsystem, selected path, or instrument as the visual subject.
- Use large negative space to clarify the subject, not to hide missing data.
- Add no more than three or four numbered explanation plates in one viewport.
- Connect a plate to its subject only with a precise anchored leader line.
- Keep each plate to a short title, one consequence-oriented sentence, and an
  optional state/value.
- ExRobotics yellow marks the current subject or active signal; it does not
  become ambient decoration.
- Preserve navigation escape, data freshness, and the selected robot context.

This layer floats above or expands from the normal workbench. It is not the
default layout for dense monitoring, logs, tables, or multi-system comparison.
Device mockups and cinematic hardware renders belong to product explanation,
not routine platform operation.

## 15. Motion and behavior

- Fast: 120 ms for hover and small state changes.
- Normal: 200 ms for selection, disclosure, and panel transitions.
- Slow: 320 ms for large layout changes.
- Standard easing: `cubic-bezier(0.2, 0, 0, 1)`.
- Emphasized easing: `cubic-bezier(0.2, 0, 0, 1.2)` only for a deliberate
  attention event.

Reference-aligned behaviors:

- selected navigation plate settles inward or becomes optically inset;
- selected instrument rises no more than 1–2 px or gains one elevation level;
- focused path or current trace draws on without displacing surrounding data;
- annotation chips appear from their anchor point;
- tile expansion preserves its original position and the user's mental map;
- glass layers do not drift or use decorative parallax.

## 16. Responsive behavior

### Desktop

- Preserve the full chassis and bento field.
- Use dual navigation only when justified.
- Keep at least one primary analytic or relationship instrument above the fold.

### Medium width

- Collapse the context panel before destroying instrument proportions.
- Move secondary filters into attached command capsules or a drawer.
- Reflow 3/4-column summaries to 6 columns.

### Mobile

- Utility rail becomes a compact tab bar or tool switcher.
- Context navigation becomes a drawer or scoped header.
- Stack instruments by diagnostic priority, not desktop left-to-right order.
- Preserve the instrument stage; do not reduce every module to text summaries.
- Keep 20 px outer padding, 12 px gaps, and 44 px targets.
- Large topology may become a focused, pannable viewport.

## 17. Screen composition recipes

These generic recipes are constrained by the factual topology in
`PLATFORM_SYSTEM_MODEL.md` and the visual-first layout rules in
`SYSTEM_VISUALIZATION_SPEC.md`. A factual system schematic takes precedence
over a generic metric-card composition.

### Platform overview

1. Compact system header with node/build/freshness.
2. Three or four non-identical summary instruments.
3. Wide resource/thermal trace paired with an event or interface-state module.
4. Topology or dependency instrument spanning most or all of the workbench.
5. Optional comparable subsystem objects.

### Compute inspection

1. Processor identity and current utilization readout.
2. Core/resource matrix or stacked interval bars.
3. Temperature/power trace with thresholds.
4. Process/container list with selected row.
5. Active annotation for the selected core, process, or time range.

### Network inspection

1. Interface identity and link state.
2. Throughput/loss trace.
3. Port or peer topology.
4. Packet/error event stream.
5. Selected path in yellow with latency/rate chips.

### Subsystem dependency view

1. Scoped subsystem header.
2. Large dependency/message-flow instrument.
3. Compact health distribution.
4. Selected-node inspector.
5. Boot/state timeline or relevant logs.

These are compositions, not fixed templates. Diagnostic purpose determines
spans and order.

## 18. Explicit anti-patterns

Do not ship:

- a flat sidebar beside three equal metric cards and a generic table;
- rows of identical rounded cards with only title/value/metadata;
- gradients as the primary source of identity;
- pastel category colors across every tile;
- thick shadows around all modules;
- full-screen glass or blur;
- decorative charts, cursors, controls, or topology;
- four-KPI openings on every page;
- oversized welcome messages;
- marketing language or consumer-product illustrations;
- rounded pills used as large content containers;
- uniform radius at every scale;
- a dark cyberpunk skin unrelated to the light system;
- a light SaaS skin unrelated to the dark system;
- status communicated by color alone;
- fleet, mission, route, checkpoint, dispatch, or autonomy concepts.

## 19. Accessibility and engineering QA

- Minimum interactive target: 44 × 44 px.
- Primary text meets WCAG AA against its surface.
- Neutral/950 text is used on yellow action surfaces.
- Status pairs color with text, icon, pattern, or shape.
- Focus remains visible independently of glow.
- Verify keyboard order, disclosure, hover-only controls, and reduced motion.
- Test long IDs, paths, units, timestamps, localization, and truncation.
- Charts expose units, scale, and non-color series differentiation.
- Topology paths expose direction and accessible labels.

## 20. Reference-fidelity acceptance gate

Before a screen can be described as applying this identity, it must pass all
eight checks:

1. **Silhouette gate:** it reads as an intentional systems chassis.
2. **Layer gate:** navigation, workbench, instruments, and floating controls
   have distinct ownership.
3. **Bento gate:** mixed spans are purposeful and edges remain aligned.
4. **Instrument gate:** a primary module contains a meaningful visualization or
   relationship view.
5. **Edge gate:** fine borders and inner contours matter more than shadows.
6. **Interaction gate:** the current scope, path, datum, or selected object is
   visibly inspectable.
7. **Density gate:** sparse and dense zones alternate deliberately.
8. **Greyscale gate:** the screen remains recognizably ExRobotics without
   yellow or semantic color.

After these pass, apply the yellow-allocation check:

- Is yellow the clearest active signal?
- Is it attached to real state or action?
- Is it scarce enough to remain dominant?

## 21. Intended character

Precise, calm, engineered, tactile, spatial, inspectable, purposeful, and
unmistakably ExRobotics.

Never generic, theatrical, game-like, decorative, or consumer-friendly at the
expense of machine truth.
