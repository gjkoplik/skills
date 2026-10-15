---
type: study
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Krzywinski et al. (2012), *Hive Plots*

Martin Krzywinski, Inanc Birol, Steven J. M. Jones and Marco A. Marra, "Hive plots: rational approach to visualizing networks," *Briefings in Bioinformatics* 13(5), 2012, pp. 627-644. The paper that introduced hive plots, as an argued alternative to force-directed and spectral layouts.

**What it is good for.** The method: how axes and node positions are assigned, and the geometric constraint on axis count.

**What it does not settle.** Whether readers do better with hive plots. The paper has no user study: a full-text search finds no "user study", "participant" or "subjects". Its claims are argued from principle and shown on worked examples.

**How this was read.** Text extracted with `pdfminer.six` from a local copy of the PDF. The paper is paywalled at Oxford Academic, with no open-access or PubMed Central deposit.

## The argument it makes

From the abstract:

> "These algorithms lack reproducibility and perceptual uniformity because they do not use a node coordinate system. The layouts can be difficult to interpret and are unsuitable for assessing differences in networks."

The body adds that such layouts shift with small network changes, differ widely across algorithms, and can show structure where none exists. The critique is largely definitional, so no experiment is offered or needed.

## The method

Three steps (p. 632):

> "To create an HP, network structural parameters (Table 1) used by rules are initially calculated (e.g. connectivity, clustering coefficient, etc.). Parameters are selected to suit the purpose of the layout ... Next, the rules are applied to each node in the network to assign it to an axis and determine its coordinate."

Axis assignment:

> "Axis assignment rules are typically Boolean tests such as 'is the node a sink?' or 'is the node's "clustering coefficient" smaller than 0.5?'. It is up to the user to define rules that create a unique assignment and rules can be a function of any number of structural parameters."

Node position:

> "Node coordinates are typically derived from the absolute or rank-ordered value of a node parameter, such as connectivity."

Both come from the graph's own topology, which the abstract does not say. The worked examples are purely structural:

- **Directed network.** Axes by edge direction, in an earlier regulatory-hierarchy paper's terms: sources (out edges only) are "regulators", sinks (in edges only) are "workhorses", the rest "managers". Coordinates from total connectivity.
- **Undirected network.** Axes by clustering coefficient: `cc = 0` to axis 1, `0 < cc < 1` to axis 2, `cc = 1` to axis 3. Coordinates from connectivity.

Metadata also works: the directed layout suits networks whose nodes "can be similarly partitioned by structure, function or annotation."

## Table 1, the menu of assignment variables

**Node parameters.** Degree (connectivity), flow (out edges minus in edges, so positive flow is a source), betweenness, closeness, eccentricity, PageRank, clustering coefficient, topological overlap, cut vertex (1 if removing the node disconnects the graph).

**Network parameters.** Module, assortativity, centralization, density, diameter, radius.

## The axis-count constraint

The reason hive plots almost always have three axes (p. 634):

> "Hive plots with three axes accommodate edges between each axis pair without crossing the other axis. In general, this condition can be achieved with more than three axes if nodes can be partitioned to axes in a way that allows for an order in which nodes are connected only to those on neighboring axes. If this is not possible, axes must be duplicated at multiple positions, or edges must be routed across or around other axes. This negatively impacts the interpretability of the figure and should be avoided."

**Axis cloning** is the paper's documented mechanism for edges within one axis, used in the undirected example to connect `cc = 0` nodes.

## Evidence class of what this paper supports

- **Definitional.** Force-directed and spectral layouts have no node coordinate system, so they are neither reproducible nor comparable. Hive plot positions are a deterministic function of the rules, so two networks under the same rules are directly comparable. The three-axis crossing property.
- **Authority-asserted.** That hive plots are "informative", "simple to understand", and "depict network structure transparently".
- **Absence of evidence.** Every claim about how well readers do.

## See also

- [nollenburg-2023-computing-hive-plots.md](nollenburg-2023-computing-hive-plots.md): the algorithmic formalization
- [../chart-types/hive-plot.md](../chart-types/hive-plot.md): the type page
- [ghoniem-2004.md](ghoniem-2004.md), [okoe-2018.md](okoe-2018.md): evaluated network-representation comparisons, for contrast
