# Opportunity workspace — nested navigation crop

## Reference identity and evidence quality

- Source: `reference/b0bd857d26850dbacf029d60cca8932e.jpg`.
- Type: close crop of a light enterprise workspace.
- Evidence: high for navigation layering; low for content, hierarchy, and interaction states beyond selection.

## Executive design reading

The useful idea is a two-depth navigation system: a narrow global tool rail and
a broader contextual taxonomy. Their contrasting surfaces make application
scope and local scope immediately distinguishable.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | restrained enterprise | Black rail, pale secondary pane | ON-AES-01 | Functional over expressive |
| Personality | orderly, quiet | Repeated rows and subtle selection | ON-AES-01 | Familiar orientation |
| Density | medium | Compact nested lists | ON-DEN-01 | Navigation is information-rich |
| Whitespace | moderate | Padding around row groups | ON-DEN-01 | Groups remain scannable |
| Grid | nested vertical rails | Two aligned left columns | ON-COMP-01 | Scope is spatially encoded |
| Typography | compact neutral sans | Small labels with regular rhythm | ON-TYPE-01 | Fast scanning, little identity |
| Color | neutral with one active cue | Black, off-white, pale highlight | ON-COLOR-01 | State survives without palette |
| Geometry | straight shell, soft row selection | Minimal radius | ON-GEO-01 | Calm navigational chassis |
| Surfaces | dark global / light contextual | Strong tonal layer break | ON-GEO-01 | Depth via surface role |
| Imagery | none | Icons and text only | ON-IMG-01 | Navigation remains utilitarian |
| Hierarchy | scope-led | Global icons → local categories | ON-HIER-01 | Users know where they are |
| Composition | edge-anchored | Navigation owns a narrow slice | ON-COMP-01 | Workbench remains available |
| Distinctiveness | low-medium | Memorable mainly for nested rails | ON-DIST-01 | Structure useful; styling generic |

## Dimension analysis

### ON-AES-01 — Aesthetic and personality

**OBSERVATION** — A black icon rail sits beside a soft off-white category pane.

**INTERPRETATION** — Contrast communicates scope more effectively than
decoration; the styling itself is conventional.

**TRANSFERABLE PRINCIPLE** — Visually separate global robot context from local
subsystem navigation using surface role, not another card.

### ON-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Both navigation depths are flush to the left edge and share a
strict vertical rhythm.

**INTERPRETATION** — Persistent spatial position builds a reliable mental map.

**TRANSFERABLE PRINCIPLE** — Keep global destinations stable and reveal the
selected system’s tree in an attached contextual lens.

### ON-DEN-01 — Density and whitespace

**OBSERVATION** — Rows are compact but grouped with larger breaks and headings.

**INTERPRETATION** — Density is managed through rhythm instead of large row
containers.

**TRANSFERABLE PRINCIPLE** — Use compact rows plus group gaps for deep system
trees; avoid pill-wrapping every entry.

### ON-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Small neutral text changes weight subtly between headings,
items, and the active row.

**INTERPRETATION** — Hierarchy is adequate but visually anonymous.

**TRANSFERABLE PRINCIPLE** — Preserve compactness while adding monospaced node
IDs and clearer selected-system naming where engineers need precision.

### ON-COLOR-01 — Color and contrast

**OBSERVATION** — Tonal neutrals do nearly all the work; selected state is a
quiet light band.

**INTERPRETATION** — Accent scarcity protects attention, though the active cue
may be too weak.

**TRANSFERABLE PRINCIPLE** — Use ExR yellow as a slim location/probe mark rather
than as the entire navigation background.

### ON-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — The global rail is flat and dark; the contextual pane is flat
and pale; selected rows use modest softness without shadows.

**INTERPRETATION** — Navigation depth is conveyed through plane changes.

**TRANSFERABLE PRINCIPLE** — Define a small set of persistent chassis planes and
reserve elevation for temporary overlays.

### ON-IMG-01 — Imagery and iconography

**OBSERVATION** — Simple monochrome icons identify global destinations; no
illustration appears.

**INTERPRETATION** — Icons support recall but cannot explain complex subsystems.

**TRANSFERABLE PRINCIPLE** — Use stable icons at the global level and truthful
schematics inside the workbench.

### ON-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — Icon selection determines which local taxonomy appears; row
highlight indicates current scope. Motion is not shown.

**INTERPRETATION** — The interface exposes progressive navigation depth.

**TRANSFERABLE PRINCIPLE** — Make global → subsystem → component scope visible
as a stable hierarchy, with no invented motion requirement.

### ON-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The strongest characteristic is the sharp black-to-soft-light
transition between navigation levels.

**INTERPRETATION** — This is a useful chassis pattern, not a complete art
direction.

**TRANSFERABLE PRINCIPLE** — Borrow the nested lens model while giving ExR its
own instrument geometry, type, and signal behavior.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Two-depth rail | Makes scope explicit | Global platform rail + contextual system tree | Exact taxonomy |
| Tonal role split | Differentiates layers without borders | Dark chassis, lighter lens | Exact black/cream colors |
| Compact grouped rows | Holds many destinations | Dense system tree with group gaps | Enterprise row styling |
| Edge anchoring | Preserves central work area | Keep rails narrow and persistent | Exact widths |
| Quiet selection band | Maintains calm | Add a yellow probe edge and stronger label | Low-contrast-only state |

## Translation decisions

- **Borrow:** nested navigation, stable rails, compact grouped lists, role-based
  planes.
- **Ignore:** sales/opportunity taxonomy and placeholder content.
- **Brand-specific:** none beyond the source icon set and product structure.
- **Accidental:** crop hides main workspace and responsive behavior.
- **Anti-patterns/limitations:** generic enterprise character; weak selected
  contrast; icon-only global rail needs tooltips and labels; two rails can become
  expensive if both are always fully open.
