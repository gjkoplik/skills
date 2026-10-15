---
type: chart-type
relationships: [flow, network-topology]
aliases: [Chord diagram]
---

# Chord diagrams

Entities as segments of a ring and flows between them as ribbons across the interior, with a segment's arc length encoding the entity's total and a ribbon's width at each end encoding one flow.

## When to reach for it, and when not

The form is defined for flows within one set of entities, running both ways, with no natural first or last state, and few enough entities to label around a circle.

| The question | Alternative |
|---|---|
| The movement runs through ordered stages | [Sankey diagram](sankey-diagram.md). The circle throws stage order away |
| Who connects to whom, is there a path, are there communities? | [Node-link](node-link.md) or [adjacency matrix](adjacency-matrix.md). See [network-topology.md](network-topology.md) |
| More than a handful of entities | [Adjacency matrix](adjacency-matrix.md). The ring fills with crossings; the matrix does not degrade |
| What are the exact flows? | A table, or a labeled matrix |
| How does one total split into parts? | [Part-to-whole](part-to-whole.md) |
| Only the entity totals matter | [Bar chart](bar-chart.md). The ring is a donut that cannot be sorted |

## Structural decomposition

| Slot | |
|---|---|
| Data | A square matrix over one entity set: (source, target, volume), both directions |
| Transform | Sum volumes per entity, then order the entities around the ring and the ribbons within each segment |
| Geometry | Annular segment per entity, curved ribbon per flow |
| Scale | Volume to arc length on the ring, and to ribbon width at each endpoint |
| Coordinates | Polar |
| Guides | Labels around the ring, sometimes a tick scale, often a color legend for identity |

It is a circular drawing of a weighted graph, so it belongs to [network-topology.md](network-topology.md) as much as to [flow.md](flow.md). The ring order does the job of a layout algorithm in [node-link.md](node-link.md) or a row ordering in [adjacency-matrix.md](adjacency-matrix.md): it shapes the picture and is not in the data. [Jacques Bertin](../people/jacques-bertin.md) described the circular construction in 1967, elements placed on a circle so every link becomes a straight chord, and argued it gives the least confused image whatever the crossings, `authority-asserted` from a book with no experiments.

## Channels

Totals sit on arc length, flows on width at two endpoints, with the ribbon body read as a region of ink. The step from chart to channel is conjecture ([channels.md](../concepts/channels.md)). On pies and donuts, [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) found readers use arc length and area, with angle least used and least accurate ([pie-and-donut.md](pie-and-donut.md)). A chord ring is a donut rim with no angle to read, which makes that a caution here, not a result.

## What it is measurably good at

No measured advantage. [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md), the only test of the form, compared it with a [Sankey diagram](sankey-diagram.md). By a reader's fourth question of a type, "there is little difference between the two types" on time.

Two network studies drew no circular layout and asked for no edge weight, so they do not transfer: [Ghoniem, Fekete & Castagliola (2004)](../studies/ghoniem-2004.md), seven static tasks on random graphs of 20 to 100 nodes at densities 0.2 to 0.6, and [Okoe, Jianu & Kobourov (2018)](../studies/okoe-2018.md), fourteen interactive tasks on real networks of 256 and 332 nodes with 864 participants.

## What it is measurably bad at

First reading. Gutwin et al. put 51 novices through 2,040 trials on static chord and Sankey drawings of the same 8-to-15-node flow data. Chord was slower (22.01s against 18.35s per question), marginally less accurate (1.07 errors against 0.96), more effortful, and preferred by 9 of 51. By the paper's thresholds the effects are small: generalized η² = 0.02 for time and 0.001 for errors, against "< .01 considered small". They concentrate on first exposure, 9.2s and 0.42 errors on the first iteration against 3.7s and 0.1 overall. The stimuli were static, and hover highlighting fixes all three of the authors' proposed mechanisms (tracing a ribbon, seeing an arrowhead, separating incoming from outgoing links at a shared node).

Preference moved more: 42 of 51 preferred Sankey, and 43 of 51 believed they were more accurate with it. Counting links at a node drew high chord error, attributed to incoming and outgoing links sharing a segment, and absent in the one-way dataset.

Two structural exposures are unmeasured. Crossings scale with flows, not entities, until nothing can be traced, the [node-link.md](node-link.md) hairball that [adjacency-matrix.md](adjacency-matrix.md) escapes because cells do not overlap. And a bidirectional pair is one ribbon or two nested ones, by an unstated convention.

## What is contested

How much the one paper weighs. Its headline, "substantially longer and more errors", rests on small, fading, static-only effects. The numbers support "static chord diagrams cost a novice a few seconds a question", not the common citation "chord diagrams are worse than Sankeys". [Okoe et al. (2018)](../studies/okoe-2018.md) reversed the static [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) result by adding interaction, so this one is provisional on the same ground.

Filing splits too: Flow for the FT, Relationship for [Schwabish](../sources/schwabish.md).

## The failure mode it invites

**Reading the ring order as structure.** Two orderings of one matrix can look like different networks. It is [adjacency-matrix.md](adjacency-matrix.md)'s "reading adjacency as similarity" and [node-link.md](node-link.md)'s "these clusters are communities" in polar coordinates. `authority-asserted`, from the construction.

**Being chosen because it looks like something.** It answers "show me the network", the request [network-topology.md](network-topology.md) names as the source of hairballs.

## Justifying the choice

**Defensible, evidence-backed:**

- "The readers are analysts who will use this repeatedly, not a one-look audience, so the first-exposure cost measured against a Sankey has mostly worn off by the fourth question." [Gutwin et al. (2023)](../studies/gutwin-2023-chord-vs-sankey.md), static 8-to-15-node directed data.
- Against the form: "This is a one-look news graphic, and novices reading a static chord diagram took about nine extra seconds and made about half an extra error on their first question of each type."

**Defensible, with the label said out loud:**

- "The flows run within one set of entities in both directions, with no first or last stage, so a circle rather than a Sankey." Structural, and untested.
- "Bertin argued in 1967 that the circular construction gives the least confused image whatever the crossings. Authority-asserted, from a book with no experiments in it."
- "The ring is ordered by region so related entities sit together. My ordering, not the data's."

**Commonly repeated, and the evidence does not support it:**

- ~~"A chord diagram shows the flows between these groups clearly."~~ Measured slower and more effortful, and 43 of 51 thought they read it *less* accurately. It shows the flows *simultaneously*.
- ~~"Readers find the circular layout intuitive."~~ Novices did not. They cited left-to-right familiarity.
- ~~"Chord diagrams are worse than Sankey diagrams."~~ One static study, effect sizes of 0.02 and 0.001, gone by the fourth exposure.
- ~~"The segments are read by the angle they subtend."~~ A ring has no wedge reaching the center.

## See also

- [../studies/gutwin-2023-chord-vs-sankey.md](../studies/gutwin-2023-chord-vs-sankey.md): the only study that tests the form
- [flow.md](flow.md): the group, and its two tests
- [network-topology.md](network-topology.md): the other reading of the same data
- [adjacency-matrix.md](adjacency-matrix.md): the same matrix drawn so nothing overlaps
- [pie-and-donut.md](pie-and-donut.md): where the arc-length evidence was measured
- [../people/jacques-bertin.md](../people/jacques-bertin.md): the circular construction, 1967
