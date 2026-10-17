---
type: index
---

# Uncertainty

How precisely an estimate is known, and whether a difference between estimates is larger than the noise.

## Is the estimate the question?

The [FT](../sources/ft-visual-vocabulary.md) taxonomy has no uncertainty family. Its Uncertainty section is an unfinished stub with reading links and no types. It files the fan chart under Change over Time and the box plot and violin under Distribution, and [distribution.md](distribution.md) has housed the mean-and-error forms for want of anywhere else. This group is this wiki's own, alongside the FT's nine. [Wilke](../sources/wilke-fundamentals.md) gives uncertainty its own section of his catalog (chapter 16), while [Schwabish](../sources/schwabish.md) files his two uncertainty sections inside Distribution. A filing is a retrieval aid, not a claim about charts ([README.md](README.md)).

Three tests decide whether a figure belongs here.

**Is the subject an estimate, or a sample's shape?** "How spread out are these numbers" is a [distribution](distribution.md) question. "How precisely do I know this mean" is this group's. The two can produce identical drawings.

**Is the interval descriptive or inferential?** [seaborn](../sources/seaborn.md) crosses what an interval shows with how it is built:

| | Parametric | Nonparametric |
|---|---|---|
| Spread of the data (descriptive) | SD | Percentile interval |
| Uncertainty of the estimate (inferential) | SE | Bootstrap CI |

"But uncertainty will decrease as sample sizes grow, whereas spread will not." Only the bottom row answers this group's question. A figure drawing the top row is a distribution figure, whatever it looks like.

**Is n a count of independent things?** [Cumming, Fidler & Vaux (2007)](../studies/cumming-2007-error-bars.md), rule 3: "error bars and statistics should only be shown for independently repeated experiments, and never for replicates." Triplicate cultures repeated four times give n = 4. An SE computed over replicates looks precise and answers nothing about the effect. `authority-asserted`, with a stated reason.

| The reader's question | Group |
|---|---|
| How sure is this estimate? Is this difference real? | **This group** |
| How spread out is the sample, and what shape is it? | [Distribution](distribution.md) |
| Three or four observations per group | The observations themselves: a [dot strip plot](dot-strip-plot.md) or [beeswarm](beeswarm-plot.md) |
| How big is it? | [Magnitude](magnitude.md). A bare point estimate still asserts a precision, and [inventory.md](../inventory.md) topic 48 asks for the interval, `authority-asserted` |
| How uncertain is a projection, and how fast does that grow? | A [fan chart](fan-chart.md), which the FT files under Change over Time. Untested here |

## What this group costs

The interval's meaning sits on no channel. An SD, an SE, a 95% CI and a percentile interval draw as the same whisker, so the meaning lives only in the guides. Cumming et al.:

> "Because error bars can be descriptive or inferential, and could be any of the bars listed in Table I or even something else, they are meaningless, or misleading, if the figure legend does not state what kind they are."

Their rules 1 and 2 ask the legend to name the interval and give n, `authority-asserted` ([inventory.md](../inventory.md) topic 49).

The label is necessary and not sufficient. [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) asked 473 published authors to drag a mean until two labeled means looked just significantly different. "Only 22% of respondents set the means so the p value was between .025 and .10." The correct answers for the CI and SE versions sit 160 units apart, and the two groups' averages differed by 48. 31.5% placed the intervals just touching, which gives p ≈ .006 for 95% CIs and p ≈ .16 for SE bars. `evidence-backed`, on one task (positioning two means to a target p-value) with a 15.2% response rate.

The glyph carries meaning too. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found that a bar with error bars biases the reader:

> "**Within-the-bar bias:** the glyph of a bar provides a false metaphor of containment, where values within the bar are seen as likelier than values outside the bar."

No symmetric encoding they tested (a modified box plot, a gradient plot, a violin) showed it. `evidence-backed`, from 240 crowdsourced participants on low-stakes predictions.

## Choosing a form

| Form | What is drawn | Where it applies |
|---|---|---|
| [Interval plot](interval-plot.md) | A point per estimate and a stated interval | Many estimates on one scale where the bounds must be read. Symmetric, with hard edges. Not itself tested |
| Bar with error bar, on [interval-plot.md](interval-plot.md) | A bar to the estimate and a whisker | The form Correll & Gleicher measured against. Shows the within-the-bar bias |
| [Gradient plot](gradient-plot.md) | A band of continuous opacity around a mean | Symmetric and continuous. Tested, no within-the-bar bias |
| [Violin plot](violin-plot.md) | A mean and its error on a symmetric continuous mark | The other tested symmetric continuous form. The authors decline to rank it against the gradient |
| [Fan chart](fan-chart.md) | A projected path with nested probability bands that widen over time | A forecast rather than an estimate per category. Not tested |
| [Dot strip plot](dot-strip-plot.md), [beeswarm](beeswarm-plot.md) | Every observation | n is small. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) measured a median smallest group of 4 across 703 physiology articles and recommend the points. Cumming et al.'s rule 4 says the same at n = 3 |

Wilke's chapter 16 catalogs further forms: quantile dotplots, hypothetical outcome plots, graded error bars, confidence strips and eye plots ([wilke-fundamentals.md](../sources/wilke-fundamentals.md)). None has a page here, and the studies he cites for two of them have no study page.

## Justifying the choice

**Defensible, evidence-backed:**

- "The legend names the interval and gives n. The four interval types draw identically, and published authors misread even labeled CI and SE bars, measured."
- "No bars under the estimates. With a bar and error bars, outcomes inside the bar were judged likelier than outcomes the same distance above it, and the symmetric encodings did not show that."
- "A gradient plot rather than a bar with error bars, for a general audience. Crowdsourced readers did better with the unfamiliar symmetric form than with the familiar one."

**Defensible, with the label said out loud:**

- "A dot with whiskers rather than a gradient or violin, because the bounds have to be readable. It is symmetric, the property the bias turned on, but it was not one of the forms tested."
- "Three observations per group, so I plotted them. That comes from two sets of authors reasoning from measured sample sizes, not from a reader experiment."
- "n counts independent experiments, not replicates. That is Cumming et al.'s rule 3, expert guidance with a stated reason."

**Commonly repeated, and not supported:**

- ~~"If the error bars don't overlap, the difference is significant."~~ SE bars that just touch give p ≈ .16 (Belia et al.).
- ~~"If the confidence intervals overlap, the difference is not significant."~~ 95% CIs on independent means that just touch give p ≈ .006. Cumming et al.'s rule 7 puts p ≈ 0.05 at an overlap of one full arm, for n = 3.
- ~~"An expert audience reads error bars correctly."~~ Belia et al.'s sample had all published in leading journals.
- ~~"Tight error bars mean good data."~~ They may mean replicates counted as n, or an SE over a large sample with a wide spread.

## The failure mode this group invites

An interval drawn without its meaning. The reader picks one of four readings, and Belia et al.'s respondents erred in opposite directions depending on which they had: too strict with CIs (mean response p ≈ .009), too lax with SE bars (p ≈ .109). The choice also does rhetorical work. Weissgerber et al. found 77.6% of bar-graph papers showed the mean with an SE and 15.3% with an SD, and [interval-plot.md](interval-plot.md) carries their point that the SE magnifies apparent differences.

The second failure is the bar under the estimate. Its containment metaphor makes the region below the mean read as likelier than the region above, and Correll & Gleicher found the bias persisted when the outcome being judged moved out of the chart into text.

## Types in this index

- [interval-plot.md](interval-plot.md): also covers the bar with error bars
- [gradient-plot.md](gradient-plot.md)
- [fan-chart.md](fan-chart.md): also change over time, where the FT files it
- [violin-plot.md](violin-plot.md): as a mean-and-error encoding, indexed primarily under [distribution.md](distribution.md)

## See also

- [distribution.md](distribution.md): the sample's shape, and the sample-size gate
- [../concepts/evidence-class.md](../concepts/evidence-class.md): the labeling discipline
- [../inventory.md](../inventory.md): topics 48 to 51, display, semantics, distribution over summary, impossible bounds
