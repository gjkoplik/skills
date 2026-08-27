---
type: chart-type
relationships: [flow, network-topology]
aliases: [Chord diagram]
---

# Chord diagrams

Entities as segments of a ring, flows between them as ribbons crossing the interior, with the segment's arc length encoding an entity's total and each ribbon's width at its endpoints encoding one flow.

## When to reach for it, and when not

**Reach for it when** the flows run within a single set of entities, both directions matter, there is no natural first and last state, and there are few enough entities to label around a circle.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| The movement runs through ordered stages | [Sankey diagram](sankey-diagram.md). Stage order is exactly what the circle throws away |
| Who connects to whom, is there a path, are there communities? | [Node-link](node-link.md) or [adjacency matrix](adjacency-matrix.md), and see [network-topology.md](network-topology.md) |
| There are more than a handful of entities | [Adjacency matrix](adjacency-matrix.md). The interior fills with crossings; the matrix does not degrade |
| What are the exact flows? | A table, or a labeled matrix. The underlying data is a square matrix and reads fine as one |
| How does one total split into parts? | [Part-to-whole](part-to-whole.md) |
| Only the entity totals matter | [Bar chart](bar-chart.md). The ring is a donut you cannot sort |

## Structural decomposition

| Slot | |
|---|---|
| Data | A square matrix over one entity set: one row per (source, target, volume), both directions |
| Transform | Sum incident volumes per entity, then **order the entities around the ring** and the ribbons within each segment |
| Geometry | Annular segment per entity, curved ribbon per flow |
| Scale | Volume to arc length on the ring, and to ribbon width at each endpoint |
| Coordinates | Polar |
| Guides | Labels around the ring, sometimes a tick scale on it. Often a color legend carrying entity identity |

**This is a circular drawing of a weighted graph**, which is why it belongs to [network-topology.md](network-topology.md) as much as to [flow.md](flow.md). The ordering around the ring does the job a layout algorithm does in [node-link.md](node-link.md) and a row ordering does in [adjacency-matrix.md](adjacency-matrix.md): it decides what the picture looks like and it is not in the data.

[Jacques Bertin](../people/jacques-bertin.md) described the construction in 1967, before it had this name, as a "circular construction, elements placed on a circle so every link becomes a straight chord". He argues the circular one gives the least confused image a priori, whatever the number of crossings in the raw data. `authority-asserted`, and firmly so: there are no experiments in that book, and the claim is about the drawing rather than about what a reader extracts from it.

## Channels

**Arc length on a circle** for the entity totals, and **width at two endpoints** for each flow, with the ribbon body read as a region of ink.

There is measurement nearby on the arc-length reading, and it is easy to over-claim. [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) isolated the cues in a circular composition chart and found arc length and area to be what people actually use, with angle the least used and the least accurate. **That was measured on pies and donuts, not on a chord diagram** ([pie-and-donut.md](pie-and-donut.md)). What carries over is a caution rather than a result: a chord ring is a donut rim, so whatever angle contributes on a pie is not available here at all, and the cue the reader is left with is the one Skau & Kosara found doing most of the work anyway.

Everything else is inherited from [channels.md](../concepts/channels.md), including the standing caveat that the step from this chart to those channels is conjecture.

## What it is measurably good at

**Nothing. No study in this corpus tests a chord diagram.**

The two network studies are adjacent and do not transfer. [Ghoniem, Fekete & Castagliola (2004)](../studies/ghoniem-2004.md) measured node-link against adjacency matrix on seven tasks, static displays, random graphs of 20 to 100 nodes at densities 0.2 to 0.6. [Okoe, Jianu & Kobourov (2018)](../studies/okoe-2018.md) measured the same pair on fourteen tasks, interactively, on two real networks of 256 and 332 nodes with 864 participants. Neither included a circular layout, and neither measured reading a weight off an edge.

## What it is measurably bad at

Nothing measured. Two exposures follow from the structure:

**Crossings scale with the number of flows, not the number of entities.** A dense matrix fills the interior with overlapping ribbons and there is no point at which the rendering breaks, only a point past which nothing can be traced. Same gradual failure as the hairball in [node-link.md](node-link.md), and the same reason [adjacency-matrix.md](adjacency-matrix.md) is the escape hatch: cells do not overlap.

**Direction.** Bidirectional flows between the same pair are drawn as one ribbon in many implementations, or as two nested ones, and reading which is which depends on a convention the figure does not state.

## What is contested

Nothing empirical. There is no record here to disagree with itself.

The record disagrees only about filing: Flow for the FT, Relationship for [Schwabish](../sources/schwabish.md), and both readings on this wiki's own account, since the data is a weighted graph and the message is usually volume.

## The failure mode it invites

**Reading the picture as structure.** The ring order is yours, so which ribbons cross which is a property of your ordering. Two chord diagrams of the same matrix under different orderings look like different networks. This is [adjacency-matrix.md](adjacency-matrix.md)'s "reading adjacency as similarity" and [node-link.md](node-link.md)'s "these clusters are communities", in polar coordinates. `authority-asserted`, following from the construction.

**Being chosen because it looks like something.** The chord diagram is the flow group's answer to "show me the network", which [network-topology.md](network-topology.md) names as the request that produces hairballs: a picture with no question behind it has no criterion for being wrong.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing is native to this form.

**Defensible, with the label said out loud:**

- "The flows run within one set of entities in both directions, with no first or last stage, so a circle rather than a Sankey." Structural, and untested.
- "Bertin argued in 1967 that the circular construction gives the least confused image whatever the crossings. Authority-asserted, from a book with no experiments in it."
- "The ring is ordered by region so related entities sit together. My ordering, not the data's."

**Commonly repeated, and the evidence does not support it:**

- ~~"A chord diagram shows the flows between these groups clearly."~~ Nobody has measured what a reader takes from one. It shows them *simultaneously*, which is a claim about the drawing.
- ~~"The segments are read by the angle they subtend."~~ The mechanism story that failed on pies fails harder here: a ring has no wedge reaching the center, so the cue the received account names is the one the form does not have. Arc length and area were what got used, measured on a pie rather than on this chart.

## See also

- [flow.md](flow.md) — the group, and its two tests
- [network-topology.md](network-topology.md) — the other reading of the same weighted-graph data
- [adjacency-matrix.md](adjacency-matrix.md) — the same square matrix drawn so nothing overlaps
- [pie-and-donut.md](pie-and-donut.md) — where the arc-length evidence actually was measured
- [../people/jacques-bertin.md](../people/jacques-bertin.md) — the circular construction, named in 1967
