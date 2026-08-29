---
type: chart-type
relationships: [part-to-whole]
aliases: [Multilevel pie, Radial treemap, Ring chart, Sunburst chart]
---

# Sunburst charts

A hierarchy drawn as concentric rings, where a node's **angular extent** is proportional to its value and its ring is its depth, so each ring is one level of the tree and each parent's children divide the parent's arc.

Also called a **radial treemap**, a **multilevel pie** or a **ring chart**. **A donut is not a sunburst.** A single ring with no nesting is a pie with its center removed, and [pie-and-donut.md](pie-and-donut.md) owns that case; what defines this form is that the rings nest.

[Schwabish](../sources/schwabish.md) files Sunburst under **Part-to-Whole**, verified from the book's own contents pages, which agrees with this index. That is unusual: the other two forms added to this group alongside it are filed elsewhere in his catalog. The filing is the verified part; the book's prose is unopened in this corpus, so nothing here reports what he argues about the form.

## When to reach for it, and when not

The form is defined for the case where the data is a hierarchy, the reader needs the top-level split and its subdivisions at once, "these are all of it" is part of the claim, and the tree is shallow enough that the outer ring still holds labelable arcs.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How big is this node? | A table, or a [bar chart](bar-chart.md). No axis exists on this form |
| Which of these is biggest? | Sorted [bar chart](bar-chart.md). Position instead of arc |
| There is no hierarchy | [Pie or donut](pie-and-donut.md). One ring is that chart, and it is the better-evidenced one |
| There are hundreds of leaves | [Treemap](treemap.md). It packs the same tree without turning leaves into slivers |
| How did this change since last year? | Anything with a shared axis. Two sunbursts sit at different rotational offsets and nothing survives the comparison |
| The hierarchy is the message and the values are not | A tree diagram. No page here, and no study |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per leaf, with a magnitude and a path through a hierarchy |
| Transform | Roll up to internal nodes, then cumulative-sum each node's children within the parent's angular extent |
| Geometry | Annular sector |
| Scale | Value to swept angle. Depth to ring index. Ring thickness is usually constant and encodes nothing |
| Coordinates | Polar |
| Guides | Labels in place or on hover, and a center that may hold the root label or the total. No axis exists |

**Setting the coordinates slot to polar is the whole difference from a [treemap](treemap.md)**, and it changes what the encoding is:

- A treemap encodes value as **area**, everywhere in the figure, at every depth.
- A sunburst encodes value as **angle**. With constant ring thickness, a sector's area grows with its distance from the center, so two nodes of equal value on different rings have different areas, and a child never has the area share of its parent that its value share would suggest.

That is geometry, not a finding. It means the phrase "radial treemap" describes the layout and misdescribes the encoding.

## Channels

**Angular extent, with arc length and area riding on it, and both of those vary by ring.**

The one direct measurement of which cue a circular form actually puts the reader on is [Skau & Kosara (2016)](../studies/skau-kosara-2016.md), and it found the received answer wrong:

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

So on a circular form, arc length and area are what readers use, and angle is the weakest of the three ([pie-and-donut.md](pie-and-donut.md) carries the full result).

The measurement was made on **single-ring, two-segment pies and donuts**. The structural fact is that on a sunburst, angle is constant across rings for a given share while arc length and area are not: a node holding a tenth of the circle has several times more arc on the outermost ring than on the innermost. Those two statements sit next to each other and do not join up into a result. Whether an outer-ring share is therefore read differently from an inner-ring one is a question **nobody in this corpus has tested**. `absence of evidence`.

The treemap results do not transfer either. Heer & Bostock measured rectangles in Cartesian coordinates, including the finding that the surrounding treemap does not interfere with the judgment ([heer-bostock-2010.md](../studies/heer-bostock-2010.md)). Annular sectors at varying radii were not in the experiment.

## What it is measurably good at

**Nothing. No study in this corpus tests a sunburst chart.**

## What it is measurably bad at

Nothing measured on this form.

One inherited result applies: on proportional judgment, a bar chart beats a pie, measured and replicated ([cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md), [heer-bostock-2010.md](../studies/heer-bostock-2010.md)). A sunburst is a pie with a depth dimension added, so there is no reason to expect it does better at reading values off a mark, and no measurement saying it does.

## What is contested

Nothing about this form. The contest it inherits from [pie-and-donut.md](pie-and-donut.md) bears on the argument commonly made here: the claim that circular forms fail *because* they encode angle is refuted, and the claim that length beats angle is unsupported by the one head-to-head test ([channels.md](../concepts/channels.md)). Bars beating pies for value extraction survives; the mechanism does not.

## The failure mode it invites

**Reading area across rings.** The form looks like a treemap and is not one. Comparing the visual weight of an outer-ring sector against an inner-ring one compares two quantities that are not on the same scale, and the chart gives no cue that they are not.

**Outer rings that do not sum to their parent.** Missing or unclassified children leave a gap, or, worse, get absorbed so the visible children fill the parent's arc and silently overstate every one of them. The whole-constraint is what this group sells, and this is where the form quietly breaks it.

**Slivers.** Below a few degrees a sector cannot be labeled, hovered reliably, or distinguished from its neighbor, and a deep tree produces them by construction rather than by accident.

All three follow from the geometry. None has been tested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing about this form directly.

**Defensible, with the label said out loud:**

- "A sunburst because the hierarchy has three levels and the reader needs to see both the top-level split and what is inside it, in one figure that shows the parts exhaust the total. No study here measures how well that reads."
- "Three rings, and the outer one carries labels. Convention, with no measured depth limit behind it."
- "Values are labeled directly, because there is no axis on this chart and nothing here says readers can recover them from the arcs."

**Commonly repeated, and the evidence does not support it:**

- ~~"It is a radial treemap, so areas are comparable across the figure."~~ With constant ring thickness the area of a sector depends on its radius, so equal values on different rings have different areas. Geometry, and it is the opposite of the treemap's defining property.
- ~~"Readers judge these by angle, and angle is a weak channel."~~ Measured on pies and donuts, angle was the least-used cue of the three, not the primary one ([skau-kosara-2016.md](../studies/skau-kosara-2016.md)).
- ~~"A sunburst shows hierarchy better than a treemap."~~ Nothing in this corpus compares the two forms on any task.

## See also

- [pie-and-donut.md](pie-and-donut.md) — the single-ring case, and the one circular form whose channels were measured
- [treemap.md](treemap.md) — the same hierarchy in Cartesian coordinates, where area really is the encoding
- [part-to-whole.md](part-to-whole.md) — the group, and what composition costs
- [../studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md) — arcs, angles and areas, on two-segment pies
- [../concepts/channels.md](../concepts/channels.md)
