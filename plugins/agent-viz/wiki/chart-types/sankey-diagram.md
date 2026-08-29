---
type: chart-type
relationships: [flow, network-topology]
aliases: [Sankey diagram]
---

# Sankey diagrams

States drawn as nodes and movements between them as ribbons, with each ribbon's width encoding the volume that moves, on one width-per-unit scale for the whole figure.

## When to reach for it, and when not

The form is defined for the case where a quantity genuinely moves between two or more states, the volumes differ enough to be told apart at a glance, and the reader is meant to see that what leaves each node equals what arrives.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How big is each state? | [Bar chart](bar-chart.md). The node totals are the answer and the ribbons are decoration |
| How does this one total break down? | [Stacked bar](stacked-bar.md) or [treemap](treemap.md). One stage is not a flow |
| Who connects to whom, or is there a path? | [Node-link](node-link.md), and see [network-topology.md](network-topology.md) |
| Flows run in both directions within one set of entities | [Chord diagram](chord-diagram.md) |
| A single running total gains and loses along a sequence | [Waterfall chart](waterfall-chart.md) |
| What are the exact volumes? | A table, or direct labels on the ribbons |
| Nothing actually moved; these are two attributes of the same rows | [Stacked bar](stacked-bar.md), grouped or small-multiple. The ribbons would assert a movement the data does not record |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (source, target, volume), across two or more stages |
| Transform | Sum incident volumes per node, assign nodes to stages, then **order nodes within a stage and ribbons within a node** to reduce crossings |
| Geometry | Rectangle per node, band per flow |
| Scale | Volume to ribbon width, on one scale shared by the whole figure. Stage position is ordinal and carries no quantity |
| Coordinates | Cartesian, with the along-flow axis carrying order only |
| Guides | Node labels and usually volume labels. **There is normally no axis at all** |

**The transform slot is doing what a layout algorithm does for a [node-link diagram](node-link.md):** it runs an optimization whose output is where every mark sits, and that output is not a function of any single data value. A Sankey is a layered drawing of a weighted directed graph, which is why it belongs to [network-topology.md](network-topology.md) as much as to [flow.md](flow.md).

## The conservation constraint

Flow in equals flow out at every node, visibly, because the node's height is the sum of its ribbons on either side. That is the same trade [part-to-whole](part-to-whole.md) makes: value-reading accuracy is spent, and what comes back is a constraint the reader can see holding.

Where the data does not conserve, or where the conservation is not part of the message, that trade returns nothing. Losses, unallocated remainders and double-counted rows all have to be drawn as something, and the usual something is a node called "other" that exists to make the arithmetic work.

Definitional throughout, and it stops there: nobody has measured whether readers notice the conservation or use it.

## Channels

**Width at a node**, which is a length reading on a stack with no common baseline except the ribbon at the node's edge, and **the band of ink along the path**, which is closer to an area reading. Neither is position along a common scale, the channel measured most accurately ([channels.md](../concepts/channels.md)).

Inherited, with the usual caveat that the mapping from this chart to those channels is conjecture rather than measurement. No study has decomposed a Sankey the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed a pie.

One property has no analog elsewhere in the wiki: **the same ribbon is read at two different widths in most implementations**, once at each endpoint, with the band interpolating between them. A reader tracing a flow across the figure is not reading a constant mark.

## What it is measurably good at

**Reading cold, against the other weighted-graph drawing.** [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md) ran 51 novices through 2,040 trials on static Sankey and [chord](chord-diagram.md) renderings of the same 8-to-15-node directed flow data, across five question types and four datasets. Sankey won on completion time (18.35s against 22.01s), on errors (0.96 against 1.07 per question), on four NASA-TLX effort scales, and on preference by 42 to 9.

The performance effects are small against the paper's own thresholds, generalized η² = 0.02 for time and 0.001 for errors, and they are mostly a first-exposure advantage that has largely closed by the fourth time a reader answers a given question type. The large, robust result is the subjective one: readers found the Sankey markedly less effortful and believed, 43 to 8, that they were more accurate with it.

**The participants' stated reason is the layout, not the ribbons.** They described the left-to-right arrangement as a familiar frame of reference and the circle as hard to keep track of. Nothing in the study asked anyone to read a volume off a width, so none of this is evidence that the ribbon encoding works.

The nearest other work is in the network group and it does not transfer. [Ghoniem, Fekete & Castagliola (2004)](../studies/ghoniem-2004.md) measured node-link diagrams against adjacency matrices on seven tasks over random graphs of 20 to 100 nodes at densities 0.2 to 0.6, in static displays. [Okoe, Jianu & Kobourov (2018)](../studies/okoe-2018.md) measured the same pair on fourteen tasks over two real networks of 256 and 332 nodes, interactively, with 864 participants. They disagree, and the disagreement is about density and interaction ([network-topology.md](network-topology.md)). Neither tested a layered layout, a weighted edge drawn as a width, or any task resembling reading a volume off a ribbon.

## What it is measurably bad at

Nothing measured. Two exposures are real and follow from the structure:

**Value extraction.** Every volume on the chart sits on a channel measured worse than position, and there is no axis to check against. This is inherited from [channels.md](../concepts/channels.md), not a finding about Sankeys.

**Crossings, which are an output of the ordering.** Two Sankeys of the same data with different node orderings look substantially different, and nothing in the figure records which ordering produced it. Same structural problem as force-directed layout in [node-link.md](node-link.md), arrived at from a different direction.

## What is contested

Nothing empirical. The one result on this form is provisional in a specific way: [Gutwin et al. (2023)](../studies/gutwin-2023-chord-vs-sankey.md) tested static drawings with no hover highlighting, and the chord diagram's measured weaknesses (tracing a ribbon, reading an arrowhead, separating incoming from outgoing links) are exactly what interaction repairs. [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) are the corpus's precedent for a static comparison of two relational layouts reversing once interaction was added. The measured Sankey advantage is a static-and-novice one.

The other disagreement is about filing: Flow for the FT, Comparing Categories for [Schwabish](../sources/schwabish.md), and a weighted-graph drawing on this wiki's own reading. That is a retrieval question, not a claim about the chart.

## The failure mode it invites

**Drawing movement that never happened.** A cross-tabulation of two columns produces a perfectly well-formed Sankey, and the ribbons then assert that rows traveled from one state to the other. This is the group's characteristic failure and it is worse here than anywhere else, because the form is at its most persuasive exactly when the underlying table is a plain contingency table. `authority-asserted`, and it follows from what the mark means rather than from taste.

**Many small flows.** Below a couple of pixels a ribbon is present but unreadable, and the eye reads the figure as the three or four widest bands plus texture. No measured threshold; aggregating the tail is the same move as "other" in [part-to-whole.md](part-to-whole.md).

## Justifying the choice

**Defensible, evidence-backed:**

- "A Sankey rather than a chord diagram, because this audience gets one look and no interaction, and novices were faster, marginally more accurate and much less frustrated with the linear layout." Measured by [Gutwin et al. (2023)](../studies/gutwin-2023-chord-vs-sankey.md) on static drawings of 8-to-15-node directed data. The performance gap is small and mostly a first-exposure effect.

The one inheritable sentence is a channel claim:

- "The volumes are labeled, because a ribbon width is a floating length judgment rather than a position one, and there is no axis on this chart to check it against" ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "The reader needs to see that everything that left the first stage arrived somewhere in the second. Conservation follows from the construction; that readers use it is untested."
- "This is a Sankey rather than two stacked bars because which part of A became which part of B is the message." Practitioner convention, no study.
- "Nodes are ordered to minimize crossings, and that ordering is mine, not the data's."

**Commonly repeated, and the evidence does not support it:**

- ~~"A Sankey shows where the money went."~~ It shows a source-by-destination tabulation drawn as movement. Whether anything moved is a fact about the data.
- ~~"The ribbon widths are proportional to the volumes, so readers read the volumes off them."~~ The first half is definitional and secure. The second half is the step nobody has measured, on this chart or any other flow form. The one flow study in this corpus compares layouts and never asks anyone to name a quantity.
- ~~"Sankey diagrams are easier to read than chord diagrams."~~ Too strong for what was measured. Static, novice readers, no interaction, effect sizes of 0.02 and 0.001, and the gap closes by the fourth exposure. What is large is that they *preferred* it and found it less effortful.

## See also

- [../studies/gutwin-2023-chord-vs-sankey.md](../studies/gutwin-2023-chord-vs-sankey.md) — the only study here that tests this form, and how far its numbers reach
- [flow.md](flow.md) — the group, its two tests, and the free parameter every form here leaves open
- [network-topology.md](network-topology.md) — the other reading of the same weighted-graph data
- [chord-diagram.md](chord-diagram.md) — the same data with one entity set and no stage order
- [part-to-whole.md](part-to-whole.md) — the parallel purchase, a whole-constraint instead of a conservation one
- [../concepts/channels.md](../concepts/channels.md)
