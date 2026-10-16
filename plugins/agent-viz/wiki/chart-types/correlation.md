---
type: index
---

# Correlation

Two or more variables measured on the same units, drawn so the reader can see how they move together.

## Is a relationship what the reader is actually asking about?

Three tests. The first fails most often.

**Are the variables measured on the same units?** A correlation chart pairs values, one row carrying x and y for the same thing. Two series that only share a time index are not paired observations, and pairing them by date manufactures a relationship from a filing decision. That is the dual-axis problem, and [refutations.md](../refutations.md#a-flat-ban-on-dual-axes) puts the caution as "the apparent correlation is a free parameter of your scaling choice." No one has shown the twin-axis form harms readers, which is `absence of evidence` rather than grounds for a ban. The free parameter exists either way.

**Is the co-movement the message, or one variable's level?** "Countries with higher x tend to have higher y" is this group. "Which country has the highest y" is ranking, answered on position by a sorted bar or dot plot, where a scatterplot makes the reader hunt.

**Is the answer being sought causal?** No chart here delivers that. Correlation is not causation is a claim about inference, not a perceptual finding, and no form fixes or causes it. The chart shows co-movement and nothing more.

| The reader's actual question | Group |
|---|---|
| How big is this one thing? | [Magnitude](magnitude.md). A bar chart |
| Which is biggest, and in what order? | [Ranking](ranking.md). A sorted bar or dot plot |
| How did this variable move over time? | [Change over time](change-over-time.md). A line chart |
| How is this single variable distributed? | [Distribution](distribution.md). A histogram, or a univariate scatterplot when n is small |
| Do these parts add up to a whole? | [Part-to-whole](part-to-whole.md) |
| Two series in different units, both over time | Two stacked panels sharing an x-axis. A [connected scatterplot](connected-scatterplot.md) is the usual proposed substitute for a dual-axis line chart |
| Who is connected to whom? | [Network and topology](network-topology.md) |
| Does x cause y? | Nothing here answers that. **This group** carries the association |

## What this group costs

Looking up one observation is two readings of position along a common scale, the most accurately read channel ([channels.md](../concepts/channels.md)). That is well supported and rarely the task. The task is the shape across points: trend, tightness, outliers, a cloud that splits. The graphical-perception literature does not cover that. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), p. 531: "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one." The [scope limit](../concepts/channels.md#what-the-ranking-is-not-about) is the authors' own.

**Direction**, the slope between two points, is the nearest elementary task the paper names. It ties with length and angle, and the authors add that "there is not enough information to separate the ties." So direction is not among the accurately read channels, and its place among the middle ones was never established.

**Aspect ratio** decides which slope differences are visible, so it gets chosen whether or not anyone notices. "Bank to 45 degrees" is scope-limited, not refuted ([talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md), [refutations.md](../refutations.md#bank-to-45-degrees)):

> "we find that, in general, slope ratio errors are not minimized around 45°"

Cleveland's model replicates inside the range he sampled and fails only when extrapolated. The shift to below 30 degrees belongs to the ANGLE strategy alone, while Cleveland's subjects were told to compare heights. The authors' own summary: "the theory of aspect ratio selection is not as simple as it once seemed." Minimizing predicted slope error "consistently selects flatter, wider aspect ratios" than the banking algorithms. A visible baseline nearly eliminated slope-judgment error below 45 degrees and did nothing above it. All of this was measured on pairs of isolated line segments, and the authors name transfer to real plots as their major limitation.

**Zero baseline.** These forms do not need one, because proportional ink is scoped by mark. The [Urban Institute guide](../sources/urban-institute.md), whose contact is [Jonathan Schwabish](../people/jonathan-schwabish.md), says so beside its own zero-baseline absolute:

> "It is important to note that other charts types that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."

`authority-asserted`. A point's position does not encode a quantity by the ink between it and zero, so forcing zero costs the resolution the chart exists for. A [bubble chart](bubble-chart.md) is the exception, because its third variable is an area.

## Choosing a form

| Form | What the third dimension rides on | Where it applies |
|---|---|---|
| [Scatterplot](scatterplot.md) | Nothing. Two variables, two positions | The default. Two paired quantities and enough observations to see a shape |
| [Bubble chart](bubble-chart.md) | Circular area | A third quantity that matters only roughly, so the least accurate of the measured channels is good enough |
| [Connected scatterplot](connected-scatterplot.md) | Path order | Both variables are time series on the same units and the joint trajectory is the point |
| [Correlation matrix](correlation-matrix.md) | Cell color, carrying the coefficient rather than the data | Too many variables to plot every pair, and the job is picking which pairs deserve a scatterplot |

No study in this source set covers binned density plots (hexbin or 2D histogram) for points that overplot into a solid mass, small multiples for a categorical third variable, or a [slope chart](slope-chart.md) for exactly two time points.

A categorical third variable rides on color, shape or faceting rather than on size, since hue is the channel for identity ([channels.md](../concepts/channels.md)). A quantitative third variable has no good home: area is read less accurately than angle, and both significantly less accurately than position ([Heer & Bostock](../studies/heer-bostock-2010.md)), and shading ranks lower still. A categorical third variable was never a candidate for size.

## Justifying the choice

**Defensible, evidence-backed:**

- "I did not force a zero baseline. Proportional ink applies to marks that encode with length or height, and a point does not."
- "The categorical third variable is on color rather than size. Hue is the channel for identity, and area is measured as less accurate than angle and both as much less accurate than position."
- "I set the aspect ratio deliberately rather than accepting the default. Banking to 45 degrees is a local result that does not extrapolate, and what replaced it is a preference for flatter and wider."

**Defensible, with the label said out loud:**

- "These summary statistics are compatible with radically different pictures, which is true by construction. That readers are actually misled by the summary has not been measured."
- "I chose a connected scatterplot over a dual-axis line chart. That is a widely stated editorial preference, not a measured result, and the case against dual axes has no experiment under it either."

**Commonly repeated, and the evidence does not support it:**

- ~~"Scatterplots are read accurately because they use position."~~ One point's value is a position reading. Trend, tightness and outliers are not value extraction, and the ranking's authors place them outside its scope.
- ~~"Bank the chart to 45 degrees."~~ A local fit to the moderate regime Cleveland sampled, reported as a global rule.
- ~~"The line goes up, so x drives y."~~ An inference claim, not a reading of the chart.

## The failure mode this group invites

**Computing the number first and drawing the chart to confirm it.** The coefficient, the regression line and the scatterplot come out of one call, and the plot decorates a result already decided.

The Datasaurus illustrates why that fails, and it is not evidence about readers. [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) is a construction with no participants, task or comprehension measure. An annealing method perturbs one dataset into twelve very different ones with the same x and y means, x and y standard deviations and Pearson's r to two decimals. It supports *these summary statistics are compatible with radically different data*, true by construction, and *so plot the data*. It does not support *readers are misled by summary statistics*, *scatterplots produce better conclusions than summary tables*, or any estimate of how often this happens in real data, since the datasets are adversarial rather than sampled.

The empirical claim rests on [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md). Of 703 physiology articles, 85.6% included a bar graph of the mean, and the median smallest group size in a figure was 4. Their Fig 1 makes the many-distributions-one-summary point with realistic data and real p-values.

## Types in this index

- [scatterplot.md](scatterplot.md)
- [bubble-chart.md](bubble-chart.md)
- [connected-scatterplot.md](connected-scatterplot.md): also change over time, and indexed there too, since filing is [by index rather than by directory](README.md#taxonomy-is-an-index-not-a-home)
- [correlation-matrix.md](correlation-matrix.md)
- [heatmap.md](heatmap.md): the same grid with any quantity in the cells, indexed primarily under [magnitude.md](magnitude.md)
- [parallel-coordinates.md](parallel-coordinates.md): many variables as parallel axes, one polyline per row
