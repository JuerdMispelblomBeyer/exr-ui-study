# Dark analytics — map and area-chart workbench

## Reference identity and evidence quality

- Source: `reference/ref-038__dark-analytics-dashboard__map-and-area-chart.png`.
- Type: direct dark analytics dashboard screenshot.
- Evidence: high for chart craft, map/region comparison, and tooltip state; medium for interaction; low for product-specific visual language.

## Executive design reading

The screen combines a world map, regional rings, a large area chart with an
explicit probe, and supporting statistics. Its chart craft and visible hover
state are useful; its many accent colors, rounded cards, and conventional
analytics arrangement make it a baseline rather than an art direction.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | polished dark analytics | Charcoal cards, map, area chart | DA-AES-01 | Familiar data product |
| Personality | energetic, contemporary | Pink/green/orange/blue accents | DA-AES-01 | Visually lively, semantically busy |
| Density | medium-high | Donut, map, regions, stats, area chart | DA-DEN-01 | Broad evidence coverage |
| Whitespace | moderate | Large modules with clear gutters | DA-DEN-01 | Readable but container-heavy |
| Grid | asymmetric dashboard | Map and chart use larger spans | DA-COMP-01 | Better hierarchy than equal cards |
| Typography | clean sans + strong values | Compact labels, larger numbers | DA-TYPE-01 | Functional hierarchy |
| Color | multicolor categorical | Four bright accent families | DA-COLOR-01 | Series/state roles may collide |
| Geometry | rounded cards, rings, smooth area | Soft component language | DA-GEO-01 | Polished, generic |
| Surfaces | elevated dark modules | Tonal cards with borders | DA-GEO-01 | Clear but fragmented |
| Imagery | data maps and charts | World map and area fill dominate | DA-IMG-01 | Evidence-led |
| Hierarchy | map/chart dual focus | Two major visual anchors | DA-HIER-01 | Good scan, some competition |
| Composition | modular with varied spans | Supporting modules orbit large views | DA-COMP-01 | Role-based sizing partly present |
| Distinctiveness | medium | Chart craft stronger than shell identity | DA-DIST-01 | Competent, not ownable |

## Dimension analysis

### DA-AES-01 — Aesthetic and personality

**OBSERVATION** — A charcoal dashboard combines several bright data colors,
rounded surfaces, and smoothly rendered charts.

**INTERPRETATION** — The product feels polished and active, but its personality
comes from a fashionable analytics palette rather than its subject.

**TRANSFERABLE PRINCIPLE** — Retain chart quality while letting ExR’s platform
architecture and yellow probe define character.

### DA-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Map and area chart receive larger spans; donuts, regional rings,
and statistics occupy smaller supporting modules.

**INTERPRETATION** — The grid has useful hierarchy, though the map and chart
compete as simultaneous focal objects.

**TRANSFERABLE PRINCIPLE** — Choose one focal engineering question and make the
second major view an attached, lower-contrast evidence lens.

### DA-DEN-01 — Density and whitespace

**OBSERVATION** — Many metrics fit comfortably through moderately compact type
and generous but consistent gutters.

**INTERPRETATION** — Density is manageable, yet repeated card padding consumes
space that could hold exact engineering context.

**TRANSFERABLE PRINCIPLE** — Consolidate related plots on shared surfaces and
spend space on source, unit, threshold, and freshness.

### DA-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Larger numbers identify current values; labels and chart axes
use a clean small sans hierarchy.

**INTERPRETATION** — Type is readable and systematic but aesthetically neutral.

**TRANSFERABLE PRINCIPLE** — Add a disciplined mono machine-data layer and use
display typography only for orientation or critical state.

### DA-COLOR-01 — Color and contrast

**OBSERVATION** — Pink, green, orange, and blue distinguish widgets and series
across the page.

**INTERPRETATION** — Color improves recognition locally but lacks one coherent
global semantic grammar.

**TRANSFERABLE PRINCIPLE** — Mute unselected series, use direct labels, reserve
yellow for current/probed, and keep warning/danger meanings stable.

### DA-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — Rounded rectangular cards, donut rings, and smooth filled areas
repeat with similar surface elevation.

**INTERPRETATION** — Component polish is high but the shell is template-like.

**TRANSFERABLE PRINCIPLE** — Use sharp/inset evidence plots inside a joined
chassis and reserve floating rounded geometry for transient inspectors.

### DA-IMG-01 — Imagery and iconography

**OBSERVATION** — A world map, donuts, regional rings, and a large area chart
provide all major imagery.

**INTERPRETATION** — Data is visually rich, but geographic imagery may be
irrelevant to an onboard platform interface.

**TRANSFERABLE PRINCIPLE** — Replace geography with the robot’s actual topology
and keep only chart forms that answer a real diagnostic question.

### DA-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — The area chart shows a visible vertical probe and tooltip;
map/region modules appear selectable. No animation is established.

**INTERPRETATION** — This is direct evidence for inspect-on-hover/probe behavior
and coordinated detail potential.

**TRANSFERABLE PRINCIPLE** — Provide an exact time probe with value, timestamp,
source, and unit, synchronized across traces and events.

### DA-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The most memorable elements are well-crafted charts and a
visible tooltip, not a proprietary composition or surface grammar.

**INTERPRETATION** — Craft/detail is high while distinctiveness remains moderate.

**TRANSFERABLE PRINCIPLE** — Treat it as a chart-quality benchmark and build an
original ExR shell around more truthful system relationships.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Visible chart probe | Makes exact inspection tangible | Shared time probe across telemetry | Exact tooltip styling |
| Varied module spans | Creates some hierarchy | Dominant topology + attached evidence | Exact grid |
| Map/region pairing | Supports overview and comparison | Platform schematic + node comparison | World geography |
| Smooth area hierarchy | Makes trend direction glanceable | One selected metric history | Decorative smoothing |
| Bright category accents | Improves local recognition | Only stable labeled semantics | Four-color page palette |

## Translation decisions

- **Borrow:** chart probe behavior, precise tooltips, varied spans, readable
  supporting statistics, high plot craft.
- **Ignore:** global user analytics, geography, donut summaries, exact grid.
- **Brand-specific:** multicolor palette, source iconography, typography.
- **Accidental:** static screenshot cannot prove cross-filtering or motion.
- **Anti-patterns/limitations:** generic analytics shell; excessive cards and
  rounded rectangles; too many accent colors; dual focal competition; smooth
  areas may hide exact variation; geography is irrelevant to onboard topology.
