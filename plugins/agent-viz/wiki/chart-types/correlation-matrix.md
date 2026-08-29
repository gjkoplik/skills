---
type: chart-type
relationships: [correlation]
aliases: [Correlation matrix, Correlogram, Corrplot]
---

# Correlation matrices

A square grid with the same variables on both axes, one cell per pair, each cell carrying that pair's correlation coefficient, usually as color.

**Also called a correlogram or a corrplot.** [Wilke](../sources/wilke-fundamentals.md) defines the first at primary: "Visualizations of correlation coefficients are called correlograms." **"Corrplot" is still in circulation with nothing here defining it**, and it is the name of an R package as often as a form.

**One collision, and it is not a naming nuisance.** The same grid is also drawn with a **scatterplot** in every cell rather than a colored coefficient, and that object is called a **scatterplot matrix** or a **SPLOM**; the two get called by each other's names freely. They are different charts. A scatterplot matrix shows the data. A colored correlation matrix shows one number per pair and nothing else, and the number is exactly the one that does not determine the picture, which is the Datasaurus argument below. No source in this corpus defines either term: [Schwabish](../sources/schwabish.md) files a **Correlation Matrix** under Relationship, with the membership verified from the book's contents pages and his prose unread, and there is no scatterplot-matrix entry anywhere in the corpus. The names are recorded here rather than adjudicated.

The general case, color on a grid whatever the cells hold, is a [heatmap](heatmap.md), and this page does not restate that argument. That page also carries the filing tangle around the two names. What follows here is only what comes from the cells being correlation coefficients.

## When to reach for it, and when not

**The form applies where** there are enough variables that plotting every pair is not an option, they are measured on the same units, and the job is to decide which pairs are worth a real chart. It is a screening device whose output is a shortlist of scatterplots.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| What does the relationship between these two variables look like? | [Scatterplot](scatterplot.md). One coefficient is compatible with radically different pictures |
| There are four variables | The six scatterplots. A grid of four cells is a table with color on it |
| The exact coefficients are the deliverable | [A table](tables.md). Numbers read exactly, and a small table needs no legend to decode |
| The relationship might not be monotone | [Scatterplot](scatterplot.md). The twelve Datasaurus datasets, including a dinosaur and a star, all share Pearson's r to two decimals ([matejka-2017-datasaurus.md](../studies/matejka-2017-datasaurus.md)) |
| The cells are counts, rates or measurements rather than coefficients | A [heatmap](heatmap.md). Everything below about symmetry, the diagonal and the bounded midpoint stops holding |
| Which variable drives which? | Nothing here answers that. [correlation.md](correlation.md) states the limit and it is a limit on inference, not on the chart |
| Who is connected to whom? | [Network and topology](network-topology.md). An [adjacency matrix](adjacency-matrix.md) is the same layout carrying edges rather than coefficients |

## Structural decomposition

| Slot | |
|---|---|
| Data | n observations across k variables. **The drawn unit is a pair of variables, not an observation** |
| Transform | **A correlation coefficient per pair**, usually Pearson's r. This is the whole chart: k(k-1)/2 numbers standing in for an n-by-k table |
| Geometry | One cell per pair, k by k. Sometimes a circle or an ellipse whose size or shape also tracks the coefficient |
| Scale | Coefficient in the interval from -1 to 1, mapped to cell color on a diverging scale pivoting at zero |
| Coordinates | Cartesian, discrete on both axes, **with the same ordering on both** |
| Guides | Both variable axes, a color legend with the midpoint labeled, and the n and the coefficient used stated somewhere |

## What follows from the cells being coefficients

All of this is definitional and carries no evidence label. It is also most of what distinguishes this chart from any other grid of colored cells.

**It is symmetric, so half of it is redundant.** The coefficient for (x, y) is the coefficient for (y, x), so the two triangles are the same numbers drawn twice. Nothing is lost by drawing one triangle, and what is gained is space for the labels.

**The diagonal is 1 by construction.** It carries no information about the data, and on a full-range color scale it is the strongest ink in the figure, so the most conspicuous marks on the chart are the ones guaranteed in advance. Blanked, or left as decoration.

**The scale is bounded, and its midpoint means something.** Coefficients run from -1 to 1 and zero is not an arbitrary place on that interval, it is the absence of the thing being measured, with sign on either side. That makes a **diverging colormap a property of the data here rather than a style preference**, which is unusual: on most colored grids the choice is a judgment call. Two inventory topics fall out of it directly, both `authority-asserted`:

- **Colormap class matched to data type** ([inventory.md](../inventory.md) topic 23). matplotlib's own guidance: "Diverging: change in lightness and possibly saturation of two different colors that meet in the middle at an unsaturated color; should be used when the information being plotted has a critical middle value, such as topography or when the data deviates around zero" ([matplotlib.md](../sources/matplotlib.md)). A correlation coefficient deviates around zero by construction.
- **The midpoint is set explicitly and labeled** ([inventory.md](../inventory.md) topic 32). The Urban Institute: "The center of the diverging palette should always be labeled to avoid confusing the reader" ([urban-institute.md](../sources/urban-institute.md)). [Observable Plot](../sources/observable-plot.md) makes it typed rather than incidental, pivoting diverging scales at zero by default.

**The color domain is a free parameter.** Spanning the full interval from -1 to 1 makes two figures comparable; fitting the domain to the observed range makes a matrix of weak correlations look like a matrix of strong ones. That follows from the scale rather than from a study, and nobody in this corpus has measured what the difference does to a reader.

## Channels

**Cell color for the magnitude**, which is shading and color saturation, the tasks at the bottom of the Cleveland & McGill ordering. [channels.md](../concepts/channels.md) records everything down there as `authority-asserted`, reasoned from psychophysics rather than measured. So the channel this chart puts its one number on is both the least accurate in the ordering and the part of the ordering with the least behind it.

**Hue for the sign.** On a diverging map, which side of zero a cell falls on is carried by hue, and hue used for identity is the job [channels.md](../concepts/channels.md) says hue is actually good at and that no accuracy ordering scores. The practical shape of that: the chart supports "positive or negative" far better than it supports "how strong".

**Position on two discrete non-aligned scales, for identity only.** Row and column say which pair a cell is, not how large anything is, the same way they do on an [adjacency matrix](adjacency-matrix.md).

All inherited, with the standing caveat that the mapping from this chart to those channels is conjecture rather than measurement.

## What it is measurably good at

**Nothing. No study in this corpus tests a correlation matrix.**

The nearest measured neighbor is the [adjacency matrix](adjacency-matrix.md), where [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) do measure a grid of cells against an alternative. It is the same layout and a different chart: those cells carry the presence of an edge, which is not a magnitude, and the tasks tested are network tasks. Nothing carries over except the ordering argument below, which is structural in both.

## What it is measurably bad at

Nothing measured on the form. The inherited exposure is the color channel, above, and it is the one the chart cannot avoid, since the coefficient has nowhere else to go.

One more: **a banded colormap invents groups.** [Ware, Stone & Szafir (2023)](../studies/ware-2023-rainbow-colormaps.md), a position piece rather than an experiment, concede the point directly: "people tend to read meaning into color categories even when they are simply artifacts of the colormap." On this chart that means an apparent tier of strong correlations and an apparent tier of weak ones, drawn by the colormap rather than found in the data.

## What is contested

Nothing native. There is no record here to disagree with itself.

The disagreement in the corpus is about filing, and it is small. [Schwabish](../sources/schwabish.md) files Correlation Matrix under Relationship, which maps onto the FT's Correlation. The FT has no correlation-matrix entry and splits heatmaps instead, XY heatmap under Correlation and heat map under Spatial. Two schemes descended from the same 2014 poster cut the color-grid family in different places, which is `authority-asserted` on both sides and says nothing about how either chart reads.

## The failure mode it invites

**Scanning the grid for the darkest cells.** The chart lays out many coefficients at once and gives no visual difference between one that was predicted and one that was noticed, so the extreme cells are the ones that get reported. That is multiple comparisons done by eye. It follows from the structure of the chart, it is `authority-asserted` at most, and there is no result in this corpus measuring either how often readers do it or what it costs. The defense named here is stating how many coefficients are on the chart, which is k(k-1)/2 and is usually larger than people expect.

**Treating the cell as the finding.** The cells are exactly the summary statistic that does not determine the shape of the data. [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) hold x and y means, x and y standard deviations and Pearson's r at -0.06 to two decimals across twelve wildly different datasets. That construction supports *these summary statistics are compatible with radically different data*, which is true by construction and therefore the strongest form of true available, and it supports *so plot the data*. It **does not** support *readers are misled by summary statistics*, and it has no participants, no task and no measurement of comprehension. [correlation.md](correlation.md) keeps the two apart. For the empirical claim, [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) is the citation with data under it.

**Shipping the default ordering.** Row and column order is a free parameter and it is the whole of the visible structure: blocks of related variables appear only if the ordering puts them next to each other. Column order in the source file is arbitrary with respect to the data. [adjacency-matrix.md](adjacency-matrix.md) makes this argument in full, and it transfers directly, with one difference in this chart's favor: the ordering can be derived from the coefficients themselves by clustering or seriation, so the input for a structural ordering is already on the chart.

**Reading adjacency as similarity.** Two neighboring rows are neighbors because of the chosen ordering, which may be alphabetical. Same trap, same page.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies, and the reason is structural rather than a gap in coverage: the one number this chart carries sits on the channel with the least measurement behind it, and no study here tests the form.

**Defensible, with the label said out loud:**

- "The colormap is diverging with the midpoint pinned at zero and labeled, because the coefficient is bounded and zero is a meaningful value rather than a convenient one. A plotting library's own guidance, a chart grammar's default and a style guide all scope colormap class this way, and none of them ran an experiment."
- "The domain is fixed from -1 to 1 rather than fitted to the observed range, so this figure is comparable with the next one and weak correlations look weak."
- "Only the lower triangle is drawn and the diagonal is blank. The upper triangle is the same numbers and the diagonal is 1 by construction."
- "Ordered by cluster rather than by the column order in the file, so the blocks are a property of the data rather than of the spreadsheet."
- "This is a screen for deciding which pairs to plot, and the pairs it picked out are plotted as scatterplots in the next figure."

**Commonly repeated, and the evidence does not support it:**

- ~~"The matrix shows the relationships among all the variables."~~ It shows one summary of each pair, and a summary does not determine the picture. That is secure by construction, not a claim about readers.
- ~~"Color makes the pattern obvious."~~ Magnitude on shading and saturation sits at the bottom of the measured ordering, and that end of the ordering is asserted rather than measured. Nobody has tested this form at all.
- ~~"The dark cells are the real relationships."~~ Picking the extremes out of a grid of many coefficients is a selection, and the chart draws the selected and the unselected the same way.
- ~~"r near zero means there is nothing there."~~ The dinosaur, the star and the parallel lines all sit at r = -0.06.

## See also

- [correlation.md](correlation.md) — the group, including the Datasaurus and the causal-inference limit in full
- [scatterplot.md](scatterplot.md) — the chart this one is a screen for, and the one that shows the data
- [adjacency-matrix.md](adjacency-matrix.md) — the same layout carrying edges, and the ordering argument with studies behind it
- [../studies/matejka-2017-datasaurus.md](../studies/matejka-2017-datasaurus.md) — what a coefficient does not pin down
- [heatmap.md](heatmap.md) — the general color-grid argument, and the names this one collides with
- [../concepts/channels.md](../concepts/channels.md) — the color channel this chart is stuck with
