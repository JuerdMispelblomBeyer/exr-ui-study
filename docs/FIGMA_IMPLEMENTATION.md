# Figma implementation map

Last updated: 2026-08-20

## Redesign status

The task-led, visual-first redesign in `INTERFACE_REDESIGN_PLAN.md` is now
implemented as a first reference draft. The earlier category-led frames remain
in Figma as a retained baseline; do not extend their repeated card composition.

The redesign is grouped in the Figma section
`Redesign · Inspect → Diagnose → Change` (`46:458`) on **02 Engineering
Interface**. It uses nine 1,440 × 900 reference frames in a 3 × 3 storyboard.
The generic visual-identity space on **00 Cover & Foundations** was not changed.

Functional content for future states is governed by
`UI_FUNCTIONAL_REQUIREMENTS.md`. New screens must map visible signals,
diagnostics, evidence and actions to its stable requirement IDs.

## File structure

- **00 Cover & Foundations** remains the generic visual-identity space. Product
  screens must not consume this page.
- **01 Components** contains foundations plus reusable engineering-interface
  patterns. The new component stage is `Redesign Grammar · Task Flow`
  (`46:464`).
- **02 Engineering Interface** contains both the retained baseline and the new
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

## Known tool limitation

FigWright created and bound the missing radius tokens, but did not expose
variable-picker scope editing. The new radius variables should be scope-reviewed
manually if strict picker filtering becomes necessary.
