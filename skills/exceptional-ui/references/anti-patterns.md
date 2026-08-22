# Anti-patterns

Read this before the first critique. Detect the underlying design habit, then
apply the correction; do not merely restyle the symptom.

| Smell | Why it fails | Corrective move |
|---|---|---|
| Sidebar + top bar + four KPI cards + chart + table | Default dashboard grammar says nothing about the product | Start from the user's decision and dominant object; compose around its evidence and actions |
| Equal cards for unequal information | Flattens priority and relationships | Vary span, depth, continuity, and density according to purpose |
| “Bento” as a mosaic of unrelated rounded boxes | Visual trend without information architecture | Share axes, baselines, flows, or a dominant instrument across modules |
| One rounded rectangle per concept | Categories replace user flow | Combine related content into a continuous work surface or relationship view |
| Oversized greeting or welcome header | Consumes prime space without helping a recurring task | Show current scope, decisive state, and next action compactly |
| Generic gradient blobs behind cards | Adds trend cues but no ownership or meaning | Establish silhouette and hierarchy; use atmosphere only when it supports the direction |
| Glass everywhere | Reduces contrast and makes every surface appear temporary | Limit translucency to chrome, overlays, or selected floating layers |
| All cards elevated equally | No surface hierarchy | Keep persistent surfaces low relief; elevate selection and temporary controls |
| Universal pill shapes | Makes content containers and actions indistinguishable | Reserve pills for compact tokens, filters, or segmented control behavior |
| One radius at every scale | Removes material hierarchy | Use a role-based radius ladder; contrast enclosure with exact inner geometry |
| Every label semibold | Weight no longer communicates hierarchy | Restore weight contrast; use position, size, and whitespace |
| Tiny grey text as sophistication | Sacrifices legibility for aesthetic restraint | Increase contrast/size and reduce content instead |
| Decorative chart | Data exists only to fill a card | Name the question, units, scale, selected datum, and action; otherwise remove it |
| Decorative topology or connector lines | Pretends complexity without explaining it | Encode direction, dependency, grouping, selection, and degraded state |
| Random category colors | Creates visual noise and unstable meaning | Use semantic roles and a controlled accent budget |
| Dark neon “command center” skin | Theatrical style substitutes for product specificity | Derive dark mode from the same semantic system and real task needs |
| Marketing hero inside an operational product | Tone and density do not match repeated work | Move storytelling to onboarding/focus mode; keep routine surfaces task-first |
| Placeholder metrics and lorem ipsum | Hides real content pressure and produces implausible layouts | Use realistic names, values, errors, long labels, and edge states early |
| Generic avatars and stock people | Adds false social proof or irrelevant personality | Use real actors/assets or omit them |
| Copied reference layout with relabeled content | Imports another product's hierarchy and interaction assumptions | Extract principles, rebuild from the current product model, and change composition where purpose differs |
| New components for visual novelty | Fragments the design system | First compose existing components differently; extend only a recurring missing behavior |
| Perfectly safe symmetry | Feels templated and removes focal tension | Introduce deliberate dominance, controlled asymmetry, crop, continuation, or scale contrast |
| Novelty everywhere | Produces incoherent generated spectacle | Keep a small motif budget and repeat signature moves with meaning |

## Generic-AI warning signs

Stop and reconsider the direction if several are true:

- the design could accept any SaaS logo without changing;
- every screen starts with the same KPI row;
- the content is organized by noun categories rather than user decisions;
- visual interest comes mainly from gradients, glows, floating cards, or icons;
- cards have title/value/trend metadata but no inspectable instrument;
- all modules use the same width, height, radius, and padding;
- there is no dominant object or relationship;
- the screenshot looks polished only at full color, not in greyscale;
- references are visible in details but the product itself is not;
- realistic long content would break the composition.

When detected, return to product purpose, visual thesis, and composition. Do
not solve these with another polish pass.
