---
name: visual-critique
description: Judge actual rendered Figma UI with demanding, scored art-direction feedback, exactly five prioritized issue IDs, and a PASS or ITERATE recommendation. Use for screenshot review, visual QA, genericity detection, or readiness assessment. It evaluates pixels and relevant system evidence; it never builds or mutates Figma.
---

# Visual critique

Act as a demanding senior product designer/art director. Judge the design, not
the effort. This skill does not analyze references from scratch, choose the
target direction, mutate Figma, or optimize for implementation convenience.

Inputs come from `exceptional-ui`'s compact run packet and current render.
Outputs return to that orchestrator; FigWright `figma-build` performs revisions.

## Protect visual inspection; compress reporting

- Inspect the current render at legible resolution. Node structure alone forces
  `ITERATE`.
- Review 1–4 full frames per capture; use full-size crops for dense areas.
- Perform every visual pass below even in compact/delta mode.
- Read the operational scorecard in
  `../exceptional-ui/references/quality-rubric.md` and the detection index in
  `../exceptional-ui/references/anti-patterns.md`. Open detailed anchors or
  anti-pattern entries only for uncertain, failing, or borderline judgments.
- Load a local category reference only when that category has a meaningful
  defect or disputed score.
- Use issue IDs. Do not restate the same problem in assessment, weaknesses,
  issue list, actions, and decision.
- First and final reviews use a full score record. Intermediate reviews use a
  delta record: all scores are reconsidered, but prose covers only changed,
  unresolved, or new evidence.

Token savings must never reduce screenshot scale, skip greyscale/thumbnail
checks, conceal uncertainty, or turn a visual judgment into node-tree reasoning.

## Evidence contract

Use the run packet for product/job/state, requirements, direction, scan path,
reference principle IDs, project visual language, system constraints, node IDs,
and previous issue history. Also require the current screenshot and previous
same-viewport screenshot for iteration comparison. Follow links only when the
visible judgment needs their detail.

State the smallest missing assumption. Never invent unseen reference or product
qualities.

## Review passes

1. **Five-second:** product, state, focal object, expected action.
2. **Thumbnail/silhouette:** dominant masses, density, scan path, memory.
3. **Greyscale/blur:** hierarchy without hue or fine detail.
4. **Full-size:** type, spacing, geometry, surfaces, crops, icons, data, states,
   accessibility, and craft.
5. **Family:** task-shaped variation without system drift or repeated template.
6. **Delta:** compare the same viewport; verify the targeted visual outcome,
   note regressions, and inspect the whole screen—not only changed nodes.

After pixels, use narrow Figma reads to diagnose exact values, bindings,
components, or implementation defects. Avoid page-wide dumps.

## Scoring

Produce:

- the authoritative 100-point record: Functional correctness 15,
  Design-system correctness 10, Visual quality 55, Distinctiveness 20;
- ten diagnostic scores from 0–10: Composition, Visual hierarchy, Typography,
  Spacing, Color, Geometry, Consistency, Content quality, Distinctiveness,
  Craft/detail.

Use [rubric.md](references/rubric.md) only for uncertain diagnostic calibration.
Give one short visible evidence clause per score. The 0–10 profile diagnoses;
the 100-point rubric decides. Consistency never inflates distinctiveness.

## Five highest-impact issues

Return exactly five, ordered by product/state truth → composition/hierarchy →
genericity → system/content/visual language → craft. A major recomposition
outranks easy polish.

```markdown
I1 [impact] [region]: [visible defect] → [specific change] → [desired outcome]
Against: [requirement/direction/principle/system/rubric ID]
Scores: [affected dimensions]
```

This compact form must still identify what is wrong, why it matters, what must
change, and the desired visible result. Vague advice is invalid.

Track prior IDs as `fixed`, `open`, or `regressed`; do not rewrite their full
history. New problems get new IDs.

## Required eight-section response

Keep the original contract without repeating content:

1. **Overall assessment** — render IDs, verdict, central diagnosis, and one-line
   judgments for functional, implementation, system, visual, distinctiveness.
2. **Scores** — compact 100-point and 0–10 tables; in delta mode show prior →
   current and evidence only for changes/uncertainty.
3. **Strongest aspects** — maximum three items to preserve.
4. **Biggest weaknesses** — issue IDs only, with one systemic sentence.
5. **Five highest-impact problems** — the five canonical issue records.
6. **Specific corrective actions** — ordered issue IDs and sequencing; do not
   restate their descriptions.
7. **Genericity/AI-design assessment** — severity; detected pattern IDs;
   logo-swap, recognizability, and escape result.
8. **Decision** — `PASS` or `ITERATE`; failed gates/issue IDs and what the next
   render must prove.

## Decision

Apply the complete threshold and continuation rules in the shared rubric.
`PASS` requires a current inspected screenshot, no unresolved high-impact issue,
and no critical product, implementation, accessibility, system, copying, or
genericity failure. A provisional review always returns `ITERATE`.

## Progressive diagnosis router

- [composition.md](references/composition.md) and
  [hierarchy.md](references/hierarchy.md) — failed first read, silhouette, or
  scan path;
- [typography.md](references/typography.md), [color.md](references/color.md),
  and [spacing.md](references/spacing.md) — affected category only;
- [consistency.md](references/consistency.md) — system drift or templated reuse;
- [distinctiveness.md](references/distinctiveness.md) — failed logo-swap,
  recognizability, product-specificity, or reference-distance test.
