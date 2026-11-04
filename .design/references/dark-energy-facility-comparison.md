# Energy facility — spacious comparison dashboard

## Reference identity and evidence quality

- Source: `reference/ref-016__dark-energy-saas__facility-comparison.png`.
- Type: direct dark facility dashboard screenshot.
- Evidence: high for chart hierarchy and comparative composition; medium for interaction; low for product distinctiveness.

## Executive design reading

The screen is a legible, roomy monitoring baseline: large facility identity,
summary values, a dominant time series, and a building comparison. It shows how
to make trends readable at distance, but relies on familiar cards, symmetry, and
purple branding.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | polished dark energy SaaS | Charcoal cards, purple lines | EF-AES-01 | Clean but familiar |
| Personality | calm, managerial | Large labels and broad plots | EF-AES-01 | Less diagnostic intensity |
| Density | medium | KPIs, main trend, comparison | EF-DEN-01 | Easy glance |
| Whitespace | generous | Wide padding around charts | EF-DEN-01 | Comfortable, sometimes wasteful |
| Grid | broad hierarchical bands | KPI row, large chart, comparison | EF-COMP-01 | Conventional but clear |
| Typography | large clean sans | Big facility/title and values | EF-TYPE-01 | Readable at distance |
| Color | charcoal + purple | Purple series and accents | EF-COLOR-01 | Brand color carries focus |
| Geometry | rounded panels | Repeated soft cards | EF-GEO-01 | Friendly, generic |
| Surfaces | layered card field | Tonal panels and subtle borders | EF-GEO-01 | Clear separation |
| Imagery | charts only | Large time series is the hero | EF-IMG-01 | Trends lead |
| Hierarchy | steep | Identity → KPIs → main trend → compare | EF-HIER-01 | Good overview sequence |
| Composition | symmetric horizontal stack | Centered content bands | EF-COMP-01 | Predictable |
| Distinctiveness | low | Purple brand over standard layout | EF-DIST-01 | Aesthetic anonymity |

## Dimension analysis

### EF-AES-01 — Aesthetic and personality

**OBSERVATION** — A charcoal interface uses purple chart lines, large values,
and broad rounded regions.

**INTERPRETATION** — It feels calm and finished but more managerial than
investigative.

**TRANSFERABLE PRINCIPLE** — Preserve calm legibility for the at-a-glance state,
then introduce ExR’s spatial and causal diagnostic language.

### EF-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Summary values form a top row, a large chart spans the center,
and comparison content sits below.

**INTERPRETATION** — The hierarchy is obvious, but the structure follows a
standard dashboard recipe.

**TRANSFERABLE PRINCIPLE** — Use one dominant evidence region, but let a system
question—not convention—determine whether it is topology, trace, camera, or map.

### EF-DEN-01 — Density and whitespace

**OBSERVATION** — Plots and cards have generous padding and large labels.

**INTERPRETATION** — Readability is excellent, while information throughput is
lower than an expert desktop interface needs.

**TRANSFERABLE PRINCIPLE** — Keep critical values readable and compress repeated
container padding, headings, and empty margins.

### EF-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Facility identity and KPI values are large; chart labels are
clean and subordinate.

**INTERPRETATION** — The type hierarchy supports distance viewing but has no
machine-data character.

**TRANSFERABLE PRINCIPLE** — Combine clear system naming with monospaced IDs,
units, timings, and freshness metadata.

### EF-COLOR-01 — Color and contrast

**OBSERVATION** — Purple is used across chart series, accents, and brand details.

**INTERPRETATION** — The palette is coherent but color roles are broad rather
than semantic.

**TRANSFERABLE PRINCIPLE** — Use ExR yellow only for active/current/probed and
keep historical series neutral unless comparison requires hue.

### EF-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — Similar rounded cards contain nearly every region.

**INTERPRETATION** — Consistency improves polish but flattens importance and
creates a standard SaaS appearance.

**TRANSFERABLE PRINCIPLE** — Join related regions, differentiate inset evidence
from raised inspectors, and reduce radius repetition.

### EF-IMG-01 — Imagery and iconography

**OBSERVATION** — A large, smooth time-series chart provides the primary visual;
no spatial model or real imagery appears.

**INTERPRETATION** — Trend is readable but source location and causal context are
absent.

**TRANSFERABLE PRINCIPLE** — Attach traces to real robot nodes and paths, and use
camera/system imagery when it answers the engineering question.

### EF-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — Time range and comparison controls imply chart interaction;
no motion is shown.

**INTERPRETATION** — The likely flow is check summary → inspect trend → compare
facilities.

**TRANSFERABLE PRINCIPLE** — Adapt the sequence to check platform → locate
affected subsystem → inspect evidence → act.

### EF-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The visual identity depends mainly on purple and polished
rounded modules.

**INTERPRETATION** — It is coherent but aesthetically anonymous.

**TRANSFERABLE PRINCIPLE** — Use it as a legibility baseline, not a source of
ExR’s signature language.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Dominant readable trend | Makes change obvious at distance | Selected-node history | Exact energy plot |
| Clear overview sequence | Supports quick orientation | System → cause → evidence | KPI-first recipe |
| Broad comparison panel | Enables relative judgment | Compare three compute nodes/subsystems | Building cards |
| Restrained dark contrast | Comfortable for monitoring | Calibrated diagnostic dark mode | Purple palette |
| Large value typography | Makes key state glanceable | Safety/system state values | Every KPI oversized |

## Translation decisions

- **Borrow:** plot readability, clear scope hierarchy, comparative scanning,
  restrained dark contrast.
- **Ignore:** facility metrics, symmetric KPI row, and generic card structure.
- **Brand-specific:** purple palette and source typography.
- **Accidental:** screenshot does not reveal hover or responsive behavior.
- **Anti-patterns/limitations:** excessive cards/radii; wasted padding; generic
  SaaS composition; weak causal model; brand depends on accent color alone.
