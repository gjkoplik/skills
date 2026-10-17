---
type: chart-type
relationships: [distribution]
aliases: [Histogram]
---

# Histograms

Observations of one continuous variable sorted into contiguous bins, with the count in each bin drawn as a bar from zero.

## When to reach for it, and when not

The form is defined for one variable with enough observations to have a shape, where the question is the shape: mass, modes, gaps, tail.

| The question | Alternative |
|---|---|
| There are eight observations | The observations. At [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md)'s sample sizes, "boxplots and histograms would be difficult to interpret" |
| How do these twelve groups compare? | [Box plot](boxplot.md) or [violin](violin-plot.md) |
| What is the median, and what is the spread? | A table, or a [box plot](boxplot.md) |
| What proportion falls below this threshold? | An [ECDF](ecdf-plot.md), for the cumulative reading. No study behind it |
| How does this change over time? | A line chart |
| Is this difference between two means real? | An estimate question ([distribution.md](distribution.md)) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable |
| Transform | Bin, then count (or divide the count by n and bin width for a density) |
| Geometry | Adjacent rectangles, one per bin |
| Scale | Bin boundaries to position on a continuous axis. Count or density to bar height from zero |
| Coordinates | Cartesian |
| Guides | Value axis with units, count-or-density axis, and the bin width, which a density axis hides |

Bin width is a free parameter. Count and density axes draw the same shape at different heights, and only density integrates to 1.

## Channels

Bin membership and count are both position along a common scale, the count with length as a second reading ([channels.md](../concepts/channels.md), a conjectured mapping). That inheritance mostly does not apply. A histogram is drawn for shape, and the ranking is scoped to reading a value off a mark ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). No study here measures perceiving bimodality or decomposes a histogram, as [Skau & Kosara](../studies/skau-kosara-2016.md) did the pie.

## What is measured

No controlled study here tests histogram reading. Weissgerber et al.'s review of 703 physiology articles measured only prevalence: 85.6% included a bar graph and 8.0% a histogram. The same review found a median minimum group size of 4, interquartile range 3 to 6. Calling histograms unreadable at those sizes is the authors' untested recommendation, made in favor of a univariate scatterplot.

By construction, a reasonable bin width keeps the multimodality, gaps and asymmetry a mean and interval discard ([distribution.md](distribution.md)). Nobody has shown readers conclude better from it. Many-group comparison, reading values off bars, and overlay are reputed weaknesses, all untested. `absence of evidence`.

No evidence-backed bin-width rule exists here. Wilke treats bin width and bandwidth as analysis choices ([wilke-fundamentals.md](../sources/wilke-fundamentals.md), chapters 7 and 14). Sturges, Freedman-Diaconis, Scott and the square-root rule are distributional derivations, not reader results. `absence of evidence`.

The record is silent rather than `contested` ([evidence-class.md](../concepts/evidence-class.md)).

## The failure mode it invites

**Tuning the bin width until the shape agrees with the conclusion, and not saying what it was.** Two defensible widths can show one mode or two, and the output hides which. [inventory.md](../inventory.md) topic 52 asks for an explicit choice, checked against wider and narrower ones. `authority-asserted`.

**Truncating the count axis.** [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) found truncation inflated perceived effect size with no significant difference between chart types, and the two axis-break glyphs tested did not measurably fix it. Their stimuli were bar and line charts, so this is inherited.

**Silently dropping rows.** Each dropped row silently changes a count. [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) found information removal degrades perceived quality and can produce wrong answers, on time series. They name the unnoticed drop as untested. The mechanical check is in [checks/matplotlib.md](../checks/matplotlib.md).

**Gaps between bars.** The FT: "keep the gaps between columns small to highlight the 'shape' of the data" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). `authority-asserted`. Padded bins read as categories.

## Justifying the choice

**Defensible, evidence-backed:**

- "I drew the distribution rather than a mean and an interval, because four visibly different datasets produce the same bar-plus-error-bar, shown with realistic data and real p-values ([Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md))."
- "The count axis starts at zero. Truncation inflated perceived effect size across every chart type tested, and the break glyphs proposed as the fix did not measurably help. The stimuli were bar and line charts, so for a histogram this is inherited."

**Defensible, with the label said out loud:**

- "Bin width is 5 units, stated in the caption, and both modes survive at 2 and at 10. There is no measured rule for bin width; the choice is an analysis decision and I disclosed it."
- "No padding between bars, so it reads as a continuous variable rather than as categories. Practitioner convention, not a measured result."
- "This is a density, not a count, so the bars integrate to 1 and the heights depend on the bin width."

**Commonly repeated, and the evidence does not support it:**

- ~~"The histogram is the default way to show a distribution."~~ The review that measured published sample sizes recommends plotting the observations, and nothing here measures how anyone reads one.
- ~~"Use N bins, by rule."~~ Each named rule is a distributional derivation, untested on readers. `absence of evidence`.

## See also

- [distribution.md](distribution.md): the group, and when shape is the question
- [boxplot.md](boxplot.md), [violin-plot.md](violin-plot.md): summary forms for many groups
- [../concepts/channels.md](../concepts/channels.md): the inherited channels
