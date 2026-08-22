# Color

Color must explain attention, state, and material hierarchy. Do not reward a
palette because it is fashionable or because the brand accent is present.

## Build a role map

Identify each visible color by semantic role:

- canvas and persistent surfaces;
- elevated/temporary/selected surfaces;
- primary and secondary text;
- edges and separators;
- primary action and focus;
- current selection or active path;
- success, warning, error, disabled, unknown, and disconnected state;
- data-series distinctions;
- atmospheric or illustrative color.

If two colors differ but do not differ in role, question the extra color. If
one color carries several incompatible roles, question the ambiguity.

## Accent-budget audit

Estimate where the eye encounters the accent. It should form a deliberate path
toward action, selection, current datum, or exceptional state. Penalize accents
used simultaneously for brand decoration, all icons, all active controls, all
charts, and all warnings; the color loses authority.

State the correction as an allocation rule, not “use less color.” Example:
reserve the lead accent for selection/current datum and move informational
series to neutral line styles.

## Surface-hierarchy test

In both color and greyscale, check whether canvas, persistent work surface,
nested instrument, selected object, and transient overlay remain distinct.
Do not allow many near-identical grey panels plus borders to simulate depth.
The difference must be visible but restrained.

## Semantic-state test

Every critical status must have a second cue: label, icon, shape, pattern, or
position. Verify that warning and brand accent do not collide semantically.
Check disabled, unknown, stale, and disconnected states—not only success/error.

## Gradient test

For each gradient, ask what it encodes:

- spatial light/material depth;
- value progression;
- focus/selection;
- image treatment;
- or nothing beyond trend decoration.

Remove or flatten gradients that do not survive that question. A generic
purple/blue/yellow glow behind cards is not a visual thesis.

## Failure patterns and corrections

| Failure | Why it matters | Correction | Desired outcome |
|---|---|---|---|
| Excessive accent colors | Competing semantic claims create noise | Assign a lead accent, semantic statuses, and restrained comparison palette | Attention follows one controlled path |
| Arbitrary category colors | Color becomes decoration instead of meaning | Use topology, label, icon, or position for categories; keep color semantic | Categories remain legible without rainbow coding |
| Brand wash | Large accent surfaces cause fatigue and erase focus | Move brand color to selection/action/current datum | Brand signal becomes precise and valuable |
| Muddy dark surfaces | Layers merge and borders do all the work | Separate surface luminance and reduce redundant strokes | Depth reads before outlines |
| Pure neutral light UI | Product feels sterile or anonymous | Introduce controlled warm/cool material relationships derived from direction | Neutral system still has a recognizable atmosphere |
| Unnecessary glow | Makes stable objects look temporary or theatrical | Keep glow for focus, live energy, or transient state only | Effects communicate behavior |
| Color-only alert | Fails accessibility and fast diagnosis | Add label/icon/shape and attach state to the affected object | Status is unambiguous in greyscale |

## Scoring constraint

If the hierarchy collapses when hue is removed, Color may still score well for
semantic craft, but Visual hierarchy cannot exceed 6. If warning and brand
accent conflict on a safety-critical control, both Color and Content quality
should be capped until the ambiguity is resolved.

