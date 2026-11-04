# Network monitor — light regional overview

## Reference identity and evidence quality

- Source: `reference/ref-025__light-network-monitoring__regional-status-map.webp`.
- Type: direct light network dashboard screenshot.
- Evidence: high for task grouping and chart/map combination; medium for interaction; low for visual distinction and small-text accessibility.

## Executive design reading

This is a clear conventional network overview: sidebar, three summary readings,
regional status, map heat overlay, and a large throughput trend. It is useful for
workflow completeness and evidence ordering, but visually generic and too
dependent on low-contrast small labels.

## Visual DNA

| Field | Value | Visible evidence | Supporting IDs | Design implication |
|---|---|---|---|---|
| Aesthetic | light network SaaS | White shell, blue plots, sidebar | NM-AES-01 | Accessible familiarity |
| Personality | neutral, managerial | Clean cards and pale dividers | NM-AES-01 | Safe and restrained |
| Density | medium | KPIs, regions, map, throughput | NM-DEN-01 | Broad overview |
| Whitespace | moderate-high | Generous card padding | NM-DEN-01 | Some capacity wasted |
| Grid | regular dashboard | Sidebar + card rows | NM-COMP-01 | Predictable |
| Typography | compact neutral sans | Small grey labels and values | NM-TYPE-01 | Clear roles, weak contrast |
| Color | white/grey + blue status | Blue lines/heat, small states | NM-COLOR-01 | Calm but generic |
| Geometry | rounded cards | Repeated containers | NM-GEO-01 | Familiar SaaS language |
| Surfaces | elevated light cards | Borders/shadows separate modules | NM-GEO-01 | Overview is fragmented |
| Imagery | regional map and line chart | Data visuals lead | NM-IMG-01 | Location and time coexist |
| Hierarchy | summary → region/map → trend | Conventional top-down flow | NM-HIER-01 | Easy to learn |
| Composition | broad modular bands | Similar card weights | NM-COMP-01 | Weak focal hierarchy |
| Distinctiveness | low | Standard network dashboard | NM-DIST-01 | Content does most of the work |

## Dimension analysis

### NM-AES-01 — Aesthetic and personality

**OBSERVATION** — A pale interface uses blue charts, white cards, and a standard
left sidebar.

**INTERPRETATION** — It feels clear and familiar but carries little specific
product character.

**TRANSFERABLE PRINCIPLE** — Use the readability baseline while replacing the
generic shell with ExR’s chassis, topology, and probe language.

### NM-COMP-01 — Composition, grid, and alignment

**OBSERVATION** — Three KPI cards lead, followed by regional/map modules and a
wide throughput chart.

**INTERPRETATION** — Task grouping is sensible, but visual weight follows a
template instead of current network risk.

**TRANSFERABLE PRINCIPLE** — Make the LAN/uplink topology primary, with current
path, failover state, and throughput evidence attached.

### NM-DEN-01 — Density and whitespace

**OBSERVATION** — Modules have ample padding and repeated headings around
moderate data.

**INTERPRETATION** — The screen is comfortable but inefficient for engineers.

**TRANSFERABLE PRINCIPLE** — Consolidate related network readings into one
instrument and use compact rows for secondary interfaces.

### NM-TYPE-01 — Typography and hierarchy

**OBSERVATION** — Labels and axes are small and pale; values are moderately
larger.

**INTERPRETATION** — Hierarchy exists, but low contrast and size reduce scan
confidence.

**TRANSFERABLE PRINCIPLE** — Use accessible contrast, direct labels, and mono for
interface names, IPs, rates, latency, and timestamps.

### NM-COLOR-01 — Color and contrast

**OBSERVATION** — Blue identifies charts and heat zones while grey defines the
shell.

**INTERPRETATION** — Color is coherent but generic and may blur data/category/
selection roles.

**TRANSFERABLE PRINCIPLE** — Use yellow for active route/probe, neutrals for
healthy links, and labeled semantic colors for degradation/failure.

### NM-GEO-01 — Geometry, borders, shadows, and surfaces

**OBSERVATION** — Rounded white cards with subtle shadows contain every evidence
type.

**INTERPRETATION** — Consistent containment fragments related network evidence.

**TRANSFERABLE PRINCIPLE** — Draw links and nodes on a continuous workbench and
place traces/logs in attached or inset regions.

### NM-IMG-01 — Imagery and iconography

**OBSERVATION** — A geographic heat map and throughput line chart are the major
visuals; small icons support summaries.

**INTERPRETATION** — Space and time are represented, but the physical/logical
network path is missing.

**TRANSFERABLE PRINCIPLE** — Use an onboard network schematic before geography;
show Wi-Fi, cellular, Tailscale, and VRRP/keepalived paths truthfully.

### NM-HIER-01 — Information hierarchy, interaction, and motion

**OBSERVATION** — Map regions and time-series points appear selectable; no linked
selection or motion is demonstrated.

**INTERPRETATION** — The likely workflow is summary → region → throughput, not
necessarily the robot engineer’s causal flow.

**TRANSFERABLE PRINCIPLE** — Support locate degraded link → inspect failover,
latency, loss, and route → act, without inventing map animation.

### NM-DIST-01 — Distinctive decisions and limits

**OBSERVATION** — No individual visual move is unique; quality depends on clean
execution.

**INTERPRETATION** — Coherence alone cannot make the interface recognizable.

**TRANSFERABLE PRINCIPLE** — Use this as a usability baseline and deliberately
depart from its card template.

## Signature moves

| Move | Why it works | Transfer | Do not copy |
|---|---|---|---|
| Map plus throughput trend | Joins location and time | Topology plus link history | Geographic heat map |
| Regional status list | Supports fast comparative scanning | Interface/path health rows | World regions |
| Broad main chart | Makes trends legible | Network throughput/loss history | Exact blue area line |
| Familiar sidebar | Low learning cost | Stable compact global rail | Generic SaaS styling |
| Neutral light field | Supports daytime use | Warm calibrated ExR light mode | Low-contrast greys |

## Translation decisions

- **Borrow:** evidence ordering, map/time pairing logic, comparative status,
  readable main trend.
- **Ignore:** regions, KPI row, geographic map, conventional card layout.
- **Brand-specific:** blue palette and source icons.
- **Accidental:** screenshot scale may exaggerate small-text issues.
- **Anti-patterns/limitations:** generic SaaS; low contrast; excess padding and
  cards; weak focus; no causal network topology; color roles are underspecified.
