---
type: chart-type
relationships: [distribution]
aliases: [Box plot, Box-and-whisker plot]
---

# Box plots

One variable reduced to five numbers per group: a box spanning the upper and lower fourths with a line at the median, whiskers to the most extreme observations inside a fence, and anything past the fence drawn individually.

## When to reach for it, and when not

The form is defined for several groups on one axis, each large enough to summarize, where the question is location and spread rather than shape. Unlike a [violin](violin-plot.md), it has no tuning parameter to adjust until the picture agrees with the analyst ([john-tukey.md](../people/john-tukey.md)).

| The question | Alternative |
|---|---|
| n is 3 to 6 per group | A strip plot or univariate scatterplot of the observations |
| Is this bimodal? | [Violin](violin-plot.md), or a [histogram](histogram.md) per group. Five numbers cannot express a second mode |
| How many observations are in each group? | n in the caption, or a form that draws every point |
| Is this group significantly different from that one? | Not this form. The box is descriptive unless redefined, with the redefinition declared |
| What is the exact first quartile? | A table. Implementations disagree about what the box ends are |
| One group, and the shape is the whole point | [Histogram](histogram.md) or an ECDF |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, usually one grouping variable |
| Transform | Median; upper and lower fourths; fences at 1.5 times the inter-fourth range; whiskers to the most extreme observation inside the fence; observations beyond it kept as points |
| Geometry | Rectangle, center line, two whisker segments, individual points for the far observations |
| Scale | Value to position along a common scale. The box's cross-axis width encodes nothing by default |
| Coordinates | Cartesian, one axis categorical |
| Guides | The value axis, the quantile definition and whisker rule used, and n per group |

Unlike a mean and SD, every statistic drawn is an observation or a robust summary. The box ends are hinges, or fourths, which differ from quartiles under most quantile definitions. Nine quantile types circulate, some tools use fixed quantiles for the whiskers, and some use multipliers other than 1.5. The secondary account relied on here measures the fences from the *median*; every implementation known here uses the *hinges*. The primary was not reached, so neither is vouched as Tukey's.

## Channels

Every statistic is position along a common scale ([channels.md](../concepts/channels.md)), with the step from chart to channel conjecture. The ranking covers value extraction, not comparing medians and spreads ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What it is measurably good at

**No containment bias.** [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found a significant interaction between an outcome's position and the encoding, F(2,2) = 21.3, p < 0.0001: on a bar chart, outcomes below the mean, inside the bar, were rated significantly likelier than outcomes equally far above. Not so for the box plot or the other symmetric encodings. Adherence to the expected strategy was 87.4% of trials with the box plot against 83.2% with bars. Their box plot was an uncertainty encoding, not Tukey's: whiskers at the 95% t-confidence interval, box at 50%, center line at the mean. On confidence it tied bars (M = 4.86), below the two distribution-detail encodings.

**The box helps.** Stock & Behrens (1991) found Tufte's box-less *midgap* variant "substantially less accurate than the original." The result is reported through Wickham & Stryjewski's history; Stock & Behrens was not reached ([refutations.md](../refutations.md)).

## What it is measurably bad at

**Multimodality.** Matejka & Fitzmaurice built six visibly different distributions with the same quartiles, median and 1.5-IQR whiskers, hence one box plot ([matejka-2017-datasaurus.md](../studies/matejka-2017-datasaurus.md)). That is a construction, silent on what readers conclude.

**Small samples.** [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) class box plots with bar and line graphs as "only meaningful when there are enough data to summarize," and at their measured sample sizes (median minimum group size 4) recommend univariate scatterplots. Box plots appeared in 5.3% of 703 articles, the rarest of the five figure types counted.

**Group size.** Eight observations and eight hundred draw alike. McGill, Tukey & Larsen's variable-width and notched variants from 1978 patch this and are rarely used. `authority-asserted`.

## What is contested

Whether the box plot fixes the bar chart with error bars:

- **For:** Correll & Gleicher measured the containment bias away.
- **Against:** Weissgerber et al. decline, since at their sample sizes no summary form is defensible.

Both turn on sample size. At four observations per group, the option left is drawing the four.

## The failure mode it invites

**A box over too few points, with n unstated.** The mark looks the same at n = 4 and n = 4,000, and only the caption can say which.

**Reading the box as inferential.** Non-overlapping boxes are not a significance test. [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) found 31.5% of the 314 published authors who answered the CI and SE tasks applying the just-touching heuristic to error bars, wrong for both bar types, a transfer to boxes rather than a measurement.

**Treating the drawing as settled.** The most-used statistical graphic invented in the twentieth century is `authority-asserted`. Its author ran no perceptual experiments, and the form predates him ([john-tukey.md](../people/john-tukey.md)).

## Justifying the choice

**Defensible, evidence-backed:**

- "I used a box plot rather than a bar with error bars. The bar glyph made outcomes inside the bar look likelier than equidistant outcomes above it, measured, and the box plot did not show that bias."
- "I kept the box. The box-less variant proposed to raise the data-ink ratio was tested against the original and came out substantially less accurate." (Reported result; the study itself was not reached.)

**Defensible, with the label said out loud:**

- "Box plot rather than violin, because a box plot has no bandwidth to choose. That is a design property of the form, not a measured advantage."
- "n is in the caption for each group, because the mark cannot carry it and there is no way to judge two boxes without it."
- "The caption states the quantile definition and the whisker rule, because implementations disagree about both."

**Commonly repeated, and not supported:**

- ~~"Box plots show the quartiles."~~ They show hinges, which match quartiles only under some definitions.
- ~~"Use a box plot instead of a bar chart."~~ Sound with enough data per group. The review usually cited prefers plotting the observations at its sample sizes.
- ~~"A box plot shows the distribution."~~ It shows five numbers.
- ~~"Boxes that do not overlap indicate a significant difference."~~ Wrong for descriptive intervals. The error-bar version failed among published authors.

## See also

- [distribution.md](distribution.md): the group, and the sample-size gate
- [violin-plot.md](violin-plot.md): shape, plus a bandwidth
- [../people/john-tukey.md](../people/john-tukey.md): where the statistics came from
- [../studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md): the box-plot-shaped glyph under test
