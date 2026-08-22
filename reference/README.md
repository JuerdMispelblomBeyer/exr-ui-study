# UI reference library

This directory is the visual-input library for the ExRobotics engineering
interface. The root contains only direct, screen-like interface references.
Photographs of computers, phones, or other display hardware do not belong here
because an agent could mistake the presentation device for part of the UI.

## Naming

Direct UI references use:

```
ref-NNN__theme-or-domain__distinguishing-feature.ext
```

Presentation imagery uses:

```
presentation-only/pres-NNN__subject__presentation-form.ext
```

Numbers are stable intake IDs. Gaps indicate rejected or unavailable
candidates; do not renumber later files.

## Library structure

- `ref-*.{jpg,jpeg,png,webp}` — visually screened screen-like UI references.
- `presentation-only/` — useful editorial imagery containing device or
  hardware mockups; excluded from direct interface learning.
- `CATALOG.md` — human-readable names, classification, and provenance.
- `SOURCES.tsv` — machine-readable provenance for the online collection.

## Handling rules

- Preserve downloaded and supplied files byte-for-byte.
- Do not crop, annotate, recompress, recolor, or overwrite originals.
- Do not sample source colors as ExRobotics brand colors.
- Learn from composition, geometry, hierarchy, depth, typography, data
  treatment, and interaction character.
- ExRobotics yellow remains the lead brand signal.
- Collection does not equal adoption. A reference contributes design rules only
  after a recorded analysis and decision in `../docs/REFERENCE_ANALYSIS.md`.
- When removing a disliked reference, remove its image and catalog row together;
  do not reuse its numeric ID.

The repeatable intake workflow is defined in
`../docs/REFERENCE_INTAKE_METHOD.md`.

## Existing-file rename record

The supplied originals were renamed without changing their bytes:

| Current name | Previous name |
|---|---|
| `ref-001__dark-resource-overview__stacked-utilization-instrument.jpg` | `19557e6f37e3581637be10d43f2ebffe.jpg` |
| `ref-002__dark-contract-dashboard__tall-crop.jpg` | `3c327b237412bc2ec4d7b1587801da0d.jpg` |
| `ref-003__dark-contract-dashboard__wide-workbench.jpg` | `a9c0f048d4b5fa97e09f727cc8f765b9.jpg` |
| `ref-004__light-health-dashboard__treatment-timeline-crop.jpg` | `636cdd859efb3ae0e5a9526be29a082e.jpg` |
| `ref-005__light-frosted-workflow-dashboard__tall-navigation.jpg` | `85ba95ea5a25d4ac98617e3fc81196e4.jpg` |
| `ref-006__dark-instrument-system__mixed-tile-grid.jpg` | `d409cdb92b96e4b8ac67559abf4c814a.jpg` |
| `presentation-only/pres-001__editorial-mobile-turbine-app__device-mockups.jpg` | `2026-08-20-attached-foto-1.jpg` |
