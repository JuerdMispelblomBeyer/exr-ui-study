# Ten-category diagnostic profile

Score the rendered outcome. Do not score the prompt, process, component tree,
or the designer's intent. Structural inspection may explain a visible issue;
it does not replace the render.

This profile diagnoses visible strengths and failures on ten 0–10 axes. It is
not a second quality gate. The authoritative weighted score and `PASS` rule are
in `../../exceptional-ui/references/quality-rubric.md`.

## Universal score anchors

| Score | Meaning |
|---:|---|
| 0 | Absent, unusable, or fundamentally broken |
| 1–2 | Severe failure; meaning, legibility, or visual order is compromised |
| 3–4 | Weak; obvious structural problems and little intentional resolution |
| 5 | Competent baseline; usable but generic, uneven, or under-directed |
| 6 | Good in parts; one or more visible weaknesses keep it from feeling resolved |
| 7 | Solid and intentional; production-worthy with meaningful room to improve |
| 8 | Strong; visually directed, coherent, product-specific, and well resolved |
| 9 | Exceptional; memorable, exact, and unusually well integrated |
| 10 | Rare benchmark quality; every choice reinforces purpose with no evident weak region |

A 5 is not a failure of implementation. It is a failure to be exceptional.
Do not award 8+ because a screen is clean, dark, fashionable, or consistent.

## Category criteria

### Composition

Judge dominant mass, silhouette, grid, balance, continuity, asymmetry, spatial
relationships, density rhythm, and use of the viewport.

- **3–4:** a stack of interchangeable sections/cards; empty or overcrowded
  zones; the primary object does not earn its area.
- **7:** coherent structure and clear grouping, but the silhouette or tension
  remains conventional.
- **8–10:** the task determines the composition; one dominant relationship
  organizes the frame; negative space and density create a controlled scan.

### Visual hierarchy

Judge first read, scan order, contrast allocation, information levels, state
prominence, and whether hierarchy survives greyscale, blur, and thumbnail scale.

- **3–4:** several regions shout equally, or nothing wins; color carries the
  full hierarchy.
- **7:** readable and correctly ordered, with minor competition or weak depth.
- **8–10:** the eye lands, moves, and resolves in the intended order without
  explanation; subordinate content remains available but quiet.

### Typography

Judge role clarity, scale/weight contrast, line length, rhythm, alignment,
legibility, content fit, numeric treatment, and typographic character.

- **3–4:** generic default styling, tiny low-contrast copy, semibold everywhere,
  weak line breaks, or ambiguous data hierarchy.
- **7:** coherent roles and readable content, but limited expression or some
  density/rhythm defects.
- **8–10:** typography carries hierarchy and brand character while remaining
  robust under real labels, values, units, and edge cases.

### Spacing

Judge alignment, grouping intervals, internal padding, whitespace ownership,
density variation, vertical rhythm, optical compensation, and viewport economy.

- **3–4:** arbitrary gaps, equal padding for unequal roles, poor alignment, or
  both wasted space and local crowding.
- **7:** a clear rhythm with a few weak joins or over-regular repeated modules.
- **8–10:** spacing exposes relationships, produces deliberate breathing room,
  and increases information density without making the screen feel cramped.

### Color

Judge semantic roles, surface separation, accent budget, contrast, state cues,
brand fit, greyscale resilience, and gradient purpose.

- **3–4:** accent sprawl, arbitrary category colors, muddy surfaces, decorative
  gradients, or color-only status.
- **7:** restrained and readable, with some missed semantic or atmospheric
  opportunity.
- **8–10:** color directs attention, explains state and surface ownership, and
  feels inseparable from the product without overwhelming content.

### Geometry

Judge shape language, radius hierarchy, edge/stroke grammar, enclosure logic,
control affordance, icon geometry, line weight, and elevation.

- **3–4:** one rounded rectangle per idea, universal pills, inconsistent radii,
  meaningless borders, or equal elevation everywhere.
- **7:** consistent and functional geometry, but predictable or insufficiently
  differentiated by role.
- **8–10:** outer and inner geometry express material hierarchy and behavior;
  every enclosure, edge, and elevation has a legible purpose.

### Consistency

Judge design-system reuse, token/component coherence, repeated behavior,
screen-family grammar, and whether exceptions are deliberate.

- **3–4:** multiple visual dialects, detached variants, token drift, or states
  that change meaning between screens.
- **7:** system use is visible and reliable, with minor drift or weak exceptions.
- **8–10:** the family is unmistakably related while composition changes with
  each task; system reuse supports, rather than suppresses, expression.

Never transfer points from Consistency to Distinctiveness. A perfect template
can score 9 for consistency and 3 for distinctiveness.

### Content quality

Judge product relevance, realism, specificity, information economy, labels,
states, units, edge cases, visualizations, and actionability.

- **3–4:** lorem ipsum, fake metrics, decorative charts, generic SaaS copy,
  impossible states, or screen-level detail that does not support the job.
- **7:** realistic and useful content with a few vague labels or low-value items.
- **8–10:** content pressure shapes the layout; data, controls, and exceptions
  feel operationally true and reveal exactly what the user needs next.

### Distinctiveness

Judge visual thesis, product specificity, signature devices, memorability,
reference distance, and resistance to the logo-swap/template test.

- **3–4:** technically polished but aesthetically anonymous; trends provide the
  identity; another SaaS logo could replace the current one.
- **7:** some specific product character, but the silhouette or components
  remain familiar and safe.
- **8–10:** a small set of meaningful signature moves creates a recognizable
  family; references are transformed into principles, not copied.

### Craft/detail

Judge optical alignment, baselines, text wrapping, icon sizing, strokes,
shadows, crops, chart labels, transitions, clipping, state finish, and
pixel-level coherence.

- **3–4:** accumulated small errors undermine trust or make the design feel
  generated rather than authored.
- **7:** polished at normal scale with a short list of visible defects.
- **8–10:** details remain exact at full size; micro-decisions reinforce the
  larger material and interaction logic.

## Scoring discipline

- Give one visible piece of evidence with every score.
- Score the weakest important region, not the best isolated component.
- A severe product-fit or correctness issue caps relevant categories at 4.
- A high-severity generic/template diagnosis caps Distinctiveness at 5.
- If hierarchy collapses in greyscale or thumbnail view, Visual hierarchy
  cannot exceed 6.
- If no rendered screenshot was inspected, mark scores provisional and do not
  return `PASS`.

## Crosswalk to the authoritative rubric

Use these relationships as evidence, not as a formula for mechanically
converting 0–10 scores into points:

| Diagnostic category | Primary 100-point dimensions |
|---|---|
| Composition | C1 Composition and spatial logic |
| Visual hierarchy | C2 Visual hierarchy and attention control |
| Typography | C3 Typography |
| Spacing | C4 Spacing, density, and alignment |
| Color | C5 Color and contrast |
| Geometry | C6 Geometry, surfaces, and craft |
| Consistency | B Design-system correctness; also visible C6 evidence |
| Content quality | A Functional correctness; C2 hierarchy evidence |
| Distinctiveness | D Distinctiveness |
| Craft/detail | C6 Geometry, surfaces, and craft; implementation blocker evidence |

Do not average the ten diagnostic scores into a verdict. Complete the weighted
100-point record separately, apply all floors and overrides there, and use that
result as the critique decision.
