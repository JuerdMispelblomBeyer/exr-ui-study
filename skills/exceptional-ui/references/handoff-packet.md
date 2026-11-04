# Compact design-run packet

Maintain one packet across the workflow. Update changed fields in place; do not
append stage transcripts. Keep it under roughly 700 words excluding file paths
and score tables. Link to durable analyses, screenshots, and Figma nodes instead
of copying their contents.

```markdown
# DESIGN RUN — [short name]

## Scope
User/job/state; decisive question; hard requirements; exclusions.

## Sources
Figma file/page/frame IDs; project-doc paths; reference-analysis index/synthesis
paths; current and previous screenshot paths.

## Existing system
Reuse: [tokens/components/styles]
Extend: [recurring missing roles]
Constraints: [system/archive/accessibility]

## Reference handoff
Adopt: [principle IDs, maximum 6]
Avoid: [anti-copy IDs, maximum 4]
Open conflict: [only unresolved choices]

## Direction
Thesis; dominant object; scan order; density/surface logic; signature moves;
foundation decisions; chosen composition and one-line rejected alternatives.

## Build state
Changed node IDs; implementation/reuse evidence; known structural risks.

## Critique state
Render ID/viewport; total and gate scores; issue IDs with impact/status
(`open`, `fixed`, `regressed`, `accepted`); genericity/recognizability result.

## Next delta
At most five changes, each: issue ID → Figma target → visible outcome.
```

## Compression rules

- Use stable IDs; never repeat a full observation or criticism already stored in
  its source file.
- Replace superseded values rather than retaining history in the packet.
- Keep only decisions that affect the next stage. Put durable rationale in the
  project decision log.
- Preserve uncertainty explicitly; do not compress “unknown” into an invented
  answer.
- The packet is context, not visual evidence. The designer and critic must still
  open the current full render and any necessary crops.
