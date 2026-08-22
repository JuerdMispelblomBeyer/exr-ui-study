# Color system and contrast

Analyze color by role, distribution, and perceptual effect. Do not turn a
reference palette into target tokens by default.

## Role map

Identify visible roles:

- canvas/background;
- persistent, nested, selected, and temporary surfaces;
- primary/secondary/disabled text;
- borders and separators;
- brand or focal accent;
- action, selection, current datum, and focus;
- success, warning, error, unknown, and disconnected state;
- data-series distinctions;
- atmospheric light, image grading, or decoration.

If a color appears in several roles, determine whether that unifies the system
or creates ambiguity.

## Distribution analysis

Record:

- palette breadth: monochrome, limited, or polychrome;
- saturation and temperature relationships;
- accent concentration: sparse, balanced, or diffuse;
- approximate light/dark value structure;
- whether color forms a scan path;
- whether color is structural, semantic, atmospheric, or decorative;
- whether imagery and interface share one grade.

Describe `a warm focal accent concentrated on current state against cool neutral
surfaces`, not merely `yellow and grey`.

## Contrast analysis

Inspect contrast at three levels:

1. **Macro:** dominant mass against canvas.
2. **Meso:** surface, selected state, and content-group separation.
3. **Micro:** text, icons, data, controls, borders, and states.

Use greyscale or squinting to determine whether hierarchy survives without hue.
Do not claim numerical accessibility compliance from a screenshot; state
`apparent contrast` and identify relationships that require measurement in the
target system.

## Gradient and light treatment

For every gradient or glow, classify its likely role:

- spatial/material depth;
- focal illumination;
- data/value progression;
- image integration;
- state/energy;
- or trend decoration.

A transferable principle needs a semantic or compositional effect. Exact stops,
colors, and glow recipes are implementation details unless explicitly measured.

## Brand-specific versus transferable

Usually brand-specific:

- proprietary accent hue;
- distinctive brand gradient;
- color combinations strongly associated with the source;
- logo-driven color blocking.

Usually transferable:

- limited accent budget;
- hue reserved for active/current state;
- surface depth created primarily through luminance;
- one temperature shift separating atmosphere from data;
- hierarchy that remains intact in greyscale.

## Required analysis blocks

Create observation/interpretation/transfer blocks for palette logic, accent
allocation, contrast structure, semantic state, and gradients/atmosphere. State
what target roles need their own brand/system colors rather than source hues.

