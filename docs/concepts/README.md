# Interface concept directions

This directory holds alternative conceptual directions for the ExRobotics
engineering interface. Concepts are exploration inputs, not approved product
architecture. Several concepts may coexist, conflict, or later be combined.

A concept becomes canonical only when the user explicitly promotes it and the
relevant rules are incorporated into `UX_ARCHITECTURE.md`,
`SYSTEM_VISUALIZATION_SPEC.md`, and `DESIGN_GUIDELINES.md`.

## Concept index

| ID | Direction | Status | Core proposition |
| --- | --- | --- | --- |
| C01 | [Topology-led diagnostic workflow](C01_TOPOLOGY_LED_DIAGNOSTIC_WORKFLOW.md) | Exploratory; retained from the v4 workflow concept | Use one stable model of the robot's connectivity and dependencies to carry the engineer from orientation through diagnosis, change, and verification. |
| C02 | [Enclosure-led hardware workbench](C02_ENCLOSURE_LED_HARDWARE_WORKBENCH.md) | Exploratory | Begin with physical containment and configuration, then trace the first unproven or failing transition from expected hardware through power, communication, health, change, and observed recovery. |
| C03 | [Evidence-led diagnostic notebook](C03_EVIDENCE_LED_DIAGNOSTIC_NOTEBOOK.md) | Exploratory | Begin with a time-scoped engineering question, align facts and evidence, test explicit hypotheses, and preserve proof through change and before/after verification. |

## Quick comparison

| Dimension | C01 — Topology-led | C02 — Enclosure-led | C03 — Evidence-led |
| --- | --- | --- | --- |
| Primary entry | Platform posture or dependency path | Physical zone, enclosure, module, or configuration mismatch | Symptom, recent change, object, or engineering question |
| Continuity anchor | Stable platform geography | Containment breadcrumb and readiness chain | Robot/object/time scope and evidence set |
| Default primary instrument | Platform topology | Source-qualified equipment map | Synchronized diagnostic notebook |
| Product fit | General platform orientation and cross-domain diagnosis | Service, as-built reconciliation, power/attachment faults | Intermittent, ambiguous, or before/after investigations |
| Cognitive ergonomics | Spatial memory and one dominant causal path | Recognition by physical location and first failing readiness transition | Chronological reasoning, explicit facts/gaps, and falsifiable hypotheses |
| Diagnostic continuity | Selection and path survive lens, evidence, and change | Physical target and readiness transition survive drill-down and change | Question, time range, evidence pins, and expected result survive change |
| Safety/change posture | Shows path impact and preserves action context | Makes shared power domains and incompatible variants explicit | Keeps motivation, preconditions, action events, and verification together |
| Default disclosure | Whole platform, one dominant path | Robot/enclosure posture, then selected internals | Current observations and evidence readiness, then selected lanes |
| Density | Medium-high; graph can become crowded | Progressive; low at robot level, high inside one enclosure | Potentially high, controlled by question-scoped evidence lanes |
| Extensibility | Strong for new objects and relationship types | Strong when containment and hardware revisions are maintained | Strong when new sources have timestamps, provenance, and cadence contracts |
| Relative implementation cost | High: stable graph layout and relationship grammar | High: source-qualified equipment geometry and variant model | Very high: correlation, evidence assembly, notebook state, and retention policy |
| Principal risk | Graph noise or false physical implication | False mechanical precision or deep hierarchy | Evidence overload or loss of physical orientation |

## Rules for future concepts

- Give each concept a stable `C##` identifier and its own Markdown file.
- State what problem the concept solves and what it deliberately does not solve.
- Separate interaction or information-architecture ideas from visual styling.
- Include its workflow, spatial model, information-disclosure model, strengths,
  risks, and unresolved questions.
- Do not silently merge a concept into the canonical architecture.
- Compare concepts on product fit, cognitive ergonomics, diagnostic continuity,
  safety, density, extensibility, and implementation cost before promotion.
