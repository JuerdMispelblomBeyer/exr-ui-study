# Industrial IoT — facility health cards

## Reference identity and evidence quality

- Source: `reference/ref-019__dark-industrial-iot__device-health-table.jpg`.
- Type: direct industrial monitoring dashboard screenshot.
- Evidence: high for component inventory and status comparison; medium for workflow; low for distinctiveness and causal visualization.

## Executive design reading

The screen is a clean industrial monitoring baseline: large metrics, facility
health cards with donut gauges, and a device table. It communicates state but
stays category-oriented, overuses containers, and provides little sense of
connectivity or fault propagation.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | dark industrial SaaS | Navy shell, metrics, donuts, table | II-AES-01 | Familiar monitoring language |
| Personality | orderly, safe | Consistent cards and status colors | II-AES-01 | Polished but anonymous |
| Density | medium | Summary, three facilities, device table | II-DEN-01 | Comfortable comparison |
| Whitespace | generous | Large card padding | II-DEN-01 | Low throughput |
| Grid | regular card stack | KPI row and three equal health cards | II-COMP-01 | Strong consistency, weak focus |
| Typography | clean sans | Large metrics and compact labels | II-TYPE-01 | Readable, generic |
| Color | navy + green/yellow/red | Donut health states | II-COLOR-01 | Familiar semantics |
| Geometry | repeated rounded rectangles/donuts | Equal cards and circular gauges | II-GEO-01 | Template-like |
| Surfaces | layered cards | Borders and raised panels | II-GEO-01 | Fragmented overview |
| Imagery | abstract gauges only | No equipment/topology imagery | II-IMG-01 | Weak system model |
| Hierarchy | summary → facility → device | Category drill-down | II-HIER-01 | Understandable but indirect |
| Composition | symmetric modular | Equal columns and bands | II-COMP-01 | Uniform visual weight |
| Distinctiveness | low | Common dashboard conventions | II-DIST-01 | Consistent does not mean memorable |

## Dimension analysis

### II-AES-01 — Aesthetic and personality

**OBSERVATION** — A navy dashboard uses familiar cards, donut gauges, and status
badges.

**INTERPRETATION** — It reads as industrial because of content labels, not
because its visual language is specific to the system.

**TRANSFERABLE PRINCIPLE** — Derive ExR character from actual platform topology,
measurement marks, and state behavior rather than industrial nouns.

### II-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Large metrics form a row, three health cards align equally,
and a device table spans below.

**INTERPRETATION** — Equality simplifies implementation but suppresses the most
consequential subsystem or current fault.

**TRANSFERABLE PRINCIPLE** — Break the grid around the dominant system question
and allow affected components to change visual weight.

### II-DEN-01 — Density and whitespace

**OBSERVATION** — Cards use broad padding and repeated titles around modest data.

**INTERPRETATION** — The screen spends too much space on containers.

**TRANSFERABLE PRINCIPLE** — Convert repeated health cards into a connected
schematic, compact health matrix, or aligned rows.

### II-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Large metric numerals and medium headings repeat across the
screen.

**INTERPRETATION** — Uniform type roles reinforce uniform module weight.

**TRANSFERABLE PRINCIPLE** — Use distinct type roles for system orientation,
selected state, machine identifiers, and evidence instead of scaling every KPI.

### II-COLOR-01 — Color and contrast

**OBSERVATION** — Green, yellow, and red appear in donut gauges and badges.

**INTERPRETATION** — Semantics are familiar but heavily color-dependent; yellow
risks collision between warning and ExR identity.

**TRANSFERABLE PRINCIPLE** — Assign brand yellow to current/probe/action and use
explicit icons, labels, and separate warning treatment.

### II-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — Rounded rectangles contain other rounded rectangles and donut
gauges.

**INTERPRETATION** — Repetition creates technical neatness but also generic card
soup.

**TRANSFERABLE PRINCIPLE** — Use joined surfaces, shared dividers, and shape
languages tied to evidence type.

### II-IMG-01 — Imagery and iconography

**OBSERVATION** — Donuts are the only large visuals; actual facilities, devices,
and links are not depicted.

**INTERPRETATION** — Health percentage is shown without causal or spatial
context.

**TRANSFERABLE PRINCIPLE** — Show the computers, LAN, CAN, subsystem branches,
and containers directly, then attach compact health readings.

### II-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — Cards and device rows imply drill-down; no linked selection or
motion is evidenced.

**INTERPRETATION** — The flow is browse categories rather than investigate from
fault to cause.

**TRANSFERABLE PRINCIPLE** — Organize around detect → locate → explain → act and
keep the selected path visible.

### II-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The design is consistent and polished but uses standard SaaS
patterns throughout.

**INTERPRETATION** — It demonstrates that a technically correct system can still
fail distinctiveness.

**TRANSFERABLE PRINCIPLE** — Use this reference only as an anti-baseline and
component completeness check.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Three-way health comparison | Makes relative state easy | Compare Intel and two Jetsons | Equal facility cards |
| Device table | Preserves exact detail | Compact node/container inventory | Put all detail in overview |
| Familiar semantic states | Reduces learning | Labeled health vocabulary | Color-only donuts |
| Stable grid | Supports predictability | Alignment within evidence regions | Uniform page composition |
| Summary-to-detail sequence | Gives a clear reading order | Platform → node → component | Category-first dashboard |

## Translation decisions

- **Borrow:** comparative health, exact device table, familiar labeled states,
  predictable evidence grammar.
- **Ignore:** facility framing, equal card rows, donut gauges, generic KPI band.
- **Brand-specific:** navy palette and source iconography.
- **Accidental:** screenshot does not show incident mode or linked selection.
- **Anti-patterns/limitations:** excessive cards/radii; uniform weight; sparse
  information; generic SaaS aesthetic; no topology; color-dependent status;
  aesthetically anonymous despite consistency.
