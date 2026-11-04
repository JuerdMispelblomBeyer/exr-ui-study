---
name: exceptional-ui
description: Orchestrate distinctive, high-quality Figma design from brief through reference intelligence, direction, composition, FigWright build, screenshot critique, and revision. Use for new screens, substantial redesigns, or visual-direction work where successful construction is not sufficient. It directs design-reference-analysis, FigWright's figma-build layer, and visual-critique without replacing them.
---

# Exceptional UI

```text
BRIEF → REFERENCES → DIRECTION → COMPOSITION → FIGMA BUILD → SCREENSHOT
→ CRITIQUE → PRIORITIZED FIXES → REVISION → SCREENSHOT → CRITIQUE → PASS
```

Operate as designer → art director → visual QA → designer. This skill owns the
target direction, composition, fix priorities, and loop. Specialists keep their
boundaries:

| Layer | Owns | Returns |
|---|---|---|
| `design-reference-analysis` | Visible reference evidence and transferable principles | Compact reference handoff |
| `exceptional-ui` | Brief, thesis, composition, system decisions, orchestration | Direction and revision briefs |
| FigWright `figma-build` | Figma inspection, construction, reuse, structural verification, exports | Frames plus implementation evidence |
| `visual-critique` | Independent screenshot-first judgment | Scores, five issue IDs, `PASS`/`ITERATE` |

Reference analysis does not choose the target design. FigWright success does not
prove visual quality. The critic does not mutate Figma.

## Token economy without visual compromise

Save tokens in context and prose, never in visual evidence:

- maintain one compact run packet using
  [handoff-packet.md](references/handoff-packet.md); pass IDs and paths instead
  of repeating source text;
- read each unchanged project source once per run; reopen only the exact section
  needed to resolve a decision;
- load references progressively from the router below, not as a bundle;
- batch compatible Figma reads, then work on the exact subtree; avoid repeated
  page-wide metadata dumps after grounding;
- inspect 1–4 legible frames per screenshot call and request full-size crops for
  dense regions; never shrink a render below reliable visual judgment;
- after the first full critique, use delta critique: inspect the entire new
  render but write only score changes, unresolved/new issue IDs, and the next
  fixes; perform a full record again at final `PASS`;
- keep rejected options, unchanged scores, and repeated rationale to one line or
  an ID reference.

If compactness would hide uncertainty, a state, or a visual defect, spend the
tokens. Creativity comes from exploring materially different compositions and
inspecting pixels—not from verbose narration.

## Workflow

### 1. Brief and ground

Capture user, situation, job, decisive question, error consequences, realistic
content/states, constraints, and exclusions. Confirm the Figma file, target
frames, current render, variables, styles, fonts, components/APIs, and archive
rules. Record only reuse, extend, and missing decisions in the run packet.

### 2. Analyze references when relevant

Invoke `../design-reference-analysis/SKILL.md` when references are supplied or
materially shape the direction. Give it the brief and source paths. Consume its
compact handoff; do not paste individual analyses into this context. If there
are no relevant references, mark the stage skipped.

### 3. Establish direction

Define:

- one product-specific visual thesis and explicit opposites;
- dominant object/relationship and scan order;
- density and surface hierarchy;
- two to four functional signature moves;
- reuse/extend/create decisions for type, color, spacing, grid, radius, edges,
  shadows, imagery, and component language;
- adopted principle IDs and explicit anti-copy/genericity exclusions.

Read [visual-language.md](references/visual-language.md) only when the direction
is unresolved, and load a foundation reference only for a system being decided
or corrected. A direction applicable to many unrelated SaaS products fails.

### 4. Resolve composition before components

When composition is not fixed, develop at least two hypotheses that differ in
dominant object, spatial model, or scan path. Select against product truth,
system fit, and distinctiveness. Resolve silhouette, grid, major spans,
navigation ownership, density changes, negative space, and focal path in
greyscale/restrained color. Use [composition.md](references/composition.md) only
for new composition or recomposition.

### 5. Build with FigWright

Follow FigWright's `figma-build` skill. Reuse attached components, variables,
styles, real assets, realistic labels/data, and consequential states. Add a
foundation only for a recurring missing role. Build incrementally and return
node IDs plus brief structural/reuse evidence; do not return verbose layer-tree
dumps unless diagnosing a defect.

### 6. Render and critique

Capture every materially changed screen at a stable, legible viewport. Open the
pixels. Invoke `../visual-critique/SKILL.md` with the run packet, current render,
and only the linked evidence it requests. The critic uses the shared rubric and
genericity index. Missing current visual evidence forces `ITERATE`.

### 7. Prioritize and revise

Convert critique issue IDs into a bounded revision brief, ordered by:

1. product/safety/state truth;
2. composition, hierarchy, scan path, density;
3. genericity and weak product-specific thesis;
4. content, interaction, imagery, and system divergence;
5. typography, color, geometry, surfaces, then micro-craft.

State the visible outcome for each fix. Send only this delta to `figma-build`,
re-render the same viewport, and critique again. Preserve resolved issue IDs so
the critic does not rediscover or rewrite them.

## Independent gates

Keep separate: functional correctness, implementation correctness,
design-system correctness, visual quality, and distinctiveness. Implementation
health is a blocker, not bonus visual-quality points. Consistency cannot rescue
an ordinary composition.

## Completion

Complete only when the current inspected render:

1. satisfies the product requirements and user job;
2. has no blocking implementation defect;
3. respects or deliberately extends the design system;
4. has strong hierarchy and intentional product-shaped composition;
5. has no high-severity generic-AI pattern;
6. remains distinctive without logo, copy, or lead accent;
7. passes `visual-critique` under the shared 100-point rubric after at least one
   material correction pass for substantial work.

Retain the compact packet, before/after screenshots, issue history, final score,
and reuse evidence. Never declare success because nodes rendered correctly.
Update project guidance only when a reusable rule changed.

## Progressive reference router

- [handoff-packet.md](references/handoff-packet.md) — always use; compact state
  shared between stages.
- [quality-rubric.md](references/quality-rubric.md) — read its operational
  scorecard for every critique; open detailed anchors only for uncertain or
  failing dimensions.
- [anti-patterns.md](references/anti-patterns.md) — read its detection index;
  open full entries only for detected/suspected patterns.
- [design-principles.md](references/design-principles.md) — use when the thesis
  or system decisions are weak.
- [typography.md](references/typography.md), [color.md](references/color.md),
  [spacing-and-geometry.md](references/spacing-and-geometry.md), and
  [imagery.md](references/imagery.md) — load only the affected system.
