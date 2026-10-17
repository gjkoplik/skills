---
type: chart-type
relationships: [correlation]
aliases: [Scatterplot]
---

# Scatterplot

One point per observation, positioned by two quantitative variables on two axes.

## When to reach for it, and when not

The form is defined for units carrying both values, a question about the joint distribution's shape (trend, spread, outliers, clusters, gaps), and enough points for a shape to mean something. Association read off six points is a statistical claim the chart does not make.

| The question | Alternative |
|---|---|
| How big is this one thing, or which is biggest? | Bar or dot plot, sorted |
| How did this variable move over time? | Line chart |
| How is one variable distributed? | Histogram, or a univariate scatterplot at small n. [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) prefer the latter at the group sizes they measured (median minimum of 4), where "boxplots and histograms would be difficult to interpret" |
| Two series in different units, both over time | Two stacked panels sharing an x-axis, or a [connected scatterplot](connected-scatterplot.md) |
| The points overplot into a solid mass | A binned density plot, hexbin or 2D histogram |
| A third variable also matters | Color or faceting first. A [bubble chart](bubble-chart.md) only if it is quantitative and rough precision will do |
| Does x cause y? | No chart. It shows co-movement |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, two quantitative values for the same unit |
| Transform | None. A fitted line, smoother or density estimate is an added layer with its own transform |
| Geometry | Point |
| Scale | Each variable to one spatial axis, usually linear and usually without a zero constraint |
| Coordinates | Cartesian |
| Guides | Two axes with labels and units. A legend only once a third variable is encoded |

Unlike a bar chart of means, a box plot or a histogram, it puts no computed statistic between the reader and the rows. That is definitional, not a finding about readers.

## Channels

Both axes are position along a common scale, the most accurately read channel in [channels.md](../concepts/channels.md), inherited since no study tests a scatterplot itself. That covers reading one point's values. Trend, tightness, outliers and clusters are shape judgments. [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) restrict their ordering to value extraction, p. 531: "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory." See the [scope limit](../concepts/channels.md#what-the-ranking-is-not-about).

The nearest elementary task is direction, the slope between two points. The paper ranks it level with length and angle: "at the moment there is not enough information to separate the ties." Any ordering of the three comes from a later table that [calls itself](../people/william-cleveland.md) "a tentative working hypothesis."

## What is measured

No study in this corpus tests the form itself. Under overplotting, apparent density depends on marker size, alpha and draw order, and the cost to readers is `absence of evidence`. Finding one named point is visual search, which the ranking does not score.

Aspect ratio, which decides which slope differences are visible, is `contested`. "Bank to 45 degrees" is scope-limited, not refuted ([Talbot, Gerth & Hanrahan 2012](../studies/talbot-2012-slope-ratio.md); [refutations.md](../refutations.md#bank-to-45-degrees)): "In general, slope ratio errors are not minimized around 45°". Cleveland's model replicates inside his sampled range, and the shift below 30 degrees belongs to one of two strategies subjects used. The replacement is flatter and wider than banking algorithms produce. A visible baseline nearly eliminated error below 45 degrees and did nothing above. The stimulus was two isolated line segments, and the authors name transfer to real plots as the major limitation.

## The failure mode it invites

**Reading a trend line as the finding and the points as texture.** The fitted line comes with the plot and looks like a conclusion. `authority-asserted`.

**Leaning on the Datasaurus.** [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) is a construction with no participants. It shows one set of summary statistics fits radically different pictures, and nothing about readers. See the [correlation index](correlation.md#the-failure-mode-this-group-invites).

**The library's default aspect ratio on a slope-comparison figure**, which decides which differences are visible.

## Justifying the choice

**Defensible, evidence-backed:**

- "Both variables are on position along a common scale, which is the most accurately read channel measured. That covers reading a point's values; the trend judgment is a different task the ranking does not cover."
- "I set the aspect ratio rather than taking the default. The 45-degree rule is a local result that does not extrapolate, and the replacement guidance is flatter and wider."

**Defensible, with the label said out loud:**

- "I drew the points rather than a bar of the mean, because a summary is compatible with many different distributions. That is true by construction. Whether readers are actually misled by the summary is a separate question, and [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) is the citation with data behind it."
- "I used transparency and jitter for overplotting. Practitioner convention; nobody in this source set has measured what overplotting costs."
- "No zero baseline. A newsroom taxonomy, a chart tool and a style guide scope proportional ink to marks that encode by length or height, none of them tested it, and one plotting library forces zero on every quantitative axis regardless of mark."

**Commonly repeated, and the evidence does not support it:**

- ~~"Scatterplots are the most accurate chart type because they use position twice."~~ The ranking scores reading a value off a mark, not seeing a relationship.
- ~~"The Datasaurus proves people are fooled by summary statistics."~~ It has no participants. It proves the statistics do not determine the picture.
- ~~"The correlation is strong, so the effect is real."~~ An inference claim, not a property of the chart.

## See also

- [correlation.md](correlation.md): the group, with the aspect-ratio and zero-baseline positions in full
- [bubble-chart.md](bubble-chart.md): a third variable on area
- [../concepts/channels.md](../concepts/channels.md): the inherited evidence and its scope limit
