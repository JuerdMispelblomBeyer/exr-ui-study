# Visual-reference intake and style-system method

## Purpose

Inspiration should make the ExRobotics visual identity more coherent and
reproducible. It must not turn the project into a collection of unrelated
screens or copied trends.

Every supplied site, shot, application, or image moves through this chain:

> source evidence → visual grammar → ExRobotics translation → reusable rule →
> component/token/test → Figma application

Figma is the last step. A reference does not authorize an immediate redesign.

## 1. Preserve provenance

For each reference:

- preserve the original image without cropping, annotation, or recompression;
- record the exact source URL, author/studio when verified, date added, and
  access status;
- record original asset URLs when local capture is blocked;
- distinguish direct observation from page copy, metadata, inference, and
  unavailable information;
- never substitute a visually similar search result for an inaccessible source;
- treat external work as inspiration, not an asset library.

Use one subdirectory and `SOURCE.md` for a web case study. A blocked or
unavailable source remains explicitly queued until a verified capture exists.

## 2. Analyse without color first

Inspect each source through nine lenses before considering its palette:

1. **Silhouette** — the recognizable outer composition.
2. **Hierarchy** — scan order, dominant object, supporting layers.
3. **Grid and density** — spans, alignment, information rhythm, negative space.
4. **Geometry** — radius ladder, strokes, corners, shapes, connector paths.
5. **Depth and material** — opaque/translucent ownership, inset/raised states,
   shadow and blur behavior.
6. **Typography** — roles, scale contrast, numeric/data treatment, line length.
7. **Instrumentation** — how charts, diagrams, values, tables, or hardware are
   made inspectable.
8. **Interaction evidence** — focus, selection, current state, disclosure,
   action placement, motion.
9. **Brand-to-product continuity** — repeated formal devices across identity,
   shell, components, diagrams, imagery, and presentation.

Color is assessed separately and is never sampled into tokens by default.
ExRobotics yellow and the established neutral/semantic system remain the
authority.

## 3. Classify every observation

Each observation receives one of four dispositions:

- **Adopt** — useful without changing its meaning.
- **Translate** — valuable structure that must be recast for ExRobotics.
- **Presentation-only** — suitable for onboarding, brand material, focus mode,
  or documentation, but not routine operations.
- **Reject** — conflicts with platform truth, accessibility, task flow,
  information density, or product scope.

Fleet, mission, mapping, route, dispatch, and autonomy content is rejected even
when the source's visual treatment is useful. Extract form and interaction
logic, not the source product model.

## 4. Synthesize across sources

Do not let one attractive reference override the system. Promote a pattern
only when it does at least one of the following:

- appears consistently across multiple strong references;
- solves a documented ExRobotics task or cognitive-ergonomics problem;
- strengthens an existing Signal Instrumentation signature;
- creates a missing but clearly bounded layer, such as editorial focus.

Resolve conflicts explicitly. For example, spacious case-study composition can
govern focus mode while dense aligned instrumentation governs the operational
workbench. Both can share typography, edges, yellow semantics, and component
anatomy.

## 5. Turn inspiration into a system

A promoted visual principle is incomplete until it has concrete outputs:

| Level | Required output |
|---|---|
| Principle | One sentence explaining the intended cognitive or brand effect |
| Layout | Grid, spans, alignment, density, and responsive behavior |
| Component | Anatomy, variants, states, ownership, and content limits |
| Token | Reusable values only when repetition justifies them |
| Interaction | Selection, focus, disclosure, motion, and failure behavior |
| Accessibility | Contrast, non-color meaning, target size, keyboard/focus rules |
| Acceptance | A test that can reject a superficially similar implementation |

Avoid creating tokens for one-off decoration. Avoid creating components before
their role and state model are known.

## 6. Brand-system continuity matrix

Use this matrix to learn from references that combine brand and product design:

| Formal device | Brand identity | Product UI | Diagrams/data | Presentation |
|---|---|---|---|---|
| ExRobotics yellow | signature accent | active/current/action | selected path/datum | focal signal |
| Chassis silhouette | framing motif | application shell | system boundary | case-study stage |
| Hairline + inset edge | graphic precision | surface ownership | node/module boundary | callout plate |
| Mono metadata | technical voice | IDs, units, time | rates, ports, topics | captions/spec labels |
| Focus brackets | capture/inspection motif | keyboard/selected scope | probed node/region | annotated detail |
| Mixed bento spans | modular identity | diagnostic workbench | comparative instruments | overview board |

The same device must retain compatible meaning across contexts. A brand motif
that becomes misleading as an operational control is not continuous identity.

## 7. Figma promotion gate

Before applying a new reference-derived direction in Figma, confirm:

1. The source is visually verified and provenance is recorded.
2. Observations are separated from inference.
3. Adopt/translate/presentation/reject decisions are documented.
4. The change supports platform introspection rather than excluded product
   domains.
5. Existing components and tokens were checked before adding new ones.
6. Light and dark expressions remain one system.
7. ExRobotics yellow keeps its active-signal meaning.
8. Operational density and accessibility survive the styling.
9. The new rule has a falsifiable acceptance test.
10. Previous Figma versions will be preserved through archive-safe siblings.

## 8. Reference-review template

Use these headings for each verified source:

1. Provenance and capture status
2. Source intent and product context
3. Composition and silhouette
4. Grid, density, and negative space
5. Geometry, material, and depth
6. Typography and data treatment
7. Interaction and motion evidence
8. Brand-to-product continuity
9. Adopt for ExRobotics
10. Translate rather than copy
11. Presentation-only patterns
12. Reject
13. Candidate component/token changes
14. Acceptance tests

This creates a durable visual-design memory that future agents can apply
without needing to rediscover the original reasoning.
