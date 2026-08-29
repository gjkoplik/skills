---
type: chart-type
relationships: [magnitude]
aliases: [Radar chart, Spider chart, Star chart]
---

# Radar charts

Several quantitative axes radiating from a shared center, one point per axis for each series, joined into a closed polygon. Also called a spider or star chart.

**This corpus contains one sentence about radar charts.** No study here uses one as a stimulus, and no style guide in the source set rules on it. The usual criticisms of the form are not supported by anything in it.

## When to reach for it, and when not

The form is defined for a profile: several measures for one entity, shown together as a shape, where the shape rather than any individual value is what the reader is meant to carry away. That is what the form is for and it is `authority-asserted` at best, since the corpus contains no evaluation of it.

The one piece of guidance available, the FT's line ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "make sure they are organised in a way that makes sense to reader"

which is about axis order, for the reason given under Structural decomposition.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How big is each of these measures? | [Bar chart](bar-chart.md). Position along a common scale, and the measures do not have to share units |
| Which entity is bigger overall? | [Bar chart](bar-chart.md) of the intended aggregate. The polygon's size is not that aggregate |
| How do six entities compare? | Small multiples of anything. Overlaid polygons occlude each other |
| How do two variables relate? | Correlation. A scatterplot |
| Does this add up? | [Part-to-whole](part-to-whole.md). The axes are separate measures and do not compose a total |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, measure) with a magnitude |
| Transform | Usually a per-axis normalization, since the measures rarely share units |
| Geometry | A point per axis, joined by a closed polyline, often filled |
| Scale | Magnitude to radial distance from the center, per axis |
| Coordinates | Polar, with a discrete angular position per measure |
| Guides | One radial axis per measure, its own tick labels, and a legend when there is more than one series |

Two properties follow from the slots and assert nothing empirical:

**The angular position is a category, not a value.** Unlike a coxcomb, where the angle is swept by the data, here the angle just says which measure the point belongs to.

**The enclosed area is a function of the axis order, not only of the data.** Permuting the axes leaves every value unchanged and changes the polygon's area and shape. That is arithmetic, not a claim about readers, and it is the reason the FT's line about organizing the axes is the guidance that exists.

## Channels

**Radial position on each axis**, with the axes sharing an origin but not a direction. Under Cleveland & McGill's list, the nearest task is positions along nonaligned scales rather than position along a common scale, which is a step down; that mapping is conjecture, and nobody has decomposed this form the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed the pie ([channels.md](../concepts/channels.md)).

**Enclosed area is available as a secondary reading**, and it is the one the form makes salient. Area is read less accurately than position, measured ([channels.md](../concepts/channels.md)). Whether readers actually use it here is untested, and the step from "the area is prominent" to "readers are misled by it" is exactly the inference this wiki refuses to make for free.

## What it is measurably good at

Nothing has been measured.

## What it is measurably bad at

Nothing has been measured.

## What is contested

Nothing. **Contested requires a record that disagrees with itself**, and here there is no record ([evidence-class.md](../concepts/evidence-class.md)). The familiar criticisms, that radar charts break down past a few axes, that overlaid polygons are unreadable, that the area misleads, are all plausible and none of them is supported by anything in this corpus. `absence of evidence`, which is not the same as refuted and not the same as endorsed.

## The failure mode it invites

**Reading the polygon's size as a total.** The area depends on which measures sit next to which, so two orderings of the same data give two different shapes. That much is definitional. The failure is treating the resulting shape as a summary of the entity. Stated as a caution with its reason rather than as a prohibition, because no one has tested whether readers do it.

**Normalizing each axis and then not saying so.** Radar charts almost always rescale each measure to a common radius, which means the polygon compares percentiles or min-max positions rather than quantities. That is an undisclosed transform, carrying the same obligation any derived statistic does.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. There is no experiment in this corpus involving this form, in either direction.

**Defensible, with the label said out loud:**

- "The reader is meant to compare profiles, not values, so the axes are ordered to group related measures. That ordering guidance is one line from a newsroom taxonomy, and the form has not been evaluated."
- "Each axis is normalized, and the caption says to what. The polygon compares relative positions, not quantities."

**Commonly repeated and not supported:**

- ~~"Radar charts are known to be hard to read."~~ Not by anything here. It may well be true; nobody in this source set checked.
- ~~"The area misleads readers."~~ The area is order-dependent, which is arithmetic. That readers read it, and are moved by it, is the untested half, and it is the half the claim needs.
- ~~"Use a bar chart instead; it is more accurate."~~ The bar chart's accuracy advantage is measured against pies, angles and areas in proportional-judgment tasks. Nobody has run a radar chart in one, and the profile-comparison task the form exists for is not what the ranking scores ([what the ranking is not about](../concepts/channels.md#what-the-ranking-is-not-about)).

## What would move this page

A proportional-judgment task on a radar chart against a bar chart of the same measures would settle the value-reading half in an afternoon, and a profile-matching task would address the half the form actually claims. Neither exists in this source set.

## See also

- [magnitude.md](magnitude.md) — the group
- [../concepts/channels.md](../concepts/channels.md) — what would be inherited if the mapping had been decomposed
- [../concepts/evidence-class.md](../concepts/evidence-class.md) — absence of evidence, kept distinct from contested and from refuted
