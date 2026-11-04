# Design decision log

## D001 — Product boundary

**Status:** Accepted  
**Decision:** The interface covers platform-layer introspection and diagnostics.
Fleet, mission, route, checkpoint, and autonomy operations are excluded.  
**Reason:** The users are engineers inspecting compute nodes, subsystems,
network, services, and machine state.

## D002 — Primary visual direction

**Status:** Accepted  
**Decision:** Adopt **Signal Instrumentation** as the primary direction.  
**Reason:** It reconciles the references' strongest shared traits—instrument
precision, modular bento composition, and controlled depth—without copying a
single source.

## D003 — Light and dark relationship

**Status:** Accepted  
**Decision:** Light is the default expression; **Night Console** is a dark
expression of the same tokens, geometry, typography, and component API.  
**Reason:** The reference set contains compelling light and dark systems. A
single component model avoids fragmentation.

## D004 — Yellow usage

**Status:** Accepted  
**Decision:** ExRobotics yellow carries primary action, selection, active probe,
current datum, and attention. It is not a general background color.  
**Reason:** Scarcity preserves the brand signal and prevents warning fatigue.

## D005 — Glass and blur

**Status:** Accepted  
**Decision:** Limit glass to navigation, overlays, command surfaces, and
selected floating controls. Keep telemetry and data work surfaces opaque.  
**Reason:** The light glass reference contributes useful depth but would reduce
legibility and reproducibility if applied indiscriminately.

## D006 — Typography

**Status:** Accepted  
**Decision:** Keep Space Grotesk for hierarchy, Inter for interface copy, and
Roboto Mono for machine data. Do not introduce a decorative segmented font.  
**Reason:** The existing hierarchy already captures the references' contrast
between human labels and instrument data with better readability.

## D007 — Reference preservation

**Status:** Accepted  
**Decision:** Preserve originals under `reference/`; store interpretation in
documentation rather than modifying or annotating source files.  
**Reason:** This keeps provenance intact and allows future re-analysis.

## D008 — Reference synthesis specimen

**Status:** Superseded by D010 and D011  
**Decision:** Add a `Signal Instrumentation` specimen to the foundations page
using the existing Navigation Item and Platform Tile component APIs. The
specimen combines a dark instrument rail, light contextual navigation,
floating gradient tiles, dependency topology, and a yellow selected-probe
surface.  
**Reason:** The specimen remains useful as an implementation baseline, but its
gradient-led summary cards do not yet express the revised chassis, bento,
low-relief edge, and micro-instrument requirements.

## D009 — Reference colors are excluded

**Status:** Accepted  
**Decision:** Extract composition, geometry, depth, typography, data treatment,
and interaction character from the supplied references, but do not sample or
adopt their colors.  
**Reason:** The references are visual-style evidence. ExRobotics already has an
authoritative palette, led by its yellow signal color.

## D010 — Layered instrument chassis is the primary signature

**Status:** Accepted  
**Decision:** Define Signal Instrumentation primarily through a coherent
application chassis, nested navigation strata, a continuous mixed-span bento
workbench, low-relief edges, and tiles with meaningful micro-instruments.  
**Reason:** The prior description overemphasized gradients and generic modular
cards. Those traits alone do not reproduce the references' recognizable visual
structure.

## D011 — Existing screens are drafts, not identity evidence

**Status:** Accepted  
**Decision:** Existing Figma screens may be reused structurally, but they are not
the visual benchmark when they conflict with the revised identity guide.  
**Reason:** The current screens do not yet express the reference silhouette,
layering, tile proportions, edge character, or diagnostic-instrument language.

## D012 — Expanded radius hierarchy

**Status:** Accepted  
**Decision:** Add panel (20 px), instrument (24 px), and chassis (28 px) radii
above the existing small/control/card/expressive scale. Internal diagrams,
tables, and controls continue to use smaller, more exact geometry.  
**Reason:** The contrast between a soft containing object and hard technical
content is a consistent cross-reference signature.

## D013 — One active platform context

**Status:** Proposed  
**Decision:** Organize the interface around one explicitly selected robot
platform. A selector may switch the active target, but the product will not
present a fleet-level dashboard.  
**Reason:** Engineers need unambiguous identity, scope, state, and action
ownership without introducing fleet-management concepts.

## D014 — Platform graph as the primary mental model

**Status:** Proposed  
**Decision:** Use a shared object and relationship model across navigation,
search, topology, inspector, events, logs, configuration, and actions.  
**Reason:** Platform failures propagate across compute, network, subsystem, and
software boundaries. Showing those dependencies supports diagnosis better than
isolated dashboard categories.

## D015 — Three disclosure layers

**Status:** Proposed  
**Decision:** Structure work as Glance, Investigate, and Evidence. Use the
overview for posture and impact, an attached inspector for contextual
drill-down, and full detail or a diagnostics drawer for raw evidence.  
**Reason:** This preserves context and makes dense engineering information
available without presenting all of it at once.

## D016 — Initial shell uses one navigation panel

**Status:** Proposed  
**Decision:** Start with a persistent global header, one 208–248 px context
navigation panel, a 12-column workbench, a right object inspector, and a bottom
diagnostics drawer. Add a utility rail only if a genuine second navigation
level emerges.  
**Reason:** The current product model has clear destinations but does not yet
justify two independent navigation layers.

## D017 — Overview prioritizes causality and freshness

**Status:** Proposed  
**Decision:** Make platform/dependency posture, causal issues, synchronized
resource history, subsystem posture, and recent change the initial Overview
composition. Treat stale, unknown, and offline data as first-class states.  
**Reason:** Engineers need to locate consequential faults and judge evidence
quality, not scan generic KPI cards.

## D018 — Safety control remains provisional

**Status:** Proposed; safety review required  
**Decision:** Treat safety state as a persistent cross-cutting concern, but do
not finalize the name or activation behavior of the requested `safety stop`
until the underlying function, command path, authority, scope, reset, and
restart behavior are classified. Request, acknowledgement, stopped state,
reset, and restart remain distinct.  
**Reason:** A prominent software control must not imply emergency-stop or
safety-rated behavior that the actual robot architecture does not provide.

## D019 — Platform facts have a separate source of truth

**Status:** Accepted  
**Decision:** Maintain the on-board platform inventory and relationships in
`data/platform-system.yaml`, with human explanation and diagrams in
`docs/PLATFORM_SYSTEM_MODEL.md`. Unknown values remain explicit.  
**Reason:** Screen copy and diagrams should be generated from stable system
facts instead of repeatedly reconstructing the robot from conversational prose.

## D020 — Stable visual topology precedes text summaries

**Status:** Accepted  
**Decision:** Use a stable spatial schematic for LAN, compute, CAN, subsystems,
uplinks, cameras, software placement, and selected dependency paths. Yellow
means selection/current signal; orange means degraded/warning.  
**Reason:** State presented on an accurate system representation reduces search,
supports causal reasoning, and is faster to interpret than detached status
lists or generic cards.

## D021 — Task-led redesign replaces category-led dashboards

**Status:** Accepted and implemented
**Decision:** Replace the current six-category navigation and repeated screen
templates with an Inspect → Diagnose → Change flow. Represent Physical,
Network, Software, Time and Integration as lenses on one stable platform map.
Collapse the inspector and evidence drawer until they are needed.  
**Reason:** The current composition spends too much space on sparse,
over-specific category cards and does not guide the user from platform posture
to cause, evidence, change and observed result.

## D022 — Drive Stall is a distinct latched protection state

**Status:** Accepted as a functional requirement; implementation details open  
**Decision:** Model Drive Stall as a motor-overload-triggered, latched
motor-protection state that requires intentional manual deactivation. Keep it
separate from Safety Stop and from any later drive enable or restart action.
Do not assume that manual deactivation is remotely available until its
controller, authority, prerequisites and action path are verified.  
**Reason:** The UI must keep showing the condition after overload current
subsides, support a truthful recovery lifecycle, and avoid conflating motor
protection with a safety function or automatic restart.

## D023 — Functional requirements derive from the task-flow components

**Status:** Accepted  
**Decision:** Maintain `UI_FUNCTIONAL_REQUIREMENTS.md` as the capability and
interaction baseline. Map each capability to the implemented System Node,
stable map, lenses, Attention Rail, comparison strip, Evidence Strip/Drawer
and Change review before creating new screens.  
**Reason:** A component-backed requirement model keeps future POI, CAN, API,
cybersecurity, ROS 2/DDS, compute and storage work consistent while the system
inventory grows.

## D024 — Visual Style v2 is promoted through archive-safe siblings

**Status:** Accepted and implemented
**Decision:** Preserve the pre-v2 foundations specimen, component stage and
nine-screen storyboard unchanged, and promote the stricter Signal
Instrumentation expression through dated v2 siblings on the same three Figma
pages. Persistent data surfaces use opaque neutral materials, one-pixel borders
and inset contours; yellow remains the active signal; stronger elevation is
reserved for selected or temporary ownership.
**Reason:** Append-only promotion keeps earlier design reasoning recoverable
while allowing the live reference direction to adopt the chassis, continuous
bento, micro-instrument and low-relief grammar consistently.

## D025 — Editorial focus is an auxiliary visual layer

**Status:** Accepted
**Decision:** Add the 2026-08-20 supplied editorial mobile composition and the
Solar21 application case study to the durable reference set. Use their
isolation, annotated storytelling, hardware context, and simplified-view
principles for onboarding, guided diagnosis, incident explanation, focus mode,
and visual-identity presentation. Do not use their colors as design tokens or
replace the operational bento workbench with device-mockup theater.
**Reason:** These sources add a valuable spacious focus state and explanatory
narrative to Signal Instrumentation while preserving the density, legibility,
truthfulness, and ExRobotics-yellow semantics required by the engineering UI.

## D026 — References enter through a provenance-to-system pipeline

**Status:** Accepted
**Decision:** Process new inspiration through `REFERENCE_INTAKE_METHOD.md`:
preserve provenance, analyse without color first, classify each observation as
adopt/translate/presentation-only/reject, synthesize across sources, and promote
only into documented principles, component rules, tokens where justified, and
falsifiable acceptance tests. Store inaccessible sources as queued rather than
substituting similar search results or inventing visual claims.
**Reason:** This turns visual browsing into a reproducible identity-building
practice and prevents attractive but unrelated fleet, mission, autonomy, or
generic dashboard patterns from diluting Signal Instrumentation.

## D027 — Visual Style v2 becomes the UX baseline; v3 rebuilds visual fidelity

**Status:** Accepted and implemented

**Decision:** Reclassify the v2 foundations, components, and nine-screen
storyboard as the preserved UX/content baseline. Visual Style v3 was built as
archive-safe siblings using the sequence in `VISUAL_STYLE_V3_PLAN.md`: chassis
and material hierarchy, heterogeneous micro-instruments and live topology,
three critical stress-test frames, paired light identity expression, and the
remaining six operational states. The implementation is mapped in
`FIGMA_IMPLEMENTATION.md`.

**Reason:** The v2 implementation contains the correct task flow and platform
geography but fails the chassis, bento, instrumentation, density, greyscale,
and yellow-allocation gates. Restyling the existing white cards would not fix
the structural mismatch with the references.

## D028 — Operational states change instruments and task planes, not only color

**Status:** Accepted and implemented

**Decision:** Keep the platform geography and graphite chassis stable across
the v3 storyboard, while each state introduces a domain-specific visual object:
degraded dependency path, shared-clock evidence, VRRP failover path, runtime
ownership stack, chrony uncertainty envelope, controlled change-review plane,
or stale-data hatching and duration. Yellow owns current focus and deliberate
action; orange owns degraded or caution state. Selection and degradation remain
independently legible through brackets, dashed paths, patterns, labels, and
time values.

**Reason:** Engineers should retain spatial orientation while moving from
Inspect to Diagnose to Change, and must be able to distinguish state without
depending on hue or rereading a category dashboard.

## D029 — Interface directions are maintained as parallel concepts before promotion

**Status:** Accepted

**Decision:** Store alternative interface concepts under `docs/concepts/` with
stable `C##` identifiers. A concept is an exploration input, not canonical UX
architecture, and does not supersede other concepts merely because it is
documented. Promote a concept only through an explicit user decision followed
by updates to the relevant canonical architecture, visualization, interaction,
and design guidance.

The first retained concept is C01, the topology-led diagnostic workflow derived
from the useful workflow logic in Visual Style v4.

**Reason:** The project will explore multiple organizing models. Keeping their
propositions, strengths, risks, and invariants separate prevents an early idea
from becoming an accidental default and makes later comparison and synthesis
more deliberate.

## D030 — Graphite is built and reviewed first, as a specimen sheet rather than screens

**Status:** Proposed — awaiting user review (2026-08-22)

**Decision:** The Figma file was reset to a clean slate, so the dark expression
is being re-established on its own before any screens are composed. Page
`01 Visual Style — Graphite (Dark)` holds one specimen sheet spanning the
nameplate, surface/colour/state, type/material/geometry, control grammar,
instrument specimens, platform field with attached lens, the two approved
spatial models, evidence datum, and intent/exclusions/open questions. No
interface is composed on this page.

This deliberately inverts D003's "light is the default expression" sequencing
for the build order only. Light remains the paired expression and must be
derived from the same composition, geometry, and component model once graphite
is accepted. D003 itself is unchanged.

**Reason:** The user asked for a dark-only style to react to, and a specimen
sheet exposes material, state, and instrument grammar for critique without
committing to an information architecture that has not been agreed.

## D031 — The dark expression needs its own state values and surface recipe

**Status:** Proposed — awaiting user review (2026-08-22)

**Decision:** Record dark-mode state colours and a dark surface recipe as
`primitives.*Dark`, `statusDark`, and `surfaceDark` in
`tokens/exrobotics-ui.tokens.json`. States lift to `#34C085` healthy,
`#5B9BFF` information, `#E08A2E` caution, and `#E86A63` critical, each with a
dim field and a mid "mark" tone for matrix and bar fills. Surfaces are defined
by a two-step plane gradient `#171B19 → #101413`, a 1 px inside stroke
`#272D28`, a 5.5 % white inner top light, and a broad low shadow, with charts
and tables inset on `#0B0E0D`.

**Reason:** The light `status.*` 600 values (`#177A4D`, `#2968C8`, `#C66B0A`,
`#B93A36`) fall to roughly 2.5–3:1 on `#090B0A` and cannot carry state on the
dark canvas. The lifted values clear 4.5:1 against both canvas and surface. The
surface recipe makes the edge stack, not the shadow, the primary separator, as
`.design/visual-language.md` §7 requires.

**Open risk:** Caution orange `#E08A2E` and lead yellow `#F5C400` are adjacent
in hue. The specimen keeps them apart with the mandatory triangle glyph and by
never using yellow for status, but the pairing needs a human judgement before
it is accepted.

## D032 — Verified-healthy is neutral in the dark expression

**Status:** Proposed — implemented in the v2 sheet, awaiting user review
(2026-08-23)

**Decision:** Remove green and blue from the dark expression. Verified-healthy
is carried by a light-grey check glyph on a neutral field rather than by
`#34C085`; information/compute and chrony relationships are carried by line
style and label rather than by `#5B9BFF`. The dark chromatic vocabulary reduces
to yellow for selection, current datum and primary action, amber for caution,
and red for critical.

This supersedes the healthy and information rows of
`.design/visual-language.md` §5.3 for the dark expression only. The light
expression is unchanged and still needs its own review.

**Reason:** Colour spent on the nominal case is colour unavailable to the
exception. In the v1 sheet the CAN matrix read as a wall of green with the real
anomaly buried inside it, which inverts the intent recorded in D028 and in the
incident-map reference — healthy structure should be quiet so that a fault and
its causal path dominate. Removing two hues also brings the sheet closer to the
restraint of the reference set the user selected.

**Consequence:** Status still never depends on colour alone. Healthy keeps its
check glyph and label; the absence of amber or red is itself the signal. Amber
and red now appear on a screen only when something is actually wrong.

**Reverses if:** users read a neutral healthy state as "unknown" or "not
checked" rather than "verified". Unknown and stale already have their own dashed
and clock treatments, but the distinction needs testing with real engineers.


## D033 — Chart style: no container, hatched area, curve shape must match observation

**Status:** Proposed — implemented across every chart in the graphite sheet,
awaiting user review (2026-08-23)

**Decision:** Adopt the chart specification recorded in
`docs/DESIGN_GUIDELINES.md` section 20a, extracted from a reference chart the
user supplied. Charts lose their inset container entirely and sit directly on
the module plane; horizontal gridlines and a left label gutter define the field.
The primary series is a 2 px white line and its area is filled with 45° diagonal
hatching rather than a flat tint.

Two of the rules are semantic rather than stylistic:

- hatched area is used only when the axis includes zero, because area encodes
  magnitude measured from nothing — a fitted axis gets a line alone;
- curve shape must match how the data was observed: gentle smoothing for
  continuously sampled telemetry, plateaus with short eased transitions only
  where the value genuinely steps.

**Reason:** the reference reads as an instrument rather than a dashboard widget,
and the hatch is the single detail most responsible for that. Adopting it
without the two semantic rules would have produced exactly the design theater
this system forbids — plateau curves imply a value was held constant, and an
area fill on a fitted axis overstates magnitude.

**Consequence:** the CPU trace uses a 0–60 % axis with hatching and a smoothed
curve; the CAN rate trace uses a fitted 35–55 Hz axis, a plateau curve, and no
fill. Where a threshold falls outside a fitted axis it is stated in the module
header instead of stretching the axis to reach it.

**Implementation note:** Figma imports SVG `clipPath` as a native vector mask,
which makes exact hatching possible. SVG `pattern` fills do not import.


## D034 — Iron tint, saturated warm states, and outline selection

**Status:** Proposed — implemented across the graphite sheet, awaiting user
review (2026-08-23)

**Decision:** Three linked changes to the dark expression.

**Iron tint.** Surfaces move off the brand neutral ramp to a cold neutral at
hue 210°, saturation 18 %: canvas `#121416`, plane `#1F2225 → #1A1D20`, border
`#292D31`, inset `#16181B`, lens `#2A2E32`. Mid-grey text cools to match
(`#CBD1D6`, `#8B939B`, `#6D757D`). Chosen from three candidates rendered side by
side; the alternatives were Slate at 218° and Basalt at 262°.

**Saturated warm states.** Caution moves from the muted `#E08A2E` to `#FF8A3D`
and critical from `#E86A63` to `#FF5765`. With signal yellow at `#F5C400` the
three sit at 48°, 24° and 355° — all fully saturated, so they separate by hue
rather than by lightness. Matrix and bar fills use dimmed derivatives
(`#A05B23`, `#A83A48`) so a saturated hue never covers a large area.

**Outline selection.** Selection becomes a 1 px yellow border, a 7 % tint and a
soft radial falloff, with the label staying white. Solid yellow is reserved for
the single primary action in a region. Recorded as guideline 19a.

**Reason:** the greys were not neutral but slightly green, inherited from the
brand ramp at hue 120°, which read as murky against the cool references. A cold
ground also pushes the warm signal and caution colours forward. The muted orange
was the least attractive element on the sheet; saturating it made it both more
beautiful and easier to separate from yellow. Filled-yellow selection states
read as dated — every reference surface treats selection as a lit outline.

**Consequence:** the dark surfaces no longer derive from
`primitives.neutral`. That ramp remains the light expression's and is unchanged;
the dark set is recorded separately as `primitives.graphite`. Light and dark are
now paired by geometry, type and composition rather than by shared greys, which
is a real divergence from D003 and needs a decision when light is built.


## D035 — Families are a content classification, not a style choice

**Status:** Adopted — audited across the graphite sheet (2026-08-24)

**Decision:** Bind each type family to a class of content rather than to a
visual role. Space Grotesk names things, Inter carries language, Roboto Mono
carries machine truth and nothing else. Sizes, tracking and colour are fixed per
token in `docs/DESIGN_GUIDELINES.md` section 8a. Analytic modules take the
shared anatomy in section 10a: title, eyebrow, readout with an optional status
annotation, stage, source line.

**Reason:** the sheet had drifted into setting prose in Roboto Mono — module
meta, notes, legends, questions. Each instance looked defensibly "technical",
and together they made the work read as a specification dump rather than a
product. Stating the rule as a test that can be applied to any string — does it
contain a measured value or identifier? — removes the judgement call that let
the drift happen.

The instrument anatomy exists for a second reason: the three instruments in band
04 had different anatomies, so nothing carried across them. Giving each one an
eyebrow, one large reading and an attached status annotation made them read as a family, and
gave each a deliberate entry point rather than a wall of small values.

**Consequence:** type is now larger and sparser. The title rises to 22 px with
negative tracking, captions to 12 px Inter, and floating labels become attached
annotations or tokens. Where a module previously carried five sizes it now
carries three. D038 later removed the pill as a mandatory status container.

## D036 — Approve two diagnostic spatial models

**Status:** Adopted (2026-08-24)

**Decision:** The canonical dark visual-style page carries exactly two approved
spatial models: **Bus schematic** and **Hex cell cluster**. Bus schematic shows
literal connectivity and the causal path along orthogonal rails. Hex cell
cluster shows compute-core composition and membership, with drawn edges as the
only authoritative connections. The Layered strata exploration is removed from
the active file and from all documentation that presents it as an option.

**Reason:** the bus and hex models answer different, repeatable diagnostic
questions without changing object identity or incident state. Layered strata
introduced a third visual grammar without adding a relationship that could not
be expressed by the other two, and its presence made experimental options look
equally canonical.

**Consequence:** future topology modules choose a model by diagnostic question,
reuse the shared diagram material and content-class typography, and retain the
same names, states, selection, and evidence when switching views. A third model
requires a new recorded relationship and decision. Exact reusable geometry is
in `spatialModelsDark`; semantic rules and exceptions are in guideline 11.3a.

## D037 — Concentrate density into shared evidence fields

**Status:** Adopted (2026-08-24)

**Decision:** Recompose the canonical graphite sheet around one dominant
platform field and five macro chapters. Related instrument specimens now share
one continuous chassis; the two approved spatial models and the shared time
datum share one evidence field. Secondary persistent modules lose drop shadows,
redundant closed borders, and repeated section ceremony. The control grammar
shows canonical states at full contrast while secondary variants recede.

**Reason:** The previous sheet was coherent but visually overworked. Eight
nearly equal bands, repeated rounded cards, and locally valid accent states
distributed similar visual weight across the whole page. The strongest
references concentrate complexity in one truthful object and keep its shell,
annotations, and neighboring evidence quieter.

**Consequence:** Reuse the calm-composition rules in guideline 18b. Composition,
spacing, shared-surface ownership, and page-level accent budgeting are resolved
before component polish. Existing `surfaceDark`, `typographyDark`,
`instrumentDark`, `selectionDark`, and `spatialModelsDark` values were unchanged
by this composition decision; D038 subsequently refines their implementation.

## D038 — Mature graphite into an industrial evidence atlas

**Status:** Adopted (2026-08-24)

**Decision:** Replace the soft, illuminated specimen grammar with a more
editorial industrial evidence atlas. The canonical page now uses one dominant
platform field, matte persistent planes, restrained 8–10 px evidence-field
radii, unequal instrument spans, an attached selected-object ledger, and exact
diagram rails. Depth is reserved for ownership. Full capsules are reserved for
removable tokens; status is glyph plus language plus machine evidence. Yellow
acts as a cursor or leading edge, not a coating.

**Reason:** Even after D037 reduced card count, the inherited inner-glow stack,
large radii, repeated pills, and materialized rails still made technically
correct work feel toy-like. The strongest references achieve authority through
large-scale contrast, sparse editorial orientation, matte surfaces, precise
alignment, and selective material—not through more effects. Full-size review
also exposed rails crossing labels in both spatial models, a small defect with
disproportionate impact on perceived craft.

**Consequence:** Guideline P6, sections 6.2a, 10a, 12, 18b, and 19a are refined.
`surfaceDark`, `selectionDark`, `typographyDark`, `instrumentDark`, and
`spatialModelsDark` now record the exact matte implementation and the editorial
specimen-scale exception. The former active sheet is recoverable on page `0:1`;
the new canonical root is `93:417` on page `93:2`.
