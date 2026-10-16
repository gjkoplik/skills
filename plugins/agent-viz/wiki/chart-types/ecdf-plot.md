---
type: chart-type
relationships: [distribution]
aliases: [ECDF plot, Empirical cumulative distribution function, Cumulative distribution plot]
---

# ECDF plots

Every observation of one continuous variable plotted at its own value against its rank, drawn as a monotonic step function so that the height at any value is the proportion of observations at or below it.

## When to reach for it, and when not

The form is defined for one variable and a cumulative question: what fraction sits below a threshold, where a quantile falls, whether a tail follows a power law. It answers those without a smoothing parameter. [Wilke](../sources/wilke-fundamentals.md) opens chapter 8 on that contrast with the histograms and density plots of chapter 7:

> "they both share the limitation that the resulting figure depends to a substantial degree on parameters the user has to choose, such as the bin width for histograms and the bandwidth for density plots. As a result, both have to be considered as an interpretation of the data rather than a direct visualization of the data itself."

He adds: "These types of visualizations require no arbitrary parameter choices, and they show all of the data at once." [seaborn](../sources/seaborn.md)'s distributions tutorial states the same two properties: "Unlike the histogram or KDE, it directly represents each datapoint. That means there is no bin size or smoothing parameter to consider." seaborn alone adds that monotonic curves overlay without occluding, `authority-asserted`: "because the curve is monotonically increasing, it is well-suited for comparing multiple distributions."

| The question | Alternative |
|---|---|
| Is this one mode or two? | [Histogram](histogram.md) or [violin](violin-plot.md). Modality is a change of slope here, which seaborn names as the hard part |
| Where is the mass, roughly? | [Histogram](histogram.md). The cumulative transform trades away shape |
| How do twelve groups compare on median and spread? | [Box plot](boxplot.md) |
| There are six observations | The six observations, plotted |
| How precisely is this mean known? | An estimate, not a sample ([distribution.md](distribution.md)) |
| Does this follow a named distribution? | A q-q plot, which Wilke pairs with the ECDF and which has no page here |

Ascending curves give the fraction at or below a value, and descending curves the fraction at or above it. Wilke: "Ascending cumulative distribution functions are more widely known and more commonly used than descending ones, but both have important applications. Descending cumulative distribution functions are critical when we want to visualize highly skewed distributions."

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable |
| Transform | Sort, then rank. Optionally divide the rank by n, giving a cumulative frequency in [0, 1] |
| Geometry | A monotonic step function, optionally with a point per observation |
| Scale | Value to position on one axis, rank or cumulative frequency to position on the other. Either may be logarithmic |
| Coordinates | Cartesian |
| Guides | Value axis with units, a cumulative axis stating count or fraction, and the direction |

The transform has no free parameter, unlike every other aggregate in the group, such as [histogram.md](histogram.md). By construction, two different samples cannot draw the same ECDF, as they can the same box plot ([Matejka & Fitzmaurice](../studies/matejka-2017-datasaurus.md)) or bar and error bar ([Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md)).

## Channels

Both axes are position along a common scale, inherited from [channels.md](../concepts/channels.md), where the mapping is conjecture. Reading a quantile is a position judgment, so the position result covers it. Modality and shape are slope judgments, which the ranking does not cover ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)), and nobody has measured reading a change of slope. No study here decomposed an ECDF into cues.

## What is measured

No controlled study in this corpus tests ECDF reading against anything. Whether readers conclude better things from the one-sample-one-drawing property is untested, and so is the weakness both sources name. `absence of evidence`. Nothing is contested; the record is silent, which [evidence-class.md](../concepts/evidence-class.md) keeps distinct from contested.

The log-log tail reading inherits a measured hazard that does not transfer directly. On a descending log-log ECDF, Wilke notes, "a power law appears as a perfect straight line". [Menge et al. (2018)](../studies/menge-2018-log-scales.md) found domain experts reading log-log axes correctly 56% of the time against 93% for linear-linear. [Romano et al. (2020)](../studies/romano-2020-log-scales-covid.md) found log scales changing comprehension, prediction and policy preference. Neither tested an ECDF.

## The failure mode it invites

**The cumulative axis read as a density.** A steep segment is a dense region and a flat one is a gap, the reverse of what a histogram trains a reader to expect. Both sources name the resulting weakness as an impression, `authority-asserted`.

Wilke: "Unfortunately, they are a little less intuitive than a histogram or a density plot is, and I don't see them used frequently outside of highly technical publications."

seaborn names the task: "The major downside to the ECDF plot is that it represents the shape of the distribution less intuitively than a histogram or density curve. Consider how the bimodality of flipper lengths is immediately apparent in the histogram, but to see it in the ECDF plot, you must look for varying slopes."

**An unlabeled direction.** Both directions are standard (Wilke chapter 8), so a reader who assumes the wrong one inverts every proportion. No source here measures the cost. `absence of evidence`.

**The parameter-free property taken as accuracy.** It constrains the analyst. Nothing here tests whether readers extract more.

**Small n.** Six observations make six steps that look like a shape. [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) found a median smallest group of 4 across 703 physiology articles, below where any aggregate form is worth drawing.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing.

**Defensible, with the label said out loud:**

- "There is no bin width or bandwidth in this figure, so no analysis choice of mine is shaping the shape. Two primary sources state that property; neither tested a reader." `authority-asserted`.
- "The question is what fraction falls below a threshold, and this is the form built for the cumulative reading."
- "Four groups are overlaid without occlusion because the curves are monotonic. seaborn's documentation, one source, no experiment." `authority-asserted`.
- "The tail is drawn as a descending log-log ECDF because a power law is a straight line there. Readers misread log-log axes badly in the one study that measured it, on a different chart, so the caption states the finding in words as well."

**Commonly repeated, and the evidence does not support it:**

- ~~"ECDFs are more accurate than histograms."~~ Neither form is measured here. The histogram's transform has a free parameter and the ECDF's does not, a fact about the analyst, not the reader.
- ~~"It shows all the data, so nothing is hidden."~~ True of the transform. Dropped rows and censoring are invisible in the result, and ties show only as taller steps, and [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) measured that removal is not a neutral act.

## See also

- [distribution.md](distribution.md): the group, and whether shape is the question
- [histogram.md](histogram.md): the form this one is defined against
- [boxplot.md](boxplot.md), [violin-plot.md](violin-plot.md): the summary forms, and what a summary does not determine
- [../concepts/channels.md](../concepts/channels.md): what may be inherited, and how little applies here
