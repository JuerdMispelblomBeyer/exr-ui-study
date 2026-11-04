---
name: design-reference-analysis
description: "Convert visually inspected UI references into compact, traceable design intelligence: Visual DNA, signature moves, transferable principles, conflicts, opportunities, and anti-copy constraints. Use for screenshots, case studies, mockups, or reference sets. It understands references; it does not choose or build the target design."
---

# Design reference analysis

Produce reusable reasoning, not screenshot narration:

> observation → interpretation → transferable principle

This skill owns reference evidence only. `exceptional-ui` chooses the target
thesis and composition; FigWright builds; `visual-critique` judges the result.

## Visual-quality and token rule

Inspect every actual reference at useful resolution. Save tokens by eliminating
repetition, not by skipping visual passes:

- use thumbnail, normal, full-size/crop, and greyscale/squint passes;
- write one evidence block for a relationship and tag all dimensions it
  supports instead of restating it under several headings;
- assign stable IDs and refer to them in Visual DNA, signature moves, and
  synthesis;
- save individual analyses as files; pass only an index and compact synthesis
  downstream;
- describe qualitative roles/relationships unless exact measurement is asked;
- for a large set, batch viewing by visual archetype but still inspect and
  identify every source individually;
- load detailed reference guides only for ambiguous dimensions.

Device mockups, hands, lighting, perspective, and case-study staging are not UI
pixels. Do not reduce resolution or crowd so many images into one contact sheet
that typography, spacing, or surface behavior cannot be judged.

## Evidence block

Use this once per substantive observation:

```markdown
ID: R1-COMP-01
Scope: [visible region]
Dimensions: [composition, grid, hierarchy]
Observation: [visible fact]
Interpretation: [decision/effect; confidence high|medium|low]
Transfer: [source-independent principle and useful condition]
```

Do not infer unseen states, motion, grids, fonts, libraries, or tokens. Record
source type, viewport/crop limits, and provenance. A URL title or filename is
not visual evidence.

## Per-reference analysis

Cover all 23 dimensions, grouped compactly where one block supports several:

1. aesthetic; 2. personality; 3. composition; 4. grid; 5. alignment;
6. density; 7. whitespace; 8. typography; 9. type hierarchy;
10. color system; 11. contrast; 12. shape language; 13. borders;
14. shadows; 15. surface hierarchy; 16. imagery; 17. iconography;
18. information hierarchy; 19. interaction cues; 20. defensible motion
implications; 21. distinctive decisions; 22. reusable principles;
23. anti-patterns/anti-copy details.

Then produce:

- a 13-field Visual DNA profile: aesthetic, personality, density, whitespace,
  grid, typography, color, geometry, surfaces, imagery, hierarchy, composition,
  distinctiveness; each field cites evidence IDs;
- 5–10 genuine signature moves, each with anatomy, effect, dependency,
  transferable use, and what not to copy;
- four dispositions: borrow, ignore, brand-specific, accidental;
- limitations and attractive-looking patterns that would be misleading or
  inappropriate in the target.

Use [visual-dna.md](references/visual-dna.md) and
[distinctive-patterns.md](references/distinctive-patterns.md) only when their
schema or calibration is needed; the requirements above remain mandatory.

## Multi-reference synthesis

For two or more sources, use [synthesis.md](references/synthesis.md). Compare by
mechanism, not adjectives, and output:

- common and complementary principles;
- precise conflicts and the condition that should decide them;
- interesting combinations and dependencies;
- principles to avoid;
- target-specific opportunities absent from the references;
- open decisions for `exceptional-ui`.

Do not average sources or choose the final target direction. Trace every
synthesis row to evidence IDs.

## Compact outputs

### Individual Markdown file

1. identity, source type, limits;
2. executive design reading, maximum three sentences;
3. Visual DNA table;
4. evidence blocks covering all dimensions;
5. signature moves;
6. borrow/ignore/brand/accidental table;
7. limitations and anti-copy constraints.

Avoid a separate prose section when a cited evidence block already says it.

### Downstream handoff

Keep the synthesis handoff under roughly 700 words unless the user requests a
report. Include source paths, strongest principle IDs (maximum six), conflicts
(maximum three), opportunities (maximum four), exclusions (maximum four), and
open decisions. Link individual files; never paste them.

## Quality gate

Complete only when every reference was visibly inspected, all dimensions are
findable, claims separate evidence/interpretation/transfer, profiles have all
13 fields, signature moves are characteristic, dispositions are explicit,
motion inferences are labeled, and the compact handoff enables original design
without copying a source.

## Progressive reference router

Load only the affected guide:

- [composition.md](references/composition.md) — grid, alignment, density,
  whitespace;
- [typography.md](references/typography.md), [color.md](references/color.md),
  [geometry.md](references/geometry.md), or [imagery.md](references/imagery.md)
  — ambiguous visual-system evidence;
- [hierarchy.md](references/hierarchy.md) — unclear scan/order;
- [interaction.md](references/interaction.md) — interaction or motion claims;
- [visual-dna.md](references/visual-dna.md) — profile calibration;
- [distinctive-patterns.md](references/distinctive-patterns.md) — weak or
  generic signature moves;
- [synthesis.md](references/synthesis.md) — multiple references only.
