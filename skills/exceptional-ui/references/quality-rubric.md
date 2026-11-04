# Exceptional UI quality rubric

Use this rubric to judge the rendered interface—not the prompt, rationale,
effort, Figma node count, or tool success message. Inspect screenshots at the
intended viewport and consult Figma structure only for facts pixels cannot prove.

The rubric separates four gates that must pass independently:

- **A. Functional correctness — 15 points**
- **B. Design-system correctness — 10 points**
- **C. Visual quality — 55 points**
- **D. Distinctiveness — 20 points**

Total: **100 points**.

Composition, visual hierarchy, typography, and distinctiveness carry 63 points.
Excellent implementation and component consistency cannot compensate for weak
visual direction.

## 0. Operational scorecard

Read this section for every review. Open a detailed dimension below only when
its score is failing, borderline, uncertain, or challenged. This is progressive
disclosure, not a lighter inspection standard: the critic must still inspect
the full current render at thumbnail, greyscale/blur, and full size.

### Evidence minimum

Current legible render; user/job/state and requirements; intended thesis and
scan path; applicable system constraints; previous same-viewport render for a
revision. Missing current pixels forces `ITERATE`.

### Compact scoring map

| ID | Dimension | Pts | Excellent | Mediocre | Poor |
|---|---|---:|---|---|---|
| A1 | Product/task fit | 5 | Dominant object/action serves the named decision | Features exist but category/page grammar dominates | Wrong job, scope, or action |
| A2 | Content/state truth | 5 | Real content and consequential states shape layout | Plausible but generic/happy-path | Fake, misleading, placeholder, or impossible |
| A3 | Usability/accessibility | 5 | Clear action, readable, non-color cues, robust priority | Usable with friction or untested edges | Inaccessible, ambiguous, or broken |
| B1 | Reuse/implementation alignment | 5 | Correct attached components/tokens and sound structure | Mostly aligned with visible drift | Detached, duplicated, or structurally inconsistent |
| B2 | Semantic consistency | 5 | Shared meanings; justified reusable extensions | Minor drift or weak exception | Treatments change meaning or fragment system |
| C1 | Composition | 18 | Task-shaped silhouette, dominant relationship, controlled density | Competent conventional arrangement | Interchangeable sections/cards or wrong dominant mass |
| C2 | Hierarchy | 14 | Intended scan order is immediate without hue | Readable with competition | Equal weight, wrong first read, color-dependent |
| C3 | Typography | 11 | Type carries order, character, and real data | Readable but generic/weakly differentiated | Role collapse, tiny copy, semibold/default texture |
| C4 | Spacing/density | 5 | Distance encodes relationships; viewport is efficient | Consistent but mechanical or uneven | Arbitrary gaps, crowding, or wasted area |
| C5 | Color/surfaces/imagery | 4 | Semantic, restrained, product-supporting | Attractive but partly decorative | Accent sprawl, weak contrast, arbitrary effects/assets |
| C6 | Geometry/craft | 3 | Role-based shape/edges and exact finish | Consistent but ordinary or slightly rough | Universal containers, meaningless borders, visible errors |
| D1 | Thesis/product specificity | 10 | Product relationship defines the visual idea | Some character; familiar silhouette | Logo-swappable/template-like |
| D2 | Signature/recognizability | 6 | Two or more meaningful recurring moves survive anonymization | One weak or decorative move | No memorable grammar |
| D3 | Reference distance/family | 4 | Principles transformed; sibling tasks vary coherently | Safe mixture or mild repetition | Copied source or unrelated/repeated screens |

Score integer points from visible evidence. Choose poor/mediocre/excellent band
first; use the detailed section only to resolve the integer. Do not double-count
one defect unless it independently harms two dimensions.

### Non-compensable decision

Base threshold: total ≥85; A ≥12; B ≥7; C ≥45; D ≥16; C1 ≥14; C2 ≥11;
C3 ≥8; no critical override; genericity and recognizability pass; current
post-change render inspected.

For an `exceptional-ui` run, return `ITERATE` below 92, C <50, D <18, when any
high-impact correction remains, or before a material critique/fix/re-render
cycle. Return `PASS` only when further changes would add novelty or reduce
clarity rather than correct a visible weakness.

Critical overrides: broken/inaccessible primary action; consequential-state
misrepresentation; fake operational data; copied protected asset/composition;
missing current render; unproved claimed state; semantic system break;
genericity or recognizability failure.

Genericity test: ignore logo, copy, and accent; run noun-swap, template
silhouette, component-swap, effect-removal, content-pressure, and
task-correspondence checks. Recognizability requires one dominant compositional
idea plus two meaningful signature moves without brand identifiers.

## 1. Required evidence

Before scoring, obtain:

- a current screenshot of every materially changed viewport at legible scale;
- the primary user, task, state, and intended design direction;
- relevant visual-language and reference-principle documents;
- the applicable design-system variables, styles, and component constraints;
- production-shaped content, including consequential and edge states;
- a previous screenshot when evaluating an iteration.

If rendered evidence is missing, do not award an excellent score. A clean layer
tree cannot prove composition, hierarchy, typography, or distinctiveness.

For a screen set, score the set as one product. Use the weakest materially
important screen when determining gate floors; a strong hero screen cannot hide
generic or broken sibling screens.

## 2. Scoring calibration

Use integer points only. Score each dimension independently before calculating
gate totals.

| Band | Meaning | General calibration |
|---|---|---|
| Excellent | Resolved and intentional | 85–100% of available points |
| Strong | Clearly above ordinary | 70–84% |
| Mediocre | Competent but generic, incomplete, or inconsistent | 40–69% |
| Poor | Missing, misleading, broken, or materially weak | 0–39% |

Calibration rules:

1. Cite visible or structural evidence for every dimension.
2. When evidence falls between bands, use the lower score unless the stronger
   qualities are visible across the whole viewport or screen set.
3. Unknown or untested behavior cannot receive excellent. Cap it at mediocre
   and state what evidence is missing.
4. Do not award points for stated intention that is absent from the render.
5. Do not deduct the same defect twice unless it independently harms two
   dimensions. Explain both effects when doing so.
6. Judge appropriateness, not fashion. A plain table can score excellently when
   it is the right dominant object and is composed with precision.
7. Use the full scale. “Looks fine” belongs in mediocre, not excellent.

### Inter-rater consistency protocol

When two independent critics evaluate the same work:

1. Give both critics the same renders, viewport, product/task statement,
   direction, reference principles, and system constraints.
2. Each critic scores privately. Do not reveal the first score to the second.
3. Select the qualitative band first—poor, mediocre, strong, excellent—then
   choose the integer inside that band from visible evidence.
4. Require a region-specific evidence sentence for every dimension. Adjectives
   such as “clean,” “polished,” or “modern” are not scoring evidence.
5. Compare scores only after both records are complete. Reconcile when critics
   differ by more than two points on composition, hierarchy, or typography, or
   by more than one point on any other dimension.
6. During reconciliation, identify the disputed visible fact and rescore once.
   If evidence remains ambiguous, keep the lower score and record what render or
   state would resolve it.

This protocol aims for comparable judgment, not artificial unanimity. Agreement
must come from shared evidence and anchors rather than averaging opinions.

## 3. Score allocation

| Gate | Dimension | Points |
|---|---|---:|
| A. Functional correctness | A1 Product and task fit | 5 |
|  | A2 Content, state, and interaction truth | 5 |
|  | A3 Usability, accessibility, and responsive priority | 5 |
| B. Design-system correctness | B1 Reuse and implementation alignment | 5 |
|  | B2 Semantic consistency and justified extension | 5 |
| C. Visual quality | C1 Composition | 18 |
|  | C2 Visual hierarchy | 14 |
|  | C3 Typography | 11 |
|  | C4 Spacing and density rhythm | 5 |
|  | C5 Color, surfaces, and imagery | 4 |
|  | C6 Geometry and craft/detail | 3 |
| D. Distinctiveness | D1 Visual thesis and product specificity | 10 |
|  | D2 Signature moves and recognizability | 6 |
|  | D3 Reference distance, restraint, and family coherence | 4 |
| **Total** |  | **100** |

## A. Functional correctness — 15 points

### A1. Product and task fit — 5 points

**Excellent — 5**

The dominant object, information, and action directly support a named user in a
specific situation. The screen exposes the shortest credible path from signal
to decision. Product boundaries and consequences are represented accurately.

**Mediocre — 2–3**

The expected features are present, but the interface is organized by software
categories or generic page conventions. The user can complete the task only
after scanning unrelated summaries or navigating through indirect structure.

**Poor — 0–1**

The screen solves the wrong problem, misrepresents the product, omits the
primary task, or gives decorative/secondary content the dominant position.

**Questions the critic should ask**

- Who is acting, at what moment, and what must they decide or do?
- Does the largest region support that task?
- Is the primary action visible at the correct stage and consequence level?
- Could the screen serve a different product after only changing nouns?
- Is anything important outside the product's stated scope?

**Common failure modes**

- “Dashboard” treated as the user job.
- KPI-first organization regardless of workflow.
- Marketing content inside a recurring operational surface.
- Feature inventory without a task path.
- Out-of-scope controls or invented product capability.

### A2. Content, state, and interaction truth — 5 points

**Excellent — 5**

Names, values, units, ranges, imagery, states, permissions, and relationships are
real or production-shaped. Current, stale, unknown, empty, loading, error,
disabled, selected, and consequential states are represented where relevant.
Controls advertise plausible behavior and distinguish request,
acknowledgement, and observed result when needed.

**Mediocre — 2–3**

Content is plausible but tidy. Some units, sources, edge states, permissions,
or interaction outcomes are missing. The happy path works, while failure or
partial-data behavior would require improvisation.

**Poor — 0–1**

The design relies on lorem ipsum, round placeholder metrics, fake charts,
impossible states, misleading controls, or invented relationships. Visual
complexity implies evidence the product does not have.

**Questions the critic should ask**

- What proves that each value, chart, connector, and control is meaningful?
- Are units, source, time range, freshness, uncertainty, and thresholds visible?
- Can the interface represent missing, stale, unknown, and conflicting state?
- Does selection persist across related evidence?
- Do dangerous or permission-controlled actions show consequence and outcome?

**Common failure modes**

- Placeholder-content design.
- Decorative charts or topology.
- Generic “Something went wrong” copy.
- Color-only state with no reason or freshness.
- Controls, handles, or motion with no defined behavior.

### A3. Usability, accessibility, and responsive priority — 5 points

**Excellent — 5**

The primary task is clear at the intended viewport and remains prioritized at
other required sizes. Text, contrast, focus, target size, reading order,
keyboard behavior, reduced motion, and state redundancy are credible. Dense
content remains legible without depending on hover.

**Mediocre — 2–3**

The main viewport is usable, but one or more accessibility or responsive states
are unverified. Small labels, weak contrast, ambiguous focus, or simple stacking
would create friction but not total task failure.

**Poor — 0–1**

Primary content or actions are inaccessible, clipped, hover-only, illegible, or
lost at a required viewport. Color or animation is the only carrier of meaning.

**Questions the critic should ask**

- Can the five-second read succeed without zoom or hover?
- Are focus, selection, status, and disabled states distinguishable without hue?
- Do production-length labels and localized content hold?
- Does a narrower layout preserve the primary task rather than merely stack?
- Are target sizes, contrast, reading order, and reduced-motion needs addressed?

**Common failure modes**

- Tiny grey text used as sophistication.
- Mobile as a collapsed desktop stack.
- Essential tooltip-only content.
- Missing focus or keyboard state.
- Color-only severity, selection, or freshness.

## B. Design-system correctness — 10 points

### B1. Reuse and implementation alignment — 5 points

**Excellent — 5**

Existing variables, styles, components, variants, and public component APIs were
inspected and reused where semantically correct. Instances remain attached.
Spacing, typography, radius, color, and effects bind to intended roles. The
render and Figma structure agree.

**Mediocre — 2–3**

Most visible styling is consistent, but some primitives duplicate existing
components, detach instances, use raw values, or bypass public properties.
These issues are repairable without changing the visual direction.

**Poor — 0–1**

The screen creates a parallel mini-system, ignores established assets, breaks
component behavior, or appears correct only because one-off styling hides
structural divergence.

**Questions the critic should ask**

- Were the existing variables, styles, fonts, components, and APIs inspected?
- Are reused instances attached and configured through supported properties?
- Are repeated values bound to semantic roles rather than copied raw values?
- Does the node structure support the visible layout and required states?
- Would a theme or component update propagate correctly?

**Common failure modes**

- Detached component copies.
- New primitives for already-supported patterns.
- Raw fills, radii, and typography despite available tokens.
- Correct screenshot with brittle fixed positioning.
- Local styling that cannot survive theme or content changes.

### B2. Semantic consistency and justified extension — 5 points

**Excellent — 5**

Type, color, spacing, geometry, surface, icon, imagery, and state roles remain
consistent across the screen set. New tokens or components fill a recurring
semantic gap, have a clear API, and extend the existing language without
flattening every composition into the same template.

**Mediocre — 2–3**

The design is mostly coherent but includes one-off roles, inconsistent states,
or component variations with unclear recurrence. Sibling screens share styling
but may repeat structure too literally.

**Poor — 0–1**

Semantic colors or component states change meaning, extensions duplicate the
system, or visual novelty fragments the product. “Consistency” is achieved only
by applying identical cards and spacing everywhere.

**Questions the critic should ask**

- Does each token and component role keep the same meaning across screens?
- Is a new foundation reusable beyond this one viewport?
- Do sibling screens feel related while adapting composition to their tasks?
- Are state combinations and edge cases represented consistently?
- Is sameness being mistaken for system coherence?

**Common failure modes**

- Accent color used for selection, warning, decoration, and data.
- New component variant for visual novelty only.
- Repeated page template presented as family coherence.
- Inconsistent icon, radius, or surface ownership.
- Token-perfect card soup.

## C. Visual quality — 55 points

### C1. Composition — 18 points

**Excellent — 16–18**

The viewport has a deliberate, product-specific silhouette; one dominant mass
earns its area; supporting regions attach through clear spatial logic; asymmetry,
negative space, grid, and density create an intentional scan path. Relationships
such as sequence, comparison, ownership, or causality shape the composition.
The layout remains recognizable at thumbnail size.

**Mediocre — 8–12**

Alignment and balance are competent, but the screen follows a familiar template
or distributes content too evenly. The dominant object is present but not
sovereign. Cards, sections, or columns could be rearranged without materially
changing meaning.

**Poor — 0–7**

There is no dominant object or scan path; the composition is accidental,
cluttered, empty, or built from interchangeable modules. Major relationships
are described rather than spatially expressed.

**Questions the critic should ask**

- What wins at five seconds, and should it?
- Can the composition be described without naming components?
- Does the dominant object directly serve the primary task?
- Are related elements joined, aligned, sequenced, or attached?
- Is negative space shaping focus or merely consuming room?
- Do width, height, and position express importance?
- Does the silhouette survive greyscale and 15–20% scale?

**Common failure modes**

- Card soup or three-column-by-default.
- Centered-everything and excessive symmetry.
- Uniform section rhythm.
- Component-first composition.
- Two or more competing focal masses.
- Empty premium spacing around trivial content.

### C2. Visual hierarchy — 14 points

**Excellent — 12–14**

The first, second, and third reads are unambiguous. Consequence, selection,
action, and supporting evidence use distinct combinations of scale, position,
density, luminance, type, and surface—not accent color alone. Hierarchy survives
blur, greyscale, and reduced scale.

**Mediocre — 6–9**

The main regions are understandable, but several elements compete or supporting
content is too prominent. The accent or card headers carry more hierarchy than
the composition. The user can recover the order with effort.

**Poor — 0–5**

Everything has equal visual weight, the wrong element dominates, or the primary
state/action is difficult to find. Removing color collapses the reading order.

**Questions the critic should ask**

- State the first, second, and third reads without zooming.
- Does the most consequential state receive appropriate weight?
- Are primary, secondary, and tertiary actions unmistakable?
- What happens when accent color is removed?
- Do navigation, content, and overlays express ownership and depth?
- Is dense detail subordinate until the user needs it?

**Common failure modes**

- Equal visual weight.
- Excessive accent color.
- Every heading/card/action at similar contrast.
- Badge-only critical state.
- Raised surfaces with no hierarchy.
- Generic hero or illustration dominating product evidence.

### C3. Typography — 11 points

**Excellent — 10–11**

Typography is a compositional system. Orientation, interface text, narrative,
data, labels, and actions have distinct roles. Scale, weight, line height,
measure, alignment, numeric behavior, and wrapping support the scan path and real
content. Type contributes personality without sacrificing reading or density.

**Mediocre — 5–7**

The hierarchy is readable but conventional. Most text uses one generic voice;
headings differ modestly; labels rely on medium weight; long content or numeric
alignment exposes weaknesses. Type supports components more than composition.

**Poor — 0–4**

Hierarchy is weak or inconsistent, text is too small/low-contrast, line lengths
and wrapping are uncontrolled, or typography feels like untouched component
defaults. Containers and color must compensate for unreadable roles.

**Questions the critic should ask**

- Can reading order be understood with containers and color ignored?
- Which role owns orientation, interface copy, and machine/data content?
- Is there one deliberate typographic focal point or many competing headings?
- Do long labels, dense values, units, and errors remain legible?
- Are weight and uppercase used selectively?
- Does the typography express the intended personality at thumbnail and reading
  scale?

**Common failure modes**

- Weak typography and tiny grey labels.
- Every label semibold.
- Oversized generic greeting or slogan.
- Default font with no role differentiation.
- Similar heading sizes across all levels.
- Uncontrolled truncation, wrapping, or numeric alignment.

### C4. Spacing and density rhythm — 5 points

**Excellent — 5**

Spacing clarifies grouping and establishes a purposeful rhythm between
orientation, work, and evidence. Sparse, standard, and dense zones correspond
to task needs. Gutters, internal padding, and alignment are systematic without
making every region feel identical.

**Mediocre — 2–3**

Spacing is consistent but generic. Most regions use the same padding and
vertical interval. The screen is readable, yet either slightly wasteful or
uniformly dense.

**Poor — 0–1**

Grouping is ambiguous, density is exhausting or empty, spacing values appear
random, or container padding consumes space needed for information.

**Questions the critic should ask**

- Does proximity express relationships before borders do?
- Where does the composition pause, accelerate, or become dense?
- Is high-value information being shrunk before low-value chrome?
- Are external gutters and internal spacing optically balanced?
- Would real content break the current rhythm?

**Common failure modes**

- Uniform section rhythm.
- Oversized card padding.
- Random one-off spacing values.
- Dense data forced into spacious marketing components.
- Large empty bands between unrelated modules.

### C5. Color, surfaces, and imagery — 4 points

**Excellent — 4**

Color has explicit brand, interaction, comparison, and semantic roles;
hierarchy survives without it. Surface depth communicates ownership and
temporariness. Imagery is real, credible, and compositionally integrated—or
deliberately absent. Gradients, glass, and effects are restrained and meaningful.

**Mediocre — 2**

Palette and assets are coherent but predictable. Accent is slightly overused,
surfaces rely on familiar card treatment, or imagery feels added after layout.
The design remains usable but visually ordinary.

**Poor — 0–1**

Color carries structure, semantics collide, gradients/shadows create most of
the interest, or imagery is generic, fake, distorted, or irrelevant. Every
surface appears equally raised or temporary.

**Questions the critic should ask**

- What does every saturated color mean?
- Does the screen remain coherent in greyscale?
- Which surfaces are persistent, selected, floating, or modal?
- Is imagery evidence, atmosphere, or decoration—and is that role appropriate?
- Would turning off gradients, shadows, and glow expose a generic layout?

**Common failure modes**

- Arbitrary gradients or colored glow.
- Excessive accent color.
- Glass, shadows, or borders everywhere.
- Generic stock imagery or fake device mockups.
- Multiple unrelated chart colors.

### C6. Geometry and craft/detail — 3 points

**Excellent — 3**

Radius, edge, icon, stroke, alignment, optical sizing, crop, and micro-spacing
form a coherent role-based language. Nested geometry steps down logically.
Pixel-level finish supports the composition without drawing attention to itself.

**Mediocre — 1**

The screen is generally neat but contains visible inconsistencies, generic
rounded geometry, awkward line breaks, doubled borders, or uneven optical
alignment.

**Poor — 0**

Misalignment, clipping, inconsistent strokes, broken crops, arbitrary radii, or
unfinished artifacts are visible at normal scale.

**Questions the critic should ask**

- Do geometry and edge treatments change with role and scale?
- Are icons optically aligned and consistent in weight?
- Are baselines, axes, dividers, and nested corners resolved?
- Are image crops, strokes, and effects consistent at 100%?
- Is any micro-detail compensating for a larger hierarchy problem?

**Common failure modes**

- Excessive rounded rectangles or pills.
- Meaningless borders and doubled seams.
- Half-pixel strokes and inconsistent icon sizes.
- Accidental shadow/glow differences.
- Polishing details before composition is solved.

## D. Distinctiveness — 20 points

### D1. Visual thesis and product specificity — 10 points

**Excellent — 9–10**

The interface expresses a specific formal idea derived from the product's real
objects, workflow, risks, and content. The thesis can be stated as a visible
relationship—not a list of adjectives—and is evident in composition before
color or decoration. The screen could not become another product by relabeling
it.

**Mediocre — 4–6**

The design has coherent styling and some product-specific content, but its
architecture remains a familiar template. The thesis depends on palette,
imagery, or one decorative motif more than on composition and interaction.

**Poor — 0–3**

The result is generic, category-led, or stylistically borrowed. It could accept
another SaaS logo and copy unchanged. No product-specific visual decision owns
the viewport.

**Questions the critic should ask**

- What is the one-sentence formal thesis, and where is it visible?
- Which product relationship shaped the composition?
- Would the same structure work unchanged for CRM, finance, or project software?
- Does distinctiveness survive removal of brand color?
- Is personality coming from meaning or applied effects?

**Common failure modes**

- Generic SaaS dashboard or hero-template syndrome.
- Noun-swappable product architecture.
- Brand color treated as the entire identity.
- Design adjectives without formal consequences.
- Novel decoration attached to conventional layout.

### D2. Signature moves and recognizability — 6 points

**Excellent — 6**

Two or three meaningful signature moves recur coherently across the screen set.
They aid orientation, relationship, state, or interaction and remain
recognizable at thumbnail scale without logo, brand name, or copy. They are
memorable without becoming spectacle.

**Mediocre — 3–4**

One promising move exists, but it is inconsistent, decorative, too dependent on
accent color, or absent from sibling screens. The interface has personality but
not yet a reliable visual point of view.

**Poor — 0–2**

There is no signature beyond common cards, icons, gradients, or type defaults;
or novelty is scattered everywhere with no coherent grammar.

**Questions the critic should ask**

- Which two or three moves would another designer name after five minutes?
- Do the moves perform a real product or interaction function?
- Are they visible in silhouette, geometry, composition, or behavior?
- Do sibling screens repeat the grammar without repeating one page template?
- Would the interface still be recognizable without brand copy and color?

**Common failure modes**

- Dark cards plus one bright accent presented as a signature.
- Novelty everywhere.
- Signature used once as a hero decoration.
- Component-library defaults mistaken for identity.
- Identical page templates mistaken for family coherence.

### D3. Reference distance, restraint, and family coherence — 4 points

**Excellent — 4**

Reference principles are visible, but no source layout, palette, signature
object, or brand-specific motif is reproduced. Distinctive moves are restrained
to a small coherent budget. Sibling screens adapt composition to their jobs
while preserving the same visual grammar.

**Mediocre — 2**

The design is original enough to use, but one source remains visible in a major
layout/detail, or sibling screens oscillate between copied inspiration and
generic templates. The motif budget is slightly uncontrolled.

**Poor — 0–1**

The result traces a reference, averages several sources into a collage, copies
brand-specific assets, or produces unrelated visual styles across screens.

**Questions the critic should ask**

- Can any source be identified from the output's silhouette or signature object?
- Which observed principles were translated, and how did product needs change
  them?
- Are copied details brand-specific, accidental, or presentation-only?
- Does each sibling screen vary according to task while retaining family traits?
- Is restraint creating clarity, or is the design merely safe?

**Common failure modes**

- Reference copying with relabeled content.
- “Like [brand], but in our colors.”
- Averaging incompatible references.
- Presentation imagery imported into operational UI.
- One motif repeated until it becomes decoration.

## 4. Critical failure overrides

The design fails regardless of total score when any of these is true:

- primary content or action is inaccessible or materially broken;
- the interface misrepresents a safety, financial, medical, legal, or other
  consequential state;
- fake/decorative data is presented as operational truth;
- a reference composition or protected asset is copied without authorization;
- the intended viewport was not rendered and visually inspected;
- a claimed state, interaction, or responsive behavior has no implementation or
  visible evidence;
- the design diverges from the system in a way that breaks semantics or product
  behavior;
- the genericity test or recognizability test fails.

## 5. Genericity test

Inspect the render at full size and thumbnail scale. Remove or ignore logo,
brand name, product copy, and accent color. Then ask whether it could plausibly
be mistaken for:

- a generic SaaS template;
- a Tailwind template;
- an AI-generated landing page;
- a standard design-system demo.

Run these checks:

1. **Noun swap:** Could CRM, analytics, finance, project-management, or health
   copy replace the current nouns without changing composition?
2. **Template silhouette:** Is the structure sidebar/header/KPI cards/chart/table
   or eyebrow/centered hero/three cards/CTA by default?
3. **Component swap:** Could another component kit replace the current kit while
   leaving the art direction unchanged?
4. **Effect removal:** Does turning off gradients, glass, shadows, glow, and
   accent reveal an ordinary arrangement?
5. **Content pressure:** Would long names, errors, missing values, permissions,
   and consequential states break the visual idea?
6. **Task correspondence:** Does the largest visual object represent the user's
   real decision, or merely a familiar page pattern?

**Genericity PASS** requires all of the following:

- none of the four template identities is a plausible first description;
- noun swapping would require a different information architecture;
- at least one product-specific relationship shapes the silhouette;
- visual interest survives effect and accent removal;
- production-shaped content strengthens rather than breaks the composition.

If the result is borderline, cap D1 at 6/10 and continue iterating. If it clearly
resembles any of the four template identities, D1 is 0–3 and the overall design
fails regardless of total.

## 6. Recognizability test

Ask exactly:

> **If the logo, brand name, and copy were removed, would the interface still
> have a recognizable visual point of view?**

Evaluate the anonymized or mentally stripped render through:

- silhouette and dominant mass;
- scan path and composition;
- typography as shape and scale;
- surface and geometry relationships;
- imagery or instrumentation language;
- two or three recurring signature moves;
- behavior implied by selection, focus, attachment, or continuity.

**Recognizability PASS** requires the critic to identify one dominant
compositional idea and at least two meaningful signature moves without relying
on logo, copy, or brand color. When an independent second review is available,
the two critics should identify substantially the same idea and moves; material
disagreement forces another inspection or a lower score.

If the answer is “clean cards with [accent color],” the test fails. A failed
recognizability test caps D2 at 2/6 and is an overall critical failure.

## 7. Quality threshold and workflow decision

A design reaches the **base quality threshold** only when every condition is
met:

- total score is **85/100 or higher**;
- A. Functional correctness is **12/15 or higher**;
- B. Design-system correctness is **7/10 or higher**;
- C. Visual quality is **45/55 or higher**;
- D. Distinctiveness is **16/20 or higher**;
- composition is **14/18 or higher**;
- visual hierarchy is **11/14 or higher**;
- typography is **8/11 or higher**;
- no critical failure override applies;
- genericity and recognizability tests both pass;
- the current render has been inspected after the last material change.

These floors are non-compensable. A perfect 25/25 across functional and
design-system correctness cannot rescue low composition, hierarchy, typography,
or distinctiveness.

### Outcome bands

| Result | Conditions | Workflow implication |
|---|---|---|
| Exceptional band | 92–100, all gate floors, C ≥ 50, D ≥ 18, no critical failures | Eligible for `PASS`, subject to the continuation checks below |
| Quality band | 85–91, all gate and priority floors, no critical failures | Meets the base threshold; return `ITERATE` when any continuation check applies |
| Iterate | 60–84, or any gate/priority floor missed | Fix highest-impact structural issue and re-render |
| Reject/reframe | 0–59, or critical failure | Revisit product model, direction, or composition before polish |

The critic returns `PASS` only when the base threshold is met **and** no
continuation condition applies. For an `exceptional-ui` run, the first
condition below always applies: work below the exceptional band remains
`ITERATE`.

### Continue iterating after the base threshold when

- the task explicitly asks for exceptional, unusually distinctive, premium, or
  art-directed work and the score is below 92;
- composition is below 16/18, hierarchy below 12/14, typography below 10/11, or
  distinctiveness below 18/20;
- a high-impact correction is obvious and proportionate to the task;
- genericity or recognizability passes only narrowly;
- one sibling screen remains template-like or repeats another screen's
  composition without task-based reason;
- the design has not undergone a material critique → fix → re-render cycle;
- the previous and current screenshots do not show a visible improvement in the
  targeted issue;
- the interface is coherent but still aesthetically anonymous.

Stop iterating when the exceptional-pass conditions are met and further changes
would add novelty, reduce usability, violate the design system, or produce only
imperceptible micro-variation.

## 8. Scoring record

Use this form after every inspected render:

```markdown
Render / viewport:
Product, user, task, state:
Design direction:
Evidence inspected:

A. FUNCTIONAL CORRECTNESS — __ / 15
- A1 Product and task fit: __ / 5
  Evidence:
- A2 Content, state, and interaction truth: __ / 5
  Evidence:
- A3 Usability, accessibility, responsive priority: __ / 5
  Evidence:

B. DESIGN-SYSTEM CORRECTNESS — __ / 10
- B1 Reuse and implementation alignment: __ / 5
  Evidence:
- B2 Semantic consistency and justified extension: __ / 5
  Evidence:

C. VISUAL QUALITY — __ / 55
- C1 Composition: __ / 18
  Evidence:
- C2 Visual hierarchy: __ / 14
  Evidence:
- C3 Typography: __ / 11
  Evidence:
- C4 Spacing and density rhythm: __ / 5
  Evidence:
- C5 Color, surfaces, and imagery: __ / 4
  Evidence:
- C6 Geometry and craft/detail: __ / 3
  Evidence:

D. DISTINCTIVENESS — __ / 20
- D1 Visual thesis and product specificity: __ / 10
  Evidence:
- D2 Signature moves and recognizability: __ / 6
  Evidence:
- D3 Reference distance, restraint, family coherence: __ / 4
  Evidence:

TOTAL: __ / 100

Critical failure overrides:
Genericity test: PASS | FAIL
Recognizability test: PASS | FAIL
Gate floors passed: A __ B __ C __ D __
Priority floors passed: composition __ hierarchy __ typography __

Strongest evidence:
Five highest-impact problems:
Next correction pass:
Rubric band: EXCEPTIONAL | QUALITY | ITERATE | REJECT/REFRAME
Decision: PASS | ITERATE
```

The written evidence is part of the score. An unexplained number is not a
rigorous evaluation.
