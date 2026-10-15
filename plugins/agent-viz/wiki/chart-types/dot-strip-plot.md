---
type: chart-type
relationships: [ranking, distribution]
aliases: [Dot plot, Dot strip plot, Strip plot, Univariate scatterplot]
---

# Dot strip plots

One dot per item on a quantitative axis shared by every row, with each group's items along a single strip.

## When to reach for it, and when not

The form is defined for more items than a bar chart could carry, in a few groups, where the question is each item's place in the shared ordering and how the groups compare. It costs one row per group, not per item. Datawrapper documents that bar charts and dot plots are sized by row count and cannot be shrunk ([datawrapper-academy.md](../sources/datawrapper-academy.md)).

| The question | Alternative |
|---|---|
| What is each item's value? | A table, or a labeled dot plot with one item per row |
| How big is each one, and by how much do they differ? | [Magnitude](magnitude.md): a [bar chart](bar-chart.md) |
| There are twelve items in one group | A sorted [bar chart](bar-chart.md) or [lollipop chart](lollipop-chart.md), which are easier to label |
| How did the order move over six periods? | [Bump chart](bump-chart.md) |
| Two values per item, and the gap is the point | [Dumbbell plot](dumbbell-plot.md) |
| What shape does this variable have? | [Distribution](distribution.md). Same drawing, different question |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per item, with a value and a group |
| Transform | None. The ordering is read off the positions |
| Geometry | One point per item |
| Scale | Value to position on a single quantitative axis shared by every strip |
| Coordinates | Cartesian, the categorical axis carrying one position per group |
| Guides | The quantitative axis, group labels, and direct labels or highlighting on the items the reader is meant to find |

It is a [lollipop chart](lollipop-chart.md) with the stem, a guide rather than an encoding, removed and more than one dot per row. The shared axis is load-bearing, as on a [slope chart](slope-chart.md): per-strip scales would make the strips silently uncomparable. It is also the strip plot [distribution.md](distribution.md) recommends at small n. Only the question differs. A ranking reading needs the items identified, a distribution reading needs the count legible, and only the title tells them apart.

## Channels

Position along a common scale, inherited from [channels.md](../concepts/channels.md), with the mark-to-channel mapping conjecture in the source literature. That accuracy claim is about extracting a value, which is not the message here, so it buys less than on a [bar chart](bar-chart.md) ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Dots picked out by color use hue for identity, a job hue does well and the accuracy ordering does not score.

## What it is measurably good at

No study in this corpus tests the form. Two nearby results do not transfer. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) note in an aside that "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots," a different task that points away from this form. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) recommend univariate scatterplots at small n, which is this drawing, but as the authors' argument from a prevalence review, and about showing a distribution rather than an order ([distribution.md](distribution.md)).

## What it is measurably bad at

Nothing measured. Ties land on the same pixel and the set looks smaller, at an unmeasured cost, as on [scatterplot.md](scatterplot.md).

## What is contested

Nothing contested in this corpus. The inherited contest, whether an unfilled mark releases the zero baseline, sets the style guides against [Vega-Lite](../sources/vega-lite.md), `authority-asserted` on both sides ([lollipop-chart.md](lollipop-chart.md)). With no stem to read as a bar, it binds less here.

## The failure mode it invites

**Overplotting that hides how many items there are.** Four merged dots read as one. Wilke's remedies are transparency, jitter or binning, all `authority-asserted` ([wilke-fundamentals.md](../sources/wilke-fundamentals.md); [inventory.md](../inventory.md) topics 58 and 59). He also states jitter's limit: "if we jitter too much, we end up placing points in locations that are not representative of the underlying dataset." The jitter runs along the categorical axis, with the seed recorded.

**A ranking read as a distribution.** Uncaptioned, a chart built for placings gets read for density, which here reflects only which items were included. What readers take from an unlabeled strip is `absence of evidence`. The fix recorded here is a title naming the question.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The inherited sentence about position along a common scale is about reading values, which this form is chosen not to be about.

**Defensible, with the label said out loud:**

- "Sixty countries across five regions in one axis-height, instead of five sorted bar charts. That is a compactness judgment, and the row-count constraint behind it is documented rather than measured."
- "The four items in question are in color and the rest are gray. Widely recommended, never measured ([refutations.md](../refutations.md#gray-plus-one-accent-as-an-evidence-backed-rule))."
- "The dots are jittered along the category axis to separate ties, with the seed recorded. Practitioner guidance from one source, `authority-asserted`, including the warning that too much jitter puts points where the data is not."
- "One shared value axis across all five strips, so the strips are comparable. Structural, and the alternative silently is not."

**Commonly repeated, and the evidence does not support it:**

- ~~"A dot strip plot is as accurate as a bar chart and uses less ink."~~ Unmeasured. The one bars-against-dots comparison, an aside on ratios, went the other way.
- ~~"Showing every observation leads readers to better conclusions."~~ Summary-only figures are measured as common, and many distributions sharing one summary is true by construction. What readers conclude is untested; [distribution.md](distribution.md) carries the same entry.

## See also

- [lollipop-chart.md](lollipop-chart.md): the same dot with a stem, one item per row
- [ranking.md](ranking.md): the group and its two free parameters
- [distribution.md](distribution.md): the same drawing read as a shape
- [../concepts/channels.md](../concepts/channels.md): why the accuracy ordering says little about reading an order
