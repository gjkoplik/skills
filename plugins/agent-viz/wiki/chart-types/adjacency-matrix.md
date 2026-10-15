---
type: chart-type
relationships: [network-topology]
aliases: [Adjacency matrix]
---

# Adjacency matrices

Nodes on both axes, a filled cell where an edge exists. It cannot produce a hairball or show a path.

## When to reach for it, and when not

The form is defined for dense graphs, static displays, and questions about groups and clusters.

| The situation | Alternative |
|---|---|
| The question is about paths | [Node-link](node-link.md). Matrices lost it in every condition tested |
| The graph is very sparse | [Node-link](node-link.md). A sparse matrix is mostly empty canvas |
| No meaningful ordering | The main advantage is gone |

## Structural decomposition

| Slot | |
|---|---|
| Data | A node table and an edge table |
| Transform | **A node ordering.** Optionally an edge-weight aggregation |
| Geometry | Cell, one per node pair |
| Scale | Presence, or weight, to cell fill |
| Coordinates | Cartesian, discrete on both axes |
| Guides | Two node axes, a legend if weighted |

The ordering plays the role of a [node-link](node-link.md) layout. A structural ordering (community, clustering, seriation) shows blocks. Alphabetical or insertion order looks like static.

## Channels

Position on two discrete scales identifies nodes. Lightness for weight ranks near the bottom ([channels.md](../concepts/channels.md)), and presence is not a magnitude.

## What it is measurably good at

**Dense and large graphs.** [Ghoniem et al. (2004)](../studies/ghoniem-2004.md): "when graphs are bigger than twenty vertices, the matrix-based visualization outperforms node-link diagrams on most tasks," at densities 0.2 to 0.6.

**Groups and clusters, even on sparse real networks.** [Okoe et al. (2018)](../studies/okoe-2018.md): "AM outperforms NL for group tasks," in 2 of 4 tested.

**Node and link finding at scale**, tied to orderability: the hypothesis "was related to the significant impact of orderability of matrices on node and link finding tasks. 'findNode' and 'findLink' tasks validate this hypothesis for large graphs and for dense graphs."

**Density.** Edges land in distinct cells, so a matrix at density 0.6 stays legible where node-link does not.

## What it is measurably bad at

**Path finding.** It lost in every 2004 condition, since a path means jumping cell to row to cell. The authors call paths hard on both forms, but this result held everywhere.

**Topology and connectivity** on sparse networks with interaction (Okoe et al. 2018).

**Space.** The matrix is quadratic in node count regardless of edge count. Unmeasured.

## What is contested

The [crossover](network-topology.md#choosing-between-node-link-and-matrix). "Matrices win above twenty nodes" holds for static displays of random graphs at density 0.2 and above, and gets quoted as general.

## The failure mode it invites

**Shipping the default ordering.** Group tasks depend on the ordering. `authority-asserted`; the measured orderability result covers node and link finding, not group tasks.

**Adjacency read as similarity.** Row neighbors are an artifact of the ordering.

## Justifying the choice

**Defensible, evidence-backed:**

- "The graph is dense and this is a static figure, so a matrix. Node-link readability was measured to degrade with density across all seven tasks tested."
- "I ordered by community rather than alphabetically. Ghoniem et al. attribute the matrix's advantage on node and link finding to orderability, and the group-task advantage plausibly rests on the same property, untested."

**Defensible, with the label said out loud:**

- "A matrix wastes space on a sparse graph. That follows from the form being quadratic in node count; it is not something anyone measured."

**Not defensible:**

- ~~"Matrices beat node-link above twenty nodes."~~ Scoped as above. A larger sparse interactive study found the opposite.
- ~~"These two rows are adjacent, so those nodes are similar."~~ Row adjacency comes from the ordering.

## See also

- [../studies/ghoniem-2004.md](../studies/ghoniem-2004.md)
- [../studies/okoe-2018.md](../studies/okoe-2018.md)
- [node-link.md](node-link.md)
