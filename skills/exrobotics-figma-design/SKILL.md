---
name: exrobotics-figma-design
description: Design, review, document, and maintain the ExRobotics Figma system for its internal engineering platform interface. Use for ExRobotics visual-direction work, reference-image synthesis, Figma foundations, variables, styles, components, desktop/mobile screens, platform-console UX, compute/subsystem/network/log interfaces, or changes that must preserve the project's reproducible design guidance.
---

# ExRobotics Figma design

## Start

1. Locate the `ExRobotics_Figma` project root.
2. Read `AGENTS.md`.
3. Read `docs/UX_ARCHITECTURE.md` for product, navigation, user-flow, screen,
   or layout work.
4. Read `docs/SAFETY_CONTROLS.md` for any safety-state, stop, reset, recovery,
   or restart work. Treat it as provisional until safety-engineering review.
5. Read `docs/DESIGN_GUIDELINES.md` and
   `tokens/exrobotics-ui.tokens.json` completely.
6. Read `docs/REFERENCE_ANALYSIS.md` only when evaluating or changing visual
   direction.
7. Read `docs/FIGMA_WORKFLOW.md` before any live Figma mutation.
8. Read `references/project-map.md` for the current operational inventory, then
   verify every ID through FigWright.

## Product constraint

Keep the interface focused on platform introspection: compute, memory,
accelerators, storage, services, containers, subsystems, network, telemetry,
logs, events, configuration, health, and diagnostics.

Do not introduce fleet management, missions, routes, checkpoints, autonomy
controls, dispatch, or operator tasking unless the user explicitly changes the
scope.

## Visual constraint

Apply **Signal Instrumentation**:

- a visibly bounded, layered systems chassis rather than a generic webpage;
- a 12-column mixed-span bento workbench with aligned edges and purposeful
  module proportions;
- primary tiles that behave as micro-instruments with meaningful traces,
  topology, matrices, paths, or direct-manipulation stages;
- warm-neutral light canvas and derived near-black dark expression;
- ExRobotics yellow for action, selection, current datum, and attention;
- Space Grotesk for hierarchy, Inter for interface copy, Roboto Mono for data;
- large outer radii contrasted with exact inner diagrams;
- a low-relief edge stack of hairline border, subtle inner contour, and
  restrained elevation;
- glass limited to navigation, overlays, and selected floating controls;
- meaningful charts and topology views instead of decorative widgets.

Do not treat gradients, equal metric cards, or a conventional sidebar as
evidence that the style has been applied. Run the eight-part reference-fidelity
gate in `docs/DESIGN_GUIDELINES.md` before visual QA.

Use the canonical project docs for detailed values. Do not restate or invent a
parallel token system inside prompts or Figma nodes.

## Figma workflow

1. Use FigWright for all Figma reads and writes.
2. Ping and confirm the routed file is
   `EX Robotics — Visual Identity & UI Foundations`.
3. Inspect variables, styles, local components, and the exact target subtree.
4. Reuse existing tokens, styles, and instances.
5. Add missing foundations before components; add components before screens.
6. Make small sequential mutations and validate after each major section.
7. Capture component and screen screenshots.
8. Audit text for excluded product concepts and update project documentation
   when a reusable rule changes.

Load the bundled Figma `figma-use`, `figma-generate-design`, or
`figma-generate-library` skills when their trigger conditions apply, while
continuing to use FigWright as this project's Figma MCP.

## Documentation workflow

- Put product model, IA, flows, layout intent, screen set, and UX plan in
  `docs/UX_ARCHITECTURE.md`.
- Put provisional safety-state and stop/recovery interaction requirements in
  `docs/SAFETY_CONTROLS.md`; do not silently convert provisional decisions into
  approved behavior.
- Put visual rationale in `docs/REFERENCE_ANALYSIS.md`.
- Put accepted rules in `docs/DESIGN_GUIDELINES.md`.
- Put exact reusable values in `tokens/exrobotics-ui.tokens.json`.
- Put material decisions and rationale in `docs/DECISION_LOG.md`.
- Put agent operating changes in `AGENTS.md` and this skill.

Keep each source focused and avoid duplicated guidance.

## Quality gate

Before completion, confirm:

- component attachment and token/style reuse;
- readable contrast and non-color status cues;
- 44 px minimum interactive targets;
- no clipping, overflow, or placeholder copy;
- correct font roles for human and machine data;
- light/dark semantic consistency;
- screenshots for every materially changed view;
- documentation updated for new reusable decisions.
