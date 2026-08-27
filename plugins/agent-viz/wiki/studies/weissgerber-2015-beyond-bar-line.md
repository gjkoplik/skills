---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Weissgerber, Milic, Winham & Garovic 2015: Beyond Bar and Line Graphs

Tracey L. Weissgerber, Natasa M. Milic, Stacey J. Winham, Vesna D. Garovic. *Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm.* PLoS Biology 13(4):e1002128, April 2015. DOI [10.1371/journal.pbio.1002128](https://doi.org/10.1371/journal.pbio.1002128).

A Perspective built on a systematic review of **703 research articles** in the top quartile of physiology journals. It measures which figure types scientists actually use for continuous data, finds bar graphs of the mean nearly everywhere and distribution plots nearly nowhere, and argues that at the sample sizes involved the summary statistic is not defensible.

**How this was read.** PDF retrieved from the PLoS printable-article endpoint and re-extracted with `pdftotext -layout`. Open access under CC-BY. Extraction caveat: `±` renders as a replacement character in the text layer, so quotes below avoid passages that depend on it.

## What it is good for

Two things. First, a **prevalence number** rather than an opinion: how often does published science hide its distribution behind a mean and an error bar? Second, the sample-size argument, which is the sharpest version of "show the data" available, because it is grounded in measured n rather than in taste.

## What it does not settle

It is a review plus an argument, not a reader experiment. Nobody was tested. It establishes that the practice is widespread and gives a principled case against it; it does not measure what readers actually conclude from either figure type. For that, use [Correll & Gleicher](correll-gleicher-2014-error-bars-harmful.md). Its scope is also narrow by design: physiology, one quarter of 2014.

## The finding

**Prevalence, from the 703-article review:**

| Figure type | Articles including at least one |
|---|---|
| Bar graph | 85.6% |
| Line graph / point-and-error-bar plot | 61.3% |
| Univariate scatterplot | 13.4% |
| Histogram | 8.0% |
| Box plot | 5.3% |

Of the papers using bar graphs, 77.6% showed mean with SE against 15.3% showing mean with SD.

**Sample sizes, which is the part that makes the prevalence damning.** The minimum sample size for any group shown in a figure had a median of 4, interquartile range 3 to 6. The maximum sample size for any group had a median of 10, interquartile range 6 to 15. In 75% of papers reviewed, the minimum group size in a figure was between two and six.

**Statistical practice:** 78.1% of studies ran only parametric analyses, 13.6% ran both parametric and nonparametric, 3.8% ran only nonparametric. More than half of the authors who ran nonparametric analyses still presented means.

The argument the numbers support:

> "Bar graphs are designed for categorical variables; yet they are commonly used to present continuous data in laboratory research, animal studies, and human studies with small sample sizes."

> "many different data distributions can lead to the same bar or line graph. The full data may suggest different conclusions from the summary statistics."

Their three named problems are worth keeping distinct, because only the first is the familiar one:

1. **Many distributions map to the same graph.** Their Fig 1 shows four datasets whose means and SEs are all within 0.5 units of the same bar graph: one symmetric, one driven by a single outlier, one possibly bimodal, one with n = 3.
2. **Bar graphs of paired data lie about the design.** They "erroneously suggest that the groups being compared are independent and provide no information about whether changes are consistent across individuals." Their Fig 2 shows three paired datasets with means and SEs differing by less than 0.3 units and completely different patterns of individual change, including one where every subject moves the same way and one that splits into responders and nonresponders.
3. **Mean plus SE or SD invites an unearned normality assumption.** Small samples cannot support it, and outliers are common.

## SE versus SD as a visual choice

The most reusable paragraph in the paper:

> "Showing the SE rather than the SD magnifies the apparent visual differences between groups. This effect is exacerbated when the groups being compared have different sample sizes, which is common in physiology and in other disciplines."

Since SE = SD / √n, two groups with equal SE and unequal n have unequal SD, and SE additionally "obscures any effect of unequal sample size." The choice of bar type does rhetorical work whether or not the author intends it.

And the framing that gives the paper its bite:

> "bar and line graphs are 'visual tables' that transform the reader from an active participant into a passive consumer of statistical information. Without the opportunity for independent appraisal, the reader must rely on the authors' statistical analyses and interpretation of the data."

## Method

All full-length original research articles published between 1 January and 31 March 2014 in the top 25% of physiology journals by 2012 impact factor, n = 703. Reviews, editorials, perspectives, commentaries, letters and short communications were excluded at screening. Reviewers abstracted figure types used for continuous outcome data, plus sample size and statistical analysis procedures. Journal-level detail, including the relationship between American Physiological Society affiliation and bar-graph use, is in the supplementary text rather than in the main article.

## Recommendations

Three, in the paper's own order:

1. **Encourage a more complete presentation of data.** For small datasets, show the full data. "Univariate scatterplots are the best choice for showing the distribution of the data in these small samples, as boxplots and histograms would be difficult to interpret." They shipped free Excel templates for paired data, independent data, and independent data with jitter, plus GraphPad PRISM instructions, because the tooling gap is a real cause of the practice.
2. **Change journal policies, specifically.** "Nonspecific policies stating that figures are preferred to tables whenever possible do not effectively promote the use of figures that show the distribution of continuous data."
3. **Train investigators in data presentation**, with the observation that statistics courses in basic science departments are often taught by people who work with very large datasets, while the students will spend their careers with n = 4.

Recommendation 1 is the same conclusion [Cumming, Fidler & Vaux](cumming-2007-error-bars.md) reach in their rule 4 by a completely different route.

## Limits the authors state themselves

They generalize beyond physiology by inference, and say so as inference:

> "The journals that we examined publish research conducted by investigators in many fields; therefore, it is likely that investigators in other disciplines follow similar practices."

They support that with prior documentation of the same overuse in psychology and medicine rather than with their own data.

On the SD-versus-SE question they explicitly decline to adjudicate: "The question of whether investigators should report the SE or the SD has been extensively debated by biomedical scientists and statisticians." Their position is that showing the full distribution makes the debate moot, which is a sidestep rather than an answer.

They also flag, against their own recommendation's chances, that ARRIVE guidelines produced "few improvements in scientific reporting among animal studies two years after" publication despite top-journal endorsement. Editorial policy is not self-executing.

## What this result does not license

"Box plots instead of bar charts" is not this paper's recommendation. Box plots go in the same "only meaningful when there are enough data to summarize" bucket as bar and line graphs, and at the sample sizes measured here the paper prefers univariate scatterplots. The generalizable rule is about sample size gating the choice of summary, not about a ranked list of chart types.

## Links

- [cumming-2007-error-bars.md](cumming-2007-error-bars.md), whose rule 4 arrives at the same place from expert guidance rather than a review
- [matejka-2017-datasaurus.md](matejka-2017-datasaurus.md), the constructed illustration of "many distributions, one summary." This paper's Fig 1 does the same thing with realistic data and real p-values, which makes it the better citation when you need evidence rather than a demo.
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md)
- [inventory.md](../inventory.md), topics 49 and 50 (show the distribution, not only the summary)
