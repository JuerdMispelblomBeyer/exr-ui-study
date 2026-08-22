# ExRobotics Figma agent entry

Read this file first. Load only the document relevant to the task.

## Product boundary

- Design an internal engineering interface for platform introspection.
- In scope: compute nodes, processors, memory, accelerators, storage, services,
  containers, subsystems, buses, network links, telemetry, logs, events,
  configuration, health, diagnostics, and dependency/topology views.
- Out of scope: fleet management, mission planning or execution, routes,
  checkpoints, autonomy control, dispatch, and operator tasking.

## Source order

1. The user's current request.
2. `data/platform-system.yaml` and `docs/PLATFORM_SYSTEM_MODEL.md` for actual
   platform inventory, topology, relationships, and explicit unknowns.
3. `docs/UI_FUNCTIONAL_REQUIREMENTS.md` for capabilities, required
   observations, actions, evidence, acceptance scenarios, and stable
   requirement IDs.
4. `docs/UX_ARCHITECTURE.md` for product structure, information architecture,
   user flows, layout regions, and screen intent.
5. `docs/SYSTEM_VISUALIZATION_SPEC.md` for spatial encoding and visual-first
   layout composition.
6. `docs/SAFETY_CONTROLS.md` for any safety-state or stop-control work; its
   provisional requirements require safety-engineering review.
7. `docs/DESIGN_GUIDELINES.md` for visual and interaction decisions.
8. `tokens/exrobotics-ui.tokens.json` for exact reusable values.
9. The live Figma file for current node/component state.
10. `docs/REFERENCE_ANALYSIS.md` for visual rationale, not literal copying.

Record material new decisions in `docs/DECISION_LOG.md` and update the design
guide or token file in the same change. Do not let Figma become the only source
of truth.

## Figma

- Use the FigWright MCP for all Figma reads and writes.
- Target file: `EX Robotics — Visual Identity & UI Foundations`.
- Ping FigWright before work and confirm that the routed file is the target.
- Inspect pages, variables, styles, local components, and target nodes before
  mutating.
- Reuse existing variables, styles, and component instances before creating
  new primitives.
- Work in order: foundations -> components -> composed screens.
- Make small, sequential changes. Validate structure and screenshots after each
  major section.
- Never infer node IDs. Read them from FigWright and verify stale IDs.
- Preserve the established Space Grotesk, Inter, and Roboto Mono hierarchy.
- Maintain both light and dark expressions as one system. Do not invent an
  unrelated dark theme.

## Visual rules

- Treat existing Figma screens as implementation drafts, not visual authority.
- Build a coherent application chassis with nested navigation and workbench
  strata; do not default to a flat SaaS sidebar-and-cards composition.
- Use a 12-column mixed-span bento field whose module size reflects diagnostic
  purpose and whose edges align across rows.
- A primary analytic tile must contain a meaningful micro-instrument such as a
  trace, topology, matrix, dependency path, state map, or direct-manipulation
  stage. Title/value/metadata alone is not sufficient.
- Define surfaces primarily with a fine outer stroke and subtle inner contour;
  reserve stronger elevation for selected or temporary objects.
- Use ExRobotics yellow for primary action, selection, current datum, and
  attention. Do not wash whole dashboards in yellow.
- Keep core data surfaces crisp. Glass and blur are limited to navigation,
  overlays, and selected floating controls.
- Use large radii for the outer chassis and signature instruments, then step
  down to exact geometry inside charts, tables, brackets, and diagrams.
- Use gradients as quiet spatial atmosphere only; they are not the visual
  identity.
- Use monospaced numerals and metadata for machine values, timestamps, IDs, and
  units.
- Status must never rely on color alone; pair it with text, icon, or pattern.
- Avoid generic SaaS language and decorative charts without diagnostic meaning.
- Require every screen to pass the color-independent reference-fidelity gate in
  `docs/DESIGN_GUIDELINES.md` before using brand color as the finishing layer.

## Documentation routing

| Task | Read next |
|---|---|
| Actual platform inventory, topology, or relationships | `docs/PLATFORM_SYSTEM_MODEL.md`, then `data/platform-system.yaml` |
| Functional requirements, capability inventory, observability, or actions | `docs/UI_FUNCTIONAL_REQUIREMENTS.md` |
| Schematic, topology visualization, or visual-first layout | `docs/SYSTEM_VISUALIZATION_SPEC.md` |
| Thorough interface redesign or replacement of current screens | `docs/INTERFACE_REDESIGN_PLAN.md` |
| Product model, user flow, IA, or layout | `docs/UX_ARCHITECTURE.md` |
| Safety state or stop/recovery control | `docs/SAFETY_CONTROLS.md` |
| Visual direction or review | `docs/DESIGN_GUIDELINES.md` |
| Visual Style v3 planning or implementation | `docs/VISUAL_STYLE_V3_PLAN.md`, then `docs/DESIGN_GUIDELINES.md` |
| Reference-image interpretation | `docs/REFERENCE_ANALYSIS.md` |
| New inspiration URL, shot, case study, or image intake | `docs/REFERENCE_INTAKE_METHOD.md`, then `docs/REFERENCE_ANALYSIS.md` |
| Structured visual-reference analysis or multi-reference design synthesis | `skills/design-reference-analysis/SKILL.md` |
| Figma mutation or component work | `docs/FIGMA_WORKFLOW.md` |
| Exact colors, spacing, radii, motion | `tokens/exrobotics-ui.tokens.json` |
| Why a decision exists | `docs/DECISION_LOG.md` |
| Reusable agent workflow | `skills/exrobotics-figma-design/SKILL.md` |
| Exceptional UI art direction, composition, or visual QA | `skills/exceptional-ui/SKILL.md`, then `skills/exrobotics-figma-design/SKILL.md` |
| Rendered UI critique, visual-quality scoring, or PASS/ITERATE review | `skills/visual-critique/SKILL.md` |

## Filesystem rules

- Preserve all original files under `reference/`.
- Record inaccessible web references as queued sources; never treat a nearby
  search result as the requested visual evidence.
- Store authored guidance under `docs/`, machine values under `tokens/`, and
  agent workflows under `skills/`.
- Use deterministic, descriptive names. Do not add unexplained exports or
  duplicate handover folders.

## Completion checks

Before handing off a visual change:

1. Confirm the screen follows the approved object model, flow, layout region,
   and disclosure level in `docs/UX_ARCHITECTURE.md`.
2. Audit visible copy for excluded fleet/mission/autonomy concepts.
3. Confirm token/style reuse and component attachment.
4. Check contrast, 44 px minimum interactive targets, clipping, overflow, and
   responsive behavior.
5. Capture screenshots of each changed screen or component family.
6. Update documentation when the work introduces a new reusable rule.
7. Do not finalize a safety control until the review gates in
   `docs/SAFETY_CONTROLS.md` are resolved.
