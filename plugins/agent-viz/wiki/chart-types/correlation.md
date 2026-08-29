---
type: index
---

# Correlation

Two or more variables measured on the same units, drawn so the reader can see how they move together.

## Is a relationship what the reader is actually asking about?

Three tests. The first is the one that fails most often.

**Are the variables measured on the same units?** A correlation chart pairs values: one row carries both x and y, for the same thing. Two series that merely share a time index are not paired observations of a unit, they are two time series, and pairing them by date manufactures a relationship out of a filing decision. This is the dual-axis problem wearing different clothes, and the accurate statement of the caution is in [refutations.md](../refutations.md#a-flat-ban-on-dual-axes): "the apparent correlation is a free parameter of your scaling choice." Nobody has shown the twin-axis form harms readers, which is `absence of evidence` rather than a ban, but the free parameter is real either way.

**Is the co-movement the message, or is one variable's level the message?** "Countries with higher x tend to have higher y" is this group. "Which country has the highest y" is ranking, and a sorted bar or dot plot answers it on position along a common scale while a scatterplot answers it by making the reader hunt.

**Is the answer being sought causal?** If so, no chart in this group delivers it. **Correlation is not causation is a claim about inference, not about the chart**: it is not a perceptual finding, no form fixes it, and no form causes it. The chart shows co-movement, which is all it can show. The inference is a separate statement, and the picture does not make it.

A failed test places the question in another group:

| The reader's actual question | Group |
|---|---|
| How big is this one thing? | Magnitude. A bar chart |
| Which is biggest, and in what order? | [Ranking](ranking.md). A sorted bar or dot plot |
| How did this variable move over time? | Change over time. A line chart |
| How is this single variable distributed? | Distribution. A histogram, or a univariate scatterplot when n is small |
| Do these parts add up to a whole? | [Part-to-whole](part-to-whole.md) |
| Two series in different units, both over time | Two stacked panels sharing an x-axis. A [connected scatterplot](connected-scatterplot.md) is the substitute usually proposed for a dual-axis line chart |
| Who is connected to whom? | [Network and topology](network-topology.md) |
| Does x cause y? | Nothing here answers that. **This group** carries the association; the inference is a separate statement |

## What this group costs

**The per-point reading is cheap; the reading the chart is usually drawn for is not the one that was measured.**

Looking up one observation is two readings of position along a common scale, the most accurately read channel in the measured record ([channels.md](../concepts/channels.md)). That part is well supported and rarely the task. The task is almost always the *shape across points*: is there a trend, how tight is it, where are the outliers, does the cloud split. The graphical-perception literature explicitly does not cover that. From [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), p. 531: "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one." The [scope limit](../concepts/channels.md#what-the-ranking-is-not-about) is the authors' own.

**The nearest elementary task the paper does name is direction**, the slope between a pair of points, and it is discussed directly. Direction sits at the **same rank as length and angle**, and the authors add that "there is not enough information to separate the ties." So direction is not one of the accurately read channels, and where it sits among the middle ones was never established. The tie is not an ordering in either direction.

**Aspect ratio is a real design lever here, and the familiar rule does not hold as stated.** The ratio decides which slope differences are visible, so it is a choice made whether or not it is noticed. But "bank to 45 degrees" is **scope-limited, not refuted**, and the stronger word is wrong ([talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md), [refutations.md](../refutations.md#bank-to-45-degrees)):

> "we find that, in general, slope ratio errors are not minimized around 45°"

Three things commonly dropped from a citation of it. Cleveland's model replicates inside the range he sampled and fails only when extrapolated past it. The shift to below 30 degrees belongs to the ANGLE strategy alone, while Cleveland's subjects were instructed to compare heights. And the authors' own summary is deflationary: "the theory of aspect ratio selection is not as simple as it once seemed." What survives constructively is that minimizing predicted slope error "consistently selects flatter, wider aspect ratios" than the banking algorithms, plus the separate finding that a visible baseline nearly eliminates slope-judgment error below 45 degrees and did nothing above it. All of this was measured on pairs of isolated line segments, and the authors name the transfer to real plots as their major limitation.

**These forms do not need a zero baseline, and the exception is built into the rule.** Proportional ink is scoped by mark. The [Urban Institute guide](../sources/urban-institute.md), whose contact is [Jonathan Schwabish](../people/jonathan-schwabish.md), states it in the same breath as its own zero-baseline absolute:

> "It is important to note that other charts types that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero."

`authority-asserted`, and correctly reasoned: nothing in a point's position encodes a quantity by the amount of ink between it and zero. Forcing zero on a scatterplot buys nothing and usually costs the resolution the chart exists for. A [bubble chart](bubble-chart.md) is the exception inside the exception, because its third variable *is* an area encoding.

## Choosing a form

| Form | What the third dimension rides on | Where it applies |
|---|---|---|
| [Scatterplot](scatterplot.md) | Nothing. Two variables, two positions | The default. Two paired quantities and enough observations to see a shape |
| [Bubble chart](bubble-chart.md) | Circular area | A third quantity matters but only roughly, and the least accurate of the measured channels is good enough for it |
| [Connected scatterplot](connected-scatterplot.md) | Path order | Both variables are time series on the same units and the joint trajectory is the point |
| [Correlation matrix](correlation-matrix.md) | Cell color, which carries the coefficient rather than the data | Too many variables to plot every pair, and the job is deciding which pairs are worth a scatterplot |

Three more that get no page for want of any study in this source set, named rather than linked: binned density plots (hexbin or 2D histogram) when the points overplot into a solid mass, small multiples when a categorical variable would otherwise become a third encoding, and a slope chart when there are exactly two time points.

Two constraints that follow from the evidence rather than from taste:

- **Color, shape and faceting carry a third variable more accurately than size does.** Area is read less accurately than angle, and both significantly less accurately than position ([Heer & Bostock](../studies/heer-bostock-2010.md)). For a categorical third variable, size was never a candidate.
- **The aspect ratio is a free choice.** The evidence does not support a specific target, and the direction of the constructive result is flatter and wider than banking produces.

## Justifying the choice

**Defensible, evidence-backed:**

- "I did not force a zero baseline. Proportional ink applies to marks that encode with length or height, and a point does not."
- "The third variable is on color rather than size, because area is measured as less accurate than angle and both as much less accurate than position."
- "I set the aspect ratio deliberately rather than accepting the default. Banking to 45 degrees is a local result that does not extrapolate, and what replaced it is a preference for flatter and wider."

**Defensible, with the label said out loud:**

- "These summary statistics are compatible with radically different pictures, which is true by construction. That readers are actually misled by the summary has not been measured."
- "I chose a connected scatterplot over a dual-axis line chart. That is a widely stated editorial preference, not a measured result, and the case against dual axes has no experiment under it either."

**Not defensible:**

- ~~"Scatterplots are read accurately because they use position."~~ Reading one point's value is a position reading and is well supported. The trend, the tightness and the outliers are not value extraction, and the ranking's authors put that outside its scope themselves.
- ~~"Bank the chart to 45 degrees."~~ Scope-limited to the moderate regime Cleveland sampled. Stated as a general rule it is a local fit reported as a global one.
- ~~"The line goes up, so x drives y."~~ An inference claim wearing a chart's clothes.

## The failure mode this group invites

**Computing the number first and drawing the chart to confirm it.** A correlation coefficient, a regression line and a scatterplot all get produced from the same call, and the plot then reads as decoration on a result that has already been decided.

The sharpest illustration of why that fails is the Datasaurus, and **it has to be cited as an illustration, because that is what it is**. [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) is a construction with no participants, no task and no measurement of comprehension: an annealing method that perturbs one dataset into twelve wildly different ones holding x and y means, x and y standard deviations and Pearson's r to two decimals. It supports *these summary statistics are compatible with radically different data*, which is true by construction and therefore the strongest form of true available, and it supports *so plot the data*. It **does not** support *readers are misled by summary statistics*, *scatterplots produce better conclusions than summary tables*, or any estimate of how often this happens in real data, since the datasets are adversarial by construction rather than sampled. It is the strongest available picture for the point and it is not evidence about readers.

For the empirical claim, [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) is the citation: a review of 703 physiology articles, 85.6% of which included a bar graph of the mean, with the median smallest group size in a figure sitting at 4. Their Fig 1 makes the many-distributions-one-summary point with realistic data and real p-values.

## Types in this index

- [scatterplot.md](scatterplot.md)
- [bubble-chart.md](bubble-chart.md)
- [connected-scatterplot.md](connected-scatterplot.md)
- [correlation-matrix.md](correlation-matrix.md)
- [heatmap.md](heatmap.md), the same grid with any quantity in the cells, indexed primarily under [magnitude.md](magnitude.md)

The connected scatterplot is also a change-over-time chart and appears in that index too, which is the point of [filing by index rather than by directory](README.md#taxonomy-is-an-index-not-a-home).
