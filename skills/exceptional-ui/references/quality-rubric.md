# Quality rubric

Score the rendered design, not the intention or the effort. Use:

- **0 — absent/broken**
- **1 — weak or misleading**
- **2 — competent but ordinary**
- **3 — strong, intentional, product-specific**
- **4 — exceptional, resolved, memorable without harming use**

Do not average the four primary gates together. Each gate must pass
independently.

## Gate A: Design quality

Score each dimension:

| Dimension | Evidence of 3–4 quality |
|---|---|
| Product fit | Dominant content/action directly serves the user's real decision |
| Composition | Recognizable silhouette, clear dominant mass, deliberate scan path |
| Information hierarchy | Importance survives greyscale, blur, and reduced scale |
| Density rhythm | Sparse and dense zones match orientation, action, and evidence |
| Typography | Roles are coherent, readable, content-tested, and expressive |
| Color/material | Semantic, accessible, restrained, and clear about surface ownership |
| Interaction clarity | Selection, focus, state, disclosure, and action priority are visible |
| Responsive priority | Narrow/wide composition preserves the primary job |

**Pass:** no dimension below 2; product fit, composition, hierarchy, and
interaction clarity are at least 3; the overall result is not being rescued by
surface polish.

## Gate B: Implementation correctness

Check:

- intended frame/viewports exist and render;
- no unintended clipping, overflow, collision, or off-canvas content;
- auto-layout, constraints, HUG/FILL/FIXED, and bounds match the intended
  behavior;
- text uses the intended fonts and production-length content;
- image/vector assets are present and correctly cropped;
- component properties and variants visibly produce the intended states;
- interaction targets, focus, and state cues are plausible;
- light/dark or responsive expressions do not regress;
- no empty export, detached placeholder, accidental duplicate, or stale target
  is presented as finished.

**Pass:** every critical item works; remaining imperfections are visual polish,
not structural defects. A clean render alone is not proof—inspect the pixels
and relevant node structure.

## Gate C: Design-system consistency

Check:

- existing variables/styles/components were inspected before creation;
- reused instances remain attached and use their public properties;
- fills, strokes, spacing, radius, typography, and effects are bound where
  tokens exist;
- new foundations represent recurring semantic roles;
- new components add a genuine missing pattern/state and fit naming/anatomy;
- component states and semantic colors remain consistent across screens;
- the design extends the system rather than creating a parallel mini-system.

**Pass:** reuse is deliberate and visible; any extension has a documented role
and can support more than the one composition.

## Gate D: Visual distinctiveness

Score:

| Dimension | Evidence of 3–4 quality |
|---|---|
| Visual thesis | The product has a specific formal idea, not adjectives |
| Signature moves | Two or three meaningful devices recur coherently |
| Product specificity | Content relationships and interaction shape the UI |
| Memorability | Thumbnail/silhouette is recognizable |
| Reference distance | Principles are visible without tracing a source layout |
| Restraint | Distinction comes from controlled choices, not novelty everywhere |
| Family coherence | Sibling screens vary by task but retain the same formal grammar |

**Pass:** visual thesis, product specificity, reference distance, and family
coherence are at least 3; at least one signature move reaches 4; the design
remains distinctive in greyscale and passes the logo-swap test.

## Critical failure overrides

The design fails regardless of score when:

- it misrepresents the product or a safety/financial/medical state;
- primary content or actions are inaccessible;
- it copies a reference composition or protected asset without authorization;
- it relies on fake/decorative data as operational truth;
- it diverges from the design system without reason;
- it was not visually inspected after rendering.

## Review record

Use this compact form after every render:

```markdown
Render:
Direction:

Gate A — Design quality: __/4
Evidence:

Gate B — Implementation correctness: __/4
Evidence:

Gate C — Design-system consistency: __/4
Evidence:

Gate D — Visual distinctiveness: __/4
Evidence:

Critical failures:
Top three fixes:
Decision: iterate | blocked | pass
```

A “2” is acceptable production utility, not exceptional UI. Iterate when any
primary gate is below 3.
