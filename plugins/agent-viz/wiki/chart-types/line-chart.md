---
type: chart-type
relationships: [change-over-time]
aliases: [Line chart]
---

# Line charts

Points ordered along a continuous axis, usually time, joined by segments, so that each segment's slope stands for a rate of change and the whole path stands for the shape of the series.

## When to reach for it, and when not

The form is defined for a continuous, ordered x where connecting consecutive points is a defensible claim, with enough points that the shape says what a table would not, and for questions about shape rather than individual values. The aspect ratio and the y-axis range sit outside the mark, and both have been measured.

| The question | Alternative |
|---|---|
| What was the value in each of these four quarters? | A column chart from zero, or a table. Values are the job, not shape |
| Which of these categories is biggest? | Sorted bar chart. Ranking, not time |
| How did these twenty categories change between 2010 and 2024? | [Slope chart](slope-chart.md). Two periods, many categories |
| x is a set of unordered categories | Bar or dot plot. A connecting line asserts a path between things that are not adjacent |
| How did the mix shift? | [Stacked bar](stacked-bar.md), or lines of shares rather than levels |
| How do these two variables relate, with time along for the ride? | [Scatterplot](scatterplot.md), or a [connected scatterplot](connected-scatterplot.md) |
| The amount accumulated under the curve is the point | [Area chart](area-chart.md), which brings the zero baseline with it |
| Every one of nine series matters equally | Small multiples. Schwabish's first redesign move on a multi-series line chart ([jonathan-schwabish.md](../people/jonathan-schwabish.md)), `authority-asserted` |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Usually none. Optionally smoothing, resampling, or interpolation across gaps, each of which is an assertion about values that are missing |
| Geometry | Path through the ordered points, optionally with a marker per point |
| Scale | Time to position on x, value to position on y. Slope is a function of both scales together, not of the data alone |
| Coordinates | Cartesian |
| Guides | Two axes, direct labels or a legend, optional gridlines |

An [area chart](area-chart.md) adds a fill, a sparkline drops the guides, a [slope chart](slope-chart.md) keeps two x positions and labels them directly, and a [connected scatterplot](connected-scatterplot.md) puts a second variable on x.

## Channels

Each point is position along a common scale, inherited from [channels.md](../concepts/channels.md) with the usual conjecture in the step from mark to channel. Hue carries series identity, not magnitude ([what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means)).

Slope, curvature, crossings and turning points are not value extraction, and the ranking's authors scope those tasks out ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Cleveland & McGill's 1985 table says the authors "have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle." So the endpoints sit on the best-measured channel, and the judgment the chart asks for is unmeasured.

## What it is measurably good at

No study in this corpus compares a line chart to a bar chart, a table or a slope chart for any task.

On slope judgment, [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md) gave a random half of their subjects a horizontal baseline under each segment:

> "As predicted, the addition of a baseline nearly eliminates the judgment error for mid-angles less than 45°. The error here is now nearly as small as in the height approximation results from Experiment 1. But, unpredicted, the linear trend was not eliminated for mid-angles larger than 45°."

Their summary is "Our hypothesis is not fully confirmed." The stimuli were isolated segment pairs, which the authors call the study's major limitation. A baseline or gridline is an evidence-backed lead for slope judgment in half the tested range, not a property of real line charts.

## What it is measurably bad at

**Aspect ratio.** [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) changed only the aspect ratio of a line chart and moved mean response on a 5-point "how much bigger" scale from 1.39 to 3.19, +129.5% (Mann-Whitney U = 1409, Z = 5.88, p < 0.0001, r = 0.66). The true values were printed on the chart. Chart type and distortion are confounded one to one, so the study cannot rank distortions, as the authors say.

**Truncation.** [Correll et al. (2020)](../studies/correll-2020-truncating-the-y-axis.md) found perceived severity rose with truncation, F(2, 76) = 89, p < 0.0001, and a line chart was no exception:

> "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)."

It is one subjective measure on one task, and this corpus's only test of whether lines are exempt.

**Silent gaps.** [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md), on line graphs among other stimuli:

> "Information removal can significantly degrade perceptions of data quality, and confidence. These methods even lead to incorrect responses if missing values break the visual continuity of a visualization."

Highlighting missing values beat downplaying them, which beat removing them. Zero-filling was the worst of three imputation methods. The authors call this preliminary guidance and say lower reader confidence is not automatically the goal.

**Log axes.** Among 623 Ecological Society of America members, comprehension was 93% on linear-linear and 56% on log-log, and the gap held for PhDs, professors and self-reported log-comfortable respondents ([Menge et al. 2018](../studies/menge-2018-log-scales.md)). On real COVID-19 death curves, a log axis left the general public with "a less accurate understanding of how the pandemic has developed," worse forecasts and different policy preferences ([Romano et al. 2020](../studies/romano-2020-log-scales-covid.md)).

## What is contested

**The zero baseline.** The sources disagree about scope, not honesty. [The Urban Institute guide](../sources/urban-institute.md) makes zero baselines absolute, then releases other chart types:

> "that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."

The FT scopes the rule by mark, capitalizing "always" for the filled column and writing "does not HAVE to start at zero (but preferable)" for the lollipop ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). Observable Plot forces zero only where area encodes the value ([observable-plot.md](../sources/observable-plot.md)). Datawrapper blocks truncated bar axes and offers a line chart as one of three remedies ([datawrapper-academy.md](../sources/datawrapper-academy.md)). [Vega-Lite](../sources/vega-lite.md) goes the other way, defaulting `zero` to true "for x and y channels if the quantitative field is not binned and no custom domain is provided," for every mark type, the strictest and least supported position here.

Proportional ink binds filled marks, not an unfilled line. Four sources reach that independently, so it is `authority-asserted` with tooling corroboration. The exaggeration effect is measured and not scoped by mark. So a line chart is released from the zero baseline, and truncating it still inflates the takeaway. Correll et al. measured that effect and still wrote "we resist the interpretation... that all charts with quantitative axes should include 0," so the range is a rhetorical choice, not a neutral default.

**Axis-break glyphs.** In the same study, a broken-axis glyph and a gradient fade made no significant difference to perceived severity. F(2, 60) = 3.1 against a critical value of 3.1504 puts p near 0.052, with 31 participants and no equivalence test or Bayes factor. A narrow failure to reject is not evidence of no effect, so "placebo" overstates it.

**Banking to 45 degrees.** [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md) widened Cleveland's sampled space and reported that "we find that, in general, slope ratio errors are not minimized around 45°." The shift "from near 45° to below 30°" is in the ANGLE submodel only, and Cleveland's subjects were told to compare heights. Cleveland's model "fit our data well in the regions considered in the original study" and fails to extrapolate. Talbot et al.'s replacement, ratios flatter and wider than banking algorithms produce, is a direction rather than a rule, untested on real plots.

**Log scales in general.** The direction is well supported and "never" is not. Menge et al. recommend instruction and author awareness rather than a ban; Romano et al. recommend linear "at least as a default option" and name a contemporaneous Canadian study that found no effect.

## The failure mode it invites

**Spaghetti.** Every series at equal weight shows only that there are many series. Small multiples and gray-plus-one-accent highlighting are the standard remedies, both `authority-asserted`. Schwabish's guideline is "Avoid the Spaghetti Chart," Urban recommends "gray for the majority of states and add color to just the few you want to highlight," and a search for a controlled experiment on one-accent emphasis found none ([refutations.md](../refutations.md)).

**Connecting points the data does not connect.** Unordered categories on x, uneven sampling drawn as even, or a straight run across missing data. The first two are `authority-asserted`. The third is measured, and the only one shown to produce wrong answers rather than lower confidence.

## Justifying the choice

**Defensible, evidence-backed:**

- "The y-axis starts at 40 rather than 0, and the subtitle says so. Truncation inflates perceived effect size on line charts as much as on bars, measured, so I am not treating the absence of a fill as an exemption."
- "The 2019 gap is drawn as a gap rather than interpolated. In the missing-data study, breaking visual continuity silently produced incorrect answers, not just lower confidence."
- "I did not put this on a log axis. Log-log comprehension measured 56% against 93% linear among professional ecologists, and holding a PhD bought zero points on log axes with untransformed values."
- "The aspect ratio is a deliberate choice, because aspect ratio alone moved reader judgments by 129.5% on a line chart with the true values printed on it."

**Defensible, with the label said out loud:**

- "Flatter and wider than the default." Talbot et al.'s model result, untested on real plots.
- "Gridlines are on, which may help slope judgment." Measured on isolated segments, and only below 45 degrees.
- "Nine series became nine small multiples, with everything else gray." Consensus across the major sources here, tested by none.

**Commonly repeated, and the evidence does not support it:**

- ~~"Bank the slopes to 45 degrees."~~ A local fit, not a general optimum. Talbot et al. call their conclusion deflationary: "the theory of aspect ratio selection is not as simple as it once seemed."
- ~~"Line charts do not need a zero baseline, so truncation is not an issue here."~~ Two rules spliced together. The second half does not follow.
- ~~"An axis break tells the reader what happened, so the chart is honest."~~ The tested designs, on bar charts, did not measurably reduce the exaggeration, at a sample too small to detect a small reduction.
- ~~"Log scales are fine for a technical audience."~~ The population that failed at 56% was 69% PhDs, and 89% of all respondents had log-transformed data themselves.

## See also

- [change-over-time.md](change-over-time.md): the group, and its two free parameters
- [area-chart.md](area-chart.md): this chart plus a fill, and what the fill costs
- [../concepts/channels.md](../concepts/channels.md): the evidence this page inherits, and its stated scope
- [../refutations.md](../refutations.md): banking, truncation remedies, log scales
