---
id: M03
title: Contextual Inquiry
kind: method
status: candidate
use_when: [seeing actual diagnostic practice, discovering real tool ecology, checking what people do vs say]
cost: medium — 1–2 weeks for 4–6 sessions plus interpretation
sources: [beyer1997, holtzblatt2016]
---

# Contextual Inquiry

**Watch the work happen where it happens, and ask about it while it happens.**

## What it is

Field interviewing built on four principles `[beyer1997]`:

- **Context** — go where the work is, not to a meeting room.
- **Partnership** — the **master/apprentice** model. They work; you watch and
  ask. You are the apprentice. This deliberately inverts the usual interview
  power dynamic and licenses you to ask naive questions.
- **Interpretation** — you check your reading aloud, in the moment: *"so you
  opened the log first because you didn't trust the health flag?"* They correct
  you. The correction is the data.
- **Focus** — you hold a declared perspective so the session stays useful,
  while staying alert to what surprises you.

Afterwards: an **interpretation session** where the team walks the notes
together and captures issues, then an **affinity diagram** clustering those
notes bottom-up across participants into a hierarchy of themes.

## Why it fits this project

`docs/UX_ARCHITECTURE.md` §3 assumes a 1440 px workstation, one active
platform, and that "most investigations begin from an abnormal state, a search
result, or a known object." Every one of those is directly observable and none
has been observed. An afternoon beside an engineer settles several assumptions
that currently prop up the whole information architecture.

It is also the only method here that reveals **tool ecology** — the terminal
windows, Grafana tabs, Slack threads, ROS CLI invocations, and spreadsheets
that the designed interface will either replace or have to live beside. That
context is entirely absent from the current docs and is likely to be the single
biggest constraint on the design.

## How to run it here

- **4–6 sessions, 90–120 min**, at a bench with a real platform or during real
  remote investigation.
- **Open with the contract:** "I'm going to watch you work and interrupt with
  dumb questions. Correct me whenever I'm wrong."
- **Trigger on real work.** If nothing is broken, ask them to walk a recent
  fault while re-opening the actual tools they used. Retrospective-with-tools
  beats hypothetical.
- **Record** (consent per `0-meta/ETHICS.md`); capture screen where permitted.
- **Note-take on observable specifics**: what they opened, in what order, what
  they typed, where they paused, what they said aloud, what they gave up on.
- **Interpretation session within 48h** while memory is warm. Affinity in
  `3-insights/`.

## What it produces

- The real diagnostic sequence, including the messy parts.
- The tool ecology and the handoffs between tools.
- Breakdowns: the moments where the current setup fails them.
- Vocabulary — the words engineers actually use, which should govern
  `0-meta/GLOSSARY.md` and all interface copy.

## Traps

- **Drifting into a normal interview.** If you're both sitting still and
  talking, you've lost the method. Get them back into the work.
- **Interviewing about the future.** CI is for what happens now. Save
  aspiration for `M02` or `M08`.
- **Silent observation.** Pure watching without in-the-moment interpretation
  yields description without reasoning. The reasoning is the point.
- **One heroic expert.** Sample across experience levels; novices reveal what
  the interface fails to teach.

## Relationship to other methods

CI gives you **what happens**. `M04` gives you **why the hard call was made**.
`M02` gives you **what it feels like and what they wish for**. Running CI first
is usually right — it grounds everything else in observed reality.

## Sources

`[beyer1997]` for the principles and the affinity process; `[holtzblatt2016]`
for the modern revision. See `SOURCES.md`.
