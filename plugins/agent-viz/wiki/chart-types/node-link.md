---
type: chart-type
relationships: [network-topology]
aliases: [Network diagram, Node-link diagram]
---

# Node-link diagrams

Nodes as points, edges as lines, positions assigned by a layout algorithm, the default network visualization.

## When to reach for it, and when not

It measured best on sparse, interactive graphs, for paths, connectivity and local topology.

| The situation | Alternative |
|---|---|
| Dense graph, or a static image | [Adjacency matrix](adjacency-matrix.md) |
| Groups or clusters | [Adjacency matrix](adjacency-matrix.md), structurally ordered |
| Comparing two networks | [Hive plot](hive-plot.md) or another fixed layout |
| A per-node question | A bar chart or table. "Which node has the highest degree" is a sort, not a drawing |
| Looking like something | Nothing. This is how hairballs get made |

## Structural decomposition

| Slot | |
|---|---|
| Data | A node table and an edge table |
| Transform | Layout algorithm: force-directed, spectral, hierarchical |
| Geometry | Point per node, line or curve per edge |
| Scale | Node attributes optionally to size or color. **Position is not a scale** |
| Coordinates | Cartesian, with meaningless axes |
| Guides | None |

## Channels

Position is an optimizer's output, not a data value, so nothing is read off it. Nearby nodes may be connected, or merely placed there. With a force-directed layout and no fixed seed, every run differs, so two layouts cannot be compared.

Edges read as connection, which the Cleveland-McGill ranking does not score. Node size and magnitude color rank below position and length ([channels.md](../concepts/channels.md)). Hue suits identity, which is unscored.

## What it is measurably good at

**Path finding**, the one task node-link won in [Ghoniem et al.](../studies/ghoniem-2004.md) at every size and density: "Only path finding is consistently in favor of node-link diagrams throughout the evaluation." It holds only for short paths, since the task "is difficult to carry out visually when the distance between the endpoints is greater than two or three arcs."

**Topology, connectivity and memorability**, on sparse real networks with interaction. [Okoe et al.](../studies/okoe-2018.md): "NL is better than AM for questions about network topology, connectivity, and memorability tasks." That is 5 wins and 3 losses in 10 topology tasks, a modest effect.

## What it is measurably bad at

**Rising density.** Ghoniem et al.: "We expected the readability of node-link diagrams to deteriorate when the size of the graph and its link density increase. This hypothesis was confirmed for the seven tasks we selected."

**Counting.** Both forms produced many wrong edge counts. The authors' explanation is untested.

## What is contested

**The crossover to matrices** ([central contest](network-topology.md#choosing-between-node-link-and-matrix)) is driven by density and interaction, not node count. The "twenty nodes" figure comes from a study whose sparsest graphs are denser than most real networks.

## The failure mode it invites

**The hairball.** Enough edges make a solid mass that looks like a chart and supports no task. `authority-asserted` as a named phenomenon. Ghoniem et al. measured the deterioration within their range.

**Structure that is not there.** Force-directed layouts of random data produce clusters inspection cannot tell from real ones. The [hive plot](hive-plot.md) was designed against this.

## Justifying the choice

**Defensible, evidence-backed:**

- "The question is whether a path exists between these two nodes. Path finding is the one task node-link won across every size and density tested."
- "The graph is sparse and interactive, which is the regime where node-link beat matrices on topology, connectivity and memorability across 864 participants."

**Defensible, with the label said out loud:**

- "Beyond a few hundred nodes I am extrapolating. No study in this set goes further, in either direction."

**Not defensible:**

- ~~"These three visible clusters are communities in the network."~~ Random layouts cluster too. An encoded community detection would.
- ~~"Node-link is fine here, it is only 80 nodes."~~ Ghoniem et al. found readability falling with both graph size and link density, and the twenty-node threshold held only at the densities they tested.

## See also

- [../studies/ghoniem-2004.md](../studies/ghoniem-2004.md)
- [../studies/okoe-2018.md](../studies/okoe-2018.md)
- [adjacency-matrix.md](adjacency-matrix.md)
- [hive-plot.md](hive-plot.md)
