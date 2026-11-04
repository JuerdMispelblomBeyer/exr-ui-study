# Figma workflow

## Target

- File: `EX Robotics — Visual Identity & UI Foundations`
- Page `93:2`: `01 Visual Style — Graphite (Dark)`
- Recovery page `0:1`: `99 Backup · Pre industrial evidence atlas · 2026-08-24`
  with editable pre-pass root `65:1287` and the earlier recovery root `84:3`.
- Recovery page `88:2`: `99 Backup · Pre visual calm redesign · 2026-08-24`
  with editable pre-redesign root `88:3`.

The file was reset to a clean slate before 2026-08-22. Earlier pages, component
sets, styles, and screens no longer exist. Use the IDs as orientation only and
verify them with FigWright before every task. The recovery page is not a second
design direction and must never be used as the active target.

## Required sequence

1. Ping FigWright and confirm the routed file once per run.
2. Batch-inspect pages, variables, styles, local components, and the exact target
   subtree; record decisive IDs in the compact run packet.
3. Read only task-relevant project sections: UX for layout, safety for
   stop/recovery, design guidelines for visual changes, and matching token
   entries for exact values.
4. Decide whether the delta belongs to foundations, components, or screens.
5. Add a foundation only for a recurring missing role; update a reusable
   component before repeating a pattern; compose screens from instances.
6. Validate changed APIs/nodes, then inspect legible full-frame screenshots and
   dense-region crops.
7. Re-query only changed or failing subtrees. Audit visible copy and update
   documentation only when a reusable rule changed.

## Token-efficient evidence policy

- Save tokens in metadata and narration, never by shrinking or skipping visual
  evidence.
- After initial grounding, use node IDs and narrow reads instead of repeating
  page-wide metadata, styles, fonts, and component inventories.
- Batch compatible read-only queries. Keep writes as small coherent sections so
  failures are local and verification is cheap.
- Return changed node IDs, bindings/reuse evidence, and unresolved risks—not a
  full layer-tree transcript.
- Inspect 1–4 full frames per screenshot call at legible scale. Use targeted
  crops when text, spacing, charts, or surfaces cannot be judged reliably.
- Reuse an unchanged screenshot in the same run; recapture after every material
  visual change.
- For iterations, compare the same viewport and state. Inspect the whole frame,
  but report only score/issue deltas until the final full critique.

## Visual preflight

Before modifying a screen, write down its intended:

1. user job, active platform scope, and disclosure layer;
2. chassis region and navigation path;
3. 12-column module spans and row depths;
4. dominant diagnostic instrument;
5. sparse, standard, and dense zones;
6. selected scope, path, datum, or object;
7. inspector and diagnostics-drawer behavior;
8. yellow allocation, and which single element carries the solid accent;
9. matte/raised material choice and elevation ownership;
10. the one brightest point, and what was dimmed to let it win.

If the proposed screen is still describable as “sidebar + equal metric cards +
table,” the visual direction has not yet been applied.

## Current reusable assets

None. The file holds no components, styles, or variables. Anything reusable has
to be built from scratch, and only after the dark visual style is accepted.

## Current style specimen

- `93:417` on page `93:2` — `EXR · Visual Style — Industrial Evidence Atlas`,
  1760 x 3200 at the canvas origin. It is the active visual benchmark.
- The page is an editorial specimen rather than a product screen: a sparse
  nameplate, one dominant platform field with attached evidence ledger, one
  foundation ledger, unequal evidence instruments, exactly two approved
  spatial models, a shared time datum and a concise rule footer.
- It carries the iron palette of D034 and the mature matte grammar of D038:
  canvas `#121416`, persistent plane `#171A1D`, caution `#FF8A3D`, critical
  `#FF5765`, and yellow `#F5C400` as current path, datum, or ownership edge.
- Persistent fields have no shadow and restrained 8–10 px corners. The selected
  inspector uses the only raised lens gradient and a 3 px yellow leading edge.
- The instrument field uses unequal spans because the trace leads, the CAN
  matrix verifies, and host lanes compare. Related evidence shares one chassis.
- The spatial chapter contains exactly two canonical approaches: Bus schematic
  and Hex cell cluster. Both express the same incident and share the same time
  datum and evidence rows. Layered strata is not active.
- Recovery page `0:1` preserves the complete immediate pre-pass sheet at
  `65:1287`; the earlier `84:3` recovery root is consolidated beside it. Page
  `88:2` preserves the complete pre-calm-redesign sheet at `88:3`.
- The light expression has not been built, and its greys no longer follow
  automatically from dark — see D034.
- All values on the sheet are illustrative and labelled as such.

Consult `skills/exrobotics-figma-design/references/project-map.md` for the
per-band node IDs, the SVG-import build technique, and the FigWright operations
that fail on these sheets.

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

- capture every materially changed applicable viewport at a legible scale;
- inspect clipping, alignment, density, and hierarchy;
- scan all visible text for excluded product concepts;
- confirm machine values use Roboto Mono;
- confirm yellow remains scarce and meaningful;
- inspect 44 px targets and focus visibility;
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
