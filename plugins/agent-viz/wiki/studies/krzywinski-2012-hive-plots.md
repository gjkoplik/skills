---
type: study
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Krzywinski et al. (2012), *Hive Plots*

Martin Krzywinski, Inanc Birol, Steven J. M. Jones and Marco A. Marra, "Hive plots: rational approach to visualizing networks," *Briefings in Bioinformatics* 13(5), 2012, pp. 627-644. The paper that introduced hive plots, as an argued alternative to force-directed and spectral layouts.

**How this was read.** 18-page PDF, text extracted locally with `pdfminer.six`. **Reachability note.** The paper is paywalled at Oxford Academic with no open-access or PubMed Central deposit, and an earlier pass on this wiki recorded it as `not-reached` on that basis. It was reachable the whole time from a local copy.

**What it is good for.** The method: how axes and node positions are actually assigned, and the geometric constraint on axis count. Also for seeing clearly what kind of paper it is.

**What it does not settle.** Whether readers perform better with hive plots. **The paper contains no user study.** A full-text search returns zero occurrences of "user study", "participant" or "subjects". The claims are argued from principle and demonstrated on worked examples.

---

## The argument it makes

Against force-directed and spectral layouts, from the abstract:

> "These algorithms lack reproducibility and perceptual uniformity because they do not use a node coordinate system. The layouts can be difficult to interpret and are unsuitable for assessing differences in networks."

Elaborated in the body: layout algorithms are sensitive to small changes in the network, different algorithms generate very different layouts of the same network, and apparent structure can appear where none exists.

**The critique is largely definitional and it is correct as far as it goes.** A stochastic optimization has no coordinate system, so it cannot be reproducible or comparable. No experiment is needed to establish that, and none is offered.

## The method

Three steps, from p. 632:

> "To create an HP, network structural parameters (Table 1) used by rules are initially calculated (e.g. connectivity, clustering coefficient, etc.). Parameters are selected to suit the purpose of the layout ... Next, the rules are applied to each node in the network to assign it to an axis and determine its coordinate."

**Axis assignment** is a Boolean test on structural quantities:

> "Axis assignment rules are typically Boolean tests such as 'is the node a sink?' or 'is the node's "clustering coefficient" smaller than 0.5?'. It is up to the user to define rules that create a unique assignment and rules can be a function of any number of structural parameters."

**Node position** likewise:

> "Node coordinates are typically derived from the absolute or rank-ordered value of a node parameter, such as connectivity."

**Both the partition and the position are derived from the graph's own topology**, which the abstract does not say. A hive plot does not require pre-existing node metadata. The two worked examples are entirely structural:

- **Directed network.** Nodes assigned by edge directionality, using the terminology of an earlier regulatory-hierarchy paper: sources (out edges only) are "regulators", sinks (in edges only) are "workhorses", and the rest are "managers". Coordinates from total connectivity.
- **Undirected network.** Nodes assigned by clustering coefficient, `cc = 0` to axis 1, `0 < cc < 1` to axis 2, `cc = 1` to axis 3. Coordinates from connectivity again.

Node metadata works too, and the paper says the directed layout is natural for networks whose nodes "can be similarly partitioned by structure, function or annotation." But structure alone is sufficient, and it is what the canonical examples use.

## Table 1, the menu of assignment variables

The variables the paper offers for axis assignment and node position:

**Node parameters.** Degree (connectivity), flow (out edges minus in edges, so positive flow is a source), betweenness, closeness, eccentricity, PageRank, clustering coefficient, topological overlap, cut vertex (1 if removing the node disconnects the graph).

**Network parameters.** Module, assortativity, centralization, density, diameter, radius.

## The axis-count constraint

A real geometric limit, and the reason hive plots are almost always drawn with three axes (p. 634):

> "Hive plots with three axes accommodate edges between each axis pair without crossing the other axis. In general, this condition can be achieved with more than three axes if nodes can be partitioned to axes in a way that allows for an order in which nodes are connected only to those on neighboring axes. If this is not possible, axes must be duplicated at multiple positions, or edges must be routed across or around other axes. This negatively impacts the interpretability of the figure and should be avoided."

**Axis cloning** is the paper's own mechanism for showing edges between nodes on the same axis, used in the undirected example so that `cc = 0` nodes can be connected to each other. It is a documented convention, not a workaround.

## Evidence class of what this paper supports

- **Definitional, and secure.** Force-directed and spectral layouts have no node coordinate system and are therefore neither reproducible nor comparable. Hive plot positions are a deterministic function of the chosen rules, so two networks under the same rules are directly comparable. The three-axis crossing property.
- **Authority-asserted.** That hive plots are "informative", "simple to understand", and "depict network structure transparently".
- **Absence of evidence.** Every claim about how well readers actually do. Not contested, not refuted: unmeasured.

## See also

- [nollenburg-2023-computing-hive-plots.md](nollenburg-2023-computing-hive-plots.md) — the algorithmic formalization, and the only other hive plot paper reached here
- [../chart-types/hive-plot.md](../chart-types/hive-plot.md) — the type page
- [ghoniem-2004.md](ghoniem-2004.md), [okoe-2018.md](okoe-2018.md) — what an evaluated network-representation comparison looks like, for contrast
