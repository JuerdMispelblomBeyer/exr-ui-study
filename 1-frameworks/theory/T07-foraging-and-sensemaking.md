---
id: T07
title: Information Foraging and Sensemaking
kind: theory
status: adopted
use_when: [designing flow, navigation, search, what to put next to what, why an interface feels slow]
sources: [pirolli1999, russell1993, klein2007df, attfield2009]
---

# Information Foraging and Sensemaking

**This is the theory of "flow." Diagnosis is a forager moving between patches
of information, following scent, trying to build a frame that the data fits.
Every navigation decision the interface imposes is a cost in that loop.**

## What it is

Three connected models. Together they explain why a diagnostic tool feels fast
or slow in a way that "good UX" does not.

### 1. Foraging — Pirolli & Card `[pirolli1999]`

Borrowed from optimal foraging theory in ecology. An analyst moves through a
**patchy** information environment and faces one recurring decision: keep
working this patch, or pay the cost of moving to another?

| Concept | Meaning | In this product |
|---|---|---|
| **Patch** | A locality of related information | The ROS 2 graph view, a log stream, a CAN trace, one node's metrics |
| **Between-patch cost** | Time to get to the next patch | Switching views, re-entering context, opening another tool |
| **Within-patch depletion** | Returns diminish as you exhaust a patch | The tenth log line tells you less than the first |
| **Information scent** | *Imperfect* perception of a source's value, cost, and access path, read from **proximal cues** | A badge, a label, a count, a colour, a link — whatever the engineer uses to guess "is the answer through there?" |
| **Enrichment** | Changing the environment to make foraging cheaper | Filtering, saved queries, pinning, pre-correlated views |

The operative insight: **people leave a patch when perceived remaining value
drops below the perceived cost of switching.** They act on *perception*, not
truth. So a view that contains the answer but advertises it badly gets
abandoned — and the engineer will report that "the information wasn't there."

### 2. The cost structure of sensemaking — Russell et al. `[russell1993]`

Sensemaking is searching for a **representation** and encoding data into it.
Three loops:

- **Generation loop** — find a candidate representation ("it's a network
  problem," "it's a startup-ordering problem").
- **Data coverage loop** — try to encode the observations into it.
- **Residue** — the observations that will not fit.
- **Representation shift loop** — residue forces you to change the
  representation and start again.

**Residue is the expensive part.** Most diagnostic effort goes into handling
data that does not fit the current story.

### 3. Data–frame theory — Klein `[klein2007df]`

Sensemaking is "fitting data into a frame and fitting a frame around the data."
A **frame** — a story, a map, a causal diagram — defines *what counts as data*
in the first place. Data and frame co-evolve: the frame directs what you look
for, and surprising data forces you to reframe.

Note this is `M09` (Dorst's framing) operating at the timescale of a single
diagnosis rather than a whole project. Same mechanism.

## Why it matters here

**This is the missing theory behind your actual question.** "Real good flow" is
not a navigation-design problem; it is a foraging-cost problem. The current
docs specify structure (`docs/UX_ARCHITECTURE.md` §7 IA, §8 primary flow) but
nowhere reason about the cost of moving between information and the cues that
make an engineer move at all.

Three consequences that bite immediately:

**Scent is a design surface, and it is currently unspecified.** Every
navigation affordance — a rail item, a lens chip, a collapsed evidence strip —
is a proximal cue an engineer uses to predict what lies behind it. A label
reading "Logs" carries almost no scent. "Logs · 3 errors since last boot"
carries a lot. The strongest available design lever on flow is putting *a
preview of the value behind the link, on the link*. This is cheap and your
current component set mostly does not do it.

**Between-patch cost is what you are actually reducing.** `M03` will very
likely show engineers holding several tools open at once — that is high
between-patch cost, paid repeatedly. The value case for this product is
collapsing that. But note the trap: a single interface with heavy internal
navigation just moves the cost inside your own product.

**Design for residue, not just for the happy path.** The representation-shift
loop is where diagnosis actually gets hard: the engineer's story stops fitting.
An interface that only supports confirming the current hypothesis accelerates
confirmation bias. Supporting *disconfirmation* — what does not fit, what was
ruled out, what is anomalous relative to the current frame — is the
higher-value and rarer capability. This also connects to `T06`: "what has been
ruled out" is exactly the residue, and it is what gets lost at handover.

## How to use it

- **Score your navigation for scent.** Take every link, tab, and chip in a
  prototype and ask: what does this cue let an engineer predict about what is
  behind it? If the answer is "only the category name," it has no scent.
- **Count patch switches per scenario.** Run an `M10` evaluation and literally
  count view changes to reach a diagnosis. It is a blunt but honest flow metric
  and it is comparable across iterations (`M07`).
- **Watch for abandonment.** In `M04` and `M10`, the moment a participant gives
  up on a view is a scent failure. Ask what they expected to find and why they
  concluded it was not there.
- **Add enrichment deliberately.** Saved filters, pinned objects, and
  pre-correlated views are enrichment activities — they pay off repeatedly in
  a domain where engineers debug the same subsystems again and again.
- **Make the frame explicit and revisable.** If the interface lets an engineer
  state a working hypothesis and shows evidence for *and against* it, you are
  supporting the data–frame loop rather than fighting it.

## Caveats

- Foraging theory is descriptive and its quantitative models were built for
  document collections and the web, not diagnostic tooling. Use the concepts —
  patch, scent, cost, residue — as design lenses; do not attempt the equations.
- "Reduce clicks" is not the lesson. A cheap switch to a high-value patch is
  fine. The cost that matters is *re-establishing context*, not the click.

## Sources

`[pirolli1999]` for foraging and scent; `[russell1993]` for cost structure;
`[klein2007df]` for data–frame. `[attfield2009]` combines the last two into
system-requirements reasoning. See `SOURCES.md`.
