---
type: chart-type
relationships: [change-over-time]
aliases: [Line chart]
---

# Line charts

Points ordered along a continuous axis, usually time, joined by segments, so that the slope of each segment stands for a rate of change and the whole path stands for the shape of the series.

## When to reach for it, and when not

**Reach for it when** x is continuous and ordered, the connection between consecutive points is a claim you are willing to defend, there are enough points that the shape carries information a table would not, and the reader's question is about the shape rather than about individual values.

**The two decisions that matter most are not the mark.** They are the aspect ratio and the y-axis range, and both have been measured.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| What was the value in each of these four quarters? | A column chart from zero, or a table. Values are the job, not shape |
| Which of these categories is biggest? | Sorted bar chart. Ranking, not time |
| How did these twenty categories change between 2010 and 2024? | [Slope chart](slope-chart.md). Two periods, many categories |
| x is a set of unordered categories | Bar or dot plot. A connecting line asserts a path between things that are not adjacent |
| How did the mix shift? | [Stacked bar](stacked-bar.md), or lines of shares rather than levels |
| How do these two variables relate, with time along for the ride? | [Scatterplot](scatterplot.md), or a [connected scatterplot](connected-scatterplot.md) |
| The amount accumulated under the curve is the point | [Area chart](area-chart.md), and accept the zero baseline with it |
| Every one of nine series matters equally | Small multiples. Schwabish's first redesign move on a multi-series line chart ([jonathan-schwabish.md](../people/jonathan-schwabish.md)), `authority-asserted` |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Usually none. Optionally smoothing, resampling, or interpolation across gaps, each of which is an assertion about values you do not have |
| Geometry | Path through the ordered points, optionally with a marker per point |
| Scale | Time to position on x, value to position on y. **Slope is a function of both scales together, not of the data alone** |
| Coordinates | Cartesian |
| Guides | Two axes, direct labels or a legend, optional gridlines |

The near-duplicates this collapses: an [area chart](area-chart.md) is this chart with a fill added to the geometry slot, a sparkline is this chart with the guides slot emptied, a [slope chart](slope-chart.md) is this chart with exactly two x positions and direct labels in place of axes, and a [connected scatterplot](connected-scatterplot.md) swaps the x scale from time to a second variable.

## Channels

**Position along a common scale, for each plotted point**, inherited from [channels.md](../concepts/channels.md) rather than measured on this form. The mapping step is conjecture in the source literature and Cleveland & McGill flag it as one every time they make it, so it stays conjecture here.

**Hue, for series identity.** Not a magnitude channel and not scored as one. See [what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means).

The complication is that **the reading a line chart is for is not the reading the ranking scores.** Slope, curvature, crossings and turning points are not value extraction, and the ranking's authors scope themselves out of exactly those tasks ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Cleveland & McGill's 1985 table also says the authors "have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle." So a line chart puts endpoints on the best-measured channel and then asks for a judgment the measurements do not cover.

## What it is measurably good at

**Nothing in this corpus measures a line chart against an alternative.** No study here compares it to a bar chart, a table, or a slope chart for any task. That is a statement about the field's coverage.

One adjacent result is worth carrying, because slope judgment is this chart's core task. [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md) randomly gave half their subjects a visible horizontal baseline under each line segment:

> "As predicted, the addition of a baseline nearly eliminates the judgment error for mid-angles less than 45°. The error here is now nearly as small as in the height approximation results from Experiment 1. But, unpredicted, the linear trend was not eliminated for mid-angles larger than 45°."

Their own summary is "Our hypothesis is not fully confirmed." The stimulus is two isolated segments rather than a plot, and the authors name that as the study's major limitation. So: a visible baseline or gridline is an evidence-backed lead for slope judgment in half the tested range, not a demonstrated property of real line charts.

## What it is measurably bad at

Each of these is better read as something the form fails to protect the reader from.

**Resisting the designer's aspect-ratio choice.** [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) changed nothing but the aspect ratio of a line chart and moved mean response on a 5-point "how much bigger" scale from 1.39 to 3.19, +129.5%, Mann-Whitney U = 1409, Z = 5.88, p < 0.0001, r = 0.66. The actual numbers were printed on the chart, so this is not a failure to read values. Do not use this to rank distortions against each other: chart type and distortion are confounded one to one in that study, and the authors say so.

**Resisting truncation.** [Correll et al. (2020)](../studies/correll-2020-truncating-the-y-axis.md) found perceived severity rose with truncation, F(2, 76) = 89, p < 0.0001, and that the chart being a line made no significant difference: "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)." One subjective measure on one task, and it is the one place to point when someone claims lines are exempt.

**Silent gaps.** [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md), on line graphs among other stimuli: "Information removal can significantly degrade perceptions of data quality, and confidence. These methods even lead to incorrect responses if missing values break the visual continuity of a visualization." Highlighting missing values beat downplaying them, which beat removing them, and zero-filling was the worst of the three imputation methods tested. The authors describe their own result as preliminary guidance, and they are explicit that degrading reader confidence is not automatically the goal.

**Log axes.** Among 623 Ecological Society of America members, comprehension was 93% on linear-linear against 56% on log-log ([Menge et al. 2018](../studies/menge-2018-log-scales.md)), and the gap did not close for PhDs, professors, or self-reported log-comfortable respondents. On the general public reading real COVID-19 death curves, a log axis left readers with "a less accurate understanding of how the pandemic has developed," worse forecasts, and different policy preferences ([Romano et al. 2020](../studies/romano-2020-log-scales-covid.md)). Time series are where log scales get reached for most.

## What is contested

**Whether a line chart needs a zero baseline. The sources disagree, and they disagree about scope rather than about honesty.**

- [The Urban Institute guide](../sources/urban-institute.md) makes zero baselines an absolute and then explicitly releases this form: other chart types "that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."
- The FT applies the rule by mark, capitalizing "always" for the filled column and writing "does not HAVE to start at zero (but preferable)" for the lollipop ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). Observable Plot forces zero only where area encodes the value ([observable-plot.md](../sources/observable-plot.md)). Datawrapper hard-blocks truncated bar axes in the product and offers a line chart as one of its three remedies ([datawrapper-academy.md](../sources/datawrapper-academy.md)).
- [Vega-Lite](../sources/vega-lite.md) goes the other way and ships the strict version as a default: `zero` is true "for x and y channels if the quantitative field is not binned and no custom domain is provided," for every mark type. That is a stronger commitment than any style guide here makes, and it is the position with the least support behind it.

**What survives.** Proportional ink is an argument about filled marks, and it genuinely does not bind an unfilled line; four sources reach that independently and it is `authority-asserted` with tooling corroboration, not measured. The exaggeration effect is a separate claim, it was measured, and it is not scoped by mark. Both facts hold at once: you are allowed to truncate a line chart, and truncating it will inflate what the reader takes away. Correll et al. refuse the maximalist reading in as many words, "we resist the interpretation... that all charts with quantitative axes should include 0," while measuring the effect anyway. Treat the range as a rhetorical choice you own and disclose.

**Whether an axis-break glyph fixes it.** The two static designs tested, a broken-axis glyph and a gradient fade, produced no significant difference in perceived severity. F(2, 60) = 3.1 against a critical value of 3.1504 means p is about 0.052, with 31 participants, no equivalence test and no Bayes factor. That is a knife-edge failure to reject, not evidence of no effect, and "placebo" overstates it. The supportable version is that you cannot rely on a jagged marker to do the work.

**Banking to 45 degrees.** Cleveland's aspect-ratio guideline is in every curriculum. [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md) widened the sampled space and reported that "we find that, in general, slope ratio errors are not minimized around 45°." Two things a careless citation drops. The shift "from near 45° to below 30°" belongs to the ANGLE submodel only, and Cleveland's subjects were instructed to compare heights. And Cleveland replicates inside his own range: his model "fit our data well in the regions considered in the original study" and fails to extrapolate. **Accurate phrasing: 45 degrees is not the error-minimizing ratio in general, and Cleveland's result holds within the moderate regime he tested.** The constructive replacement is a direction rather than a rule, that flatter and wider ratios than banking algorithms produce should be preferred, and it has never been tested on real plots.

**Log scales in general.** The direction is well supported and "never" is not. Menge et al. recommend instruction and author awareness rather than a ban; Romano et al. recommend linear "at least as a default option" and themselves name a contemporaneous Canadian study that found no effect. Cite the pair, or neither.

## The failure mode it invites

**Spaghetti.** Every series drawn at equal weight, so the chart shows that there are many series and nothing else. The standard remedies are small multiples and gray-plus-one-accent highlighting, and both are `authority-asserted`: Schwabish's guideline is literally named "Avoid the Spaghetti Chart," Urban recommends "gray for the majority of states and add color to just the few you want to highlight," and a search for a controlled experiment testing one-accent emphasis returned nothing ([refutations.md](../refutations.md)). The breadth of agreement is not evidence.

**Connecting points the data does not connect.** Unordered categories on x, uneven sampling drawn as if even, or a straight run across a period where the data is missing. The first two are `authority-asserted`; the third is the measured one, and it is the only failure in this section that produced wrong answers rather than lower confidence.

## Justifying the choice

**Defensible, evidence-backed:**

- "The y-axis starts at 40 rather than 0, and the subtitle says so. Truncation inflates perceived effect size on line charts as much as on bars, measured, so I am not treating the absence of a fill as an exemption."
- "The 2019 gap is drawn as a gap rather than interpolated. Breaking visual continuity silently is the one thing in this literature that produced incorrect answers, not just lower confidence."
- "I did not put this on a log axis. Log-log comprehension measured 56% against 93% linear among professional ecologists, and holding a PhD bought zero points on the log condition."
- "The aspect ratio is a deliberate choice, because aspect ratio alone moved reader judgments by 129.5% on a line chart with the true values printed on it."

**Defensible, with the label said out loud:**

- "Flatter and wider than the default." That is Talbot et al.'s constructive result from a model, not a validated design rule, and it has not been shown to transfer to real plots.
- "Gridlines are on, which may help slope judgment." A visible baseline nearly eliminated slope error below 45 degrees and did nothing above it, on isolated line segments rather than plots.
- "Nine series became nine small multiples, with everything else gray." Practitioner consensus, stated by every major source here and tested by none of them.

**Commonly repeated, and the evidence does not support it:**

- ~~"Bank the slopes to 45 degrees."~~ Not the error-minimizing ratio in general. Cleveland's result is a local fit inside the range he tested, and the paper that showed this calls its own conclusion deflationary: "the theory of aspect ratio selection is not as simple as it once seemed."
- ~~"Line charts do not need a zero baseline, so truncation is not an issue here."~~ Two rules spliced into one. The first half is right and the second does not follow from it.
- ~~"An axis break tells the reader what happened, so the chart is honest."~~ The tested designs did not measurably reduce the exaggeration, at a sample size that could not have detected a small one either.
- ~~"Log scales are fine for a technical audience."~~ The population that failed at 56% was 69% PhDs, 89% of whom had log-transformed data themselves.

## See also

- [change-over-time.md](change-over-time.md) — the group, and the two free parameters it hands you
- [area-chart.md](area-chart.md) — this chart plus a fill, and what the fill costs
- [../concepts/channels.md](../concepts/channels.md) — the evidence this page inherits, and its stated scope
- [../refutations.md](../refutations.md) — banking, truncation remedies, log scales
