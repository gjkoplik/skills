---
type: chart-type
relationships: [network-topology]
aliases: [Adjacency matrix]
---

# Adjacency matrices

Nodes on both axes, a filled cell where an edge exists. The representation that cannot produce a hairball, and cannot show a path.

## When to reach for it, and when not

**Reach for it when** the graph is dense, or the display is static, or the question is about groups and clusters. It is the representation that cannot produce a hairball: density adds ink to distinct cells rather than overlapping marks.

**Choose the ordering deliberately, because it is the whole design.** A structural ordering (community, clustering, seriation) makes block structure visible. Alphabetical or insertion order is effectively random with respect to structure and produces a matrix that looks like static.

**Do not reach for it when:**

| The situation | Use instead |
|---|---|
| The question is about paths | [Node-link](node-link.md). Matrices lost path finding in every condition tested |
| The graph is very sparse | [Node-link](node-link.md). The matrix is quadratic in node count regardless of edge count, so a sparse graph wastes the canvas |
| You cannot choose a meaningful ordering | Reconsider. Without one, the form's main advantage is gone |

## Structural decomposition

| Slot | |
|---|---|
| Data | A node table and an edge table |
| Transform | **A node ordering.** Optionally an edge-weight aggregation |
| Geometry | Cell, one per node pair |
| Scale | Presence, or weight, mapped to cell fill |
| Coordinates | Cartesian, discrete on both axes |
| Guides | Two node axes, one legend if weighted |

**The ordering is the entire design decision.** It sits where a layout algorithm sits for a node-link diagram, and it determines whether structure is visible. The same matrix under a random ordering and under a clustered ordering are different charts.

## Channels

Position along two discrete non-aligned scales for identity, plus a fill channel for the cell.

The fill sits near the bottom of the ordering if it encodes weight by lightness, and it is nowhere on it at all if it encodes mere presence, since presence is not a magnitude. This is a case where the ranking's exclusion of unordered channels matters: **a binary matrix asks no magnitude question of the reader**, so the channel evidence is silent on it.

## What it is measurably good at

**Dense and large graphs, on most tasks.** [Ghoniem et al. (2004)](../studies/ghoniem-2004.md): "when graphs are bigger than twenty vertices, the matrix-based visualization outperforms node-link diagrams on most tasks," across densities 0.2 to 0.6.

**Group and cluster tasks, even on sparse real networks.** [Okoe et al. (2018)](../studies/okoe-2018.md): "AM outperforms NL for group tasks," at 2 of 4 tested. Consistent with the 2004 finding that a good ordering makes block structure visible.

**Node and link finding at scale**, which Ghoniem et al. attribute to orderability: the hypothesis "was related to the significant impact of orderability of matrices on node and link finding tasks. 'findNode' and 'findLink' tasks validate this hypothesis for large graphs and for dense graphs."

**Not degrading.** Density adds ink to distinct cells rather than overlapping marks. A matrix at density 0.6 is legible where the equivalent node-link diagram is not. This is structural, and it is why the crossover exists.

## What it is measurably bad at

**Path finding.** Lost consistently across every condition in 2004. Following a path means jumping from a cell to a row to another cell, repeatedly, with no visual continuity. The authors' conclusion is that paths are hard on both and need interaction, but the node-link advantage here is the one result that held everywhere.

**Topology and connectivity questions on sparse networks with interaction**, per 2018.

**Space.** The matrix is quadratic in node count regardless of edge count, so a sparse network wastes almost the entire canvas. Not measured in either study; it follows from the form.

## What is contested

The [crossover](network-topology.md#choosing-between-node-link-and-matrix). "Matrices win above twenty nodes" is a scope-limited result quoted as a general one. The scope is: static displays, random graphs, density at or above 0.2.

## The failure mode it invites

**Shipping the default ordering.** Alphabetical or insertion order is effectively random with respect to structure, and produces a matrix that looks like static. The form's entire advantage on group tasks depends on the ordering, and the ordering is the one thing a default cannot supply. `authority-asserted`, though it follows directly from the measured orderability result.

**Reading adjacency as similarity.** Two adjacent rows are adjacent because of the ordering, which may be arbitrary. Same trap as proximity in a node-link layout, from the opposite direction.

## Justifying the choice

**Defensible, evidence-backed:**

- "The graph is dense and this is a static figure, so a matrix. Node-link readability was measured to degrade with density across all seven tasks tested."
- "I ordered by community rather than alphabetically. The matrix's advantage on group tasks is attributed directly to orderability."

**Defensible, with the label said out loud:**

- "A matrix wastes space on a sparse graph. That follows from the form being quadratic in node count; it is not something anyone measured."

**Not defensible:**

- ~~"Matrices beat node-link above twenty nodes."~~ True for static displays of random graphs at density 0.2 and above. Quoted as a general rule it is a scope-limited result stated as a universal one, and a larger sparse interactive study found the opposite.
- ~~"These two rows are adjacent, so those nodes are similar."~~ Adjacency in the matrix is a property of the ordering you chose.

## See also

- [../studies/ghoniem-2004.md](../studies/ghoniem-2004.md)
- [../studies/okoe-2018.md](../studies/okoe-2018.md)
- [node-link.md](node-link.md)
