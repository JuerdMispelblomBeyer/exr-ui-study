# Anti-patterns: resisting generic generated UI

Use this reference before choosing a direction and again during every visual
critique. It is a diagnostic field guide, not a ban list. Cards, centered
layouts, gradients, symmetry, and component libraries are not inherently bad.
They fail when an agent uses them without a product-specific reason.

Genericity is a **correspondence failure**: the interface looks plausible, but
its composition, hierarchy, content, and visual language do not correspond to
the product's actual user, task, objects, risks, or behavior. A substitution
test exposes it: if changing only the nouns turns the same screen into a CRM,
finance dashboard, project manager, or health app, the design is describing a
software category rather than this product.

Research supports treating this as a systemic generator problem rather than a
matter of taste. A 2026 benchmark of 120 generated interfaces found convergence
in visual appearance and layout across tools, while stated design rationale
often failed to appear in the result ([Design Theater](https://arxiv.org/abs/2607.22928)).
Practitioner analyses repeatedly identify centered heroes, identical card
grids, glass/gradient styling, placeholder content, missing states, and
component-library defaults as common fallback behavior
([SmoothUI](https://smoothui.dev/blog/ai-design-slop),
[v-1.design](https://v-1.design/blog/why-ai-built-apps-look-the-same),
[Built In](https://builtin.com/articles/ai-design-slop-era)). These sources are
evidence inputs, not style authorities; the operational rules below are the
skill's synthesis.

## Token-efficient detection index

Read this index for every direction/critique. Open the matching full entry only
when the trigger is visible or plausible. Cite the stable ID in the run packet.

| ID | Pattern | Fast visual trigger |
|---|---|---|
| AP01 | Card soup | Nearly every idea is an independent rounded box |
| AP02 | Excessive rounded rectangles | One radius/enclosure language covers surfaces and controls |
| AP03 | Generic SaaS dashboard | Sidebar + KPI row + chart + activity/table survives noun swap |
| AP04 | Centered-everything | Alignment avoids direction, relationship, and operational scan |
| AP05 | Uniform section rhythm | Every band repeats the same spacing/anatomy |
| AP06 | Three-column-by-default | Equal thirds appear without comparison logic |
| AP07 | Excessive symmetry | Mirrored/equal masses erase priority |
| AP08 | Equal visual weight | Nothing wins at thumbnail or squint scale |
| AP09 | Component-first composition | Component inventory determines layout before user decision |
| AP10 | Weak typography | Default roles, semibold texture, tiny secondary copy |
| AP11 | Excessive pills | Labels, states, filters, and actions all become capsules |
| AP12 | Icon-decoration overload | Icons repeat without improving recognition or action |
| AP13 | Arbitrary gradients | Gradient encodes no light, value, focus, depth, or image role |
| AP14 | Excessive shadows | Most persistent surfaces float equally |
| AP15 | Meaningless borders | Strokes outline everything without semantic separation |
| AP16 | Excessive accent color | Brand/category/status/action compete in saturated hues |
| AP17 | Hero-template syndrome | Eyebrow + centered headline + cards/CTA replaces product logic |
| AP18 | Placeholder-content design | Lorem, round metrics, generic users, happy-path data |
| AP19 | Fake visual complexity | Decorative charts/topology/lines have no operational question |
| AP20 | Consistency mistaken for quality | Token-perfect system remains compositionally anonymous |
| AP21 | Reference copying | Source structure/assets remain after label/color swap |
| AP22 | Design theater | Visual drama implies capability, state, or depth the product lacks |
| AP23 | Garnish rendered as information | Crosshairs, ticks, brackets, ghost grids sit at full contrast |
| AP24 | Outline-defined surfaces | Every surface is bounded by a visible stroke; light is never used |
| AP25 | Colour spent on the nominal case | The healthy, normal, expected state is the most colourful thing on screen |

High/Critical genericity forces `ITERATE`. If several triggers stem from one
cause, open and fix the highest-level entry first—usually AP03, AP08, AP09,
AP18, AP20, or AP21—rather than loading the entire catalogue.

## How to use this document

For each rendered viewport:

1. Find symptoms in the pixels, not only in the layer tree or rationale.
2. Identify the missing decision that caused the symptom.
3. Apply the smallest structural correction that restores product meaning.
4. Render the same viewport and confirm that hierarchy and distinctiveness
   visibly improved.
5. Do not “fix” a generic layout by adding decoration. Composition, content, and
   task correspondence come first.

## Composition failures

### 1. Card soup

**Description**
Every fact, metric, action, or section receives its own rounded container. The
page becomes a field of detached boxes instead of a coherent work surface.

**Why AI agents tend to produce it**
Cards are easy to generate, responsive, reusable, and safe with unknown content.
Component libraries make them the lowest-friction answer to every grouping
problem. Repeating one pattern also reduces implementation reasoning.

**Visual symptoms**

- Six or more similarly treated containers dominate the viewport.
- Every module has title → value/content → optional footer anatomy.
- Relationships are explained in text because the boxes do not show them.
- Gutters and card padding consume more area than the evidence.
- Removing any card does not change the composition of its neighbors.

**Why it hurts the design**
Cards flatten priority, hide continuity and causality, increase scanning cost,
and make unrelated products look interchangeable. Container boundaries compete
with the information they are supposed to organize.

**When it is actually appropriate**
For genuinely independent, movable, dismissible, or comparable objects—for
example products in a catalog, saved views, files, or a small set of entities
with the same interaction contract.

**Better alternatives**

- One dominant canvas, timeline, table, topology, queue, map, or editor.
- Joined surfaces with shared dividers and axes.
- Aligned lanes or small multiples for comparison.
- A compact summary strip plus one deeper evidence region.
- An attached inspector for selected detail.

**How a visual critic should detect it**
Count major standalone containers and test whether their order can be shuffled
without changing meaning. If most can move freely, report which relationship or
priority the composition fails to express and name the shared surface or
dominant object that should replace them.

### 2. Excessive rounded rectangles

**Description**
The same soft rectangle contains navigation, data, media, alerts, charts,
buttons, and even other rounded rectangles.

**Why AI agents tend to produce it**
Large radii are strongly associated with “modern” UI in templates and generated
examples. One radius token also guarantees easy consistency without requiring a
material or shape hierarchy.

**Visual symptoms**

- Nearly every visible object has 16–32 px corner rounding.
- Outer shells and inner controls use the same radius.
- Pills, cards, dialogs, and charts differ mainly by size.
- Nested corners do not step down as surfaces move inward.
- Technical or tabular content appears inside pillow-like containers.

**Why it hurts the design**
Shape stops communicating scale, ownership, interaction, or content type. The
result feels soft, template-like, and spatially imprecise.

**When it is actually appropriate**
For touch-oriented consumer surfaces, friendly content objects, media tiles, or
a product whose brand deliberately owns a soft shape language.

**Better alternatives**

- A radius ladder: soft chassis, moderate panels, exact internal geometry.
- Shared straight dividers for tables and dense instruments.
- Shape tied to behavior: pill for token, rectangle for field, bespoke geometry
  only for a meaningful object.
- Contrast between enclosing form and internal measurement marks.

**How a visual critic should detect it**
Compare the radii of the five largest and five smallest objects. If they express
no role difference, identify where sharper, joined, inset, or square geometry
would clarify function.

### 3. Generic SaaS dashboard

**Description**
The canonical fallback: sidebar, top header, greeting/page title, three or four
KPI cards, generic chart, recent-activity list, and table.

**Why AI agents tend to produce it**
“Dashboard” is often supplied as the product job. Training examples and UI kits
make this architecture statistically common and technically dependable. When
the brief does not identify the decisive task, the generator distributes weight
evenly among familiar modules.

**Visual symptoms**

- The first row is always KPI cards regardless of the page's purpose.
- A chart exists because dashboards “need a chart,” not to answer a question.
- Sidebar nouns define the product more than the workbench does.
- The same screen could become CRM, analytics, finance, or operations by
  relabeling sections.
- The highest-risk action or most important object is not visually dominant.

**Why it hurts the design**
It expresses software-category convention instead of user intent. The screen
may be usable but has weak hierarchy, poor differentiation, and an indirect
path from signal to decision.

**When it is actually appropriate**
For a broad administrative overview where users genuinely compare a stable set
of independent summaries before choosing a domain.

**Better alternatives**

- Start with the user's dominant question and primary object.
- Use a task-specific workbench: queue, editor, canvas, split comparison,
  topology, timeline, or dense table.
- Put summary metrics inside or beside the object they qualify.
- Compose around detect → locate → explain → act.

**How a visual critic should detect it**
Run the logo-and-noun swap test. Name the product-specific relationship or action
missing from the silhouette. If the screen remains intact after relabeling it as
another SaaS product, mark visual distinctiveness as failed.

### 4. Centered-everything

**Description**
Headlines, paragraphs, buttons, forms, empty states, illustrations, and section
content all align to a central axis.

**Why AI agents tend to produce it**
Centering handles unknown width, creates instant symmetry, and works for short
placeholder copy. It is a safe default for one-shot screenshots.

**Visual symptoms**

- Every section begins with a centered eyebrow, heading, and paragraph.
- Primary and supporting content stack vertically with no directional tension.
- Dense information is center-aligned despite needing comparison.
- The page lacks strong left/right anchors or edge relationships.
- Reading requires repeated re-acquisition of the central axis.

**Why it hurts the design**
Centering weakens scanning, comparison, and narrative direction. It removes
useful asymmetry and makes sections feel interchangeable.

**When it is actually appropriate**
For a singular decision, short confirmation, loading state, focused login, or
brief marketing statement where one object genuinely owns the viewport.

**Better alternatives**

- Left-align reading and data-heavy content.
- Use an asymmetric split between proposition and proof/action.
- Anchor related evidence to a dominant object or edge.
- Let imagery, typography, or a system model create a deliberate off-center
  focal point.

**How a visual critic should detect it**
Draw the viewport's major alignment axes. If nearly all content depends on one
centerline and no task requires it, specify which region should become the
dominant anchor and how the scan path should change.

### 5. Uniform section rhythm

**Description**
Every section repeats the same vertical padding, title placement, content width,
and module pattern.

**Why AI agents tend to produce it**
Generators often assemble pages from reusable section blocks. Token consistency
and code simplicity encourage a fixed `py-24` rhythm regardless of content.

**Visual symptoms**

- Each section follows eyebrow → heading → paragraph → three cards.
- Section heights are suspiciously similar.
- Sparse and dense content receive identical breathing room.
- There is no acceleration, pause, compression, or climax in the page.
- Scroll position does not change the visual or informational tempo.

**Why it hurts the design**
Uniform cadence flattens narrative and information hierarchy. Important moments
cannot feel important because the page gives every block the same ceremony.

**When it is actually appropriate**
For reference documentation, settings categories, or comparable repeated
records where predictability is the primary value.

**Better alternatives**

- Alternate sparse orientation with dense proof or interaction.
- Vary section depth by task and evidence volume.
- Use continuation, overlap, crop, or shared datum where content is related.
- Create one or two compositional peaks instead of many equal beats.

**How a visual critic should detect it**
Compare section silhouettes at thumbnail scale. If they form identical stripes,
identify the section that should dominate, the one that should compress, and
the relationship that should bridge sections.

### 6. Three-column-by-default

**Description**
Features, pricing, metrics, testimonials, and content modules automatically
become three equal columns.

**Why AI agents tend to produce it**
Three columns fill desktop width cleanly, collapse predictably on mobile, and
match common component examples. The pattern resolves layout without judging
importance.

**Visual symptoms**

- Unrelated content sets are forced into groups of three.
- Cards have equal width despite very different content or consequence.
- The middle column is centered by geometry rather than importance.
- A fourth item becomes an awkward second row or is omitted.
- Desktop composition simply collapses to a stack on narrow screens.

**Why it hurts the design**
It creates arbitrary taxonomy, equal visual weight, and a recognizable template
signature. Content is edited to fit the grid rather than the user's priorities.

**When it is actually appropriate**
When exactly three equivalent choices or objects must be compared on the same
dimensions.

**Better alternatives**

- One dominant item plus supporting details.
- Two-way comparison with a shared baseline.
- Horizontal sequence, ranked list, matrix, or variable-span grid.
- Let the number and size of regions emerge from content roles.

**How a visual critic should detect it**
Ask why there are exactly three items and why they are equal. If the answer is
“it fits,” require a composition based on rank, sequence, relationship, or
actual comparison dimensions.

### 7. Excessive symmetry

**Description**
The viewport is balanced so perfectly that no region creates tension,
direction, or priority.

**Why AI agents tend to produce it**
Symmetry is easy to validate computationally, looks orderly in a screenshot,
and avoids awkward whitespace. It is a reliable proxy for “polished.”

**Visual symptoms**

- Mirrored masses or equal columns dominate.
- The focal object sits exactly in the center by default.
- Negative space is distributed evenly rather than intentionally.
- Repeated objects all use identical scale and contrast.
- The screen feels static even when the task is urgent or directional.

**Why it hurts the design**
Perfect balance suppresses scan direction and consequence. It often makes
dynamic, investigative, or editorial work feel templated.

**When it is actually appropriate**
For direct comparisons, ceremonial/threshold moments, radial controls, or
systems where physical symmetry is itself meaningful.

**Better alternatives**

- Controlled asymmetry around one dominant object.
- Off-center focus balanced by denser supporting evidence.
- Unequal spans on a strict grid.
- Allow real state or content length to affect visual mass.

**How a visual critic should detect it**
Blur the screenshot and compare the largest masses. If they cancel one another
without a task-based reason, state which side/object should dominate and what
supporting region should recede.

### 8. Equal visual weight

**Description**
Everything is styled as if equally important: headings, cards, charts, actions,
states, and navigation all compete at similar contrast and scale.

**Why AI agents tend to produce it**
Component reuse applies identical anatomy and tokens. Without priority in the
brief, the model avoids making a “wrong” choice by emphasizing everything.

**Visual symptoms**

- Several modules win the five-second read simultaneously.
- Primary and secondary buttons have similar presence.
- All charts use saturated colors.
- Every card has the same title size, shadow, and border.
- Critical state is one badge among many.

**Why it hurts the design**
The user must reconstruct priority cognitively. High-risk signals and decisive
actions are slower to find, while the page feels noisy despite being orderly.

**When it is actually appropriate**
For a true gallery, inventory, or comparison set where items are intentionally
equivalent.

**Better alternatives**

- Define one first read, one second read, and a quiet remainder.
- Use span, placement, density, luminance, and type before accent color.
- Mute unselected series and subordinate chrome.
- Let consequence change visual weight.

**How a visual critic should detect it**
Use thumbnail, greyscale, and blur tests. If three or more regions still compete,
name the intended winner and specify which competing properties—scale,
contrast, elevation, saturation, or density—must be reduced.

### 9. Component-first composition

**Description**
The page is designed by selecting and arranging available components before
deciding the dominant object, user flow, or overall silhouette.

**Why AI agents tend to produce it**
Agents can enumerate components more easily than reason about composition.
Existing libraries reward reuse, and generator workflows often begin with code
or node construction instead of massing.

**Visual symptoms**

- The layer inventory is coherent but the page has no thesis.
- Every region fits a known component even when the content needs a new form.
- Layout decisions follow component dimensions.
- The screen is polished at 100% but anonymous at thumbnail size.
- Changing the component library would change the art direction completely.

**Why it hurts the design**
Components solve local consistency, not global hierarchy. The output becomes an
assembly rather than a composition.

**When it is actually appropriate**
For routine maintenance screens, CRUD utilities, or narrowly scoped extensions
whose composition is already established by a mature product shell.

**Better alternatives**

- Sketch two whole-viewport massing hypotheses first.
- Define dominant object, navigation ownership, focal path, and density rhythm.
- Reuse components inside the chosen composition.
- Extend the system only for a recurring missing behavior.

**How a visual critic should detect it**
Judge the screenshot at 15–20% scale. If the composition cannot be described
without naming components, identify the missing dominant mass or relationship
and require a structural pass before component polish.

## Typography and control failures

### 10. Weak typography

**Description**
Typography is treated as neutral labeling: one generic sans, small changes in
size, many medium weights, and little compositional presence.

**Why AI agents tend to produce it**
Default fonts are dependable, available, and easy to render. Agents avoid large
or unconventional type because wrapping and hierarchy become harder to control.

**Visual symptoms**

- Heading levels differ by only 2–4 px.
- Every label is semibold; weight no longer conveys importance.
- Tiny grey text is used as a proxy for sophistication.
- Numbers, metadata, narrative, and navigation share one voice.
- Line length, leading, and wrapping are unconsidered.

**Why it hurts the design**
The interface loses hierarchy, personality, and reading efficiency. Color and
containers must compensate for distinctions type should carry.

**When it is actually appropriate**
A deliberately quiet type system can suit dense expert tools—provided role,
alignment, contrast, and numeric treatment remain precise.

**Better alternatives**

- Define display/orientation, interface, and data roles.
- Use scale contrast intentionally; one large type object is stronger than many
  medium headings.
- Test real long labels, values, units, and errors.
- Use alignment and whitespace with weight, not weight everywhere.

**How a visual critic should detect it**
Temporarily ignore containers and color. If the reading order collapses, cite
the exact roles that are indistinguishable and specify changes in size, weight,
family, line length, alignment, or contrast.

### 11. Excessive pills

**Description**
Navigation items, statuses, filters, tags, tabs, buttons, counters, and labels
all become capsule shapes.

**Why AI agents tend to produce it**
Pills tolerate variable text length, look immediately interactive, and are
common in modern component libraries. They solve several states with one style.

**Visual symptoms**

- Rows of capsules appear in multiple regions.
- Static metadata looks clickable.
- Selected tabs, status badges, and primary buttons share geometry.
- Large content containers receive full rounding.
- The screen resembles a bag of tokens rather than a spatial hierarchy.

**Why it hurts the design**
Affordances become ambiguous and the interface looks soft, busy, and generated.
Pill outlines create visual noise around short text.

**When it is actually appropriate**
For short tags, compact filters, status tokens, segmented controls, removable
selections, or brief actions whose capsule affordance is established.

**Better alternatives**

- Plain text with alignment for metadata.
- Underline/edge/inset selection for navigation.
- Compact rectangular controls.
- Status glyph + label without a surrounding capsule.
- Reserve full radius for one defined token family.

**How a visual critic should detect it**
Count capsule families and ask whether each is interactive, stateful, or
token-like. Identify capsules whose border can be removed without losing
meaning; those are decorative containers.

### 12. Icon-decoration overload

**Description**
Every heading, card, feature, metric, and action receives an icon, often inside
its own colored square or circle.

**Why AI agents tend to produce it**
Icon libraries are easy to access and icons make sparse cards appear designed.
They also let the agent differentiate otherwise identical component anatomy.

**Visual symptoms**

- Repeated icon tile → title → description modules.
- Icons are semantically vague or interchangeable.
- Decorative icons are larger than the information they label.
- Multiple icon styles, stroke weights, or containers coexist.
- Removing icons reveals a weak composition underneath.

**Why it hurts the design**
Icons add false focal points, reduce density, and mask poor hierarchy. Generic
symbols create visual noise without improving recognition.

**When it is actually appropriate**
For stable global navigation, quick-recognition actions, object types, or
critical semantic states with text redundancy.

**Better alternatives**

- Use type, data marks, imagery, or real object silhouettes as anchors.
- Apply icons only where recognition is faster than reading.
- Maintain one icon language and optical size system.
- Remove icon containers unless surface/state requires them.

**How a visual critic should detect it**
Hide icons mentally. If the page loses all hierarchy, the icons are compensating
for weak composition. Flag any icon that cannot be named accurately without its
label or that repeats the adjacent word without adding recognition.

## Color and surface failures

### 13. Arbitrary gradients

**Description**
Purple-blue, cyan-pink, aurora, mesh, or pastel gradients appear because they
signal “modern technology,” not because they encode atmosphere, hierarchy, or
state.

**Why AI agents tend to produce it**
Gradients create immediate visual richness from minimal structure and are common
in portfolio imagery and AI-tool branding. They make a screenshot look finished
before composition is resolved.

**Visual symptoms**

- A vivid gradient blob sits behind a hero or dashboard chassis.
- Each card has a different pastel wash.
- Text contrast changes unpredictably across a surface.
- Gradients do not correspond to depth, light source, data, or state.
- Turning gradients off reveals an ordinary layout.

**Why it hurts the design**
Arbitrary gradients compete with content, weaken semantics and accessibility,
and make unrelated products share the same aesthetic.

**When it is actually appropriate**
For a controlled brand atmosphere, spatial depth, continuous scale, lighting
model, image scrim, or state transition with a defined meaning.

**Better alternatives**

- Establish silhouette, type, and surface hierarchy first.
- Use a flat or tonal field with localized contrast.
- Limit gradients to one large atmospheric role or one meaningful signal.
- Derive stops from brand tokens and validate contrast across the full field.

**How a visual critic should detect it**
Ask what variable the gradient encodes and whether the screen survives without
it. If there is no answer, request its removal and a hierarchy fix using scale,
position, tone, or real imagery.

### 14. Excessive shadows

**Description**
Most containers float through broad, blurred shadows, often with different
recipes or colored glows.

**Why AI agents tend to produce it**
Shadows separate components quickly and create perceived polish without solving
surface ownership. Template examples often use them by default.

**Visual symptoms**

- Persistent cards appear to hover independently.
- Shadow blur exceeds the gutters between objects.
- Several elevation levels exist without interaction meaning.
- Dark mode uses colored glow as a substitute for edge definition.
- Nested shadows create muddy halos.

**Why it hurts the design**
The page loses material logic; every object feels temporary or clickable.
Shadows reduce crispness, compete with spacing, and exaggerate card soup.

**When it is actually appropriate**
For overlays, menus, dragged objects, floating inspectors, dialogs, or a
deliberately tactile object whose elevation communicates ownership.

**Better alternatives**

- Fine borders, inner contours, tonal steps, and shared dividers.
- One explicit elevation ladder tied to interaction state.
- Flat/inset persistent work surfaces.
- Local occlusion only where layers truly overlap.

**How a visual critic should detect it**
Map each shadow to a semantic layer. If persistent siblings all float at the
same elevation, identify which should be joined/inset and which rare object is
allowed to remain raised.

### 15. Meaningless borders

**Description**
Outlines are added around every object as a default separator, not to express
grouping, focus, state, or interaction.

**Why AI agents tend to produce it**
One-pixel borders are a safe alternative to shadows and help generated layouts
survive uncertain backgrounds. Agents apply them universally through component
tokens.

**Visual symptoms**

- Cards, rows, pills, buttons, tables, and plots all have similar outlines.
- Adjacent borders double into dark seams.
- Borders repeat spacing relationships already clear from alignment.
- Focus, selection, and normal containment use nearly identical strokes.
- Removing outlines makes the hierarchy collapse.

**Why it hurts the design**
Meaningless edges create visual chatter and fragment related information. They
also leave no distinct border treatment for focus or critical state.

**When it is actually appropriate**
For form fields, focus rings, selected regions, exact table rules, bounded
interactive objects, or surfaces needing contrast against variable content.

**Better alternatives**

- Group through proximity, shared background, alignment, or a single divider.
- Use internal rules rather than full boxes.
- Assign distinct edge grammar to containment, focus, and semantic state.
- Remove redundant nested outlines.

**How a visual critic should detect it**
Trace every closed outline and ask what boundary it communicates. Flag borders
whose removal does not change grouping or affordance, and specify whether space,
tone, or one shared divider should replace them.

### 16. Excessive accent color

**Description**
The brand or accent hue appears on headings, icons, buttons, links, badges,
charts, selected navigation, card backgrounds, and decoration simultaneously.

**Why AI agents tend to produce it**
Applying a supplied brand color everywhere is an easy way to make a generic
layout look “branded.” It also supplies hierarchy that the composition lacks.

**Visual symptoms**

- Multiple unrelated elements compete in the same saturated hue.
- Primary action, selection, and status share color.
- Every chart uses the accent as its main series.
- The screen becomes structureless in greyscale.
- Brand color occupies large areas without a defined role.

**Why it hurts the design**
Accent loses signaling power, semantic meanings collide, and users cannot tell
what is current, actionable, or merely branded.

**When it is actually appropriate**
A campaign, immersive brand moment, or intentionally monochromatic art
direction may use a dominant hue—provided state and action remain accessible.

**Better alternatives**

- Write an accent budget and priority order.
- Use neutrals for structure and accent for one coherent current context.
- Separate brand, interaction, and semantic state roles.
- Ensure hierarchy survives a yellow-off/greyscale test.

**How a visual critic should detect it**
Mark every accent-colored region and group them by meaning. If one hue carries
three or more unrelated roles, require role separation and reduction of the
least consequential uses.

## Marketing-template failures

### 17. Hero-template syndrome

**Description**
A page defaults to eyebrow badge, enormous centered headline, vague supporting
copy, two CTAs, gradient glow, and product screenshot—regardless of product,
audience, or page purpose.

**Why AI agents tend to produce it**
This block is abundant in landing-page examples and converts vague prompts into
a complete above-the-fold composition with little product knowledge.

**Visual symptoms**

- Headline could belong to any software company.
- Copy uses abstract promises such as “unlock,” “streamline,” or “reimagine.”
- Product proof sits below the fold or inside a generic browser mockup.
- Internal applications contain a marketing hero above routine work.
- Primary space is spent on slogan rather than object, evidence, or action.

**Why it hurts the design**
It delays substance, weakens credibility, wastes recurring workspace, and makes
brand voice interchangeable.

**When it is actually appropriate**
For a focused marketing landing page with one proposition, credible proof, a
clear audience, and a real conversion goal; or a sparse onboarding threshold.

**Better alternatives**

- Lead with concrete product evidence or an interactive demonstration.
- Use asymmetric proposition/proof composition.
- In products, replace hero copy with compact context and the primary work
  surface.
- Write claims that reference real capability, constraint, or outcome.

**How a visual critic should detect it**
Read only the hero and ask which product it belongs to. Then measure how much of
the initial viewport performs recurring work. If substance is delayed, specify
which real object or proof should replace the template block.

## Content and evidence failures

### 18. Placeholder-content design

**Description**
Layout is optimized around lorem ipsum, “Metric 1,” round numbers, short names,
generic avatars, and perfect happy-path states.

**Why AI agents tend to produce it**
Real content requires domain knowledge and creates difficult wrapping, density,
missing-data, and state problems. Placeholder strings keep generated components
visually stable.

**Visual symptoms**

- Labels are uniformly short and values suspiciously tidy.
- Tables have no long identifiers, missing values, warnings, or permissions.
- Charts show smooth decorative data with no units or source.
- Empty/error/loading states are absent or generic.
- Copy sounds polished but names no real actor, object, or consequence.

**Why it hurts the design**
Placeholders hide information architecture, sizing, priority, credibility, and
edge-state failures. The resulting design breaks when real data arrives.

**When it is actually appropriate**
Only in very early massing where content is explicitly unknown and the next pass
is guaranteed to use production-shaped examples.

**Better alternatives**

- Use realistic names, ranges, units, timestamps, errors, permissions, and long
  labels from the product model.
- Include stale, unknown, empty, degraded, and partial states.
- Label synthetic values as sample/illustrative.
- Let real content determine column widths and hierarchy.

**How a visual critic should detect it**
Replace one short label with a plausible long one, one number with missing data,
and one healthy state with a consequential error. If the composition fails or
the hierarchy stays unchanged, flag placeholder-shaped design.

### 19. Fake visual complexity

**Description**
Charts, topology lines, grid overlays, glows, tiny labels, technical glyphs, and
motion create the appearance of a sophisticated system without encoding useful
information.

**Why AI agents tend to produce it**
Technical decoration supplies instant domain mood and fills empty surfaces.
Static references show the appearance of complex tools but not their data model
or behavior, encouraging imitation.

**Visual symptoms**

- Charts have no question, unit, source, threshold, or selected datum.
- Connector lines do not encode direction or relationship type.
- Tiny random numbers simulate telemetry.
- Animated particles imply flow without measurement.
- A graph-paper grid or reticle exists only to look technical.

**Why it hurts the design**
It damages trust, creates false precision, and increases cognitive load. In
operational contexts it can imply causality or system state that is not true.

**When it is actually appropriate**
Abstract data-inspired imagery is acceptable in brand/marketing contexts when
clearly presented as illustration rather than operational evidence.

**Better alternatives**

- Every visual instrument answers a named question.
- Expose unit, source, time window, freshness, uncertainty, and selection.
- Use truthful diagrams with a limited relationship vocabulary.
- Remove marks that do not change interpretation or interaction.

**How a visual critic should detect it**
Ask the designer to explain what each major mark encodes and what user decision
it supports. Any answer based on mood—“adds depth,” “feels technical,” “creates
interest”—is evidence of fake complexity.

### 23. Garnish rendered as information

**Description**
Technical decoration — corner brackets, tick stubs, crosshairs, reticles, ghost
grids, connector dots — is drawn at the same contrast as real data.

**Why AI agents tend to produce it**
The motifs are copied from reference imagery where they sit at three to eight
per cent opacity and function as texture. Reproduced at full strength they look
like precision, and an agent has no way to feel the difference between texture
and signal.

**Visual symptoms**

- Brackets frame a selected object that is already outlined and tinted.
- Every lane, bar, or axis repeats the same tick mark.
- Dashed leaders point at things that need no pointing.
- Squinting, the decoration competes with the values it surrounds.

**Why it hurts the design**
The viewer spends attention decoding marks that carry nothing, and the real
signal loses the contrast budget the decoration consumed.

**Correct alternative**
There is no useful middle setting. Either drop the mark to roughly five per cent
so it reads as material, or delete it. When a selection needs emphasis, an
outline plus a tint plus a soft falloff carries it without any bracket.

**Test**
Cover the data. If the remaining marks still look like a diagram, they are too
loud.

### 24. Outline-defined surfaces

**Description**
Every plane, card, and stage is separated from its ground by a visible one-pixel
stroke. Gradient, inner highlight, and shadow do no work.

**Why AI agents tend to produce it**
A stroke is deterministic and easy to specify; light is not. Borders also read
as correct in code review, where a design's material quality is invisible.

**Visual symptoms**

- The screen reads as a wireframe at thumbnail scale despite finished content.
- Nested surfaces produce three or four concentric outlines.
- Removing all strokes makes the layout vanish entirely.

**Why it hurts the design**
Outlines describe boundaries; light describes objects. A surface that is only a
boundary never feels manufactured, and the accumulated strokes add visual noise
in proportion to nesting depth.

**Correct alternative**
Separate with a plane gradient, a one-pixel inner top highlight, a broad soft
inner glow, and a bottom floor, then calibrate the border down until it sits
just below notice. Reserve visible strokes for semantic separation.

**Test**
Turn every border off. If nothing is legible, the surfaces were never lit.

### 25. Colour spent on the nominal case

**Description**
Healthy, normal, or expected states are given saturated colour, so the exception
has nowhere louder to go.

**Why AI agents tend to produce it**
Semantic palettes conventionally pair green with success, and applying the full
set feels like completeness. The cost only appears at scale, when the nominal
case covers most of the surface.

**Visual symptoms**

- A status matrix or list is a wall of green with one small warning inside it.
- Success badges outnumber every other coloured element.
- The eye lands on a healthy region before it finds the fault.

**Why it hurts the design**
Colour is a fixed budget. Anything spent describing "nothing is wrong" is
unavailable to describe what is. It also inverts the scan order the product
needs.

**Correct alternative**
Make the nominal case neutral and let the absence of alarm be the signal.
Reserve saturated hue for states that require a response, and keep the
non-colour redundancy — glyph, label, pattern — on every state including the
neutral one.

**Test**
Squint. If the first thing you see is something that is fine, the palette is
inverted.

## Process and quality failures

### 20. Design-system consistency mistaken for visual quality

**Description**
A design is declared successful because it uses the correct tokens, components,
spacing scale, and variants, even though its hierarchy and composition are
ordinary.

**Why AI agents tend to produce it**
Consistency is machine-verifiable; visual quality is not. Agents can count token
reuse and component attachment, so those implementation facts become a proxy
for design judgment.

**Visual symptoms**

- Every component is correct, but the screen has no dominant object.
- Sibling pages repeat the same template regardless of task.
- Token-perfect cards still create card soup.
- The design-system audit is detailed while the visual rationale is vague.
- The result is coherent but interchangeable with products using the same kit.

**Why it hurts the design**
Consistency prevents local chaos; it does not establish product fit,
composition, hierarchy, emotional tone, or distinctiveness. Treating it as the
quality bar institutionalizes mediocrity.

**When it is actually appropriate**
Consistency may be the dominant goal for maintenance work, accessibility fixes,
or mature screens whose art direction and composition are already solved.

**Better alternatives**

- Evaluate design quality, implementation correctness, system consistency, and
  distinctiveness as independent gates.
- Compose existing components in a product-specific hierarchy.
- Extend components only when a recurring semantic behavior is missing.
- Judge rendered pixels and scan path, not only layer metadata.

**How a visual critic should detect it**
Run the thumbnail and logo-swap tests after confirming system compliance. If the
screen is still anonymous, explicitly pass the system gate and fail the design
or distinctiveness gate.

### 21. Reference copying instead of principle extraction

**Description**
An agent reproduces a reference's layout, palette, geometry, imagery placement,
or signature object, then swaps in the current product's labels.

**Why AI agents tend to produce it**
Screenshot imitation is more concrete than interpreting why a design works.
Agents also confuse visual similarity with reference fidelity.

**Visual symptoms**

- Source and output share the same major regions and proportions.
- Brand-specific colors, motifs, device mockups, or object metaphors reappear.
- Current content is forced into another product's information architecture.
- Multiple references are averaged into a collage of recognizable details.
- The design is described as “like [brand] but with our colors.”

**Why it hurts the design**
Copying imports mismatched user goals and interaction assumptions, undermines
originality, and may create intellectual-property risk. The product never gains
its own visual logic.

**When it is actually appropriate**
Exact reproduction can be valid for authorized migration, parity work,
education, or implementing an owned design—not for reference-led art direction.

**Better alternatives**

- Separate observation, interpretation, and transferable principle.
- Classify details as borrow, translate, presentation-only, brand-specific,
  accidental, or reject.
- Combine complementary principles around the current product model.
- Change composition whenever purpose, content, or behavior differs.

**How a visual critic should detect it**
Compare source and output at thumbnail scale and in greyscale. If the silhouette,
major masses, or signature object remain recognizably the same, identify the
copied decision and require a product-derived alternative.

### 22. Design theater

**Description**
The rationale claims intentional hierarchy, accessibility, responsive behavior,
or product specificity that is not visible or implemented in the actual design.

**Why AI agents tend to produce it**
Language models can produce convincing design explanations independently of
their construction results. Tool success and polished prose can mask a gap
between intention and rendered evidence.

**Visual symptoms**

- The brief names a dominant object, but the render shows equal cards.
- The agent claims restrained color while accent appears everywhere.
- “Accessible states” are described but focus, error, loading, and contrast are
  absent.
- Responsive intent exists only as prose.
- Successful rendering is presented as proof of quality.

**Why it hurts the design**
It blocks honest critique. Reviewers approve the stated intention rather than
the artifact, allowing structural failures to survive.

**When it is actually appropriate**
Never as a quality practice. A speculative rationale is acceptable only when it
is explicitly labeled as a hypothesis awaiting implementation and inspection.

**Better alternatives**

- Tie every claim to screenshot or Figma-node evidence.
- Maintain separate gates for design, correctness, system, and distinctiveness.
- Render, critique, fix, and render again.
- Record unresolved gaps instead of narrating them as complete.

**How a visual critic should detect it**
Create a two-column check: claimed decision vs visible evidence. Fail any claim
that cannot be pointed to in the render or verified in structure. Critique the
artifact, never the confidence of the explanation.

## How to escape genericity

Distinctiveness is not extra ornament. It is the visible consequence of making
specific decisions about user purpose, content, hierarchy, composition, and
behavior. Use the strategies below deliberately.

### 1. Replace the page type with a user decision

Do not begin with “dashboard,” “landing page,” or “settings screen.” Write:

> At this moment, **[user]** must decide or do **[task]** using **[evidence]**,
> under **[constraint/consequence]**.

Make the object or evidence required for that decision the largest region. Let
the rest of the composition support it.

### 2. Develop two incompatible composition hypotheses

Before components, sketch at least two whole-viewport ideas that differ in
dominant object and scan path, for example:

- topology + attached inspector;
- dense queue + persistent detail pane;
- continuous timeline + event lens;
- editor/canvas + contextual tools;
- comparison lanes + shared evidence axis;
- object stage + sparse consequential action.

If two options differ only in color, radius, or card style, they are the same
composition.

### 3. Give one object visual sovereignty

Choose one first read. Allocate it the strongest combination of span, position,
density, scale, and contrast. Subordinate everything else. A distinctive screen
usually has one memorable compositional object—not ten novel components.

Use a one-sentence hierarchy contract:

> First see **X**, then verify **Y**, then act through **Z**.

Check the contract at thumbnail size and in greyscale.

### 4. Turn relationships into composition

When order, flow, dependency, comparison, hierarchy, or causality matters, show
it spatially instead of describing it across separate cards.

- sequence → timeline or staged path;
- dependency → topology or attached graph;
- comparison → aligned lanes or small multiples;
- ownership → nested or contiguous surfaces;
- evidence → attached lens or synchronized lower rail;
- progression → controlled continuation through the viewport.

This creates product-specific structure without decorative novelty.

### 5. Use density as rhythm

Alternate orientation, work, and evidence:

- sparse regions establish scope or a consequential decision;
- standard regions support active work;
- dense regions expose comparison, traces, tables, and proof.

Compress low-value chrome before shrinking high-value information. Avoid both
uniform emptiness and uniform busyness.

### 6. Design silhouette before surfaces

In greyscale, resolve:

- outer silhouette and navigation ownership;
- dominant mass and supporting masses;
- directional scan path;
- negative-space shape;
- where density changes;
- which surfaces are joined, inset, or floating.

Only then apply type, color, radii, borders, effects, and component details. If
the silhouette is generic, polish will preserve genericity.

### 7. Create a small signature-move budget

Define two or three recurring moves with functional reasons, such as:

- a selection bracket that connects object and inspector;
- a continuous datum linking time and evidence;
- a role-based surface transition between global and local scope;
- a distinctive but truthful diagram or instrument;
- an editorial type treatment reserved for major orientation.

Repeat them coherently. Do not make every region novel. A signature move must
still work when brand color is removed.

### 8. Make content exert pressure early

Use real or production-shaped content before polishing:

- long names and identifiers;
- uneven values and units;
- missing, stale, error, loading, disabled, and permission states;
- destructive and routine actions together;
- realistic imagery and aspect ratios;
- real comparison counts and data density.

Content pressure reveals whether the composition is genuinely resilient or
only screenshot-deep.

### 9. Assign explicit visual roles

Do not stop at token values. Define rules:

- what type owns orientation, interface text, and machine data;
- what color means current, semantic state, comparison, or brand;
- which surfaces are persistent, selected, floating, or modal;
- how radius changes by scale and content;
- which edge indicates containment, selection, focus, or danger;
- when imagery is evidence versus atmosphere.

Visual roles make reuse expressive instead of repetitive.

### 10. Break symmetry with evidence, not decoration

Allow actual priority, content length, state, or relationship to determine
visual mass. Useful moves include:

- a dominant span with a narrow evidence rail;
- an off-center focal object balanced by denser detail;
- one item expanded within an aligned comparison set;
- a cropped/continued work surface that implies real navigation;
- an annotation attached to the exact point it explains.

Do not introduce arbitrary rotation, overlap, or imbalance merely to look
different.

### 11. Convert cards into stronger structures

For every proposed card, ask what relationship it has to its neighbors:

- same object → combine into one instrument;
- same axis → use a shared plot or table;
- same sequence → use a timeline;
- same comparison dimensions → use aligned lanes or matrix;
- selected detail → use an attached inspector;
- temporary/movable object → keep the card;
- unrelated summary → question whether it belongs on the screen.

The goal is not zero cards. It is zero unjustified cards.

### 12. Separate system consistency from art direction

Reuse tokens and components, but judge four gates independently:

1. design quality;
2. implementation correctness;
3. design-system consistency;
4. visual distinctiveness.

A screen can pass the middle two and still fail. Compose existing components in
a new hierarchy before inventing component variants for novelty.

### 13. Use references as a vocabulary, not a target

For each reference record:

- observation—what is visibly present;
- interpretation—what decision it represents;
- transferable principle—how the decision can serve this product;
- reject/ignore—what is brand-specific, accidental, or mismatched.

Synthesize complementary principles into a new thesis. Do not average sources
or let one screenshot dictate the product architecture.

### 14. Run genericity stress tests

Before passing the design:

- **Logo swap:** could any SaaS brand own it unchanged?
- **Noun swap:** could CRM/finance/project labels replace the content?
- **Silhouette:** is the viewport recognizable without text, icons, and color?
- **Accent-off:** does hierarchy survive without brand color?
- **Card count:** are most facts detached containers?
- **Five-second read:** is the primary object/state/action correct?
- **Real-content test:** do long, missing, error, and permission states hold?
- **Reference-distance test:** is any source still recognizable as a copied
  layout or motif?

Failing a stress test requires another composition or hierarchy pass—not a new
gradient, icon set, or shadow recipe.

### 15. Close the visual loop

The escape from genericity is iterative:

1. render the intended viewport;
2. critique the actual pixels;
3. identify the highest-impact missing decision;
4. fix composition before surface polish;
5. render the same viewport again;
6. compare scan path, hierarchy, content truth, and distinctiveness;
7. repeat until the result passes all four quality gates.

Never declare success because the file rendered, the nodes are valid, or the
components are consistent. Those facts prove implementation health, not visual
intent.
