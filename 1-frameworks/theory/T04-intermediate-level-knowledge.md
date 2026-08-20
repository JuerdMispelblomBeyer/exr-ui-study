---
id: T04
title: Intermediate-Level Knowledge
kind: theory
status: adopted
use_when: [deciding what to write down as a finding, packaging results, handover]
sources: [hook2012, lowgren2013, gaver2012ap, gaver2012]
---

# Intermediate-Level Knowledge

**Between "here is my file" and "here is a theory of interaction" sits the
level where design knowledge actually transfers. Aim there deliberately.**

## What it is

Design research produces knowledge at several altitudes:

| Altitude | Form | Transfers? |
|---|---|---|
| **Particular** | The artefact itself — this Figma file | Barely. Dies with the file. |
| **Intermediate** | Strong concepts, patterns, annotated portfolios, experiential qualities, bridging concepts | Yes — this is the useful band |
| **General** | Theory of interaction | Rarely reached by a design project, and usually over-claimed when it is |

Höök & Löwgren's **strong concepts** `[hook2012]` are the sharpest form: an
idea that is abstracted from any single instance, carries a *behaviour over
time*, is generative for new designs, and is grounded in demonstrated
instances. Not a UI pattern — something closer to a design move with a name.

Gaver & Bowers' **annotated portfolios** `[gaver2012ap]` reach the same band by
the opposite route: rather than abstracting upward, keep the instances and
annotate the dimensions along which they differ (`M07`).

Löwgren's point is that these forms interlink — patterns, strong concepts,
qualities, and portfolios build one web of transferable knowledge
`[lowgren2013]`.

## Why it matters here

This determines what your final deliverable to ExRobotics actually is.

A Figma file is particular knowledge. When the next person needs a screen you
never drew, it gives them nothing but precedent to imitate. `docs/` in its
current form is closer to general prescription — rules asserted without the
instances that would justify or bound them.

The intermediate band is what is missing, and it is what makes design work
survive the designer's departure. It is also `M01`'s **extensibility**
criterion, which is the one design projects reliably fail.

There is already a candidate strong concept latent in this project. The
"instrument stage" rule in `docs/DESIGN_GUIDELINES.md` §10 — every primary tile
must contain a real micro-instrument (trace, topology, matrix, path, state map)
rather than title/value/metadata — is abstracted from instances, generative,
and makes a claim about how understanding forms. Right now it is written as a
house style rule. Evidenced through iterations and evaluation, it could be
stated and defended as a strong concept: *a diagnostic surface earns its space
by showing structure, not by reporting a number.*

## How to use it

- **When writing an insight, name its altitude.** "P03 could not find the CAN
  status" is particular. "Engineers look for the *relationship* before the
  *value*" is intermediate — and is a claim you can test in the next iteration.
- **Watch for recurrence.** A dimension that keeps appearing across `M07`
  annotations is a strong-concept candidate. Three independent instances is a
  reasonable bar before promoting it.
- **Promote deliberately.** Insight (`3-insights/`) → recurring annotation
  dimension (`M07`) → named concept in `4-design/` → decision in
  `6-log/decisions.md`. Each step should be traceable back to evidence.
- **Do not over-claim.** Gaver's position is that RtD knowledge is provisional,
  contingent, and aspirational `[gaver2012]`. State confidence; a concept
  supported by two sessions is a hypothesis with a name.

## Caveats

- Strong concepts have a high bar. Most findings are patterns or annotations,
  and that is fine — mislabelling a pattern as a strong concept weakens both.
- The band is not a licence for vagueness. "Make it feel trustworthy" is not
  intermediate-level knowledge; it is an unfinished thought.

## Sources

`[hook2012]` for strong concepts; `[lowgren2013]` for how the forms interlink;
`[gaver2012ap]` for annotated portfolios. See `SOURCES.md`.
