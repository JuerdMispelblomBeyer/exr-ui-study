# Consistency

Consistency is predictable meaning and shared visual grammar. It is not the
repetition of one card template across every screen.

## Inspect the design system

After visual inspection, use FigWright to check:

- local variables and their semantic names/modes;
- paint, text, effect, and grid styles;
- fonts actually in use;
- attached local components and component sets;
- public component properties and intended variants;
- duplicated or detached primitives that imitate existing components;
- screen-family state behavior.

Do not penalize a deliberate exception merely because it is new. Ask whether
the exception has a recurring semantic role and fits the existing grammar.

## Three-layer audit

### Foundation consistency

Check typography roles, semantic colors, spacing tiers, radius ladder, edge
grammar, shadows/elevation, grids, and icon construction. Flag raw values only
when an appropriate token exists or the drift is visibly harmful.

### Component consistency

Check anatomy, states, affordances, labels, targets, and interaction meaning.
The same visual treatment must not mean “selected” in one region and “warning”
in another.

### Screen-family consistency

Compare sibling frames. Shared navigation, type, surface, edge, and signature
moves should make them related. The dominant composition should change with
the task. Identical page skeletons are repetitive, not coherent.

## Failure patterns and corrections

| Failure | Why it matters | Corrective action | Desired outcome |
|---|---|---|---|
| Token-correct but visually weak | System compliance preserves a bad rule | Identify the system rule causing the defect; revise centrally if recurring | Consistency improves quality instead of freezing it |
| Detached lookalike controls | States drift and maintenance becomes brittle | Replace with attached instances and public properties | One reliable interaction language |
| One layout reused everywhere | Screens feel template-generated | Preserve grammar but recompose around each task's dominant object | Coherent family with purposeful variation |
| Unexplained exception | Looks accidental and erodes trust | Map it to an existing role or define/document a recurring new role | Exceptions feel authored |
| Mixed edge/radius dialects | Makes regions look imported | Assign geometry by surface/component role | Material hierarchy is predictable |
| Over-unification | Removes necessary differences between evidence, action, and navigation | Restore role-specific density, geometry, and hierarchy | Shared system, differentiated behavior |

## Scoring boundary

Score visible and structural coherence here. Score memorability and
product-specific character under Distinctiveness. A highly standardized,
anonymous dashboard may earn a high Consistency score and still fail overall.

