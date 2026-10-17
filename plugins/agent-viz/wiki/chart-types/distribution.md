---
type: index
---

# Distribution

How often each value occurs across one variable, and the shape that makes.

## Is the shape the question?

The FT's Distribution relationship reads "Show values in a dataset and how often they occur. The shape (or 'skew') of a distribution can be a memorable way of highlighting the lack of uniformity or equality in the data," and houses the box plot and the violin ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). Its uncertainty section is a stub in the source repository, so the taxonomy has no uncertainty family. About half this group's evidence concerns a mean and its error, not a sample's shape. Those forms are indexed here, and the pages keep the two questions apart.

Three tests. The first fails more often than the other two together.

**Is there enough data for a shape to exist?** [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) reviewed 703 physiology articles. The smallest group shown in a figure had a median size of 4 (interquartile range 3 to 6), and in 75% of papers it held between two and six. At those sizes there is nothing to summarize, and the paper recommends: "Univariate scatterplots are the best choice for showing the distribution of the data in these small samples, as boxplots and histograms would be difficult to interpret." [Cumming, Fidler & Vaux (2007)](../studies/cumming-2007-error-bars.md) say the same from expert guidance, in their rule 4: "if n is very small (for example n = 3), rather than showing error bars and statistics, it is better to simply plot the individual data points." The sample sizes are measured. The recommendation is the authors' argument, and no reader experiment tests it.

**Is the subject one variable's values, or something computed from them?** "How spread out are these numbers" and "how precisely do I know this mean" have different answers and identical-looking drawings. Range and SD are descriptive. SE and CI are inferential and shrink as n grows, while SD does not. Cumming et al.: "Because error bars can be descriptive or inferential, and could be any of the bars listed in Table I or even something else, they are meaningless, or misleading, if the figure legend does not state what kind they are." An estimate still belongs in this group and still owes the label. [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) measured what happens when readers guess.

**Is n a count of independent things?** Cumming et al.'s rule 3 holds outside cell biology: "error bars and statistics should only be shown for independently repeated experiments, and never for replicates." A benchmark run twenty times on one machine has n = 1 machine, and the drawing looks the same either way. `authority-asserted`, with a stated reason.

Where a test fails:

| The reader's question | Group |
|---|---|
| How big is this one thing? | Magnitude. A bar chart, or a single large number |
| Which of these is biggest? | [Ranking](ranking.md). A sorted bar chart |
| How did it change? | Change over time. A line chart |
| How do two variables move together? | Correlation. A scatterplot |
| How does one total divide into parts? | [Part-to-whole](part-to-whole.md) |
| Four observations per group | The four observations drawn. A strip plot or univariate scatterplot, not a summary form |
| What shape is this variable, and does it have one mode or two? | **This group** |

## What this group costs

[Part-to-whole](part-to-whole.md) costs channel accuracy. This group costs something else.

Every form except the plotted observations computes a statistic, and the result hides the computation. Weissgerber et al.'s Fig 1 puts four datasets (one symmetric, one driven by a single outlier, one possibly bimodal, one with n = 3) behind means and SEs all within 0.5 units of the same bar graph: "many different data distributions can lead to the same bar or line graph. The full data may suggest different conclusions from the summary statistics." That is evidence, from realistic data with real p-values. [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) generate six distributions with identical quartiles, median and 1.5-IQR whiskers, and so one identical box plot. That holds by construction and says nothing about what readers conclude.

Wilke's chapters 7 and 14 treat histogram bin width and violin bandwidth as analysis choices and give no rule ([wilke-fundamentals.md](../sources/wilke-fundamentals.md)). [inventory.md](../inventory.md) topic 52 asks for both to be stated and for the conclusion to be checked at another setting. `authority-asserted`. The box plot has no knob, by design ([john-tukey.md](../people/john-tukey.md)).

The reader's task here is usually a shape judgment (modality, skew, gaps, outliers), and the graphical-perception literature measures reading a number off a mark ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)), so the accuracy ranking mostly does not apply. Only a form that puts a number on a channel inherits from [channels.md](../concepts/channels.md), for that reading.

## Choosing a form

| Form | What is drawn | Where it applies |
|---|---|---|
| [Strip plot](dot-strip-plot.md) (univariate scatterplot) | Every observation | n is small. The recommended form at the sample sizes Weissgerber et al. measured |
| [Beeswarm](beeswarm-plot.md) | Every observation, displaced sideways so none is hidden | Same intent as the strip plot, with collisions resolved deterministically rather than by jitter or overlap. Untested |
| [Histogram](histogram.md) | Counts per bin | One variable, enough data, and modality or gaps matter |
| [ECDF](ecdf-plot.md) | Every observation at its value against its rank, as a step function | The question is cumulative: what fraction is below a threshold, or where a quantile sits. No bin width and no bandwidth. Untested |
| [Box plot](boxplot.md) | Five numbers per group | Many groups compared at once, and within-group shape is not the question |
| [Violin plot](violin-plot.md) | A mirrored density estimate | Shape matters across groups, or a mean and its error are encoded on a symmetric continuous mark |
| [Ridgeline](ridgeline-plot.md) | One density estimate per group, stacked and overlapping | Many groups in a known order share one value axis in one figure, with occlusion accepted to get them there. Untested |
| [Gradient plot](gradient-plot.md) | Continuous uncertainty around an estimate | The other alternative [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) tested, and they decline to rank it against the violin |

Histogram-of-histograms has no page; [small-multiples.md](small-multiples.md) covers the device. A page is not a warrant, and a missing page is not a verdict. [beeswarm-plot.md](beeswarm-plot.md), [ridgeline-plot.md](ridgeline-plot.md) and [ecdf-plot.md](ecdf-plot.md) carry a decomposition and cautions, and no experiment in this source set tests any of the three against anything.

Four constraints follow from the evidence rather than from taste:

- **At small n, the points rather than a summary**, on the authors' argument above.
- **A drawn interval is named, and n is stated with it** (Cumming et al.'s rules 1 and 2). Belia et al. show the label is necessary and not sufficient. They asked 473 published authors to set two means "just significantly different," and "only 22% of respondents set the means so the p value was between .025 and .10." The CI group's average and the SE group's differed by 48 units, where the correct answers sit 160 apart. And 31.5% used the just-touching rule, which is wrong for both bar types, in opposite directions.
- **For an inferential comparison, a symmetric continuous encoding outperformed a bar with error bars.** Correll & Gleicher measured that the bar's "false metaphor of containment" made outcomes inside the bar look likelier than equidistant outcomes above it. The effect was absent from all three symmetric encodings. Scope: crowdsourced, low-stakes prediction, 240 participants, no real decisions.
- **Dropped rows are disclosed.** [Song & Szafir (2019)](../studies/song-szafir-2019-missing-data.md) tested time series, not distributions. Information removal "can significantly degrade perceptions of data quality, and confidence" and gave wrong answers when it broke visual continuity. A caller who never noticed the drop, the common case for a plotting library, is untested, as the paper says. The mechanical form is a comparison of input and plotted row counts, which [checks/matplotlib.md](../checks/matplotlib.md) does not yet carry.

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

- ~~"Use a box plot instead of a bar chart."~~ The review usually cited for it puts box plots with bar and line graphs, "only meaningful when there are enough data to summarize," and prefers univariate scatterplots at the measured sample sizes. Matejka & Fitzmaurice's six distributions also share one box plot.
- ~~"Error bars are fine as long as you label them."~~ Belia et al. found the misconceptions above among expert readers of labeled bars.
- ~~"Readers cannot handle an unfamiliar form like a violin."~~ Crowdsourced readers did better on inferential tasks with the unfamiliar symmetric encodings than with the bar and error bar. The authors name a separate cultural cost, "viewers might prefer to see familiar but known suboptimal encodings," which is about preference, not accuracy.
- ~~"Showing the distribution leads readers to better conclusions."~~ The prevalence of summary-only figures is measured, and one summary fitting many distributions holds by construction. The step from those to reader outcomes is `absence of evidence`.

## The failure mode this group invites

A summary stands in for the data, and the reader believes they have seen the distribution. Weissgerber et al.:

> "bar and line graphs are 'visual tables' that transform the reader from an active participant into a passive consumer of statistical information. Without the opportunity for independent appraisal, the reader must rely on the authors' statistical analyses and interpretation of the data."

The choice of summary also does rhetorical work, intended or not: "Showing the SE rather than the SD magnifies the apparent visual differences between groups. This effect is exacerbated when the groups being compared have different sample sizes."

If a reader could not reconstruct roughly how many observations sit behind each mark, and what the drawn interval or width means, the figure asserts more than it shows.

## Types in this index

- [histogram.md](histogram.md)
- [boxplot.md](boxplot.md)
- [violin-plot.md](violin-plot.md)
- [beeswarm-plot.md](beeswarm-plot.md): the strip plot with collisions displaced deterministically
- [ridgeline-plot.md](ridgeline-plot.md)
- [ecdf-plot.md](ecdf-plot.md)
- [density-plot.md](density-plot.md)
- [small-multiples.md](small-multiples.md): one panel per group at shared scales, for any of the forms above
- [dot-strip-plot.md](dot-strip-plot.md): the strip plot, also indexed under [ranking.md](ranking.md)

## See also

- [../concepts/channels.md](../concepts/channels.md): the evidence tier, and why it bears on this group less than on part-to-whole
- [../concepts/evidence-class.md](../concepts/evidence-class.md): the labeling discipline
- [README.md](README.md): the page template and the inheritance rule
