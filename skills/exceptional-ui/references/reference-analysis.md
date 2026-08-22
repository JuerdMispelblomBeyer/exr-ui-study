# Reference analysis

Use references to discover transferable principles, not to outsource design
decisions.

## 1. Establish evidence

For each source record:

- exact source and creator when known;
- whether it is an original screenshot, case-study composition, device mockup,
  photograph, animation, or inferred/partial capture;
- what was directly observed versus described by page text;
- product context and likely user;
- access, licensing, and reuse limits.

Direct UI screenshots are strongest for interface analysis. Device mockups and
editorial compositions may inform presentation, depth, or storytelling but
must be marked presentation-only so an agent does not treat the hardware frame
as interface structure.

## 2. Analyze through ten lenses

Do not begin with color.

1. **Silhouette** — outer composition recognizable at thumbnail size.
2. **Hierarchy** — dominant object and scan sequence.
3. **Grid** — columns, spans, alignment, continuation, asymmetry.
4. **Density** — sparse/dense rhythm and negative-space ownership.
5. **Geometry** — radius ladder, shapes, crops, lines, connectors.
6. **Depth/material** — persistent, inset, selected, floating, temporary layers.
7. **Typography** — roles, contrast, line length, numeric/data handling.
8. **Imagery/instrumentation** — how images, charts, diagrams, tables, or data
   become inspectable.
9. **Interaction evidence** — selection, focus, disclosure, manipulation,
   current state, motion.
10. **Brand-product continuity** — formal devices repeated across shell,
    component, data, imagery, and presentation.

Then analyze color by role: accent allocation, surface values, semantics,
contrast, and theme behavior. Never sample a palette into the target system by
default.

## 3. Classify observations

- **Adopt** — useful without changing meaning.
- **Translate** — structurally valuable but must be recast for the target
  product, content, user, or design system.
- **Presentation-only** — useful for storytelling, onboarding, focus mode, or
  identity work but unsuitable for routine UI.
- **Reject** — decorative, misleading, inaccessible, off-scope, trend-only, or
  incompatible with the target system.

Most valuable observations should be translated, not adopted literally.

## 4. Convert observation into an operational principle

Use:

| Field | Required content |
|---|---|
| Evidence | What is visibly present in the source |
| Effect | Why it changes hierarchy, comprehension, tone, or interaction |
| Target need | Which current user job/problem it supports |
| Translation | How it changes for the target product/system |
| Do not copy | Which source-specific layout/content/device must remain behind |
| Implementation consequence | Composition, component, token, imagery, or state work |
| Acceptance test | What would reject a superficial imitation |

Example:

- Evidence: one large topology field with an attached narrow inspector.
- Effect: relationship stays visible while one node gains detail.
- Target need: diagnose a selected dependency without losing context.
- Translation: use the target system's node shapes, data, and inspector
  component.
- Do not copy: source node positions, palette, labels, or exact proportions.
- Acceptance: selecting any node preserves topology context and shows truthful
  object-specific evidence.

## 5. Synthesize across sources

Create a matrix of recurring principles. Promote a principle only when it:

- appears across several strong references;
- solves a documented target problem;
- strengthens an existing product/brand signature; or
- defines a clearly bounded presentation or interaction layer.

Resolve conflicts by context. A spacious editorial reference may govern focus
mode while a dense operational reference governs routine work. They can still
share typography, edge grammar, and accent semantics.

## 6. Prevent copying

Run these tests before building:

1. **Source-hidden test:** hide the images and describe the direction entirely
   through target-product principles.
2. **Structure test:** rebuild the information architecture from the target
   user's flow. If it matches the source despite different product needs,
   investigate copying.
3. **Content substitution test:** source-specific labels or objects must not
   remain as placeholders.
4. **Distance test:** retain effects (hierarchy, attachment, density rhythm)
   while changing source-specific proportions, geometry, assets, and layout.
5. **Multi-source test:** no one source should determine the entire screen.

## 7. Reference-analysis output

Before design direction, produce:

```markdown
Reference set:
Shared visual principles:
Product-relevant translations:
Presentation-only ideas:
Rejected patterns:
Existing design-system elements that support the direction:
Missing reusable elements:
Anti-copy constraints:
```

This analysis feeds the direction brief. It is not itself permission to build.
