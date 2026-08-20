---
id: M05
title: Reflexive Thematic Analysis
kind: method
status: adopted
use_when: [analysing interview transcripts, turning session notes into insights, any qualitative dataset]
cost: medium — roughly equal to the time spent collecting the data
sources: [braun2022, braun2021]
---

# Reflexive Thematic Analysis

**Themes are built, not found. Say who built them and how.**

## What it is

Braun & Clarke's six phases `[braun2022]`:

1. **Familiarisation** — read everything, repeatedly, before coding. Note
   impressions but do not systematise yet.
2. **Coding** — label meaningful segments. Codes are frequent, small, and
   revisable. Code the whole dataset, not just the striking bits.
3. **Generating initial themes** — cluster codes into candidate patterns of
   shared meaning.
4. **Reviewing themes** — test each against the coded data and the full
   dataset. Most candidates collapse or split here.
5. **Defining and naming** — write a short definition and a name for each
   theme. If you cannot define it in two sentences, it is not one theme.
6. **Writing up** — the write-up *is* analysis, not a report of it.

The word **reflexive** is the load-bearing part. Braun & Clarke explicitly
reject the language of themes "emerging" `[braun2021]` — themes are analytic
constructions produced by *you*, with your background and your design agenda.
The method's rigour comes from making that positioning explicit, not from
pretending to neutrality.

Four decisions to declare before you start:

| Continuum | Choose |
|---|---|
| Epistemology | essentialist ←→ constructionist |
| Orientation | experiential ←→ critical |
| Coding logic | inductive ←→ deductive |
| Coding depth | semantic ←→ latent |

## Why it fits this project

You are recording interviews and generating transcripts. Something has to turn
them into design-usable claims, and the default — skimming for good quotes that
support what you already drew — is exactly the failure mode a documented method
prevents.

For this project the honest declaration is roughly: **experiential**
orientation (engineers' accounts are treated as reports of real practice),
**mostly inductive** but with deductive passes against `T01`/`T02` (you *are*
looking for cues and abstraction levels), coding at **semantic** level first
and **latent** on a second pass. Write that into each study's `findings.md`.

Note the mismatch to watch: reflexive TA assumes a moderate dataset. With four
CDM interviews you are closer to case-based analysis. That is fine — but say
so, and lean on `M04`'s own structure (timelines, cue inventories) rather than
forcing thematic saturation language onto four cases.

## How to run it here

- **Transcribe in full.** Working from memory or notes silently discards the
  disconfirming material.
- **Code in a plain-text or spreadsheet register**, one row per coded segment:
  `code | participant | study | excerpt | latent?`. Greppable, diffable,
  cheap to re-read — see `0-meta/CONVENTIONS.md`.
- **Keep a reflexive log** as you go: what surprised you, what you resisted,
  what you were hoping to find. Two lines per session. This is the audit trail
  that makes the analysis defensible.
- **Anonymise at transcription.** Real names never leave `private/`.
- Promote surviving themes into `3-insights/` as `I-*` entries, each carrying
  its evidence and a stated confidence.

## What it produces

Named themes with definitions, evidence, and traceable provenance from
transcript to insight to design decision. That chain is what makes a design
change defensible to an ExRobotics stakeholder six months later.

## Traps

- **Topic summaries dressed as themes.** "Logging" is a topic. "Engineers
  distrust health flags they cannot trace to a raw observation" is a theme —
  it makes a claim.
- **Counting.** Reflexive TA is not frequency analysis. Three participants is
  not "more valid" than one if the one is better evidenced. Do not report `n=`
  as if it were incidence.
- **Coding only the quotable.** The boring middle of a transcript is where
  routine practice hides.
- **Skipping phase 4.** Most first-pass themes do not survive contact with the
  full dataset. If all of yours did, you did not review them.

## Sources

`[braun2022]` for the full procedure; `[braun2021]` on what counts as quality.
See `SOURCES.md`.
