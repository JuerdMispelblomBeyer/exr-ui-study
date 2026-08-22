# Typography

Typography establishes voice, hierarchy, density, and credibility. Audit the
file's existing text styles, fonts, available weights, and numeric conventions
before defining anything new.

## 1. Assign roles before sizes

Use only roles the product needs:

| Role | Job | Typical treatment decision |
|---|---|---|
| Display | rare identity or orientation moment | distinctive scale/face; never routine chrome |
| Page title | identifies the current workspace or object | strongest persistent human-language role |
| Section title | divides major tasks or evidence groups | quieter than page title; aligned consistently |
| Body | explanation and readable prose | comfortable measure and line height |
| Interface label | controls, navigation, table headers | compact, stable, high legibility |
| Data | values, units, IDs, time, code, paths | tabular/mono where useful; strict alignment |
| Annotation | contextual evidence attached to an object | compact but not low-contrast |
| Action | describes a verb | weight and contrast appropriate to priority |

Avoid creating a distinct size for every text node. New styles are justified by
a recurring semantic role, not by a one-off visual preference.

## 2. Create hierarchy through contrast, not noise

Adjacent roles should differ through at least two relevant channels:

- size;
- weight;
- family;
- case;
- tracking;
- color/opacity;
- placement and whitespace.

Do not make every label semibold. Weight loses meaning when it is universal.
Do not use uppercase merely to make weak hierarchy feel technical.

## 3. Control reading measure

- Body copy: keep a readable line length; narrow it for annotations and widen
  it only when scan behavior justifies it.
- Headings: balance wrapping intentionally. Avoid single orphan words.
- Tables and dense UI: shorten labels or provide disclosure rather than
  compressing text below a legible size.
- Buttons: use explicit verbs; do not rely on icon-only actions unless the icon
  is established and accessible.

Test production-length labels, localization expansion, long identifiers, and
mixed numeric units before approving the layout.

## 4. Treat machine data as a system

For numbers, timestamps, IDs, paths, versions, rates, ports, and units:

- use tabular figures or a mono/data face when it improves comparison;
- align decimals and units consistently;
- keep value and unit close but typographically distinct;
- distinguish current value, range, threshold, and comparison;
- avoid oversized numbers that have no decision value;
- do not format fake precision such as `74.000%` unless the system truly has it.

When a table or trace is dense, use stable alignment and restrained contrast
instead of shrinking everything.

## 5. Make typography part of the visual signature

Choose one or two controlled moves:

- a distinctive display/section contrast;
- editorial scale tension between a large focal statement and compact evidence;
- a data face with disciplined alignment;
- unusual but repeatable caption placement;
- object-attached annotation typography.

Do not create distinction by mixing many unrelated fonts. A third family must
have a job that the first two cannot perform.

## 6. Figma execution

- Reuse existing text styles and typography variables first.
- Create a new shared style only after identifying a recurring missing role.
- Apply real font family/style; never leave newly created text in FigWright's
  fallback font.
- Use one text node for inline emphasis and style ranges rather than splitting
  a sentence into manually positioned fragments.
- Name styles by semantic role, not appearance: `Type/Data/Value`, not
  `Small Grey Mono`.

## 7. Typography QA

Inspect the screenshot at full size and at 50%:

1. Can the page title, current object, primary evidence, and action be found
   without reading every label?
2. Are any secondary labels louder than the data they explain?
3. Are line breaks deliberate?
4. Do values compare cleanly?
5. Are controls legible without excessive weight?
6. Does the interface still have a clear voice when color is removed?
7. Is any important content represented by placeholder or lorem-ipsum text?

Fix hierarchy and content before tuning tracking by fractions.
