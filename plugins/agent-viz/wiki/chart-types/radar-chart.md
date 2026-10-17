---
type: chart-type
relationships: [magnitude]
aliases: [Radar chart, Spider chart, Star chart]
---

# Radar charts

Several quantitative axes radiating from a shared center, with one point per axis for each series, joined into a closed polygon. Also called a spider or star chart.

## When to reach for it, and when not

The form is defined for a profile: several measures for one entity, shown as a shape, where the shape matters more than any single value. That purpose is `authority-asserted` at best. No style guide in the source set rules on the form, and the one line of guidance, from the [FT](../sources/ft-visual-vocabulary.md), concerns axis order:

> "make sure they are organised in a way that makes sense to reader"

| The question | Alternative |
|---|---|
| How big is each of these measures? | [Bar chart](bar-chart.md). Position on a common scale, and no shared units needed |
| Which entity is bigger overall? | [Bar chart](bar-chart.md) of the intended aggregate. The polygon's size is not that aggregate |
| How do six entities compare? | Small multiples of anything. Overlaid polygons occlude each other |
| How do two variables relate? | Correlation. A scatterplot |
| Does this add up? | [Part-to-whole](part-to-whole.md). The axes are separate measures, not parts of a total |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, measure) with a magnitude |
| Transform | Usually a per-axis normalization, since the measures rarely share units |
| Geometry | A point per axis, joined by a closed polyline, often filled |
| Scale | Magnitude to radial distance from the center, per axis |
| Coordinates | Polar, with a discrete angular position per measure |
| Guides | One radial axis per measure, each with tick labels. A legend for more than one series |

Unlike a pie, where the angle is swept by the data, the angle here is a category naming the measure, as on a coxcomb.

Permuting the axes leaves every value unchanged and changes the polygon's area and shape. That arithmetic is why axis order is the guidance that exists.

## Channels

Radial position on each axis, with a shared origin but no shared direction. The nearest task on Cleveland & McGill's list is position along nonaligned scales, a step down from a common scale. That mapping is conjecture, and nobody has decomposed this form the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed the pie ([channels.md](../concepts/channels.md)).

Enclosed area is the salient secondary reading, and area is read less accurately than position, `evidence-backed`. Whether readers use it here is untested.

## What is measured

No study in this corpus tests the form. This source set has neither a proportional-judgment task against a bar chart of the same measures, which would settle value reading, nor a profile-matching task, which would test what the form claims. With no record, nothing can be contested ([evidence-class.md](../concepts/evidence-class.md)). The familiar criticisms, that the form breaks down past a few axes, that overlaid polygons are unreadable and that the area misleads, are plausible and unsupported here. `absence of evidence`.

## The failure mode it invites

**Reading the polygon's size as a total.** Two axis orderings of the same data give two shapes. Treating either as a summary of the entity is the failure, untested on readers.

**Normalizing each axis without saying so.** Radar charts almost always rescale each measure to a common radius, so the polygon silently compares percentiles or min-max positions rather than quantities.

## Justifying the choice

**Defensible, evidence-backed:**

- None. No experiment here involves the form.

**Defensible, with the label said out loud:**

- "The reader is meant to compare profiles, not values, so the axes are ordered to group related measures. That ordering guidance is one line from a newsroom taxonomy, and the form has not been evaluated."
- "Each axis is normalized, and the caption says to what. The polygon compares relative positions, not quantities."

**Commonly repeated, and the evidence does not support it:**

- ~~"Radar charts are known to be hard to read."~~ Nobody in this source set checked.
- ~~"The area misleads readers."~~ Order-dependence is arithmetic. That readers are moved by it is untested, and the claim needs that half.
- ~~"Use a bar chart instead; it is more accurate."~~ The bar chart's advantage was measured in proportional-judgment tasks against pies, angles and areas, never radar charts, and profile comparison is not what the ranking scores ([what the ranking is not about](../concepts/channels.md#what-the-ranking-is-not-about)).

## See also

- [magnitude.md](magnitude.md): the group
- [../concepts/channels.md](../concepts/channels.md): the rankings that would be inherited
- [../concepts/evidence-class.md](../concepts/evidence-class.md): absence of evidence versus contested
