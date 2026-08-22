# Light activity calendar

## Reference identity and evidence quality

- Source: `reference/9d38ab315ad57ef606f310f8a0cbfb4d.jpg`.
- Visible label: Crack.
- Type: direct light dashboard concept.
- Evidence: medium; some low-contrast details are unreadable.

## Executive design reading

The reference treats time as the composition. Large day/week blocks, a dominant
activity strip, and a right-side monthly summary create an editorial temporal
landscape rather than a stack of standard charts.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | editorial-analytic | Large type, pale field, abstract activity blocks | CAL-AES-01 | Data feels composed |
| Personality | quiet, playful, experimental | Soft greys with black/purple/red blocks | CAL-AES-01 | Restraint plus one eccentric device |
| Density | medium, uneven | Large activity field plus compact right summary | CAL-DEN-01 | Time scales get different density |
| Whitespace | expansive | Pale gaps isolate date and profile zones | CAL-DEN-01 | Space creates pacing |
| Grid | asymmetric split | Main timeline and narrow month column | CAL-COMP-01 | Time hierarchy is spatial |
| Typography | display-led neutral sans | Oversized day/profile labels | CAL-TYPE-01 | Type anchors composition |
| Color | restrained neutrals + sparse event hues | Purple/red mark activity exceptions | CAL-COLOR-01 | Event color stays local |
| Geometry | soft blocks with minimal borders | Broad panels and activity rectangles | CAL-GEO-01 | Shape depicts time |
| Surfaces | flat/soft | Few edges, tonal layers | CAL-GEO-01 | Low visual friction |
| Imagery | absent | Abstract block timeline is primary visual | CAL-IMG-01 | Data is imagery |
| Hierarchy | steep | Current day/activity → profile stats → history | CAL-HIER-01 | Current state wins |
| Composition | temporal landscape | Activity strip spans the main field | CAL-COMP-01 | Product concept shapes layout |
| Distinctiveness | recognizable | Abstract block history and editorial type | CAL-DIST-01 | Nonstandard data form creates identity |

## Dimension analysis

### CAL-AES-01 — Overall aesthetic and personality

**OBSERVATION** — Warm-white surfaces, large black type, soft grey blocks, and a
few saturated activity rectangles create a quiet but experimental field.

**INTERPRETATION** — The UI feels editorial because composition and typography
matter as much as controls.

**TRANSFERABLE PRINCIPLE** — Give one meaningful system dimension—time, topology,
or dependency—an expressive spatial form while keeping the rest restrained.

### CAL-COMP-01 — Composition, grid, alignment

**OBSERVATION** — A broad left timeline shares a top axis with current-day cards;
a narrow right column stacks personal stats and prior weeks.

**INTERPRETATION** — Current activity and historical context remain visible at
different scales without equal modules.

**TRANSFERABLE PRINCIPLE** — Let the dominant time scale own the largest span and
place alternate scales in a narrower aligned rail.

### CAL-DEN-01 — Density and whitespace

**OBSERVATION** — Large pale areas surround current-day blocks; the activity strip
and right history rail are denser.

**INTERPRETATION** — Whitespace prioritizes current context, while denser zones
reward inspection.

**TRANSFERABLE PRINCIPLE** — Use sparse current-state orientation beside denser
history/evidence regions.

### CAL-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Large day, task, and profile text functions as mass; small grey
annotations and outlined count pills remain secondary.

**INTERPRETATION** — Typography is the primary structural tool, not a label layer.

**TRANSFERABLE PRINCIPLE** — Use concise typographic anchors to shape the scan path
when the interface has one clear current state.

### CAL-COLOR-01 — Color and contrast

**OBSERVATION** — Most structure is monochrome; purple and red identify activity
segments, with black defining current cards.

**INTERPRETATION** — Color marks events rather than surfaces. Greyscale preserves
macro hierarchy but low-contrast grey labels may disappear.

**TRANSFERABLE PRINCIPLE** — Use brand/status color for events and selected
segments; maintain readable label contrast independent of hue.

### CAL-GEO-01 — Geometry, borders, shadows, surfaces

**OBSERVATION** — Broad soft cards, minimally rounded activity blocks, and almost
no visible shadows create a flat editorial canvas.

**INTERPRETATION** — Different shape scales separate containers from temporal
data without heavy outlines.

**TRANSFERABLE PRINCIPLE** — Keep persistent surfaces flat and let data marks use
more exact geometry.

### CAL-IMG-01 — Imagery and iconography

**OBSERVATION** — No photography appears; block patterns, tiny bars, and minimal
icons represent activity and controls.

**INTERPRETATION** — Abstract data marks become the central image.

**TRANSFERABLE PRINCIPLE** — Develop a product-specific state map whose shape is
readable before labels.

### CAL-HIER-01 — Information hierarchy, interaction, motion

**OBSERVATION** — Home/profile tabs, add, search, filter, edit, and selected task
states are visible; block sequences imply temporal continuation, not actual motion.

**INTERPRETATION** — Current-day manipulation is clear while history remains
quiet. Motion inference is low confidence.

**TRANSFERABLE PRINCIPLE** — Keep current scope/actions visually near the active
state and treat history as a continuous supporting rail.

### CAL-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — Large typographic labels and an abstract block timeline define
the silhouette.

**INTERPRETATION** — The design is memorable because its data shape is unusual,
though some content clarity is sacrificed.

**TRANSFERABLE PRINCIPLE** — Invent one recognizable state visualization from
real product behavior; test it against precise labels and edge cases.

## Signature moves

| Move | Observation | Interpretation | Transfer | Do not copy |
|---|---|---|---|---|
| Temporal block landscape | Activity is a chain of irregular rectangles | Time becomes spatial | Event/state strip for diagnostics | Exact block pattern |
| Current-vs-history split | Main day and right week rail coexist | Multiple time scales stay visible | Current event + history inspector | Personal tracking content |
| Typographic mass | Day/task/profile labels shape layout | Type establishes focus | Large selected subsystem/state label | Exact typeface/line breaks |
| Sparse neutral field | Pale space isolates key states | Calm editorial pacing | Focus mode or incident review | Excess emptiness in routine views |
| Local event color | Purple/red only in activity strip | Color marks exceptions | Yellow active segment + semantic failures | Source hues |

## Translation decisions

- **Borrow:** current/history composition, data-as-imagery, typographic anchors,
  event-local color, and flat surfaces.
- **Ignore:** personal productivity content, profile panel, exact block shapes,
  and pale placeholder labels.
- **Brand-specific:** Crack wordmark and purple/red event palette.
- **Accidental:** some text is blurred/low resolution.
- **Anti-patterns/limitations:** low contrast; abstract marks may obscure exact
  values; spacious editorial rhythm is unsuitable for dense routine monitoring
  unless bounded to focus/history modes.

