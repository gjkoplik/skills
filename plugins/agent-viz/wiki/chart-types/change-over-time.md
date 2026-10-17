---
type: index
---

# Change over time

One or more quantities measured repeatedly along an ordered axis, almost always time, drawn so that the shape of the change is what the reader takes away.

## Is time the question, or just a column in the data?

Almost every dataset has a timestamp, and few questions are about it. A form here needs to pass three tests.

**Would the answer survive deleting the middle?** "How much did it grow" is two numbers and a subtraction. The path is the answer only when the series accelerates, reverses, plateaus, spikes or has a season. Without such a feature, the drawing carries a shape and no claim.

**Does the space between adjacent points mean anything?** A connecting mark asserts that the values in between lie along it. That is false for unordered categories, for successive measurements that are not comparable, and across missing data. [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) found that methods that remove information "even lead to incorrect responses if missing values break the visual continuity of a visualization."

**Is the message robust to the window?** If extending the axis by a year flips the conclusion, the conclusion belongs to the window. The FT writes this into the category definition: "Choosing the correct time period is important to provide suitable context for the reader" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). `authority-asserted`.

| The reader's actual question | Group |
|---|---|
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md), zero baseline |
| Which is biggest, and in what order? | [Ranking](ranking.md). A sorted bar chart |
| Did the order change between two dates? | **This group**. A [slope chart](slope-chart.md), also a ranking chart |
| How did the mix shift? | [Part-to-whole](part-to-whole.md). [Stacked bar](stacked-bar.md), or lines of shares |
| How do these two variables relate, with time incidental? | [Correlation](correlation.md). A [scatterplot](scatterplot.md) |
| How far is each period from target? | [Deviation](deviation.md) |
| How spread out are the values within each period? | [Distribution](distribution.md). A box or violin per period |
| Is this rising, falling, cycling, or breaking? | **This group** |

## What this group costs

Both axes are position along a common scale, the most accurately read channel ([channels.md](../concepts/channels.md)). The group still cannot claim that evidence.

**The task differs.** The graphical-perception record measures reading a value off a mark. Line charts are read for slope, shape, crossings and turning points, which the source authors place outside their ordering ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). The one study aimed at slope judgment, [Talbot, Gerth & Hanrahan (2012)](../studies/talbot-2012-slope-ratio.md), concludes that "the theory of aspect ratio selection is not as simple as it once seemed."

**The trend is partly a design output.** Aspect ratio and axis range change the apparent rate without changing a number, and the reader cannot see either choice. Both effects are measured:

- [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) changed a line chart's aspect ratio and moved mean response on a 5-point "how much bigger" scale from 1.39 to 3.19, up 129.5%, with the true values printed on the chart.
- [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) found truncation raised perceived severity, F(2, 76) = 89, p < 0.0001, and lines fared no better than bars: "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)."

## Choosing a form

| Form | Carries the change as | Where it applies |
|---|---|---|
| [Line chart](line-chart.md) | Endpoint position, read as slope and shape | Many ordered points, with a real connection between them |
| [Area chart](area-chart.md) | The same, plus filled area | One series or total whose area under the curve is a real quantity. The fill brings back the zero baseline |
| [Stacked area chart](stacked-area-chart.md) | Band thickness, plus position for the total and the bottom band | A few components, the total as important as the parts |
| [Streamgraph](streamgraph.md) | Band thickness, against a baseline computed from the data | Many components, read as a silhouette rather than as values |
| [Slope chart](slope-chart.md) | Two endpoint positions on a shared scale | Exactly two periods, many categories, direction and reordering as the story |
| [Stacked bar](stacked-bar.md) | Segment length | A few discrete periods where composition and total both matter |
| [Connected scatterplot](connected-scatterplot.md) | Position in a two-variable plane, with time only in the path order | Two quantities whose joint trajectory is the message. Time leaves the axis |
| [Bump chart](bump-chart.md) | Position on a rank axis, with the value discarded | Several periods, few items, who overtook whom rather than by how much |
| [Sparkline](sparkline.md) | Shape alone, with the axes removed by design | Inside a sentence or a table row, with no value to read off |
| [Fan chart](fan-chart.md) | A projected path with nested probability bands | A forecast beyond the last observation, where the width of the plausible range at each horizon is the message |
| Column over time *(no page yet)* | Length from zero | Few discrete periods of counted quantities, the value mattering more than the trend |

No study here tests the fan chart, the bump chart, the stacked area chart, the streamgraph or the sparkline.

- **Aspect ratio** is a free choice that no rule in this corpus settles, and a library default is an unmade choice. Banking to 45 degrees is scope-limited ([line-chart.md](line-chart.md#what-is-measured)).
- **Missing values** are drawn as missing. Highlighting beat downplaying beat removal on perceived data quality, and zero-filling was the worst imputation tested (Song & Szafir).

## Justifying the choice

**Defensible, evidence-backed:**

- "This axis is truncated and the subtitle says so. Truncation inflates perceived effect size, measured, and it does that on line charts as much as on bars, so I did not treat the absence of a fill as an exemption."
- "The gap in 2019 is drawn as a gap. Repairing a break in continuity silently is the one thing in this literature that produced outright wrong answers rather than just lower confidence."
- "The axis is linear. Log-log comprehension measured 56% against 93% for linear-linear among professional ecologists, 69% of them PhDs, so an expert audience is not the escape hatch" ([Menge et al. 2018](../studies/menge-2018-log-scales.md); figures from the publisher's abstract, main text unread).

**Defensible, with the label said out loud:**

- "I chose a flatter, wider aspect ratio than the default." Talbot et al.'s model picks flatter, wider ratios than banking does, but they never showed readers do better on them. A lead, not a rule.
- "Everything is gray except the one series in question." Universal practitioner advice with no controlled experiment under it ([refutations.md](../refutations.md)).
- "Five series became five small multiples." Schwabish calls the guideline "Avoid the Spaghetti Chart" ([schwabish.md](../sources/schwabish.md)). `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"Bank the slopes to 45 degrees."~~ Talbot et al.: "we find that, in general, slope ratio errors are not minimized around 45°." Cleveland's model fits inside the moderate range he tested and fails to extrapolate.
- ~~"Line charts are exempt from the truncation critique, because there is no bar to cut off."~~ Two rules merged. Proportional ink is scoped by mark and releases an unfilled line. The exaggeration effect is not, and was measured on lines.
- ~~"An axis-break glyph makes the truncation honest."~~ The two static designs tested produced no measurable reduction. At F(2, 60) = 3.1 and n = 31 that is a narrow failure to reject, not a demonstrated null, so "placebo" overstates it.
- ~~"A log scale is fine, my audience is technical."~~ Menge et al. found the gap did not close for PhDs, professors, or people who report being comfortable with logarithms.

## The failure mode this group invites

**A trend presented as a property of the data when it is partly a property of the drawing.** Stretching the plot, cropping the axis or starting a year later changes no number and changes the conclusion. Redrawing at a different aspect ratio and axis range is the check. A conclusion that stops being true was about the drawing.

## Types in this index

- [line-chart.md](line-chart.md)
- [area-chart.md](area-chart.md)
- [stacked-area-chart.md](stacked-area-chart.md): also part-to-whole
- [streamgraph.md](streamgraph.md)
- [sparkline.md](sparkline.md)
- [slope-chart.md](slope-chart.md): also ranking
- [bump-chart.md](bump-chart.md): primarily ranking
- [ridgeline-plot.md](ridgeline-plot.md): primarily distribution, here when the stacked variable is time
- [dumbbell-plot.md](dumbbell-plot.md): primarily ranking, here when the two values are two dates
- [stacked-bar.md](stacked-bar.md): primarily part-to-whole, here for repeated composition
- [connected-scatterplot.md](connected-scatterplot.md): primarily correlation
- [horizon-graph.md](horizon-graph.md)
- [fan-chart.md](fan-chart.md): primarily uncertainty, here because the FT files it under this group
- [small-multiples.md](small-multiples.md): one panel per series at shared scales

## See also

- [../concepts/channels.md](../concepts/channels.md): why the accuracy ordering says little about trend reading
- [../refutations.md](../refutations.md): banking, truncation remedies and log scales
- [README.md](README.md): the page template and the inheritance rule
