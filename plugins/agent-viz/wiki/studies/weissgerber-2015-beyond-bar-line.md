---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Weissgerber, Milic, Winham & Garovic 2015: Beyond Bar and Line Graphs

Tracey L. Weissgerber, Natasa M. Milic, Stacey J. Winham, Vesna D. Garovic. *Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm.* PLoS Biology 13(4):e1002128, April 2015. DOI [10.1371/journal.pbio.1002128](https://doi.org/10.1371/journal.pbio.1002128).

A Perspective built on a systematic review of **703 research articles** in top-quartile physiology journals. Bar graphs of the mean are nearly everywhere and distribution plots nearly nowhere, at sample sizes too small for the summary to be defensible.

**What it is good for.** A prevalence number for mean-and-error-bar figures, and a case for showing the data grounded in measured sample sizes.

**What it does not settle.** What readers conclude from either figure type. Nobody was tested; that is [Correll & Gleicher](correll-gleicher-2014-error-bars-harmful.md)'s territory. The scope is physiology, one quarter of 2014.

**How this was read.** PDF from the PLoS printable-article endpoint, extracted with `pdftotext -layout`. Open access under CC-BY. The text layer renders `±` as a replacement character, so the quotes below avoid passages that depend on it.

## The finding

| Figure type | Articles including at least one |
|---|---|
| Bar graph | 85.6% |
| Line graph / point-and-error-bar plot | 61.3% |
| Univariate scatterplot | 13.4% |
| Histogram | 8.0% |
| Box plot | 5.3% |

Of papers using bar graphs, 77.6% showed mean with SE and 15.3% mean with SD.

The smallest group in a figure had a median size of 4 (IQR 3 to 6), the largest a median of 10 (IQR 6 to 15). In 75% of papers the smallest group had two to six members. 78.1% of studies ran only parametric analyses, 13.6% both kinds, 3.8% only nonparametric. More than half of those running nonparametric analyses still presented means.

> "Bar graphs are designed for categorical variables; yet they are commonly used to present continuous data in laboratory research, animal studies, and human studies with small sample sizes."

> "many different data distributions can lead to the same bar or line graph. The full data may suggest different conclusions from the summary statistics."

1. **Many distributions map to the same graph.** Fig 1 shows four datasets whose means and SEs fall within 0.5 units of one bar graph: symmetric, outlier-driven, possibly bimodal, and n = 3.
2. **Bar graphs of paired data misstate the design.** They "erroneously suggest that the groups being compared are independent and provide no information about whether changes are consistent across individuals." Fig 2 shows three paired datasets with means and SEs within 0.3 units and completely different individual changes, from all subjects moving together to a responder/nonresponder split.
3. **Mean plus SE or SD invites an unearned normality assumption**, which small samples with common outliers cannot support.

## SE versus SD as a visual choice

> "Showing the SE rather than the SD magnifies the apparent visual differences between groups. This effect is exacerbated when the groups being compared have different sample sizes, which is common in physiology and in other disciplines."

Since SE = SD / √n, equal SEs with unequal n mean unequal SDs, and SE also "obscures any effect of unequal sample size." The bar choice does rhetorical work.

> "bar and line graphs are 'visual tables' that transform the reader from an active participant into a passive consumer of statistical information. Without the opportunity for independent appraisal, the reader must rely on the authors' statistical analyses and interpretation of the data."

## Method

All full-length original research articles published 1 January to 31 March 2014 in the top 25% of physiology journals by 2012 impact factor, n = 703, excluding reviews, editorials, perspectives, commentaries, letters and short communications. Figure types, sample sizes and statistical procedures were abstracted. Journal-level detail, including American Physiological Society affiliation and bar-graph use, is in the supplement.

## Recommendations

**1. More complete presentation of data.** For small datasets, show the full data. The authors shipped free Excel templates (paired, independent, independent with jitter) and GraphPad PRISM instructions, treating the tooling gap as a cause.

> "Univariate scatterplots are the best choice for showing the distribution of the data in these small samples, as boxplots and histograms would be difficult to interpret."

**2. Specific journal policies.**

> "Nonspecific policies stating that figures are preferred to tables whenever possible do not effectively promote the use of figures that show the distribution of continuous data."

**3. Training.** Basic-science statistics courses are often taught by people who work with very large datasets, to students who will work with n = 4.

## Limits the authors state themselves

> "The journals that we examined publish research conducted by investigators in many fields; therefore, it is likely that investigators in other disciplines follow similar practices."

That inference rests on prior documentation of the same overuse in psychology and medicine, not on their data.

> "The question of whether investigators should report the SE or the SD has been extensively debated by biomedical scientists and statisticians."

They decline to adjudicate, holding that showing the full distribution makes the debate moot. They also note that ARRIVE guidelines produced "few improvements in scientific reporting among animal studies two years after" publication despite top-journal endorsement, which bears on their own policy recommendation.

## What this result does not license

- **Not "Box plots instead of bar charts."** Box plots go in the same "only meaningful when there are enough data to summarize" bucket as bar and line graphs. At these sample sizes the paper prefers univariate scatterplots.
- **Not a ranked list of chart types.** The rule is that sample size gates the choice of summary.

## Links

- [cumming-2007-error-bars.md](cumming-2007-error-bars.md): rule 4 reaches recommendation 1 from expert guidance
- [matejka-2017-datasaurus.md](matejka-2017-datasaurus.md): a constructed "many distributions, one summary." This paper's Fig 1 does it with realistic data and real p-values.
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md)
- [inventory.md](../inventory.md), topics 49 and 50 (show the distribution, not only the summary)
