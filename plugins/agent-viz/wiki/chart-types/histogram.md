---
type: chart-type
relationships: [distribution]
aliases: [Histogram]
---

# Histograms

Observations of one continuous variable sorted into contiguous bins, with the count in each bin drawn as a bar from zero.

## When to reach for it, and when not

The form is defined for the case where one variable is the subject, there are enough observations for a shape to exist, and the question is about that shape: where the mass sits, whether there are one or two modes, whether there is a gap, whether the tail is long. The histogram is the form that keeps every observation in the picture without drawing every observation.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| There are eight observations | The eight observations, plotted individually. At the sample sizes [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) measured, "boxplots and histograms would be difficult to interpret" |
| How do these twelve groups compare? | [Box plot](boxplot.md) or [violin](violin-plot.md). Histograms do not tile well and are hard to overlay past two |
| What is the median, and what is the spread? | A table, or a [box plot](boxplot.md). Reading a quantile off bar heights is a poor way to get a number |
| What proportion falls below this threshold? | An ECDF. No page here and no study; the cumulative reading is what it is built for |
| How does this change over time? | Change over time. A line chart |
| Is this difference between two means real? | That is a question about an estimate, not about the sample's shape. See [distribution.md](distribution.md) on descriptive versus inferential |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable |
| Transform | Assign each observation to a contiguous bin, then count (or count and divide by n and bin width for a density) |
| Geometry | Adjacent rectangles, one per bin |
| Scale | Bin boundaries to position on a continuous axis; count or density to bar height from zero |
| Coordinates | Cartesian |
| Guides | Value axis with units, count-or-density axis, and the bin width, which is not recoverable from the picture when the axis is a density |

Two slots carry everything that goes wrong with this chart. **The transform has a free parameter**, and **the scale slot has two different y meanings** that look identical: a count axis and a density axis produce the same drawing at different heights, and only one of them integrates to 1.

## Channels

Bin membership is position along a common scale; the count is bar height, read as position along a common scale with length as a second reading. That mapping is conjecture in the same way every chart-type-to-channel mapping is, and the accuracy claims attached to those channels are inherited from [channels.md](../concepts/channels.md) rather than native here.

**The inheritance mostly does not matter here.** The task a histogram is drawn for is shape: modality, skew, gaps, outliers. The channel ranking measures reading a value off a mark and its authors scope it to that explicitly ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Nothing in that literature says how accurately anyone perceives bimodality.

No study in this wiki's source set decomposed a histogram into its cues, the way [Skau & Kosara](../studies/skau-kosara-2016.md) did for the pie. So there is no type-level channel finding here.

## What it is measurably good at

**Nothing has been measured.** No controlled study in this source set tests histogram reading against anything.

What is measured is that almost nobody draws one. In Weissgerber et al.'s review of 703 physiology articles, 85.6% included a bar graph and 8.0% included a histogram. That is a prevalence finding about a literature, not a performance finding about the chart.

What follows from the construction, and needs no experiment: a histogram at a reasonable bin width preserves multimodality, gaps and asymmetry, all of which a mean and an interval discard. That is what makes it an answer to the many-distributions-one-summary problem ([distribution.md](distribution.md)), and the step from there to "readers therefore conclude better things" has nobody behind it.

## What it is measurably bad at

**Small samples.** The measured part is the sample sizes: median minimum group size of 4 across 703 articles, interquartile range 3 to 6. The judgment that histograms are unreadable at those sizes is the authors' own, stated as a recommendation rather than tested on readers. Their preferred form there is a univariate scatterplot.

**Everything else is untested rather than measured.** Comparison across many groups, reading values off bars, and side-by-side overlay are all commonly said to be histogram weaknesses, and no study here measures any of them.

## What is contested

Nothing is contested. The record does not disagree with itself here; it is mostly silent, which [evidence-class.md](../concepts/evidence-class.md) keeps deliberately distinct from contested and from refuted.

The specific hole: **there is no evidence-backed rule for bin width in this source set**, and the most complete general reference in it declines to give one, treating bin width and smoothing bandwidth as analysis choices ([wilke-fundamentals.md](../sources/wilke-fundamentals.md), chapters 7 and 14). Sturges, Freedman-Diaconis, Scott and the square-root rule are statistical derivations under distributional assumptions, not results about readers. `absence of evidence`.

## The failure mode it invites

**Tuning the bin width until the shape agrees with the conclusion, and not saying what it was.** The knob is invisible in the output, the reader cannot check it, and two defensible widths can show one mode or two. The mitigation [inventory.md](../inventory.md) topic 52 states is an explicit choice, confirmed against a wider and a narrower one. `authority-asserted`.

**Truncating the count axis.** A histogram is a bar chart, and bars encode by length from zero. [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) measured truncation inflating perceived effect size, found no significant difference between chart types, and found that the two tested axis-break glyphs did not measurably fix it. Their stimuli were bar and line charts of values rather than histograms, so this is inherited and scope-limited, not a result about histograms.

**Silently dropping rows.** Every dropped observation changes a count, and nothing in the drawing shows it. [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) measured that information removal degrades perceived quality and can produce wrong answers, on time series rather than on distributions, and they name the untested case: a caller who never noticed rows were dropped. The mechanical check is in [checks/matplotlib.md](../checks/matplotlib.md).

**Gaps between bars.** The FT's one-line gloss is "keep the gaps between columns small to highlight the 'shape' of the data" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). `authority-asserted`. A histogram with bar padding reads as a categorical bar chart, and the bins are not categories.

## Justifying the choice

**Defensible, evidence-backed:**

- "I drew the distribution rather than a mean and an interval, because four visibly different datasets produce the same bar-plus-error-bar, shown with realistic data and real p-values."
- "The count axis starts at zero. Truncation inflated perceived effect size across every chart type tested, and the break glyphs proposed as the fix did not measurably help."

**Defensible, with the label said out loud:**

- "Bin width is 5 units, stated in the caption, and both modes survive at 2 and at 10. There is no measured rule for bin width; the choice is an analysis decision and I disclosed it."
- "No padding between bars, so it reads as a continuous variable rather than as categories. Practitioner convention, not a measured result."
- "This is a density, not a count, so the bars integrate to 1 and the heights depend on the bin width."

**Commonly repeated, and not supported:**

- ~~"The histogram is the default way to show a distribution."~~ At the sample sizes actually found in published science it is the wrong choice, and the review that measured them recommends plotting the observations instead. It is also the least-tested common chart in this wiki: nothing here measures how anyone reads one.
- ~~"Use N bins, by rule."~~ Every named bin-count rule is a derivation under assumptions about the underlying distribution. None of them is a finding about readers, and no study here compares any two of them. `absence of evidence`.

## See also

- [distribution.md](distribution.md) — the group, and the tests for whether shape is the question at all
- [boxplot.md](boxplot.md), [violin-plot.md](violin-plot.md) — the summary forms, for when many groups have to fit on one axis
- [../concepts/channels.md](../concepts/channels.md) — what may be inherited, and why little of it applies here
