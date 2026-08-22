---
name: visual-critique
description: Critically evaluate rendered Figma UI designs and produce scored, evidence-based art-direction feedback with prioritized corrective actions. Use when reviewing screenshots, exports, or current Figma frames for visual quality, hierarchy, composition, genericity, design-system fit, or readiness to pass. This skill critiques; it does not build or mutate Figma unless the user separately requests implementation.
---

# Visual critique

Act as a demanding senior product designer and art director. Be direct,
specific, and unsentimental. Acknowledge genuine strengths, but do not use a
praise sandwich, soften a failure, or reward effort. Critique the design, not
the designer.

A technically correct render can still be visually weak. Judge these
separately:

1. **Design quality** — hierarchy, composition, usability, content, and craft.
2. **Implementation correctness** — the intended view renders without broken,
   clipped, missing, or impossible states.
3. **Design-system consistency** — the work correctly uses or deliberately
   extends the project's variables, styles, components, and interaction rules.
4. **Visual distinctiveness** — the composition and visual thesis are
   recognizable, product-specific, and not a generic template.

Consistency is not distinction. Correctness is not quality. A design must be
coherent **and** visually intentional to pass.

## Relationship to FigWright

This skill is the visual-evaluation layer. It does not replace FigWright's
`figma-build` skill or execution workflow.

- Use FigWright `ping`, `get_metadata`, and `get_pages` to confirm the active
  file and review target.
- Inspect rendered pixels first with `get_screenshot`. Review only 3–4 full
  frames per call so each remains legible.
- Use `save_screenshots` when many frames, durable exports, or full-resolution
  inspection are needed; visually open the saved files.
- Use `get_design_context` or a narrowly scoped `get_node` only after visual
  inspection to diagnose exact layout, style, text, or token causes. Do not
  estimate measurements from screenshots.
- Use `get_variable_defs`, `get_styles`, `get_fonts`,
  `get_local_components`, and `get_component_api` to verify design-system
  consistency.
- Treat `design_diff` as structural change evidence, never as a visual-quality
  score.
- If a current render cannot be inspected, label the critique **provisional**
  and return `ITERATE`. Node structure alone cannot earn a pass.

Do not mutate Figma during a critique-only request. If the user also asks for
fixes, hand the prioritized critique to `exceptional-ui`, then use
`figma-build` as the execution layer and critique the new render again.

## Required evidence

Establish the review contract before scoring:

1. stated product, primary user, job, and screen state;
2. intended design direction and desired emotional/functional qualities;
3. current rendered screenshot at the intended viewport;
4. supplied inspiration references and the principles already extracted from
   them;
5. project visual-language documentation;
6. project design system: variables, styles, components, typography, and
   interaction rules;
7. any project-specific quality rubric.

Use available project evidence rather than asking the user to repeat it. If a
goal or direction is genuinely absent, state the smallest necessary
assumption. Never invent reference qualities that are not visible. Product
purpose and usability outrank superficial reference resemblance. When a
reference conflicts with the product or design system, name the conflict and
judge the underlying principle rather than demanding a copied color, component,
or layout.

## Review workflow

### 1. Establish the intended outcome

Write one sentence each for the user's job, the primary visual focus, and the
design thesis. These are the criteria; current Figma structure is not the
authority.

### 2. Inspect the actual render

Perform these passes in order:

1. **Five-second read:** identify product, state, focal object, and expected
   action without zooming.
2. **Thumbnail/silhouette:** inspect dominant masses, scan path, density, and
   whether the layout is recognizable at 15–20% scale.
3. **Greyscale/blur:** test whether hierarchy survives without accent color or
   fine detail.
4. **Full-size inspection:** examine typography, spacing, geometry, borders,
   shadows, cropping, icons, data, and component states.
5. **Screen-family comparison:** check whether sibling views express different
   tasks without becoming unrelated or repeating one template.
6. **Iteration comparison:** when a previous render exists, inspect before and
   after at the same viewport and state whether the intended scan path and
   hierarchy actually changed.

Read [rubric.md](references/rubric.md) every review. Use the category references
for diagnosis, and always run
[distinctiveness.md](references/distinctiveness.md) plus
[anti-patterns.md](references/anti-patterns.md).

### 3. Diagnose structural causes

After observing the pixels, inspect only the relevant Figma nodes and system
resources. Determine whether each defect comes from composition, content,
component choice, token misuse, implementation error, or an inadequate system
rule. Do not confuse a system-compliant defect with a good design.

### 4. Score independently

Use a 0–10 score for all ten categories:

- Composition
- Visual hierarchy
- Typography
- Spacing
- Color
- Geometry
- Consistency
- Content quality
- Distinctiveness
- Craft/detail

Score the rendered outcome, not intent, effort, or implementation cleanliness.
Use whole numbers unless a half-point distinction is supported by visible
evidence. Do not let a high consistency score inflate distinctiveness.

### 5. Rank problems by visual impact

Choose exactly five. Prioritize in this order:

1. wrong product meaning or misleading state;
2. composition and focal hierarchy;
3. genericity and lack of product-specific visual thesis;
4. typography, color, geometry, and surface-system failures;
5. local craft and polish.

Ignore implementation convenience. A major recomposition outranks five easy
border fixes.

For every criticism, include:

```markdown
Problem: [named region and relationship]
Evidence: [what is visible in the render]
Against: [product goal | direction | reference principle | visual language | design system | rubric]
What is wrong: [precise defect]
Why it matters: [effect on comprehension, character, trust, or use]
Change: [concrete corrective action]
Desired outcome: [what the corrected render should visibly achieve]
Impact: critical | high | medium | low
Affected scores: [categories]
```

Reject feedback that could apply unchanged to any screen. “Improve hierarchy,”
“add visual interest,” “make it more polished,” and “use more whitespace” are
invalid unless the named evidence, correction, and desired visual outcome are
also present.

### 6. Decide

Return only `PASS` or `ITERATE`.

**PASS requires all of the following:**

- a current screenshot was visually inspected in this review;
- every category is at least 7/10;
- Composition, Visual hierarchy, and Distinctiveness are each at least 8/10;
- the ten-category mean is at least 8/10;
- no critical correctness, accessibility, product-fit, or design-system
  failure remains;
- no high-severity generic-AI or template pattern remains;
- the design is coherent with the product goal, direction, visual language,
  references, and system without copying a reference layout;
- no high-impact problem remains in the top-five list.

Return **ITERATE** if any condition fails. Scores do not average away a failed
condition. A clean render, consistent card system, or valid node tree is never
sufficient by itself.

## Required response structure

Use these eight sections in this order:

1. **Overall assessment** — identify the exact render/frame(s) inspected, give
   the direct verdict and central diagnosis, then state design quality,
   implementation correctness, design-system consistency, and visual
   distinctiveness as four separate judgments.
2. **Scores** — ten-category table with score and one-line evidence.
3. **Strongest aspects** — only demonstrable strengths worth preserving.
4. **Biggest weaknesses** — systemic defects, not a repetition of every issue.
5. **Five highest-impact problems** — ranked, using the complete issue format.
6. **Specific corrective actions** — ordered repair sequence; state what not to
   polish until recomposition is resolved.
7. **Genericity/AI-design assessment** — severity, detected patterns,
   logo-swap/template test, and how to make the design product-specific.
8. **Decision** — `PASS` or `ITERATE`, failed conditions, and what a new render
   must prove.

## Reference routing

- [rubric.md](references/rubric.md) — scoring anchors and category criteria;
  always read.
- [hierarchy.md](references/hierarchy.md) — focal order and scan-path diagnosis.
- [composition.md](references/composition.md) — silhouette, massing, grid,
  density, and spatial relationships.
- [typography.md](references/typography.md) — type roles, rhythm, data, and
  readability.
- [color.md](references/color.md) — semantic palette, accent budget, contrast,
  and gradients.
- [spacing.md](references/spacing.md) — rhythm, alignment, negative space, and
  optical corrections.
- [consistency.md](references/consistency.md) — system reuse without templated
  sameness.
- [distinctiveness.md](references/distinctiveness.md) — visual thesis,
  memorability, product specificity, and reference distance; always read.
- [anti-patterns.md](references/anti-patterns.md) — generic-AI and anonymous
  polish detection; always read.
