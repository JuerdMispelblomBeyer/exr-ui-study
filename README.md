# ExRobotics Figma

Working source for the ExRobotics internal engineering-interface design system.

The product scope is the platform layer: compute nodes, subsystems, network,
storage, services, logs, events, and diagnostics. Fleet management, missions,
routes, and autonomy controls are outside this project.

## Start here

- `AGENTS.md` — project operating rules for agents.
- `docs/UX_ARCHITECTURE.md` — initial product model, information architecture,
  user flows, layout blueprint, screen set, and phased design plan.
- `docs/UI_FUNCTIONAL_REQUIREMENTS.md` — evolving functional baseline with
  stable requirement IDs, component mappings, observability, evidence,
  actions, acceptance scenarios, and open questions.
- `docs/PLATFORM_SYSTEM_MODEL.md` — actual on-board computers, networks,
  field bus, subsystems, cameras, runtimes, and integration boundaries.
- `docs/SYSTEM_VISUALIZATION_SPEC.md` — visual-first schematic grammar and
  layout recipes for representing the platform.
- `docs/INTERFACE_REDESIGN_PLAN.md` — proposed task-led redesign, screen
  storyboard, information budget, component strategy, and implementation phases.
- `docs/SAFETY_CONTROLS.md` — provisional stop, recovery, state, and failure UX;
  requires safety-engineering review.
- `docs/REFERENCE_ANALYSIS.md` — visual analysis of every supplied reference.
- `docs/DESIGN_GUIDELINES.md` — canonical visual and interaction direction.
- `docs/FIGMA_WORKFLOW.md` — how to translate the system into Figma safely.
- `docs/FIGMA_IMPLEMENTATION.md` — current Figma page, component, and screen map.
- `docs/DECISION_LOG.md` — durable design decisions and their rationale.
- `tokens/exrobotics-ui.tokens.json` — machine-readable palette and UI values.
- `data/platform-system.yaml` — extensible machine-readable platform inventory
  and relationship model.
- `skills/exrobotics-figma-design/` — reusable Codex skill for this project.
- `reference/` — supplied visual references; preserve the originals.

## Figma output

The connected file now includes `Style Direction · Signal Instrumentation`
(`36:56`) on `00 Cover & Foundations`. It demonstrates the reference synthesis
with attached navigation and platform-tile instances, a limited dark tool rail,
floating diagnostic tiles, a dependency-path panel, and a selected-probe tile.
It predates the stricter identity revision documented in August 2026 and is an
implementation baseline, not the target visual benchmark. Treat the node ID as
orientation only and verify it live before editing.

## Current direction

The primary direction is **Signal Instrumentation**: a layered systems chassis
containing a continuous bento workbench of low-relief, directly inspectable
engineering instruments. The signature comes from silhouette, nested material
strata, purposeful mixed spans, exact microvisualizations, and interaction
marks—not from gradients or the source references' colors. The dark expression
is **Night Console**. ExRobotics yellow remains the lead optical signal for
selection, current state, active paths, focus, and primary action.

## Current layout plan

The implemented task flow treats one connected robot platform as a graph of
compute, subsystem, connectivity, software, and evidence objects. Inspect,
Diagnose and Change operate on one stable platform map; Physical, Network,
Software, Time and Integration are lenses. The first nine reference states are
applied in Figma; see `docs/FIGMA_IMPLEMENTATION.md`. Functional content and
future capability expansion are governed by `docs/UI_FUNCTIONAL_REQUIREMENTS.md`.
