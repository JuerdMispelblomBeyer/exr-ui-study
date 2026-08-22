# Design principles

Apply these as decisions and tests, not slogans.

## Purpose precedes aesthetics

Name the decision the screen enables. Give the most area and contrast to the
information required for that decision. Reject visually attractive content that
does not affect the user's next action.

**Test:** Ask what the user can decide after five seconds that they could not
decide before opening the screen.

## Composition carries identity

Establish a recognizable silhouette, dominant mass, scan path, and density
rhythm before styling individual components. Component polish cannot rescue a
flat or evenly weighted composition.

**Test:** Replace all fills with neutral grey. The intended hierarchy should
remain obvious.

## Components are vocabulary, not composition

Reuse the design system, but do not let its component catalog dictate the page
shape. A card component does not imply a grid of identical cards. Use scale,
span, grouping, continuation, and adjacency to create meaning.

**Test:** Count repeated component silhouettes. If repetition flattens
importance, vary composition before inventing new styling.

## Information has spatial consequence

Show relationships spatially when sequence, dependency, causality, comparison,
or location matters. Do not decompose one relationship into isolated category
cards because cards are easy to generate.

**Test:** Draw arrows between modules that users mentally connect. If many are
needed, the composition is hiding structure.

## Hierarchy uses several channels

Combine scale, position, whitespace, typography, edge strength, density,
opacity, and selective color. Do not ask color or font weight to carry the
entire hierarchy.

**Test:** Blur or squint at the screen. The focal order should still match the
task order.

## Contrast is budgeted

Reserve the strongest scale, brightness, saturation, elevation, and detail for
important states. When everything glows, floats, or shouts, nothing is
important.

**Test:** Identify the single strongest element for each contrast channel. If
there are several accidental winners, rebalance.

## Real content shapes the design

Use plausible names, values, dates, errors, image crops, states, and long labels
early. Real content reveals layout requirements that placeholder content hides.

**Test:** Insert one long title, one empty state, one warning, one dense data
case, and one missing asset. The composition should remain coherent.

## Material expresses ownership

Use surfaces, borders, blur, shadows, and overlap to explain what is persistent,
selected, temporary, floating, or interactive. Effects without ownership are
decoration.

**Test:** For every elevated or translucent surface, name why it sits above
what is behind it.

## Distinctive does not mean arbitrary

Novelty must reinforce product meaning, brand character, or interaction. Avoid
novel shapes, motion, and color applied only to look different.

**Test:** Remove each unusual device. If product comprehension is unchanged,
either justify it as a controlled brand signature or remove it.

## Refinement includes subtraction

At each critique, remove redundant labels, containers, borders, badges, and
effects before adding detail. Visual quality often improves when two weak
devices become one strong one.

**Test:** Identify three elements that can disappear without losing meaning.
If none can, verify that the interface is not merely overexplained.

## Every state belongs to the same language

Default, hover, focus, selected, loading, empty, warning, error, disabled, and
success states should preserve the same composition and component logic.

**Test:** A screenshot of an error or empty state should still be recognizable
as the same product, not a fallback template.
