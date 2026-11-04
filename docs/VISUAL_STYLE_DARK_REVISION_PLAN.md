# Graphite dark — revision plan (v2)

**Status:** Implemented and accepted as the working benchmark; v1 removed 2026-08-23
**Date:** 2026-08-23
**Scope:** Visual revision of the dark specimen sheet. Content model, product
boundary, and information architecture are unchanged.

## 1. Why

Reviewed against four reference surfaces supplied by the user: a monochrome
dark icon-tile set, a dark bento feature-card page, the Lunor contract
dashboard, and a dark analytics tile grid.

Three of the four are marketing surfaces carrying almost no information, so
their restraint is inexpensive. Lunor is the only real product UI in the set and
is the relevant benchmark for information behaviour: it is dense, useful, and
still almost entirely monochrome. Material and restraint come from all four;
information behaviour comes from Lunor.

## 2. Findings against v1

| Dimension | Reference behaviour | v1 behaviour |
|---|---|---|
| Surface definition | Soft light — gradient, inner top glow, faint vignette; borders nearly invisible | Every surface outlined with a visible 1 px stroke |
| Colour | Effectively monochrome; the bento page spends its entire colour budget on one card | Five hues on one sheet: green, blue, amber, red, yellow |
| Technical garnish | Crosshairs, ticks, grids present at roughly 5 % opacity — texture, not content | The same motifs at full strength, reading as information |
| Focal hierarchy | Exactly one bright point per tile | Three or four equally bright elements per module |
| Text | Minimal; Lunor labels a number and stops | Category line, title, right meta, and footnote on every module |
| Base tone | Roughly #171717–#262626 | #090B0A canvas; the olive cast reads murky at that depth |

**Accessibility defect.** The 9 px footnote grey `#6E776D` measures 4.15:1 on
`#090B0A`, below the 4.5:1 AA threshold for small text. It is the most repeated
text on the sheet. The fix and the aesthetic fix coincide: most of it should not
be on the canvas at all.

## 3. Changes

### 3.1 Tone

| Role | v1 | v2 |
|---|---|---|
| Canvas | `#090B0A` | `#121412` |
| Plane | `#171B19 → #101413` | `#1F221F → #1A1D1A` |
| Inset stage | `#0B0E0D` | `#161816` |
| Plane border | `#272D28` | `#292D29` |
| Lens | `#1A1F1C` | `#262A26` |

The border value barely moves while the surface lifts, so the stroke stops
carrying the separation and the inner top light takes over.

### 3.2 Colour — five hues to three

Green and blue are removed. Verified-healthy becomes neutral: a light grey check
on a grey field. Blue information and the blue chrony relationship become
neutral line styles.

Remaining chromatic vocabulary:

- **yellow** — selection, current datum, primary action;
- **amber** — caution / degraded;
- **red** — critical / fault.

Amber and red therefore appear only when something is wrong, which makes the
CAN matrix and the host lanes read as quiet grey structure with a single
unmissable anomaly.

This supersedes the healthy row of `.design/visual-language.md` §5.3 for the
dark expression. See decision D032.

### 3.3 Subtraction

Removed from the canvas:

- **Band 05** — the four corner brackets on the selected node; the `?` glyph and
  the dashed elbow to the camera box; the `ONBOARD` label; the healthy
  check-marks on `intel` and `jetson-1`; the module footer note. A status glyph
  now appears only where status is not nominal.
- **Band 04** — all nine per-lane threshold ticks, replaced by one faint line;
  axis tick stubs; both healthy checks; three footnotes.
- **Band 06** — axis tick stubs; the `AGE` column, redundant with the timestamp;
  the footnote.
- **Band 03** — four column footnotes; slider tick marks; three vertical
  dividers and the header rule, replaced by spacing.
- **Bands 00–02** — the nameplate vertical rule and two spec rows; outer strokes
  on both colour ladders; the third label row under the signal ramp; the hex
  column in state encoding; the twelve-line legend under the material diagram;
  four footnotes.
- **Every module** — the `CATEGORY / SUBCATEGORY` line above each title, and the
  trailing sentences on eyebrows 04, 05 and 06.

Design commentary moves to this document and to `docs/DESIGN_GUIDELINES.md`.
Machine metadata — unit, source, threshold, freshness, timestamp — stays beside
its observation. The cut is commentary out, data in.

### 3.4 Material

- Soft radial glow behind each module's focal object, authored as an SVG radial
  gradient rather than a blurred node.
- Inner top light plus bottom inner shadow on raised elements.
- No border on inset stages; a fill step and an inner shadow are sufficient.
- Optional and colourless: a faint bloom in the page background.

### 3.5 Space and focus

Module padding rises from 24 to 32; band gaps from 48 to 56. Each module resolves
to a single brightest point, reached by removing competition rather than adding
emphasis. The neutral ladder is recessed into a well and loses height so it stops
dominating the sheet.

## 4. Method

v1 was preserved untouched at canvas origin while v2 was built fresh beside it
at x = 1960, so the two could be compared side by side. After review the v1
frame was deleted and v2 moved to the origin; v1's renders under
`.design/renders/visual-style-dark-2026-08-22/` remain the before-state record.

A full-frame `clone_node` of the v1 sheet disconnected the Figwright plugin and
must not be retried; build the sibling rather than duplicating.

## 5. Open

- The relationship legend in band 05 is load-bearing — it defines what solid,
  dashed and dotted mean. Retained on canvas in compressed form pending review.


## 6. Follow-on — chart pass (2026-08-23)

After the v2 sheet was accepted as the working benchmark, the user supplied a
reference chart and asked for the graphs to match it. Every chart in the sheet
was rebuilt against a new specification, `docs/DESIGN_GUIDELINES.md` section 20a,
recorded as decision D033.

The visible changes: charts lost their inset containers, gained a left y-label
gutter and full-width horizontal gridlines, and their flat translucent area
tints were replaced with 45° diagonal hatching. The primary series went to 2 px
white. Vertical ghost gridlines inside the material-strata miniature were
replaced with horizontal ones so it obeys the same rules.

Two rules in that spec carry meaning rather than style — hatch only on a
zero-based axis, and curve shape must match how the data was observed — and are
the reason the CPU trace and the CAN rate trace look deliberately different from
each other.


## 7. Colour temperature — candidates (resolved: B · Iron)

The user asked for the greys to leave neutral and take a slight cold tint. Three
candidates are built as live tiles on the option board beside the sheet, each
carrying its own canvas, plane, border, inset and lens at identical lightness so
only hue varies.

| Role | A · Slate (218°) | B · Iron (210°) | C · Basalt (262°) |
|---|---|---|---|
| Canvas | `#111318` | `#121416` | `#131218` |
| Plane top | `#1E2128` | `#1F2225` | `#201F28` |
| Plane bottom | `#191C22` | `#1A1D20` | `#1B1A22` |
| Border | `#272B34` | `#292D31` | `#2B2935` |
| Inset | `#15171C` | `#16181B` | `#17161D` |
| Gridline | `#262A32` | `#272B2F` | `#292733` |
| Lens top | `#292D36` | `#2A2E32` | `#2C2A36` |
| Lens bottom | `#22262E` | `#23272B` | `#25232E` |
| Lens border | `#383D48` | `#3A3F44` | `#3C3A4A` |

Note that the current sheet is not neutral — it carries a slight **green** cast
inherited from the brand neutral ramp, where `#242925` and `#394039` sit near
hue 120°. All three candidates move away from that, which is why even B reads as
a change.

**Recommendation: A · Slate.** It is unmistakably cold without becoming a colour,
it reads closest to the reference set, and a cool ground makes the warm signal
yellow and caution amber sit further forward. B risks being invisible against
the current green-grey; C is attractive but reads consumer rather than
industrial, and its violet ground sits closer in hue to the red critical state.

Applying a choice means re-importing most module SVGs, since inset backgrounds,
gridlines, dividers, field and control fills are baked into them. It is one
pass, not an incremental change.


## 8. Third pass — iron, saturated states, outline selection (2026-08-23)

Option B (Iron) was chosen and applied across every module. Three further
changes went in at the same time, recorded as D034 and guideline 19a:

- caution and critical were saturated to `#FF8A3D` and `#FF5765`, giving a warm
  progression at 48° / 24° / 355° that separates by hue rather than lightness;
- selection became an outline, a tint and a radial falloff, with solid yellow
  reserved for one primary action per region;
- the selected causal path in band 05 became a stacked triple stroke with a
  filled dot at every bend, and every object not on that path was stepped back
  one level in contrast.

Further subtraction in this pass: the brand neutral ramp was replaced by the
graphite surface set it actually uses, the button-size row and breadcrumb and
evidence strip left band 03, band 04B lost a legend item, and band 07 dropped
from five items per column to four.
