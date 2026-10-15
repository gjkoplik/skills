---
type: index
---

# Network and topology

Charts whose subject is a set of items and the connections among them.

The FT files networks under **Flow**, with Sankey diagrams and waterfalls. But its other relationships each name a *message*, and a network is a *dataset*. Flow is one message a network can carry, alongside community structure, degree distribution and path. So this index sits alongside the FT's nine rather than amending them ([taxonomy is an index, not a home](README.md#taxonomy-is-an-index-not-a-home)).

## Is the network the subject, or just how the data arrived?

Purchases, citations and service calls are all networks, and most questions asked of them are not network questions. Where a per-node table answers the question, a sorted bar chart answers it on position along a common scale, and a network diagram answers it badly or not at all.

| The reader's question | Group |
|---|---|
| Which service gets called most? Which authors publish most? | [Magnitude](magnitude.md) or [ranking](ranking.md). A sorted bar chart of a per-node column |
| How much volume moves between states? | [Flow](flow.md) |
| Who connects to whom? Does a path exist? | **This group** |
| Does the graph separate into communities? | **This group** |
| Do two networks differ structurally? | **This group** |

"Show me the network" is not a task. It produces hairballs, because a picture with no question behind it has no criterion for being wrong.

## What this group costs

In most network visualizations, position is not an encoding. Every other group spends position, the most accurately read channel, on a value. In a force-directed node-link diagram, a node's position is the output of an optimization over edge lengths and repulsion. It is not a data value, it is not reproducible across runs, and nearness may or may not mean anything.

1. **The Cleveland-McGill ranking mostly does not apply.** It ranks accuracy of reading a value off a mark, and network tasks are search, path tracing, neighborhood, grouping and comparison ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). So the studies in this group use their own task taxonomies.
2. **The design axis is whether position means anything**, not node-link against matrix. Force-directed: no. Adjacency matrix: row and column order, meaningful once an ordering is chosen. [Hive plot](hive-plot.md): assigned from node attributes or graph metrics.

## Choosing between node-link and matrix

Two studies have opposite headlines, and neither is wrong.

[Ghoniem, Fekete & Castagliola (2004)](../studies/ghoniem-2004.md) used static displays of random graphs, 20 to 100 nodes, density 0.2 to 0.6, and seven tasks. Matrices won most tasks above about twenty nodes, and node-link won path finding.

[Okoe, Jianu & Kobourov (2018)](../studies/okoe-2018.md) used interactive displays of two real networks of 256 and 332 nodes, 864 participants, and fourteen tasks. Node-link won topology, connectivity and memorability, and matrices won group and cluster tasks.

| | Favors node-link | Favors matrix |
|---|---|---|
| **Density** | Sparse. Real networks are typically near 0.03 | Dense. From roughly 0.2 up, node-link occludes |
| **Interaction** | Available. Hover, filter and highlight rescue exactly node-link's weaknesses | Static |
| **Task** | Path, topology, connectivity, memorability | Group and cluster identification, node and link lookup at scale |
| **Size** | Not the deciding variable | Not the deciding variable |

The 2004 result is usually quoted as a size threshold. But node-link fails by edge occlusion, a function of density, and Ghoniem's sparsest condition is denser than most real networks. His displays were also static. That is why a larger, sparser, interactive study came out the other way. For comparing two networks with position carrying a real variable, the [hive plot](hive-plot.md) is built for the job and unevaluated.

## Justifying the choice

**Defensible, evidence-backed:**

- "The graph is dense and the display is static, so I used a matrix. Node-link readability degrades with density, measured across seven tasks."
- "The question is whether a path exists, so I used node-link. It is the one task that favored node-link across every condition tested."
- "I ordered the matrix by community rather than alphabetically, because the matrix's advantage on group tasks depends entirely on the ordering."

**Defensible, with the label said out loud:**

- "This is a hive plot because two networks need to be compared and force-directed layouts are not comparable. That the layout is reproducible follows from its construction. That readers *do better* with it is untested."

**Not defensible:**

- ~~"Matrices beat node-link above twenty nodes."~~ True only for static displays of random graphs at density 0.2 and above.
- ~~"This layout shows three clusters, so the network has three communities."~~ A force-directed layout of random data produces apparent clusters. Position carries no defined meaning, so structure read off it is not a finding.

## Where the evidence stops

- **A few hundred nodes.** The largest network in either study has 332 nodes and 2,126 edges. Nothing here covers the tens of thousands of nodes behind most real network work.
- **Three comparisons**: node-link against adjacency matrix, and chord against Sankey. Every other form here, including the one this wiki's author has a stake in, is described but never evaluated. The hive plot literature is thorough about construction and silent about readers.
- **One layout algorithm.** Ghoniem et al. note that their node-link condition is one program, not node-link diagrams in general.

## Types in this index

- [node-link.md](node-link.md)
- [adjacency-matrix.md](adjacency-matrix.md)
- [hive-plot.md](hive-plot.md)
- [chord-diagram.md](chord-diagram.md), a circular drawing of a weighted graph, indexed primarily under [flow.md](flow.md)
- [sankey-diagram.md](sankey-diagram.md), a layered drawing of a weighted directed graph, indexed primarily under [flow.md](flow.md)

The chord diagram and the Sankey are here because the data is a weighted graph, and under Flow because the message is a volume moving between states. [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md) compared them as radial against linear layouts of the same weighted directed graph. On static displays of 8-to-15-node data, the linear one was faster and strongly preferred by novices. [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) favored the matrix under the same static conditions, and [Okoe et al. (2018)](../studies/okoe-2018.md) reversed that with interaction and real topology. Every layout comparison in this index turns on whether the reader can interact.

No page and no study: arc diagram, biofabric, edge bundling, bipartite layouts.

## See also

- [../concepts/channels.md](../concepts/channels.md): the channel evidence, and why it applies less here
- [README.md](README.md): the page template and the inheritance rule
