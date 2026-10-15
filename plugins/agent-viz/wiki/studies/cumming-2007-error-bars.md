---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Cumming, Fidler & Vaux 2007: Error bars in experimental biology

Geoff Cumming, Fiona Fidler, David L. Vaux. *The Journal of Cell Biology* 177(1):7-11, April 2007. DOI [10.1083/jcb.200611141](https://doi.org/10.1083/jcb.200611141).

A tutorial on what the four common error bars mean, with **eight numbered rules** for using them.

**What it is good for.** What a figure owes the reader about its error bars (the bar type and n, in the legend), and what counts as n. The replicates-versus-independent-experiments distinction is how a figure can state its sample size and still be meaningless.

**What it does not settle.** Anything experimental. It is expert guidance from the group behind [Belia et al. 2005](belia-2005-ci-misconceptions.md), so the rules are authority-asserted with a reason ([evidence-class](../concepts/evidence-class.md)). Encoding choices are [Correll & Gleicher](correll-gleicher-2014-error-bars-harmful.md)'s territory, and showing the distribution instead is [Weissgerber](weissgerber-2015-beyond-bar-line.md)'s.

**How this was read.** Full text from the Europe PMC REST API (`/PMC2064100/fullTextXML`), the publisher-deposited JATS, CC-BY-NC-SA after six months. The PMC PDF endpoint returns a "Preparing to download" HTML interstitial instead of the PDF.

## The eight rules, verbatim

> **Rule 1:** when showing error bars, always describe in the figure legends what they are.

> **Rule 2:** the value of n (i.e., the sample size, or the number of independently performed experiments) must be stated in the figure legend.

> **Rule 3:** error bars and statistics should only be shown for independently repeated experiments, and never for replicates. If a "representative" experiment is shown, it should not have error bars or P values, because in such an experiment, n = 1.

> **Rule 4:** because experimental biologists are usually trying to compare experimental results with controls, it is usually appropriate to show inferential error bars, such as SE or CI, rather than SD. However, if n is very small (for example n = 3), rather than showing error bars and statistics, it is better to simply plot the individual data points.

> **Rule 5:** 95% CIs capture μ on 95% of occasions, so you can be 95% confident your interval includes μ. SE bars can be doubled in width to get the approximate 95% CI, provided n is 10 or more. If n = 3, SE bars must be multiplied by 4 to get the approximate 95% CI.

> **Rule 6:** when n = 3, and double the SE bars don't overlap, P < 0.05, and if double the SE bars just touch, P is close to 0.05. If n is 10 or more, a gap of SE indicates P ≈ 0.05 and a gap of 2 SE indicates P ≈ 0.01.

> **Rule 7:** with 95% CIs and n = 3, overlap of one full arm indicates P ≈ 0.05, and overlap of half an arm indicates P ≈ 0.01.

> **Rule 8:** in the case of repeated measurements on the same group (e.g., of animals, individuals, cultures, or reactions), CIs or SE bars are irrelevant to comparisons within the same group.

Rules 1 and 2 can be checked mechanically. Rules 5 through 7 are eyeball approximations for reading a figure, not for drawing one.

## Why rule 1 exists

Range and SD are **descriptive** (spread of the data). SE and CI are **inferential** (precision of the mean). All four are drawn identically.

> "Because error bars can be descriptive or inferential, and could be any of the bars listed in Table I or even something else, they are meaningless, or misleading, if the figure legend does not state what kind they are."

SD does not shrink with n; SE and CI do. A tight unlabeled bar might mean "the data cluster" or "we ran it a lot of times," with no way to tell.

## Replicates versus independent experiments

> "It is essential that n (the number of independent results) is carefully distinguished from the number of replicates, which refers to repetition of measurement on one individual in a single condition, or multiple measurements of the same or identical samples."

One mutant and one wild-type mouse tail, each measured 20 times, give means, SDs and SEs but n = 1 per genotype. Replicate wells from one stock culture measure pipetting fidelity, not the effect.

> "If an experiment involves triplicate cultures, and is repeated four independent times, then n = 4, not 3 or 12."

> "Whenever you see a figure with very small error bars ... you should ask yourself whether the very small variation implied by the error bars is due to analysis of replicates rather than independent samples. If so, the bars are useless for making the inference you are considering."

Outside biology, a benchmark run 20 times on one machine has n = 1 machine. Twenty raters scoring one document have n = 1 document.

## The n = 3 problem

> "We illustrate and give rules for n = 3 not because we recommend using such a small n, but because researchers currently often use such small n values and it is necessary to be able to interpret their papers. It is highly desirable to use larger n, to achieve narrower inferential error bars and more precise estimates of true population values."

Rule 4's fallback, plotting the points at very small n, is what [Weissgerber](weissgerber-2015-beyond-bar-line.md) recommends from a systematic review eight years later.

## Method and sample

None. A tutorial with seven worked figures, published as a Rockefeller University Press feature, supported by citation: mainly [Belia et al. 2005](belia-2005-ci-misconceptions.md) (its reference 1), Cumming, Williams & Fidler 2004, and Schenker & Gentleman 2001.

## Limits the authors state themselves

> "remember that error bars and other statistics can only be a guide: you also need to use your biological understanding to appreciate the meaning of the numbers shown in any figure."

## What this result does not license

- **Not a measured effect.** The reader evidence is in Belia et al.
- **Not overlap rules for repeated measures.** Rules 6 and 7 assume independent means and behave differently at n = 3 than at n ≥ 10. Rule 8 says the bars do not answer within-group questions.

## Links

- Open text: [pmc.ncbi.nlm.nih.gov/articles/PMC2064100](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/)
- [belia-2005-ci-misconceptions.md](belia-2005-ci-misconceptions.md): researchers misread these bars even when labeled
- [weissgerber-2015-beyond-bar-line.md](weissgerber-2015-beyond-bar-line.md): how often figures show a summary and an SE where the points or an SD would serve, measured across 703 articles
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md): the encoding, rather than the labeling, of mean and error
- [inventory.md](../inventory.md), topics 49 (error-bar semantics must be stated) and 50 (show the distribution, not only the summary)
