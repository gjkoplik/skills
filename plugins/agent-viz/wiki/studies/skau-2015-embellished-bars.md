---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Skau, Harrison & Kosara 2015: An Evaluation of the Impact of Visual Embellishments in Bar Charts

Drew Skau, Lane Harrison, Robert Kosara. *Computer Graphics Forum* 34(3), EuroVis 2015. DOI [10.1111/cgf.12662](https://doi.org/10.1111/cgf.12662).

A crowdsourced experiment testing six infographic embellishments of the bar itself (rounded tops, triangles, end caps, overlapping triangles, quadratically scaled area, extension below zero) against a plain baseline, on absolute-value and relative-comparison tasks. Almost everything that changes the shape of the bar raises error.

**What it is good for.** The scope of the anti-embellishment result. It is not "decoration is bad." It is **"do not deform the mark that encodes the value,"** the one claim in the chartjunk debate with a clean quantitative result behind it.

**What it does not settle.** Bar charts only, two tasks only, Mechanical Turk, and no memorability measure. It names a memorability-versus-accuracy tradeoff but measured only the accuracy side.

**How this was read.** PDF retrieved from [kosara.net/papers/2015/Skau-EuroVis-2015.pdf](https://kosara.net/papers/2015/Skau-EuroVis-2015.pdf) and re-extracted with `pdftotext -layout`. The text layer loses apostrophes and mangles Table 1's hypothesis-versus-result grid across columns. Numbers here come from Tables 2 and 3 and the running text, which extract cleanly. Both tables were also checked against renders of pages 7 and 8. Table 1's pairings are not reproduced.

## The finding

> "none of the embellishments tested in this experiment performed better at communication of the data than the baseline standardized chart."

**Absolute judgments** (estimate one bar's value, y-axis present). Rounded (0.009) and triangle (0.012) sit just above the corrected α = 0.0083, so they count as non-significant. The SD column is the paper's own: Tables 2 and 3 print the same SD for every condition except extended (1.68 against 1.66), and the running text repeats those values.

| Embellishment | Mean MLAE | SD | p vs. baseline |
|---|---|---|---|
| baseline | 1.41 | 1.85 | n/a |
| capped | 1.41 | 1.68 | 0.50 |
| extended below zero | 1.45 | 1.68 | 0.562 |
| overlapping triangles | 1.64 | 1.76 | 0.048 |
| rounded | 1.67 | 1.77 | 0.009 |
| triangle | 1.70 | 1.68 | 0.012 |
| quadratic | 1.70 | 1.78 | 0.007 |

The paper sums up this task as "only quadratic bars performed significantly worse than the baseline."

**Relative comparisons** (estimate one bar as a percentage of another, with no y-axis to read).

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

## The proposed mechanism

The capped bar (a T-shape, wider at the top) matched the baseline on absolute judgments with slightly lower variance. Every embellishment that softens or points the top did worse:

> "This result suggests that users indeed rely on strong lines at the ends of bars to mentally extend the bar end to the value axis, especially when considering the comparatively poor performance of the embellishments that distort the top of the bar (rounded caps, triangles, etc.)"

A strong horizontal terminator lets a reader project the bar's end onto the axis. [Gillan & Richman](gillan-richman-1994-data-ink.md) found the same class of effect, where removing the axis line hurt response time: some non-data marks do orientation work.

## Method

Mechanical Turk. Seven chart types (six embellishments plus baseline) crossed with two question types, giving 35 absolute and 56 relative judgments per participant. Block order and the first embellishment were rotated per participant to control learning effects. The stimuli abstract embellishments found on Visual.ly, isolating the shape change from color, typography and imagery, so no real infographic was tested.

Error was the midmean of log-absolute error (MLAE), with 95% confidence intervals by bootstrapping, following Cleveland & McGill and Heer & Bostock. Errors were non-normal, so six Mann-Whitney-Wilcoxon tests against baseline with a Bonferroni correction set **α = 0.0083**.

## Sample size and population

100 participants recruited, paid US $2.00. Three HITs were rejected and re-run because over a quarter of their answers were off by more than 30%, so 103 people took part and 100 were paid. Six more were removed as outliers for average error above 172%. Maximum error among the remaining 94 was 45%. Average completion time was 19 minutes 11 seconds.

## The authors' advice

> "It is advisable to stay away from creating triangular bar charts. Triangular charts that overlap and that have quadratically changing areas are especially worth avoiding."

> "these results suggest that it is inadvisable to scale chart elements on two axes simultaneously. This is in line with common wisdom."

> "End caps with a strong horizontal top are not advisable for tasks that involve comparing bars, but are fine (and perhaps better) for absolute judgements."

> "Bars that have a portion extending below the zero point on the value axis seem to be fine to use, assuming the portion that extends is a visibly different color from the value portion of the bar."

Two of these depend on task, so a flat "embellishment raises error" misquotes the paper.

## Limits the authors state themselves

They frame the result as a qualification of the memorability literature, not a refutation:

> "The results of this study qualify findings by Borkin and Borgo suggesting that memorability can be aided by embellishment. Changes to charts that affect the primary chart elements can reduce the communication accuracy of the chart. Increasing the memorability of a chart is certainly a worthwhile pursuit, however it must be balanced with the need to communicate information accurately in the first place."

"Balanced with" is a value judgment. The study did not measure memorability, so it establishes one side's cost and cannot say where the balance sits.

The conclusion calls the contribution "a basis for exploring the impact of low-level design elements in graphical perception," a first step rather than a settled question.

## What this result does not license

- **Not "Studies show chartjunk hurts comprehension."** It shows that deforming the bar hurts numeric estimation, mostly on comparison tasks, under Bonferroni correction, on abstracted stimuli.
- **Not a claim about imagery around a correctly drawn chart.** That was not tested.
- **Not a claim about recall**, which was not measured.

## Relation to Bateman et al.

[Bateman et al.](bateman-2010-useful-junk.md) tested Nigel Holmes cartoon imagery around and behind a correctly drawn chart, and measured verbal description and recall. Skau et al. tested deformations of the bar itself and measured numeric estimation error. Holmes's bars still have flat tops, so Skau's mechanism predicts they read accurately, which is what Bateman found. Decoration around the marks is contested. Deformation of the marks is not. That is finer-grained than [refutations.md](../refutations.md)'s "strip decoration, keep orientation," and compatible with it.

## Links

- Study code and data: [github.com/dwskau/chart-embellishment](https://github.com/dwskau/chart-embellishment)
- [bateman-2010-useful-junk.md](bateman-2010-useful-junk.md)
- [gillan-richman-1994-data-ink.md](gillan-richman-1994-data-ink.md)
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md), cited by this paper: another result about the bar glyph carrying unintended perceptual meaning
- [refutations.md](../refutations.md), "Chartjunk and the data-ink ratio as settled"
- [inventory.md](../inventory.md), topics 67 and 88
