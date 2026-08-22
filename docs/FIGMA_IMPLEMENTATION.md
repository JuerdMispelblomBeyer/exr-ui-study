# Figma implementation map

Last updated: 2026-08-21

## Visual Style v3 implementation

Visual Style v3 is implemented as archive-safe sibling sections. The v2
foundations, component stage, and nine-screen UX/content baseline remain
unchanged. V3 is the current visual-reference candidate pending user promotion.

| Page | V3 section | Contents |
| --- | --- | --- |
| 00 Cover & Foundations | `49:4706` | Graphite and paired-light chassis studies plus material, yellow-ownership, and micro-instrument rules |
| 01 Components | `50:5179` | Reusable chassis, topology, selected scope, resource, network, timeline, runtime, CAN, focus, path-value, and evidence patterns |
| 02 Engineering Interface | `50:5617` | Nine 1,440 × 900 Inspect → Diagnose → Change reference states |

V3 component masters:

| Pattern | Figma node |
| --- | --- |
| Application Chassis · Graphite | `50:5499` |
| Platform Topology | `50:5236` |
| Selected Scope | `50:5245` |
| Resource Matrix | `50:5284` |
| Network Pulse | `50:5300` |
| Causal Timeline | `50:5325` |
| Evidence Dock | `50:5331` |
| Evidence Plane · Expanded | `50:5573` |
| Runtime Stack | `50:5500` |
| CAN Distribution | `50:5501` |
| Focus Bracket | `50:5551` |
| Path Value Chip | `50:5552` |

V3 storyboard:

| State | Figma node | Distinguishing instrument or task plane |
| --- | --- | --- |
| Inspect · Healthy | `50:5622` | Stable topology with resource, network, timeline, and collapsed evidence |
| Inspect · Selected degraded motor drive | `50:5623` | Orange degraded dependency path plus yellow focus ownership |
| Diagnose · Evidence expanded | `50:5624` | Shared time-axis evidence plane while platform geography remains visible |
| Inspect · Degraded motor drive | `50:6219` | Degraded path without selection treatment |
| Inspect · Network / VRRP | `50:6221` | VIP ownership and WiFi-to-4G/5G failover path |
| Inspect · Software runtimes | `50:6223` | Per-node runtime ownership and selected partner stack |
| Diagnose · Clock uncertainty | `50:6225` | Chrony envelope, Jetson 2 offset, and Diagnose task ownership |
| Change · Motor-drive power cycle | `50:6227` | Before/proposed/impact/prerequisite review with explicit acknowledgement |
| Inspect · Stale Jetson 2 | `50:6229` | Dashed topology, hatched missing data, freshness duration, and evidence gaps |

Validated exports are stored in
`../renders/latest-v3-2026-08-21/`. The section-level exports are `49-4706.png`,
`50-5179.png`, and `50-5617.png`; the remaining files are individual storyboard
states named from their node IDs.

## Visual audit status

The 2026-08-21 reference comparison found that the promoted v2 nodes preserve
the intended task flow and factual platform layout but do not yet meet the
visual-reference fidelity gates. They are now the current **UX/content
baseline**, not the approved visual benchmark. The resulting archive-safe v3
revision is documented in `VISUAL_STYLE_V3_PLAN.md` and mapped above.

## Visual Style v2 promotion

The stricter **Signal Instrumentation** visual direction is now applied as an
archive-safe v2 layer across all three Figma pages. Previous implementations
remain intact and are explicitly prefixed `Archive · Pre-v2`.

| Page | Promoted v2 node | Archived source |
| --- | --- | --- |
| 00 Cover & Foundations | `48:3030` — Style Direction · Signal Instrumentation · Visual Style v2 | `36:56` |
| 01 Components | `48:2129` — Visual Style v2 · Components | `46:464` |
| 02 Engineering Interface | `48:2165` — Visual Style v2 · Engineering Interface | `46:458` |

The v2 expression removes gradients from persistent data surfaces, adds the
documented chassis/instrument radius hierarchy, uses a one-pixel outer border
plus inset contour as the default edge stack, and reserves stronger elevation
for the adaptive attention rail and selected instruments. Compact comparison
tiles now include meaningful resource traces; the foundations specimen also
demonstrates resource bars, a network distribution, and a subsystem-state
matrix.

New shared effect style:

- `Elevation/00 · Inset contour` (`S:4e843fbc50c7447fda634106059212238ac60dbb,`)

Promoted v2 component masters:

| Pattern | V2 node |
| --- | --- |
| System Node · v2 | `48:2132` |
| Task Rail Item · v2 | `48:2138` |
| Lens Chip · v2 | `48:2145` |
| Attention Rail · v2 | `48:2150` |
| Evidence Strip · Collapsed · v2 | `48:2160` |

The nine promoted screen frames are `48:2171`, `48:2258`, `48:2346`,
`48:2442`, `48:2574`, `48:2661`, `48:2751`, `48:2844`, and `48:2942`.

## Redesign status

The task-led, visual-first redesign in `INTERFACE_REDESIGN_PLAN.md` was first
implemented as the pre-v2 reference draft and is now retained as an archived
baseline. New visual iteration should target the v2 nodes listed above.

The archived draft is grouped in `46:458`; the promoted visual version is
grouped in `48:2165` on **02 Engineering Interface**. Both use nine 1,440 × 900
reference frames in a 3 × 3 storyboard. The generic visual-identity page now
contains the original specimen and its promoted v2 sibling.

Functional content for future states is governed by
`UI_FUNCTIONAL_REQUIREMENTS.md`. New screens must map visible signals,
diagnostics, evidence and actions to its stable requirement IDs.

## File structure

- **00 Cover & Foundations** remains the generic visual-identity space. Product
  screens must not consume this page.
- **01 Components** contains foundations plus reusable engineering-interface
  patterns. `46:464` is archived; `48:2129` is the current v2 component stage.
- **02 Engineering Interface** contains archived baselines and the current v2
  task-flow storyboard. A separate page was not added because the Figma Starter
  file already uses all three available pages.

## Implemented task-flow grammar

| Pattern | Figma node | Contract |
| --- | --- | --- |
| System Node | `46:467` | Object name, state marker, kind glyph and one glance signal |
| Task Rail Item | `46:479` | Selected/default states for Inspect, Diagnose and Change |
| Lens Chip | `46:484` | Active/default overlay lens without moving map objects |
| Attention Rail | `46:485` | Current concern, impact and one next action |
| Evidence Strip · Collapsed | `46:495` | Compact entry into correlated evidence |

These components reuse the existing Figma variables, text styles, gradients and
elevations. Yellow means focus, selection or deliberate action; orange means a
degraded or caution state. When an object is both selected and degraded, its
state remains orange and yellow corner brackets add focus.

## Implemented storyboard

| State | Figma node | Purpose |
| --- | --- | --- |
| Inspect · Healthy | `47:500` | Whole-platform orientation with no scrolling |
| Inspect · Degraded motor drive | `47:671` | Detection and dependency-path emphasis |
| Inspect · Selected subsystem | `47:843` | Exact telemetry only after selection |
| Diagnose · Evidence expanded | `47:1023` | Causal chain, metrics and event evidence |
| Inspect · Network lens | `47:1243` | Uplink, VRRP, Tailscale and LAN emphasis |
| Inspect · Software lens | `47:1416` | Docker runtime distribution by compute node |
| Diagnose · Clock uncertainty | `47:1592` | Chrony relationship and timing confidence |
| Change · Review & acknowledge | `47:1771` | GPIO change scope, impact, preconditions and rollback |
| Inspect · Stale / disconnected | `47:1957` | Freshness, uncertainty and dependent impact |

## Realised layout contract

- Reference viewport: 1,440 × 900; no scrolling for the default glance state.
- Global header: 56 px, with robot context, freshness and the provisional
  Safety stop affordance.
- Task rail: 80 px, dark and persistent; it expresses the user flow rather than
  system categories.
- Scope/lens bar: 52 px; Physical, Network, Software, Time and Integration are
  overlays on a stable map.
- Main workbench: 980 px platform map plus a 316 px adaptive attention rail.
- Lower glance band: cross-node comparison plus recent changes.
- Evidence: 44 px collapsed strip; an expanded drawer replaces only the lower
  glance band and leaves platform geography visible.
- Stable map: external services and uplinks at the top, shared VRRP/uplink and
  LAN spines, three compute nodes, Intel-to-CAN branch, five CAN subsystems, and
  provisional camera attachments.
- Unselected objects show only name, state and one signal. Precise values,
  hypotheses, logs and chronology appear after selection or evidence expansion.

## Reusable engineering patterns

| Pattern | Figma node | Intended use |
| --- | --- | --- |
| Causal Issue Row | `42:55` | A cause or symptom with impact, confidence and freshness |
| Topology Node | `42:63` | Compute, subsystem or network object in a dependency stage |
| Trace Instrument | `42:68` | Current value plus a compact time-series impression |
| Object Inspector | `42:85` | Persistent right-side inspection of the selected object |
| Diagnostics Drawer | `42:95` | Evidence layer for correlated events and export actions |

All five patterns use local Figma variables and expose text properties for
screen-specific content. Existing Button, Status badge, Navigation item and
Platform Tile components remain part of the shared library.

## Current reference flows

| Flow | Figma node | Primary question |
| --- | --- | --- |
| Platform Overview · Degraded | `42:107` | What is unhealthy, why, and what is affected? |
| Compute Node Detail | `42:224` | What is the resource and runtime posture of this computer? |
| Connectivity Overview | `43:341` | Which link is degraded and what depends on it? |

The screens share a 1,440 px shell with a 64 px global header, 224 px context
navigation, a 12-column workbench, a 408 px inspection column and a bottom
evidence drawer. The shell excludes fleet, mission, autonomy, SLAM and
navigation concepts.

## Safety-control wording

The header reserves a persistent yellow **Safety stop** control. It represents
an important platform function, but must not be presented as a certified
emergency-stop control. Reset, restart and recovery actions remain separate.
See `SAFETY_CONTROLS.md`.

## Visual hierarchy

- ExR yellow marks current selection, current data and the safety-stop affordance.
- White and subtle neutral surfaces carry information; yellow does not fill
  ordinary metric cards.
- Causal issues are ordered as root candidate followed by dependent symptoms.
- Glance content is always visible; attention and evidence are progressive
  disclosure layers rather than permanent inspection panels or navigation
  detours.
- Legacy mission and teleoperation frames are retained but hidden and prefixed
  `Legacy ·` so the change is reversible.

## Known tool limitations

FigWright created and bound the missing radius tokens, but did not expose
variable-picker scope editing. The new radius variables should be scope-reviewed
manually if strict picker filtering becomes necessary.

FigWright does not currently expose variable scope assignment for a newly
created semantic collection. A separate `Color · Dark` collection was therefore
not created: doing so would pollute variable pickers with incorrect default
scopes. Graphite components bind to the existing scoped primitives; the paired
light specimen binds to existing `Color · Light` semantics. Introduce a dark
semantic collection only when scopes can be assigned and audited safely.
