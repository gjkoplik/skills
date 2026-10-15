---
type: chart-type
relationships: [magnitude, correlation]
aliases: [Calendar heatmap, Heat map, Heatmap, Matrix chart, Tile chart, XY heatmap]
---

# Heatmaps

A grid of equal cells, with two categorical or ordered keys along the axes and one quantitative value per cell encoded in color.

Also called a matrix or tile chart. Variants are the XY heatmap (both keys ordered), the calendar heatmap (day-of-week by week-of-year) and the correlation matrix (one list of variables crossed with itself). [Schwabish](../sources/schwabish.md) files Heatmap under Comparing Categories and Correlation Matrix under Relationship (contents pages). The [FT Visual Vocabulary](../sources/ft-visual-vocabulary.md) puts an XY heatmap under Correlation, a heat map under Spatial and a Calendar heatmap under Change over Time. So one name carries four filings across two schemes, plus a fifth under another name, which fits the moral on Schwabish's page: these taxonomies are retrieval aids. It is indexed under [magnitude](magnitude.md) because the cell value is a size comparison.

Two other things share the name. A [choropleth map](choropleth-map.md) is loosely called a heat map, but its geometry comes from a base geography. A density heatmap is a two-dimensional histogram over binned continuous coordinates, with counts in the cells. Nothing in this wiki settles which one the bare word "heatmap" means. This page covers the grid of keyed cells.

## When to reach for it, and when not

The form is defined for a complete cross-tabulation of two keys, read for where highs and lows sit or for block structure, with approximate magnitudes enough. It shows every value at once, with no occlusion.

| The question | Alternative |
|---|---|
| How big is each of these, and by how much? | [Bar chart](bar-chart.md). Position along a common scale rather than color |
| What is the rank order? | [Ranking](ranking.md). Color does not support ordering by eye the way position does |
| There is only one key | [Bar chart](bar-chart.md) or [lollipop chart](lollipop-chart.md). A one-row heatmap wastes the accurate channel |
| The reader needs the numbers | [Tables](tables.md). A table with shaded cells keeps the digits |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). A grid asserts no total |
| Where is this? | [Spatial](spatial.md). A [choropleth](choropleth-map.md) puts the value where its thing is |
| Which nodes connect to which? | [Adjacency matrix](adjacency-matrix.md), this form applied to a graph |
| Do these two variables move together, observation by observation? | [Correlation](correlation.md). A [scatterplot](scatterplot.md) shows the observations; a correlation matrix shows one number per pair |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (row key, column key) pair, carrying one value |
| Transform | An ordering for the rows and one for the columns. Often an aggregation into the cell, sometimes a per-pair statistic such as a correlation |
| Geometry | One rectangle per key pair, all the same size |
| Scale | Value to fill color, on a sequential, diverging or binned ramp |
| Coordinates | Cartesian, discrete on both axes |
| Guides | Two key axes, and a colorbar or legend with units. A diverging ramp also needs its midpoint labeled |

Every cell is the same size in the same place whatever the values, so color is the only channel carrying magnitude. A [choropleth](choropleth-map.md) shares this, with the extent fixed by geography instead of a grid.

The row and column ordering is a free parameter that decides the picture. A clustered order shows blocks, and an alphabetical one shows noise. [adjacency-matrix.md](adjacency-matrix.md) makes the full argument for graphs, where the ordering "sits where a layout algorithm sits for a node-link diagram", and an adjacency matrix is a heatmap of a graph. A default sort order is a decision made by whatever produced the dataframe.

## Channels

Color carries the magnitude. Position carries only identity. The step from "this chart puts the reader on that channel" to an accuracy number is conjecture in the source literature. [channels.md](../concepts/channels.md) separates two defects that "color is the worst channel" blurs.

Ordered lightness or saturation is low-accuracy for magnitude, and that is measured. Shading and color saturation share the bottom rank of the 1984 Cleveland & McGill table, below area and volume. The 1985 table keeps saturation and density near the bottom and adds hue below them. A heatmap supports "more here than there", not "twice as much there as here".

Hue is unsuited to magnitude, a different defect. The 1984 paper leaves hue off the list because it has no unambiguous order from small to large. The remedy for a rainbow is a ramp whose lightness moves monotonically. [matplotlib](../sources/matplotlib.md): "Researchers have found that the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue."

The colormap class matches the data type: sequential for ordered values, diverging for one with a critical middle, qualitative only for unordered ones ([inventory.md](../inventory.md) topic 23, `authority-asserted` from matplotlib's documentation). A diverging ramp's midpoint asserts which value is neutral, and topic 32 records the labeling rule as `authority-asserted`, from the Urban Institute: "The center of the diverging palette should always be labeled to avoid confusing the reader." A correlation matrix has a true midpoint at zero.

[Ware, Stone & Szafir (2023)](../studies/ware-2023-rainbow-colormaps.md) is a Visualization Viewpoints article with no experiment, participants or data. It argues the blanket rainbow ban overreaches for purpose-built rainbows, while conceding that classic RGB-interpolated rainbows "inevitably perform poorly on any test of perceived metric distance between displayed quantities". Its point is that feature resolving power comes mostly from the luminance gradient, whatever the hues do.

## What it is measurably good at

No study in this corpus tests a heatmap, compares one against another form, or decomposes it the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed the pie. `absence of evidence`.

[Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) do not transfer. They measured graph-reading tasks on an [adjacency matrix](adjacency-matrix.md), such as finding nodes, paths and clusters, and none involves reading a quantity from a colored cell. Their result is about the grid surviving density, not about the fill.

## What it is measurably bad at

Unmeasured on this form. The value sits on the channel family ranked least accurate for magnitude, so precise value extraction is unsupported by inheritance ([channels.md](../concepts/channels.md)), with no number attached.

Every cell has the same visual weight, and the image is a joint function of the values, the ordering and the color scale. Only the values are data.

## What is contested

The palette, at one edge. [inventory.md](../inventory.md) topic 25 records the rainbow ban as `authority-asserted` with an evidence-backed lightness argument, and contested at the edges. matplotlib names `turbo` among the maps whose lightness runs dark-light-dark, so that "This would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale". Observable Plot ships turbo as its default continuous color scheme, "chosen primarily to ensure high-contrast visibility" ([matplotlib.md](../sources/matplotlib.md), [refutations.md](../refutations.md)). Neither side disputes that lightness carries ordered data better than hue.

## The failure mode it invites

**Shipping the default ordering.** Alphabetical or insertion order is effectively random with respect to structure. [adjacency-matrix.md](adjacency-matrix.md) ties the same failure to a measured result about orderability. Here it is `authority-asserted`, from the transform slot.

**Reading adjacency as similarity.** Adjacency from a clustering means something, and which clustering is part of the fact. Adjacency from the alphabet means nothing.

**Asking the reader to read values off the fill.** Numbers that matter go in the cells or a table beside the grid. `authority-asserted`, with the accuracy half inherited and measured.

**An accidental midpoint** on a diverging ramp asserts a neutral value nobody chose (topic 32). **A rainbow on a continuous quantity** asks for an order hue does not have.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing native. The inherited sentence is about the channel: "the value is on color, which is read less accurately for magnitude than position or length, measured, so nothing precise rides on any single cell."

**Defensible, with the label said out loud:**

- "A sequential ramp, because the value is ordered and has no meaningful middle. Colormap class matched to data type is matplotlib's rule, stated in its documentation and not tested there."
- "A diverging ramp centered on zero, and the midpoint is labeled. That is a style-guide rule with the reason attached, not a measured result."
- "Rows and columns are ordered by a hierarchical clustering, stated in the caption. The ordering decides what the picture shows, which is arithmetic, and no experiment here compares orderings for a general heatmap."
- "The cross-tabulation is complete and the reader is looking for where the highs cluster, not for values, so the accurate channel is not being wasted."

**Commonly repeated, and the evidence does not support it:**

- ~~"Color is the least accurate channel, so a heatmap is a poor chart."~~ The ranking covers magnitude only and separates imprecise lightness from unsuited hue. No study here tests a heatmap against anything.
- ~~"Matrices are known to beat other layouts at this size."~~ That result is about graph-reading on an adjacency matrix, limited to static displays of random graphs at density 0.2 and above. A larger sparse interactive study found the opposite for topology tasks.
- ~~"A study showed rainbow colormaps are fine."~~ No study. [Ware, Stone & Szafir (2023)](../studies/ware-2023-rainbow-colormaps.md) is an essay, and it concedes classic rainbows perform poorly on metric judgments.

## See also

- [magnitude.md](magnitude.md): the group it is indexed under, and fits least comfortably
- [adjacency-matrix.md](adjacency-matrix.md): the same grid on a graph, with a measured ordering result
- [choropleth-map.md](choropleth-map.md): geometry fixed before the values arrive, and the other "heat map"
- [../concepts/channels.md](../concepts/channels.md): ordered lightness versus hue
- [../sources/schwabish.md](../sources/schwabish.md): the filing, and the moral about taxonomies
- [../sources/matplotlib.md](../sources/matplotlib.md): the colormap classes and the grayscale argument
