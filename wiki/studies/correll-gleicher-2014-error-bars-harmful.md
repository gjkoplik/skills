# Correll & Gleicher 2014: Error Bars Considered Harmful

Michael Correll, Michael Gleicher. *Error Bars Considered Harmful: Exploring Alternate Encodings for Mean and Error.* IEEE TVCG 20(12):2142-2151, December 2014. DOI [10.1109/TVCG.2014.2346298](https://doi.org/10.1109/TVCG.2014.2346298).

## What it is

Three crowdsourced experiments comparing the standard bar-chart-with-error-bars against three symmetric alternatives (modified box plot, gradient plot, violin plot) on inferential tasks. The finding that matters: the bar glyph creates a **containment metaphor** that biases judgment, and the bias survives even when you move the numbers out of the chart and into text.

## Status

**`primary-read`.** Authors' preprint PDF retrieved from [graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf](https://graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf) and re-extracted locally with `pdftotext -layout`. The file carries the line "Authors' preprint version. To appear in IEEE Transactions on Visualization and Computer Graphics, Dec. 2014." Page numbering differs from the journal version.

Retrieval date: **2026-08-23**.

## What it is good for

The evidence behind "the encoding of uncertainty is a design decision with measurable consequences, not a formatting detail." Cite it for within-the-bar bias specifically, and for the result that alternate encodings cost a general audience nothing despite being unfamiliar. It is also the paper that establishes bar-plus-error-bar as the modal encoding in the visualization community's own publications, which makes the finding awkward in a useful way.

## What it does not settle

It does not tell you *which* alternative to use, and says so. It does not test decision-making with real stakes. And the title overstates the paper's own conclusion, which is comparative rather than absolute.

## The finding

Two named defects in bar charts with error bars:

> "**Within-the-bar bias:** the glyph of a bar provides a false metaphor of containment, where values within the bar are seen as likelier than values outside the bar."

> "**Binary interpretation:** values are within the margins of error, or they are not. This makes it difficult for viewers to confidently make detailed inferences about outcomes, and also makes viewers overestimate effect sizes in comparisons."

The proposed fix is stated as a property rather than as a specific chart:

> "We can mitigate these problems by choosing encodings that are visually symmetric and visually continuous. Gradient plots and violin plots are example solutions."

The abstract's claim, which is the one usually quoted:

> "the encoding of mean and error significantly changes how viewers make decisions about uncertain data."

## The findings, experiment by experiment

**Experiment 1, one-sample judgments** (96 participants, 8 per encoding-by-framing cell). A red dot proposes an outcome; participants rate its likelihood. Six margin-of-error levels from 2.5 to 15.0.

- Significant interaction between dot position (above or below the mean) and encoding, F(2,2) = 21.3, p < 0.0001. Post-hoc HSD: in the bar chart condition, dots *below* the mean, and so inside the bar's visual area, were rated significantly more likely than dots above. Not significant for any of the symmetric encodings.
- Adherence to the expected strategy was higher with symmetric encodings (violin 89.2% of trials, gradient 88.5%, box 87.4%) than with bars (83.2%).
- Confidence was higher with the two encodings carrying distribution detail (gradient M = 5.12, violin M = 5.06) than with bars and box plots (both M = 4.86).

**Experiment 2, textual one-sample judgments** (48 participants, 24 per graph type). Moves the proposed outcome, and then also the margin of error, out of the chart and into text. This is how polling data is often presented in practice.

- Within-the-bar bias persisted when only the outcome moved to text. It was mitigated only when *both* the outcome and the margin of error left the chart, F(1,1717) = 15.3, p < 0.0001.
- But that fix breaks the chart. Adherence to the expected strategy fell from 91.6% of trials (visual error bars) to 62.2% (text-only margins), while confidence went *up*, F(1,1717) = 64.8, p < 0.0001, M = 5.4 versus 4.9. The authors' phrasing: participants were "unjustifiably more confident in their incorrect judgments."

**Experiment 3, two-sample judgments** (96 participants, 8 per cell). Comparison of two groups.

- Average confidence tracked p-value across all graph types, R² = 0.66, β = -8.30. Even a lay audience is doing something statistically sensible.
- Bar-chart participants were significantly more confident than users of the other encodings, and the gap widened on stimuli that *fail* a t-test at α = .05 (bars M = 4.42 versus M = 4.15 for other encodings). The authors call this elevated confidence "in a sense unjustified, occurring whether differences were statistically significant or not."

## Method

Amazon Mechanical Turk, North American workers only. Mixed design: encoding type and problem framing were between-subjects (each participant saw one encoding and one wording), while distance between means and margin-of-error size were within-subjects. Problem framing was polling, weather or financial prediction; framing was a significant effect every time it was varied, so it was carried as a covariate. Each participant saw 36 graphs in sequence.

The box plot was modified for the task: whiskers are the 95% t-confidence interval, the box is a 50% t-confidence interval computed from the inverse cdf at 0.25 and 0.75, and the center line is the mean rather than the median.

## Sample size and population

Total recruited including piloting: 368. In the three reported experiments: **240 participants** (102 male, 138 female, mean age 33.3, SD 10.2), of whom 90 had some college, 110 were college graduates and 31 held postgraduate degrees.

## Limits the authors state themselves

They are notably restrained about their own title.

On the recommendation:

> "Our experiments suggest that some encoding other than bar charts with error bars should be used, but are less specific in recommending the best replacement."

On the two alternatives they proposed:

> "Our data do not support the use of one over the other for decisions tasks, however paper authors, reviewers, and colleagues have stated differing preferences between the two on aesthetic and theoretical grounds."

On bars not being uniformly bad:

> "This is not to say that bar charts do not have utility. There are tasks where asymmetric encodings outperform symmetric encodings; for instance, comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots."

They also name the cultural cost: "viewers might prefer to see familiar but known suboptimal encodings."

Four further limits they state:

1. **No real decision-making.** "One area not well-covered by our experimental tasks was decision-making: does the presentation of different sorts of statistical graphs result in different actions (beyond mere predictions)?" They suggest an experiment with real-world stakes would show clearer differences.
2. **Practical significance unknown.** "The performance improvements of the alternate encodings are measurable in our experiments, but the practical effect of these differences is difficult to determine."
3. **Design parameters unexplored.** They colored the gradient plot so the region inside the margin of error is fully opaque rather than encoding the pdf directly, and used a single set of color ramps. They flag that other choices might bias judgments, citing the Cleveland & McGill color-caused optical illusion result.
4. **Little qualitative data.** They did not collect viewer preferences among chart types.

## What this result does not license

"Never use error bars." The paper's own conclusion is that a *symmetric, continuous* encoding outperforms bar-plus-error-bar on inferential tasks, in a lab, on low-stakes prediction. It does not test scientific-publication figures, it does not compare against showing the raw distribution, and it explicitly declines to rank its own two proposals.

## Where this sits against the rest of the cluster

[Belia et al. 2005](belia-2005-ci-misconceptions.md), which this paper cites, shows that expert readers misread error bars. This paper shows that part of the problem is the glyph rather than the reader, and that a general audience does better with an unfamiliar encoding than with the familiar broken one. The two papers point in different remedial directions: Belia's authors ask for better training and clearer conventions, these authors ask for a different mark.

The within-the-bar result is also worth putting next to [Skau et al. 2015](skau-2015-embellished-bars.md), which finds that the bar's *strong horizontal top* is load-bearing for absolute value estimation. Both papers are about the bar glyph carrying more perceptual meaning than its designers intend, in opposite directions.

## Links

- Preprint: [graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf](https://graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf)
- [belia-2005-ci-misconceptions.md](belia-2005-ci-misconceptions.md)
- [cumming-2007-error-bars.md](cumming-2007-error-bars.md)
- [skau-2015-embellished-bars.md](skau-2015-embellished-bars.md)
- [inventory.md](../inventory.md), topic 49, which already quotes this paper's abstract
