---
type: chart-type
relationships: [distribution]
aliases: [Bee swarm, Beeswarm plot, Swarm plot]
---

# Beeswarm plots

One dot per observation, placed at its value on a shared quantitative axis, with the perpendicular axis used for nothing except displacing dots that would otherwise collide, so every observation keeps its true value and no mark is hidden behind another.

**Also called a swarm plot or a bee swarm.** Some tools additionally offer a **sina plot** or a **violin scatter**, and those are different constructions rather than other names for this one. The **sina plot is now defined at primary**: [Wilke](../sources/wilke-fundamentals.md) calls it, citing Sidiropoulos et al. 2018, "a hybrid between a violin plot and jittered points", which is a different construction from this page's deterministic displacement. **"Violin scatter" is still undefined anywhere here**, so confirm which form someone means before relying on that name. The corpus does not define "beeswarm" either. Its single appearance is a listing: the Urban Institute style guide includes a beeswarm among its chart examples ([roll-call.md](../roll-call.md)), with no gloss recorded here, and that guide is not independent of [Schwabish](../people/jonathan-schwabish.md) ([urban-institute.md](../sources/urban-institute.md)). Read the definition above as this page's stipulation.

## When to reach for it, and when not

**Reach for it when** the observations themselves are the message, there are enough of them that they would collide at their true values, and you want the collisions resolved without either hiding points or moving them randomly. Its offer over a strip plot is narrow and exact: **every observation is visible and countable, and the layout is deterministic, so there is no seed and the same data redraws identically.**

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| What is each item, and which one is which? | [Dot strip plot](dot-strip-plot.md) with direct labels, or a table. A swarm identifies nothing |
| Where does each item place in the order? | [Ranking](ranking.md). Same dots, different question, and the sideways displacement gets in the way |
| Ten thousand observations | The swarm becomes a solid slab. A [violin](violin-plot.md), a [histogram](histogram.md), or a 2D binning |
| Twelve groups compared on location and spread | [Box plot](boxplot.md). Twelve swarms cost twelve times the space and the reading is the same |
| What is the median, exactly? | [Box plot](boxplot.md) or a table. A swarm draws no statistic unless you overlay one |
| Is this bimodal? | A [histogram](histogram.md) or [violin](violin-plot.md), where the density has a stated parameter. A swarm's width suggests modality without declaring how |
| Is this difference beyond chance? | The dots are the sample. That is a question about an estimate; see [distribution.md](distribution.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, usually one grouping variable |
| Transform | **None on the value.** A layout pass computes a perpendicular offset for each point from the positions of the others, such that no two marks overlap at the chosen mark size |
| Geometry | One point per observation |
| Scale | Value to position along a common scale, shared across groups. **The perpendicular offset is not a scale. It maps nothing** |
| Coordinates | Cartesian, one axis categorical |
| Guides | The value axis, group labels, n per group, and the mark size, which is a parameter of the layout rather than a styling choice |

Three consequences, all definitional:

- **Nothing is summarized.** Every mark on the chart is an observation at its own value. That is the property the form is chosen for and it is secure without any experiment.
- **The offset is a function of the whole set.** Adding one observation can move others sideways, and the layout depends on mark size and on the figure's width. The same data at a different figure size is a different picture.
- **The layout is deterministic**, which is what separates it from jitter. Same data, same size, same drawing, with no seed to record.

**The neighbor to keep it apart from is the [dot strip plot](dot-strip-plot.md), and the difference is what the layout does with collisions.** A strip plot lets points overlap, or displaces them randomly with jitter. A beeswarm displaces them deterministically so that none overlaps. What that buys: no point is hidden, so the count is recoverable by eye, and no seed is needed for the figure to be reproducible. What it costs: the sideways position of any one point now depends on every other point, on the mark size and on the figure width, none of which is data; a strip plot's overlap at least advertises itself as overlap. Wilke's warning about jitter, "if we jitter too much, we end up placing points in locations that are not representative of the underlying dataset" ([wilke-fundamentals.md](../sources/wilke-fundamentals.md), and [inventory.md](../inventory.md) topics 58 and 59), applies to the perpendicular axis here as well. It bites less only because that axis was carrying nothing to begin with.

## Channels

**Position along a common scale for the value**, shared across groups, inherited from [channels.md](../concepts/channels.md) with the standing caveat that the mapping from mark to channel is conjecture in the source literature. That is the whole of the intended encoding.

**The perpendicular axis carries no data.** The width of the swarm at a given value is a monotone function of how many observations sit near that value at the mark size you happened to pick. So the outline of the swarm reads as a density. It has no axis, no legend, no stated bandwidth, and it changes if you resize the figure or the dots. **It is a density estimate whose smoothing parameter is the dot radius, presented as though it were a layout artifact.** That is definitional: the width does vary with local count, by construction, and it is undeclared, by construction. What readers actually take from it has not been measured by anyone in this corpus.

This inverts the contrast that [boxplot.md](boxplot.md) draws with the [violin](violin-plot.md). The box plot's offer is that it has no tuning parameter; the violin's cost is that it has one and shows the result of it. A beeswarm has one and does not look like it does.

No study in this source set has decomposed a beeswarm into its cues, the way [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) did for the pie.

## What it is measurably good at

**Nothing. No study in this corpus tests a beeswarm against anything.**

The closest thing to a warrant it has is [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md), and the distance has to be stated rather than glossed. They reviewed 703 physiology articles: 85.6% included a bar graph, 13.4% a univariate scatterplot, 5.3% a box plot. They measured the sample sizes behind the figures, and the minimum group size shown in a figure had a median of 4, interquartile range 3 to 6. At those sizes their recommendation is to draw the observations: "Univariate scatterplots are the best choice for showing the distribution of the data in these small samples, as boxplots and histograms would be difficult to interpret."

A beeswarm is one way to draw the observations, and that is the whole of the connection.

- The prevalence and the sample sizes are **measured**. The recommendation that follows is the **authors' argument**, and no reader was tested. Nobody has compared a beeswarm against a jittered strip plot, a box plot, a violin, or anything else.
- The recommendation is about **drawing the points**, not about this layout. It is equally satisfied by a strip plot, which is what they actually name.
- And the ranges do not line up. At n = 4 there is almost nothing to collide, so the layout this form exists for earns nothing; it starts to matter well above the sizes where the review's argument is strongest. That follows from the construction, not from a study.

[Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) is the picture people reach for next, and it is a construction with no participants, no task and no measurement of comprehension. It supports *these summary statistics are compatible with radically different data*, which is true by construction and therefore the strongest form of true available, and it supports *so plot the data*. It does not support *readers are misled by summaries* or *drawing the points produces better conclusions*. Use it for the slide and Weissgerber for the argument.

## What it is measurably bad at

**Nothing measured.** Three exposures follow from the construction:

- **Large n.** The swarm fills its lane and the individual dots stop being resolvable, which is the condition [inventory.md](../inventory.md) topic 60 names: past the point where marks are readable, change idiom rather than pushing this one further. From Wilke, `authority-asserted`, with no measured threshold.
- **The redraw problem.** Mark size and figure width are inputs to the layout, so a figure regenerated at a different size is a genuinely different arrangement of the same data. Nothing in the output says so. This is [inventory.md](../inventory.md) topic 77, repeatability, arriving from an unusual direction: the drawing is deterministic in the seed sense and still not stable.
- **No statistic at all.** There is no median, no interval and no n on the chart unless you overlay them, and a reader counting dots in a dense swarm will undercount.

## What is contested

Nothing. There is no record here to disagree with itself. The one live argument nearby is inherited and is about sample size rather than about this form: whether a summary form is defensible at the sizes published science actually uses, which [boxplot.md](boxplot.md) carries in full.

## The failure mode it invites

**Reading the swarm's width as a measured density.** It is a density readout the reader was never told about: undeclared, unlabeled, and parameterized by the dot radius. That the width is undeclared is definitional. What a reader concludes from it is `absence of evidence`, not a refuted claim, and the cheap mitigation is to say in the caption that the width is a layout artifact, or to overlay a form whose parameter is stated.

**Letting n grow until the swarm is a slab.** The form's promise is that every observation is visible. At the point where the dots merge, the promise is broken and the chart still looks like it is keeping it.

**Treating "shows every point" as the end of the argument.** It is definitional that a beeswarm draws every observation. It is untested that readers reach better conclusions from one, and running those two together in a sentence upgrades a definition into a finding.

**Overlaying a box plot and letting the two disagree silently.** A common composite, and the box's quantile definition and whisker rule still have to be stated ([boxplot.md](boxplot.md)). The dots do not settle them.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing on this page qualifies. The available inheritance is that value sits on position along a common scale ([channels.md](../concepts/channels.md)), and that accuracy claim is about extracting a number from a mark, which is not why this form was chosen. It buys less here than it looks like it does; see [the scope limit](../concepts/channels.md#what-the-ranking-is-not-about).

**Defensible, with the label said out loud:**

- "Every observation is drawn and none is hidden by another. That is definitional. Whether readers conclude better things from it is untested."
- "Deterministic displacement rather than random jitter, so there is no seed to record and the figure redraws identically from the same data at the same size."
- "Six observations per group, so the points rather than a summary. That recommendation comes from a review of measured sample sizes plus its authors' argument, not from a reader experiment."
- "The caption states n per group, because a reader counting dots in a dense swarm will undercount."
- "The caption says the swarm's width is a layout artifact, because the chart otherwise shows a density it never declared."

**Commonly repeated, and the evidence does not support it:**

- ~~"A beeswarm shows the density."~~ It shows a width that varies with how many points sit near a value at the dot size you picked. No axis, no stated parameter, and it changes with the figure size.
- ~~"It is a strip plot with the overlap fixed, so the strip plot evidence applies."~~ There is no strip plot evidence. Nothing in this corpus tests either form, and [dot-strip-plot.md](dot-strip-plot.md) says the same from its side.
- ~~"A beeswarm is a better violin."~~ Nobody has compared them. The one experiment here that drew a violin was testing an encoding of a mean and its error against a bar with error bars ([correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md)), which is a different chart answering a different question.
- ~~"Showing every observation leads readers to better conclusions."~~ The prevalence of summary-only figures is measured and the claim that many distributions produce one summary is secure by construction. The step from those to what readers conclude is untested. [distribution.md](distribution.md) and [dot-strip-plot.md](dot-strip-plot.md) carry the same entry.

## See also

- [dot-strip-plot.md](dot-strip-plot.md) — the same dots with collisions left alone or jittered, usually drawn for a ranking question
- [violin-plot.md](violin-plot.md) — the same silhouette computed from a kernel with a declared bandwidth, instead of falling out of the dots
- [boxplot.md](boxplot.md) — five numbers instead of every point, and the form with no tuning parameter at all
- [distribution.md](distribution.md) — the group, and the sample-size gate that decides most of this
- [../studies/weissgerber-2015-beyond-bar-line.md](../studies/weissgerber-2015-beyond-bar-line.md) — the show-the-data argument, what it measured, and what it did not
