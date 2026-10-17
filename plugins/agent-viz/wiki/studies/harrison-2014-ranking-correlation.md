---
type: study
status: primary-read
retrieved: 2026-10-17
---

# Harrison et al. (2014), *Ranking Visualizations of Correlation Using Weber's Law*, and the Kay & Heer (2016) reanalysis

Lane Harrison, Fumeng Yang, Steven Franconeri and Remco Chang, *IEEE TVCG* 20(12), InfoVis 2014. Matthew Kay and Jeffrey Heer, "Beyond Weber's Law: A Second Look at Ranking Visualizations of Correlation," *IEEE TVCG* 22(1), InfoVis 2015. One experiment and the secondary analysis of its published data, on one page because the second paper changes what the first one licenses.

**What it is good for.** The one measurement in this corpus of a shape judgment rather than value extraction: how precisely readers tell two correlations apart, on nine forms, with 1,687 participants. It is the evidence behind choosing a scatterplot for a correlation, and it puts numbers on parallel coordinates, radar, stacked and line forms that otherwise have none.

**What it does not settle.** Accuracy. The task was discrimination, which of two charts is more correlated, so a reader could be precise and systematically biased. The stimulus was Pearson's r between 0.3 and 0.8 on 100 bivariate normal points at 300 by 300 pixels, so nothing here reaches nonlinear structure, clusters, outliers or real data. Several forms were put to a job they are rarely chosen for: the "donut" and "stacked bar" here show 100 paired values, not a part-to-whole.

**How this was read.** Both PDFs downloaded, Harrison et al. from the Tufts author site and Kay & Heer from the IDL file host, extracted locally with `pdftotext`, titles checked against the first page. Table values were cross-checked against the running text. The text layer drops minus signs in places, so model-comparison statistics are reported here in words where the sign could not be confirmed. The rankings in Figure 7 and Figure 8 were read from extracted figure labels, which lose layout, and are quoted from the text where the text states them.

---

## The task

Two charts side by side, one at a target r and one further from it. The participant picks the one that looks more correlated. A correct pick shrinks the gap by 0.01 and a wrong one widens it by 0.03, and the staircase converges on the difference a reader detects 75% of the time, the just-noticeable difference. Six target values of r (0.3 to 0.8), approached from above and from below, with positively and negatively correlated data. Simulating a participant guessing at random 10,000 times put the chance boundary at a JND of 0.45.

Experiment 1 re-ran Rensink and Baldridge's 2010 laboratory scatterplot study with 88 Mechanical Turk workers and reproduced it: the Weber fit had r² = 0.98, with a slightly lower intercept (0.21 against 0.25) and a similar slope (-0.17 against -0.22). Experiment 2 extended it to nine forms.

## The nine forms

Scatterplot, parallel coordinates, stacked area, stacked bar, stacked line, line, ordered line, radar and donut. Line and stacked forms were "included based on the top recommendations when viewing one of our datasets (100 points, 2 dimensions) in Microsoft Excel." Donut and radar "are essentially radial transforms of stacked bar charts and line charts, respectively." The authors note that only two forms are bivariate in the strict sense:

> "scatterplots and parallel coordinates plots are the only two that are truly bivariate, in that the two quantitative variables in the data displayed (X, Y) determine the exact position of the graphical elements. In contrast, all of the other visualizations contain an additional explicit variable order."

The ordered line chart, sorted on x, was added to test the effect of that order.

## What Harrison et al. found

1,687 participants, about 30 per form, direction and target r. JNDs beyond three median absolute deviations were dropped. Six of the eighteen form-direction pairs had more than 20% of judgments at or beyond the chance boundary and were excluded from the ranking: stacked area, stacked bar, stacked line and donut with positive data, and radar and line with negative data.

The scatterplot was symmetric, with no difference between positive and negative data (p = 0.54), and "among the best performing visualizations." Parallel coordinates were not:

> "We find clear evidence of asymmetry in parallel coordinates plots, with those depicting negatively correlated data significantly outperforming those depicting positively correlated data (p < 0.001)."

With negative data, parallel coordinates did not differ from scatterplots with either positive (p = 0.16) or negative (p = 0.42) data. Among the stacked forms with negative data, the stacked bar beat both the stacked area and the stacked line (both p < 0.001), and did not differ from the donut. Among the line forms with positive data, the ordered line beat both the line (p < 0.001) and the radar (p < 0.001), and the radar beat the line (p = 0.0017). The Bonferroni-corrected threshold was α = 0.0036.

Every retained pair fit a straight line of JND against adjusted r, which the paper reads as Weber's law holding for all nine forms. Table 2 gives the scatterplot with positive data an intercept of 0.17 and r² = 0.98, and the line chart with positive data an intercept of 0.46 and r² = 0.74. The overall ranking in Figure 7, best first: scatterplot positive, parallel coordinates negative, scatterplot negative, stacked bar negative, ordered line positive, donut negative, stacked area negative, ordered line negative, stacked line negative, parallel coordinates positive, radar positive, line positive.

The paper draws a design implication from the asymmetry: "new layout algorithms could be developed to maximize the number of negative correlations depicted by flipping and re-arranging axes." On mechanism, it argues that the forms differ in which visual feature carries the correlation, with a participant in the stacked bar condition comparing "how much white and orange were compared to the blue" while stacked line participants looked at spikiness, and that for scatterplots "the underlying visual features that vary with correlation follow Weber's law," naming the width of the point cloud.

## What Kay & Heer changed

The reanalysis used the released data and refit it in four steps, each with a stated reason.

**Individual observations instead of condition means.** Harrison et al. fit lines to the mean JND in each condition, which is how Rensink and Baldridge and the classical Weber literature proceed. "98% of individual variation is not explained by this model, as individual variation was discarded before the model was fit."

**A log-linear model instead of a linear one.** JND cannot go below zero and bunches up as it approaches it, so the linear model's residuals had non-constant variance and skew. A Box-Cox fit estimated the transformation parameter at 0.0292 with a 95% confidence interval that includes 0, the log transform, and excludes 1, the linear model. The log-linear model had lower AIC and less skewed residuals, and "deviates from Weber's Law."

**Censored regression instead of exclusion.** Observations at the chance boundary or at the ceilings set by r itself are known only to be at least that bad. Treating them as exact values biases a fit: "This bias conspires to make low-performing visualizations seem better than they are." Censoring lets the six excluded pairs back in with wider uncertainty.

**A Bayesian mixed model with a participant effect.** Four JNDs per participant are not four independent observations.

The result is a partial ranking in four groups, each at least 1.5 times more precise than the one below on average:

| Group | Form-direction pairs |
|---|---|
| High precision | Scatterplot positive, scatterplot negative, parallel coordinates negative |
| Medium precision | Stacked bar negative, ordered line positive, ordered line negative, donut negative, stacked area negative, stacked line negative |
| Low precision | Parallel coordinates positive, radar positive, line positive |
| Indistinguishable from chance | Stacked line positive, stacked area positive, stacked bar positive, line negative, donut positive, radar negative |

The high group is about 1.5 to 2 times more precise than the medium group, and the low group about 1.5 to 3 times more precise than the chance group. The authors add that "indistinguishable from chance" means "so far as this model and data can tell."

On the headline comparison:

> "We believe that these design recommendations overstate the strength of evidence. By contrast, our model finds that the performance of scatterplots and parallel coordinates are virtually indistinguishable at those values of r for negatively-correlated data, and that when considering variance between individuals, scatterplots may even be better."

And on the form that comes out ahead:

> "scatterplots are unique in combining low variance between individuals and high precision on both positively- and negatively- correlated data."

Their recommendation is to "use scatterplots to visualize bivariate correlation, regardless of the value of r."

## Limits

- Discrimination, not estimation. Neither paper measures whether readers over- or under-estimate r on any form.
- r from 0.3 to 0.8. Kay & Heer note that Weber's law and the log-linear model disagree most at 0.1 and 0.9, where no data was collected.
- 100 bivariate normal points, 300 by 300 pixels, two colors, Mechanical Turk, with mobile devices blocked. No real data, no nonlinear relationship, no outliers.
- Harrison et al. on their exclusions: "it is possible that either correlation is not reliably perceived in these [form-direction] pairs, or that a larger starting distance (and corresponding penalties) is required." Kay & Heer's censoring addresses the modeling, not the design.
- Kay & Heer: "What remains is to articulate credible perceptual processes driving the observed data."

## What this does and does not license

- **Evidence-backed.** For telling two correlations apart, the scatterplot is in the highest-precision group with positive and negative data alike, and its variance between individuals is no higher than its nearest rival. Parallel coordinates with two axes match it on negative data and sit two groups down on positive data. Line, stacked and radial forms are a step or more down, and six form-direction pairs are indistinguishable from chance.
- **Overstated by the original and corrected by the reanalysis.** That parallel coordinates beat the scatterplot for negative correlations at low r. The total ranking carried no uncertainty, and the two forms are indistinguishable there. The axis-flipping proposal rests on an asymmetry that survives, not on a lead that does.
- **Not licensed.** "Scatterplots are the most accurate chart," as a general claim. The task was correlation discrimination, and value extraction, trend shape, clusters and outliers were not measured. Nothing here concerns parallel coordinates with the many axes the form is chosen for, or a donut, stacked bar or radar used as a part-to-whole, composition or profile chart.
- **Changed.** Weber's law as a model of correlation perception. The reanalysis fits a log-linear model better and declines to call the relationship Weber's.

## See also

- [../chart-types/scatterplot.md](../chart-types/scatterplot.md) and [../chart-types/parallel-coordinates.md](../chart-types/parallel-coordinates.md): the two forms this result reaches
- [../chart-types/correlation.md](../chart-types/correlation.md): the group, with the scope of what is measured
- [../chart-types/radar-chart.md](../chart-types/radar-chart.md): drawn here for a job it is rarely chosen for
- [heer-bostock-2010.md](heer-bostock-2010.md): the same crowdsourcing method on value extraction
- [../people/jeffrey-heer.md](../people/jeffrey-heer.md) and [../people/steven-franconeri.md](../people/steven-franconeri.md): an author on each paper
- [../concepts/channels.md](../concepts/channels.md): the value-extraction ranking this task sits outside
