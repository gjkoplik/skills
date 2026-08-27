---
type: chart-type
relationships: [correlation]
aliases: [Scatterplot]
---

# Scatterplot

One point per observation, positioned by two quantitative variables on two axes.

## When to reach for it, and when not

**Reach for it when** each row of your data is a unit carrying both values, the question is about the shape of the joint distribution (trend, spread, outliers, clusters, gaps), and there are enough points that a shape is a meaningful thing to look at. A scatterplot of six points shows the reader six points; any claim about association from those six is a statistical claim the chart does not make.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| How big is this one thing, or which is biggest? | Bar or dot plot. Position along a common scale, sorted, instead of a hunt through a cloud |
| How did this variable move over time? | Line chart. Time on an axis rather than implied |
| How is one variable distributed? | Histogram, or a univariate scatterplot at small n. [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) prefer the latter below roughly a dozen points, where "boxplots and histograms would be difficult to interpret" |
| Two series in different units, both over time | Two stacked panels sharing an x-axis, or a [connected scatterplot](connected-scatterplot.md) |
| The points overplot into a solid mass | A binned density plot, hexbin or 2D histogram. Once marks overlap, the ink stops being one-per-observation |
| A third variable also matters | Color or faceting first. [Bubble chart](bubble-chart.md) only if the third variable is quantitative and rough precision will do |
| Does x cause y? | Nothing does. The chart shows co-movement, and the causal claim is yours to make and defend separately |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, carrying two quantitative values for the same unit |
| Transform | None. This is the rare chart that draws the data as given. Any fitted line, smoother or density estimate is an added layer with its own transform |
| Geometry | Point |
| Scale | Each variable maps to one spatial axis, usually linearly and usually without a zero constraint |
| Coordinates | Cartesian |
| Guides | Two axes with labels and units. Gridlines optional; a legend only once a third variable is encoded |

The empty transform slot is what distinguishes it from most of this wiki. A bar chart of means, a box plot and a histogram all put a computed statistic between the reader and the rows. A scatterplot does not, which is the whole of its structural argument and is `definitional`, not a finding about readers.

## Channels

**Both axes are position along a common scale**, the most accurately read channel in the measured record. Inherited from [channels.md](../concepts/channels.md), not restated here as a native result: no study has tested a scatterplot as an artifact.

That inheritance covers less than it looks like. What position accuracy buys is *reading one point's values off the axes*, and that is almost never why the chart was drawn. The trend, the tightness, the outliers and the clusters are shape judgments, and [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) restrict their ordering to accuracy of value extraction explicitly, p. 531: "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory." See the [scope limit](../concepts/channels.md#what-the-ranking-is-not-about).

**The elementary task nearest to reading a scatterplot is direction**, meaning the slope between a pair of points, and the paper does discuss it directly. Direction sits at the **same rank as length and angle**, with the authors' note that "at the moment there is not enough information to separate the ties." Two consequences worth keeping: direction is not one of the accurately read channels, and its standing relative to length and angle has never been established. Anyone ordering those three is reading a later table, and [that one calls itself](../people/william-cleveland.md) "a tentative working hypothesis."

## What it is measurably good at

**Value lookup on either axis**, inherited from the position result, with the caveat above that this is rarely the task.

**Nothing else has been measured.** No study in this source set tests the scatterplot as a form: not against a table, not against a summary, not against a binned density plot. What can be said without measurement, because it follows from the decomposition, is that the chart interposes no statistic between the reader and the rows.

## What it is measurably bad at

**Nothing has been measured here either.** The usual criticisms are plausible and untested in this corpus:

- **Overplotting.** Once points overlap, apparent density is a function of marker size, alpha and draw order rather than of the data. This follows from the geometry, and what it costs a reader is unmeasured. `absence of evidence`.
- **Many points, one lookup.** Finding a named observation in a cloud is a visual search task; the channel ranking scores value extraction and does not bear on search at all.

## What is contested

**Aspect ratio.** The ratio decides which slope differences are visible, so it is a design choice being made whether or not anyone makes it. What is contested is the rule: "bank to 45 degrees" is **scope-limited, not refuted** ([Talbot, Gerth & Hanrahan 2012](../studies/talbot-2012-slope-ratio.md); [refutations.md](../refutations.md#bank-to-45-degrees)). "In general, slope ratio errors are not minimized around 45°", Cleveland's model replicates inside the range he sampled, the shift below 30 degrees belongs to only one of two strategies subjects used, and the constructive replacement is a direction rather than a number: flatter and wider than banking algorithms produce. The authors also found a visible baseline nearly eliminates slope-judgment error below 45 degrees and does nothing above it, and they name transfer to real plots as their study's major limitation, since the stimulus was two isolated line segments.

## The failure mode it invites

**Reading a trend line as the finding and the points as texture.** The fitted line arrives from the same function call as the plot and looks like a conclusion. `authority-asserted`.

The sharpest illustration is the Datasaurus, which belongs here with its status attached: [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) is a **construction, not an experiment**. No participants, no task, no measurement of comprehension. It establishes that one set of summary statistics is compatible with radically different pictures, which is true by construction, and it does not establish anything about what readers do. Full treatment on the [correlation index](correlation.md#the-failure-mode-this-group-invites).

**Letting the software pick the aspect ratio for a slope-comparison figure.** The default is a choice about which differences the reader can see, made by whoever wrote the plotting library.

## Justifying the choice

**Defensible, evidence-backed:**

- "Both variables are on position along a common scale, which is the most accurately read channel measured. That covers reading a point's values; the trend judgment is a different task the ranking does not cover."
- "No zero baseline. Proportional ink is scoped to marks that encode by length or height, and a point is not one."
- "I set the aspect ratio rather than taking the default. The 45-degree rule is a local result that does not extrapolate, and the replacement guidance is flatter and wider."

**Defensible, with the label said out loud:**

- "I drew the points rather than a bar of the mean, because a summary is compatible with many different distributions. That is true by construction. Whether readers are actually misled by the summary is a separate question, and [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) is the citation with data behind it."
- "I used transparency and jitter for overplotting. Practitioner convention; nobody in this source set has measured what overplotting costs."

**Not defensible:**

- ~~"Scatterplots are the most accurate chart type because they use position twice."~~ The premise is inherited and fine. The conclusion is about a task nobody measured: the ranking scores reading a value off a mark, not seeing a relationship.
- ~~"The Datasaurus proves people are fooled by summary statistics."~~ It has no participants. It proves the statistics do not determine the picture, which is a different and fully secure claim.
- ~~"The correlation is strong, so the effect is real."~~ An inference claim, not a property of the chart.

## See also

- [correlation.md](correlation.md) — the group argument, including the aspect-ratio and zero-baseline positions in full
- [bubble-chart.md](bubble-chart.md) — the same chart with a third variable on area, and what that costs
- [../concepts/channels.md](../concepts/channels.md) — the evidence this page inherits, and the scope limit that matters most here
