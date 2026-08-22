# Composition

Use this before refining colors, shadows, buttons, badges, or component
variants. The goal is to make importance and relationships visible through
space.

## Composition brief

Record:

- target viewport(s);
- primary user job and first decision;
- dominant object or relationship;
- required navigation and context;
- persistent, scrollable, selected, and temporary regions;
- sparse, standard, and dense content zones;
- expected scan path;
- one region that may be removed if space becomes constrained.

## Build in five passes

### Pass 1: silhouette

Block only the outer application shape, navigation ownership, main field, and
temporary layers. Inspect at thumbnail size. Avoid beginning with components.

Questions:

- Does the product read as one object or unrelated rectangles?
- Is the shell appropriate to the host environment?
- Is navigation structural, or an arbitrary sidebar?

### Pass 2: dominant mass and scan path

Give one object, relationship, message, or work area clear dominance. Arrange
supporting regions in the order the user needs them. Use size and position
before color.

Reject:

- four equally strong quadrants;
- a universal row of identical KPI cards;
- several unrelated hero elements;
- empty oversized headers that delay useful information.

### Pass 3: grid and alignment

Choose a column/grid model supported by the existing system. Define outer
inset, gutters, major spans, and alignment lines. Deliberate asymmetry is
welcome; accidental misalignment is not.

Use mixed spans when they encode purpose:

- wide/deep for relationships, timelines, canvases, or primary work;
- narrow/tall for ordered streams, filters, or inspectors;
- compact for decisive summaries;
- full-width only for content that genuinely needs continuity.

### Pass 4: density rhythm

Alternate information pressure:

- sparse region for orientation or the selected object;
- standard region for comparison and action;
- dense region for evidence, data, logs, or details.

Uniform spaciousness feels empty. Uniform density feels exhausting. Preserve
meaningful negative space inside the dominant region instead of inserting
blank bands between repeated cards.

### Pass 5: overlap, crop, and continuation

Use overlap only to show attachment, selection, temporary ownership, or depth.
Use cropping/continuation to imply a real scroll, pan, timeline, carousel, or
larger system—not as arbitrary decoration.

## Composition-first Figma pass

Before component polish:

1. build or identify the top-level frame;
2. establish real layout grids;
3. place major auto-layout regions using restrained neutral fills;
4. add representative real content to establish genuine size;
5. render a screenshot;
6. correct dominance, spans, gaps, and scan path;
7. only then apply the detailed system and component states.

Do not leave grey placeholder boxes in the finished design. The composition
pass is a decision tool, not a deliverable.

## Diagnostic checks

### Thumbnail check

At 15–20% scale, mark the first, second, and third visual stops. If several
elements tie for first, rebalance scale or contrast.

### Blur/squint check

Blurred masses should reveal a clear focal path. Tiny local styling should not
be required to understand the layout.

### Edge map

Trace the strongest horizontal and vertical edges. Misaligned near-edges create
visual noise. Either align them or separate them decisively.

### Container count

Count visible enclosing rectangles. Remove containers whose only purpose is to
put padding around another container. Prefer grouping through alignment and
surface continuity.

### Card dependency

Temporarily remove card fills. If the page collapses into unrelated labels,
charts, and buttons, the composition relies on card chrome instead of
relationships.

## Responsive composition

Do not shrink the desktop artboard. Re-prioritize:

1. preserve the dominant job;
2. retain required context and primary action;
3. move secondary evidence into disclosure or a later region;
4. change spatial relationships only when the narrower format requires it;
5. keep the visual thesis recognizable through silhouette, type, and signature
   behavior.
