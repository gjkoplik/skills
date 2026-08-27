---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Correll, Bertini & Franconeri 2020: Truncating the Y-Axis: Threat or Menace?

Michael Correll (Tableau Research), Enrico Bertini (NYU), Steven Franconeri (Northwestern). CHI 2020. arXiv [1907.02035v2](https://arxiv.org/abs/1907.02035), 8 January 2020.

Three crowdsourced experiments on whether y-axis truncation inflates perceived effect size, whether the chart type changes that, and whether design interventions that announce the truncation (a broken-axis glyph, a gradient fade at the bar tops) reduce it. Answers: yes, no, and no measurable reduction.

**How this was read.** Extracted locally with `pdftotext` from the arXiv v2 PDF. Retrieval date: **2026-08-23**.

## What it is good for

- The one place to point when someone claims **line charts are exempt** from the truncation critique. Chart type made no significant difference.
- The one place to point when someone proposes a **jagged-axis marker as the honesty fix**. The tested markers did not measurably help.
- A carefully hedged source for the position that **there is no honest/dishonest binary** for quantitative axes.

## What it does not settle

Whether *any* truncation indicator can work. Two static designs were tested. The authors say so themselves, and the headline null is a knife-edge non-rejection with no equivalence test behind it. See below.

---

## The findings, experiment by experiment

**Experiment One (framing and chart type).** Truncation drove perceived severity up: F(2, 76) = 89, p < 0.0001, with all three truncation levels significantly different from each other under a Bonferroni-corrected pairwise t-test. Chart type did nothing: "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)." Question framing (value-based versus trend-based) reached significance, F(1, 38) = 7.4, p = 0.01, but the post-hoc did not confirm it and the effect was tiny: an average decrease of 0.07 on the 1-to-5 rating, against an increase of 0.36 for starting the axis at 25% rather than 0%.

**Experiment Two (design interventions).** The headline null:

> "Our results fail to support our first hypothesis: there was no significant difference between perceived severity among visualization designs (F(2, 60) = 3.1, p = 0.05). A post-hoc pairwise t-test with a Bonferroni correction failed to find any significant difference between visualization designs."

**Experiment Three (value estimation).** Forcing participants to type numeric estimates of the first and last bar did not remove the bias. Perceived severity still differed across truncation levels, F(1, 20) = 11, p = 0.003. Error in estimating the *trend* did not differ across truncation levels, F(1, 20) = 0.002, p = 0.96. Error in estimating *individual values* did differ, F(1, 20) = 8.3, p = 0.009, driven entirely by the 25% condition, which participants complained about: P1 said charts running 25 to 100 were harder than any other scale. The authors attribute that to an awkward anchor point rather than to truncation per se, and say it "does not suggest that y-axis truncation creates a monotonic increase in error."

## The null in Experiment Two is knife-edge

The critical value of F(2, 60) at alpha = .05 is **3.1504**. The observed 3.1 sits just under it, so the exact p is about **0.052**. This is a failure to reject, not evidence of no effect. No equivalence test and no Bayes factor is reported, and the pattern in Fig. 8 is in the predicted direction.

Power is thin: 32 participants in Experiment Two (31 after exclusion, which is what the error df of 60 implies) and 25 in Experiment Three.

**Calling the tested indicators a "placebo" overstates the evidence.** The supportable claim is that two specific static designs did not produce a measurable reduction at this sample size.

## Method

Crowd-sourced on prolific.ac, approved by the Tableau Software IRB. Within-subjects, repeated measures ANOVA.

Central dependent measure: a 5-point rating of how severe or important the difference in the data series was. Under the value framing the item read "Subjectively, how different is the first value compared to the last value?" with anchors "Almost the Same," "Somewhat Different," "Extremely Different." Under the trend framing it read "Subjectively, how quickly are the values changing?" with anchors "Barely," "Somewhat," "Extremely Quickly."

Factors: truncation level (y-axis begins at 0, 25 or 50%), slope (12.5% or 25% change from first to last value), data size (two or three data values), plus chart type and question framing in Experiment One, and three visualization designs (plain bar, broken-axis bar, gradient bar) in Experiments Two and Three. 48 stimuli per participant in Experiment One; 36 plus 8 calibration stimuli in Experiments Two and Three.

An engagement question ("Are the values increasing or decreasing?") served as the comprehension check. Participants more than three standard deviations below mean engagement accuracy were excluded but still paid. Free-text responses were qualitatively coded by a paper author plus a third-party researcher for whether the participant spontaneously noticed the truncation.

Materials, data and analyses: [osf.io/gz98h](https://osf.io/gz98h/).

## Sample size and population

| | Recruited | Analyzed | Demographics | Pay |
|---|---|---|---|---|
| Experiment One | 40 | 39 | 21 male, 18 female, 1 non-binary; M_age 27.7, SD 8.4 | $4, ~$12/hr |
| Experiment Two | 32 | 31 | 20 female, 12 male; M_age 29.0, SD 11.7 | $4, ~$16/hr |
| Experiment Three | 25 | 25 | 14 female, 11 male; M_age 26.1, SD 9.2 | $4, ~$8.89/hr |

Prolific crowd workers, graphically literate as a group: mean scores of 10, 10.8 and 11 on the 13-item Galesic and Garcia-Retamero graph literacy scale, and 78%, 78% and 84% respectively answered the scale's own y-axis-truncation item correctly.

One arithmetic caution: Experiment Three reports F(1, 20) for a three-level factor with 25 participants. The numerator df of 1 and the error df of 20 are both inconsistent with a straightforward three-level within-subjects test on 25 people. The direction and the effect are not in doubt, but do not build anything on that particular df.

## Limits the authors state themselves

The paper's Limitations & Future Work section, quoted:

> "Our experiments focus on a limited set of designs to assess the impact of truncation on perceived effect size. We also focus on detecting the relative difference in subjective effect size across a few different levels of truncation, rather than attempting to fully model the complex relationship between slope, axis truncation, and perceived severity."

> "Similarly, we tested only two potential designs for indicating axis truncation in bar charts as representatives of common classes of design interventions. Even of the designs we considered, we focused only on methods for static charts. Other methods using animation or interaction (such as in Ritchie et al.) could result in different patterns of subjective judgments."

> "our designs were presented in a relatively context-free manner. We believe that analysts in different domains have different internal models of effect size severity that would therefore not be captured in our results."

> "visualizations from different sources or presented with different levels of perceived expertise or authority could produce differing patterns of judgment in different audiences... a quantitative study of the persuasive power of y-axis truncation (especially for decision-making tasks) falls to future work."

And in the Discussion, the hedge that matters most:

> "Merely indicating that truncation has occurred, even in a prominent and unambiguous way, **may not be sufficient** to 'de-bias' viewers of truncated charts."

They also explicitly refuse the maximalist reading in the other direction:

> "we resist the interpretation of our experimental results to mean that, as Huff suggests, all charts with quantitative axes should include 0. The designer of the visualization, by selecting a y-axis starting point, has control over the subjective importance of the resulting differences. There is no a priori, domain-agnostic ground truth for how severe, important, or meaningful an effect size ought to be... We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

## What this result does not license

- **Not "axis-break glyphs are a placebo."** Two static designs failed to clear significance at n=31, one of them at p ≈ 0.052. That is not a demonstrated absence of effect.
- **Not "always start at zero."** The authors reject this explicitly and by name.
- **Not "line charts and bar charts are perceptually equivalent."** The finding is that *the truncation effect* did not differ between them on a subjective severity rating. That is one measure on one task.
- **Not a claim about decision-making, persuasion, or real-world consequence.** The authors flag persuasion as future work.
- **Not a claim about interactive or animated truncation indicators**, which were not tested.
- **Not a claim that truncation causes value-reading errors.** Experiment Three found trend-estimation error flat across truncation levels. The mechanism the paper argues for is visual magnification, not misreading.

## Links

- arXiv: [1907.02035](https://arxiv.org/abs/1907.02035)
- Data and materials: [osf.io/gz98h](https://osf.io/gz98h/)
- [refutations.md](../refutations.md), "Axis-break glyphs as the truncation remedy"
- [inventory.md](../inventory.md), topic 10 (axis truncation)
- Related: [Pandey et al. 2015](pandey-2015-deceptive-visualizations.md), whose rating-scale design this study extends and cites as reference 27
