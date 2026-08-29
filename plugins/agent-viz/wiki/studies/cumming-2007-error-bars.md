---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Cumming, Fidler & Vaux 2007: Error bars in experimental biology

Geoff Cumming, Fiona Fidler, David L. Vaux. *The Journal of Cell Biology* 177(1):7-11, April 2007. DOI [10.1083/jcb.200611141](https://doi.org/10.1083/jcb.200611141).

A five-page tutorial that lays out what the four common error bars mean and gives **eight numbered rules** for using them. It is the closest thing the statistical-reporting literature has to a checkable style guide for figures.

**How this was read.** Full text retrieved from the Europe PMC REST API (`/PMC2064100/fullTextXML`), which serves the publisher-deposited JATS. The article is CC-BY-NC-SA after its first six months. The PMC PDF endpoint returns a "Preparing to download" HTML interstitial rather than the PDF, so the XML route is the one that works.

## What it is good for

Two questions. First, *what does a figure owe the reader about its error bars?* This paper answers with mechanizable rules: the bar type is named in the legend and n is stated. Second, *what counts as n?* The replicates-versus-independent-experiments distinction is the part a naive reading of "state your sample size" misses entirely, and it is the reason a figure can satisfy the letter of the rule and still be meaningless.

## What it does not settle

Nothing here is an experiment. It is expert guidance, written by the same group whose experimental evidence is [Belia et al. 2005](belia-2005-ci-misconceptions.md). The rules are authority-asserted-with-a-reason rather than measured effects; see [evidence-class](../concepts/evidence-class.md).

It also does not touch chart *design*. There is no claim about bar-plus-error-bar versus gradient or violin encodings, which is [Correll & Gleicher](correll-gleicher-2014-error-bars-harmful.md)'s territory, and no claim about showing the distribution instead, which is [Weissgerber](weissgerber-2015-beyond-bar-line.md)'s.

## The eight rules, verbatim

They are reproduced in full rather than paraphrased.

> **Rule 1:** when showing error bars, always describe in the figure legends what they are.

> **Rule 2:** the value of n (i.e., the sample size, or the number of independently performed experiments) must be stated in the figure legend.

> **Rule 3:** error bars and statistics should only be shown for independently repeated experiments, and never for replicates. If a "representative" experiment is shown, it should not have error bars or P values, because in such an experiment, n = 1.

> **Rule 4:** because experimental biologists are usually trying to compare experimental results with controls, it is usually appropriate to show inferential error bars, such as SE or CI, rather than SD. However, if n is very small (for example n = 3), rather than showing error bars and statistics, it is better to simply plot the individual data points.

> **Rule 5:** 95% CIs capture μ on 95% of occasions, so you can be 95% confident your interval includes μ. SE bars can be doubled in width to get the approximate 95% CI, provided n is 10 or more. If n = 3, SE bars must be multiplied by 4 to get the approximate 95% CI.

> **Rule 6:** when n = 3, and double the SE bars don't overlap, P < 0.05, and if double the SE bars just touch, P is close to 0.05. If n is 10 or more, a gap of SE indicates P ≈ 0.05 and a gap of 2 SE indicates P ≈ 0.01.

> **Rule 7:** with 95% CIs and n = 3, overlap of one full arm indicates P ≈ 0.05, and overlap of half an arm indicates P ≈ 0.01.

> **Rule 8:** in the case of repeated measurements on the same group (e.g., of animals, individuals, cultures, or reactions), CIs or SE bars are irrelevant to comparisons within the same group.

Rules 1 and 2 are the mechanizable pair. Rules 5 through 7 are eyeball approximations for reading an existing figure rather than rules for drawing one.

## Why rule 1 exists

The four bar types are drawn identically and mean different things. Range and SD are **descriptive** (how spread out the data are). SE and CI are **inferential** (how well the mean is pinned down). The paper's framing:

> "Because error bars can be descriptive or inferential, and could be any of the bars listed in Table I or even something else, they are meaningless, or misleading, if the figure legend does not state what kind they are."

The practical asymmetry: SD does not shrink as n grows, SE and CI both do. So an unlabeled bar that looks tight might mean "the data cluster" or might mean "we ran it a lot of times," and the reader cannot tell which.

## Replicates versus independent experiments

This is rule 3, and it is the rule that survives being ported out of cell biology into any other domain.

> "It is essential that n (the number of independent results) is carefully distinguished from the number of replicates, which refers to repetition of measurement on one individual in a single condition, or multiple measurements of the same or identical samples."

Their example: one mutant mouse's tail measured 20 times and one wild-type mouse's tail measured 20 times yield means, SDs and SEs, but n = 1 per genotype and the comparison is unavailable no matter how many measurements were taken. The pipetting example has the same shape. Replicate wells from one stock culture measure pipetting fidelity, not reproducibility of the biological effect.

> "If an experiment involves triplicate cultures, and is repeated four independent times, then n = 4, not 3 or 12."

And the diagnostic they hand the reader:

> "Whenever you see a figure with very small error bars ... you should ask yourself whether the very small variation implied by the error bars is due to analysis of replicates rather than independent samples. If so, the bars are useless for making the inference you are considering."

The generalization outside biology: repeated measurement of one thing is not a sample of things. A benchmark run 20 times on one machine has n = 1 machine. Twenty raters scoring one document have n = 1 document. The rule is about which population a claim is entitled to cover.

## The n = 3 problem, stated against their own advice

They give rules for n = 3 while disclaiming them:

> "We illustrate and give rules for n = 3 not because we recommend using such a small n, but because researchers currently often use such small n values and it is necessary to be able to interpret their papers. It is highly desirable to use larger n, to achieve narrower inferential error bars and more precise estimates of true population values."

Rule 4's escape hatch, that at very small n the points are plotted instead of the bars, is the same recommendation [Weissgerber](weissgerber-2015-beyond-bar-line.md) arrives at from a systematic review eight years later.

## Method and sample

There is no experiment and no sample. It is a tutorial with seven worked figures, published as a Rockefeller University Press feature. Its evidentiary support is by citation, principally to [Belia et al. 2005](belia-2005-ci-misconceptions.md) (its reference 1), Cumming, Williams & Fidler 2004, and Schenker & Gentleman 2001.

## Limits the authors state themselves

They close by scoping the whole apparatus:

> "remember that error bars and other statistics can only be a guide: you also need to use your biological understanding to appreciate the meaning of the numbers shown in any figure."

The overlap rules in 6 and 7 carry assumptions the article states but does not belabor: independent means, and approximations that behave differently at n = 3 than at n ≥ 10. Rule 8 is the explicit carve-out for correlated measurements, where the drawn bars simply do not answer the within-group question.

## Links

- Open text: [pmc.ncbi.nlm.nih.gov/articles/PMC2064100](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/)
- [belia-2005-ci-misconceptions.md](belia-2005-ci-misconceptions.md), the experiment showing that researchers do not read these bars correctly even when labeled
- [weissgerber-2015-beyond-bar-line.md](weissgerber-2015-beyond-bar-line.md), how often rules 1 through 4 are ignored in practice
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md), the encoding rather than the labeling of mean and error
- [inventory.md](../inventory.md), topics 49 (error-bar semantics must be stated) and 50 (show the distribution, not only the summary)
