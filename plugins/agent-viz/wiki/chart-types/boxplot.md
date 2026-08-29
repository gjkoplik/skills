---
type: chart-type
relationships: [distribution]
aliases: [Box plot, Box-and-whisker plot]
---

# Box plots

One variable reduced to five numbers per group: a box spanning the upper and lower fourths with a line at the median, whiskers reaching the most extreme observations inside a fence, and anything past the fence drawn individually.

## When to reach for it, and when not

**The form applies where** several groups have to be compared on one axis, each group has enough observations for a summary to mean anything, and the question is about location and spread rather than about shape. The form's offer is that one very simple mark repeats across a strip, so ten groups cost the same reading effort as two.

Its second offer is that **it has no tuning parameter**. Nothing about a box plot can be adjusted until the picture agrees with the analyst, which is a deliberate design property and the main difference between it and a [violin](violin-plot.md) ([john-tukey.md](../people/john-tukey.md)).

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| n is 3 to 6 per group | A strip plot or univariate scatterplot of the observations |
| Is this bimodal? | [Violin](violin-plot.md), or a [histogram](histogram.md) per group. Five numbers cannot express a second mode |
| How many observations are in each group? | The box plot does not say. n stated in the caption, or a form that draws every point |
| Is this group significantly different from that one? | The box is a descriptive interval, not an inferential one, unless it is redefined and the redefinition declared |
| What is the exact first quartile? | A table. Implementations disagree about what the box ends even are |
| One group, and the shape is the whole point | [Histogram](histogram.md) or an ECDF. The comparison strip is what the form charges for |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, usually one grouping variable |
| Transform | Median; upper and lower fourths; fences at 1.5 times the inter-fourth range; whiskers to the most extreme observation inside the fence; observations beyond it kept as points |
| Geometry | Rectangle, center line, two whisker segments, individual points for the far observations |
| Scale | Value to position along a common scale. The box's cross-axis width encodes nothing by default |
| Coordinates | Cartesian, one axis categorical |
| Guides | The value axis, plus a statement of which quantile definition and which whisker rule were used, plus n per group |

**Every drawn statistic sits at a real observation or at a robust summary of them**, which is what separates this from a mean and an SD: nothing on the plot is at a coordinate the data does not support ([john-tukey.md](../people/john-tukey.md)).

**The box ends are hinges, or fourths, and those are not identical to quartiles under most quantile definitions.** Implementations differ further: nine quantile types are in circulation, some tools substitute fixed quantiles for the whisker extremes, and multipliers other than 1.5 are in use. This is definitional rather than a claim, and it is the reason "what is the first quartile" is a question for a table. One detail is unresolved: the secondary account this wiki relies on places the fences 1.5 inter-fourth ranges from the *median*, while every implementation known here measures from the *hinges*. Those are different plots. The primary was not reached, so neither phrasing is vouched as Tukey's own.

## Channels

Every statistic is read as position along a common scale, shared across groups. That inherits from [channels.md](../concepts/channels.md) and is not restated here as a native finding.

The inheritance buys less than it looks like it does. The reader's task is comparing medians and spreads across a strip, not extracting a number from one box, and the ranking's authors scope their result to value extraction ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What it is measurably good at

Two results, and they are the only measurements in this source set that decompose a box-plot-shaped glyph rather than a channel.

**It does not produce the bar chart's containment bias.** [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found a significant interaction between an outcome's position and the encoding, F(2,2) = 21.3, p < 0.0001: with a bar chart, outcomes below the mean and so inside the bar were rated significantly likelier than outcomes the same distance above it. That effect was not significant for the box plot or for either of the other symmetric encodings. Adherence to the expected strategy was 87.4% of trials with the box plot against 83.2% with bars.

**Deleting the box makes it worse.** Tufte proposed a box-less *midgap* variant to raise the data-ink ratio, and Stock & Behrens (1991) found it "substantially less accurate than the original." It is a case of a specific reduction tested against the thing it reduced, and losing. It is reported rather than primary: the result reaches this wiki through Wickham & Stryjewski's history, and Stock & Behrens was not reached ([refutations.md](../refutations.md)).

**Two scope notes.** Correll & Gleicher's box plot was modified for their task: whiskers at the 95% t-confidence interval, box at a 50% t-confidence interval, center line at the mean rather than the median. It is a box-plot-shaped uncertainty encoding, not Tukey's box plot. And on confidence, rather than accuracy, their box plot did not separate from bars at all: both sat at M = 4.86, below the two encodings carrying distribution detail.

## What it is measurably bad at

**Multimodality, completely.** Matejka & Fitzmaurice generated six visibly different distributions sharing a first quartile, median, third quartile and 1.5-IQR whisker positions, so all six draw the identical box plot ([matejka-2017-datasaurus.md](../studies/matejka-2017-datasaurus.md)). That is a construction, not an experiment, and construction is the right kind of proof for this particular claim: it establishes that the five numbers do not determine the shape. It establishes nothing about what readers conclude.

**Small samples.** [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) put box plots in the same bucket as bar and line graphs, "only meaningful when there are enough data to summarize," and at the sample sizes they measured (median minimum group size 4) they recommend univariate scatterplots instead. Their prevalence count found box plots in 5.3% of 703 articles, the rarest of the five figure types they counted.

**Group size, which it does not show.** There is no way to tell whether a box covers eight observations or eight hundred, so no way to judge whether a difference between two boxes means anything. McGill & Larsen's variable-width and notched variants from 1978 exist to patch this, and are almost never used. `authority-asserted`.

## What is contested

**Whether the box plot is the fix for the bar chart with error bars.** It is the most common recommendation in the neighborhood, and the record splits on it:

- **For:** Correll & Gleicher measured the containment bias away. On their inferential tasks the box plot behaved like the other symmetric encodings and unlike the bar.
- **Against:** Weissgerber et al. explicitly decline to recommend it. Their objection is not about the glyph, it is that at the sample sizes in question no summary form is defensible, box plots included.

What survives both: **the argument is about sample size, not about a ranked list of chart types.** With enough data per group the box plot is a defensible replacement for a bar and error bars. With four observations per group nothing in this family is, and the remaining option is drawing the four.

## The failure mode it invites

**Drawing a box over too few points, and never saying how few.** The mark looks the same at n = 4 and n = 4,000, the reader has no way to tell them apart, and the form gives no place to put n except the caption.

**Reading the box or the whiskers as inferential.** They are descriptive by construction. Non-overlapping boxes are not a significance test, and the just-touching heuristic that [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) measured on error bars, applied by 31.5% of 473 published authors and wrong for both bar types, is the same mistake wearing a different mark. That study tested error bars rather than box plots, so this is a transfer, not a measurement.

**Treating the drawing as standard and therefore settled.** The box plot is the most-used statistical graphic invented in the twentieth century and it entered the world entirely `authority-asserted`; its author ran no perceptual experiments, and the graphic form itself predates him ([john-tukey.md](../people/john-tukey.md)).

## Justifying the choice

**Defensible, evidence-backed:**

- "I used a box plot rather than a bar with error bars. The bar glyph made outcomes inside the bar look likelier than equidistant outcomes above it, measured, and the box plot did not show that bias."
- "I kept the box. The box-less variant proposed to raise the data-ink ratio was tested against the original and came out substantially less accurate." (Reported result; the study itself was not reached.)

**Defensible, with the label said out loud:**

- "Box plot rather than violin, because a box plot has no bandwidth to choose. That is a design property of the form, not a measured advantage."
- "n is in the caption for each group, because the mark cannot carry it and there is no way to judge two boxes without it."
- "The caption states the quantile definition and the whisker rule, because implementations disagree about both."

**Commonly repeated, and not supported:**

- ~~"Box plots show the quartiles."~~ They show hinges, which coincide with quartiles only under some quantile definitions, and tools disagree. This is a misdescription of what the chart is, not a disputed finding.
- ~~"Use a box plot instead of a bar chart."~~ Sound when there are enough data per group, and explicitly not the recommendation of the review usually cited for it, which prefers plotting the observations at the sample sizes it measured.
- ~~"A box plot shows the distribution."~~ It shows five numbers. Six visibly different distributions produce one identical box plot, by construction.
- ~~"Boxes that do not overlap indicate a significant difference."~~ No version of this is right for descriptive intervals, and the analogous heuristic on error bars was measured and found badly wrong among published authors.

## See also

- [distribution.md](distribution.md) — the group, and the sample-size gate that decides most of this
- [violin-plot.md](violin-plot.md) — the same strip, with shape instead of five numbers, and a knob
- [../people/john-tukey.md](../people/john-tukey.md) — where the statistics came from, and what the form cannot do
- [../studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md) — the one experiment that put a box-plot-shaped glyph under test
