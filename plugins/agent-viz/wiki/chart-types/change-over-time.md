---
type: index
---

# Change over time

One or more quantities measured repeatedly along an ordered axis, almost always time, drawn so that the shape of the change is what the reader takes away.

## Is time the question, or just a column you happen to have?

Almost every dataset has a timestamp. Very few questions are about it. Three tests, and a form in this group needs all three.

**Would the answer survive deleting the middle?** "How much did it grow" and "which is bigger now" are answered by two numbers and a subtraction. Draw the path only when the path is the answer: when the series accelerates, reverses, plateaus, spikes, or has a season in it. If you cannot name the feature you want the reader to see, you are drawing a shape and hoping.

**Does the space between two adjacent points mean anything?** A connecting mark asserts that the values in between lie along it. That is a claim, and it is false when x is a set of unordered categories, when successive measurements are not comparable, or when the gap is missing data rather than a straight run. [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) measured the sharp end of this: methods that remove information "even lead to incorrect responses if missing values break the visual continuity of a visualization."

**Is the message robust to the window?** If extending the axis by a year flips the conclusion, the conclusion belongs to the window. The FT builds this into the category definition itself: "Choosing the correct time period is important to provide suitable context for the reader" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). `authority-asserted`.

If a test fails, you are in the wrong group:

| The reader's actual question | Go to |
|---|---|
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md), zero baseline |
| Which is biggest, and in what order? | [Ranking](ranking.md). A sorted bar chart |
| Did the order change between two dates? | **Stay here**, and see [slope-chart.md](slope-chart.md), which is also a ranking chart |
| How did the mix shift? | [Part-to-whole](part-to-whole.md). [Stacked bar](stacked-bar.md), or lines of shares |
| How do these two variables relate, with time incidental? | [Correlation](correlation.md). A [scatterplot](scatterplot.md) |
| How far is each period from target? | [Deviation](deviation.md) |
| How spread out are the values within each period? | [Distribution](distribution.md). A box or violin per period |
| Is this rising, falling, cycling, or breaking? | **Stay here** |

## What this group costs

**It is the one group that spends the best channel on the value and still cannot claim the evidence.** Both axes are position along a common scale, which is the most accurately read channel measured ([channels.md](../concepts/channels.md)). That should be the end of the argument, and it is not, for two reasons.

First, **the task is wrong for the literature.** The graphical-perception record measures reading a value off a mark and reporting it as a number. Nobody reads a line chart that way. They read slope, shape, crossing points and turning points, and the source authors say plainly that their ordering does not speak to those tasks ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). The one study aimed squarely at slope judgment, [Talbot, Gerth & Hanrahan (2012)](../studies/talbot-2012-slope-ratio.md), concludes that "the theory of aspect ratio selection is not as simple as it once seemed."

Second, and this is the real price, **the trend is partly a design output.** Aspect ratio and axis range both change the apparent rate of change without changing a single number, and neither is visible to the reader as a choice. Both have been measured:

- [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) manipulated the aspect ratio of a line chart and moved mean response on a 5-point "how much bigger" scale from 1.39 to 3.19, an increase of 129.5%, **with the true values printed on the chart.**
- [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) found truncation drove perceived severity up, F(2, 76) = 89, p < 0.0001, and that being a line chart rather than a bar chart did not help: "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)."

Every other group in this wiki asks you to pick a mark. This one also asks you to pick two free parameters that decide what the mark says, and you own both.

## Choosing a form

| Form | Carries the change as | Reach for it when |
|---|---|---|
| [Line chart](line-chart.md) | Endpoint position, read as slope and shape | Many ordered points, and the connection between them is real |
| [Area chart](area-chart.md) | The same, plus filled area | One series or a stacked total, where the amount under the curve is a real quantity. The fill brings the zero baseline back into scope |
| [Stacked area chart](stacked-area-chart.md) | Band thickness, plus position for the total and the bottom band | A few components on a continuous axis, where the total matters as much as the parts |
| [Streamgraph](streamgraph.md) | Band thickness, against a baseline computed from the data | Many components, and the reading wanted is the silhouette of the total rather than any value |
| [Slope chart](slope-chart.md) | Two endpoint positions on a shared scale | Exactly two periods, many categories, and direction plus reordering is the story |
| [Stacked bar](stacked-bar.md) | Segment length | A few discrete periods where composition and total both matter |
| [Connected scatterplot](connected-scatterplot.md) | Position in a two-variable plane, with time only in the path order | Two quantities move together and the joint trajectory is the message. Time comes off the axis entirely |
| [Bump chart](bump-chart.md) | Position on a rank axis, with the value discarded | Several periods, few items, and who overtook whom is the question rather than by how much |
| [Sparkline](sparkline.md) | Shape alone, with the axes removed by design | The graphic belongs inside a sentence or a table row, and no value has to be read off it |
| Column over time *(no page yet)* | Length from zero | Few discrete periods, counted quantities, and the value rather than the trend is the point |

Fan charts and horizon graphs both belong to this group and neither has a page. No study in this corpus tests either of them, and none tests the bump chart, the stacked area chart, the streamgraph or the sparkline either.

Three constraints that follow from the evidence rather than from taste:

- **Pick the aspect ratio deliberately, and do not reach for a rule to justify it.** The library default is a choice you did not make. The received fix, banking to 45 degrees, is scope-limited rather than general; see the contested section of [line-chart.md](line-chart.md#what-is-contested).
- **Truncating the y-axis is a rhetorical decision on every mark in this group, filled or not.** The proportional-ink argument releases lines and dots. The measured exaggeration effect does not.
- **Draw missing values as missing.** Highlighting beat downplaying beat removal on perceived data quality, and zero-filling was the worst imputation tested (Song & Szafir).

## Justifying the choice

**Defensible, evidence-backed:**

- "This axis is truncated and the subtitle says so. Truncation inflates perceived effect size, measured, and it does that on line charts as much as on bars, so I did not treat the absence of a fill as an exemption."
- "The gap in 2019 is drawn as a gap. Repairing a break in continuity silently is the one thing in this literature that produced outright wrong answers rather than just lower confidence."
- "The axis is linear. Log-log comprehension measured 56% against 93% for linear-linear among professional ecologists, 69% of them PhDs, so an expert audience is not the escape hatch" ([Menge et al. 2018](../studies/menge-2018-log-scales.md); the figures come from the publisher's own abstract, the main text is unread).

**Defensible, with the label said out loud:**

- "I chose a flatter, wider aspect ratio than the default." Talbot et al.'s model selects flatter and wider ratios than the banking algorithms do, and they never showed that readers do better on the resulting plots. A lead, not a rule.
- "Everything is gray except the one series in question." Universal practitioner advice with no controlled experiment under it ([refutations.md](../refutations.md)).
- "Five series became five small multiples." Schwabish's own name for the guideline is "Avoid the Spaghetti Chart" ([schwabish.md](../sources/schwabish.md)). `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"Bank the slopes to 45 degrees."~~ Talbot et al.: "we find that, in general, slope ratio errors are not minimized around 45°." Cleveland's model fits inside the moderate range he tested and fails to extrapolate. The accurate sentence keeps the scope.
- ~~"Line charts are exempt from the truncation critique, because there is no bar to cut off."~~ Two different rules get merged here. Proportional ink is scoped by mark and genuinely releases an unfilled line. The exaggeration effect is not scoped by mark and was measured on lines.
- ~~"An axis-break glyph makes the truncation honest."~~ The two static designs tested produced no measurable reduction. Note the care the source takes: at F(2, 60) = 3.1 and n = 31 this is a knife-edge failure to reject, not a demonstrated null, so "placebo" overstates it.
- ~~"A log scale is fine, my audience is technical."~~ Menge et al. found the gap did not close for PhDs, professors, or people who report being comfortable with logarithms.

## The failure mode this group invites

**Presenting a trend as a property of the data when it is partly a property of the drawing.** Nothing in the numbers changes when you stretch the plot, crop the axis, or start the series a year later, and all three change what the reader concludes. This is the group where a figure can be entirely accurate and still wrong.

A usable check: state the conclusion out loud, then redraw at a different aspect ratio and a different axis range. If the sentence stops being true, the sentence was about your choices.

## Types in this index

- [line-chart.md](line-chart.md)
- [area-chart.md](area-chart.md)
- [stacked-area-chart.md](stacked-area-chart.md), which is also a part-to-whole form and keeps only the total and the bottom band on a fixed baseline
- [streamgraph.md](streamgraph.md), the same stack with the baseline computed from the data, so nothing on it is a fixed-scale reading
- [sparkline.md](sparkline.md), a line chart with the guides removed on purpose, so nothing on it is a value
- [slope-chart.md](slope-chart.md), which is also a ranking chart
- [bump-chart.md](bump-chart.md), which is primarily a ranking chart and puts the rank on the axis instead of the value
- [ridgeline-plot.md](ridgeline-plot.md), for the common case where the stacked variable is time, and which is primarily a distribution chart
- [dumbbell-plot.md](dumbbell-plot.md), for the case where the two values are two dates, and which is primarily a ranking chart
- [stacked-bar.md](stacked-bar.md), which is here for repeated composition and is primarily a part-to-whole form
- [connected-scatterplot.md](connected-scatterplot.md), which is primarily a correlation chart and takes time off the axis

## See also

- [../concepts/channels.md](../concepts/channels.md) — and specifically why the accuracy ordering says so little about trend reading
- [../refutations.md](../refutations.md) — banking, truncation remedies, and log scales all have entries
- [README.md](README.md) — the page template and the inheritance rule
