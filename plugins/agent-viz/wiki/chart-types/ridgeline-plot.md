---
type: chart-type
relationships: [distribution, change-over-time]
aliases: [Joyplot, Ridgeline plot]
---

# Ridgeline plots

One kernel density estimate per group, each drawn as a filled curve on its own baseline, with the baselines stacked along a second axis at a spacing smaller than the curves are tall, so the fills overlap while every group shares one value axis.

**Also called a joyplot**, which is the older, informal name and is usually traced to the Joy Division album cover. **"Ridgeline plot" is now vouched**: [Wilke](../sources/wilke-fundamentals.md) files the form under distributions and gives it a second reading in one sentence, "Ridgeline plots tend to work particularly well if want to show trends in distributions over time," which corroborates both of this page's memberships from a single source read at primary. **"Joyplot" is still unvouched by anything here.** The form also appears as a filing: Schwabish's *Better Data Visualizations* lists **Ridgeline** in its Distribution chapter, p. 179ff, in the same chapter as its two dedicated uncertainty sections ([schwabish.md](../sources/schwabish.md)). That membership is verified from the book's contents pages; nobody here has opened what he argues about the form, and this page cites the filing only. So read the definition above as this page's stipulation, and check it against any source later opened that defines the term.

Where the stacking variable is time, which is its most common use, it is also a change-over-time chart, and it is the one form in that group whose vertical extent is a distribution rather than a value. It is indexed under [distribution](distribution.md) first because that is what each curve is.

It is a close relative of the [violin](violin-plot.md), which is the same estimate mirrored and given a slot of its own, and of a grid of small-multiple density plots, which is the same set of estimates with the overlap taken out.

## When to reach for it, and when not

**Reach for it when** there are many groups, the reader already knows the order over them (months, years, cohorts, an ordinal scale), each group has enough observations for a density estimate to be about the data rather than about the bandwidth, and the question is how the shape moves along that order. **The overlap is the reason to pick it.** It fits more groups into a figure than a grid of separate density plots of the same height, and the way it does that is by hiding part of every curve.

When the ordering variable is time, this is a change-over-time chart as much as a distribution one. The page is filed here only.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| What shape does this one variable have? | [Histogram](histogram.md). The stack buys nothing with one group |
| Where is each group's median, and how wide is the middle? | [Box plot](boxplot.md). A ridgeline draws no quantile unless you add one on top |
| How tall is each group's peak, exactly? | Nothing here. Peaks sit on per-group baselines and each is partly covered by the next curve |
| I have five observations per group | Plot the five. A density over five points is a picture of the bandwidth. [Beeswarm](beeswarm-plot.md), or a strip plot |
| How many observations are in each group? | The ridgeline does not say, and per-group normalization actively hides it |
| Are these groups different beyond chance? | The curve is the spread of the sample, not an interval about an estimate. See [distribution.md](distribution.md) on descriptive versus inferential |
| The groups have to be compared precisely rather than surveyed | Small multiples of the same densities on one shared scale, with the overlap removed. No page here, and no study |
| The groups have no order | A [box plot](boxplot.md) or [violin](violin-plot.md) strip. Stacking implies a sequence, and a ridgeline of unordered categories asserts one |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, one grouping variable that carries an order |
| Transform | Kernel density estimate per group with a chosen kernel and bandwidth, then normalized: per group to equal area or equal height, or across groups to encode count |
| Geometry | One filled curve per group, drawn on its own baseline, in a specified draw order, with later curves painted over earlier ones |
| Scale | Value to position along **a single value axis shared by every group**; density to height above that group's own baseline. The offset between baselines is a layout constant, not a scale |
| Coordinates | Cartesian, with the second axis carrying one baseline per group rather than a measured quantity |
| Guides | The value axis, a label at each baseline, the bandwidth, the normalization rule, and n per group. The density itself has no axis |

Four consequences follow from those slots. All are definitional and none is empirical.

- **The overlap is specified, not incidental.** Baseline spacing and curve height are set independently, so the fraction of each curve that is covered is a parameter you chose. It does not appear anywhere in the output.
- **Occlusion is directional.** A curve hides the tail of the one behind it and not the reverse, so what is visible depends on draw order as well as on the data.
- **Peak heights sit on nonaligned baselines.** Every group's density is measured from a different origin, which is a different reading from the value axis they all share.
- **Everything the [violin](violin-plot.md) inherits from a kernel estimate applies here too**: the estimate places mass where no observation lies, bandwidth decides modality, and the normalization decides what height means. Equal-area-per-group makes a group of eight as tall as a group of eight hundred.

**This is a violin cut in half, un-mirrored, and shingled.** That is the whole difference. The mirroring goes, which halves the ink per group and removes the symmetry; the slots go from side by side to overlapping, which is what buys the group count.

## Channels

**Value on position along a common scale**, shared by every group, which is the one strong channel on the chart. **Density on height above the group's own baseline**, which is position along a nonaligned scale once you compare one group's peak against another's. Both accuracy claims are inherited from [channels.md](../concepts/channels.md), which carries those two as separate ranks, and neither is restated here as a native finding. The mapping from this mark to those channels is conjecture in the source literature, as it is for every chart type.

**No study in this source set has decomposed a ridgeline into its cues**, the way [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) did for the pie.

**And the reader is reading part of every mark through an occlusion the chart chose.** Nothing in this corpus measures reading a partly covered shape. That is `absence of evidence` about the design's central feature: the form's whole trade is occlusion for compactness, and the cost side of that trade has never been measured.

## What it is measurably good at

**Nothing. No study in this corpus tests a ridgeline plot, against anything, on any task.**

The two nearest results do not transfer.

[Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found that symmetric, continuous encodings beat a bar with error bars on inferential tasks. A ridgeline is continuous and is **not** symmetric, since the mirror is exactly what it removes, and their stimuli encoded a mean and its error rather than a sample's shape. Their result is about the bar's containment metaphor and does not reach this form.

[Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) argue for drawing the observations at small n. A ridgeline draws no observations. It is a summary form with a tuning parameter, which puts it on the far side of that argument.

The one thing on the record is preference, not accuracy: [Claus Wilke](../people/claus-wilke.md) wrote `ggridges` and reaches for ridgelines more readily than any of the business-communication authors in this corpus. `authority-asserted`, and it is a fact about his habits rather than about readers.

## What it is measurably bad at

**Nothing measured.** Four exposures follow from the construction, and none needs an experiment to be true:

- **Peak heights are not comparable across groups** unless you scaled by count and said so, and the drawing gives no sign of which normalization ran.
- **Part of every curve is hidden**, including tails, which is where a distribution's interesting behavior often is.
- **Two knobs, both invisible in the output.** Bandwidth decides modality; overlap decides how much of the answer you can see. The [violin](violin-plot.md) has one of those, the [histogram](histogram.md) has one, and this form has both.
- **Density can spill past a bound.** A quantity that cannot go below zero can be drawn with visible mass there. Same mechanism as on the violin page, and the transfer is by construction rather than by measurement.

## What is contested

Nothing. There is no record here to disagree with itself, and there is barely a record: one verified chapter membership and one author's stated habit.

## The failure mode it invites

**Ordering the groups by a statistic and then reading a trend off the ordering.** Sort groups by their own medians and the ridge marches smoothly in one direction, for any data at all. That is true by construction. Whether a reader takes it for a finding is untested, and the fix is cheap: order by something exogenous, calendar month or cohort, and say what the order is.

**Tuning the overlap until it looks right.** The parameter is a styling control in every implementation and an analysis control in effect, since it decides how much of each distribution the reader can see. The mitigation is the one [inventory.md](../inventory.md) topic 52 states for bin width and bandwidth: choose it explicitly and confirm the claim survives a different choice. `authority-asserted`, and it applies here twice over.

**Twenty groups arriving as texture.** Every group added shortens the height available to it, and past some point the ridge stops carrying shape and becomes a pattern. Where that point sits has not been measured. [inventory.md](../inventory.md) topic 60 is the general version, from Wilke: past the point where marks stop being readable, change idiom instead of pushing the current one further. `authority-asserted`.

**A confident set of shapes over almost no data.** The estimate produces a smooth curve at n = 5 and at n = 5,000, and the median smallest group size Weissgerber et al. measured across 703 published articles was 4. Nothing on a ridgeline carries n.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing on this page qualifies. No study here touches the form. The one inheritance available is that all the groups share a value axis, so where each group's mass sits is read as position along a common scale ([channels.md](../concepts/channels.md)), and the step from this chart to that channel is conjecture, as it is everywhere.

**Defensible, with the label said out loud:**

- "Thirty months in one figure instead of a thirty-panel grid, because the shared value axis is the point and the panels would each be too short to read. That is a compactness judgment and nobody has measured what the overlap costs."
- "Bandwidth is stated, the overlap fraction is stated, and the second mode survives a wider and a narrower bandwidth. There is no measured rule for either parameter."
- "Groups are in calendar order, not sorted by their medians, so the shape of the sequence is not an artifact of the sort."
- "Heights are scaled by count rather than normalized per group, so a taller ridge means more data. Structural, and the alternative silently does not."
- "n per group is in the caption, because the curve cannot carry it."

**Commonly repeated, and the evidence does not support it:**

- ~~"A ridgeline shows the distributions."~~ It shows one smoothed estimate per group, with two tunable parameters, and it covers part of each one with the next. Drawing the observations is a different chart ([beeswarm-plot.md](beeswarm-plot.md)).
- ~~"A taller ridge means more data."~~ Only under count scaling. Under equal-area or equal-height normalization, which are common defaults, height says nothing about n and the drawing does not say which ran.
- ~~"Ridgelines beat violins when there are many groups."~~ Nobody has compared them. Nothing in this corpus tests either form, so this is `absence of evidence` rather than a refuted claim, and the compactness argument for it is structural rather than measured.
- ~~"The overlap is just a style choice."~~ It decides how much of each distribution is visible. That is definitional, and it is the reason the parameter belongs in the caption rather than in the theme.

## See also

- [violin-plot.md](violin-plot.md) — the same kernel estimate, mirrored and given a slot of its own, and where the one experiment touching this family lives
- [histogram.md](histogram.md) — the same question for a single group, with a bin width instead of a bandwidth
- [beeswarm-plot.md](beeswarm-plot.md) — the other end of the same trade: every observation drawn, no estimate, no knob you declared
- [distribution.md](distribution.md) — the group, and the sample-size gate that decides most of this
- [../concepts/channels.md](../concepts/channels.md) — position along a common scale and position along nonaligned scales, and this chart uses one of each
