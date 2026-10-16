---
type: chart-type
relationships: [magnitude]
aliases: [Bar chart, Column chart, Coxcomb, Grouped bar chart]
---

# Bar charts

One filled rectangle per category, running from a common baseline, its length encoding the value.

## When to reach for it, and when not

The form is defined for reading and comparing values across a handful of named categories, on position along a common scale ([channels.md](../concepts/channels.md)).

| The question | Alternative |
|---|---|
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). A bar chart asserts nothing about a total |
| What does the distribution look like? | A histogram or the raw points (below) |
| Are these two group means different? | Not a bar with error bars (below) |
| How did this move over time? | A line chart |
| Forty categories | [Lollipop chart](lollipop-chart.md) or an aggregated tail. Row count sets the height |
| Where does each item sit relative to a target? | A [diverging bar](diverging-bar-chart.md) off the reference ([deviation](deviation.md)) |
| The values span orders of magnitude | A log scale with the base stated, not a truncated bar |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with a magnitude |
| Transform | Usually none. A count, mean or rate computed upstream is an undisclosed transform |
| Geometry | Filled rectangle, one edge on the baseline |
| Scale | Magnitude to length, anchored at zero |
| Coordinates | Cartesian. Orientation only picks the value axis |
| Guides | A quantitative axis with visible baseline, a category axis, labels |

A **column chart** swaps the axes. A **grouped bar chart** adds a second category, a **[stacked bar](stacked-bar.md)** a cumulative sum, and a **[lollipop](lollipop-chart.md)** a point and stem in place of the rectangle. A **coxcomb** (polar-area diagram) puts it in polar coordinates with equal angles, the quantity encoded by radius and read as area. Nightingale used "coxcomb" for a booklet, never a diagram, and Cook's 1914 biography moved the name to the chart ([florence-nightingale.md](../people/florence-nightingale.md)).

## Channels

Cleveland & McGill call the mapping conjecture: position along a common scale, read at the bar's end, is primary "but judgments of area and length probably also play a role." Claims are inherited from [channels.md](../concepts/channels.md) unless a study used bars.

[Skau, Harrison & Kosara (2015)](../studies/skau-2015-embellished-bars.md) give the one piece of type-level evidence on the mechanism. A capped bar matched the plain bar on absolute judgments with slightly lower variance, and rounded or pointed tops did worse:

> "This result suggests that users indeed rely on strong lines at the ends of bars to mentally extend the bar end to the value axis, especially when considering the comparatively poor performance of the embellishments that distort the top of the bar (rounded caps, triangles, etc.)"

It is offered as a hypothesis, not a tested finding.

## What is measured

Bars are measured as good at reading values, `evidence-backed`. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), on the substitution a stacked or floating bar forces:

> "the average errors for length judgments are 40%-250% larger than those for position judgments"

Their second experiment set bars against pies:

> "In only 3 of the 40 cases was the pie chart more accurate on average than the bar chart."

The error difference was "a factor of 2^.97 = 1.96, and is statistically significant." [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) replicated it on Mechanical Turk: "position still significantly outperformed length," and angle and area also trailed position.

Bars beat dot plots on ratio comparisons, `evidence-backed` at secondhand, from an aside in [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md):

> "There are tasks where asymmetric encodings outperform symmetric encodings; for instance, comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots."

A deformed bar is measured as worse, `evidence-backed`. Skau et al. tested six embellishments. On relative comparisons, with the axis removed:

> "All adaptations except the extended embellishment performed significantly worse than the baseline on relative judgements. Even small changes, for example the rounded bar, produced a significantly higher error rate."

Mean log error was 1.43 plain, 1.86 with a rounded top and 2.33 for quadratically scaled bars. On absolute judgments, with the axis present, only the quadratic bars cleared the corrected threshold.

A truncated bar axis exaggerates differences, `evidence-backed`. In [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) it moved responses on a "how much bigger" scale from a control mean of 1.45 to 2.77, up 91.0% (Mann-Whitney U = 1144, Z = 3.36, p = 0.0003), with true values printed. [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) could not tell two break glyphs from plain truncation on perceived severity: "the exaggeration introduced through truncation appears to persist across chart types and chart designs, and even when participants make accurate reports of the numbers they observe." The phrasing is hedged and the statistics knife-edge ([refutations.md](../refutations.md#axis-break-glyphs-as-the-truncation-remedy)). The zero-baseline rule itself is `authority-asserted`: style guides here scope it by mark without testing it, and [Vega-Lite](../sources/vega-lite.md) forces zero on every quantitative positional scale.

Error bars on a bar are measured as biasing inference, `evidence-backed`. Correll & Gleicher name two defects. The first:

> "**Within-the-bar bias:** the glyph of a bar provides a false metaphor of containment, where values within the bar are seen as likelier than values outside the bar."

Outcomes inside the bar were rated significantly likelier than outcomes equally far above the mean (interaction F(2,2) = 21.3, p < 0.0001), and no symmetric encoding did this. It persisted with the outcome in text and lifted only when the margin of error left the chart too, when strategy adherence fell from 91.6% of trials to 62.2% while confidence rose. The second is binary interpretation, a value read as either inside the margin of error or outside it. In the two-sample experiment, bar readers were more confident than readers of the other encodings, more so on differences that fail a t-test (M = 4.42 versus 4.15).

A bar standing in for a distribution hides it. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) found that 85.6% of 703 physiology articles used a bar graph, at a median minimum group size of 4, `evidence-backed` as prevalence. They note "many different data distributions can lead to the same bar or line graph." Their Fig 1 shows four datasets (symmetric, outlier-driven, possibly bimodal, n = 3) whose bars are within half a unit. No readers were tested.

Embellishment around the bar is `contested`. [Bateman et al. (2010)](../studies/bateman-2010-useful-junk.md) put Nigel Holmes imagery around correctly drawn bars. Accuracy was "no worse than for plain charts," recall was better after two to three weeks, and the value-message score favored the embellished charts (p = .003). Skau et al. deformed the bar itself, and error rose. A Holmes bar keeps its flat top, so Skau's mechanism predicts Bateman's result, and Skau warns only that embellishment touching "the primary chart elements can reduce the communication accuracy of the chart." Deforming the mark is not contested. Two limits on Bateman:

- In a four-way replication (Syeda et al. 2023), the asynchronous study found no significant difference on any of the four long-term recall questions, while synchronous replications matched. Preference held in all five studies, and description accuracy replicated best. Bateman's directional tests were one-tailed at α = .05, uncorrected across a dozen-plus comparisons.
- The designer encoded the message into the imagery, as the authors concede: the monster's teeth trace the trend and the title says "monstrous." The result may concern integrated illustration, not embellishment in general.

The reason bars beat pies is `contested`, though the result is secure. "Length beats angle" was never tested by Cleveland & McGill, who say their two experiments may not be compared. Heer & Bostock ran it head to head and reported "the results do not support this" ([channels.md](../concepts/channels.md#the-one-joint-where-the-folk-ranking-breaks)). Bars are read on position, and position against angle is measured.

Orientation is measured only in a headset. [Siqueira Rodrigues, Israel & Kosch (2026)](../studies/siqueira-rodrigues-2026-vr-graphical-perception.md) measured 6.40% mean absolute error for horizontal bars against 3.33% for vertical in a head-mounted display (d = 2.46, generalized η² = .49). The gap was absent face-on (p = .713) and grew with lateral offset (2.75 m, 4.8125 m) for horizontal bars only, as their value axis foreshortens. The authors call it an apparatus effect, "consistent with the removal of bezel-based spatial anchors rather than a fundamental change in the perceptual hierarchy." Orientation on a flat screen is `absence of evidence`.

## The failure mode it invites

**Drawn by default.** Plotting libraries draw a grouped table as bars, so the form absorbs questions about distribution, uncertainty and change. `authority-asserted`, though Weissgerber's prevalence numbers are `evidence-backed`.

**Categories in arrival order.** The [BBC cookbook](../sources/bbc-cookbook.md) treats sorting as a bug fix, not a design decision. `authority-asserted`.

**Truncation to show a small difference.** The [Urban Institute](../sources/urban-institute.md) remedy keeps the mark intact: "consider adjusting the data to show percent change, difference, or some other similar adjustment." `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- "The reader has to read values off this chart, so it is a bar chart. Position instead of arc length: bars beat pies on value extraction in the original experiment and in the crowdsourced replication."
- "The value axis starts at zero because the mark is a filled bar. Truncating one moved readers' size judgments 91% in a controlled test, and marking the truncation did not measurably undo it."
- "These are the individual observations, not a bar of the mean. At this sample size, several very different distributions produce the same bar."
- "The bars have plain flat tops. Rounding or pointing the top of a bar measurably raises comparison error, on this exact chart form."
- "No error bars on the bars. The bar glyph makes values inside it look likelier than values the same distance outside, measured, and symmetric encodings do not do that."

**Defensible, with the label said out loud:**

- "The bars are sorted by value. Practitioner consensus, not a measured result, and the alternative is whatever order the data was in."
- "The illustration sits behind the plot area and does not touch the bars. Whether decoration around a chart helps or hurts is contested; what is not contested is that deforming the bar hurts, and this does not."
- "Zero baseline because the mark is filled, not because the axis is quantitative. Every guide here scopes it that way and none of them tested the rule."

**Commonly repeated and not supported:**

- ~~"Bars beat pies because length is a better channel than angle."~~ Right conclusion, wrong reason (above).
- ~~"Studies show chartjunk hurts comprehension."~~ Only deforming the bar was shown to raise error (above).
- ~~"Embellished charts are remembered better."~~ It did not survive the asynchronous replication.
- ~~"Every quantitative axis must start at zero."~~ The truncation study's authors explicitly refuse this version.

## See also

- [../studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md)
- [../studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md)
- [../studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md)
- [../refutations.md](../refutations.md#chartjunk-and-the-data-ink-ratio-as-settled)
- [magnitude.md](magnitude.md) and [../concepts/channels.md](../concepts/channels.md)
