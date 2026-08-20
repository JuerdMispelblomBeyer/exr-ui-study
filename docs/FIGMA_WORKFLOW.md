# Figma workflow

## Target

- File: `EX Robotics — Visual Identity & UI Foundations`
- Page `0:1`: `00 Cover & Foundations`
- Page `9:18`: `01 Components`
- Page `9:19`: `02 Reference Screens`

Use the IDs as orientation only. Verify them with FigWright before every task.

## Required sequence

1. Ping FigWright and confirm the routed file.
2. Inspect pages, variables, shared styles, local components, and the exact
   target subtree.
3. Read `docs/UX_ARCHITECTURE.md` for any screen or layout work, and
   `docs/SAFETY_CONTROLS.md` for any safety-state or stop-control work.
4. Read `docs/DESIGN_GUIDELINES.md` and the relevant token entries.
5. Decide whether the change belongs to foundations, components, or screens.
6. Update foundations first when a reusable token or style is missing.
7. Build or update a reusable component before repeating a pattern in screens.
8. Compose screens from instances and shared styles.
9. Validate component API, node structure, and screenshots.
10. Audit visible copy and update documentation/decision log.

## Visual preflight

Before modifying a screen, write down its intended:

1. user job, active platform scope, and disclosure layer;
2. chassis region and navigation path;
3. 12-column module spans and row depths;
4. dominant diagnostic instrument;
5. sparse, standard, and dense zones;
6. selected scope, path, datum, or object;
7. inspector and diagnostics-drawer behavior;
8. yellow allocation;
9. edge stack and elevation ownership.

If the proposed screen is still describable as “sidebar + equal metric cards +
table,” the visual direction has not yet been applied.

## Current reusable assets

- Button component set.
- Status Badge component set.
- Navigation Item component set.
- Metric Tile component.
- Alert Banner component.
- Platform Tile component set: Compute, Network, Subsystem, Event.
- Gradient paint styles: Atmosphere, Signal, Compute, Healthy.
- Elevation styles: Raised, Floating, Overlay.

## Current style specimen

- `36:56` — `Style Direction · Signal Instrumentation` on the foundations page.
- This specimen predates the stricter chassis/bento/micro-instrument revision
  and must not be used as the visual benchmark without further restyling.
- Its navigation and summary tiles remain attached instances with content set
  through component properties.
- Its topology and selected-probe panels are examples of the relationship and
  diagnostic-focus grammar, not production components yet.

Consult `skills/exrobotics-figma-design/references/project-map.md` for the latest
known IDs, then verify them live.

## Naming

- Pages: numbered sentence case.
- Shared styles: `Category/Subcategory/Name`.
- Components: title case; variants use `Property=Value`.
- Frames: semantic purpose, not visual appearance.
- Text layers: content or semantic role; avoid `Text 123`.
- Examples: `Platform Tile`, `Type=Compute`, `Platform console · Desktop · Light`.

## Construction rules

- Use auto layout for structural relationships.
- Bind fills, strokes, spacing, radii, and sizes to variables where available.
- Apply shared text, paint, and effect styles rather than duplicating values.
- Use component text properties for reusable content. If a legacy instance
  property does not visibly update, inspect and repair the binding rather than
  detaching the instance.
- Keep components attached in reference screens.
- Do not use destructive cleanup based on fuzzy names.

## Validation

For every component family:

- confirm variant axes and property definitions;
- confirm variant count and names;
- confirm gradient/effect/style attachment;
- capture the component stage.

For every screen:

- capture desktop and mobile at a legible scale;
- inspect clipping, alignment, density, and hierarchy;
- scan all visible text for excluded product concepts;
- confirm machine values use Roboto Mono;
- confirm yellow remains scarce and meaningful;
- inspect 44 px targets and focus visibility.
- run the eight-part reference-fidelity acceptance gate from
  `docs/DESIGN_GUIDELINES.md` before the yellow-allocation check.

## Dark expression

Dark UI must be derived from the same semantics. On Figma Starter, if an
additional variable mode is unavailable, use a paired `Color · Dark`
collection with matching semantic names. Do not hardcode dark values directly
into components.

## Documentation requirement

When introducing a reusable visual rule, update:

1. `docs/DESIGN_GUIDELINES.md`;
2. `tokens/exrobotics-ui.tokens.json` if values change;
3. `docs/DECISION_LOG.md` with rationale;
4. the local project skill if the agent workflow changes.
