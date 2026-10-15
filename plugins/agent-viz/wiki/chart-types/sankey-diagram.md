---
type: chart-type
relationships: [flow, network-topology]
aliases: [Sankey diagram]
---

# Sankey diagrams

States drawn as nodes and movements between them as ribbons, with each ribbon's width encoding the volume that moves, on one width-per-unit scale for the whole figure.

## When to reach for it, and when not

The form is defined for a quantity that moves between states, in volumes different enough to tell apart, where what leaves each node equaling what arrives is part of the message.

| The question | Alternative |
|---|---|
| How big is each state? | [Bar chart](bar-chart.md). The node totals are the answer |
| How does this one total break down? | [Stacked bar](stacked-bar.md) or [treemap](treemap.md). One stage is not a flow |
| Who connects to whom? | [Node-link](node-link.md). See [network-topology.md](network-topology.md) |
| Flows run both ways within one set of entities | [Chord diagram](chord-diagram.md) |
| One running total gains and loses along a sequence | [Waterfall chart](waterfall-chart.md) |
| Exact volumes | A table, or labels on the ribbons |
| Nothing moved; these are two attributes of the same rows | [Stacked bar](stacked-bar.md), grouped or small-multiple. Ribbons would assert movement |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (source, target, volume), across two or more stages |
| Transform | Sum incident volumes per node, assign nodes to stages, then **order nodes within a stage and ribbons within a node** to reduce crossings |
| Geometry | Rectangle per node, band per flow |
| Scale | Volume to ribbon width, one scale for the figure. Stage position is ordinal |
| Coordinates | Cartesian. The along-flow axis is order only |
| Guides | Node labels, usually volume labels. Normally no axis |

A Sankey is a layered drawing of a weighted directed graph, laid out by optimization like a [node-link diagram](node-link.md), so it belongs to [network-topology.md](network-topology.md) as much as to [flow.md](flow.md).

## The conservation constraint

A node's height is the sum of its ribbons on either side, so flow in visibly equals flow out. That is the [part-to-whole](part-to-whole.md) trade, value-reading accuracy spent for a visible constraint. Data that does not conserve needs an "other" node. Whether readers use the constraint is unmeasured.

## Channels

Width at a node is a length with no common baseline, and the band along the path is closer to area. Neither is position along a common scale ([channels.md](../concepts/channels.md)), and no study has decomposed a Sankey the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed a pie. Most implementations draw a ribbon at a different width at each end.

## What it is measurably good at

First reads, against a [chord diagram](chord-diagram.md). [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md) ran 51 novices through 2,040 trials on static Sankey and chord renderings of the same 8-to-15-node directed flow data, across five question types and four datasets. Sankey won on time (18.35s against 22.01s), errors (0.96 against 1.07 per question), four NASA-TLX effort scales, and preference, 42 to 9.

The performance effects are small by the paper's own thresholds (generalized η² = 0.02 for time, 0.001 for errors) and mostly close by a reader's fourth question of a given type. The subjective result is large: readers believed, 43 to 8, that they were more accurate with the Sankey. They credited the left-to-right layout, and no task asked for a volume read off a width.

The node-link against matrix studies on [network-topology.md](network-topology.md) drew no layered layout and no weight as width. They are [Ghoniem, Fekete & Castagliola (2004)](../studies/ghoniem-2004.md) (static, random graphs of 20 to 100 nodes, densities 0.2 to 0.6) and [Okoe, Jianu & Kobourov (2018)](../studies/okoe-2018.md) (interactive, networks of 256 and 332 nodes, 864 participants).

## What it is measurably bad at

Nothing measured. Every volume is on a channel worse than position, with no axis. Crossings come from the ordering, so two Sankeys of the same data can look substantially different, as with force-directed layout in [node-link.md](node-link.md).

## What is contested

Nothing empirical. [Gutwin et al. (2023)](../studies/gutwin-2023-chord-vs-sankey.md) drew static figures, and the chord weaknesses it measured (tracing a ribbon, reading an arrowhead, separating incoming from outgoing links) are what hover highlighting repairs. A static layout result reversed under interaction once before, from [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) to [Okoe et al. (2018)](../studies/okoe-2018.md). Filing differs: Flow for the FT, Comparing Categories for [Schwabish](../sources/schwabish.md).

## The failure mode it invites

**Movement that never happened.** A cross-tabulation of two columns makes a well-formed Sankey whose ribbons assert that rows traveled between states, and the form is most persuasive on exactly that kind of table. `authority-asserted`, from what the mark means.

**Many small flows.** Below a couple of pixels a ribbon is unreadable, and the figure reads as its widest few bands. There is no measured threshold. The tail can be aggregated, as with "other" in [part-to-whole.md](part-to-whole.md).

## Justifying the choice

**Defensible, evidence-backed:**

- "A Sankey rather than a chord diagram, because this audience gets one look and no interaction, and novices were faster, marginally more accurate and much less frustrated with the linear layout." [Gutwin et al. (2023)](../studies/gutwin-2023-chord-vs-sankey.md), on static 8-to-15-node data, with a small gap.
- "The volumes are labeled, because a ribbon width is a floating length judgment rather than a position one, and there is no axis on this chart to check it against" ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "The reader needs to see that everything that left the first stage arrived somewhere in the second. Conservation follows from the construction; that readers use it is untested."
- "This is a Sankey rather than two stacked bars because which part of A became which part of B is the message." Convention, no study.
- "Nodes are ordered to minimize crossings, and that ordering is mine, not the data's."

**Commonly repeated, and the evidence does not support it:**

- ~~"A Sankey shows where the money went."~~ It shows a source-by-destination tabulation drawn as movement. Whether anything moved is a fact about the data.
- ~~"The ribbon widths are proportional to the volumes, so readers read the volumes off them."~~ The first half is definitional. The second is unmeasured on any flow form.
- ~~"Sankey diagrams are easier to read than chord diagrams."~~ Too strong for small, closing effects on static drawings. Readers *preferred* it and found it less effortful.

## See also

- [../studies/gutwin-2023-chord-vs-sankey.md](../studies/gutwin-2023-chord-vs-sankey.md): the one study of this form
- [flow.md](flow.md): the group and its tests
- [network-topology.md](network-topology.md): the other reading of weighted-graph data
- [chord-diagram.md](chord-diagram.md): one entity set, no stage order
- [part-to-whole.md](part-to-whole.md): the parallel trade
- [../concepts/channels.md](../concepts/channels.md): the inherited channel evidence
