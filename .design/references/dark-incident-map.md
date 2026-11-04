# Dark incident map — localized critical event

## Reference identity and evidence quality

- Source: `reference/ca82a1f762bc89f3f6fbb4775da24655.jpg`.
- Type: direct map-based incident monitoring concept.
- Evidence: high for hierarchy and event localization; medium for data semantics; low for interaction and motion.

## Executive design reading

The screen makes one incident impossible to miss by placing a hot red/orange
halo inside an otherwise near-monochrome network map. A compact narrative sits
at the lower edge, leaving spatial causality visible.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | geospatial, forensic | Black map and fine white network lines | IM-AES-01 | Feels investigative |
| Personality | urgent but controlled | One intense incident, quiet surroundings | IM-AES-01 | Urgency is localized |
| Density | medium | Detailed network with little chrome | IM-DEN-01 | Map carries complexity |
| Whitespace | spatial negative field | Dark regions separate network traces | IM-DEN-01 | Context stays visible |
| Grid | map-first, edge annotation | Full canvas with lower-left narrative | IM-COMP-01 | Evidence overlays the model |
| Typography | compact incident caption | Small white/orange labels | IM-TYPE-01 | Text explains, not dominates |
| Color | neutral network + hot event | Red/orange halo | IM-COLOR-01 | Semantic heat has authority |
| Geometry | organic network, radial incident | Fine paths and one circular bloom | IM-GEO-01 | Shape communicates spread |
| Surfaces | continuous field | Minimal cards or dividers | IM-GEO-01 | Relationships remain unbroken |
| Imagery | cartographic data | Map is the interface | IM-IMG-01 | System diagram can be the workspace |
| Hierarchy | extreme event focus | Halo first, narrative second | IM-HIER-01 | Fault location is immediate |
| Composition | ambient context around focal anomaly | Incident off-center | IM-COMP-01 | Asymmetry increases tension |
| Distinctiveness | high | Fine network and hot bloom | IM-DIST-01 | Signature is semantic contrast |

## Dimension analysis

### IM-AES-01 — Aesthetic and personality

**OBSERVATION** — Thin white routes cover a black field while one red/orange
incident glows intensely.

**INTERPRETATION** — The scene feels urgent without making every element loud.

**TRANSFERABLE PRINCIPLE** — Keep healthy infrastructure visually quiet so the
abnormal subsystem can dominate instantly.

### IM-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — The map fills the viewport; the alert narrative is anchored
to a corner and visually linked to the incident region.

**INTERPRETATION** — Context and explanation share one continuous space.

**TRANSFERABLE PRINCIPLE** — Overlay concise diagnosis near the selected fault
instead of replacing the topology with a separate alert page.

### IM-DEN-01 — Density and whitespace

**OBSERVATION** — Network lines are dense locally, but large dark regions give
the field air.

**INTERPRETATION** — Negative space is produced by system structure rather than
by oversized padding.

**TRANSFERABLE PRINCIPLE** — Let topology determine spatial density and avoid
packing every open region with secondary metrics.

### IM-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Type is small, high contrast, and confined to incident
identity and context.

**INTERPRETATION** — The visual model answers where; text answers what and why.

**TRANSFERABLE PRINCIPLE** — Pair a visual fault marker with a concise diagnosis,
timestamp, consequence, and recommended next action.

### IM-COLOR-01 — Color and contrast

**OBSERVATION** — A hot red/orange range is isolated against white and black.

**INTERPRETATION** — Extreme scarcity grants semantic color enormous authority,
though glow may blur exact boundaries.

**TRANSFERABLE PRINCIPLE** — Reserve danger color for unsafe/fault state and keep
ExR yellow for selected/current/action so the meanings never collide.

### IM-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — The system is drawn as fine paths; the incident is radial and
soft-edged; no card grid interrupts the field.

**INTERPRETATION** — Geometry directly encodes connectivity and event spread.

**TRANSFERABLE PRINCIPLE** — Use lines for connections, bounded nodes for
components, and halos only for propagation or uncertainty.

### IM-IMG-01 — Imagery and iconography

**OBSERVATION** — Cartographic lines and the incident bloom replace traditional
illustration and charts.

**INTERPRETATION** — The model is both navigation and evidence.

**TRANSFERABLE PRINCIPLE** — Make the robot’s compute/LAN/CAN/power topology the
primary navigable image.

### IM-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — The incident marker implies selection and the route network
implies propagation; no actual interaction or animation is shown.

**INTERPRETATION** — The likely task is detect → locate → read consequence →
inspect path.

**TRANSFERABLE PRINCIPLE** — Preserve this sequence in fault states, but do not
add pulsing animation unless it communicates fresh or escalating state.

### IM-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — Almost all visual energy is allocated to one event within a
fine continuous network.

**INTERPRETATION** — The reference is memorable because hierarchy is decisive,
not because it contains many styled components.

**TRANSFERABLE PRINCIPLE** — Design the normal interface to become quiet around
a real fault, allowing the fault’s location and consequence to take over.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Singular hot anomaly | Guarantees instant detection | One dominant faulty subsystem | Exact halo treatment |
| Continuous network field | Preserves causal context | Onboard LAN/CAN/power paths | Geographic map |
| Edge-anchored diagnosis | Explains without covering the model | Attached fault narrative | Exact caption styling |
| Off-center focal tension | Feels active, not templated | Let selected node determine composition | Arbitrary asymmetry |
| Quiet healthy state | Protects semantic contrast | Neutral healthy nodes and paths | Low contrast that hides them |

## Translation decisions

- **Borrow:** localized urgency, continuous topology, attached diagnosis,
  semantic scarcity, visual causal path.
- **Ignore:** geography, road-network styling, and exact incident content.
- **Brand-specific:** red/orange bloom and cartographic linework.
- **Accidental:** unknown temporal behavior and cropped controls.
- **Anti-patterns/limitations:** glow obscures precision; red/orange alone is not
  accessible; a map-first view fails if the system diagram is not truthful;
  context text may be too small during incidents.
