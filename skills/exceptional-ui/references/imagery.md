# Imagery

Imagery includes photography, illustration, 3D renders, diagrams, maps, icons,
textures, and product screenshots. Use it as content or explanation, not as
cosmetic filler.

## 1. State the job of every image

Classify each asset:

- **identity** — establishes brand/product character;
- **subject** — the object the user is inspecting or buying;
- **evidence** — proves a condition, state, location, or result;
- **navigation** — helps recognition across objects or categories;
- **explanation** — diagram, anatomy, topology, sequence, or annotation;
- **atmosphere** — supports tone without carrying product truth.

If an image has no job, remove it. Atmosphere should not displace required
content.

## 2. Prefer real assets

Use, in order:

1. project-provided brand and product assets;
2. verified real product photos/renders/screens;
3. coherent commissioned or generated imagery made for the direction;
4. a deliberately designed fallback state.

Do not finish with grey boxes, random stock photography, generic 3D blobs,
unrelated avatars, or hand-typed logos. Do not use a physical laptop/phone
mockup as the UI reference when a direct screen export is available.

## 3. Integrate imagery into composition

Decide:

- focal point and crop;
- image scale relative to text and data;
- whether the image is full-bleed, bounded, masked, annotated, or attached;
- how it behaves responsively;
- whether controls sit over it and require a scrim;
- what happens when it is missing, loading, or low quality.

Avoid putting every image into the same rounded thumbnail. Subject imagery may
deserve a large stage; evidence thumbnails may be dense and comparable.

## 4. Diagrams and system imagery

When relationships matter:

- show direction, ownership, grouping, current selection, and degraded paths;
- attach labels and annotations to the object they explain;
- preserve scale or topology truth when the user relies on it;
- distinguish schematic abstraction from physical geometry;
- avoid decorative node clouds and meaningless connector lines.

A diagram is successful when it reduces the work required to locate, compare,
or diagnose—not merely when it looks technical.

## 5. 3D and generated visuals

Use 3D or generated imagery only when it adds product specificity, physical
context, spatial understanding, or brand character. Match:

- camera perspective;
- lighting direction and contrast;
- material realism;
- background treatment;
- depth of field;
- level of detail;
- crop grammar.

Do not mix unrelated render styles across one product. Do not let cinematic
lighting reduce the legibility of operational overlays.

## 6. Icons

- Reuse the file's icon components or established library.
- Keep stroke/fill language and optical size consistent.
- Prefer a familiar symbol for common actions.
- Reserve bespoke icons for product-specific objects or concepts.
- Pair ambiguous or safety-relevant icons with text.

## 7. Provenance and Figma handling

- Preserve provenance and usage constraints for external references/assets.
- Reference work is evidence for principles, not automatically reusable art.
- Import real SVG/vector assets as vectors and raster assets as images through
  `figma-build`.
- Use screenshots for visual QA; use the original image asset rather than a
  screenshot when the source pixels are needed in the design.

## 8. Imagery QA

Inspect:

1. Does every image have a stated job?
2. Is the crop intentional at every target viewport?
3. Does image style belong to the same product?
4. Are overlays legible and truthfully attached?
5. Are diagrams informative rather than decorative?
6. Do loading, missing, and error states preserve composition?
7. Could a generic stock image be swapped in without changing meaning? If yes,
   the imagery is not product-specific enough.
