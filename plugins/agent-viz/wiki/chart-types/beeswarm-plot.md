---
type: chart-type
relationships: [distribution]
aliases: [Bee swarm, Beeswarm plot, Swarm plot]
---

# Beeswarm plots

One dot per observation at its value on a shared quantitative axis, with the perpendicular axis used only to displace dots that would otherwise collide, so every observation keeps its true value and none is hidden.

It is also called a swarm plot or a bee swarm. The corpus does not define "beeswarm", so that definition is this page's own. The name appears once, in the Urban Institute style guide's chart examples ([roll-call.md](../roll-call.md)), and that guide is not independent of [Schwabish](../people/jonathan-schwabish.md) ([urban-institute.md](../sources/urban-institute.md)). A sina plot is a different construction, which [Wilke](../sources/wilke-fundamentals.md), citing Sidiropoulos et al. 2018, calls "a hybrid between a violin plot and jittered points". "Violin scatter" is defined nowhere here.

## When to reach for it, and when not

The form is defined for cases where the observations themselves are the message and there are enough of them to collide at their true values. Over a strip plot, every observation is visible and countable, and the layout is deterministic, so the same data redraws identically with no seed.

| The question | Alternative |
|---|---|
| What is each item, and which one is which? | [Dot strip plot](dot-strip-plot.md) with direct labels, or a table |
| Where does each item place in the order? | [Ranking](ranking.md). The sideways displacement gets in the way |
| Ten thousand observations | A [violin](violin-plot.md), a [histogram](histogram.md), or 2D binning |
| Twelve groups compared on location and spread | [Box plot](boxplot.md), at a twelfth of the space |
| What is the median, exactly? | [Box plot](boxplot.md) or a table |
| Is this bimodal? | A [histogram](histogram.md) or [violin](violin-plot.md), where the density has a stated parameter |
| Is this difference beyond chance? | A question about an estimate; see [distribution.md](distribution.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, usually one grouping variable |
| Transform | None on the value. A layout pass computes each point's perpendicular offset from the others, so no two marks overlap at the chosen mark size |
| Geometry | One point per observation |
| Scale | Value to position along a common scale, shared across groups. The offset maps nothing |
| Coordinates | Cartesian, one axis categorical |
| Guides | Value axis, group labels, n per group, and the mark size, which is a layout parameter |

It differs from a [dot strip plot](dot-strip-plot.md) in the transform. A strip plot lets points overlap or jitters them randomly; a beeswarm displaces them deterministically. The cost is that each point's sideways position depends on every other point, the mark size and the figure width, none of which is data. Wilke's warning about jitter, "if we jitter too much, we end up placing points in locations that are not representative of the underlying dataset", applies here too ([wilke-fundamentals.md](../sources/wilke-fundamentals.md); [inventory.md](../inventory.md) topics 58 and 59), though less, since the axis carries nothing.

## Channels

The value is position along a common scale ([channels.md](../concepts/channels.md)), with the usual caveat that the mark-to-channel mapping is conjecture in the source literature.

The swarm's width grows with how many observations sit near a value, so the outline reads as a density with no axis, no legend and no stated bandwidth. Its smoothing parameter is the dot radius, and it changes with figure or dot size. That is definitional. A [box plot](boxplot.md) has no tuning parameter and a [violin](violin-plot.md) has one and shows it; a beeswarm has one and hides it. No study here has decomposed the form into its cues, as [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) did for the pie.

## What is measured

No study in this corpus tests the form. Two nearby results do not transfer.

[Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) is the nearest warrant. Of 703 physiology articles, 85.6% included a bar graph, 13.4% a univariate scatterplot and 5.3% a box plot. The minimum group size shown had a median of 4, interquartile range 3 to 6. They recommend drawing the observations: "Univariate scatterplots are the best choice for showing the distribution of the data in these small samples, as boxplots and histograms would be difficult to interpret." The counts are measured; the recommendation is the authors' argument, with no reader tested. It names a strip plot, not this layout, and at n = 4 almost nothing collides.

[Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) is a construction with no participants or task. It supports *these summary statistics are compatible with radically different data* and *so plot the data*, not *readers are misled by summaries* or *drawing the points produces better conclusions*.

The inherited argument, whether a summary is defensible at the sample sizes published science uses, is on [boxplot.md](boxplot.md).

## The failure mode it invites

**Reading the width as a measured density.** What readers conclude from it is `absence of evidence`. The mitigations named here are a caption calling the width a layout artifact, or an overlay with a declared parameter.

**Letting n grow until the swarm is a slab**, where the chart still appears to show every observation. The dots stop being resolvable, and [inventory.md](../inventory.md) topic 60 says the idiom changes there, from Wilke, `authority-asserted`, with no measured threshold.

**Redrawing at another size.** A figure regenerated at another size is a different arrangement, and nothing says so. This is [inventory.md](../inventory.md) topic 77, repeatability: deterministic in the seed sense, still not stable.

**No statistic.** No median, interval or n appears unless overlaid. Readers counting a dense swarm undercount, a claim no study here measures. `absence of evidence`.

**An overlaid box plot with unstated rules.** Its quantile definition and whisker rule still need stating ([boxplot.md](boxplot.md)).

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. Value on position is inherited ([channels.md](../concepts/channels.md)), but that is about extracting a number from a mark, which is not why the form is chosen ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

**Defensible, with the label said out loud:**

- "Every observation is drawn and none is hidden by another. That is definitional. Whether readers conclude better things from it is untested."
- "Deterministic displacement rather than random jitter, so there is no seed to record and the figure redraws identically from the same data at the same size."
- "Six observations per group, so the points rather than a summary. That recommendation comes from a review of measured sample sizes plus its authors' argument, not from a reader experiment."
- "The caption states n per group, because a reader counting dots in a dense swarm may undercount. Nobody here has measured that."
- "The caption says the swarm's width is a layout artifact, because the chart otherwise shows a density it never declared."

**Commonly repeated, and the evidence does not support it:**

- ~~"A beeswarm shows the density."~~ It shows a width set by local count and dot size, with no stated parameter.
- ~~"It is a strip plot with the overlap fixed, so the strip plot evidence applies."~~ Nothing in this corpus tests either form ([dot-strip-plot.md](dot-strip-plot.md)).
- ~~"A beeswarm is a better violin."~~ Nobody has compared them. The one experiment here with a violin tested an encoding of a mean and its error against bars with error bars ([correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md)).
- ~~"Showing every observation leads readers to better conclusions."~~ Summary-only figures are measured as common, and many distributions sharing one summary is true by construction. What readers conclude is untested. [distribution.md](distribution.md) and [dot-strip-plot.md](dot-strip-plot.md) carry the same entry.

## See also

- [dot-strip-plot.md](dot-strip-plot.md): the same dots with collisions left alone or jittered
- [violin-plot.md](violin-plot.md): the same silhouette from a kernel with a declared bandwidth
- [boxplot.md](boxplot.md): five numbers instead of every point, with no tuning parameter
- [distribution.md](distribution.md): the group, and the sample-size gate
- [../studies/weissgerber-2015-beyond-bar-line.md](../studies/weissgerber-2015-beyond-bar-line.md): the show-the-data argument and its limits
