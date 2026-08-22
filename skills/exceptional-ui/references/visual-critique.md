# Visual critique

Critique is a diagnosis of rendered evidence followed by a prioritized repair
plan. Avoid vague reactions such as “make it pop,” “needs polish,” or “looks
clean.”

## Required inputs

- current screenshot at the intended viewport;
- previous screenshot from the same viewport when iterating;
- design-direction brief;
- primary user job and state shown;
- relevant reference principles, not just reference images;
- known design-system constraints.

Use `get_screenshot` for a small number of frames the model must inspect. Use
`save_screenshots` for durable/full-resolution output or many frames. Exact
values come from FigWright structure reads; screenshots are visual evidence.

## Critique sequence

### 1. Five-second read

Without zooming:

- What is the product/scope?
- What is happening?
- What is the primary object or evidence?
- What action or decision is expected?
- Which element wins first, and should it?

If the answers are unclear, do not begin with micro-polish.

### 2. Thumbnail and silhouette

View at 15–20% scale:

- identify the dominant mass and scan path;
- check whether navigation and content form one intentional object;
- compare the overall silhouette with sibling screens;
- apply the logo-swap test for genericness.

For a screen set, check that each view's dominant composition changes with its
job while the edge, type, interaction, and signature grammar remains shared.
Repeated page templates are not family coherence.

### 3. Greyscale and blur

Remove color mentally or through an available preview; squint/blur:

- hierarchy must remain;
- surface layers must remain distinct;
- accent must not be carrying structure;
- several regions must not compete equally.

### 4. Composition and relationships

Check:

- dominant object earns its area;
- spans and alignments reveal purpose;
- related information is spatially connected;
- negative space is intentional;
- sparse and dense zones alternate;
- repeated cards do not flatten priority;
- overlaps and floating layers explain ownership.

### 5. Content and interaction truth

Check realistic names, values, ranges, units, states, labels, images, and edge
cases. Verify that charts, diagrams, maps, and controls have real meaning. Look
for fake precision, decorative signals, missing selection, and impossible
states.

### 6. Visual-system coherence

Inspect typography roles, accent budget, radius ladder, edge grammar, surface
hierarchy, icon language, imagery treatment, and component states. Identify
where one region looks imported from a different design.

### 7. Design-system and implementation health

Confirm component attachment, variables/styles, intended fonts, auto-layout,
constraints, image crop, clipping, overflow, target size, and responsive/theme
behavior. This is a separate judgment from aesthetic quality.

### 8. Pixel-level finish

Only after earlier checks pass:

- optical alignment and baselines;
- awkward line breaks;
- inconsistent strokes or doubled borders;
- uneven internal padding;
- icon optical size;
- chart-label collisions;
- half-pixel artifacts;
- accidental shadow/glow differences.

## Record issues with evidence

Use:

```markdown
Issue:
Evidence in render:
Gate affected: design | correctness | system | distinctiveness
Impact: critical | high | medium | low
Root cause:
Proposed correction:
Expected visual result:
```

Name the region and relationship. “Cards feel generic” is incomplete.
“The four equal 3-column tiles dominate before the selected topology, flattening
the diagnostic hierarchy” is actionable.

## Prioritize fixes

- **P0 — meaning/correctness:** wrong product model, misleading state,
  inaccessible primary action, missing content, clipping.
- **P1 — composition/hierarchy:** wrong dominant object, weak scan path,
  uniform density, generic page silhouette.
- **P2 — visual system:** weak typography contrast, uncontrolled color,
  inconsistent geometry, missing signature, asset mismatch.
- **P3 — polish:** small alignment, spacing, stroke, crop, and optical issues.

Fix no more than a coherent cluster per pass. Composition changes may invalidate
component polish; therefore work P0 → P1 → P2 → P3.

## Compare the iteration

Render the same viewport and answer:

1. Did the targeted issue visibly improve?
2. Did the scan path move as intended?
3. Did any new region become too dominant?
4. Did content, layout, component attachment, or responsive behavior regress?
5. Did distinctiveness increase through meaning rather than decoration?

Keep before/after screenshots until approval. If a change cannot be seen in the
render, it did not solve the visual problem.
