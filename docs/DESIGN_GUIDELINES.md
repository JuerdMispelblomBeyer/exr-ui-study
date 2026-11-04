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

### 1.1 How to read this specification

Every reusable decision belongs to one of four authority types:

- **Semantic principle** — why the system behaves or looks this way. Principles
  remain true when dimensions or technology change.
- **Design rule** — the normal construction or content choice. Follow it unless
  an explicit exception applies.
- **Token or specification** — an exact reusable implementation value. These
  live in `tokens/exrobotics-ui.tokens.json`; prose links to them rather than
  creating a second value.
- **Exception** — a deliberate, bounded break from a rule, with the diagnostic
  reason stated. A one-off visual preference is not an exception.

When prose and a token disagree, first decide whether the conflict is semantic
or numeric: this document owns semantics and rules; the token file owns exact
values. Record a material change in `DECISION_LOG.md` and update both sources in
the same change.

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

### P6. Calm enclosure, exact instrument

The application chassis may own a generous radius, but persistent evidence
fields use restrained 8–10 px corners and little or no elevation. Internal
grids, tables, chart axes, brackets, paths, and data marks stay exact and
technical. Softness is a scale cue, not the product's personality.

### P7. Dense and sparse zones alternate

Use sparse summaries and selected-object views beside denser traces, tables,
and topology. Uniform density makes the interface either empty or exhausting.

### P8. Relationships are first-class

When causality, flow, or dependency matters, show it spatially. Do not replace
a topology or sequence with unrelated cards. The current robot's stable spatial
grammar, object shapes, edge semantics, and degraded-path treatment are defined
in `SYSTEM_VISUALIZATION_SPEC.md`; the two approved view models and their
exceptions are defined in section 11.3a below.

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
- Canonical evidence fields and design-system specimens normally use 8–10 px;
  20–28 px belongs to the application chassis or a genuinely floating object.
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

> **Superseded for the dark expression, 2026-08-23.** The edge stack below is
> the light expression's. Dark separates surfaces with the inner light stack in
> 6.2a and keeps the border below the threshold of notice. See P12 and D034.


The preferred surface definition is:

1. one-pixel outer border;
2. a subtle inner highlight or inset contour;
3. optional broad, low-opacity ambient shadow;
4. selected-state focus border, bracket, or glow.

The border and inner contour should do more visual work than the shadow.

### 6.2a Selective inner light

**Status:** Refined 2026-08-24 by D038. The earlier rule that every plane must
carry a three-part inner-light stack is superseded.

Persistent planes are matte by default: one quiet fill, a structural border
only where containment needs it, and no shadow. Use the inner-light stack only
when it communicates raised ownership, selection, or temporary interaction.

| Layer | Value | Role |
|---|---|---|
| Top edge | `inset 0 1px 0 rgba(255,255,255,0.065)` | crisp catch-light on the upper border |
| Glow | `inset 0 12px 32px rgba(255,255,255,0.032)` | soft light falling from the top edge inward |
| Floor | `inset 0 -10px 26px rgba(0,0,0,0.16)` | bottom darkening that gives the surface volume |

A floating lens may run the stack at roughly 150 % — `0.085`, `0.05`, and
`0.20` — because it sits closer to the light. The selected inspector may also
use a 3 px signal edge instead of a diffuse glow.

When present, inner light is white and vertical. It never tints, never comes
from a corner, and never appears on an inset instrument stage. A single broad
neutral atmospheric wash may shape the page background; it is not repeated per
module.

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

Light derives from `primitives.neutral`. **Dark no longer does.** Its surfaces
are a separate cold-neutral set, `primitives.graphite`, at hue 210° and 18 %
saturation — the brand ramp sits near hue 120° and read as green once the dark
surfaces were lifted. See D034.

| Role | Light | Dark · iron |
|---|---:|---:|
| Canvas | `#F8F9F7` | `#121416` |
| Plane | `#FFFFFF` | `#1A1D20`, top `#1F2225` |
| Inset stage | `#F1F3EF` | `#16181B` |
| Control | — | `#262A2E` |
| Border | `#CDD2CA` | `#292D31` |
| Floating lens | — | `#2A2E32`, edge `#3A3F44` |
| Primary text | `#141715` | `#F8F9F7` |
| Secondary text | `#515A51` | `#CBD1D6` |
| Muted text | `#8C958B` | `#8B939B` |
| Garnish only | — | `#6D757D` |

`#6D757D` measures 3.6:1 on the dark plane and must never carry text a reader
needs. Anything nameable — a hex, a role, an axis value, a unit — sits at
`#8B939B` or lighter.

Light and dark are now paired by geometry, type, composition and component model
rather than by shared greys. Building the light expression requires a decision
about whether it follows dark into a cold neutral or stays on the brand ramp.

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

> **Dark expression, 2026-08-23.** The values below describe the light
> expression. Dark uses a fully saturated warm progression — signal `#F5C400`
> (48°), caution `#FF8A3D` (24°), critical `#FF5765` (355°) — separating by hue
> rather than lightness, with healthy left neutral. Green and blue are absent.
> See D032, D034 and `tokens/exrobotics-ui.tokens.json`.


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

- **Space Grotesk names things:** product and sheet names, module titles, and
  actual object names inside diagrams.
- **Inter carries human language:** navigation, controls, explanations,
  captions, notes, legends, descriptions, and table labels.
- **Roboto Mono carries machine truth:** measured values, units, timestamps,
  IDs, ports, paths, rates, hashes, versions, and code-like metadata.

Classify mixed strings by character run. For example, the label in
`rate 42/50 Hz` is Inter while `42/50 Hz` is Roboto Mono. Do not force the whole
line into one family for convenience. Section 8a defines the adopted dark scale
and supersedes section 8.2 for that expression.

### 8.2 Established styles

> **Superseded for dark by section 8a, 2026-08-23.** The scale below is the
> light expression's.


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

### 11.3a Approved spatial models

**Status:** Adopted 2026-08-24; recorded as D036. Exactly two spatial models
are approved. They may show the same objects and incident, but they answer
different questions and must remain visibly distinct.

#### Semantic principle

Choose spatial encoding by the diagnostic relationship, not by novelty. Object
identity, state, selection, and incident evidence remain stable when the model
changes; only the relationship being made legible changes.

#### Design rules

1. **Bus schematic** answers *which bus carries the fault?* Use literal,
   orthogonal wiring, horizontal rails, explicit drops, and a left-to-right scan
   within each bus. Rows imply depth; do not add decorative perspective.
2. **Hex cell cluster** answers *what is the compute core made of?* Use the
   tessellated core to show composition and membership, then fan out to attached
   subsystems. Adjacency is packing, not wiring; only drawn edges assert a
   connection.
3. Keep the object set, names, status, selection, and incident values identical
   when comparing the two models. A viewer must be able to switch models
   without relearning the platform.
4. Apply the type classification at character-run level: object names use
   Space Grotesk, explanations and legends use Inter, and values, units, IDs,
   and timestamps use Roboto Mono.
5. Nodes reuse the dark plate material at smaller geometry. Rails, grooves,
   connector dots, selected paths, and status treatments reuse
   `spatialModelsDark`, `surfaceDark`, `selectionDark`, and `statusDark`; do not
   redraw approximate variants.
6. Status never relies on colour alone. Keep the label, glyph, outline, or
   pattern that identifies the state, and preserve one brightest point per
   module.

#### Exceptions

- A bus with many drops does not tessellate: use the bus schematic even when a
  cluster would be more compact.
- A composition view may draw a small number of authoritative edges through or
  away from the cluster, but unconnected adjacency must never imply wiring.
- A new spatial model is permitted only when neither approved model can express
  the required diagnostic relationship. Document the new relationship and
  decision before adding it to the canonical page.

Layered strata is not an approved spatial model. Do not preserve it as an
active option, a navigation label, or an undocumented hybrid of the two models.

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

### Attached controls and tokens

Use compact attached controls for time range, trace selection, interface
filters, zoom, view mode, and selected-object actions. The default is a
rectilinear 5–8 px control. A full capsule is reserved for a removable token,
compact filter value, or genuinely floating transient control.

- Height: 32–40 px.
- Horizontal padding: 12–16 px.
- Radius: 5–8 px by default; full only when the object behaves as a token.
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
- an unapproved third spatial model or a hybrid whose adjacency and wiring
  semantics cannot be distinguished;
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

## 18a. Working principles learned in review

**Status:** Added 2026-08-23 from a reference-led revision of the graphite
sheet. These are the rules that changed the work most; they sit above the
detailed systems below.

### P12. Light before line

A surface is separated from its ground by light, not by an outline. The plane
gradient, the 1 px inner top highlight, the soft inner glow and the bottom floor
do the work; the border is calibrated to sit just below notice. A design whose
every surface is defined by a visible 1 px stroke reads as a wireframe no matter
how correct its spacing.

### P13. Colour spent on the nominal case is colour unavailable to the exception

Healthy is the absence of alarm, not a colour. When the CAN matrix rendered
every in-rate cell green, the one real anomaly was buried inside a wall of
colour; making the nominal case neutral did more for hierarchy than any amount
of added emphasis could have. Reserve saturated hue for the states that need a
response.

### P14. Garnish lives at 5 % or does not exist

Crosshairs, tick stubs, corner brackets, ghost grids and connector dots are
texture. Rendered at full strength they read as information, and the viewer
spends attention trying to decode something that carries none. There is no
useful middle setting: make it nearly invisible or delete it.

### P15. One brightest point per module

Hierarchy comes from removing competitors, not from amplifying the subject. If
three things in a module are equally bright, dim two rather than brightening the
third. The same rule scales up: a sheet or screen should have one focal module,
and it may carry a lifted plane and a stronger glow to say so.

### P16. Commentary out, metadata in

Design commentary — explanations of why a thing looks the way it does — belongs
in this document. Machine metadata — unit, source, threshold, freshness,
timestamp — belongs on the canvas beside the observation it qualifies. This is
the line that makes subtraction decidable instead of arbitrary. A footnote under
every module is a habit, not a design, and in practice it also failed contrast:
the 9 px grey it was set in measured 4.15:1.

### P17. Sort references before borrowing from them

A marketing surface carrying no information can afford restraint that a
diagnostic tool cannot. Establish which references are product UI and which are
presentation before transferring anything: take material and restraint from all
of them, but take information behaviour only from the ones that actually carry
information.

## 18b. Calm evidence-field composition

**Status:** Adopted 2026-08-24 after the reference-led graphite-sheet
recomposition; recorded as D037.

The system remains technically dense, but the density is concentrated inside
evidence rather than distributed across equally framed modules.

### Semantic principles

1. **One compositional peak.** A sheet or screen establishes one dominant
   object, path, or evidence field. Secondary specimens support that read.
2. **Concentrate complexity.** Dense topology, traces, matrices, logs, and
   machine metadata may remain dense; their surrounding shell stays quiet.
3. **Repeat anatomy, not chrome.** Related instruments share ordering,
   alignment, and behavior without each receiving an independent raised card.
4. **Elevation communicates ownership.** Persistent siblings are joined or
   inset. Full elevation belongs to selected lenses, overlays, and the single
   focal module.
5. **Accent is budgeted at page level.** A locally valid yellow state may still
   be too loud when many specimens are shown together. Overview documentation
   shows one dominant yellow event per macro-region.
6. **Matte is the persistent state.** Depth is evidence of ownership, not a
   blanket material recipe. Selected inspectors and transient controls may
   lift; the work surface stays quiet.

### Design rules

- Organize canonical visual documentation into a small number of macro
  chapters. Do not give every specimen its own eyebrow, divider, and ceremony.
- Alternate sparse orientation, standard grammar, and dense proof. Uniform
  section rhythm is not a virtue when the contents have different importance.
- Join related specimens on a continuous field with shared dividers or axes.
  Use independent cards only for genuinely independent or movable objects.
- Show canonical control and state examples at primary contrast. Exhaustive,
  disabled, historical, and edge variants move to a subordinate matrix or
  component inventory.
- Group with spacing and alignment before adding a closed border. A border must
  communicate containment, focus, state, or interaction.
- Use unequal spans when evidence has unequal diagnostic value. A trace may
  lead while a matrix verifies and narrow lanes compare; equal thirds are not a
  default composition.
- Keep diagram labels clear of rails and paths. Put language above or beside a
  line, preserve at least 10 px optical separation, and keep values aligned to
  a shared edge.
- Keep design commentary and provisional feedback prompts out of the canonical
  visual page. Durable rules live here; machine metadata stays beside evidence.

### Exceptions

- A true comparison set may give siblings equal weight when equivalence is the
  diagnostic question. The two approved spatial models are the canonical
  example, but they still share incident context and one comparison chassis.
- A selected inspector may overlap a persistent field and carry full floating
  material because the elevation communicates ownership.
- Dense evidence must not be removed merely to manufacture whitespace. Quiet
  the container before cutting diagnostic truth.

## 8a. Type system (dark expression)

**Status:** Adopted 2026-08-23. Supersedes the scale in section 8.2 for dark.

### 8a.1 What each family is for

The families are not decorative choices, they are a classification of the
content.

- **Space Grotesk** — identity and naming. Sheet title, module title, the name
  of an object inside a diagram. Nothing else.
- **Inter** — anything a human reads as *language*. Explanations, captions,
  module meta, notes, control labels, column headers, questions.
- **Roboto Mono** — machine truth only. A string is mono if and only if it
  contains a measured value, a unit, an identifier, a hostname, a path, a
  timestamp or a hex code.

**The most common failure is putting prose in mono.** `edge before shadow`,
`glyph + label` and `which object is causing the degradation?` are sentences,
not machine values; setting them in mono is what made earlier revisions read as
a spec dump rather than a product. If it would survive being read aloud, it is
Inter.

### 8a.2 Scale

| Token | Family / weight | Size / line | Tracking | Colour |
|---|---|---|---|---|
| `display` | Space Grotesk Medium | 46 / 52 | −2 % | `#F8F9F7` |
| `title` | Space Grotesk Medium | 22 / 28 | −1 % | `#F8F9F7` |
| `object` | Space Grotesk Regular | 15 / 20 | −0.5 % | `#F8F9F7` |
| `eyebrow` | Inter Regular, UPPER | 10 / 12 | +13 % | `#6D757D` |
| `body` | Inter Regular | 13 / 20 | 0 | `#CBD1D6` |
| `caption` | Inter Regular | 12 / 16 | 0 | `#8B939B` |
| `micro` | Inter Regular | 11 / 14 | +2 % | `#8B939B` |
| `data-xl` | Roboto Mono Medium | 34 / 40 | −2 % | value colour |
| `data` | Roboto Mono Regular | 12 / 18 | 0 | `#CBD1D6` |
| `data-s` | Roboto Mono Regular | 10 / 14 | +2 % | `#8B939B` |

Tracking rule: negative above 20 px, zero between 11 and 20, positive below 11.
Uppercase only at 10 px or smaller, and never without tracking.

One `display` per sheet. One `title` per module. One `data-xl` per module — if a
module needs two large numbers it is really two modules.

### 8a.3 Rules and exceptions

- Uppercase is a navigational or taxonomic device, not emphasis. Use it for
  tracked eyebrows and compact category labels at 10 px or smaller; names,
  sentences, notes, and status labels stay in their natural case.
- Tracking follows optical scale, not component type: negative above 20 px,
  zero from 11–20 px, positive below 11 px. Do not add tracking to make a weak
  hierarchy feel more technical.
- A mixed label/value string uses mixed runs. Preserve the machine fragment in
  Roboto Mono and the language fragment in Inter.
- An identifier that is also a user-facing object name may use Space Grotesk in
  the diagram and Roboto Mono in a log, filter token, or evidence table. The
  surrounding content class decides the intentional exception.
- Do not compress below the documented scale to fit commentary. Remove or move
  commentary to documentation; retain machine metadata beside its observation.

## 10a. Instrument anatomy

**Status:** Refined 2026-08-24 by D038. Every analytic module uses this order,
but status is annotation rather than mandatory chrome.

```text
title                                    caption, right-aligned
EYEBROW LABEL
data-xl  unit     [ status annotation ]  caption, right-aligned
── stage ────────────────────────────────────────────────────
caption: source · freshness
```

1. **Title row** — `title` left, `caption` right naming window and sampling.
2. **Eyebrow** — names what the big number *is*, in `eyebrow`. Without it a
   large number is ambiguous.
3. **Readout row** — `data-xl` with its unit at `data` size in a dimmed tone.
   Add a glyph plus short label, comparison, or threshold only when state needs
   explanation. The annotation may sit inline or right-aligned; it does not
   receive a pill by default.
4. **Stage** — chart, matrix or lanes, per section 20a.
5. **Source line** — `caption`, source and freshness.

Use a 26 px pill only for a removable or switchable status token. Persistent
status uses icon or pattern plus language and nearby machine evidence. Never
turn every healthy, degraded, selected, and filtered state into a capsule.

**Stage material.** Matte fills are the default. Bars, rails, and cells may use
a subtle vertical value shift or top highlight only when that helps distinguish
track from measure. Matrix cells keep a 3 px radius; topology rails stay exact.
Material must never compete with the measured state.

## 19a. Selection treatment

**Status:** Refined 2026-08-24 by D038. Supersedes any filled-block selection.

A selected element is an **outline, a tint and a soft falloff**. It is never a
filled yellow block.

| Layer | Value |
|---|---|
| Border | `#F5C400`, 1 px |
| Field | `rgba(245,196,0,0.07)`, or `0.05` across a large region |
| Falloff | optional radial `#F5C400` 0.10 → 0, reserved for a selected lens or direct-manipulation target |
| Glyph | `#F5C400` — the radio dot, check, icon or count |
| Label | `#F8F9F7` — **the label never turns yellow** |

Solid yellow is reserved for the single primary action in a region. Everything
else that is "on", "current" or "selected" uses the outline treatment: toggles,
checkboxes, filter chips, navigation items, selected rows, focused fields, time
flags.

Do not add a glow merely because an object is selected. An outline, a leading
edge, and a small path halo are normally sufficient. When spatial falloff is
needed it must be a radial gradient, never a second fuzzy border.

**A selected path is drawn, not filled.** Where selection follows a route
through a diagram, use a 2 px signal core and, only when separation is needed,
an 8 px halo at roughly 12 %. Place a filled 3–4 px dot at meaningful bends.
Diagram rails stop short of labels or labels sit at least 10 px off the rail;
machine truth must never be crossed by decorative or structural linework.

## 20a. Chart and plot style

**Status:** Adopted 2026-08-23 from a reviewed reference chart; recorded as
D033. This section is authoritative for every trace, plot, and time series. It overrides the earlier
container-and-tint treatment used in the first graphite sheet.

### 20a.1 Anatomy

A chart is four things and nothing else: a label gutter, a grid, one or more
series, and a label row. There is no plot container.

```text
[ y gutter ]│ plot area                                   │
  60 ───────┼─────────────────────────────────────────────┤ ← gridline
            │        ╭──────╮                             │
  40 ───────┼───╭────╯      ╰────╮────────────────────────┤
            │╭──╯   hatched area  ╰──╮                    │
   0 ───────┴────────────────────────────────────────────┘ ← baseline gridline
            Jan        Feb        Mar        Apr
```

### 20a.2 Rules

**Container.** None. The chart sits directly on its module plane. No inset well,
no border, no rounded box, no fill behind the plot. The gridlines define the
field.

**Grid.** Horizontal only, spanning the full plot width, 1 px, `#272B27`. One
line per labelled value, including the baseline. Never vertical gridlines, axis
rules, or tick marks.

**Labels.** Y values sit in a left gutter outside the plot, right-aligned to the
gutter edge, Roboto Mono 10 in `#565E55`, optically centred on their gridline.
X labels sit below the baseline with at least 20 px of clearance, same size and
colour, aligned to the position they name. Three to five gridlines; more is
noise.

**Primary series.** 2 px solid `#F8F9F7`, round joins and caps. One primary
series per chart.

**Primary area.** Diagonal hatching at 45°, 1 px lines on a 9 px pitch,
`#CDD2CA` at 13 %, clipped to the region between the curve and the baseline.
Never a flat tint and never a gradient — the hatch is what makes the chart read
as an instrument rather than a dashboard widget.

**Secondary series.** 1.5 px dashed `6 4` in `#6E776D`, no fill. A comparison or
prior period, never a threshold.

**Threshold.** 1 px dashed `4 3` in its semantic colour at 50 % opacity, full
plot width, value labelled at the right end.

**Probe.** 1 px dashed `#F5C400` vertical, plus a 3.5 px filled dot on the
curve. The dot is the brightest point in the chart.

**Forbidden.** Point markers on every sample, legends, data labels on the line,
vertical gridlines, tick marks, drop shadows on series, and more than one
hatched area per chart.

### 20a.3 The two rules that carry meaning

These are not stylistic. Breaking them makes the chart lie.

**Hatched area only when the axis includes zero.** Area encodes magnitude
measured from nothing. On a fitted axis that starts above zero, draw the line
alone. A rate chart zoomed to 35–55 Hz gets a line; a load chart running 0–60 %
gets the hatch.

**Curve shape must match how the data was observed.** Continuously sampled
telemetry gets gentle Catmull-Rom smoothing — it varies between samples because
the thing being measured did. Genuinely stepped values get plateaus joined by
short eased transitions. Never apply plateaus to continuous sampling: the
plateau is a claim that the value was held constant, and applying it decoratively
is exactly the design theater this system forbids.

**Axis choice.** Fit the axis to the observed range and keep zero in it where
that is possible. When a threshold falls outside the fitted range, state the
threshold in the module header instead of stretching the axis to reach it.

### 20a.4 Implementation

Figma imports SVG `clipPath` as a native vector mask, so the hatch is authored
as a clipped group of diagonal lines. SVG `pattern` fills do **not** import and
must not be used. Generate the curve, the clip path, and the hatch lines
programmatically rather than by hand.

## 21. Intended character

Precise, calm, engineered, tactile, spatial, inspectable, purposeful, and
unmistakably ExRobotics.

Never generic, theatrical, game-like, decorative, or consumer-friendly at the
expense of machine truth.
