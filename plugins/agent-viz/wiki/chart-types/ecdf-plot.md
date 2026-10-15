---
type: chart-type
relationships: [distribution]
aliases: [ECDF plot, Empirical cumulative distribution function, Cumulative distribution plot]
---

# ECDF plots

Every observation of one continuous variable plotted at its own value against its rank, drawn as a monotonic step function so that the height at any value is the proportion of observations at or below it.

## When to reach for it, and when not

The form is defined for the case where one variable is the subject and the question is *cumulative*: what fraction sits below a threshold, where a given quantile falls, or whether a tail follows a power law. It is also the form that answers those questions without a smoothing parameter. [Wilke](../sources/wilke-fundamentals.md) opens chapter 8 on exactly that contrast, having spent chapter 7 on histograms and density plots:

> "they both share the limitation that the resulting figure depends to a substantial degree on parameters the user has to choose, such as the bin width for histograms and the bandwidth for density plots. As a result, both have to be considered as an interpretation of the data rather than a direct visualization of the data itself."

and states what the alternative buys: "These types of visualizations require no arbitrary parameter choices, and they show all of the data at once."

[seaborn](../sources/seaborn.md) reaches the same two properties independently, in its distributions tutorial: "Unlike the histogram or KDE, it directly represents each datapoint. That means there is no bin size or smoothing parameter to consider."

Questions the form does not answer:

| The question | Alternative |
|---|---|
| Is this one mode or two? | [Histogram](histogram.md) or [violin](violin-plot.md). Modality is a change of slope here, and both sources say so is the hard part |
| Where is the mass, roughly? | [Histogram](histogram.md). Shape is what the cumulative transform trades away |
| How do twelve groups compare on median and spread? | [Box plot](boxplot.md). Twelve step functions on one axis is a different kind of unreadable from twelve boxes |
| There are six observations | The six observations, plotted individually. [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) measured the sample sizes that make summary forms unreadable |
| How precisely do I know this mean? | That is the estimate, not the sample. See [distribution.md](distribution.md) on descriptive against inferential |
| Does this follow a named distribution? | A q-q plot, which Wilke pairs with the ECDF in the same chapter and which has no page here |

**Two directions exist and they answer different questions.** Ascending gives the fraction at or below a value; descending gives the fraction at or above it. Wilke: "Ascending cumulative distribution functions are more widely known and more commonly used than descending ones, but both have important applications. Descending cumulative distribution functions are critical when we want to visualize highly skewed distributions."

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable |
| Transform | Sort, then rank. Optionally normalize the rank by n, so the second axis is a cumulative frequency in [0, 1] rather than a count |
| Geometry | A monotonic step function, optionally with a point per observation |
| Scale | Value to position on one axis; rank or cumulative frequency to position on the other. Either axis may be logarithmic |
| Coordinates | Cartesian |
| Guides | Value axis with units, cumulative axis stating whether it is a count or a fraction, and the direction, since ascending and descending are both in use |

**The transform slot has no free parameter**, which is the whole argument for the form and the one structural fact that separates it from every other aggregate in this group. Compare [histogram.md](histogram.md), where the transform's bin width is a knob invisible in the output.

## Channels

Both axes are position along a common scale. That mapping is conjecture in the same way every chart-type-to-channel mapping is, and the accuracy attached to that channel is inherited from [channels.md](../concepts/channels.md) rather than native here.

**The inheritance is worth less than it looks, in both directions.** Reading a quantile off an ECDF is genuinely a position judgment, so the rank-1 result applies to that one task. But the tasks the form is criticized for, seeing modality and shape, are slope judgments, and the ranking's authors scope it to reading a value off a mark ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Nothing in that literature measures how accurately anyone reads a change of slope.

No study in this source set decomposed an ECDF into its cues.

## What it is measurably good at

**Nothing has been measured.** No controlled study in this source set tests ECDF reading against anything, or against any other distribution form.

What follows from the construction, and needs no experiment: the drawing determines the sample and the sample determines the drawing, so two different samples cannot produce the same ECDF the way they can produce the same box plot ([Matejka & Fitzmaurice](../studies/matejka-2017-datasaurus.md)) or the same bar-and-error-bar ([Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md)). That is definitional. The step from there to "readers therefore conclude better things" has nobody behind it.

## What it is measurably bad at

**Nothing has been measured here either.** Both primary sources in this corpus name the same weakness, and both name it as an impression rather than a result.

Wilke: "Unfortunately, they are a little less intuitive than a histogram or a density plot is, and I don't see them used frequently outside of highly technical publications."

seaborn is more specific about the task that suffers: "The major downside to the ECDF plot is that it represents the shape of the distribution less intuitively than a histogram or density curve. Consider how the bimodality of flipper lengths is immediately apparent in the histogram, but to see it in the ECDF plot, you must look for varying slopes." Both `authority-asserted`.

**The log-log tail reading carries a measured hazard from elsewhere.** Wilke's use for the descending log-log ECDF is that "a power law appears as a perfect straight line" on it, which is a fact about the construction. What that reading costs the reader is measured, on a different chart: [Menge et al. (2018)](../studies/menge-2018-log-scales.md) found domain experts reading log-log axes at 56% against 93% for linear-linear, and [Romano et al. (2020)](../studies/romano-2020-log-scales-covid.md) found log scales changing comprehension, prediction and policy preference. Neither tested an ECDF, so this is inherited and scope-limited rather than a finding about this form. It is the one place where the form's headline application sits on top of the corpus's clearest negative result about a scale.

## What is contested

Nothing is contested. The record does not disagree with itself here; it is silent, which [evidence-class.md](../concepts/evidence-class.md) keeps distinct from contested and from refuted.

Two sources agreeing is not a contest either, and the agreement is narrow: both say the form has no tuning parameter and both say shape is harder to see on it. Neither ran a reader experiment, and seaborn adds a third property Wilke does not, that monotonic curves overlay without occluding, which makes multiple groups comparable on one axis: "because the curve is monotonically increasing, it is well-suited for comparing multiple distributions." That is one voice, not two.

## The failure mode it invites

**Reading the cumulative axis as a density.** The height at a value is a running total, so a steep segment is a dense region and a flat segment is a gap. Nothing on the chart announces that, and the two are visually the reverse of what a histogram trains a reader to expect. `authority-asserted`, and it is the mechanism behind both sources' "less intuitive" complaint rather than a separate claim.

**Leaving the direction unlabeled.** Ascending and descending are both standard, they are reflections of each other, and a curve alone does not say which is drawn. The reader who assumes the wrong one inverts every proportion read off it. `authority-asserted`; the two directions are documented in Wilke chapter 8 and the ambiguity is this page's own stipulation.

**Treating the parameter-free property as accuracy.** The absence of a bin width removes one way for the analyst to shape the conclusion. It does not follow that readers extract more from the result, and no study in this corpus tests that.

**Small n.** With six observations the step function has six steps, and it looks like a shape without being one. The sample sizes [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) measured across 703 physiology articles, a median smallest group of 4, are below where any aggregate form in this group is worth drawing.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. No study in this corpus measures this form, and the page says so rather than borrowing a bar-chart result.

**Defensible, with the label said out loud:**

- "There is no bin width or bandwidth in this figure, so no analysis choice of mine is shaping the shape. Two primary sources state that property; neither tested a reader."
- "The question is what fraction falls below a threshold, and this is the form built for the cumulative reading."
- "Four groups are overlaid without occlusion because the curves are monotonic. seaborn's documentation, one source, no experiment."
- "The tail is drawn as a descending log-log ECDF because a power law is a straight line there. Readers misread log-log axes badly in the one study that measured it, on a different chart, so the caption states the finding in words as well."

**Commonly repeated, and not supported:**

- ~~"ECDFs are more accurate than histograms."~~ Nothing here measures either form. What is supported is that the histogram's transform has a free parameter and the ECDF's does not, which is a statement about the analyst, not about the reader.
- ~~"It shows all the data, so nothing is hidden."~~ True of the transform, and the sources say it. Ties, dropped rows and censoring are all invisible in the result, and [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) measured that removal is not a neutral act.

## See also

- [distribution.md](distribution.md) — the group, and the tests for whether shape is the question at all
- [histogram.md](histogram.md) — the form this one is defined against, and the free parameter it removes
- [boxplot.md](boxplot.md), [violin-plot.md](violin-plot.md) — the summary forms, and what a summary does not determine
- [../concepts/channels.md](../concepts/channels.md) — what may be inherited, and why little of it applies here
