---
type: chart-type
relationships: [part-to-whole]
aliases: [Multilevel pie, Radial treemap, Ring chart, Sunburst chart]
---

# Sunburst charts

A hierarchy drawn as concentric rings, one ring per level, where each node's **angular extent** is proportional to its value and each parent's children divide the parent's arc.

Also called a **radial treemap**, a **multilevel pie** or a **ring chart**. A single unnested ring is a donut, covered in [pie-and-donut.md](pie-and-donut.md). [Schwabish](../sources/schwabish.md) files Sunburst under Part-to-Whole, per the book's contents pages. His prose on it is unopened here.

## When to reach for it, and when not

The form is defined for a hierarchy whose top-level split and subdivisions are needed at once, where "these are all of it" is part of the claim and the tree is shallow enough to label the outer ring.

| The question | Alternative |
|---|---|
| How big is this node? | A table, or a [bar chart](bar-chart.md). No axis exists on this form |
| Which of these is biggest? | Sorted [bar chart](bar-chart.md). Position instead of arc |
| There is no hierarchy | [Pie or donut](pie-and-donut.md). One ring is that chart, and it is better evidenced |
| There are hundreds of leaves | [Treemap](treemap.md). It packs the same tree without turning leaves into slivers |
| How did this change since last year? | Anything with a shared axis. Two sunbursts sit at different rotational offsets and do not compare |
| The hierarchy is the message and the values are not | A tree diagram. No page here, and no study |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per leaf, with a magnitude and a path through a hierarchy |
| Transform | Roll up to internal nodes, then cumulative-sum each node's children within the parent's angular extent |
| Geometry | Annular sector |
| Scale | Value to swept angle. Depth to ring index. Ring thickness is usually constant and encodes nothing |
| Coordinates | Polar |
| Guides | Labels in place or on hover. The center may hold the root label or the total. No axis exists |

Polar coordinates are the whole difference from a [treemap](treemap.md), and they change the encoding. A treemap encodes value as **area** at every depth, a sunburst as **angle**. With constant ring thickness, area grows with distance from the center, so equal values on different rings get different areas and a child's area share of its parent never matches its value share. That is geometry. "Radial treemap" names the layout and misnames the encoding.

## Channels

The value is on angular extent, with arc length and area riding on it, both varying by ring. [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) is the one direct measurement of which cue a circular form puts the reader on:

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Readers used arc length and area, and angle least, on single-ring, two-segment pies and donuts ([pie-and-donut.md](pie-and-donut.md)). On a sunburst a share's angle is fixed across rings while its arc and area grow outward, so a tenth of the circle has several times more arc on the outermost ring than on the innermost. Whether outer-ring shares read differently is untested. `absence of evidence`.

Treemap results do not transfer either. Heer & Bostock measured Cartesian rectangles, finding that the surrounding treemap does not interfere with the judgment, and tested no annular sectors ([heer-bostock-2010.md](../studies/heer-bostock-2010.md)).

## What it is measurably good at

No study in this corpus tests a sunburst chart.

## What it is measurably bad at

Nothing measured on this form. It inherits the result that a bar chart beats a pie on proportional judgment, measured and replicated ([cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md), [heer-bostock-2010.md](../studies/heer-bostock-2010.md)). Nothing measures a pie with depth added doing better.

## What is contested

Nothing about this form. From [pie-and-donut.md](pie-and-donut.md) it inherits two results against the usual argument. That circular forms fail *because* they encode angle is refuted, and that length beats angle is unsupported by the one head-to-head test ([channels.md](../concepts/channels.md)). Bars still beat pies for value extraction.

## The failure mode it invites

All three follow from the geometry, and none has been tested on readers.

**Reading area across rings.** It looks like a treemap, but outer and inner sectors are on different area scales, and nothing on the chart says so.

**Outer rings that do not sum to their parent.** Missing or unclassified children leave a gap, or are absorbed so the visible children fill the parent's arc and each is overstated. That breaks the whole-constraint this group is for.

**Slivers.** Below a few degrees a sector cannot be labeled, hovered or told from its neighbor, and a deep tree produces them by construction.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing about this form directly.

**Defensible, with the label said out loud:**

- "A sunburst because the hierarchy has three levels and the reader needs to see both the top-level split and what is inside it, in one figure that shows the parts exhaust the total. No study here measures how well that reads."
- "Three rings, and the outer one carries labels. Convention, with no measured depth limit behind it."
- "Values are labeled directly, because there is no axis on this chart and nothing here says readers can recover them from the arcs."

**Commonly repeated, and the evidence does not support it:**

- ~~"It is a radial treemap, so areas are comparable across the figure."~~ Area depends on radius, the opposite of the treemap's defining property.
- ~~"Readers judge these by angle, and angle is a weak channel."~~ On pies and donuts, angle was the least-used cue ([skau-kosara-2016.md](../studies/skau-kosara-2016.md)).
- ~~"A sunburst shows hierarchy better than a treemap."~~ Nothing in this corpus compares the two forms on any task.

## See also

- [pie-and-donut.md](pie-and-donut.md): the single-ring case, with measured channels
- [treemap.md](treemap.md): the same hierarchy in Cartesian coordinates, encoded as area
- [part-to-whole.md](part-to-whole.md): the group, and what composition costs
- [../studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md): arcs, angles and areas, on two-segment pies
- [../concepts/channels.md](../concepts/channels.md)
