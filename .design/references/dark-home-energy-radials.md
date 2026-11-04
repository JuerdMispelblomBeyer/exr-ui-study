# Home energy — radial category monitor

## Reference identity and evidence quality

- Source: `reference/ref-017__dark-home-energy__radial-distribution-instruments.jpg`.
- Type: direct dark energy-management dashboard screenshot.
- Evidence: high for multi-view chart composition and radial geometry; medium for interaction; low for semantic accessibility.

## Executive design reading

The screen pairs a conventional device/mode rail and small line charts with an
expressive concentric radial category instrument. The radial creates a strong
focal object, but many hues and unfamiliar encoding increase interpretation
cost.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | dark consumer instrumentation | Grey shell, luminous radial | HR-AES-01 | Technical but approachable |
| Personality | exploratory, colorful | Concentric categories and small charts | HR-AES-01 | Engaging, less austere |
| Density | medium-high | Nav, three traces, bar/table, radial | HR-DEN-01 | Multiple evidence modes |
| Whitespace | moderate | Dark gaps around focal radial | HR-DEN-01 | Supports one visual anchor |
| Grid | asymmetric evidence grid | Radial lower right, plots above/left | HR-COMP-01 | Focal imbalance creates rhythm |
| Typography | compact neutral sans | Small values and labels | HR-TYPE-01 | Functional but secondary |
| Color | multihue categorical | Green, yellow, red, blue rings | HR-COLOR-01 | Rich but semantically crowded |
| Geometry | concentric radial + rectangular shell | Rings contrast with panels | HR-GEO-01 | One special instrument stands out |
| Surfaces | low-relief dark modules | Tonal panels with few shadows | HR-GEO-01 | Evidence remains coherent |
| Imagery | data visualization | Radial is main visual object | HR-IMG-01 | Data provides identity |
| Hierarchy | radial and top traces | Two competing first reads | HR-HIER-01 | Focal hierarchy needs tuning |
| Composition | varied chart mosaic | Unequal spans and chart types | HR-COMP-01 | Avoids total repetition |
| Distinctiveness | medium-high | Concentric multicolor instrument | HR-DIST-01 | Memorable, decoding-heavy |

## Dimension analysis

### HR-AES-01 — Aesthetic and personality

**OBSERVATION** — A charcoal energy interface combines familiar charts with a
bright concentric category visualization.

**INTERPRETATION** — One expressive instrument gives an otherwise conventional
dashboard personality.

**TRANSFERABLE PRINCIPLE** — Let one ExR-specific instrument—such as LAN/CAN
path health or subsystem ring—carry visual recognition.

### HR-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Three small plots align across the top; a table/bar region and
large radial occupy unequal lower spans.

**INTERPRETATION** — Varied span and chart form produce rhythm, though two strong
regions compete.

**TRANSFERABLE PRINCIPLE** — Establish a single dominant question per viewport
and reduce saturation/scale of supporting evidence.

### HR-DEN-01 — Density and whitespace

**OBSERVATION** — The screen contains many readings but preserves dark gutters
and open space around the radial.

**INTERPRETATION** — Density can coexist with a focal object when support regions
stay compact.

**TRANSFERABLE PRINCIPLE** — Concentrate supporting telemetry in aligned strips
around a larger system model.

### HR-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Small neutral labels and values defer to the charts.

**INTERPRETATION** — Visual data dominates, but exact reading may suffer at
screenshot scale.

**TRANSFERABLE PRINCIPLE** — Keep labels compact while surfacing selected value,
unit, source, and freshness in an attached inspector.

### HR-COLOR-01 — Color and contrast

**OBSERVATION** — Many saturated hues distinguish ring categories and chart
series.

**INTERPRETATION** — The view is visually engaging but state meaning becomes
hard to learn and inaccessible by color alone.

**TRANSFERABLE PRINCIPLE** — Use yellow for current selection, neutral families
for categories, and labeled semantic colors only for actual health states.

### HR-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — A concentric radial contrasts with restrained rectangular
modules; elevation is modest.

**INTERPRETATION** — Special geometry remains effective because it is rare.

**TRANSFERABLE PRINCIPLE** — Reserve bespoke geometry for a relationship that
benefits from circular encoding; do not use radial charts for novelty.

### HR-IMG-01 — Imagery and iconography

**OBSERVATION** — Charts act as imagery and icons remain small utilities.

**INTERPRETATION** — Visual identity stays data-led, though the radial’s exact
meaning is not immediately obvious.

**TRANSFERABLE PRINCIPLE** — Every expressive visual must answer a named
engineering question and expose a precise textual reading.

### HR-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — Radial segments and plot points appear selectable; multiple
time-series imply coordinated filtering. No motion is shown.

**INTERPRETATION** — The likely interaction is select category/device and inspect
its history.

**TRANSFERABLE PRINCIPLE** — Share selection across system object and traces,
but do not infer animated ring behavior.

### HR-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The concentric multicolor category map is the recognizable
element.

**INTERPRETATION** — Distinctiveness is meaningful only if users can decode the
geometry faster than a simpler chart.

**TRANSFERABLE PRINCIPLE** — Require every signature instrument to outperform a
table or bar chart for the target decision.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Expressive radial anchor | Makes one relationship memorable | Only for cyclic/layered subsystem state | Exact rings |
| Compact supporting strip | Keeps multiple traces available | CPU/GPU/network trends around topology | Exact chart arrangement |
| Rare special geometry | Creates contrast | One platform-specific instrument | Radials throughout |
| Data-as-imagery | Avoids stock decoration | Truthful system visuals | Ambiguous encoding |
| Varied module spans | Breaks repetition | Role-based evidence regions | Uncontrolled mosaic |

## Translation decisions

- **Borrow:** rare signature instrument, supporting evidence strip, varied spans,
  low-relief shell.
- **Ignore:** home-energy categories, exact radial encoding, device taxonomy.
- **Brand-specific:** multicolor palette and source navigation.
- **Accidental:** screenshot cannot prove linked highlighting or motion.
- **Anti-patterns/limitations:** too many colors; unclear radial decoding;
  competing focal regions; small text; special geometry can become ornamental.
