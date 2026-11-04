---
name: exrobotics-figma-design
description: Design, review, document, and maintain the ExRobotics Figma system for its internal robot-platform engineering interface. Use for ExRobotics visual direction, Figma foundations/components/screens, or compute, subsystem, network, telemetry, log, and diagnostic UX that must preserve the project's product and design constraints.
---

# ExRobotics Figma design

This skill supplies project truth. `exceptional-ui` orchestrates substantial
design; FigWright builds; the specialist critic and reference analyst remain
independent.

## Cheap grounding

1. Locate the project root and read `AGENTS.md` once.
2. Load only task-relevant sources:
   - product/flow/layout: `docs/UX_ARCHITECTURE.md`;
   - platform facts: `docs/PLATFORM_SYSTEM_MODEL.md` and relevant
     `data/platform-system.yaml` entries;
   - functional scope: `docs/UI_FUNCTIONAL_REQUIREMENTS.md`;
   - safety action/state: `docs/SAFETY_CONTROLS.md`;
   - visual direction: `docs/DESIGN_GUIDELINES.md`; its section 18a carries the
     working principles, 19a selection, 20a charts, 6.2a surface glow;
   - exact reusable value: matching entry in
     `tokens/exrobotics-ui.tokens.json`;
   - Figma mutation: `docs/FIGMA_WORKFLOW.md` and
     `references/project-map.md`.
3. Put paths plus only decisive constraints into the compact design-run packet.
   Do not paste or repeatedly reread whole documents. Reopen the exact section
   only when a decision depends on it.

## Product boundary

The interface introspects the robot platform: compute, accelerators, memory,
storage, containers/services, CAN and other subsystems, network/uplink/VPN/time,
telemetry, events, configuration, health, logs, and diagnostics.

Exclude fleet operations, missions, routes, checkpoints, autonomy, SLAM,
navigation, dispatch, and operator tasking unless the user changes scope.

Safety stop, stall reset, power control, and recovery work must follow
`docs/SAFETY_CONTROLS.md` and remain explicitly provisional where documented.

## Visual invariant

Apply **Signal Instrumentation** as product logic, not decoration:

- bounded layered systems chassis;
- mixed-span diagnostic workbench rather than equal card grid;
- topology, traces, paths, matrices, timelines, and direct evidence shaped by
  real platform relationships;
- ExRobotics yellow reserved for action, selection, current datum, and attention;
- strong hierarchy, exact inner instruments, restrained atmospheric depth;
- glass only for navigation, overlays, or selected floating controls;
- realistic machine data and non-color status cues.

Canonical type, color, spacing, geometry, and motion values remain in project
guidelines/tokens. Never restate a parallel token system in prompts or nodes.

The dark expression has diverged from the brand neutral ramp: its surfaces are
`primitives.graphite`, healthy is neutral, and only yellow, amber and red carry
hue. See D032 and D034 before touching dark colour.

## Workflow routing

- Substantial new screen, redesign, art direction, or build-and-critique loop:
  load `../exceptional-ui/SKILL.md`; it invokes the other layers.
- Reference-analysis-only deliverable: load
  `../design-reference-analysis/SKILL.md` directly.
- Critique-only or readiness request: load `../visual-critique/SKILL.md`
  directly.
- Mechanical Figma change: follow `docs/FIGMA_WORKFLOW.md` and FigWright
  `figma-build`; do not load the art-direction stack unless visual judgment is
  material.

## Figma efficiency

Confirm the routed file once, then inspect variables/styles/components and the
exact target subtree in batched reads. Reuse existing foundations and attached
instances. Build small coherent sections, returning node IDs rather than full
trees. Capture legible full frames and targeted dense-region crops; do not save
tokens by lowering visual fidelity. Re-query only changed or failing regions.

## Documentation

Update only the authoritative source affected by a reusable change:

- UX/product model → `docs/UX_ARCHITECTURE.md`;
- safety behavior → `docs/SAFETY_CONTROLS.md`;
- visual rule → `docs/DESIGN_GUIDELINES.md`;
- exact value → `tokens/exrobotics-ui.tokens.json`;
- durable rationale → `docs/DECISION_LOG.md`;
- agent workflow → this skill or `AGENTS.md`.

Do not duplicate unchanged rationale across them.

## Project completion checks

Confirm scope, realistic content/states, component/token reuse, readable
contrast and non-color cues, 44 px targets where applicable, no clipping or
placeholder copy, correct human/machine type roles, legible screenshots for
every changed view, and documentation only where reusable decisions changed.
