# 1 · Frameworks

Borrowed knowledge: the methods this project uses and the theory it thinks
with. Grounded in credible academic sources, biased toward TU Delft IDE
practice, and written to be *applied here* rather than summarised.

**Agents:** grep `frameworks.yaml` first, then open exactly one card. Do not
read this lane end to end — it is ~140 KB and no task needs all of it. Budget:
authored cards stay under 8 KB; `SOURCES.md` and `frameworks.yaml` are
registers, meant to be grepped rather than read whole.

**Humans:** the tables below are the map. Every card is one page.

## How a card is built

| Section | What it gives you |
|---|---|
| One-line summary | Whether to keep reading |
| What it is | The method or theory, from the sources |
| **Why it fits this project** | The honest argument, naming the specific gap it closes |
| **How to run it here** | Concrete steps for ExRobotics, not generic procedure |
| What it produces | What lands in the workspace afterwards |
| Traps | The ways it usually fails |

Front-matter carries `status`, `use_when`, `cost`, and `sources`. Cite sources
by key (`[stappers2017]`); `SOURCES.md` holds the bibliography.

`status` means: **adopted** — in use, follow it · **candidate** — plausible,
not committed · **reference** — know it exists · **partial** — needs
verification.

## Methods — things you do

| | Card | Status | Cost | Use when |
|---|---|---|---|---|
| M01 | [Research through Design](methods/M01-research-through-design.md) | adopted | structural | Framing the project; deciding what counts as a result |
| M02 | [Contextmapping](methods/M02-contextmapping.md) | candidate | 2–4 wk | Reaching tacit needs; how diagnosis *feels* |
| M03 | [Contextual Inquiry](methods/M03-contextual-inquiry.md) | candidate | 1–2 wk | Seeing real practice and the real tool ecology |
| M04 | [Critical Decision Method](methods/M04-critical-decision-method.md) | **adopted** | 1 wk | Eliciting expert diagnostic reasoning ← **start here** |
| M05 | [Reflexive Thematic Analysis](methods/M05-reflexive-thematic-analysis.md) | adopted | ≈ collection | Turning transcripts into defensible claims |
| M06 | [Prototyping Strategy](methods/M06-prototyping-strategy.md) | adopted | none | Before building anything |
| M07 | [Annotated Portfolio](methods/M07-annotated-portfolio.md) | adopted | 30 min/iter | Making in-between versions into knowledge |
| M08 | [Interaction Vision](methods/M08-interaction-vision.md) | candidate | 1 day | Setting a quality target; settling style arguments |
| M09 | [Frame Creation](methods/M09-frame-creation.md) | reference | low | When the problem as stated isn't yielding |
| M10 | [Scenario Evaluation](methods/M10-scenario-evaluation.md) | adopted | 3–5 sessions | Testing any prototype |
| M11 | [Work Domain Analysis](methods/M11-work-domain-analysis.md) | **adopted** | 1–2 wk | Building the structure the interface must represent |

## Theory — things you think with

| | Card | Status | Use when |
|---|---|---|---|
| T01 | [Ecological Interface Design](theory/T01-ecological-interface-design.md) | **adopted** | Any diagnostic view; what to show at which level |
| T02 | [Situation Awareness](theory/T02-situation-awareness.md) | adopted | Information hierarchy; overview screens; eval probes |
| T03 | [Skill–Rule–Knowledge](theory/T03-skill-rule-knowledge.md) | adopted | Expertise range; consistency; safety-state presentation |
| T04 | [Intermediate-Level Knowledge](theory/T04-intermediate-level-knowledge.md) | adopted | Deciding what to write down; what the deliverable is |
| T05 | [Trust and Transparency](theory/T05-trust-and-transparency.md) | adopted | Computed state, uncertainty, stale and unknown values |
| T06 | [Distributed Cognition](theory/T06-distributed-cognition.md) | candidate | Handover; what the tool should remember |
| T07 | [Foraging and Sensemaking](theory/T07-foraging-and-sensemaking.md) | **adopted** | Flow, navigation, scent, why it feels slow |
| T08 | [Mental Models](theory/T08-mental-models.md) | adopted | What "full picture" actually means; runnability |
| T09 | [Attention and Alarms](theory/T09-attention-and-alarms.md) | candidate | What deserves attention; alerting; flooding |
| T10 | [Visual Information Seeking](theory/T10-visual-information-seeking.md) | adopted | Screen composition; linked views; history; extract |

## Domain

| | Card | Status | Use when |
|---|---|---|---|
| D01 | [ExRobotics Operating Context](domain/D01-exrobotics-context.md) | partial | Grounding decisions; writing scenarios; recruiting |
| D02 | [Observability Practice](domain/D02-observability-practice.md) | **adopted** | What already exists; prior art; what data can exist |

## The five cards that matter most

If you read nothing else:

- **`M04` Critical Decision Method** — the highest-yield research method
  available for a diagnostic product, and cheap. Four interviews would replace
  most of the guesswork currently propping up
  `docs/UI_FUNCTIONAL_REQUIREMENTS.md`.
- **`T01` Ecological Interface Design** — the native theory for this exact kind
  of interface. It predicts a specific current weakness: the platform model in
  `data/platform-system.yaml` is almost entirely physical-function level, so
  *"is this platform fit to deploy"* has nothing to render. It also supplies the
  **procedural trap** — the Three Mile Island failure, where a proxy cue that
  was right in normal operation inverted under saturation and operators acted
  on it. That is the sharpest concrete warning in this knowledge base about how
  to treat every rolled-up health indicator in this product.
- **`M07` Annotated Portfolio** — how your in-between versions stop being a
  folder and start being knowledge. It is the method that answers the
  extensibility question design projects usually fail.
- **`T07` Foraging and Sensemaking** — the theory of "flow." Diagnosis is
  foraging between patches under an imperfect perception of value called
  *information scent*. It reframes navigation design as cost reduction and
  names the design surface — scent on the link — that the current component set
  mostly lacks.
- **`D02` Observability Practice** — what already exists. Foxglove, Rerun,
  PlotJuggler, rqt, `diagnostic_msgs`. Study these before designing or you will
  rebuild them.

## What this lane deliberately does not contain

Empirical findings. Nothing here is evidence about ExRobotics engineers — it is
borrowed knowledge about how to *get* that evidence and how to think about it.
Findings belong in `2-research/` and `3-insights/`.

## Forward references

Source verification is recorded honestly in `SOURCES.md`. Three of the five
load-bearing papers have been read in the original; the rest are summaries and
are marked as such, with a list of what still needs obtaining.

Cards point at lanes from the workspace plan that are not built yet:
`0-meta/CONVENTIONS.md`, `0-meta/GLOSSARY.md`, `2-research/`, `3-insights/`,
`5-prototypes/`, `6-log/`. `0-meta/ETHICS.md` **does** exist — it had to,
because several cards send you there before recording anyone.

References to `docs/`, `data/`, and `tokens/` are live and correct today; they
will need updating when those move in the migration.

## Adding a card

Only when it will change what you actually do. A card that is a literature
summary with no "how to run it here" section is shelf-ware — delete it rather
than let the lane become a reading list. Copy the shape of an existing card,
add the source to `SOURCES.md`, add the row to `frameworks.yaml` and to the
table above.
