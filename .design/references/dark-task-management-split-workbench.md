# Dark task-management split workbench

## Reference identity and evidence quality

- Source: `reference/357cd47f6a5b40888f31d24d957647d8.jpg`.
- Type: direct dashboard crop.
- Evidence: medium; screenshot is cropped but major layout and states are clear.

## Executive design reading

The screen achieves density through a strong split workbench: scheduled work
and trend evidence occupy the left, personal activity and project context the
right. Thin green outlines and small status colors highlight exceptions without
brightening the whole dark canvas.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | compact dark operations | Dense modules, thin dividers, live charts | TASK-AES-01 | Repeated work feels serious |
| Personality | pragmatic, focused | Sparse chrome and direct labels | TASK-AES-01 | Low ceremony |
| Density | high, rhythmic | Dense calendar/trend areas with quiet gutters | TASK-DEN-01 | Much fits without a wall of text |
| Whitespace | compressed/structural | Space exists mainly between work zones | TASK-DEN-01 | Gaps show grouping |
| Grid | split modular | Strong central divider and nested columns | TASK-COMP-01 | Work modes remain distinct |
| Typography | compact neutral | Large percentages, small labels | TASK-TYPE-01 | Values punctuate dense UI |
| Color | mostly monochrome + status accents | Green/red/blue remain local | TASK-COLOR-01 | Color marks exceptions |
| Geometry | medium-soft modules, thin edges | Rounded blocks with restrained elevation | TASK-GEO-01 | Controls feel accessible |
| Surfaces | nested low relief | Dark-on-black layers separated by value | TASK-GEO-01 | Persistence without glass |
| Imagery | supporting avatars only | Faces identify team context | TASK-IMG-01 | Human evidence stays local |
| Hierarchy | moderate | Schedule block and 83% activity lead | TASK-HIER-01 | Two parallel priorities |
| Composition | two-column workbench | Vertical division organizes screen | TASK-COMP-01 | Split follows workflow |
| Distinctiveness | contextual | Dense split and outlined selection | TASK-DIST-01 | Stronger as workflow than style |

## Dimension analysis

### TASK-AES-01 — Overall aesthetic and personality

**OBSERVATION** — Near-black surfaces, compact labels, subtle borders, and small
status accents create a subdued operational field.

**INTERPRETATION** — The UI feels focused because decoration is suppressed and
information carries the visual interest.

**TRANSFERABLE PRINCIPLE** — Let meaningful states, traces, and controls produce
character in routine engineering views; keep the shell quiet.

### TASK-COMP-01 — Composition, grid, alignment

**OBSERVATION** — A hard vertical split separates meetings/trends from activity/
projects; nested blocks align to each half.

**INTERPRETATION** — The composition supports parallel work modes rather than a
single scrolling page.

**TRANSFERABLE PRINCIPLE** — Use a split workbench when users must compare active
operations with evidence or context continuously.

### TASK-DEN-01 — Density and whitespace

**OBSERVATION** — Modules are tightly packed but local content alternates between
sparse event tiles and dense charts.

**INTERPRETATION** — Density is manageable because internal rhythm varies and
major zones have explicit boundaries.

**TRANSFERABLE PRINCIPLE** — In high-density interfaces, vary internal density
and preserve clear work-zone boundaries instead of enlarging all padding.

### TASK-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Large numbers and concise headings punctuate small operational
copy; weight contrast is restrained.

**INTERPRETATION** — The typography is efficient but somewhat generic; numbers
carry most focal weight.

**TRANSFERABLE PRINCIPLE** — Use local numeric emphasis inside instruments while
reserving stronger display character for global state or selected scope.

### TASK-COLOR-01 — Color and contrast

**OBSERVATION** — Green outlines a selected schedule block and marks success;
red marks cancellation; blue is limited to a secondary link.

**INTERPRETATION** — Color remains semantic and localized, though selection and
success sharing green may be ambiguous.

**TRANSFERABLE PRINCIPLE** — Keep state color local and distinguish selection
from health through shape, label, or a separate brand signal.

### TASK-GEO-01 — Geometry, borders, shadows, surfaces

**OBSERVATION** — Rounded modules use fine outlines and value shifts; selection
adds an outline rather than large elevation.

**INTERPRETATION** — Low-relief layering preserves density and keeps temporary
state visible.

**TRANSFERABLE PRINCIPLE** — Signal selected regions through precise edge/state
changes before adding shadow or glow.

### TASK-IMG-01 — Imagery and iconography

**OBSERVATION** — Small avatars only appear where team membership matters; icons
are compact and functional.

**INTERPRETATION** — Imagery adds ownership rather than atmosphere.

**TRANSFERABLE PRINCIPLE** — Include imagery only when it identifies a real
actor, device, or evidence source.

### TASK-HIER-01 — Information hierarchy, interaction, motion

**OBSERVATION** — Add, filter, close, refresh, dropdown, and manage affordances
are attached to their modules; no motion is shown.

**INTERPRETATION** — Local ownership makes the dense interface operable without a
large global toolbar.

**TRANSFERABLE PRINCIPLE** — Keep filters and actions adjacent to the evidence or
object they modify; preserve a stable global chassis.

### TASK-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The split workbench and outlined active zone are the strongest
recognizable choices; individual cards remain conventional.

**INTERPRETATION** — The composition is useful, but a generic card anatomy keeps
the visual language from becoming memorable.

**TRANSFERABLE PRINCIPLE** — Borrow the workflow split, then replace generic
modules with product-specific instruments and relationships.

## Signature moves

| Move | Observation | Interpretation | Transfer | Do not copy |
|---|---|---|---|---|
| Parallel workbench | Two durable columns support different jobs | Context remains visible | Pair topology with evidence/inspector | Exact task content |
| Edge-based selection | Thin outline marks active schedule | Selection stays precise | Yellow/inset contour for selected scope | Green outline |
| Local action ownership | Tools sit inside owning modules | Less toolbar scanning | Attach actions to affected subsystem | Icon set |
| Density modulation | Sparse tiles alternate with dense charts | High density stays legible | Vary density by evidence role | Card sizes |
| Quiet shell | Chrome recedes behind content | Work remains primary | Keep navigation low contrast | Near-black palette recipe |

## Translation decisions

- **Borrow:** split workbench, local controls, restrained status color, and
  density modulation.
- **Ignore:** task-management content, avatars, generic project card, and exact
  column ratio.
- **Brand-specific:** none clearly identifiable beyond icon/green styling.
- **Accidental:** cropped left content and missing viewport bounds.
- **Anti-patterns/limitations:** equal rounded modules remain generic; two large
  focal regions can compete; small grey labels require contrast validation.

