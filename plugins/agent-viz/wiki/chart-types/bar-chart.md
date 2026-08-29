---
type: chart-type
relationships: [magnitude]
aliases: [Bar chart, Column chart, Coxcomb, Grouped bar chart]
---

# Bar charts

One filled rectangle per category, running from a common baseline, its length encoding the value. The form every other chart in this wiki is measured against, and the only one that was the stimulus in the experiment that produced the measuring stick.

## When to reach for it, and when not

**The form applies where** the reader has to get values off the chart and compare them across a handful of named categories. The value sits on position along a common scale, which is read more accurately than anything else that has been tested ([channels.md](../concepts/channels.md)). Being the default is also its failure mode, below.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). A bar chart asserts nothing about a total |
| What does the distribution look like? | A histogram, or a univariate scatterplot of the raw points. A bar of the mean is compatible with distributions that disagree |
| Are these two group means different? | Not a bar with error bars. The bar glyph biases the judgment; see below |
| How did this move over time? | A line chart. Change over time |
| There are forty categories | [Lollipop chart](lollipop-chart.md), or an aggregated tail. A bar chart's height is set by its row count and cannot be shrunk |
| Where does each item sit relative to a target? | [Deviation](deviation.md). A [diverging bar](diverging-bar-chart.md) off the reference, not off zero |
| The values span orders of magnitude | Not a truncated bar. A log scale with the base stated, or a different mark |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with a magnitude |
| Transform | None, usually. A count, mean or rate computed upstream is a transform, and the chart does not disclose it |
| Geometry | Filled rectangle, one edge on the baseline |
| Scale | Magnitude to length, anchored at zero |
| Coordinates | Cartesian. Vertical and horizontal bars differ only in which axis carries the value |
| Guides | One quantitative axis with its baseline visible, a category axis, and labels |

A **column chart** is this chart with the axes swapped, which is a layout decision rather than a different form. A **grouped bar chart** adds a second categorical variable to the position slot. A **[stacked bar](stacked-bar.md)** adds a cumulative sum to the transform. A **coxcomb**, or polar-area diagram, sets coordinates to polar, with equal angles and the quantity carried by area. The name is a documented misnomer: Nightingale used "coxcomb" for a booklet and never for a diagram, and the transfer to the chart is traceable to Cook's 1914 biography ([florence-nightingale.md](../people/florence-nightingale.md)). A **[lollipop](lollipop-chart.md)** changes the geometry slot alone, from a filled rectangle to a point plus a stem.

## Channels

**Primary: position along a common scale**, read at the bar's end. **Secondary: length**, since the bar's extent is also available.

That mapping is a conjecture in the source, and Cleveland & McGill flag it as one: on bar charts, position is primary "but judgments of area and length probably also play a role." The accuracy claims below are inherited from [channels.md](../concepts/channels.md) rather than measured on this artifact, with two exceptions noted where they occur.

**One piece of direct type-level evidence exists for the mapping.** [Skau, Harrison & Kosara (2015)](../studies/skau-2015-embellished-bars.md) found that a capped bar, one with a strong horizontal terminator wider than the body, matched the plain baseline on absolute judgments with slightly lower variance, while every embellishment that rounded or pointed the top made things worse:

> "This result suggests that users indeed rely on strong lines at the ends of bars to mentally extend the bar end to the value axis, especially when considering the comparatively poor performance of the embellishments that distort the top of the bar (rounded caps, triangles, etc.)"

That is a mechanism for *how* the reader gets to position, offered by the authors as a hypothesis consistent with their data rather than as a tested finding. It is the closest thing this wiki has to a channel decomposition of the bar chart.

## What it is measurably good at

**Reading a value off the mark, against every alternative that has been tested.**

[Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), position-length experiment, on the substitution a stacked or floating bar forces:

> "the average errors for length judgments are 40%-250% larger than those for position judgments"

Their second experiment put a bar chart directly against a pie chart, which makes it one of the few genuinely type-level results in the perception literature rather than a channel result wearing a chart's clothes:

> "In only 3 of the 40 cases was the pie chart more accurate on average than the bar chart."

with an overall error difference of "a factor of 2^.97 = 1.96, and is statistically significant." Replicated on Mechanical Turk by [Heer & Bostock (2010)](../studies/heer-bostock-2010.md), where "position still significantly outperformed length" and both angle and area came in worse than position.

**Ratio comparisons, including against dot plots.** From [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md), a paper otherwise arguing against bars:

> "There are tasks where asymmetric encodings outperform symmetric encodings; for instance, comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots."

Reported as an aside rather than as this paper's experiment, so treat it as evidence-backed and secondhand within the same paper.

## What it is measurably bad at

**Surviving deformation of the bar itself.** Skau et al. tested six embellishments against a plain baseline. On relative comparisons, with the axis removed so readers had to compare bars rather than read the scale, everything except extending the bar below zero got significantly worse:

> "All adaptations except the extended embellishment performed significantly worse than the baseline on relative judgements. Even small changes, for example the rounded bar, produced a significantly higher error rate."

Mean log error ran 1.43 for the baseline, 1.86 for merely rounding the top, and 2.33 for quadratically scaled bars. On absolute judgments, where the axis was present, only the quadratic bars cleared the corrected significance threshold. **The task decides how much this costs.** A flat reading of the paper as "embellishment raises error" drops that split.

**Being truncated.** [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) measured a truncated bar axis against the same data drawn honestly and found responses on a "how much bigger" scale went from a control mean of 1.45 to 2.77, an increase of **91.0%** (Mann-Whitney U = 1144, Z = 3.36, p = 0.0003). Evidence-backed, on a chart where the true values were printed.

**Being fixed afterward with a break glyph.** [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) tested two truncation-marking designs and could not distinguish them from plain truncation on perceived severity, and found "the exaggeration introduced through truncation appears to persist across chart types and chart designs, and even when participants make accurate reports of the numbers they observe." Their own phrasing is hedged and the statistics are knife-edge; [refutations.md](../refutations.md#axis-break-glyphs-as-the-truncation-remedy) carries the reading.

**Carrying an error bar.** Correll & Gleicher named two defects, both measured:

> "**Within-the-bar bias:** the glyph of a bar provides a false metaphor of containment, where values within the bar are seen as likelier than values outside the bar."

In their first experiment, proposed outcomes falling *inside* the bar were rated significantly more likely than ones the same distance above the mean (interaction F(2,2) = 21.3, p < 0.0001), an effect absent from every symmetric encoding they tested. The bias survived moving the proposed outcome out of the chart into text; it lifted only when the margin of error left the chart too, at which point strategy adherence collapsed from 91.6% of trials to 62.2% while confidence went *up*.

**Standing in for a distribution.** [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md): 85.6% of 703 physiology articles used a bar graph, at a median minimum group size of 4, and "many different data distributions can lead to the same bar or line graph." Their Fig 1 shows four datasets, one symmetric, one outlier-driven, one possibly bimodal, one at n = 3, whose bars are within half a unit of each other. Prevalence and construction, not a reader experiment.

## What is contested

**Embellishment around the bar.** This is the live one, and the two papers usually set against each other are not actually opposed.

[Bateman et al. (2010)](../studies/bateman-2010-useful-junk.md) used Nigel Holmes cartoon charts, where imagery sits *around and behind* a correctly drawn bar, and measured verbal description and recall: accuracy "no worse than for plain charts," recall better after two to three weeks, and a significant *advantage* for the embellished charts on the value-message score (p = .003). Skau et al. deformed *the bar itself* and measured numeric estimation error, which went up.

**The distinction that reconciles them is where the paint lands.** A Holmes bar still has a flat top and a straight side. Under Skau's own proposed mechanism, readers project from that terminator onto the axis, so a Holmes bar should read accurately, which is exactly what Bateman found. Skau's paper says so in its own words, positioning the result as a qualification rather than a refutation: embellishment that touches "the primary chart elements can reduce the communication accuracy of the chart."

So: **decoration around the mark is contested; deformation of the mark is not.** Two things follow that are usually dropped from citations in both directions:

- Bateman's headline long-term recall result **does not replicate cleanly.** A four-way replication (Syeda et al. 2023) found no significant differences on any of the four long-term questions in the asynchronous study, while synchronous replications matched. What is robust across all five studies is *preference*; what replicates best is description accuracy holding up. Bateman's directional tests were one-tailed at α = .05 with no correction for the dozen-plus comparisons run.
- Bateman's stimuli were built by a professional who **encoded the message into the imagery**, which the authors concede: the monster's teeth trace the trend and the title says "monstrous." That may make the result about integrated illustration rather than about embellishment as a category.

**The mechanism behind "bars beat pies."** The finding is secure and replicated. The reason everyone gives for it is not. "Length beats angle" was never tested by Cleveland & McGill, whose two experiments they say may not be compared, and Heer & Bostock ran it head to head and reported "the results do not support this" ([the one joint where the folk ranking breaks](../concepts/channels.md#the-one-joint-where-the-folk-ranking-breaks)). The confusion is compounded here, because a bar chart's primary reading is **position**, not length. Position against angle *is* measured, and it is the comparison that supports the finding.

**The zero baseline.** Every style guide in this corpus scopes it by mark and none ran an experiment on the rule itself. Vega-Lite disagrees, defaulting to zero on every quantitative positional scale regardless of mark ([vega-lite.md](../sources/vega-lite.md)). What *is* measured is the harm from truncating a bar specifically, and the failure of a break glyph to undo it. `authority-asserted` for the rule; evidence-backed for the consequence.

## The failure mode it invites

**Being drawn because nobody decided anything.** The bar chart is the shape a plotting library produces from a grouped table, so it absorbs questions belonging to distribution, uncertainty and change over time. Weissgerber's prevalence numbers are that failure measured in one field. `authority-asserted` as a rule; the prevalence itself is evidence-backed.

**Leaving the categories in the order they arrived.** Alphabetical order is the default in the absence of a choice, which the BBC cookbook treats as a bug fix rather than a design decision ([bbc-cookbook.md](../sources/bbc-cookbook.md)). `authority-asserted`.

**Truncating to make a small difference visible.** Urban names a remedy that leaves the mark intact: "consider adjusting the data to show percent change, difference, or some other similar adjustment" ([urban-institute.md](../sources/urban-institute.md)).

## Justifying the choice

**Defensible, evidence-backed:**

- "The reader has to read values off this chart, so it is a bar chart. Position instead of arc length: bars beat pies on value extraction in the original experiment and in the crowdsourced replication."
- "The value axis starts at zero because the mark is a filled bar. Truncating one moved readers' size judgments 91% in a controlled test, and marking the truncation did not measurably undo it."
- "These are the individual observations, not a bar of the mean. At this sample size, several very different distributions produce the same bar."
- "The bars have plain flat tops. Rounding or pointing the top of a bar measurably raises comparison error, on this exact chart form."
- "No error bars on the bars. The bar glyph makes values inside it look likelier than values the same distance outside, measured, and symmetric encodings do not do that."

**Defensible, with the label said out loud:**

- "The bars are sorted by value. Practitioner consensus, not a measured result, and the alternative is whatever order the data was in."
- "The illustration sits behind the plot area and does not touch the bars. Whether decoration around a chart helps or hurts is genuinely contested; what is not contested is that deforming the bar hurts, and this does not."
- "Zero baseline because the mark is filled, not because the axis is quantitative. Every guide here scopes it that way and none of them tested the rule."

**Commonly repeated and not supported:**

- ~~"Bars beat pies because length is a better channel than angle."~~ The conclusion is right and the reason is not. The one head-to-head test of length against angle did not find it, and Cleveland & McGill's two experiments cannot be compared to each other. A bar's primary channel is position anyway.
- ~~"Studies show chartjunk hurts comprehension."~~ What is shown is that deforming the bar raises numeric estimation error, mostly on comparison tasks. Imagery placed around a correctly drawn bar did not hurt description accuracy, and was preferred.
- ~~"Embellished charts are remembered better."~~ The long-term recall advantage is the least stable part of Bateman, and did not survive the asynchronous replication.
- ~~"Every quantitative axis must start at zero."~~ Scoped by mark. The authors of the truncation study explicitly refuse this version of the rule.

## See also

- [../studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) — the bar-versus-pie experiment and the ties it could not break
- [../studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md) — deformation, task by task, and the terminator mechanism
- [../studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) — the other half of the embellishment question
- [../refutations.md](../refutations.md#chartjunk-and-the-data-ink-ratio-as-settled) — the reconciliation, stated once for the whole wiki
- [magnitude.md](magnitude.md) and [../concepts/channels.md](../concepts/channels.md)
