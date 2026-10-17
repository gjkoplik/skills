---
type: chart-type
relationships: [uncertainty]
aliases: [Bar chart with error bars, Confidence interval plot, Dot-and-whisker plot, Error bar chart, Interval plot, Mean with error bars, Point-range plot]
---

# Interval plots

One point estimate per category on a shared quantitative axis, with a line through it spanning an interval whose meaning the figure states.

It is also called an error bar chart, dot-and-whisker plot, point-range plot or confidence interval plot, and none of those names is defined by a source here. [Wilke](../sources/wilke-fundamentals.md) catalogs "error bars" in chapter 16, and in chapter 9, on showing many distributions at once, labels "mean with error bars" "bad". The bar with error bars, the variant [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) tested, is covered here too.

## When to reach for it, and when not

The form is defined for several estimates on one scale, each with an inferential interval, where the question is how precisely each is known or whether two differ beyond the noise. It is the common form for that job. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) found a line graph or point-and-error-bar plot in 61.3% of 703 physiology articles and a bar graph in 85.6%. Correll & Gleicher report the bar with error bars as the modal encoding in visualization publications.

| The question | Alternative |
|---|---|
| How spread out is the sample, and what shape? | [Distribution](distribution.md). An SD or percentile interval answers that question, not this one |
| n is 3 or 4 per group | The observations: a [dot strip plot](dot-strip-plot.md) or [beeswarm](beeswarm-plot.md) |
| How likely is this outcome, for a general audience? | [Gradient plot](gradient-plot.md) or [violin](violin-plot.md), the symmetric continuous forms that were tested |
| Did each subject change between conditions? | One line per subject. Cumming et al.'s rule 8 says CIs and SE bars are irrelevant to within-group comparisons |
| What are the exact bounds? | A table |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation with a grouping variable, or one row per category carrying an estimate and two bounds computed elsewhere |
| Transform | A statistic per group (mean, median, model coefficient) and an interval: SD, SE, a parametric or bootstrap CI, or a percentile interval, with its multiplier or level. For a bootstrap, also the resample count and seed |
| Geometry | A point at the estimate and a segment spanning the interval, often capped. The bar variant draws a bar from zero to the estimate in place of the point |
| Scale | The estimate and both bounds to position on one shared quantitative axis |
| Coordinates | Cartesian, one axis categorical |
| Guides | The quantitative axis, and a legend or caption naming the interval (which statistic, which level) and n |

The interval's meaning is chosen in the transform and changes nothing in the geometry, so only the guides carry it. In [seaborn](../sources/seaborn.md) the size argument even changes units with the method: "For parametric error bars, it is a scalar factor that is multiplied by the statistic defining the error... For nonparametric error bars, it is a percentile width." `("se", 2)` is two standard errors, and `("pi", 50)` is the interquartile range.

A [dumbbell plot](dumbbell-plot.md) draws the same two endpoints, but they are two measurements rather than the bounds of one; [aliases.md](aliases.md) records "range plot" colliding across the two.

## Channels

The estimate is position along a common scale, the most accurately read channel in [channels.md](../concepts/channels.md). The bounds are positions on the same scale. Judging whether two intervals overlap is a comparison of the facing endpoints. The interval's length has no common baseline, as on the dumbbell. The step from mark to channel is conjecture in the source literature.

The bar variant puts the estimate on a length from zero and fills it. The fill is what Correll & Gleicher's containment metaphor attaches to.

## What is measured

Labeled means with error bars, read by experts, are misread. [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) asked 473 published authors to drag one mean until two means with error bars looked "just statistically significantly different." Only 22% landed within a factor of two of the target p-value. Respondents did not distinguish CIs from SE bars: the correct answers sit 160 units apart, and the groups' averages differed by 48. 31.5% used the just-touching rule, wrong for both bar types. A third got a repeated-measures display the bars cannot answer, and 11% showed any sign of noticing. `evidence-backed`, on one task with a 15.2% response rate.

The bar with error bars biases inference against symmetric forms. Correll & Gleicher, three crowdsourced experiments, 240 participants:

- With bars, outcomes below the mean, inside the bar, were rated likelier than outcomes the same distance above it, F(2,2) = 21.3, p < 0.0001. No symmetric encoding showed this.
- Adherence to the expected strategy was 83.2% of trials with bars, against 87.4% box, 88.5% gradient and 89.2% violin.
- In two-sample judgments, bar readers were more confident than the others, more so on stimuli that fail a t-test at α = .05.

`evidence-backed`, on low-stakes predictions with no real decisions. "The practical effect of these differences is difficult to determine."

The dot with whiskers itself is untested. The nearest stimulus is Correll & Gleicher's modified box plot (mean line, 50% CI box, 95% CI whiskers), which is symmetric with hard edges and showed no within-the-bar bias. It transfers only as far as symmetry is the mechanism. The authors also name **binary interpretation**, "values are within the margins of error, or they are not," and prescribe forms "visually symmetric and visually continuous." A dot with whiskers is the first and not the second. `absence of evidence`.

The authors' aside that "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots" concerns bars without intervals and a different task.

## The failure mode it invites

**Unlabeled meaning.** Any of four intervals, read as whichever the reader assumes. Cumming et al.'s rule 1 asks the legend to say which ([cumming-2007-error-bars.md](../studies/cumming-2007-error-bars.md)), `authority-asserted`. The choice does rhetorical work. Weissgerber et al.:

> "Showing the SE rather than the SD magnifies the apparent visual differences between groups. This effect is exacerbated when the groups being compared have different sample sizes, which is common in physiology and in other disciplines."

**Two whiskers meaning two things.** Panels or series drawing different interval types in one figure. Belia et al. found the error flips direction with the bar type, CI readers too strict and SE readers too lax. No study here tests a mixed figure. `absence of evidence`.

**A symmetric interval crossing a bound.** seaborn: "In some cases, standard deviation error bars may extend to 'impossible' values." Percentile and bootstrap intervals cannot leave the data's range. A check that drawn bounds stay inside the variable's domain catches it ([inventory.md](../inventory.md) topic 51), `authority-asserted`.

**An unseeded bootstrap.** "Bootstrapping involves randomness, and the error bars will appear slightly different each time you run the code that creates them." Without a seed the figure does not reproduce.

**Replicates counted as n.** Cumming et al.'s rule 3. The bars come out tight and answer nothing about the effect.

## Justifying the choice

**Defensible, evidence-backed:**

- "The legend names the interval and gives n. The four interval types draw identically, and published authors misread even labeled CI and SE bars, measured."
- "Points rather than bars under the estimates. With bars, outcomes inside the bar were judged likelier than equidistant ones above it, measured with 240 crowdsourced readers."

**Defensible, with the label said out loud:**

- "A dot with whiskers rather than a gradient or violin, because the bounds must be readable. It is symmetric, the property the bias turned on, but it was not one of the forms tested."
- "Percentile intervals, because the quantity cannot go below zero and an SD interval would cross it. That is library documentation, not a study."
- "n counts independent experiments, not replicates, per Cumming et al.'s rule 3."

**Commonly repeated, and not supported:**

- ~~"Non-overlapping error bars mean a significant difference."~~ SE bars that just touch give p ≈ .16 (Belia et al.).
- ~~"Overlapping CIs mean no significant difference."~~ Just-touching 95% CIs on independent means give p ≈ .006.
- ~~"Error bars are a formatting detail."~~ Correll & Gleicher: "the encoding of mean and error significantly changes how viewers make decisions about uncertain data."
- ~~"Error bars should never be used."~~ The result is comparative, from a lab, on low-stakes prediction.

## See also

- [uncertainty.md](uncertainty.md): the group, and the descriptive-versus-inferential test
- [gradient-plot.md](gradient-plot.md): the symmetric continuous alternative
- [../studies/cumming-2007-error-bars.md](../studies/cumming-2007-error-bars.md): the eight rules, verbatim
