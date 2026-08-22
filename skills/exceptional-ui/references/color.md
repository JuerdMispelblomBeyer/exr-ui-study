# Color

Color communicates role, state, selection, and atmosphere. It must reinforce a
composition that already works in greyscale.

## 1. Start with the existing semantic system

Inspect variables, modes, paint styles, component bindings, and current light/
dark behavior. Map available colors to roles:

- canvas;
- chassis or shell;
- primary surface;
- secondary/inset surface;
- border/contour;
- primary, secondary, and muted text;
- brand/action accent;
- selection/focus/current datum;
- success, warning, error, and informational state;
- data series and comparison;
- overlay/scrim.

Reuse semantic variables. Do not choose a primitive solely because its hex
looks close; its meaning must fit.

## 2. Establish an accent budget

Write down what earns the strongest accent:

- primary action;
- current selection or focus;
- live/current datum;
- selected path/object;
- decisive warning or exception.

Choose at most one primary meaning per screen unless the design system already
defines another controlled use. Audit the screenshot: the accent should form a
readable path, not confetti.

If removing the accent destroys the composition, fix hierarchy first.

## 3. Build surface hierarchy with value

Define surfaces by luminance and edge treatment before hue:

1. background/canvas;
2. containing chassis;
3. persistent work surface;
4. inset or dense data surface;
5. selected/floating/temporary surface;
6. scrim/overlay.

Adjacent layers need enough separation to establish ownership but should not
become alternating colored boxes. In dark UI, avoid stacking several nearly
identical blacks with no edge definition. In light UI, avoid white cards on a
nearly white canvas differentiated only by shadow.

## 4. Use semantic color truthfully

- Pair state color with text, icon, pattern, or shape.
- Do not use red or orange for decorative warmth if those colors indicate
  failure elsewhere.
- Do not assign every category a pastel identity unless users must track those
  categories across contexts.
- Keep disabled content distinguishable from unavailable or unknown states.
- Use data-series colors only when each series can be identified without hue
  alone.

## 5. Gradients, glow, and translucency

Use a gradient only when it:

- establishes atmosphere behind readable content;
- explains spatial transition or focus;
- belongs to an established brand device;
- differentiates a selected/temporary layer without reducing clarity.

Reject gradients used to make a generic card feel “designed.” Keep dense data
on stable, sufficiently opaque surfaces. Glow is reserved for actual focus,
energy, live state, or depth ownership; never outline every component with it.

## 6. Derive dark and light expressions

Do not invert colors mechanically. Preserve semantic roles while recalibrating:

- surface luminance steps;
- border visibility;
- text contrast;
- accent dominance;
- shadow versus inner-contour behavior;
- image treatment;
- semantic-state accessibility.

The two expressions should share the same composition and component language.
An unrelated cyberpunk dark theme is not a mode.

## 7. Color QA

Run:

1. **Greyscale check:** hierarchy and product identity remain.
2. **Accent isolation:** view only saturated/high-contrast areas; they match
   action and state priority.
3. **Contrast check:** primary text, controls, focus, and data marks meet the
   project's accessibility target.
4. **State matrix:** default, hover, focus, selected, disabled, loading,
   success, warning, error, and unknown remain distinguishable.
5. **Surface check:** every layer's ownership is clear without heavy shadow.
6. **Theme check:** light and dark use the same semantics.

Bind accepted colors to existing variables/styles through `figma-build`.
Create new semantic tokens only for recurring roles.
