---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Correll & Gleicher 2014: Error Bars Considered Harmful

Michael Correll, Michael Gleicher. *Error Bars Considered Harmful: Exploring Alternate Encodings for Mean and Error.* IEEE TVCG 20(12):2142-2151, December 2014. DOI [10.1109/TVCG.2014.2346298](https://doi.org/10.1109/TVCG.2014.2346298).

Three crowdsourced experiments comparing bar-chart-with-error-bars against a modified box plot, a gradient plot and a violin plot on inferential tasks. The bar creates a **containment metaphor** that biases judgment, and the bias survives when the numbers move into text.

**What it is good for.** Evidence that "the encoding of uncertainty is a design decision with measurable consequences, not a formatting detail." Within-the-bar bias, and unfamiliar encodings costing a general audience nothing. It also establishes bar-plus-error-bar as the modal encoding in visualization publications.

**What it does not settle.** Which alternative to use, or decisions with real stakes. The conclusion is comparative; the title is absolute.

**How this was read.** Authors' preprint from [graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf](https://graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf), extracted locally with `pdftotext -layout`. The file reads "Authors' preprint version. To appear in IEEE Transactions on Visualization and Computer Graphics, Dec. 2014." Page numbering differs from the journal version.

## The finding

> "**Within-the-bar bias:** the glyph of a bar provides a false metaphor of containment, where values within the bar are seen as likelier than values outside the bar."

> "**Binary interpretation:** values are within the margins of error, or they are not. This makes it difficult for viewers to confidently make detailed inferences about outcomes, and also makes viewers overestimate effect sizes in comparisons."

The fix is a property, not a chart:

> "We can mitigate these problems by choosing encodings that are visually symmetric and visually continuous. Gradient plots and violin plots are example solutions."

> "the encoding of mean and error significantly changes how viewers make decisions about uncertain data."

## Experiment by experiment

**Experiment 1, one-sample judgments** (96 participants, 8 per encoding-by-framing cell). Participants rated the likelihood of a red-dot outcome, at six margin-of-error levels from 2.5 to 15.0.

- Dot position interacted with encoding, F(2,2) = 21.3, p < 0.0001. With bars, dots *below* the mean, inside the bar, were rated significantly more likely than dots above (post-hoc HSD). No symmetric encoding showed this.
- Adherence to the expected strategy was 83.2% of trials with bars, against 87.4% box, 88.5% gradient and 89.2% violin.
- Confidence was higher for gradient (M = 5.12) and violin (M = 5.06) than for bars and box plots (both M = 4.86).

**Experiment 2, textual one-sample judgments** (48 participants, 24 per graph type). The outcome, then also the margin of error, moved into text.

- The bias persisted with only the outcome in text and eased only when *both* left the chart, F(1,1717) = 15.3, p < 0.0001.
- Adherence then fell from 91.6% of trials to 62.2% while confidence rose, F(1,1717) = 64.8, p < 0.0001, M = 5.4 versus 4.9. Participants were "unjustifiably more confident in their incorrect judgments."

**Experiment 3, two-sample judgments** (96 participants, 8 per cell).

- Confidence tracked p-value across all graph types, R² = 0.66, β = -8.30.
- Bar-chart participants were significantly more confident than the others, more so on stimuli that *fail* a t-test at α = .05 (M = 4.42 versus 4.15), which the authors call "in a sense unjustified, occurring whether differences were statistically significant or not."

## Method

Mechanical Turk, North American workers. Encoding and framing (polling, weather or finance) were between-subjects, distance between means and margin of error within-subjects. Framing was always significant and became a covariate. Each participant saw 36 graphs. The box plot's whiskers are the 95% t-confidence interval, its box a 50% t-confidence interval from the inverse cdf at 0.25 and 0.75, and its center line the mean.

## Sample size and population

368 recruited including piloting. The three reported experiments had **240 participants** (102 male, 138 female, mean age 33.3, SD 10.2): 90 with some college, 110 college graduates, 31 with postgraduate degrees.

## Limits the authors state themselves

> "Our experiments suggest that some encoding other than bar charts with error bars should be used, but are less specific in recommending the best replacement."

> "Our data do not support the use of one over the other for decisions tasks, however paper authors, reviewers, and colleagues have stated differing preferences between the two on aesthetic and theoretical grounds."

> "This is not to say that bar charts do not have utility. There are tasks where asymmetric encodings outperform symmetric encodings; for instance, comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots."

They name a cultural cost: "viewers might prefer to see familiar but known suboptimal encodings."

**No real decision-making.** They expect real stakes to show clearer differences.

> "One area not well-covered by our experimental tasks was decision-making: does the presentation of different sorts of statistical graphs result in different actions (beyond mere predictions)?"

**Practical significance unknown.**

> "The performance improvements of the alternate encodings are measurable in our experiments, but the practical effect of these differences is difficult to determine."

**Design parameters unexplored.** The gradient was opaque inside the margin of error rather than encoding the pdf, with one color ramp set. Other choices might bias judgments (Cleveland & McGill's color-caused optical illusion).

**Little qualitative data.** Preferences among chart types were not collected.

## What this result does not license

- **Not "never use error bars."** A symmetric, continuous encoding beat bar-plus-error-bar on inferential tasks, in a lab, on low-stakes prediction.
- **Not a result about scientific-publication figures**, which were not tested.
- **Not a comparison with showing the raw distribution.**
- **Not a ranking of gradient against violin**, which the authors decline to give.

## Related studies

[Belia et al. 2005](belia-2005-ci-misconceptions.md), cited here, finds experts misread error bars and asks for training. This paper blames the glyph and asks for a different mark. [Skau et al. 2015](skau-2015-embellished-bars.md) finds the bar's strong horizontal top aids absolute value estimation, the same glyph carrying unintended meaning in the other direction.

## Links

- Preprint: [graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf](https://graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf)
- [belia-2005-ci-misconceptions.md](belia-2005-ci-misconceptions.md)
- [cumming-2007-error-bars.md](cumming-2007-error-bars.md)
- [skau-2015-embellished-bars.md](skau-2015-embellished-bars.md)
- [inventory.md](../inventory.md), topic 49 (quotes the abstract)
- [../people/michael-correll.md](../people/michael-correll.md): the first author
