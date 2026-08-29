---
type: index
---

# Flow

A quantity moving between states or conditions, drawn so that both the size of the movement and where it goes are visible at once.

The FT's definition is the one this index uses ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Show the reader volumes or intensity of movement between two or more states or conditions. These might be logical sequences or geographical locations."

**That demands two things: a volume, and a between.** Without both, the question belongs to another group.

It is also the least stable category in the two taxonomies this wiki uses. [Schwabish](../sources/schwabish.md) files Sankey and waterfall under Comparing Categories, chord under Relationship, and has no Flow category at all; the FT files Sankey under Flow, waterfall under both Part-to-whole and Flow, and chord and networks under Flow. As that page puts it: "Three placements for two charts across two schemes is the clearest available evidence that these taxonomies are retrieval aids rather than facts about charts." This index locates candidates; it does not settle what a chart is.

## Is flow the message, or just the shape of the data?

Three tests, and a form here needs all three.

**Is there a quantity?** Not a connection, a quantity: dollars, people, packets, kilowatt-hours, students. If the data records only that A relates to B, there is no volume to give a width to, and the whole group collapses to a network drawing with fat edges.

**Is there a real between?** Two or more states, and rows that genuinely move from one to the other. A cross-tabulation of two attributes of the same rows is not movement. It draws identically and asserts something the data does not contain, which is this group's characteristic lie.

**Does the movement matter more than the endpoints?** If the message is "the total fell by 12" or "these five sources are the biggest", the sizes at the ends are the answer and the ribbons are decoration.

| The reader's actual question | Group |
|---|---|
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md) |
| Which is biggest, and in what order? | Ranking. A sorted bar chart |
| How does this one total break down? | [Part-to-whole](part-to-whole.md). A [stacked bar](stacked-bar.md) or a [treemap](treemap.md) |
| How did the total move across many periods? | [Change over time](change-over-time.md). A [line chart](line-chart.md) |
| Who connects to whom, is there a path, are there communities? | [Network and topology](network-topology.md) |
| How far is each item from a target? | Deviation. No index here |
| Where does the quantity go, and does it add up on the way? | **This group** |

## Flow is a message; a network is a dataset

The FT files networks in this group. This wiki does not, and [network-topology.md](network-topology.md) carries the argument: flow is one message relational data can carry, alongside community structure, degree distribution and path, so filing the whole class here routes every network question through a category built for Sankeys. Schwabish's scheme lands on the same split from the other direction, filing network, chord, arc and tree under Relationship.

The two indexes overlap on exactly the forms that draw a weighted graph. A [Sankey diagram](sankey-diagram.md) and a [chord diagram](chord-diagram.md) are both weighted-graph drawings and both belong to both readings: this index holds the question of how much went where, and [network-topology.md](network-topology.md) holds the question of how the connections are structured. Neither index resolves which question a given dataset carries.

## What this group costs

**Almost nothing here is read as position along a common scale**, which is the channel measured most accurately ([channels.md](../concepts/channels.md)).

- A Sankey ribbon is a width at each node, stacked against its neighbors with no common baseline, and a band of ink along its path. Width at a node is a length reading; the path is closer to area.
- A chord's ring segment is arc length on a circle, and its ribbons are widths at two endpoints.
- A waterfall's step is a floating bar. Only the opening bar and any explicitly drawn totals touch the axis.

That is the same trade [part-to-whole](part-to-whole.md) makes: value-reading accuracy spent for a constraint the form makes visible. Those accuracy claims are inherited with the link; none of them was measured on a chart in this group.

**The second cost is a free parameter the reader cannot see.** Every form here orders something to reduce crossings: nodes into columns and ribbons within a node for a Sankey, entities around the ring for a chord, steps along the axis for a waterfall. That ordering changes the picture without changing a number, exactly as a layout algorithm does for a [node-link diagram](node-link.md) and an ordering does for an [adjacency matrix](adjacency-matrix.md). It is structural rather than stylistic, and it is unmeasured everywhere.

## Choosing a form

| Form | What carries the value | Where it applies |
|---|---|---|
| [Sankey diagram](sankey-diagram.md) | Ribbon width | Directed movement through ordered states, with the volume conserving at every node as part of the reading |
| [Chord diagram](chord-diagram.md) | Ring arc length, plus ribbon width at each end | Flows run within one set of entities, in both directions, with no natural first and last state |
| [Waterfall chart](waterfall-chart.md) | Floating bar length, with the running total at each bar's end | One total decomposes into an ordered sequence of additions and subtractions |
| Alluvial diagram or parallel sets *(no page yet)* | Ribbon width | Category membership is tracked across several steps and the crossings are the message |
| [Flow map](flow-map.md) | Line width on a geography | The states are places and their positions are the point. The one form here whose arrangement is not a design choice |

Two constraints, both following from structure rather than taste:

- **One width-per-unit scale across the whole figure.** A Sankey or chord with per-column scaling is uncomparable in the direction the reader is looking, and nothing on the chart shows it.
- **The volumes meant to be read are labeled.** Every value in this group sits on a channel measured worse than position for value extraction, and there is usually no axis at all.

## Justifying the choice

**Defensible, evidence-backed:**

**One thing, and it is about layout rather than about flow.** [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md) put 51 novices through 2,040 trials on static [Sankey](sankey-diagram.md) and [chord](chord-diagram.md) drawings of the same 8-to-15-node directed data. The linear layout won on time (18.35s against 22.01s), on errors (0.96 against 1.07 per question), on four effort scales and on preference by 42 to 9.

- "A Sankey rather than a chord diagram, because this is a one-look audience with no interaction available." Defensible, with the numbers said out loud: the performance gap is small by the paper's own thresholds (generalized η² of 0.02 and 0.001), it is largest on first exposure (9.2s and 0.42 errors) and close to gone by the fourth, and the stimuli had no hover highlighting. The large effect is subjective, not performance.

**That is the whole of it.** No study here tests a waterfall, an alluvial diagram or a [flow map](flow-map.md), and none tests whether a reader can get a volume off a ribbon width, which is the claim every form in this group actually rests on. The other nearby work, [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md), compared node-link diagrams against adjacency matrices on task batteries at given node counts and densities, and included no form in this index.

What is inheritable, with the link, is channel-level:

- "The flow volumes are labeled, because a ribbon width is a floating length judgment rather than a position one" ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "This is a Sankey rather than two stacked bars because the reader needs to see which parts of the first total became which parts of the second." The conservation reading follows from the construction. That readers do better with it is untested.
- "The steps are in the order the accounts are reported, not in the order things happened." Structural, and not recoverable from the drawing.
- "The entities are ordered around the ring by region rather than by size, so the groups read together." Practitioner convention, no measured threshold.

**Commonly repeated, and the evidence does not support it:**

- ~~"A Sankey shows the reader where the money went."~~ It shows one tabulation of source against destination, drawn as movement. Whether anything moved is a property of the data, not of the chart.
- ~~"These forms make the volumes obvious."~~ Nobody has measured whether a reader can get a volume off any of them. The one study here compared two layouts on lookup and comparison tasks and never asked for a quantity. These forms make the volumes *visible*, which is a different claim.
- ~~"The circular layout is the intuitive one for flows between groups."~~ Novices reading a static chord diagram were slower, more error-prone and much more frustrated than with the linear equivalent, and said the left-to-right frame was why.

## The failure mode this group invites

**Asserting movement that the data does not contain.** A ribbon between two boxes says a quantity left one state and arrived in the other. Cross-tabulated attributes, survey responses to two questions, and a spend breakdown by two dimensions all produce a valid-looking Sankey and none of them describes anything moving. The form supplies the narrative for free and the reader has no way to check it.

A check on that: the rows named, then what happened to them stated out loud. A sentence with no verb of motion the data actually recorded describes a composition chart drawn as a flow.

## Types in this index

- [sankey-diagram.md](sankey-diagram.md), which is also a weighted-network drawing
- [chord-diagram.md](chord-diagram.md), which is also a weighted-network drawing
- [waterfall-chart.md](waterfall-chart.md), which is a stacked bar taken apart along an axis of steps
- [flow-map.md](flow-map.md), which is the only one whose node positions are not a design choice. **Both source taxonomies file it under Spatial rather than here**; the flow membership is this wiki's reading

Alluvial diagrams, parallel sets and stream graphs all belong to this group and none has a page, because no study in this corpus tests any of them and no source read here defines either of the first two names.

## See also

- [network-topology.md](network-topology.md) — the other reading of the same weighted-graph data, and why this index does not swallow it
- [part-to-whole.md](part-to-whole.md) — the same trade, made for a different constraint
- [../concepts/channels.md](../concepts/channels.md) — what the widths and arcs here are read on
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) — the category definition
- [../sources/schwabish.md](../sources/schwabish.md) — a second taxonomy with no Flow category at all
