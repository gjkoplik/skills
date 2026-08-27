---
type: index
---

# Network and topology

Charts whose subject is a set of items and the connections among them.

## First: is the network the subject, or just how the data arrived?

**A great deal of data is relational without the reader's question being relational.** Users and their purchases, papers and their citations, services and their calls: all networks, and most questions asked of them are not network questions.

The test: **can the question be answered from a per-node table?** "Which service gets called most" is a column sort. "Which authors publish most" is a count. Both are magnitude or ranking questions that happen to sit on relational data, and a sorted bar chart answers them on position along a common scale while a network diagram answers them badly or not at all.

Draw the network when the question is about **connection itself**: who connects to whom, whether a path exists, whether the graph separates into communities, whether two networks differ structurally. If you cannot state the question in those terms, you probably want a different group.

**"Show me the network" is not a task.** It is the request that produces hairballs, because a picture with no question behind it has no criterion for being wrong.

## What makes this group unlike every other

**In most network visualizations, position is not an encoding.**

Every other group here spends position, the most accurately read channel, on a value. A bar's height is the number. A point's x is the number.

In a force-directed node-link diagram, a node's position is the output of an optimization over edge lengths and repulsion. It is not a data value, it is not reproducible across runs, and two nodes near each other may or may not mean anything. The highest-accuracy channel available is spent on something with no defined reading.

Two consequences, both structural rather than stylistic:

1. **The Cleveland-McGill ranking mostly does not apply here.** It ranks accuracy of reading a value off a mark, and network tasks are search, path tracing, neighborhood, grouping and comparison. See [the scope limit](../concepts/channels.md#what-the-ranking-is-not-about). This is why the studies in this group use their own task taxonomies rather than proportional judgment.
2. **The real design axis is whether position means anything.** Force-directed: no. Adjacency matrix: position is row and column order, which means something once you choose an ordering. [Hive plot](hive-plot.md): position is assigned from node attributes or graph metrics, deliberately. That axis, not node-link-versus-matrix, is what actually separates the forms.

## Choosing between node-link and matrix

Two studies, opposite headlines, and neither is wrong.

[Ghoniem, Fekete & Castagliola (2004)](../studies/ghoniem-2004.md): static displays, random graphs, 20 to 100 nodes, density 0.2 to 0.6, seven tasks. Matrices win most tasks above about twenty nodes. Node-link wins path finding.

[Okoe, Jianu & Kobourov (2018)](../studies/okoe-2018.md): interactive displays, two real networks of 256 and 332 nodes, 864 participants, fourteen tasks. Node-link wins topology, connectivity and memorability. Matrices win group and cluster tasks.

What separates them, and therefore what should drive your choice:

| | Favors node-link | Favors matrix |
|---|---|---|
| **Density** | Sparse. Real networks are typically near 0.03 | Dense. From roughly 0.2 up, node-link occludes |
| **Interaction** | Available. Hover, filter and highlight rescue exactly node-link's weaknesses | Static |
| **Task** | Path, topology, connectivity, memorability | Group and cluster identification, node and link lookup at scale |
| **Size** | Not the deciding variable | Not the deciding variable |

**Size alone does not decide it, and that is how the 2004 result is almost always quoted.** Node-link's failure mode is edge occlusion, which is a function of density. Ghoniem's sparsest condition is denser than most real networks, and his displays were static, which is why a larger sparser interactive study came out the other way.

If your graph is sparse, interactive and you care about paths, use node-link. If it is dense, static, or the question is about groups, use a matrix. If position could carry a real variable and you need to compare two networks, consider a [hive plot](hive-plot.md), understanding that no one has evaluated it.

## Justifying the choice

**Defensible, evidence-backed:**

- "The graph is dense and the display is static, so I used a matrix. Node-link readability degrades with density, measured across seven tasks."
- "The question is whether a path exists, so I used node-link. It is the one task that favored node-link across every condition tested."
- "I ordered the matrix by community rather than alphabetically, because the matrix's advantage on group tasks depends entirely on the ordering."

**Defensible, with the label out loud:**

- "This is a hive plot because two networks need to be compared and force-directed layouts are not comparable. That the layout is reproducible follows from its construction. That readers *do better* with it is untested."

**Not defensible:**

- ~~"Matrices beat node-link above twenty nodes."~~ True only for static displays of random graphs at density 0.2 and above. Quoted as a general rule it is a scope-limited result stated as a universal one.
- ~~"This layout shows three clusters, so the network has three communities."~~ A force-directed layout of random data produces apparent clusters. Position carries no defined meaning, so structure read off it is not a finding.

## Where the evidence stops

Hard, and early. Worth knowing before you cite anything here:

- **A few hundred nodes.** The largest network in either study has 332 nodes and 2,126 edges. Nothing here speaks to the tens of thousands of nodes that motivate most real network visualization work.
- **Two representations have been evaluated.** Node-link and adjacency matrix. Every other form here, including the one this wiki's author has a stake in, is **described but never evaluated**. The hive plot literature is not thin; it is thorough about construction and silent about readers.
- **One layout algorithm.** Ghoniem et al. flag this themselves: their node-link condition is one program, not node-link diagrams in general.

## Types in this index

- [node-link.md](node-link.md)
- [adjacency-matrix.md](adjacency-matrix.md)
- [hive-plot.md](hive-plot.md)
- [chord-diagram.md](chord-diagram.md), a circular drawing of a weighted graph, indexed primarily under [flow.md](flow.md)
- [sankey-diagram.md](sankey-diagram.md), a layered drawing of a weighted directed graph, indexed primarily under [flow.md](flow.md)

No page yet, and no study either: arc diagram, biofabric, edge bundling, bipartite layouts. The chord diagram and the Sankey now have pages and still have no study; both are here because the data is a weighted graph, and under Flow because the message is a volume moving between states.

## A note on filing

The FT files networks under **Flow**, alongside Sankey diagrams and waterfalls. The other nine relationships name a *message*; a network is a *dataset*. Flow is one message you can send with a network, alongside community structure, degree distribution and path, so filing the whole class under Flow routes every network question through a category built for Sankeys.

This index is an addition rather than an amendment: the FT's nine stay as published, and this one sits alongside them. See [taxonomy is an index, not a home](README.md#taxonomy-is-an-index-not-a-home).

## See also

- [../concepts/channels.md](../concepts/channels.md) — and specifically why it applies less here than anywhere else
- [README.md](README.md) — the page template and the inheritance rule
