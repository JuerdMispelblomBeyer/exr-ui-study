---
id: T10
title: Visual Information Seeking and Coordinated Views
kind: theory
status: adopted
use_when: [composing a screen, linking views, deciding overview vs detail, multi-panel layout]
sources: [shneiderman1996, baldonado2000, roberts2007, pirolli1999]
---

# Visual Information Seeking and Coordinated Views

**The craft layer under "flow": how many views, what each shows, and how
selection in one propagates to the others.**

## What it is

**Shneiderman's mantra** `[shneiderman1996]`: *overview first, zoom and filter,
then details-on-demand.* Backed by a task-by-data-type taxonomy — seven tasks
across seven data types (1D, 2D, 3D, temporal, multidimensional, tree,
network). The seven tasks, verbatim:

| Task | Definition |
|---|---|
| **Overview** | Gain an overview of the entire collection |
| **Zoom** | Zoom in on items of interest |
| **Filter** | Filter out uninteresting items |
| **Details-on-demand** | Select an item or group and get details when needed |
| **Relate** | View relationships among items |
| **History** | Keep a history of actions to support undo, replay, and progressive refinement |
| **Extract** | Allow extraction of sub-collections and query parameters |

**History** and **extract** are the two almost every product omits, and both
matter disproportionately here — see below.

**Coordinated multiple views** `[baldonado2000, roberts2007]`: showing the same
underlying data in several linked representations. **Brushing** is selecting in
one view; **linking** is that selection highlighting in the others. The core
design tension: each additional view costs the user effort to maintain their
mental map across views. Baldonado et al.'s rule of thumb is to use multiple
views only when there is a genuine diversity of attributes or a real need for
comparison — not by default.

**Focus+context** keeps the detail and its surroundings in one view rather than
splitting them, avoiding the context-switch cost entirely.

## Why it matters here

Your platform data spans at least three of Shneiderman's data types at once —
**network** (the platform topology, ROS 2 graph, CAN bus), **temporal** (logs,
traces, telemetry, event sequences), and **multidimensional** (per-node
metrics). That combination is exactly what coordinated views exist for, and
exactly what a single bento field of independent tiles handles badly.

The sharpest question this raises about the current design: **your tiles are
composed but are they coordinated?** `docs/DESIGN_GUIDELINES.md` §10 specifies
what a tile contains; `docs/UX_ARCHITECTURE.md` §7 specifies structure. Neither
specifies what happens to *every other tile* when an engineer selects a compute
node in one. If the answer is "nothing," the screen is a set of separate
readouts sharing a background, and each one is a separate foraging patch
(`T07`) with full switching cost.

Making selection propagate — select a node, and the log stream filters, the
topology highlights the dependency path, the timeline marks its events — is
probably the single highest-leverage structural change available to this
design, and it costs nothing in screen space.

Two more, both cheap and both currently absent:

- **History.** Diagnosis is iterative and, per `T06`, often spans people and
  days. A visible trail of what has been looked at and ruled out is the
  residue-handling capability `T07` argues for, and the handover artefact
  `T06` argues for. Same feature, three justifications.
- **Extract.** Engineers will need to get evidence *out* — into a ticket, a
  message, a report. If the tool cannot hand over a citable fragment, they will
  screenshot it, and the provenance (`T05`) is lost at exactly the moment it
  matters most.

## How to use it

- **Declare the coordination contract** for each screen: what is brushable,
  what links to what, what persists across navigation. Write it into
  `4-design/` as an explicit contract, not an implied behaviour.
- **Justify every view.** If two panels show the same attributes at the same
  granularity, merge them. Each view must earn its context-switching cost.
- **Prefer focus+context over overview+detail** where the surroundings matter —
  in a dependency path, the neighbours *are* the diagnosis.
- **Apply the mantra as a checklist, not a sequence.** "Overview first" is not
  a mandate that every session starts at a dashboard; `M04` will likely show
  many investigations start from a specific known object or a search result —
  which `docs/UX_ARCHITECTURE.md` §3 already assumes. Support entry at any
  point, then ensure zoom/filter/details/relate are all reachable from there.

## Caveats

- The mantra is 1996 and was aimed at exploratory visualisation of static
  collections. Expert diagnostic work on live systems often inverts it —
  detail first, context second. Treat it as a coverage checklist for
  capabilities, not a prescription for flow.
- More coordination is not automatically better. Unpredictable propagation
  ("why did that panel change?") breaks the rule-based consistency `T03`
  requires. Coordination must be legible and stable.

## Sources

`[shneiderman1996]` **read in the original**; `[baldonado2000]` and
`[roberts2007]` from secondary summaries. See `SOURCES.md`.
