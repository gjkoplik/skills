---
type: chart-type
relationships: [magnitude, correlation]
aliases: [Calendar heatmap, Heat map, Heatmap, Matrix chart, Tile chart, XY heatmap]
---

# Heatmaps

A grid of equal cells, two categorical or ordered keys running along the two axes, and one quantitative value per cell encoded in **color**.

Also called a **matrix chart** or a **tile chart**; an **XY heatmap** when both keys are ordered; a **calendar heatmap** when the two keys are day-of-week and week-of-year; and a **correlation matrix** when the cells hold correlation coefficients and the two keys are the same list of variables.

**The filing problem here is about the name rather than about the drawing.** [Schwabish](../sources/schwabish.md) files **Heatmap** under **Comparing Categories** and **Correlation Matrix**, the same grid with correlations in the cells, under **Relationship**. The [FT Visual Vocabulary](../sources/ft-visual-vocabulary.md) splits the name itself: an **XY heatmap** under **Correlation** and a **heat map** under **Spatial**. Both filings are recorded in this wiki: the first read from the book's own contents pages, the second from the Visual Vocabulary's own category listing. Neither is a claim about what anyone argues about the form. The FT's full listing carries a third heatmap of its own, **Calendar heatmap**, under Change over Time. So one name carries at least four filings across two schemes, plus a fifth for the same construction under another name. `sources/schwabish.md` draws the moral for the Sankey and waterfall case and it applies here without modification: three placements for two charts across two schemes is the clearest available evidence that these taxonomies are retrieval aids rather than facts about charts. It is indexed here under [magnitude](magnitude.md) because the cell value is a size comparison; it would sit as comfortably under correlation or spatial, and that is a fact about taxonomies rather than about the form.

Two name collisions need keeping straight. A [choropleth map](choropleth-map.md) is loosely called a heat map in ordinary usage, and it is a different construction: its geometry comes from a base geography rather than from a grid, which changes what the mark can be asked to carry. And a **density heatmap**, a two-dimensional histogram over continuous coordinates with the bin counts shown in color, shares the name and is not a grid of categorical cells; its two keys are binned continuous variables and its cell value is a count the transform produced. **Nothing in this wiki settles which of those the bare word "heatmap" refers to**, and this page does not resolve it. Everything below is about the grid of keyed cells.

## When to reach for it, and when not

**Reach for it when** every combination of two keys has a value, the reader's job is to find where the highs and lows sit or to see block structure across the grid, and approximate magnitudes are enough. The form's offer is that it shows the entire cross-tabulation at once, with no mark occluding another and no space cost per value beyond one cell.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| How big is each of these, and by how much? | [Bar chart](bar-chart.md). Position along a common scale rather than color |
| Rank these for me | [Ranking](ranking.md). Color does not support ordering by eye the way position does |
| There is only one key | [Bar chart](bar-chart.md) or a [lollipop chart](lollipop-chart.md). A one-row heatmap throws away the accurate channel for nothing |
| The reader needs the numbers | [Tables](tables.md). A table with the cells shaded is still a table, and it keeps the digits |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). A grid asserts no total |
| Where is this? | [Spatial](spatial.md). A [choropleth](choropleth-map.md) puts the value where its thing is |
| Which nodes connect to which? | [Adjacency matrix](adjacency-matrix.md), which is this form applied to a graph |
| Do these two variables move together, observation by observation? | [Correlation](correlation.md). A [scatterplot](scatterplot.md) shows the observations; a correlation matrix shows one number per pair |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (row key, column key) pair, carrying one value |
| Transform | **An ordering for the rows and an ordering for the columns.** Often an aggregation into the cell, and sometimes a per-pair statistic such as a correlation |
| Geometry | One rectangle per key pair, all the same size |
| Scale | Value to fill color, on a sequential, diverging or binned ramp |
| Coordinates | Cartesian, discrete on both axes |
| Guides | Two key axes, and a colorbar or legend with units. A diverging ramp also needs its midpoint labeled |

Two properties follow from those slots and assert nothing empirical.

**The geometry takes no input from the value.** Every cell is the same size and sits in the same place whatever the numbers are, so color is the only channel carrying the magnitude. That is the same structural fact a [choropleth](choropleth-map.md) has, arrived at from the opposite direction: there the mark's extent is fixed by a base geography, here by a grid. In both cases there is no secondary channel to fall back on.

**The row and column ordering is a free parameter that decides what the picture looks like.** Permuting rows changes no value and changes the image completely: a clustered ordering shows blocks, an alphabetical one shows noise. [adjacency-matrix.md](adjacency-matrix.md) makes this argument in full for the graph case, where the ordering "sits where a layout algorithm sits for a node-link diagram", and the argument is the same one because an adjacency matrix **is** a heatmap of a graph. Read it there rather than twice. The consequence for a general heatmap is that the ordering is a design decision you own, and a default sort order is a decision made by whatever produced the dataframe.

## Channels

**Color, carrying the magnitude, and position carrying only identity.** The two axes place a cell by its keys, which are categories or an order rather than values, so the position channel is doing lookup work and not magnitude work. Everything quantitative rides on the fill.

Read the section of [channels.md](../concepts/channels.md) on what "color is the worst channel" actually means before repeating any of this, because the usual one-line version blurs two different defects.

**Ordered lightness or saturation is low-accuracy for magnitude**, and that part is measured territory: shading and color saturation sit together in the bottom rank of the 1984 Cleveland & McGill table, below area and below volume, and the 1985 table keeps saturation and density near the bottom while adding hue below them ([channels.md](../concepts/channels.md)). Inherited with the standard caveat that the step from "this chart puts the reader on that channel" to the accuracy number is conjecture in the source literature. The practical reading is that a heatmap supports "more here than there" and does not support "twice as much there as here".

**Hue is not low-accuracy for magnitude, it is unsuited to it**, which is a different defect with a different remedy. The 1984 paper excludes hue from the list because it has no unambiguous ordering from small to large. A heatmap drawn with a rainbow colormap is making that specific error: it asks the reader to order hues, which have no order to find, and the remedy is not "be more careful" but a ramp whose lightness moves monotonically. matplotlib states the underlying result flatly ([matplotlib.md](../sources/matplotlib.md)): "Researchers have found that the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue."

**So the colormap class has to match the data type**, which is [inventory.md](../inventory.md) topic 23, `authority-asserted` from matplotlib's own documentation: sequential for an ordered value, diverging for one with a critical middle, qualitative only for something unordered. And **if the ramp diverges, the midpoint is an assertion about which value is neutral**, so it must be set deliberately and labeled. That is topic 32, `authority-asserted`, from the Urban Institute: "The center of the diverging palette should always be labeled to avoid confusing the reader." A correlation matrix is the case where this is least optional, since zero is a real midpoint and a ramp centered anywhere else is claiming something false for free.

On rainbows specifically, the page to read is [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md). **That piece is a Visualization Viewpoints department article and not a study**: no experiment, no participants, no data of its own. It argues that the blanket prohibition overreaches for purpose-built rainbows while conceding that classic RGB-interpolated rainbows "inevitably perform poorly on any test of perceived metric distance between displayed quantities". Its constructive point is the usable one here: feature resolving power is driven mostly by the **luminance gradient**, so what a detection task needs from a colormap is a monotonic or deliberately shaped lightness profile, whatever the hues do.

## What it is measurably good at

**Nothing. No study in this corpus tests a heatmap**, compares one against another form, or decomposes it into channels the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed the pie. `absence of evidence`.

The nearest measured thing in this corpus is the matrix-versus-node-link pair, and it does not transfer. [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) both measured **graph-reading tasks** on an [adjacency matrix](adjacency-matrix.md): counting nodes and links, finding a named node, finding a link between two named nodes, finding a common neighbor, finding a path, identifying and comparing clusters. Not one of those is extracting a quantity from a colored cell. What they establish is that a matrix layout survives density and supports group and cluster tasks, which is an argument about the grid, and they say nothing at all about how accurately anyone reads a value off a fill.

## What it is measurably bad at

**Also unmeasured on this form.** The one thing that can be said without measuring is inherited rather than native: the value sits on the family of channels ranked least accurate for magnitude, so precise value extraction is the wrong job to give it ([channels.md](../concepts/channels.md)). That is an inheritance, and it does not license a number.

One structural cost is certain. **Every cell has the same visual weight**, so a grid full of near-identical values and three extreme ones looks like three colored cells on a flat field, and a grid of wildly different values at the same ordering can look like the same picture under a different ramp. The image is a joint function of the values, the ordering and the color scale, and only the first of those is data.

## What is contested

**Not the form, which nothing here disputes. The palette, and only at one edge.**

[inventory.md](../inventory.md) topic 25 records the rainbow ban as `authority-asserted` with an evidence-backed lightness argument, and **contested at the edges**: matplotlib names `turbo` among the maps whose lightness runs dark-light-dark, so that "This would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale", while Observable Plot ships turbo as its **default** continuous color scheme, "chosen primarily to ensure high-contrast visibility". Two projects reading the same evidence and shipping opposite defaults ([matplotlib.md](../sources/matplotlib.md), [refutations.md](../refutations.md)). Whatever you conclude, the disagreement is about a specific family of maps and not about whether lightness carries ordered data better than hue, which neither side disputes.

## The failure mode it invites

**Shipping the default ordering.** Alphabetical or insertion order is effectively random with respect to structure, and the whole picture is a function of the ordering. This is the same failure [adjacency-matrix.md](adjacency-matrix.md) names for its own form, and there it is anchored to a measured result about orderability. Here it is `authority-asserted`, and it follows directly from the transform slot.

**Reading adjacency as similarity.** Two neighboring rows are neighbors because of an ordering somebody chose. If that ordering came from a clustering, the adjacency means something and you should say which clustering; if it came from the alphabet, it means nothing.

**Asking the reader to read values off the fill.** The failure is not the heatmap, it is the sentence under it that quotes a number the reader is expected to verify. If the numbers matter, print them in the cells or put a table next to the grid. `authority-asserted`, with the accuracy half inherited and measured.

**A diverging ramp with an accidental midpoint**, which asserts a neutral value nobody chose. Topic 32.

**A rainbow on a continuous quantity**, which asks for an ordering hue does not have.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing is native to this form. The one inherited sentence available is about the channel rather than the chart: "the value is on color, which is read less accurately for magnitude than position or length, measured, so nothing precise rides on any single cell." The step from this chart to that channel is conjecture in the source literature.

**Defensible, with the label said out loud:**

- "A sequential ramp, because the value is ordered and has no meaningful middle. Colormap class matched to data type is matplotlib's rule, stated in its documentation and not tested there."
- "A diverging ramp centered on zero, and the midpoint is labeled. That is a style-guide rule with the reason attached, not a measured result."
- "Rows and columns are ordered by a hierarchical clustering, stated in the caption. The ordering decides what the picture shows, which is arithmetic, and no experiment here compares orderings for a general heatmap."
- "The cross-tabulation is complete and the reader is looking for where the highs cluster, not for values, so the accurate channel is not being wasted."

**Commonly repeated, and the evidence does not support it:**

- ~~"Color is the least accurate channel, so a heatmap is a poor chart."~~ Two errors stacked. The ranking is about magnitude judgments only, and it separates ordered lightness, which is imprecise, from hue, which is unsuited. And no study in this corpus has tested a heatmap against anything.
- ~~"Matrices are known to beat other layouts at this size."~~ That result is about graph-reading tasks on an adjacency matrix, it is scope-limited to static displays of random graphs at density 0.2 and above, a larger sparse interactive study found the opposite for topology tasks, and none of it was about reading a value from a cell.
- ~~"A study showed rainbow colormaps are fine."~~ No study. [Ware, Stone & Szafir (2023)](../studies/ware-2023-rainbow-colormaps.md) is a Viewpoints essay with no experiment, arguing about how to read other people's evidence, and it concedes that classic rainbows perform poorly on metric judgments.

## See also

- [magnitude.md](magnitude.md) — the group it is indexed under, and the one it fits least comfortably
- [adjacency-matrix.md](adjacency-matrix.md) — the same grid applied to a graph, where the ordering argument is made in full and has a measured result behind it
- [choropleth-map.md](choropleth-map.md) — the other form whose geometry is fixed before the values arrive, and the one people mean when they say heat map about a map
- [../concepts/channels.md](../concepts/channels.md) — ordered lightness versus hue, and why the difference is not a matter of degree
- [../sources/schwabish.md](../sources/schwabish.md) — the filing, verified, and the moral about taxonomies
- [../sources/matplotlib.md](../sources/matplotlib.md) — the colormap classes and the grayscale argument
