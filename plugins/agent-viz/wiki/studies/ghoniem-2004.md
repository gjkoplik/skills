---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Ghoniem, Fekete & Castagliola (2004/2005), *Node-Link vs Matrix*

Mohammad Ghoniem, Jean-Daniel Fekete and Philippe Castagliola, "A Comparison of the Readability of Graphs Using Node-Link and Matrix-Based Representations," InfoVis 2004, extended as "On the Readability of Graphs Using Node-Link and Matrix-Based Representations: A Controlled Experiment and Statistical Analysis," *Information Visualization* 4(2), 2005. The source of the "matrices win above twenty nodes" result.

**What it is good for.** The size-and-density crossover between node-link diagrams and adjacency matrices, and the one task that goes the other way.

**What it does not settle.** Interactive views, or real-world network topology. Both limits change the answer; see [okoe-2018.md](okoe-2018.md).

**How this was read.** PDF of the extended version from the INRIA server, text re-extracted locally.

## Design

Seven generic tasks, chosen to be independent of data semantics:

1. `nodeCount`: approximate number of nodes
2. `edgeCount`: approximate number of links
3. `mostConnected`: find the most connected node
4. `findNode`: find a node given its label
5. `findLink`: find a link between two specified nodes
6. `findNeighbor`: find a common neighbor of two nodes
7. `findPath`: find a path between two nodes

Nine graphs in a 3x3 design: 20, 50 and 100 vertices crossed with link densities 0.2, 0.4 and 0.6. Random graphs, with an extra 10% of links added to the highest-degree node so `mostConnected` had an unambiguous answer. Static displays.

## Results

From the abstract:

> "we show that when graphs are bigger than twenty vertices, the matrix-based visualization outperforms node-link diagrams on most tasks. Only path finding is consistently in favor of node-link diagrams throughout the evaluation."

From the discussion:

> "We expected the readability of node-link diagrams to deteriorate when the size of the graph and its link density increase. This hypothesis was confirmed for the seven tasks we selected. Only for 'findPath' task did node-link diagrams prove superior to matrix-based representations, although their performance deteriorates on large and dense graphs."

The authors' own conclusion is more measured than the version in circulation:

> "These techniques proved to be complementary: node-link diagrams are well suited for small graphs, and matrices are suitable for large or dense graphs. Path related tasks remain difficult on both representations and require an appropriate interaction that helps perform them."

## Caveats the authors state themselves

**Path finding.** findPath "is difficult to carry out visually when the distance between the endpoints is greater than two or three arcs," citing prior work. The node-link advantage on paths is a short-path advantage.

**`edgeCount`.** Both representations drew large shares of wrong answers. The authors flag their explanation as untested: "we account for, but this has yet to be proven through experimentation."

**Layout.** "We may also question the extensibility of the results obtained in this evaluation to other node-link layout programs than the one we chose." The node-link condition is one layout algorithm (`neato`), not node-link diagrams in general.

## Two limits not stated in the paper

**Density.** The tested range is 0.2 to 0.6. Nearly all real-world networks are sparser than that by one to two orders of magnitude. A 256-node network with 1,090 edges, as in the later replication, has density around 0.03, below anything tested here.

**Static displays.** No interaction. Hovering, filtering and highlighting change both representations substantially, and the authors' own conclusion calls for interaction on path tasks.

These two limits are why [Okoe et al.](okoe-2018.md) reach a different answer without either study being wrong.

## Evidence class of what this paper supports

- **Evidence-backed, within scope.** On static displays of random graphs of 20 to 100 nodes at densities 0.2 to 0.6, matrices outperform node-link on most of these seven tasks above about twenty nodes. Node-link wins path finding.
- **Authority-asserted.** The generalization to networks at large, which the authors do not make and their density range does not support.
- **Contested.** "Matrices beat node-link above twenty nodes" as a general rule. See the replication.

## See also

- [okoe-2018.md](okoe-2018.md): the larger, interactive, real-network study that comes out the other way
- [../chart-types/adjacency-matrix.md](../chart-types/adjacency-matrix.md)
- [../chart-types/node-link.md](../chart-types/node-link.md)
