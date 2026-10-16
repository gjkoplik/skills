---
type: chart-type
relationships: [network-topology]
aliases: [Hive plot]
---

# Hive plots

A network layout with a node coordinate system: nodes assigned by a rule to a few radial axes, positioned along their axis by a structural quantity, with edges drawn as curves between axes.

This wiki's author maintains a hive plot library, and the page is held to the same labels as the rest ([evidence-class.md](../concepts/evidence-class.md)).

## When to reach for it, and when not

The form is defined for comparing networks, or laying out one graph identically every time, given a variable to partition on and one to sort by.

| The situation | Alternative |
|---|---|
| One exploratory look at one sparse graph | [Node-link](node-link.md). Cheaper, familiar, and better evidenced |
| The question is about paths | [Node-link](node-link.md). Edges here are curves between axes, not built for tracing |
| The question is about dense local structure | [Adjacency matrix](adjacency-matrix.md) |
| Nodes cannot be partitioned so edges run between neighboring axes | A different partition. Beyond three axes, edges between non-neighboring axes must cross or route around others, which the paper says "should be avoided" |
| The audience will see it once and needs no comparison | [Node-link](node-link.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | An edge table. Node attributes are optional |
| Transform | Compute structural metrics; apply a rule assigning each node to an axis; position along each axis by a chosen quantity, absolute or rank-ordered. Optionally clone an axis so within-group edges have somewhere to go |
| Geometry | Point per node, curve per edge |
| Scale | Rule output to axis identity; chosen quantity to radial position |
| Coordinates | Polar, with a small fixed number of discrete axes, typically three |
| Guides | The axes themselves, labeled, each with its own scale |

The transform is a deterministic function of the graph rather than an optimization over it, and the guides slot is non-empty. No other network form has either. In [Krzywinski et al.](../studies/krzywinski-2012-hive-plots.md) the rules are Boolean tests on structural quantities: "is the node a sink?" or "is the node's 'clustering coefficient' smaller than 0.5?". Positions come from "the absolute or rank-ordered value of a node parameter, such as connectivity." Both worked examples in the paper are purely structural, positioning by connectivity:

- **Directed networks.** Partition by edge directionality: sources are "regulators", sinks are "workhorses", the rest are "managers".
- **Undirected networks.** Partition by clustering coefficient (`cc = 0`, `0 < cc < 1`, `cc = 1`).

The paper's Table 1 lists the menu: degree, flow, betweenness, closeness, eccentricity, PageRank, clustering coefficient, topological overlap, cut-vertex status, plus network-level module membership and assortativity. A bare edge list is sufficient input, though node metadata works too.

Three properties follow from the construction, all definitional:

- **Reproducibility.** Positions are a deterministic function of the rules and the graph.
- **Comparability.** Two networks under the same partition and sort compare node for node. This is the form's main claim.
- **Density.** The rule fixes nodes, so they cannot drift into a hairball. Edge overplotting remains.

## Channels

A force-directed [node-link diagram](node-link.md) spends position, the most accurate channel, on an optimizer output. A hive plot spends it on a value: position along non-aligned scales, which the [Cleveland-McGill ordering](../concepts/channels.md#the-working-ranking) places just below position on a common baseline and above length, angle and area. Axis membership is an unordered categorical channel, which that ranking excludes by design.

That position becomes an encoding is definitional. That position along non-aligned scales beats length, angle or area is `evidence-backed`. That hive plots are therefore read more accurately is not supported: the ranking covers value extraction, not the search, path, neighborhood, grouping and comparison tasks of networks ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)), and nobody has run the experiment.

## What is measured

No study in this corpus tests the form with readers. `absence of evidence`. Missing are a comparison with node-link and matrix on standard network tasks at matched interaction, which the [Okoe et al.](../studies/okoe-2018.md) protocol would transfer to nearly unchanged, and a test of whether readers spot differences between networks better on hive plots than on force-directed layouts. Unfamiliarity is untested too; Skau & Kosara flagged it as an unresolved confound for novel chart forms.

One computational result bears on the form. [Nöllenburg & Wallinger](../studies/nollenburg-2023-computing-hive-plots.md) show the partition cannot be automated away: their three construction steps (partition the vertices, order the axes cyclically, order vertices on each axis) each correspond to a problem known to be NP-complete or NP-hard, so their framework adapts heuristics instead of exact solutions. Nothing is contested in this corpus.

## The failure mode it invites

**Treating the axis assignment as a finding.** Clean separation between three groups shows the partition, not the network's structure: the force-directed proximity trap in reverse, with a more principled-looking picture. Positions are reproducible *given* the partition, not invariant to it, and the rule is a free parameter that cannot be computed exactly. The layout is cheap and deterministic, so several partitions and sorts can be shown side by side.

**Axis count.** Three axes let every pair connect without crossing a third. Beyond three, that holds only if nodes can be ordered so connections run between neighboring axes. Otherwise, per the paper, "axes must be duplicated at multiple positions, or edges must be routed across or around other axes. This negatively impacts the interpretability of the figure and should be avoided."

**Within-axis edges.** Axis cloning, the paper's fix, is an idiom readers must learn.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies; no study tests the form. The three sentences below are definitional, which is as secure as a claim about construction gets and says nothing about readers.

- "Two networks need comparing. A force-directed layout has no node coordinate system, so two of them are not comparable by construction. A hive plot's positions are a deterministic function of the rules, so they are."
- "The layout has to be identical across runs for this figure to be reused. Force-directed layouts are stochastic; this is not."
- "Node position carries a data value here rather than being an optimizer artifact."

**Defensible, with the label said out loud:**

- "I chose the partition and the sort variable. Positions are reproducible given those choices and not invariant to them. Automating the choice is not an available option: the three construction steps each correspond to a known NP-hard problem."

**Commonly repeated, and the evidence does not support it:**

- ~~"Hive plots are easier to read than node-link diagrams."~~ Untested.
- ~~"Position is on a well-measured channel here, so readers extract values more accurately."~~ True premise, but network tasks are not value extraction.
- ~~"The three clean groups on the axes show the network's structure."~~ The groups are the partition, an input.

## See also

- [../studies/krzywinski-2012-hive-plots.md](../studies/krzywinski-2012-hive-plots.md): the original method
- [../studies/nollenburg-2023-computing-hive-plots.md](../studies/nollenburg-2023-computing-hive-plots.md): why the rule cannot be automated
- [node-link.md](node-link.md): the form this one argues against
- [../concepts/channels.md](../concepts/channels.md): the ranking and its scope
