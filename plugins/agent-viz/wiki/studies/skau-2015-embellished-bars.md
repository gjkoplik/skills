# Skau, Harrison & Kosara 2015: An Evaluation of the Impact of Visual Embellishments in Bar Charts

Drew Skau, Lane Harrison, Robert Kosara. *Computer Graphics Forum* 34(3), EuroVis 2015. DOI [10.1111/cgf.12662](https://doi.org/10.1111/cgf.12662).

## What it is

A crowdsourced experiment testing six common infographic embellishments of the bar itself (rounded tops, triangles, end caps, overlapping triangles, quadratically scaled area, extension below zero) against a plain baseline, on absolute-value and relative-comparison tasks. Almost everything that changes the shape of the bar raises error.

## Status

**`primary-read`.** PDF retrieved from [kosara.net/papers/2015/Skau-EuroVis-2015.pdf](https://kosara.net/papers/2015/Skau-EuroVis-2015.pdf) and re-extracted with `pdftotext -layout`.

Extraction caveat: the text layer loses apostrophes and mangles Table 1's hypothesis-versus-result grid across columns. The numbers below come from Tables 2 and 3 and the running text, which extract cleanly. Table 1's layout was not trusted and its hypothesis-versus-result pairings are not reproduced here.

Retrieval date: **2026-08-23**.

## What it is good for

The precise scope of the anti-embellishment result. It is not "decoration is bad." It is **"do not deform the mark that encodes the value,"** which is a much sharper and much more defensible rule, and it is the one thing in the chartjunk debate with a clean quantitative result behind it.

## What it does not settle

Bar charts only, two tasks only, Mechanical Turk, no memorability measurement at all. It cannot adjudicate the memorability-versus-accuracy tradeoff it names, because it only measured one side of it.

## The finding

> "none of the embellishments tested in this experiment performed better at communication of the data than the baseline standardized chart."

The results split hard by task, which is the interesting part.

**Absolute judgments** (estimate the value of one bar, y-axis present). Only the quadratically scaled bars were significantly worse at the corrected threshold. Rounded tops and triangles came in below it.

| Embellishment | Mean MLAE | SD | p vs. baseline |
|---|---|---|---|
| baseline | 1.41 | 1.85 | n/a |
| capped | 1.41 | 1.68 | 0.50 |
| extended below zero | 1.45 | 1.68 | not significant |
| overlapping triangles | 1.64 | 1.76 | not significant |
| rounded | 1.67 | 1.77 | 0.009 |
| triangle | 1.70 | 1.68 | 0.012 |
| quadratic | 1.70 | 1.78 | significant |

Note that rounded (0.009) and triangle (0.012) both sit just above the corrected α = 0.0083, so they count as non-significant here by a hair. The paper's summary of this task is that "only quadratic bars performed significantly worse than the baseline."

**Relative comparisons** (estimate one bar as a percentage of another, no y-axis, to force comparison rather than reading off the scale). Everything except extension below zero got significantly worse.

| Embellishment | Mean MLAE | SD | p vs. baseline |
|---|---|---|---|
| baseline | 1.43 | 1.85 | n/a |
| extended below zero | 1.59 | 1.66 | 0.097 |
| capped | 1.70 | 1.68 | 0.0013 |
| overlapping triangles | 1.82 | 1.76 | < 0.001 |
| triangle | 1.85 | 1.68 | < 0.001 |
| rounded | 1.86 | 1.77 | < 0.001 |
| quadratic | 2.33 | 1.78 | < 0.001 |

> "All adaptations except the extended embellishment performed significantly worse than the baseline on relative judgements. Even small changes, for example the rounded bar, produced a significantly higher error rate."

## The mechanism they propose, which is the reusable part

The capped bar (a T-shape, wider at the top than the body) performed *equally well as, and with slightly lower variance than*, the baseline on absolute judgments, while every embellishment that softens or points the top performed worse:

> "This result suggests that users indeed rely on strong lines at the ends of bars to mentally extend the bar end to the value axis, especially when considering the comparatively poor performance of the embellishments that distort the top of the bar (rounded caps, triangles, etc.)"

The strong horizontal terminator is not decoration. It is the affordance that lets a reader project the bar's end onto the axis. That is the same class of finding as [Gillan & Richman](gillan-richman-1994-data-ink.md)'s result that removing the axis line hurts response time: certain non-data marks are doing orientation work.

## Method

Amazon Mechanical Turk. Seven chart types (six embellishments plus baseline) crossed with two question types, giving 35 absolute and 56 relative judgments per participant. Block order and the first embellishment shown were both rotated per participant to control learning effects. The relative-comparison charts omitted the y-axis so participants could not answer by reading values off the scale.

The stimuli are **abstractions** of embellishments found in the wild on Visual.ly, simplified for the study rather than lifted whole. That is a deliberate methodological choice, isolating the shape change from color, typography and imagery. It also means the study does not test any real infographic.

Error was the midmean of log-absolute error (MLAE), with 95% confidence intervals by bootstrapping, following Cleveland & McGill and Heer & Bostock. Errors were non-normally distributed, so comparisons used six Mann-Whitney-Wilcoxon tests against baseline with a Bonferroni correction, giving **α = 0.0083**.

## Sample size and population

100 participants recruited, paid US $2.00. Three HITs were rejected and re-run because over a quarter of their answers were off by more than 30%, so 103 people took part and 100 were paid. Six further participants were removed as outliers for average error exceeding 172%; maximum error among the remaining 94 was 45%. Average completion time was 19 minutes 11 seconds.

## Their own advice, stated as advice

> "It is advisable to stay away from creating triangular bar charts. Triangular charts that overlap and that have quadratically changing areas are especially worth avoiding."

> "these results suggest that it is inadvisable to scale chart elements on two axes simultaneously. This is in line with common wisdom."

> "End caps with a strong horizontal top are not advisable for tasks that involve comparing bars, but are fine (and perhaps better) for absolute judgements."

> "Bars that have a portion extending below the zero point on the value axis seem to be fine to use, assuming the portion that extends is a visibly different color from the value portion of the bar."

Two of those are conditional on task, which is why quoting this paper as a flat "embellishment raises error" distorts it.

## Limits the authors state themselves

They position the result explicitly as a qualification of the memorability literature rather than a refutation of it:

> "The results of this study qualify findings by Borkin and Borgo suggesting that memorability can be aided by embellishment. Changes to charts that affect the primary chart elements can reduce the communication accuracy of the chart. Increasing the memorability of a chart is certainly a worthwhile pursuit, however it must be balanced with the need to communicate information accurately in the first place."

"Balanced with" is a value judgment, not a measurement. This study did not measure memorability, so it cannot say where the balance sits. It establishes one side's cost.

They also name the scope directly in the conclusion: the contribution is "a basis for exploring the impact of low-level design elements in graphical perception," which is a first-step framing rather than a settled-question one.

## What this result does not license

"Studies show chartjunk hurts comprehension." It shows that *deforming the bar* hurts numeric estimation, mostly on comparison tasks, under Bonferroni correction, on abstracted stimuli. It says nothing about imagery placed around a correctly drawn chart, and it did not measure recall.

## Why this does not actually contradict Bateman

Both results can be true at once, and reading them as a contradiction is the most common error in this corner of the literature.

[Bateman et al.](bateman-2010-useful-junk.md) tested Nigel Holmes cartoon imagery placed *around and behind* a correctly drawn chart, and measured verbal description and recall. Skau et al. tested deformations *of the bar itself*, and measured numeric estimation error. The bars in a Holmes chart still have flat tops. Under the mechanism Skau proposes, they would be expected to read accurately, which is what Bateman found.

The synthesis: **decoration around the marks is contested, deformation of the marks is not.** That is a finer-grained statement than [refutations.md](../refutations.md)'s "strip decoration, keep orientation," and compatible with it.

## Links

- Study code and data: [github.com/dwskau/chart-embellishment](https://github.com/dwskau/chart-embellishment)
- [bateman-2010-useful-junk.md](bateman-2010-useful-junk.md)
- [gillan-richman-1994-data-ink.md](gillan-richman-1994-data-ink.md)
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md), cited by this paper. The other result about the bar glyph carrying unintended perceptual meaning.
- [refutations.md](../refutations.md), "Chartjunk and the data-ink ratio as settled"
- [inventory.md](../inventory.md), topics 67 and 88
