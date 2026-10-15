---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Correll, Bertini & Franconeri 2020: Truncating the Y-Axis: Threat or Menace?

Michael Correll (Tableau Research), Enrico Bertini (NYU), Steven Franconeri (Northwestern). CHI 2020. arXiv [1907.02035v2](https://arxiv.org/abs/1907.02035), 8 January 2020.

Three crowdsourced experiments on whether y-axis truncation inflates perceived effect size (yes), whether chart type changes that (no), and whether announcing the truncation with a broken-axis glyph or a gradient fade reduces it (no measurable reduction).

**What it is good for.** Evidence that line charts are not exempt from the truncation critique, and that the tested axis-break markers did not measurably help. A hedged source for the position that quantitative axes have no honest/dishonest binary.

**What it does not settle.** Whether any truncation indicator can work. Only two static designs were tested, and the null is knife-edge.

**How this was read.** Extracted locally with `pdftotext` from the arXiv v2 PDF.

## The findings

**Experiment One (framing and chart type).** Truncation raised perceived severity, F(2, 76) = 89, p < 0.0001, with all three truncation levels significantly different from each other under a Bonferroni-corrected pairwise t-test. Chart type did nothing:

> "There was no significant effect of visualization design on perceived effect size (F(1, 38) = 0.5, p = 0.50)."

Question framing (value versus trend) reached significance, F(1, 38) = 7.4, p = 0.01, but the post-hoc did not confirm it. Its effect was an average decrease of 0.07 on the 1-to-5 rating, against an increase of 0.36 for starting the axis at 25% rather than 0%.

**Experiment Two (design interventions).** The headline null:

> "Our results fail to support our first hypothesis: there was no significant difference between perceived severity among visualization designs (F(2, 60) = 3.1, p = 0.05). A post-hoc pairwise t-test with a Bonferroni correction failed to find any significant difference between visualization designs."

**Experiment Three (value estimation).** Typing estimates of the first and last bar did not remove the bias: severity still differed across truncation levels, F(1, 20) = 11, p = 0.003. Trend-estimation error did not, F(1, 20) = 0.002, p = 0.96. Value-estimation error did, F(1, 20) = 8.3, p = 0.009, driven entirely by the 25% condition (P1 said charts running 25 to 100 were harder than any other scale). The authors blame an awkward anchor point, and say the result "does not suggest that y-axis truncation creates a monotonic increase in error."

## The null in Experiment Two is knife-edge

The critical F(2, 60) at alpha = .05 is 3.1504, so the observed 3.1 gives p of about 0.052. That is a failure to reject, not evidence of no effect. No equivalence test or Bayes factor is reported, and the Fig. 8 pattern runs in the predicted direction. Power is thin: 32 participants in Experiment Two (31 after exclusion, as the error df of 60 implies) and 25 in Experiment Three. The supportable claim is that two static designs produced no measurable reduction at this sample size.

## Method

Within-subjects on prolific.ac, approved by the Tableau Software IRB, analyzed by repeated measures ANOVA. The measure was a 5-point rating of how severe or important the difference was. The value framing asked "Subjectively, how different is the first value compared to the last value?" with anchors "Almost the Same," "Somewhat Different," "Extremely Different." The trend framing asked "Subjectively, how quickly are the values changing?" with anchors "Barely," "Somewhat," "Extremely Quickly."

Factors: truncation (y-axis starts at 0, 25 or 50%), slope (12.5% or 25% change) and data size (two or three values), plus chart type and framing in Experiment One and three designs (plain, broken-axis, gradient bar) in Two and Three. 48 stimuli per participant in Experiment One; 36 plus 8 calibration stimuli in Two and Three. The comprehension check was "Are the values increasing or decreasing?" and participants more than three SDs below mean accuracy were excluded but paid. A paper author and a third-party researcher coded free text for whether participants noticed the truncation unprompted.

Materials, data and analyses: [osf.io/gz98h](https://osf.io/gz98h/).

## Sample size and population

| | Recruited | Analyzed | Demographics | Pay |
|---|---|---|---|---|
| Experiment One | 40 | 39 | 21 male, 18 female, 1 non-binary; M_age 27.7, SD 8.4 | $4, ~$12/hr |
| Experiment Two | 32 | 31 | 20 female, 12 male; M_age 29.0, SD 11.7 | $4, ~$16/hr |
| Experiment Three | 25 | 25 | 14 female, 11 male; M_age 26.1, SD 9.2 | $4, ~$8.89/hr |

Graphically literate as a group: mean scores of 10, 10.8 and 11 on the 13-item Galesic and Garcia-Retamero graph literacy scale, and 78%, 78% and 84% right on its y-axis-truncation item.

Experiment Three's F(1, 20) does not fit a three-level within-subjects factor on 25 people, in either df. The direction of the effect is not in doubt, but that df is unreliable.

## Limits the authors state themselves

From the Limitations & Future Work section:

> "Our experiments focus on a limited set of designs to assess the impact of truncation on perceived effect size. We also focus on detecting the relative difference in subjective effect size across a few different levels of truncation, rather than attempting to fully model the complex relationship between slope, axis truncation, and perceived severity."

> "Similarly, we tested only two potential designs for indicating axis truncation in bar charts as representatives of common classes of design interventions. Even of the designs we considered, we focused only on methods for static charts. Other methods using animation or interaction (such as in Ritchie et al.) could result in different patterns of subjective judgments."

> "our designs were presented in a relatively context-free manner. We believe that analysts in different domains have different internal models of effect size severity that would therefore not be captured in our results."

> "visualizations from different sources or presented with different levels of perceived expertise or authority could produce differing patterns of judgment in different audiences... a quantitative study of the persuasive power of y-axis truncation (especially for decision-making tasks) falls to future work."

From the Discussion:

> "Merely indicating that truncation has occurred, even in a prominent and unambiguous way, **may not be sufficient** to 'de-bias' viewers of truncated charts."

And the maximalist reading in the other direction:

> "we resist the interpretation of our experimental results to mean that, as Huff suggests, all charts with quantitative axes should include 0. The designer of the visualization, by selecting a y-axis starting point, has control over the subjective importance of the resulting differences. There is no a priori, domain-agnostic ground truth for how severe, important, or meaningful an effect size ought to be... We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."

## What this result does not license

- **Not "axis-break glyphs are a placebo."** Two static designs missed significance at n=31, at p ≈ 0.052.
- **Not "always start at zero."** The authors reject it by name.
- **Not "line charts and bar charts are perceptually equivalent."** Only the truncation effect, on one severity rating, did not differ.
- **Not a claim about decision-making, persuasion, or real-world consequence.** Persuasion is left to future work.
- **Not a claim about interactive or animated indicators**, which were not tested.
- **Not a claim that truncation causes value-reading errors.** Trend-estimation error was flat. The paper's mechanism is visual magnification, not misreading.

## Links

- arXiv: [1907.02035](https://arxiv.org/abs/1907.02035)
- Data and materials: [osf.io/gz98h](https://osf.io/gz98h/)
- [refutations.md](../refutations.md), "Axis-break glyphs as the truncation remedy"
- [inventory.md](../inventory.md), topic 10 (axis truncation)
- [Pandey et al. 2015](pandey-2015-deceptive-visualizations.md), whose rating-scale design this study extends and cites as reference 27
- [../people/michael-correll.md](../people/michael-correll.md): the first author, and the other rules his name gets attached to
