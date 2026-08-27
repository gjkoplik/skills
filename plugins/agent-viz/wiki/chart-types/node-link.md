---
type: chart-type
relationships: [network-topology]
aliases: [Network diagram, Node-link diagram]
---

# Node-link diagrams

Nodes as points, edges as lines between them, positions assigned by a layout algorithm. The default network visualization, and the one whose failure mode has its own name.

## When to reach for it, and when not

**Reach for it when** the graph is sparse, the reader can interact with it, and the question is about paths, connectivity or local topology. That combination is where it measured best.

**Do not reach for it when:**

| The situation | Use instead |
|---|---|
| Dense graph, or a static image | [Adjacency matrix](adjacency-matrix.md). Node-link degrades with density, measured across seven tasks |
| The question is about groups or clusters | [Adjacency matrix](adjacency-matrix.md) with a structural ordering |
| Two networks need comparing | [Hive plot](hive-plot.md) or another fixed layout. Force-directed layouts are not comparable, by construction |
| The question is answerable from a per-node table | A bar chart or a table. "Which node has the highest degree" is a sort, not a drawing |
| You want it to look like something | Nothing. This is how hairballs get made |

## Structural decomposition

| Slot | |
|---|---|
| Data | A node table and an edge table |
| Transform | A layout algorithm assigning coordinates. Force-directed, spectral, hierarchical |
| Geometry | Point per node, line or curve per edge |
| Scale | Node attributes optionally map to size or color. **Position is not a scale** |
| Coordinates | Cartesian, but the axes have no meaning |
| Guides | None. There is no axis to draw |

**The transform slot is doing something no other chart in this wiki does.** Elsewhere the transform computes a statistic. Here it runs an optimization whose output is the position of every mark, and that output is not a function of any single data value.

## Channels

**Position, carrying nothing directly readable.** Proximity in the layout is a soft consequence of connectivity, not an encoding of it. Two adjacent nodes may be adjacent because they are connected, or because the optimizer had nowhere else to put them.

Edges are read as connection, which is a topological reading rather than a magnitude reading. The Cleveland-McGill ranking does not bear on it. Node size and color, when used, are ordinary channels and the ranking does bear on those: size is area, and color for a magnitude is shading or saturation, which sit below position and length ([channels.md](../concepts/channels.md)). Where color carries identity rather than magnitude, the ranking does not score it and hue is well suited to the job.

Consequence: **the same data produces a different picture on every run** unless the seed is fixed, and two networks cannot be compared by looking at two layouts. This is not a criticism of any implementation, it is a property of the form.

## What it is measurably good at

**Path finding.** The one task node-link won in [Ghoniem et al.](../studies/ghoniem-2004.md) across every size and density they tested: "Only path finding is consistently in favor of node-link diagrams throughout the evaluation."

Qualified by the authors: the advantage holds for short paths, since the task "is difficult to carry out visually when the distance between the endpoints is greater than two or three arcs."

**Topology, connectivity and memorability on sparse real networks with interaction.** [Okoe et al.](../studies/okoe-2018.md): "NL is better than AM for questions about network topology, connectivity, and memorability tasks." Read the underlying counts, which are 5 wins and 3 losses out of 10 topology tasks. A real effect, a modest one.

## What it is measurably bad at

**Everything, once density rises.** Ghoniem et al. tested exactly this and confirmed it: "We expected the readability of node-link diagrams to deteriorate when the size of the graph and its link density increase. This hypothesis was confirmed for the seven tasks we selected."

**Counting.** Both representations produced large shares of wrong answers on edge counting, and the authors flag their explanation as untested.

## What is contested

**When matrices overtake it.** The whole of the category's [central contest](network-topology.md#choosing-between-node-link-and-matrix). The short version: the crossover is driven by density and by whether interaction is available, not by node count, and the widely quoted "twenty nodes" figure comes from a study whose sparsest condition is denser than most real networks.

## The failure mode it invites

**The hairball.** Enough edges and the diagram becomes a solid mass in which no task succeeds, while still looking like a chart. It fails gradually and without warning: there is no point at which the rendering breaks, only a point past which nothing can be read off it.

`authority-asserted` as a named phenomenon, though the underlying deterioration is measured by Ghoniem et al. within their range.

**The deeper version of the same problem** is the one the [hive plot](hive-plot.md) was designed against: because position carries no meaning, a layout can look structured while encoding nothing, and a reader cannot tell the difference by inspection. A force-directed layout of random data produces clusters.

## Justifying the choice

**Defensible, evidence-backed:**

- "The question is whether a path exists between these two nodes. Path finding is the one task node-link won across every size and density tested."
- "The graph is sparse and interactive, which is the regime where node-link beat matrices on topology, connectivity and memorability across 864 participants."

**Defensible, with the label said out loud:**

- "Beyond a few hundred nodes I am extrapolating. No study in this set goes further, in either direction."

**Not defensible:**

- ~~"These three visible clusters are communities in the network."~~ Position is not an encoding here. A force-directed layout of random data produces apparent clusters, so structure read off proximity is not a finding. Run a community detection and encode the result if you want to claim it.
- ~~"Node-link is fine here, it is only 80 nodes."~~ Node count is not the variable. Density is.

## See also

- [../studies/ghoniem-2004.md](../studies/ghoniem-2004.md)
- [../studies/okoe-2018.md](../studies/okoe-2018.md)
- [adjacency-matrix.md](adjacency-matrix.md)
- [hive-plot.md](hive-plot.md)
