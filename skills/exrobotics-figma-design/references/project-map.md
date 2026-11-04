# Project map

Treat IDs as orientation only. Verify them live through FigWright before use.

## Figma file

- `EX Robotics — Visual Identity & UI Foundations`

**The file was reset to a clean slate before 2026-08-22.** Every component set,
style, variable, and screen recorded in earlier versions of this map no longer
exists. Do not cite those IDs.

## Pages

- `93:2` — `01 Visual Style — Graphite (Dark)`
- `0:1` — `99 Backup · Pre industrial evidence atlas · 2026-08-24`
  (recovery-only; editable pre-pass root `65:1287` and earlier root `84:3`)
- `88:2` — `99 Backup · Pre visual calm redesign · 2026-08-24`
  (recovery-only; editable pre-redesign root `88:3`)

## Current state

- No variable collections.
- No local components, paint styles, text styles, or effect styles.
- Fonts confirmed available in the file: Space Grotesk, Inter, Roboto Mono
  (Regular / Medium / Bold).

## Page `93:2` — dark visual style specimen

Root frame `93:417` — `EXR · Visual Style — Industrial Evidence Atlas`, 1760 x
3200 at the canvas origin. It is the active benchmark and implements D038.

The imported root contains five named SVG groups rather than independent Figma
component frames:

| Group | Purpose |
|---|---|
| `Nameplate` | Editorial identity, direction and issue ledger |
| `Platform evidence field` | Dominant topology, selected-object ledger and shared datum |
| `Foundation ledger` | Typography content classes, state/material ownership and controls |
| `Evidence instruments` | Unequal trace, CAN matrix and host-comparison spans |
| `Approved spatial approaches` | Bus schematic, Hex cell cluster, shared datum and evidence rows |

The page uses a 72 px outer inset and one continuous 1616 px evidence width.
Persistent planes are matte `#171A1D` with an 8–10 px radius and no shadow.
The attached selected-object ledger is the only raised lens and has a 3 px
yellow ownership edge. Yellow identifies the current path or datum; orange and
red appear only for degraded and critical evidence.

Exactly two topology models are active. Bus schematic encodes literal wiring;
Hex cell cluster encodes composition and membership with explicit fan-out.
Labels sit clear of rails and both models share the same incident, time datum,
and evidence rows. Layered strata is rejected by D036.

The complete pre-pass benchmark remains editable at `65:1287` on recovery page
`0:1`. Do not mutate recovery roots during ordinary design work.

## Build technique used on this page

The canonical sheet was authored as one deterministic SVG at
`.design/work/industrial-evidence-atlas.svg` and imported with `import_svg`,
which yields editable vectors and real TEXT nodes. The file intentionally uses
Space Grotesk Regular for its large editorial orientation while retaining the
family semantics in guideline 8a. Matte fills, rails, lens gradient and the
single atmospheric wash are baked into the source so the specimen can be
re-imported reproducibly; product components must still be promoted into Figma
variables, styles and components before screen composition.

### FigWright behaviour worth knowing before you start

**SVG import**

- `clipPath` imports as a native Figma vector mask. This is how the charts' hatch
  fills are built.
- `radialGradient` imports as a native `GRADIENT_RADIAL` paint. Use it for every
  glow; never fake one with a wide low-opacity stroke.
- `pattern` fills do **not** import. The element silently produces no node at
  all, with no error.
- Font weight resolves to two values only: `font-weight` of 500 or less becomes
  Regular, 600 or more becomes Bold. Family-with-style names and CSS
  `font-weight` in a `style` attribute do not help. Every Medium role therefore
  needs a `set_text_properties` pass after import.
- Text nodes are named after their own characters, so `search_nodes` with
  `type: TEXT` and a name substring is the cheap way to find one. The first
  `<text>` element in a module usually lands at the frame's id + 1, which is a
  reasonable guess to verify rather than trust.

**Operations that fail**

- `clone_node` on a full sheet disconnects the plugin. Build a sibling instead
  of duplicating. Cloning a small subtree is fine, and `clone_node` plus
  `reparent_nodes` is the cheapest way to repeat identical content across
  sibling tiles.
- A `batch` of more than about six `set_text_properties` ops times out, because
  each one loads a font. Split font work into chunks of five.
- `batch` only accepts invertible writes. `set_position`, `set_layout_grids`,
  `delete_nodes`, `reparent_nodes` and `resize_nodes` must be called on their
  own.
- `set_text` takes `characters`, not `text`.

Consequence: the page is a specimen artefact, not a component library. Nothing
on it is an instance, a style, or a variable yet. Promote accepted decisions
into real foundations before composing screens.

## Renders

- `.design/renders/visual-style-dark-2026-08-22/` — v1, superseded
- `.design/renders/visual-style-dark-v2-2026-08-23/` — v2 graphite, plus the
  three-way colour option board
- `.design/renders/visual-style-dark-iron-2026-08-23/` — current
- `.design/renders/design-system-consolidation-2026-08-24/before/` — full
  pre-change visual recovery evidence
- `.design/renders/design-system-consolidation-2026-08-24/after/` — final
  typography and approved-spatial-model audit renders
- `.design/renders/visual-calm-redesign-2026-08-24/` — calmer composition run,
  including intermediate and final full-sheet evidence
- `.design/renders/industrial-evidence-atlas-2026-08-24/` — pre-pass backup
  capture, critique crops, corrected pass and final 2x canonical render
