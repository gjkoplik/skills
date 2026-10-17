---
type: chart-type
relationships: [change-over-time]
aliases: [Line chart]
---

# Line charts

Points ordered along a continuous axis, usually time, joined by segments, so that each segment's slope stands for a rate of change and the whole path stands for the shape of the series.

## When to reach for it, and when not

The form is defined for a continuous, ordered x where connecting consecutive points is a defensible claim, with enough points that the shape, not any one value, says what a table would not. Its group is [change-over-time](change-over-time.md).

| The question | Alternative |
|---|---|
| What was the value in each of these four quarters? | A column chart from zero, or a table. Values are the job, not shape |
| Which of these categories is biggest? | Sorted bar chart. Ranking, not time |
| How did these twenty categories change between 2010 and 2024? | [Slope chart](slope-chart.md). Two periods, many categories |
| x is a set of unordered categories | Bar or dot plot. A line asserts a path between things that are not adjacent |
| How did the mix shift? | [Stacked bar](stacked-bar.md), or lines of shares rather than levels |
| How do these two variables relate, with time along for the ride? | [Scatterplot](scatterplot.md), or a [connected scatterplot](connected-scatterplot.md) |
| The amount accumulated under the curve is the point | [Area chart](area-chart.md), which brings the zero baseline with it |
| Every one of nine series matters equally | Small multiples, Schwabish's first redesign move ([jonathan-schwabish.md](../people/jonathan-schwabish.md)), `authority-asserted` |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Usually none. Optionally smoothing, resampling, or interpolation across gaps, each an assertion about missing values |
| Geometry | Path through the ordered points, optionally with a marker per point |
| Scale | Time to position on x, value to position on y. Slope is a function of both scales together, not of the data alone |
| Coordinates | Cartesian |
| Guides | Two axes, direct labels or a legend, optional gridlines |

An [area chart](area-chart.md) adds a fill, a sparkline drops the guides, a [slope chart](slope-chart.md) keeps two x positions, and a [connected scatterplot](connected-scatterplot.md) puts a second variable on x.

## Channels

Each point is position along a common scale, with the usual conjecture in the step from mark to channel ([channels.md](../concepts/channels.md)). Hue carries series identity, not magnitude ([what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means)).

Slope, curvature, crossings and turning points are not value extraction, and the ranking's authors scope them out ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Cleveland & McGill's 1985 table says they "have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle." So the endpoints sit on the best-measured channel, and the judgment the chart asks for is unmeasured.

## What is measured

No study in this corpus compares a line chart to a bar chart, a table or a slope chart for any task.

[Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md) gave half their subjects, at random, a baseline under each segment:

> "As predicted, the addition of a baseline nearly eliminates the judgment error for mid-angles less than 45°. The error here is now nearly as small as in the height approximation results from Experiment 1. But, unpredicted, the linear trend was not eliminated for mid-angles larger than 45°."

Their summary is "Our hypothesis is not fully confirmed." The authors name the isolated segment-pair stimuli as the major limitation. `evidence-backed` for segments only.

Four settings distort the reading, each `evidence-backed`:

- **Aspect ratio** alone moved mean response on a 5-point "how much bigger" scale from 1.39 to 3.19, +129.5% (Mann-Whitney U = 1409, Z = 5.88, p < 0.0001, r = 0.66), with the true values printed ([Pandey et al. 2015](../studies/pandey-2015-deceptive-visualizations.md)). Chart type and distortion are confounded, so it cannot rank distortions.
- **Truncation** raised perceived severity, F(2, 76) = 89, p < 0.0001, on lines as on bars ([Correll et al. 2020](../studies/correll-2020-truncating-the-y-axis.md)). It is one subjective measure on one task, and the only test here of a line exemption.

  > "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)."

- **Silent gaps**, on line graphs among other stimuli ([Song & Szafir 2019](../studies/song-szafir-2019-missing-data.md)):

  > "Information removal can significantly degrade perceptions of data quality, and confidence. These methods even lead to incorrect responses if missing values break the visual continuity of a visualization."

  Highlighting missing values beat downplaying them, which beat removing them, and zero-filling was the worst of three imputations. The authors call this preliminary and say lower confidence is not automatically the goal.
- **Log axes.** Among 623 Ecological Society of America members (69% PhDs, 89% having log-transformed data themselves), comprehension was 93% on linear-linear and 56% on log-log. The gap held for PhDs, professors and the self-reported log-comfortable, and a PhD added 0 points on log axes with untransformed values ([Menge et al. 2018](../studies/menge-2018-log-scales.md)). On real COVID-19 death curves, a log axis left the public with "a less accurate understanding of how the pandemic has developed," worse forecasts and different policy preferences ([Romano et al. 2020](../studies/romano-2020-log-scales-covid.md)). A ban is `contested`. Menge et al. recommend instruction and author awareness. Romano et al. recommend linear "at least as a default option" and name a contemporaneous Canadian study that found no effect.

Where the record disagrees:

- **The zero baseline** is `contested` on scope. Four sources independently confine it to filled marks, `authority-asserted` with tooling corroboration. [The Urban Institute guide](../sources/urban-institute.md) makes zero absolute, then exempts charts

  > "that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."

  The FT capitalizes "always" for the filled column and writes "does not HAVE to start at zero (but preferable)" for the lollipop ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). [Observable Plot](../sources/observable-plot.md) forces zero only where area encodes the value. [Datawrapper](../sources/datawrapper-academy.md) offers a line chart as one of three fixes for a truncated bar axis. [Vega-Lite](../sources/vega-lite.md), least supported, defaults `zero` to true "for x and y channels if the quantitative field is not binned and no custom domain is provided," on every mark. Truncation still inflates a line, and Correll et al. wrote "we resist the interpretation... that all charts with quantitative axes should include 0," so the range is a rhetorical choice, not a neutral default.
- **Banking to 45 degrees** is `contested`. Widening Cleveland's sampled space, Talbot et al. report that "we find that, in general, slope ratio errors are not minimized around 45°." The shift "from near 45° to below 30°" is in the ANGLE submodel only, and Cleveland's subjects compared heights. Cleveland's model "fit our data well in the regions considered in the original study" and fails to extrapolate.
- **Axis-break glyphs**, on bar charts in Correll et al., did not significantly reduce perceived severity. F(2, 60) = 3.1 against a critical value of 3.1504 puts p near 0.052, with 31 participants and no equivalence test or Bayes factor. A narrow miss is not evidence of no effect, so "placebo" overstates it: `absence of evidence`.

## The failure mode it invites

**Spaghetti.** Equal-weight series show only that there are many. Schwabish says "Avoid the Spaghetti Chart." Urban recommends "gray for the majority of states and add color to just the few you want to highlight," and both are `authority-asserted`. No controlled experiment on one-accent emphasis was found ([refutations.md](../refutations.md)).

**Connecting points the data does not connect.** Unordered categories on x and uneven sampling drawn as even are `authority-asserted`. Bridging missing data is the measured silent gap.

## Justifying the choice

**Defensible, evidence-backed:**

- "The y-axis starts at 40, stated in the subtitle. Truncation inflates lines as much as bars."
- "The 2019 gap is drawn as a gap, because bridged gaps produced wrong answers."
- "No log axis. Professional ecologists read log-log at 56% against 93% linear."
- "The aspect ratio was chosen, not defaulted, because it alone moved judgments by 129.5%."

**Defensible, with the label said out loud:**

- "Flatter and wider than the default." A model result, untested on real plots.
- "Gridlines are on, which may help slope judgment." Measured on isolated segments below 45 degrees.
- "Nine series became nine small multiples, with everything else gray." Consensus here, tested by none.

**Commonly repeated, and the evidence does not support it:**

- ~~"Bank the slopes to 45 degrees."~~ A local fit. Talbot et al.: "the theory of aspect ratio selection is not as simple as it once seemed."
- ~~"Line charts do not need a zero baseline, so truncation is not an issue here."~~ The second half does not follow.
- ~~"An axis break tells the reader what happened, so the chart is honest."~~ Untested at adequate power.
- ~~"Log scales are fine for a technical audience."~~ The 56% audience was mostly PhDs who log-transform their own data.
