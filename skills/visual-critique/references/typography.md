# Typography

Typography must establish order, carry product character, and survive real
content. A screen does not earn a high score merely because it uses the correct
font family or text style.

## Inspect roles, not isolated text

Inventory visible roles from the render:

- screen/context title;
- section or object heading;
- operational value;
- label and unit;
- body/explanation;
- control label;
- metadata, timestamp, identifier, and code/log text;
- alert and state text.

For each role, record family, apparent size, weight, line height, contrast,
case, and alignment using structural reads for exact values. Two roles that
look identical but carry different importance are a hierarchy defect even when
they use different named Figma styles.

## Operational tests

### Squint test

Blur fine details. Headings, values, labels, and secondary guidance should form
distinct tonal bands. If every text element becomes the same grey texture,
size/weight/contrast roles are too weak.

### Content-pressure test

Use the visible longest labels, realistic values, units, errors, and timestamps.
Flag:

- clipped or ellipsized critical content;
- awkward one-word wraps;
- labels that collide when localized or expanded;
- values whose decimals/units jump across repeated rows;
- headings sized for placeholder copy rather than production content.

### Numeric and machine-data test

Check tabular alignment, decimal alignment, unit separation, sign handling,
timestamps, hashes, and identifiers. Monospace is useful only when comparison
or machine identity benefits; it is not an automatic “technical” aesthetic.

### Line-length test

Body copy should remain comfortably scannable; dense product surfaces should
prefer concise labels and disclosed explanation over wide paragraphs. Narrow
columns must not create ragged, stuttering text.

## Aggressive failure checks

| Failure | Why it matters | Corrective action | Desired outcome |
|---|---|---|---|
| Every label semibold | Removes weight as a hierarchy channel and creates noise | Keep emphasis for decisions/state; reduce supporting label weight | Clear type color and calmer scan |
| Tiny grey copy | Hides information behind fashionable restraint | Increase size/contrast or remove low-value copy | Secondary text remains comfortably readable |
| Oversized generic title | Consumes area without helping repeat use | Compress context heading; give area to operational evidence | Product state wins before page naming |
| Display font everywhere | Turns character into texture and harms density | Reserve expressive face for strategic hierarchy; use a workhorse for interface text | Brand character with operational clarity |
| Weak value/unit distinction | Makes metrics slow to parse | Align values, reduce unit prominence, establish consistent spacing | Values compare instantly without losing units |
| All-caps proliferation | Produces a flat, loud texture | Limit all-caps to short metadata roles with tracking | Labels become quieter and more distinct |
| Arbitrary type sizes | Breaks system trust and vertical rhythm | Map roles to a compact scale; use position/spacing before inventing another size | Few roles, strong order |

## Score evidence

A typography criticism must name the role and visible consequence. Example:

> The 11 px low-contrast service labels and 12 px timestamps collapse into the
> same texture, so the user cannot distinguish identity from recency. Raise
> service labels one role, reduce timestamp contrast, and align timestamps to a
> shared column. The list should read service → state → recency at a glance.

“Weak typography” without named roles and a target hierarchy is invalid.

