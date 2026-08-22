# Research agenda

**What to study, what to find out, and in what order — for an interface with
good flow that gives engineers a full picture of the machine's internal state.**

Framework cards are in `1-frameworks/`. This file says which to use when, and
what is still unknown. It becomes `questions.yaml` when this lane is built out.

## 0. The two goals, stated precisely

Both goals are real, and both are vaguer than they look. Sharpening them is the
first piece of work, because each has two readings that lead to different
designs.

### "Real good flow"

Not a navigation-layout problem. In `T07` terms it is a **foraging cost**
problem: diagnosis moves between patches of information under an imperfect
perception of value called **information scent**, and people abandon a patch
when perceived remaining value drops below perceived switching cost. They act
on the perception, not the truth — so a view that holds the answer but
advertises it badly gets abandoned, and gets reported as "the information
wasn't there."

> **Sharpened:** minimise the cost of moving between evidence, put scent on
> every navigation cue, and support **representation shift** — the moment the
> engineer's current story stops fitting the data.

Measurable in `M10`: patch switches per diagnosis · abandonment moments · time
to first correct hypothesis · whether disconfirming evidence was ever found.

### "Full picture of internal state"

Two readings, and the difference matters more than anything else on this page:

| Reading | Where it leads |
|---|---|
| *Show all the state* | Exhaustive readouts. Maximises SA Level 1, degrades comprehension (`T02`), produces the flat metric dashboard `docs/DESIGN_GUIDELINES.md` §18 already forbids |
| *Support a runnable mental model* (`T08`) | Expose structure, causality and constraint so an engineer can **simulate and explain**. Fewer values, better arranged |

> **Sharpened:** the target is a runnable model — the engineer can predict what
> breaks if a node dies, and explain why the platform is in the state it is in.
> When space runs out, **relationships beat readings**.

Measurable in `M10`: prediction questions, not recognition questions.

## 1. Study — desk work, no dependencies, start now

| # | What | Card | Why it is on the list |
|---|---|---|---|
| **S1** | **Hands-on with the existing tools**: Foxglove, Rerun, PlotJuggler, `rqt_graph`, `ros2 doctor`, `diagnostic_msgs` — with real ExRobotics data if you can get it | `D02` | **Highest priority.** These are prior art and some are what your engineers use today. Your product's territory is where they stop helping; you cannot find that boundary from a description |
| **S2** | **Observability as a discipline**: three pillars, the wide-events critique, monitoring vs observability, distributed tracing, the microservice failure-diagnosis survey | `D02` | Gives you the vocabulary and the known/unknown-unknown distinction, which maps directly onto `T01`'s rule- vs knowledge-based split |
| **S3** | **Foraging and sensemaking**: Pirolli & Card, Russell et al., Klein's data–frame theory | `T07` | The theory of flow. Read before any navigation work |
| **S4** | **CWA in practice**: Lintern's tutorial first (short), then the INL methodology report | `M11` | You need the procedure, not just the concept. `T01` says build an abstraction hierarchy; this is how |
| **S5** | **EID primary sources**: Vicente & Rasmussen 1992, then Vicente 2002 | `T01` | Closest native theory for this product. The 1992 paper is already read and summarised in the card |
| **S6** | **Obtain the paywalled priority sources** — Hoffman et al. 1998 above all | `SOURCES.md` | `M04` is the method you would run first and it currently rests on a stand-in |

Roughly two weeks. **S1 and S2 are the ones that change what you design**; the
rest change how well you justify it.

## 2. Analyse — desk work on material you already have

| # | What | Card | Output |
|---|---|---|---|
| **A1** | **Build a first-pass abstraction–decomposition space** for the platform | `M11` §1 | The missing abstract-function layer: power, thermal, data flow, freshness, information integrity. Directly amends `data/platform-system.yaml` |
| **A2** | **Build the contextual activity matrix** — work situations × tasks | `M11` §2 | May be the highest-value cheap analysis available. See §4 below |
| **A3** | **Procedural-trap audit** of every derived indicator in the current design | `T01` | For each rolled-up health state or proxy cue: under what conditions does it stop meaning what an engineer will read it as? |
| **A4** | **Scent audit** of the current navigation | `T07` | Every rail item, lens chip, tab: what does this cue let someone predict about what is behind it? Most will score near zero |
| **A5** | **Coordination audit** | `T10` | For each screen: when an engineer selects a compute node, what changes elsewhere? If nothing, the tiles are separate patches sharing a background |

A1 and A2 are about one week together. A3–A5 are half-day audits each and will
each produce concrete design changes.

## 3. Find out — empirical, needs ExRobotics access

Ordered by value per hour.

| # | Question set | Method | Notes |
|---|---|---|---|
| **F1** | **Tool ecology and data reality.** What is used today, for what, what is bad about it. What data exists, what is retained on-robot, what reaches the ground, at what fidelity, for how long | `M03` + `D02` | Do this first. It bounds every subsequent design decision, and half of it is answerable by an engineer in an hour |
| **F2** | **Expert diagnostic reasoning.** Four to six real hard incidents, walked through the participant's own material | `M04` | Produces the cue inventory, decision timelines, and decision requirement tables. The "why was this difficult" column is where requirements come from |
| **F3** | **Mental models.** Have engineers draw the platform before seeing anything you have made | `T08` | Divergence from `data/platform-system.yaml` is a finding about the IA. Their carving may not be yours |
| **F4** | **Situated experience and latent needs** | `M02` | Higher cost. Run only if F1–F3 leave the *why it feels bad* question open |
| **F5** | **Evaluation cycles** | `M10` | Begins once there is a prototype worth confronting. Every iteration from then on |

## 4. Critical unknowns

These could invalidate design decisions already made. Each is cheap to ask and
expensive to discover late.

| ID | Question | Why it is critical | Where |
|---|---|---|---|
| **Q1** | Is end-to-end causality across the ROS 2 graph, containers and CAN reconstructible with what is instrumented today? | If not, the dependency-path view — central to D014 and D020 — cannot be fed. This is a data-model question that precedes any UI | `D02`, F1 |
| **Q2** | What data actually survives from robot to ground? Volume, fidelity, latency, retention | Per `D01` the platform is autonomous, so retrospective diagnosis dominates. If evidence is thin or lossy, the whole product shifts | `D02`, F1 |
| **Q3** | Is diagnosis a single session, or a relay across people and days? | `docs/UX_ARCHITECTURE.md` §3 assumes one engineer at one workstation. If it is a relay, the primary need is transferring established understanding, not live inspection — a materially different product | `T06`, F1 |
| **Q4** | How many genuinely distinct work situations are there? | If pre-deployment check, returned-from-site, and active fault investigation have different task sets, then "one good flow" is the wrong target and the interface must fit each | `M11` §2, A2 |
| **Q5** | Does ExRobotics already use `diagnostic_msgs` or another structured health model? | An existing health convention is either a foundation to build on or a competing model to reconcile with | `D02`, F1 |
| **Q6** | Where exactly is the boundary with the Energy Robotics partner stack, and what does it already expose? | Defines this product's scope from the outside. `AGENTS.md` draws the boundary conceptually; nobody has checked it against the real system | `D01`, F1 |
| **Q7** | Does any safety classification apply to platform-state displays? | `docs/SAFETY_CONTROLS.md` §3 flags this as unresolved and **blocking**. It is a question for ExRobotics' safety engineers, not a design decision | `T09`, F1 |

Q1, Q2 and Q7 are the ones that would hurt most if answered late.

## 5. Suggested sequence

```
Week 1–2    S1 S2      hands-on with existing tools; observability concepts
            F1         tool ecology + data reality  ← overlaps deliberately
            Q1 Q2 Q5   Q6 Q7 asked in the same conversations

Week 2–3    S3 S4      foraging/sensemaking; CWA procedure
            A1 A2      abstraction–decomposition space; work situations → Q4

Week 3–4    F2         CDM interviews on real incidents
            F3         mental-model drawings, appended to the same sessions

Week 4–5    A3 A4 A5   audits, now informed by fieldwork
                       → concrete design changes

Week 5+     M06 → M10 → M07     iterate: build, confront, annotate, tag
```

The overlap in weeks 1–2 is intentional. S1 makes you competent enough to ask
F1 well, and F1 is what makes S1 concrete. Do not serialise them.

## 6. What this does not cover

Visual identity and Figma craft. That work is already well developed in `docs/`
and is not the constraint right now — the constraint is that the design rests
on assumptions nobody has checked. Nothing above requires pausing design work;
`M01` is explicit that designing *is* the instrument of inquiry.
