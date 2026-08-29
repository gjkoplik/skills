---
type: chart-type
relationships: [ranking, distribution]
aliases: [Dot plot, Dot strip plot, Strip plot, Univariate scatterplot]
---

# Dot strip plots

One quantitative axis shared by every row, one dot per item, with the items of a group laid out along a single strip, so every item's place in the ordering reads off its position and the whole set is visible in one axis-height.

## When to reach for it, and when not

**The form applies where** there are more items than a bar chart could carry, they fall into a few groups, and the reader's job is to see where each item sits in the shared ordering and how the groups sit against each other. The form's property is compactness: it costs one row per *group*, not one row per item, which is the constraint a bar chart cannot escape. Datawrapper documents that bar charts and dot plots are sized by their row count and cannot be shrunk at all ([datawrapper-academy.md](../sources/datawrapper-academy.md)); a dot strip plot changes what a row is.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| What is each item's value? | A table, or a labeled dot plot with one item per row |
| How big is each one, and by how much do they differ? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md), where the value is the point |
| There are twelve items in one group | A sorted [bar chart](bar-chart.md) or a [lollipop chart](lollipop-chart.md). One dot per row is easier to label |
| How did the order move over six periods? | [Bump chart](bump-chart.md) |
| Two values per item, and the gap is the point | [Dumbbell plot](dumbbell-plot.md). Still no study, but there is a page |
| What shape does this variable have? | [Distribution](distribution.md). Same drawing, different question; see below |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per item, with a value and a group |
| Transform | None. The ordering is read off the positions rather than computed |
| Geometry | One point per item |
| Scale | Value to position on **a single quantitative axis shared by every strip** |
| Coordinates | Cartesian, with the categorical axis carrying one position per group rather than per item |
| Guides | The quantitative axis, group labels, and direct labels or highlighting on whichever items the reader is meant to find |

**It is a [lollipop chart](lollipop-chart.md) with the stem removed and more than one dot per row.** Lollipop's page makes the same point from its side: taking the stem away leaves a dot plot, because the stem was a guide rather than an encoding. The shared axis is load-bearing in the same way it is on a [slope chart](slope-chart.md): per-strip scales would make the strips uncomparable and nothing on the chart would say so.

**It is also the same drawing as the strip plot that [distribution.md](distribution.md) recommends at small n.** Geometry, scale and coordinates are identical. What differs is the question brought to it, and therefore what the guides have to do: a ranking reading needs the items identified, and a distribution reading needs the count legible. The chart does not distinguish the two; the title is what carries it.

## Channels

**Position along a common scale**, inherited from [channels.md](../concepts/channels.md) with the standard caveat that the mapping from mark to channel is conjecture in the source literature.

Two things about that inheritance, both bearing on this being a ranking form. The accuracy claim behind position is about extracting a value, and this form was chosen on the grounds that the value is not the message, so the inheritance buys less here than it does on a [bar chart](bar-chart.md); see [the scope limit](../concepts/channels.md#what-the-ranking-is-not-about). And where a subset of the dots is picked out by color, that is **hue used for identity**, which is the job the accuracy ordering does not score and which [channels.md](../concepts/channels.md) says hue is actually good at. A highlighted dot strip plot is not using a bottom-ranked channel badly.

## What it is measurably good at

**Nothing. No study in this corpus tests a dot strip plot.**

Two results sit nearby and neither transfers. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) note in passing that "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots," which is a different task, points away from this form, and is an aside in a paper about something else. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) recommend univariate scatterplots at small n, which is this drawing, but the recommendation is the authors' argument from a prevalence review rather than a reader experiment, and it is about showing a distribution rather than an order ([distribution.md](distribution.md) states the same limit).

## What it is measurably bad at

Nothing measured. The exposure worth naming is overplotting: ties and near-ties land on the same pixel and the reader undercounts the set. Nobody in this source set has measured what overplotting costs, which is the same position [scatterplot.md](scatterplot.md) is in.

## What is contested

Nothing native. There is no record here to disagree with itself.

The one nearby contest is inherited and it barely binds: whether an unfilled mark releases the zero baseline is disputed between the style guides and [Vega-Lite](../sources/vega-lite.md), and it is `authority-asserted` on both sides. [lollipop-chart.md](lollipop-chart.md) carries that argument in full. It bites less here because there is no stem running back to an axis for the reader to read as a bar.

## The failure mode it invites

**Overplotting that hides how many items there are.** The compactness that is the reason to use the form is also what produces the pile-up, and a strip where four dots have merged into one reads as a set of the wrong size. The remedies are Wilke's, all `authority-asserted`: transparency, jitter, or binning ([wilke-fundamentals.md](../sources/wilke-fundamentals.md), and [inventory.md](../inventory.md) topics 58 and 59). Jitter has its own limit, stated by the same author: "if we jitter too much, we end up placing points in locations that are not representative of the underlying dataset." Jitter runs along the categorical axis rather than the value axis, and the seed is recorded.

**Letting the reader take it for a distribution when it is a ranking.** The drawing is identical to the strip plot in [distribution.md](distribution.md), so a reader with no caption reads density and shape off a chart built to show placings, and the density is an artifact of how many items were included. `absence of evidence` rather than a prohibition: nobody has checked what readers actually take from an unlabeled strip. The cheap fix recorded here is a title that names the question.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The inherited sentence about position along a common scale is available and it is about reading values, which is the task this form was chosen to *not* be about, so it does not even do the usual work here.

**Defensible, with the label said out loud:**

- "Sixty countries across five regions in one axis-height, instead of five sorted bar charts. That is a compactness judgment, and the row-count constraint behind it is documented rather than measured."
- "The four items in question are in color and the rest are gray. Widely recommended, never measured ([refutations.md](../refutations.md#gray-plus-one-accent-as-an-evidence-backed-rule))."
- "The dots are jittered along the category axis to separate ties, with the seed recorded. Practitioner guidance from one source, `authority-asserted`, including the warning that too much jitter puts points where the data is not."
- "One shared value axis across all five strips, so the strips are comparable. Structural, and the alternative silently is not."

**Commonly repeated, and the evidence does not support it:**

- ~~"A dot strip plot is as accurate as a bar chart and uses less ink."~~ Nobody has measured this form. The one comparison in the literature that puts bars against dot plots, on ratio comparison, went the other way, and it was an aside rather than an experiment.
- ~~"Showing every observation leads readers to better conclusions."~~ The prevalence of summary-only figures is measured and the claim that many distributions produce one summary is secure by construction. The step from those to what readers conclude is untested; [distribution.md](distribution.md) carries the same entry.

## See also

- [lollipop-chart.md](lollipop-chart.md) — the same dot with a stem, one item per row
- [ranking.md](ranking.md) — the group, and the two free parameters it carries
- [distribution.md](distribution.md) — the same drawing read as a shape rather than as an order
- [../concepts/channels.md](../concepts/channels.md) — including why the accuracy ordering says little about reading an order
