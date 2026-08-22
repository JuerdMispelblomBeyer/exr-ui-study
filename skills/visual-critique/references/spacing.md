# Spacing

Spacing is relational logic expressed as distance. The critic must distinguish
intentional density from crowding and generous whitespace from wasted area.

## Inspect in tiers

Evaluate separately:

1. viewport/chassis margins;
2. distances between major regions;
3. distances between related modules;
4. component padding;
5. label/value/icon micro-spacing;
6. optical corrections around curved, diagonal, or visually heavy shapes.

A screen can use consistent numeric tokens and still fail because the wrong
tier was applied to a relationship.

## Relationship test

For each gap, ask what it communicates:

- same object;
- same task but different evidence;
- adjacent but independent object;
- new section or state;
- persistent boundary versus temporary disclosure.

Distances should increase with semantic separation. If all gaps are equal, the
layout has rhythm but no grouping intelligence.

## Alignment audit

Trace shared edges and baselines through the screenshot. Flag:

- nearly aligned edges that create visual vibration;
- text baselines broken by icon boxes;
- charts whose plot area ignores adjacent labels/values;
- inconsistent start positions across repeated rows;
- nested padding that creates accidental double gutters;
- centered objects that are mathematically but not optically balanced.

Use Figma structure reads to confirm exact values after identifying the visible
misalignment.

## Whitespace-ownership test

Every large empty region must belong to something: focus, separation,
continuation, safe action area, or composition. If it has no owner, reclaim it
for evidence or reduce the frame. Conversely, if dense content has no breathing
edge, create space at the boundary rather than sprinkling equal gaps inside.

## Failure patterns and corrections

| Failure | Why it matters | Correction | Desired outcome |
|---|---|---|---|
| Equal padding everywhere | Treats all components and relationships alike | Use role-based padding tiers; reduce nested double padding | Grouping becomes visible through distance |
| Huge gaps around little content | Wastes viewport and signals false importance | Compress region or add decision-relevant evidence | Area tracks information value |
| Tight labels, loose sections | Micro crowding persists inside an otherwise empty screen | Rebalance from outer whitespace into local readability | Dense but comfortable information field |
| Repeated card gutters | Grid rhythm dominates the product relationship | Merge related modules or create shared axes | Content connects across modules |
| Accidental near-alignment | Makes the design feel unrefined | Snap to a deliberate axis or separate visibly | No ambiguous edges |
| Uniform vertical rhythm | Produces a mechanical, generated texture | Introduce controlled grouping and density changes | Repetition supports, rather than flattens, priority |

## Actionable criticism pattern

Do not say “needs more whitespace.” Say where space is missing or wasted and
which relationship must change:

> The alert title, explanation, and reset control use the same 16 px interval,
> so the action reads as another line of copy. Tighten title-to-explanation,
> then create a larger separation before the control. The block should read as
> one message followed by one deliberate action.

