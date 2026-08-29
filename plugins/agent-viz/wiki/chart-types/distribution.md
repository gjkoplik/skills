---
type: index
---

# Distribution

How often each value occurs across one variable, and the shape that makes.

## Is the shape the question?

Three tests. The first one fails more often than the other two together.

**Is there enough data for a shape to exist?** [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) reviewed 703 physiology articles and measured the sample sizes behind the figures. The minimum group size shown in a figure had a median of 4, interquartile range 3 to 6; in 75% of papers the smallest group in any figure was between two and six. At those sizes there is nothing to summarize, and the paper's recommendation is to draw the observations: "Univariate scatterplots are the best choice for showing the distribution of the data in these small samples, as boxplots and histograms would be difficult to interpret." [Cumming, Fidler & Vaux (2007)](../studies/cumming-2007-error-bars.md) land in the same place from expert guidance rather than from a review, in their rule 4: "if n is very small (for example n = 3), rather than showing error bars and statistics, it is better to simply plot the individual data points."

The prevalence and the sample sizes are measured. The recommendation that follows from them is the authors' argument, not a reader experiment. Nobody has tested whether readers reach better conclusions from the points.

**Is the subject one variable's values, or something computed from them?** "How spread out are these numbers" and "how precisely do I know this mean" have different answers and identical-looking drawings. Range and SD are descriptive; SE and CI are inferential, and both shrink as n grows while SD does not. Cumming et al.: "Because error bars can be descriptive or inferential, and could be any of the bars listed in Table I or even something else, they are meaningless, or misleading, if the figure legend does not state what kind they are." Where the subject is the estimate rather than the sample, the form is still in this group and the label is still owed; [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) is the measurement of what happens when readers guess.

**Is n a count of independent things?** Cumming et al.'s rule 3 is the one that survives being carried out of cell biology: "error bars and statistics should only be shown for independently repeated experiments, and never for replicates." Twenty measurements of one specimen are not a sample of twenty specimens, and a benchmark run twenty times on one machine has n = 1 machine. The drawing does not distinguish the two. `authority-asserted`, with a stated reason.

A failed test places the question in a different group, or in a different figure:

| The reader's actual question | Group |
|---|---|
| How big is this one thing? | Magnitude. A bar chart, or a single large number |
| Which of these is biggest? | [Ranking](ranking.md). A sorted bar chart |
| How did it change? | Change over time. A line chart |
| How do two variables move together? | Correlation. A scatterplot |
| How does one total divide into parts? | [Part-to-whole](part-to-whole.md) |
| Four observations per group | The four observations drawn. A strip plot or univariate scatterplot, not a summary form |
| What shape is this variable, and does it have one mode or two? | **This group** |

## What this group costs

[Part-to-whole](part-to-whole.md) costs channel accuracy. This group costs something else, and forcing it into the channel frame gets it wrong.

**Every form here except plotting the observations computes a statistic, and the computation is invisible in the result.** Weissgerber et al.'s Fig 1 puts four datasets behind means and SEs all within 0.5 units of the same bar graph: one symmetric, one driven by a single outlier, one possibly bimodal, one with n = 3. Their summary of it: "many different data distributions can lead to the same bar or line graph. The full data may suggest different conclusions from the summary statistics." That is evidence, drawn from realistic data with real p-values. [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) make the same point for the box plot specifically, generating six distributions with identical quartiles, median and 1.5-IQR whiskers and therefore an identical drawing. That one is true by construction rather than by experiment, which is the strongest form of true available for a claim about what a summary does not determine, and no weight at all for a claim about what readers conclude.

**Most of these forms have a knob, and the knob is an analysis choice.** Bin width for a histogram, bandwidth for a violin. Wilke's chapters 7 and 14 treat both as analysis choices without giving a rule ([wilke-fundamentals.md](../sources/wilke-fundamentals.md)), and [inventory.md](../inventory.md) topic 52 asks for both to be stated and for the conclusion to be checked against a different setting. `authority-asserted`. The box plot's absence of a knob is a deliberate design property, not an accident ([john-tukey.md](../people/john-tukey.md)).

**The reader's task here is usually not value extraction, so the accuracy ranking mostly does not bear on it.** Modality, skew, gaps and outliers are shape judgments, and the graphical-perception literature measures reading a number off a mark. See [the scope limit](../concepts/channels.md#what-the-ranking-is-not-about). Where a form does put a number on a channel, that reading inherits from [channels.md](../concepts/channels.md) and nothing else does.

## Choosing a form

| Form | What is actually drawn | Where it applies |
|---|---|---|
| Strip plot / univariate scatterplot *(no page yet)* | Every observation | n is small. The recommended form at the sample sizes Weissgerber et al. measured |
| [Beeswarm](beeswarm-plot.md) | Every observation, displaced sideways so that none is hidden | Same intent as the strip plot, with the collisions resolved deterministically rather than by jitter or overlap. Untested |
| [Histogram](histogram.md) | Counts per bin | One variable, enough data, and modality or gaps matter |
| [Box plot](boxplot.md) | Five numbers per group | Many groups compared at once, and within-group shape is not the question |
| [Violin plot](violin-plot.md) | A mirrored density estimate | Shape matters across groups, or a mean and its error are being encoded on a symmetric continuous mark |
| [Ridgeline](ridgeline-plot.md) | One density estimate per group, stacked and overlapping | Many groups in a known order have to share one value axis in one figure, and occlusion is accepted to get them there. Untested |
| Gradient plot *(no page yet)* | Continuous uncertainty around an estimate | The other alternative [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) tested, and they decline to rank it against the violin |

ECDF, histogram-of-histograms and the whole small-multiple family have no page here for the same reason: no study in this source set touches them. **A page is not a warrant.** [beeswarm-plot.md](beeswarm-plot.md) and [ridgeline-plot.md](ridgeline-plot.md) have pages and no study either; what they carry is a decomposition and a set of cautions.

Four constraints that follow from the evidence rather than from taste:

- **At small n, the points rather than a summary.** Two groups arrive there by different routes, one from a 703-article review and one from expert guidance, and neither ran a reader experiment.
- **A drawn interval is named, and n is stated with it.** Cumming et al.'s rules 1 and 2 are the mechanizable pair. Belia et al. is why the label is necessary and not sufficient: 473 published authors, asked to set two means "just significantly different," and "only 22% of respondents set the means so the p value was between .025 and .10." The gap between the CI group's average and the SE group's was 48 units where the correct answers sit 160 apart, and 31.5% used the just-touching rule, which is wrong for both bar types in opposite directions.
- **For an inferential comparison, a symmetric continuous encoding outperformed a bar with error bars.** Correll & Gleicher, measured: the bar's "false metaphor of containment" made outcomes inside the bar look likelier than equidistant outcomes above it, an effect absent from all three symmetric encodings. Scope: crowdsourced, low-stakes prediction, 240 participants, no real decisions.
- **Dropped rows are disclosed.** [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) tested time series rather than distributions, and found that information removal "can significantly degrade perceptions of data quality, and confidence" and can produce incorrect answers when it breaks visual continuity. What transfers is that removal is not a neutral act. What is untested is the case a plotting library hits most often, which is a caller who never noticed rows were dropped; the paper says so itself. The mechanical version is in [checks/matplotlib.md](../checks/matplotlib.md): the input row count against the plotted count.

## Justifying the choice

**Defensible, evidence-backed:**

- "I plotted the observations rather than a mean and an interval. Four different distributions produce the same bar plus SE, shown with realistic data and real p-values, and my smallest group has five points."
- "I used a violin rather than a bar with error bars. The bar glyph made values inside the bar look likelier than values the same distance above it, measured, and the symmetric encodings did not show that bias."
- "The legend says these are 95% CIs and states n, because an unlabeled interval is ambiguous between at least four things and published authors misread them at rates measured directly."
- "This is a distribution of independent experiments, not of replicate measurements on one sample."

**Defensible, with the label said out loud:**

- "I chose this bin width and the shape survives a wider and a narrower one. There is no measured rule for bin width; the reference that covers it most thoroughly declines to give one."
- "Small n, so I plotted the points. That recommendation comes from two sets of authors reasoning from measured sample sizes, not from a reader experiment."
- "Violin rather than gradient plot. The study that recommends both explicitly declines to rank them: 'Our data do not support the use of one over the other for decisions tasks.'"

**Commonly repeated, and not supported:**

- ~~"Use a box plot instead of a bar chart."~~ Not what the review that is usually cited for it says. Box plots sit in the same bucket as bar and line graphs there, "only meaningful when there are enough data to summarize," and at the measured sample sizes the paper prefers univariate scatterplots. Six different distributions also produce one identical box plot.
- ~~"Error bars are fine as long as you label them."~~ Labeling is required and it is not sufficient. Belia et al. measured expert readers on labeled bars and found severe misconceptions, including a third of respondents applying a just-touching rule that is wrong for both bar types.
- ~~"Readers cannot handle an unfamiliar form like a violin."~~ A general crowdsourced audience did better on inferential tasks with the unfamiliar symmetric encodings than with the familiar bar and error bar. The authors do name the cultural cost separately: "viewers might prefer to see familiar but known suboptimal encodings," which is about preference, not accuracy.
- ~~"Showing the distribution leads readers to better conclusions."~~ Nobody has measured this. The prevalence of summary-only figures is measured, the many-distributions-one-summary claim is secure by construction, and the step from those to reader outcomes is `absence of evidence`, not a finding.

## The failure mode this group invites

**Letting a summary stand in for the data and letting the reader believe they have seen the distribution.** Weissgerber et al. name it precisely:

> "bar and line graphs are 'visual tables' that transform the reader from an active participant into a passive consumer of statistical information. Without the opportunity for independent appraisal, the reader must rely on the authors' statistical analyses and interpretation of the data."

There is a second, quieter version specific to this group: the choice of summary does rhetorical work whether or not it is intended. "Showing the SE rather than the SD magnifies the apparent visual differences between groups. This effect is exacerbated when the groups being compared have different sample sizes."

A usable check: if a reader could not reconstruct roughly how many observations are behind each mark, and what the drawn interval or width means, the figure is asserting more than it shows.

## Types in this index

- [histogram.md](histogram.md)
- [boxplot.md](boxplot.md)
- [violin-plot.md](violin-plot.md)
- [beeswarm-plot.md](beeswarm-plot.md), which is the same drawing as the strip plot above with the collisions displaced deterministically instead of jittered or left to overlap
- [ridgeline-plot.md](ridgeline-plot.md)
- [dot-strip-plot.md](dot-strip-plot.md), which is the strip plot drawn for a ranking question and is indexed primarily under [ranking.md](ranking.md)

ECDFs and gradient plots have no page. The gradient plot is the one with a real result attached to it, in Correll & Gleicher, and it is a result about encoding a mean and its error rather than about showing a sample. Ridgelines and beeswarms now have pages and still have no study: no experiment in this source set tests either form against anything, and the pages say so under *measurably good at*.

## A note on filing

The FT's Distribution relationship is defined as "Show values in a dataset and how often they occur. The shape (or 'skew') of a distribution can be a memorable way of highlighting the lack of uniformity or equality in the data," and it houses the box plot and the violin ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). **That taxonomy has no uncertainty family**; the section that would create one is a stub in its source repository.

That matters here more than anywhere else, because roughly half the evidence attached to this group is about encoding a mean and its error rather than about drawing a sample's shape. Those forms are indexed here for want of a better home, and the two questions are kept apart on the pages.

## See also

- [../concepts/channels.md](../concepts/channels.md) — the evidence tier, and why it bears on this group less than on part-to-whole
- [../concepts/evidence-class.md](../concepts/evidence-class.md) — the labeling discipline
- [README.md](README.md) — the page template and the inheritance rule
