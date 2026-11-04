# Treatment timeline — connected temporal path

## Reference identity and evidence quality

- Source: `reference/ref-004__light-health-dashboard__treatment-timeline-crop.jpg`.
- Type: close crop of a light healthcare workflow.
- Evidence: high for temporal composition and attached detail; medium for controls; low for overall application shell and motion.

## Executive design reading

A long curved timeline makes time the organizing object. A bright current-date
marker and attached metric cards transform a sequence of events into a readable
path rather than a list of timestamped rows.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | soft clinical editorial | Warm light field, delicate path | TT-AES-01 | Calm and approachable |
| Personality | reassuring, guided | Rounded filters and current-date marker | TT-AES-01 | Continuity over urgency |
| Density | medium | Metrics above, path and cards below | TT-DEN-01 | Detail follows temporal position |
| Whitespace | generous but structured | Air around the long path | TT-DEN-01 | Time remains legible |
| Grid | horizontal temporal spine | Events align to one curve | TT-COMP-01 | Sequence organizes modules |
| Typography | clean sans + strong values | Dates, labels, readings | TT-TYPE-01 | Values and time read quickly |
| Color | warm neutral + yellow current | Current date highlighted | TT-COLOR-01 | Accent marks “now” |
| Geometry | pills, cards, continuous curve | Soft connected forms | TT-GEO-01 | Relationship through continuity |
| Surfaces | pale layered planes | Selected date floats above path | TT-GEO-01 | Elevation marks current context |
| Imagery | no decorative image | Timeline is the main visual | TT-IMG-01 | Process becomes imagery |
| Hierarchy | current moment first | Yellow date → attached readings | TT-HIER-01 | “Now” anchors history |
| Composition | lateral narrative | Past/future distributed along path | TT-COMP-01 | Supports change over time |
| Distinctiveness | medium-high | Curved spine and floating current marker | TT-DIST-01 | Temporal grammar is recognizable |

## Dimension analysis

### TT-AES-01 — Aesthetic and personality

**OBSERVATION** — A warm pale field, rounded controls, and a delicate connected
path create a calm clinical atmosphere.

**INTERPRETATION** — The softness lowers anxiety, though it may understate
engineering urgency.

**TRANSFERABLE PRINCIPLE** — Use continuity and clear current-state markers to
make system history approachable, while retaining sharper ExR technical edges.

### TT-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Events, labels, and detail surfaces align to a long horizontal
spine rather than independent columns.

**INTERPRETATION** — The relationship between moments is the composition.

**TRANSFERABLE PRINCIPLE** — Organize incidents, container restarts, CAN-rate
changes, and safety events around a shared temporal path.

### TT-DEN-01 — Density and whitespace

**OBSERVATION** — The timeline is spacious, while readings cluster near the
selected date.

**INTERPRETATION** — Detail appears where attention is focused, preventing every
moment from carrying equal weight.

**TRANSFERABLE PRINCIPLE** — Show a compressed history by default and expand
evidence only around the current probe or selected event.

### TT-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Dates and numeric readings are stronger than descriptive copy;
labels remain compact.

**INTERPRETATION** — The hierarchy supports quick orientation in time and value.

**TRANSFERABLE PRINCIPLE** — Use mono for timestamps/values and a quiet sans for
event descriptions; visually promote the selected moment.

### TT-COLOR-01 — Color and contrast

**OBSERVATION** — Yellow singles out the current date while neutrals define the
rest of the sequence.

**INTERPRETATION** — Accent color means “current focus,” a strong fit for ExR.

**TRANSFERABLE PRINCIPLE** — Assign ExR yellow to now/current/probed, never to
historical decoration or warning severity.

### TT-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — A continuous curve connects events; the selected date floats
as a rounded marker; metric cards attach below.

**INTERPRETATION** — Geometry shows sequence and attachment, but excess pills
soften precision.

**TRANSFERABLE PRINCIPLE** — Use a fine signal path with an explicit current
probe and attached evidence lens, rendered in ExR’s sharper geometry.

### TT-IMG-01 — Imagery and iconography

**OBSERVATION** — No stock image appears; the temporal model itself is the main
visual object.

**INTERPRETATION** — Process structure can supply visual richness.

**TRANSFERABLE PRINCIPLE** — Turn system history, fault propagation, and restart
sequences into navigable diagrams instead of decorative charts.

### TT-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — Filters, date markers, and attached cards imply selecting a
time point; no animation is evidenced.

**INTERPRETATION** — The likely flow is choose period → probe event → inspect
readings.

**TRANSFERABLE PRINCIPLE** — Keep the time probe synchronized across logs,
metrics, and topology without assuming animated travel along the path.

### TT-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — The floating yellow date on a curved horizontal narrative is
the recognizable move.

**INTERPRETATION** — It provides a useful “current lens” grammar but is bound to
a soft healthcare aesthetic in its present form.

**TRANSFERABLE PRINCIPLE** — Rebuild the current-lens concept with technical
ticks, exact timestamps, and system-state semantics.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Temporal spine | Makes sequence spatial | Shared platform event history | Treatment journey content |
| Floating current marker | Establishes “now” instantly | Yellow time probe | Exact pill/date shape |
| Attached readings | Relates evidence to a moment | Logs/metrics at selected timestamp | Healthcare cards |
| Detail around focus | Controls density | Expand selected event only | Excess empty timeline |
| Soft path continuity | Reduces list fragmentation | Signal/event continuity | Organic clinical styling |

## Translation decisions

- **Borrow:** timeline as primary object, current probe, attached evidence,
  focus-dependent detail, synchronized time context.
- **Ignore:** patient metrics, treatment vocabulary, exact curved path.
- **Brand-specific:** clinical softness and source palette.
- **Accidental:** crop hides navigation and actual transition behavior.
- **Anti-patterns/limitations:** excess whitespace; pills and rounded cards feel
  consumer-oriented; a continuous path can imply causality where only chronology
  exists; exact timestamps and zoom controls are required for engineering use.
