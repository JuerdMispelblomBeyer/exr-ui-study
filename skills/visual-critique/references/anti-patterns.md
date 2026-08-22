# Anti-patterns

Detect the underlying design habit, not just the surface symptom. For each
detected pattern, cite the visible region, explain the consequence, prescribe a
structural correction, and state the desired visual outcome.

## Aggressive detection table

| Pattern | Visible evidence | Why it fails | Corrective direction | Desired outcome |
|---|---|---|---|---|
| Excessive cards | Nearly every concept has its own rounded box; relationships stop at card edges | Categories replace flow and all objects appear independent | Merge related evidence into continuous surfaces, shared axes, paths, or tables | Relationships dominate containers |
| Repetitive sections | Every view repeats title → KPI row → cards → table | Product tasks become relabeled templates | Recompose each view around its actual primary object/decision | Sibling screens share grammar but have distinct silhouettes |
| Generic SaaS aesthetic | Sidebar, greeting, four metrics, gradient chart, recent-activity table | Layout communicates market category, not product purpose | Start from the user's decision and product-specific evidence | Interface could not plausibly belong to an unrelated SaaS tool |
| Excessive rounded rectangles | One radius and enclosure is used for content, controls, charts, and tags | Material hierarchy and affordance disappear | Reserve enclosure by role; contrast outer chassis with exact inner geometry | Shape communicates ownership and behavior |
| Unnecessary gradients | Color transitions sit behind content without encoding light, focus, depth, or data | Trend decoration competes with evidence | Flatten or tie gradient to a specific spatial/semantic role | Atmosphere supports, never substitutes for, hierarchy |
| Weak typography | Small grey labels, semibold everywhere, generic display headings | Information levels merge and content feels machine-generated | Rebuild role contrast and content-test real labels/values | Type alone establishes a clear read order |
| Uniform visual weight | Cards, controls, values, and chrome share similar contrast/size | Nothing wins; scanning becomes labor | Concentrate scale, contrast, and density at the primary state/object | One dominant read with quiet support |
| Excessive symmetry | Equal columns and mirrored masses are used without comparison logic | Priority and directional flow vanish | Introduce controlled dominance/asymmetry at the core relationship | Layout expresses direction or importance |
| Arbitrary decoration | Floating shapes, lines, glows, or icons have no semantic role | Visual novelty feels generated and distracts from product truth | Remove or assign each device a recurring meaning | Every flourish earns its place |
| Insufficient focal hierarchy | Several regions attract attention equally or the title wins over the task | User must consciously search for the current state/action | Reallocate area, contrast, position, density, and depth | Intended first read is immediate |
| Poor whitespace | Large unused zones coexist with locally cramped controls/content | Space does not express relationships and viewport economy suffers | Reassign whitespace by grouping tier and decision value | Dense areas remain readable; empty areas create focus |
| Meaningless borders | Every surface has a stroke regardless of ownership or interaction | The screen becomes visually noisy and depth depends on outlines | Remove redundant strokes; use surface contrast and role-based edges | Boundaries appear only where they explain separation/state |
| Excessive accent colors | Brand, category, series, status, and decoration all use saturated hues | Semantic authority fragments | Set a lead accent budget and a restrained status/comparison palette | Color directs a single attention path |
| Template-like layout | Components can be rearranged or relabeled without changing meaning | Composition is not shaped by the product | Make relationships, state, and manipulation determine the spatial model | Layout becomes product-specific |
| Polished anonymity | Alignment, tokens, and components are correct but no visual thesis is memorable | Professional finish hides the absence of direction | Recompose around a product relationship and define meaningful signature moves | Coherence plus recognizable character |
| Bento mosaic | Mixed-size cards create variety but lack a dominant object or shared logic | Trend composition masquerades as information architecture | Establish one organizing instrument/relationship; subordinate the mosaic | Varied spans support a clear argument |
| Glass everywhere | Persistent surfaces are translucent and equally elevated | Contrast weakens and all content looks temporary | Limit glass to navigation, overlays, or selected floating layers | Material state explains persistence and ownership |
| Decorative chart/topology | Visualizations have no question, units, scale, selection, direction, or action | Fake evidence consumes attention and undermines trust | Add operational semantics and interaction or remove the visual | Every visualization helps decide or diagnose |
| Stock/placeholder content | Lorem ipsum, round numbers, generic avatars, or invented happy-path metrics | Real content pressure and product identity are hidden | Use realistic names, values, errors, long labels, and edge states | Content visibly belongs to the product |
| Copied reference layout | Source composition and proprietary devices survive with labels swapped | Imports another product's hierarchy and risks imitation | Extract principles; rebuild from current product model | Reference influence is felt but not traceable |

## Genericity/AI-design assessment

Report one severity: `Low`, `Moderate`, `High`, or `Critical`.

Include:

1. patterns detected and their locations;
2. whether the logo-swap test succeeds;
3. whether sibling screens repeat one template;
4. whether visual interest comes from product relationships or decoration;
5. whether realistic content would strengthen or break the layout;
6. the structural change most likely to reduce genericity.

Do not write “slightly generic.” State what makes it generic. High or Critical
severity forces `ITERATE`, regardless of polish or consistency.

## Stop polishing when

- the wrong object dominates;
- all content is enclosed in interchangeable cards;
- hierarchy disappears in greyscale;
- the logo-swap test succeeds;
- the layout is still a copied/reference-shaped composition;
- decorative visuals have no operational meaning.

Return to composition, product model, and visual thesis before adjusting
shadows, radii, icons, or micro-spacing.

