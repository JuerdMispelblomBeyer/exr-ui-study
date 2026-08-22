# Interaction cues and motion implications

Static references reveal cues, not verified behavior. Separate what is visibly
interactive from what is merely plausible.

## Interaction-evidence ladder

Use these confidence levels:

- **Observed state:** visible selected, focused, disabled, expanded, dragged,
  loading, error, hover, pressed, or modal state.
- **Strongly implied:** familiar affordance plus state contrast and spatial
  ownership make an interaction likely.
- **Weakly implied:** layout suggests a possible interaction but no visible
  cue confirms it.
- **Unsupported:** no evidence; omit the claim.

Never write “this animates” from a still image. Write “the layered before/after
states imply a depth transition” and state confidence.

## Inspect interaction cues

Look for:

- current selection and scope;
- focus ring or keyboard target;
- handles, cursors, grab areas, or drag affordance;
- chevrons, overflow, tabs, pagination, or disclosure;
- attached inspectors, tooltips, menus, or sheets;
- primary versus secondary action placement;
- disabled, destructive, loading, error, and success states;
- continuation beyond a crop or carousel;
- direct manipulation of diagrams, images, maps, timelines, or objects;
- relationship between persistent content and temporary controls.

Interpret how visual treatment communicates behavior: elevation may imply
temporary ownership; an inset region may imply an editable stage; a connected
inspector may preserve context during selection.

## Motion implications

Infer motion only from visible evidence such as:

- multiple sequential frames;
- motion blur, trails, or displaced states;
- progress or timeline position;
- layered elements with clear source/destination geometry;
- continuity between collapsed and expanded forms;
- carousel peeking or off-canvas continuation;
- animation described by the supplied source and visually corroborated.

Describe motion by purpose and spatial model:

- preserve object continuity;
- shift focal hierarchy;
- explain parent/child ownership;
- reveal detail without losing context;
- confirm state change;
- pace a narrative.

Do not prescribe exact durations/easing from a screenshot. Those belong to
target interaction design.

## Transfer guidance

Transfer `selected detail remains spatially attached to its source object`, not
`copy this right-side drawer`. Transfer `transition preserves the object's
identity`, not `use a 300 ms scale animation`.

## Required analysis blocks

Create observation/interpretation/transfer blocks for visible interaction
states and, separately, motion implications. Include confidence and list what
cannot be determined from the evidence.

