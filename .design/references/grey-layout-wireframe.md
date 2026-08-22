# Grey layout wireframe

## Reference identity and evidence quality

- Source: `reference/64b7d277f909aa5b5084805d0926f82f.jpg`.
- Type: abstract layout/wireframe composition, not a finished interface.
- Evidence: high for massing and hierarchy; none for typography, color system,
  realistic content, interaction detail, or motion.

## Executive design reading

The wireframe is useful because it exposes the spatial skeleton without surface
styling: a slim tool rail, one dominant stage, stacked side inspectors, and two
secondary bottom modules. Its value is compositional, not aesthetic.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | abstract structural | Greyscale placeholders only | WIRE-AES-01 | Judge layout without polish |
| Personality | neutral | No brand or content cues | WIRE-AES-01 | Personality is unsupported |
| Density | low–medium | One large stage, compact supports | WIRE-DEN-01 | Dominance is explicit |
| Whitespace | balanced | Broad gutters around main stage | WIRE-DEN-01 | Regions remain separable |
| Grid | asymmetric modular | Rail + main + stacked right + bottom row | WIRE-COMP-01 | Strong workbench skeleton |
| Typography | unsupported | Text is placeholder strokes | WIRE-TYPE-01 | Do not infer type rules |
| Color | unsupported monochrome | Grey values only | WIRE-COLOR-01 | Color cannot be learned here |
| Geometry | very soft enclosure | Large uniform radii | WIRE-GEO-01 | Role distinction is weak |
| Surfaces | flat placeholders | Tonal boxes without material semantics | WIRE-GEO-01 | Surface system is unresolved |
| Imagery | placeholder | Main stage shows generic image glyph | WIRE-IMG-01 | Asset role only is inferable |
| Hierarchy | steep | Main stage dominates | WIRE-HIER-01 | Clear first read |
| Composition | dominant stage with attached inspectors | Unequal regions surround main object | WIRE-COMP-01 | Good overview/detail scaffold |
| Distinctiveness | low | Generic wireframe shapes | WIRE-DIST-01 | Structure needs product specificity |

## Dimension analysis

### WIRE-AES-01 — Overall aesthetic and personality

**OBSERVATION** — The image deliberately suppresses color, type, content, and
detail, leaving only rounded masses.

**INTERPRETATION** — It is a composition study rather than a style reference;
personality cannot be inferred.

**TRANSFERABLE PRINCIPLE** — Evaluate major massing in neutral wireframes before
surface styling, but do not promote placeholder geometry into the final system.

### WIRE-COMP-01 — Composition, grid, alignment

**OBSERVATION** — A narrow left rail, dominant upper-left stage, two stacked
right modules, and two lower modules align on a compact asymmetric grid.

**INTERPRETATION** — The scaffold supports stable context, a dominant object,
attached inspectors, and secondary evidence.

**TRANSFERABLE PRINCIPLE** — Start engineering views from one dominant schematic
with adjacent detail/evidence zones rather than an equal dashboard mosaic.

### WIRE-DEN-01 — Density and whitespace

**OBSERVATION** — The main stage is sparse; lower/right regions imply higher
information density; gutters are consistent.

**INTERPRETATION** — Density is reserved for support while the primary object
retains visual breathing room.

**TRANSFERABLE PRINCIPLE** — Protect the dominant system view from overlay noise
and concentrate detail in attached secondary regions.

### WIRE-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Text is represented only by grey lines.

**INTERPRETATION** — No typeface, scale, or content behavior is evidenced.

**TRANSFERABLE PRINCIPLE** — Carry only the role hierarchy into exploration;
derive actual typography from the target design system and real content.

### WIRE-COLOR-01 — Color and contrast

**OBSERVATION** — Greyscale tonal blocks separate regions.

**INTERPRETATION** — Macro hierarchy is color-independent, which is useful, but
no semantic palette can be inferred.

**TRANSFERABLE PRINCIPLE** — Ensure composition passes in greyscale before using
brand color as a finishing signal.

### WIRE-GEO-01 — Geometry, borders, shadows, surfaces

**OBSERVATION** — Every region uses large similar radii; borders and shadows are
not meaningfully differentiated.

**INTERPRETATION** — The uniform geometry is appropriate for a sketch but would
be generic and semantically weak as finished UI.

**TRANSFERABLE PRINCIPLE** — Preserve the layout relationships, then assign
radius, edge, and elevation by actual surface role.

### WIRE-IMG-01 — Imagery and iconography

**OBSERVATION** — A generic image placeholder occupies the dominant stage; tool
rail and list icons are abstract blocks.

**INTERPRETATION** — The composition expects a visual object, but its nature is
unresolved.

**TRANSFERABLE PRINCIPLE** — Replace placeholders early with real topology,
camera, schematic, or diagnostic evidence to test the composition.

### WIRE-HIER-01 — Information hierarchy, interaction, motion

**OBSERVATION** — Rail, main stage, stacked inspector, bottom list, and supporting
graphic imply navigation, selection, and drill-down; no state or motion is shown.

**INTERPRETATION** — Only the spatial hierarchy is defensible.

**TRANSFERABLE PRINCIPLE** — Use the scaffold to prototype flow, then validate
selection, actions, and motion with real component states.

### WIRE-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The dominant-stage arrangement is useful but composed from
generic rounded placeholders.

**INTERPRETATION** — It offers no finished visual DNA and must not become a style
reference.

**TRANSFERABLE PRINCIPLE** — Borrow the unequal spatial hierarchy only; generate
distinctiveness from product-specific instruments and system relationships.

## Signature moves

| Move | Observation | Interpretation | Transfer | Do not copy |
|---|---|---|---|---|
| Dominant stage | One large region owns the viewport | Clear focus | Main platform schematic | Placeholder image |
| Attached side stack | Two small regions hug the stage | Contextual inspection | Selected-object status/actions | Exact placement |
| Persistent tool rail | Slim vertical strip remains separate | Mode control is stable | Compact inspect/diagnose/change rail | Generic icon stack |
| Bottom evidence band | List and visual sit beneath stage | Detail follows context | Events/logs/trace rail | Uniform rounded boxes |
| Color-independent massing | Hierarchy works in grey | Composition precedes styling | Greyscale composition gate | Grey palette |

## Translation decisions

- **Borrow:** dominant-stage scaffold, attached inspectors, supporting evidence
  band, and greyscale composition testing.
- **Ignore:** all placeholder dimensions, generic image/list content, and icon
  blocks.
- **Brand-specific:** none.
- **Accidental:** monochrome values and identical radii are sketch artifacts.
- **Anti-patterns/limitations:** not a finished UI; excessive rounded containers;
  unsupported typography, color, surface, and interaction claims.

