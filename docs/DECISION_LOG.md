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
