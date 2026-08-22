# Spacing and geometry

Spacing and geometry create rhythm, alignment, material character, and
structural credibility. Inspect existing dimension variables, layout grids,
component padding, radii, and effect styles before adding values.

## 1. Define spatial tiers

Assign existing scale steps to roles:

| Tier | Purpose |
|---|---|
| Micro | icon-to-label, inline metadata, chart marks |
| Control | internal control padding and compact row gaps |
| Component | card/module internals and list rhythm |
| Region | separation between related modules or panes |
| Section | change of task or content mode |
| Canvas | viewport/chassis inset and major composition breathing room |

The exact values come from the design system. If none exists, choose a compact
base scale and reuse it; do not create a new gap for every relationship.

## 2. Establish the grid

Define:

- viewport and responsive breakpoints;
- outer inset;
- column count;
- gutters;
- baseline or spacing grid when relevant;
- preferred component spans;
- alignment anchors shared across regions.

Use real Figma layout grids for explicit column systems. Use auto-layout for
structural child relationships. Absolute positioning is appropriate for
top-level placement or purposeful overlays, not for ordinary internal layout.

## 3. Build a radius ladder

Radius should express scale and function:

- smallest: marks, tags, compact fields, diagram nodes;
- control: buttons, inputs, compact panels;
- module: workbench surfaces and cards;
- shell: application chassis, modal, or major stage;
- full: pills only when the content is genuinely pill-like.

Avoid one universal radius. Contrast a softer enclosure with more exact inner
geometry when the product calls for precision.

## 4. Define an edge grammar

Choose how ownership is shown:

- outer stroke for boundary;
- inner contour/highlight for low-relief material;
- divider for content rhythm;
- focus ring/bracket for active selection;
- shadow for genuine elevation;
- scrim for modal ownership.

Do not stack border, inner border, shadow, glow, and gradient on every surface.
Assign each effect a job. Adjacent modules may share edges or baselines when
they belong to one continuous field.

## 5. Budget elevation

Classify layers:

1. canvas/background;
2. persistent chassis;
3. work surface;
4. inset evidence/data;
5. selected or directly manipulated object;
6. popover/dialog/temporary overlay.

Only layers 5–6 normally need pronounced elevation. A wall of equally floating
cards has no depth hierarchy.

## 6. Use optical, not merely mathematical, alignment

After structural alignment:

- compensate for icon visual weight;
- align text baselines rather than bounding boxes where appropriate;
- check circular controls and asymmetric symbols;
- balance unequal text lengths in repeated modules;
- verify that borders do not create doubled dark lines;
- inspect half-pixel artifacts and inconsistent stroke alignment.

## 7. Geometry as identity

Select one or two repeatable formal devices tied to behavior:

- clipped/cropped continuation for a pan or timeline;
- bracketed selection;
- attached inspector;
- stepped or nested surface edge;
- mixed-span continuous field;
- a distinct diagram-node family.

Avoid decorative notches, arbitrary diagonals, or exotic masks with no product
meaning.

## 8. Geometry QA

On the screenshot, inspect:

1. Are the strongest edges intentionally aligned?
2. Do spacing tiers reveal relationship strength?
3. Are radii consistent by role rather than identical everywhere?
4. Does elevation explain ownership?
5. Are containers nested only when necessary?
6. Are repeated rows/modules optically consistent with realistic content?
7. Does the layout still work at the target narrow/wide viewport?
8. Are any component dimensions hardcoded where HUG/FILL or bounds should be
   used?
