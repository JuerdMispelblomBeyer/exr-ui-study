---
name: exceptional-ui
description: Art-direct, design, review, and iteratively elevate visually distinctive interfaces in Figma through FigWright. Use when a Figma screen, product surface, component family, or visual direction must be unusually polished, compositionally intentional, reference-informed, or resistant to generic AI-dashboard patterns. Use alongside figma-build for Figma execution; not for routine mechanical edits or Figma-to-code work.
---

# Exceptional UI

Produce work through four roles in sequence:

> designer → art director → visual QA → designer

This skill owns product interpretation, visual direction, reference synthesis,
composition, critique, and the quality threshold. It does not replace
`figma-build`.

## Relationship to FigWright

- Load and follow FigWright's `figma-build` skill for every Figma write. It is
  the execution layer: connection, design-system grounding, auto-layout,
  component reuse, variable/style binding, construction, and structural
  verification.
- Use `figma-codegen` only for Figma-to-code work. Do not duplicate its
  provider-first code workflow here.
- Use `get_screenshot` for images the model must inspect and
  `save_screenshots` for durable or full-resolution exports. Screenshots
  verify visual output; exact measurements and bindings come from Figma reads,
  not image estimation.
- `design_diff` detects structural design changes for code synchronization. It
  is not a visual-quality score.

## Four independent gates

A design succeeds only when all four gates pass:

1. **Design quality** — the product purpose, information hierarchy,
   composition, legibility, interaction emphasis, and visual coherence work.
2. **Implementation correctness** — the Figma structure renders and behaves
   correctly: no clipping, broken sizing, missing assets, accidental overlap,
   or implausible states.
3. **Design-system consistency** — existing variables, styles, components,
   states, naming, and component APIs are reused or deliberately extended.
4. **Visual distinctiveness** — the result has a context-appropriate visual
   thesis and recognizable signature; it is not interchangeable with a generic
   AI-generated SaaS dashboard.

Technical correctness cannot compensate for weak design. Rendering without an
error proves only that rendering worked.

## Required workflow

### 1. Understand product, user, and purpose

Establish the primary user, situation, job, decision, frequency, consequences,
content truth, and platform constraints. Distinguish operational work from
marketing, onboarding, exploration, configuration, and presentation.

### 2. Inspect the existing Figma file and system

Before proposing a direction, use FigWright to confirm the connected file and
inspect pages, relevant existing screens, variables, styles, fonts, components,
component APIs, and the target subtree. Record what must be reused, what may be
extended, and what is genuinely missing. Respect project archive/version rules.
Use `ping` + `get_metadata`/`get_pages` for identity, then
`get_variable_defs`, `get_styles`, `get_fonts`,
`get_local_components`/`get_component_api`, and
`get_design_context` as relevant. For a redesign, screenshot the current
state before mutation so the visual change can be judged.

### 3. Inspect visual references

Visually open every relevant reference; filenames and page copy are not visual
evidence. Separate direct screenshots from device mockups and presentation
imagery. Read [reference-analysis.md](references/reference-analysis.md). For a
substantial reference set, formal Visual DNA profile, or cross-reference
synthesis, also load `../design-reference-analysis/SKILL.md`; its output becomes
the evidence base for the direction brief.

### 4. Extract principles; do not copy layouts

For each source, identify observable principles in silhouette, hierarchy, grid,
density, geometry, depth, typography, imagery, instrumentation, and
interaction. Classify each as adopt, translate, presentation-only, or reject.
Never import the source product model or reproduce its composition by swapping
labels.

### 5. Establish a design direction before building

Write a compact direction brief containing:

- product/user/job;
- one-sentence visual thesis;
- intended character and explicit opposites;
- two or three signature moves with functional reasons;
- dominant composition and scan order;
- density rhythm and surface hierarchy;
- typography, color, geometry, imagery, and component-language intent;
- reference principles being translated;
- patterns explicitly prohibited for this design.

If the direction could describe dozens of unrelated products, it is not
specific enough. Use [visual-language.md](references/visual-language.md) and
[design-principles.md](references/design-principles.md).

When the visual direction is not already fixed, develop at least two materially
different composition hypotheses before choosing. They must differ in dominant
object, spatial model, or scan path—not merely palette, radius, or card styling.
Select one against user purpose, content truth, system fit, and distinctiveness.

### 6. Define or reuse the visual system

Create a reuse/extend/create decision for typography, color, spacing, grid,
radius, borders, shadows, surface hierarchy, imagery, and component language.
Prefer existing Figma variables, styles, and components. Add a foundation only
when a recurring role is missing; avoid one-off tokens for decoration.

Load the relevant operational references:

- [typography.md](references/typography.md)
- [color.md](references/color.md)
- [spacing-and-geometry.md](references/spacing-and-geometry.md)
- [imagery.md](references/imagery.md)

### 7. Develop composition before component detail

Resolve the viewport silhouette, dominant mass, navigation ownership, grid,
major spans, negative space, density changes, and primary focal path before
polishing controls. Work in greyscale or restrained color first. Read
[composition.md](references/composition.md).

### 8. Build through `figma-build`

Use FigWright incrementally. Reuse components and variables before creating
primitives. Use realistic content, real assets, plausible states, meaningful
data, and production-length labels. Do not let placeholder content determine
the layout.

### 9. Render and visually inspect

Screenshot every materially changed screen at a legible scale. Inspect the
rendered pixels, not only the layer tree or tool response. A successful export
is the beginning of visual QA, not completion.

### 10. Perform a rigorous critique

Use [visual-critique.md](references/visual-critique.md) and score
[quality-rubric.md](references/quality-rubric.md). Check first impression,
scan path, composition, hierarchy, distinctiveness, content credibility,
system consistency, states, accessibility, clipping, and pixel-level polish.
Run a greyscale check and a reduced-size/squint check.

### 11. Fix the highest-impact problems

Prioritize in this order unless task risk demands otherwise:

1. wrong product model, user flow, or dominant object;
2. weak composition, hierarchy, density, or scan path;
3. generic visual language or missing signature;
4. misleading content, state, interaction, or imagery;
5. design-system divergence and component inconsistency;
6. typography, color, geometry, and surface ownership;
7. alignment, optical balance, and micro-polish.

Do not spend a pass tuning shadows while the composition is still ordinary.

### 12. Render and inspect again

Capture the same viewport after fixes. Verify that the intended problems
actually improved and that no regression appeared elsewhere.

### 13. Repeat until the rubric passes

Continue critique → prioritized fix → screenshot until all four gates pass.
When a blocking limitation remains, state it explicitly and do not label the
design exceptional.

For multi-screen work, also compare the set together: each screen needs a
different task-specific composition while remaining recognizably one product.

## Non-negotiable constraints

- Do not blindly copy references, trace their layout, or transplant their
  product model.
- Do not default to sidebar + header + equal KPI cards + generic chart + table.
- Avoid decorative gradients, excessive pills, indiscriminate glass, universal
  rounded cards, fake charts, and empty “premium” spacing.
- Do not add visual novelty without product meaning.
- Prefer real logos, icons, photographs, illustrations, diagrams, and realistic
  copy over grey boxes, generic avatars, lorem ipsum, or repeated round-number
  metrics.
- Distinctiveness must survive removal of brand color. Color may amplify a
  visual language; it may not substitute for one.
- Reuse does not require sameness: compose existing components in a more
  intentional hierarchy before inventing new component styling.
- Never declare success merely because FigWright returned valid nodes or the
  frame rendered correctly.

Read [anti-patterns.md](references/anti-patterns.md) before the first critique.

## Completion evidence

Do not complete the task without:

- the stated design direction;
- an inspected pre-fix screenshot;
- a recorded critique with prioritized issues;
- at least one material correction pass;
- an inspected post-fix screenshot;
- a passing four-gate rubric, or an explicit account of unresolved failures;
- confirmation of component/variable/style reuse and implementation health.

When the project maintains design guidance, tokens, or a decision log, record
new reusable rules there; do not leave the design rationale only in Figma.
