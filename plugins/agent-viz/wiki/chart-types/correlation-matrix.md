---
type: chart-type
relationships: [correlation]
aliases: [Correlation matrix, Correlogram, Corrplot]
---

# Correlation matrices

A square grid with the same variables on both axes, one cell per pair, each cell carrying that pair's correlation coefficient, usually as color.

[Wilke](../sources/wilke-fundamentals.md) calls it a correlogram: "Visualizations of correlation coefficients are called correlograms." "Corrplot", undefined here, names an R package as often as a form. The same grid with a scatterplot in each cell is a **scatterplot matrix** (SPLOM), and the two names get swapped freely. A scatterplot matrix shows the data. A correlation matrix shows one number per pair, which does not determine the picture. No source here defines either name. [Schwabish](../sources/schwabish.md) files Correlation Matrix under Relationship (contents pages only, prose unread), and no source has a scatterplot-matrix entry. Colored grids in general, and the filing tangle, are on [heatmap](heatmap.md).

## When to reach for it, and when not

The form is defined for too many same-unit variables to plot every pair. It screens for which pairs deserve a chart, and its output is a shortlist of scatterplots.

| The question | Alternative |
|---|---|
| What does the relationship between these two variables look like? | [Scatterplot](scatterplot.md). One coefficient fits radically different pictures |
| There are four variables | The six scatterplots. A four-by-four grid with six distinct cells is a table with color on it |
| The exact coefficients are the deliverable | [A table](tables.md), which reads exactly and needs no legend |
| The relationship might not be monotone | [Scatterplot](scatterplot.md). The twelve Datasaurus datasets, a dinosaur and a star among them, share Pearson's r to two decimals ([matejka-2017-datasaurus.md](../studies/matejka-2017-datasaurus.md)) |
| The cells are counts, rates or measurements | A [heatmap](heatmap.md). The symmetry, diagonal and bounded midpoint below no longer hold |
| Which variable drives which? | Nothing here. [correlation.md](correlation.md) states the limit, which is on inference, not the chart |
| Who is connected to whom? | [Network and topology](network-topology.md). An [adjacency matrix](adjacency-matrix.md) is the same layout carrying edges |

## Structural decomposition

| Slot | |
|---|---|
| Data | n observations across k variables. The drawn unit is a pair of variables, not an observation |
| Transform | A correlation coefficient per pair, usually Pearson's r: k(k-1)/2 numbers standing in for an n-by-k table |
| Geometry | One cell per pair, k by k. Sometimes a circle or ellipse whose size or shape also tracks the coefficient |
| Scale | Coefficient from -1 to 1, to cell color on a diverging scale pivoting at zero |
| Coordinates | Cartesian, discrete on both axes, with the same ordering on both |
| Guides | Both variable axes, a color legend with the midpoint labeled, and the n and coefficient type stated |

## What follows from the cells being coefficients

All definitional, with no evidence label.

The grid is symmetric, so one triangle carries everything and the other frees room for labels.

The diagonal is 1 by construction, so the strongest ink on a full-range scale says nothing about the data. It is usually blanked.

The scale is bounded, and zero means no correlation, with sign on either side. That makes a diverging colormap a property of the data here rather than a style choice. Two inventory topics follow, both `authority-asserted`:

- **Colormap class matched to data type** ([inventory.md](../inventory.md) topic 23). matplotlib: "Diverging: change in lightness and possibly saturation of two different colors that meet in the middle at an unsaturated color; should be used when the information being plotted has a critical middle value, such as topography or when the data deviates around zero" ([matplotlib.md](../sources/matplotlib.md)).
- **The midpoint set and labeled** ([inventory.md](../inventory.md) topic 32). The Urban Institute: "The center of the diverging palette should always be labeled to avoid confusing the reader" ([urban-institute.md](../sources/urban-institute.md)). [Observable Plot](../sources/observable-plot.md) pivots diverging scales at zero by default.

The color domain is a free parameter. Fitting it to the observed range rather than -1 to 1 makes weak correlations look strong, an effect nobody here has measured.

## Channels

Magnitude is on cell color, as shading and saturation, the bottom of the Cleveland & McGill ordering. [channels.md](../concepts/channels.md) records that end as `authority-asserted`, reasoned from psychophysics rather than measured. So the chart's one number sits on the least accurate and least tested channel.

Sign is on hue, used for identity, a job hue does well and no accuracy ordering scores. The chart supports "positive or negative" far better than "how strong".

Row and column give identity only, as on an [adjacency matrix](adjacency-matrix.md). The mapping from this chart to those channels is conjecture, not measurement.

## What it is measurably good at

No study in this corpus tests the form. [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) test the same layout as an [adjacency matrix](adjacency-matrix.md), but its cells carry edges rather than magnitudes, on network tasks. Only the ordering argument carries over.

## What it is measurably bad at

Nothing measured on the form. A banded colormap invents groups. [Ware, Stone & Szafir (2023)](../studies/ware-2023-rainbow-colormaps.md), a position piece rather than an experiment, concede that "people tend to read meaning into color categories even when they are simply artifacts of the colormap." Here that means tiers of strong and weak correlations that come from the colormap, not the data.

## What is contested

Nothing native to the form. The disagreement is over filing. [Schwabish](../sources/schwabish.md) files Correlation Matrix under Relationship, matching the FT's Correlation. The FT has no correlation-matrix entry and splits heatmaps between Correlation (XY heatmap) and Spatial. Both schemes descend from the same 2014 poster, both are `authority-asserted`, and neither bears on how the chart reads.

## The failure mode it invites

**Reporting the darkest cells.** A predicted coefficient and a noticed one look the same, so the extremes get reported. That is multiple comparisons by eye, `authority-asserted` at most and unmeasured. The named defense is stating the count shown, k(k-1)/2, usually more than people expect.

**Treating the cell as the finding.** [Matejka & Fitzmaurice (2017)](../studies/matejka-2017-datasaurus.md) hold means, standard deviations and Pearson's r (-0.06) fixed to two decimals across twelve very different datasets. That shows the statistics fit radically different data, so the data should be plotted. It has no participants, so it does not show that readers are misled. [correlation.md](correlation.md) keeps the two apart. For the empirical claim, [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) is the citation with data under it.

**Shipping the default ordering.** Related variables form blocks only when the ordering puts them together, and file order is arbitrary. [adjacency-matrix.md](adjacency-matrix.md) makes the argument in full, including the twin failure of reading alphabetical neighbors as similar. Here the ordering can come from the coefficients themselves, by clustering or seriation.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing qualifies. The one number sits on the least-measured channel, and no study tests the form.

**Defensible, with the label said out loud:**

- "The colormap is diverging with the midpoint pinned at zero and labeled, because the coefficient is bounded and zero is a meaningful value rather than a convenient one. A plotting library's own guidance, a chart grammar's default and a style guide all scope colormap class this way, and none of them ran an experiment."
- "The domain is fixed from -1 to 1 rather than fitted to the observed range, so this figure is comparable with the next one and weak correlations look weak."
- "Only the lower triangle is drawn and the diagonal is blank. The upper triangle is the same numbers and the diagonal is 1 by construction."
- "Ordered by cluster rather than by the column order in the file, so the blocks are a property of the data rather than of the spreadsheet."
- "This is a screen for deciding which pairs to plot, and the pairs it picked out are plotted as scatterplots in the next figure."

**Commonly repeated, and the evidence does not support it:**

- ~~"The matrix shows the relationships among all the variables."~~ It shows one summary per pair, which does not determine the picture.
- ~~"Color makes the pattern obvious."~~ Shading and saturation sit at the asserted bottom of the ordering, and the form is untested.
- ~~"The dark cells are the real relationships."~~ Picking extremes is a selection, and the chart draws selected and unselected cells alike.
- ~~"r near zero means there is nothing there."~~ The dinosaur, the star and the parallel lines all sit at r = -0.06.

## See also

- [correlation.md](correlation.md): the group, the Datasaurus and the causal-inference limit
- [scatterplot.md](scatterplot.md): the chart this one screens for
- [adjacency-matrix.md](adjacency-matrix.md): the same layout carrying edges, and the ordering argument with studies
- [../studies/matejka-2017-datasaurus.md](../studies/matejka-2017-datasaurus.md): what a coefficient does not pin down
- [heatmap.md](heatmap.md): the general color-grid argument and the name collisions
- [../concepts/channels.md](../concepts/channels.md): the color channel this chart is stuck with
