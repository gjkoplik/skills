---
type: chart-type
relationships: [network-topology]
aliases: [Hive plot]
---

# Hive plots

Nodes assigned to a small number of radial axes by a rule, positioned along their axis by a structural quantity, with edges drawn as curves between axes. A network layout with a node coordinate system.

**Disclosure.** This wiki's author maintains a hive plot library. That is why this page is held to the same standard as the others rather than a looser one. [evidence-class.md](../concepts/evidence-class.md) says labeling a rule you rely on is the part that costs something.

## When to reach for it, and when not

**Reach for it when** you need to compare two or more networks, or you need the same graph to lay out identically every time, and you have or can compute a variable to partition on and one to sort by. Comparability and reproducibility are the form's real offer, and they follow from its construction rather than needing an experiment.

**You do not need node metadata.** Both of the original paper's worked examples partition on graph structure alone: edge directionality for directed graphs, clustering-coefficient bands for undirected ones, with connectivity for position. A bare edge list is sufficient input.

**Do not reach for it when:**

| The situation | Use instead |
|---|---|
| One exploratory look at one sparse graph | [Node-link](node-link.md). Cheaper, familiar, and better evidenced |
| The question is about paths | [Node-link](node-link.md). Edges here are curves between axes and are not built for tracing |
| The question is about dense local structure | [Adjacency matrix](adjacency-matrix.md) |
| Nodes cannot be partitioned so edges run between neighboring axes | Reconsider the partition. Beyond three axes, edges must cross or route around, which the paper says "should be avoided" |
| The audience will see it once and needs no comparison | [Node-link](node-link.md). The reproducibility you are paying for is not being used |

## Structural decomposition

| Slot | |
|---|---|
| Data | An edge table. Node attributes are optional, not required |
| Transform | Compute structural metrics; apply a rule assigning each node to an axis; position along each axis by a chosen quantity, absolute or rank-ordered. Optionally clone an axis so within-group edges have somewhere to go |
| Geometry | Point per node, curve per edge |
| Scale | Rule output to axis identity; chosen quantity to radial position |
| Coordinates | Polar, with a small fixed number of discrete axes, typically three |
| Guides | The axes themselves, labeled, each with its own scale |

Two slots distinguish it from every other network form. **The transform is a deterministic function of the graph rather than an optimization over it**, and **the guides slot is non-empty**, which for a network chart is unusual to the point of being the whole idea.

## Channels

In a force-directed [node-link diagram](node-link.md), position is the output of an optimization. It is the highest-accuracy channel a chart has, and it is spent on a quantity with no defined reading.

A hive plot spends it on a value. Node position becomes **position along non-aligned scales**, rank 2 in the [Cleveland-McGill ordering](../concepts/channels.md#the-working-ranking), one step below a bar chart's baseline and above length, angle and area. Axis membership is an unordered categorical channel, which that ranking excludes by design rather than ranking last.

**Label this carefully, because the overclaim is easy and tempting.** That position becomes a real encoding is *definitional*: it follows from the decomposition above. That an encoding at rank 2 is read more accurately than length, angle or area is *evidence-backed*. The conclusion people want from stringing those together, that hive plots are therefore read more accurately, is **not supported**, for two independent reasons:

1. The ranking measures accuracy of reading a value off a mark. Network tasks are search, path, neighborhood, grouping and comparison, and the ranking's authors restrict it to value extraction explicitly. See [the scope limit](../concepts/channels.md#what-the-ranking-is-not-about).
2. Nobody has run the experiment.

## What the axes are built from

The single most misunderstood thing about the form: **a hive plot does not need pre-existing node metadata.** Both the partition and the position are normally derived from the graph's own topology.

From Krzywinski et al., the rules are Boolean tests on structural quantities: "is the node a sink?" or "is the node's 'clustering coefficient' smaller than 0.5?". Positions come from "the absolute or rank-ordered value of a node parameter, such as connectivity." Both worked examples in the paper are purely structural:

- **Directed networks.** Partition by edge directionality: sources are "regulators", sinks are "workhorses", the rest are "managers". Position by connectivity.
- **Undirected networks.** Partition by clustering coefficient (`cc = 0`, `0 < cc < 1`, `cc = 1`). Position by connectivity.

The paper's Table 1 lists the menu: degree, flow, betweenness, closeness, eccentricity, PageRank, clustering coefficient, topological overlap, cut-vertex status, plus network-level module membership and assortativity.

Node metadata works too, and is natural when the network carries a meaningful type or annotation. But an edge list with no attributes at all is sufficient input, which is not true of most charts that require a categorical variable.

## What it is measurably good at

**Nothing has been measured.**

What can be said without measurement, because it follows from the construction:

**Reproducibility.** Positions are a deterministic function of the rules and the graph. A force-directed layout cannot offer this, and no amount of tuning changes that.

**Comparability.** Two networks under the same partition and sort produce directly comparable pictures, node for node. This is the form's real claim and it is definitional, not empirical.

**Density does not destroy it the way it destroys a node-link diagram.** Nodes cannot drift into a hairball because their positions are fixed by the rule. Edge overplotting still happens and is a separate problem.

## What it is measurably bad at

**Nothing has been measured.** No user study exists on this form, so there is no measured weakness to report any more
than there is a measured strength. What the form costs is real and follows from its construction rather than from an
experiment; it is the next section.

## What it costs

**The rule is a free parameter, and it is where the hardness lives.** Two analysts partitioning the same network differently produce different pictures. Positions are reproducible *given* the choice; they are not invariant to it.

[Nöllenburg & Wallinger](../studies/nollenburg-2023-computing-hive-plots.md) explain why this cannot simply be automated away. Their three construction steps (partition the vertices, order the axes cyclically, order vertices on each axis) each correspond to a problem already known to be NP-complete or NP-hard, so their framework adapts heuristics rather than solving anything exactly. The choice is not an unfinished piece of engineering. It is the intractable part, handed to a human.

**A hard limit on axis count.** Three axes let every pair of axes connect without crossing a third. Beyond three, the property survives only if nodes can be ordered so that connections run between neighboring axes; otherwise, per the paper, "axes must be duplicated at multiple positions, or edges must be routed across or around other axes. This negatively impacts the interpretability of the figure and should be avoided."

**Within-axis edges need a convention.** Axis cloning is the paper's own mechanism, used in its undirected example. It is documented rather than improvised, and it is still an idiom a reader has to learn.

**Unfamiliarity.** Readers have seen node-link diagrams. Whether an unfamiliar form costs accuracy is untested here. Skau & Kosara flagged unfamiliarity as an unresolved confound when they introduced novel chart forms, which is the nearest relevant caution in this source set. `absence of evidence`.

## What is contested

Nothing. **Contested requires a record that disagrees with itself.** Here there is no record. This is `absence of evidence`, which [evidence-class.md](../concepts/evidence-class.md) keeps deliberately distinct from contested and from refuted.

The honest position, both halves stated together: the structural argument is sound and does not depend on an experiment; the perceptual claims are unmeasured. The second half should not be quietly dropped when the first is quoted.

## The failure mode it invites

**Treating the axis assignment as a finding.** The partition is an input. A hive plot showing clean separation between three groups shows that you partitioned by those groups, not that the network has that structure. This is the same trap as reading meaning into force-directed proximity, arriving from the opposite direction, and it is arguably easier to fall into because the picture looks principled.

The mitigation that follows from the form rather than from taste: because the layout is cheap and deterministic, sweeping several partition and sort choices and showing them together is tractable in a way that sweeping force-directed seeds is not.

## Justifying the choice

The honest justification here is weaker than the enthusiastic one.

**Defensible, definitional and secure:**

- "Two networks need comparing. A force-directed layout has no node coordinate system, so two of them are not comparable by construction. A hive plot's positions are a deterministic function of the rules, so they are."
- "The layout has to be identical across runs for this figure to be reused. Force-directed layouts are stochastic; this is not."
- "Node position carries a data value here rather than being an optimizer artifact."

**Defensible, with the label said out loud:**

- "I chose the partition and the sort variable. Positions are reproducible given those choices and not invariant to them. Automating the choice is not an available option: the three construction steps each correspond to a known NP-hard problem."

**Not defensible:**

- ~~"Hive plots are easier to read than node-link diagrams."~~ Nobody has measured it. Not contested, not refuted: untested.
- ~~"Position is on a rank-2 channel here, so readers extract values more accurately."~~ The premise is true and the conclusion does not follow. The channel ranking measures reading a value off a mark, and network tasks are not that.
- ~~"The three clean groups on the axes show the network's structure."~~ The groups are your partition. That is an input, not a finding.

## What would move this page

- A controlled comparison against node-link and matrix on the standard network task taxonomies at matched interaction levels. The [Okoe et al.](../studies/okoe-2018.md) protocol would transfer nearly unchanged.
- A test of comparability as a *reader* claim rather than an algorithmic one: can people detect differences between two networks better from two hive plots than from two force-directed layouts. This is the form's headline claim and the one most worth measuring.

## See also

- [../studies/krzywinski-2012-hive-plots.md](../studies/krzywinski-2012-hive-plots.md) — the original method
- [../studies/nollenburg-2023-computing-hive-plots.md](../studies/nollenburg-2023-computing-hive-plots.md) — why the rule cannot be automated
- [node-link.md](node-link.md) — the form this one is an argument against
- [../concepts/channels.md](../concepts/channels.md) — the ranking, and why it applies less here than the mechanism suggests
