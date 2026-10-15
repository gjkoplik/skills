---
type: chart-type
relationships: [distribution, change-over-time]
aliases: [Joyplot, Ridgeline plot]
---

# Ridgeline plots

One kernel density estimate per group, each a filled curve on its own baseline, with the baselines stacked closer together than the curves are tall, so the fills overlap while every group shares one value axis.

"Joyplot", the older name, traces to the Joy Division album cover and is vouched by no source here. [Wilke](../sources/wilke-fundamentals.md) files "ridgeline plot" under distributions and adds a time reading, "Ridgeline plots tend to work particularly well if want to show trends in distributions over time." Schwabish's *Better Data Visualizations* lists Ridgeline in its Distribution chapter, p. 179ff ([schwabish.md](../sources/schwabish.md); contents pages only, his argument unread). The definition above is this page's own.

## When to reach for it, and when not

The form is defined for many groups in a known order (months, cohorts, an ordinal scale), each with enough data that the density reflects the data rather than the bandwidth, where the question is how the shape moves along that order. It fits more groups than a grid of density plots by hiding part of every curve. With time as the stacking variable it is also a change-over-time chart. It is indexed under [distribution](distribution.md) because each curve is one.

| The question | Alternative |
|---|---|
| What shape does this one variable have? | [Histogram](histogram.md). The stack buys nothing with one group |
| Where is each group's median, and how wide is the middle? | [Box plot](boxplot.md). A ridgeline draws no quantile unless one is added |
| How tall is each group's peak, exactly? | Nothing here. Peaks sit on separate baselines, each partly covered |
| Five observations per group | The observations, as a [beeswarm](beeswarm-plot.md) or strip plot. A density over five points pictures the bandwidth |
| How many observations are in each group? | The ridgeline does not say, and per-group normalization hides it |
| Are these groups different beyond chance? | Not this. The curve is the sample's spread, not an interval ([distribution.md](distribution.md)) |
| The groups must be compared precisely, not surveyed | Small multiples of the same densities on one shared scale, without overlap. No page here, and no study |
| The groups have no order | A [box plot](boxplot.md) or [violin](violin-plot.md) strip. Stacking implies a sequence |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, one ordered grouping variable |
| Transform | Kernel density estimate per group (chosen kernel and bandwidth), normalized per group to equal area or height, or across groups to encode count |
| Geometry | One filled curve per group on its own baseline, later curves painted over earlier ones |
| Scale | Value to position on one shared axis. Density to height above the group's baseline. The baseline offset is a layout constant, not a scale |
| Coordinates | Cartesian, the second axis carrying one baseline per group |
| Guides | Value axis, a label per baseline, the bandwidth, the normalization rule, n per group. The density has no axis |

It is a [violin](violin-plot.md) cut in half, un-mirrored and shingled. Dropping the mirror halves the ink. Overlapping the slots buys the group count. By definition:

- The overlap is a chosen parameter (baseline spacing against curve height) that appears nowhere in the output.
- Occlusion is directional. A curve hides the tail of the one behind it, so what shows depends on draw order.
- Every kernel-estimate hazard on the violin applies. Mass lands where no observation lies, even past a bound such as zero. Bandwidth decides modality. Under equal area per group, a group of eight is as tall as a group of eight hundred.

## Channels

Value is position along a common scale shared by every group, the one strong channel here. Density is height above each group's own baseline, so comparing peaks is position along nonaligned scales. Both ranks come from [channels.md](../concepts/channels.md), and the mark-to-channel step is conjecture in the source literature. No study has decomposed a ridgeline into its cues, as [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) did for the pie, or measured reading a partly covered shape. What the occlusion costs is `absence of evidence`.

## What it is measurably good at

No study in this corpus tests the form. Two nearby results do not transfer. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found symmetric, continuous encodings beat bars with error bars on inferential tasks, but a ridgeline is not symmetric and their stimuli encoded a mean and its error. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) argue for drawing observations at small n, and a ridgeline draws none.

[Claus Wilke](../people/claus-wilke.md) wrote `ggridges` and reaches for the form more readily than the business-communication authors here, a fact about his habits rather than readers. `authority-asserted`.

## What it is measurably bad at

Nothing measured. The structural exposures: peaks compare across groups only under stated count scaling, every curve is partly hidden, tails included, and bandwidth and overlap are two invisible parameters where the [histogram](histogram.md) and violin have one.

## What is contested

Nothing contested in this corpus. The record is one chapter membership and one author's habit.

## The failure mode it invites

**Ordering by a statistic, then reading a trend off the order.** Groups sorted by their own medians march smoothly for any data. Whether readers take that for a finding is untested.

**Tuning the overlap until it looks right.** It is a styling control that decides how much of each distribution shows. [inventory.md](../inventory.md) topic 52 asks for bin width and bandwidth to be an explicit choice, checked against another. `authority-asserted`, and here it applies twice.

**Twenty groups arriving as texture.** Past some unmeasured group count the ridge stops carrying shape. [inventory.md](../inventory.md) topic 60, from Wilke, says the idiom changes at that point. `authority-asserted`.

**Confident shapes over almost no data.** The curve is as smooth at n = 5 as at n = 5,000. Weissgerber et al. found a median smallest group size of 4 across 703 published articles. Nothing on a ridgeline carries n.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The one inheritance is the shared value axis: where each group's mass sits is position along a common scale ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "Thirty months in one figure instead of a thirty-panel grid, because the shared value axis is the point and the panels would each be too short to read. That is a compactness judgment and nobody has measured what the overlap costs."
- "Bandwidth is stated, the overlap fraction is stated, and the second mode survives a wider and a narrower bandwidth. There is no measured rule for either parameter."
- "Groups are in calendar order, not sorted by their medians, so the shape of the sequence is not an artifact of the sort."
- "Heights are scaled by count rather than normalized per group, so a taller ridge means more data. Structural, and the alternative silently does not."
- "n per group is in the caption, because the curve cannot carry it."

**Commonly repeated, and the evidence does not support it:**

- ~~"A ridgeline shows the distributions."~~ It shows one smoothed, partly covered estimate per group, with two tunable parameters. Drawing the observations is a different chart ([beeswarm-plot.md](beeswarm-plot.md)).
- ~~"A taller ridge means more data."~~ Only under count scaling. Under equal-area or equal-height normalization, both common defaults, height says nothing about n.
- ~~"Ridgelines beat violins when there are many groups."~~ Nobody has compared them. `absence of evidence`, not a refuted claim.
- ~~"The overlap is just a style choice."~~ It decides how much of each distribution is visible, so it belongs in the caption.

## See also

- [violin-plot.md](violin-plot.md): the same estimate, mirrored in its own slot, and the one experiment touching this family
- [histogram.md](histogram.md): one group, with a bin width instead of a bandwidth
- [beeswarm-plot.md](beeswarm-plot.md): every observation drawn, no estimate, no hidden parameter
- [distribution.md](distribution.md): the group, and the sample-size gate
- [../concepts/channels.md](../concepts/channels.md): position along common and nonaligned scales, one of each here
