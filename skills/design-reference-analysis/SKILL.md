---
name: design-reference-analysis
description: Analyze visual UI references and convert visible evidence into structured, reusable design intelligence. Use for screenshots, case studies, mockups, videos, or reference sets when another AI designer needs visual principles, signature moves, anti-copy constraints, or an original synthesized direction—not a description of what the image contains.
---

# Design reference analysis

Turn reference imagery into design reasoning another agent can recombine. Do
not narrate screenshots, reverse-engineer a clone, or tell a downstream agent
to “make it look like” the source.

The deliverable is evidence-based visual intelligence:

> visible evidence → inferred design decision → transferable principle

This skill analyzes references. It does not build in Figma, choose final tokens,
or critique the target design. Feed its output into `exceptional-ui` for art
direction and construction; use `visual-critique` on rendered target work.

## Evidence rules

1. Visually inspect the actual reference. A filename, URL title, alt text, or
   case-study description is not visual evidence.
2. Record source type: direct UI screenshot, device mockup, editorial/case-study
   composition, marketing render, photograph, animation/video, or partial crop.
3. Separate interface pixels from presentation framing. Hardware, hands,
   lighting, perspective, and background staging may inform presentation but
   are not automatically UI structure.
4. Identify the visible region behind each claim. Do not infer unseen screens,
   states, grids, tokens, interactions, or motion as facts.
5. Mark inference confidence `high`, `medium`, or `low`. Omit unsupported claims.
6. Do not name a font, component library, or exact measurement unless evidence
   supports it. Describe the functional category when identity is uncertain.
7. Do not sample exact colors, dimensions, radii, or shadows into a target
   system unless the user explicitly requests measurement. Analyze roles and
   relationships first.

## The mandatory analysis unit

Every meaningful observation must use all three labels:

```markdown
ID: [reference]-[dimension]-[sequence], for example R1-COMP-01
Scope: [visible region or element relationship]

OBSERVATION
[What is visibly present, where it appears, and how elements relate.]

INTERPRETATION
[The design decision and the perceptual, cognitive, emotional, or interaction
effect it likely creates. Include confidence.]

TRANSFERABLE PRINCIPLE
[A product-agnostic rule another designer can apply without copying the source.
State the conditions under which it is useful.]
```

“The hero has a large heading” is only an observation. A complete analysis
explains that typography is the primary compositional object, why it wins before
imagery, and how another product could use typographic mass to establish focus
without reusing the words, font, size, or layout.

Assign stable IDs to every analysis block. Reuse those IDs in signature moves,
synthesis matrices, and the downstream brief so principles remain traceable to
visible evidence.

## Workflow

### 1. Establish provenance and viewing limits

For each source, record identifier, creator/brand when known, URL or local path,
capture type, visible viewport/state, and any crop, occlusion, perspective, or
resolution limitation. Separate direct observation from page copy.

### 2. Inspect at multiple scales

Use four passes:

1. **Thumbnail:** silhouette, dominant mass, composition, and memorability.
2. **Normal view:** scan path, grid, alignment, density, whitespace, and surface
   ownership.
3. **Full-size/crops:** type, icons, borders, shadows, images, data, and control
   cues.
4. **Greyscale/squint:** hierarchy, contrast distribution, and dependence on
   color.

For animation or video, sample stable key states plus the transitions that
change hierarchy, ownership, or spatial continuity. Do not catalog every frame.

### 3. Analyze all required dimensions

For each reference, cover:

1. Overall aesthetic
2. Visual personality
3. Composition
4. Grid
5. Alignment
6. Density
7. Whitespace
8. Typography
9. Type hierarchy
10. Color system
11. Contrast
12. Shape language
13. Border treatment
14. Shadow treatment
15. Surface hierarchy
16. Imagery
17. Iconography
18. Information hierarchy
19. Interaction cues
20. Motion implications, only where visually inferable
21. Distinctive design decisions
22. Reusable principles
23. Anti-patterns or details that should not be copied

Do not force 23 disconnected paragraphs. Group related dimensions using the
reference files, but make every dimension findable and ensure each substantive
claim uses the observation/interpretation/transfer structure.

### 4. Build the Visual DNA profile

Read [visual-dna.md](references/visual-dna.md). Create a compact qualitative
profile with these fields:

- aesthetic
- personality
- density
- whitespace
- grid
- typography
- color
- geometry
- surfaces
- imagery
- hierarchy
- composition
- distinctiveness

Use calibrated qualitative values such as `low / medium / high`,
`restrained / balanced / expressive`, or specific paired axes. Add one evidence
sentence and supporting observation IDs per field. The profile summarizes
completed analysis blocks; it must not introduce unexamined claims. Avoid
meaningless adjective clouds.

### 5. Extract 5–10 signature moves

Read [distinctive-patterns.md](references/distinctive-patterns.md). A signature
move is an unusual or characteristic relationship that materially contributes
to recognition. It is not merely “rounded cards” or “clean typography.”

For each move, record anatomy, effect, dependencies, transferable principle,
what must not be copied, and whether it is strong enough to influence a new
direction.

### 6. Classify what survives translation

Explicitly separate:

- **Principles worth borrowing** — effects and decision logic that transfer.
- **Implementation details worth ignoring** — source-specific dimensions,
  breakpoints, component anatomy, content, or technology assumptions.
- **Brand-specific details** — logos, proprietary assets, signature typefaces,
  colors, illustrations, shapes, or motifs whose identity belongs to the source.
- **Accidental details** — compression, crop, browser/device chrome, capture
  artifacts, temporary data, or one-off production imperfections.

Also list anti-patterns: attractive-looking decisions that would become
misleading, inaccessible, generic, or inappropriate outside the source context.

### 7. Synthesize multiple references

When more than one reference is supplied, read
[synthesis.md](references/synthesis.md) and identify:

- common principles;
- complementary principles;
- conflicting principles;
- interesting combinations;
- principles to avoid;
- opportunities for a new visual language.

Do not average the references. Resolve conflicts against the target product,
user, content, and design system. Produce an **ORIGINAL DESIGN DIRECTION** whose
composition and signature grammar are not traceable to one source layout.

## Required Markdown output

For each reference, write:

1. **Reference identity and evidence quality**
2. **Executive design reading** — the central design decision, not a screenshot
   summary
3. **Visual DNA profile**
4. **Dimension analysis** — all 23 dimensions using the mandatory analysis unit
5. **Signature moves** — 5–10
6. **Principles worth borrowing**
7. **Implementation details worth ignoring**
8. **Brand-specific details**
9. **Accidental details**
10. **Anti-patterns and anti-copy constraints**

For a reference set, append:

11. **Cross-reference synthesis**
12. **ORIGINAL DESIGN DIRECTION**
13. **Downstream designer brief** — concise principles, signature grammar,
    explicit exclusions, and open decisions another skill can consume directly

Use stable headings, tables, and bullets so the output can be saved as Markdown
without rewriting. Preserve source traceability: each synthesized principle
must cite which reference observations support it.

## Quality gate

Do not complete until:

- every reference was visually inspected;
- all 23 dimensions are covered;
- every substantive claim separates observation, interpretation, and transfer;
- the Visual DNA profile contains all 13 fields;
- 5–10 genuinely characteristic signature moves are identified per reference;
- borrow/ignore/brand/accidental classifications are explicit;
- motion claims are labeled as inference and grounded in visible cues;
- anti-copy constraints remove exact source layouts and brand assets;
- multi-reference synthesis creates a new thesis rather than a visual average;
- the handoff can guide a designer without naming a source as the target look.

## Reference routing

- [visual-dna.md](references/visual-dna.md) — profile schema and qualitative axes;
  always read.
- [composition.md](references/composition.md) — composition, grid, alignment,
  density, and whitespace.
- [typography.md](references/typography.md) — typography and type hierarchy.
- [color.md](references/color.md) — color roles, contrast, and palette logic.
- [geometry.md](references/geometry.md) — shape, border, shadow, and surface
  hierarchy.
- [imagery.md](references/imagery.md) — imagery and iconography.
- [hierarchy.md](references/hierarchy.md) — information hierarchy and scan order.
- [interaction.md](references/interaction.md) — interaction cues and defensible
  motion implications.
- [distinctive-patterns.md](references/distinctive-patterns.md) — signature
  moves, disposition, and anti-copy analysis; always read.
- [synthesis.md](references/synthesis.md) — cross-reference synthesis and
  original-direction method; read for two or more sources.
