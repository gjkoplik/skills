# Chart types

**What it is.** One page per chart type, stored flat, with separate **index pages** that group them by data relationship. Deliberately the *shallow* tier of a two-tier structure: the evidence lives one level up in [../concepts/channels.md](../concepts/channels.md), and these pages inherit it.

**Status.** Structure complete, coverage partial. Six type pages, two indexes. See [Coverage](#coverage).

**What it is good for.** Choosing a form for a specific dataset and question, and being able to defend the choice afterward. Two entry points: arrive with a question ("this is composition") and get pointed at the candidates, or arrive with a named chart and go straight to its page.

**What it does not settle.** It will not hand you an answer from a lookup table, because the answer depends on the reader's question rather than on the shape of the data. What it does is narrow the candidates, name what each one costs, and tell you which justifications hold up. Where the evidence is silent it says so rather than inventing a tiebreaker.

---

## Taxonomy is an index, not a home

Every type page lives directly in this directory. Grouping happens in index pages that point at them.

**A data relationship is a view of a chart, not a property of it.** A stacked bar is part-to-whole; it is also magnitude, and it is change-over-time the moment you make it an area chart. A dot plot is ranking and distribution. A directory tree forces each type into exactly one home and demotes its other readings to cross-links, which encodes a claim about the type that is not true. Flat storage lets a type appear in three indexes with no duplication.

Three consequences, all of which are why this is the structure rather than a compromise:

**Nobody's taxonomy gets amended.** The FT's nine relationships are an authority-asserted scheme by other people. An earlier draft of this tier added a tenth category for networks, which meant editing that scheme while still citing it, the exact degradation this project exists to catch. Under indexes, the FT nine stay as published and [network-topology.md](network-topology.md) is visibly an index of ours, sitting alongside rather than inside.

**Paths are stable.** Reclassifying a type is an edit to an index, not a file move that breaks every inbound link. This wiki is densely cross-linked and that matters.

**Bespoke forms have somewhere to go.** A chart that fits no relationship cleanly still gets a page. It just appears in fewer indexes, or in none, and that is information rather than a filing problem.

**Membership is declared on the page**, in a `**Relationships.**` line in each type page's header, so an index can be checked against the pages rather than maintained by hand. This is the trick [roll-call.md](../roll-call.md) plays against [inventory.md](../inventory.md): the audit is possible because the claim is written down in two places that must agree.

## The indexes

**[part-to-whole.md](part-to-whole.md)** and **[network-topology.md](network-topology.md)** are written. They are more than pointer lists: each carries the argument that is common to its group, which is the part that would otherwise be repeated on every member page.

The seven remaining FT relationships (Deviation, Correlation, Ranking, Distribution, Change over Time, Magnitude, Spatial, Flow) have no index yet. An unlinked relationship in a type page's header means exactly that.

**Provenance.** The Visual Vocabulary is not the origin of these nine: it credits the Graphic Continuum by Jon Schwabish and Severino Ribecca (2014). Crediting only the FT credits the derivative, and it explains the heavy overlap with Schwabish's *Better Data Visualizations*, which is descent rather than convergence. The full source page is [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md), which also carries the copyright note: the FT material is all rights reserved and can be cited but not copied.

**Evidence class of the taxonomy itself: `authority-asserted`.** No experiment establishes that these are the right nine, that they are exhaustive, or that they are mutually exclusive. It is a well-designed practitioner scheme that works for retrieval. Used here as an index, not as a claim.

Other index axes are possible on the same flat store and would be genuinely useful: an index **by channel** (every type that puts the reader on area) would fall straight out of the decomposition already on each page.

## Who these pages are for, and what that rules out

**The reader is someone standing in front of a dataset who has to pick a form and defend the pick.** Usually an agent, sometimes a person. Every section on every page earns its place by helping with that, or it comes out.

Three consequences, and the first two are where the early drafts of this tier went wrong:

**Lead with the choice, not the anatomy.** The first substantive question is always *is this group even the right frame for the reader's question*, because the most common failure is not picking the wrong chart within a group, it is being in the wrong group. Composition charts get reached for when the question is really ranking. Network diagrams get drawn when the question is answerable from a per-node table. That section goes first, before structure, channels or evidence.

**No process narration.** How this wiki was built, which page was written first, what is a "shape-setter" for the tier, what remains uncovered: none of it helps someone choose a chart. Coverage and status belong in this README. They do not belong on a page an agent reads to make a decision.

**Give it the sentences.** The reader has to *justify* the choice to someone. Pages carry a short "justifying the choice" section: what is defensible and evidence-backed, what is defensible with the label said out loud, and what is commonly said and wrong. That last one is where this wiki's research actually pays off, and it is useless if it only exists in `refutations.md`.

## The page template

**Index pages** (one per relationship) carry: is this group the right frame, and how to tell; what the group costs, in channel terms; how to choose a form within it; how to justify the choice; the failure mode the group invites; the types it indexes.

**Type pages** carry, after the standard wiki header plus a `**Relationships.**` line:

**1. When to reach for it, and when not.** The conditions under which this form is the right answer, and the nearest alternative when it is not.

**2. Structural decomposition.** Six slots, borrowed from Wilkinson's *Grammar of Graphics* by way of ggplot2's layered restatement:

| Slot | The question |
|---|---|
| Data | What is one row |
| Transform | What statistic is computed before drawing, if any |
| Geometry | What mark is drawn |
| Scale | How values map to the mark's properties |
| Coordinates | What space the mark is placed in |
| Guides | What axes, legends and reference marks are required to read it |

**These slots carry no evidence label.** They are definitional: they describe what the chart *is* and assert nothing empirical. Labeling them would dilute the labels on rows that are actually claims. See [../concepts/evidence-class.md](../concepts/evidence-class.md#what-is-exempt-and-why-the-exemption-matters).

The decomposition earns its place by collapsing near-duplicates. A coxcomb is a bar chart with polar coordinates. An area chart is a line chart with a fill. Stacked and grouped bars differ in one transform slot. Without it, this tier becomes sixty pages holding ten pages of content.

**3. Channels.** Which perceptual channel the mark puts the reader on, primary and secondary, linking to [../concepts/channels.md](../concepts/channels.md). Flagged as conjecture unless a study has decomposed this specific type, which for most types it has not.

**4. What it is measurably good at.** Only claims traceable to a study. Cited, with the effect.

**5. What it is measurably bad at.** Same bar.

**6. What is contested.** Where the record disagrees with itself, both sides named.

**7. The failure mode it invites.** What goes wrong in practice. Usually `authority-asserted`, and labeled as such.

**8. Justifying the choice.** The defensible sentences, and the commonly repeated ones that the evidence does not support.

## The inheritance rule

**Evidence attaches to channels, not to chart types.** No controlled study has tested a chart type as an artifact in the world; they test stripped judgment tasks on stimuli that resemble one. So every accuracy claim on these pages is a two-step inference, and the first step (this chart puts the reader on that channel) is conjecture in the source literature, flagged as such by Cleveland and McGill every time they make it.

A type page may therefore **inherit** an accuracy claim with a link. It may not **restate** it as a native finding, and it may not present the mapping as settled when the source calls it a conjecture. The full argument is in [../concepts/channels.md](../concepts/channels.md).

Where a study *has* decomposed a specific type into its channels, that is a genuine type-level finding and belongs here rather than upstream. [pie-and-donut.md](pie-and-donut.md) is the model case and currently the only one.

## Where the evidence runs out

Stated up front, because it determines how thin most of this tier has to be:

- The graphical-perception literature concentrates almost entirely on **proportional judgment**: read a value off a mark, report it as a number. Groups whose job is something else inherit very little from it.
- Most individual chart types have **no study at all**. Pie, donut, treemap and bar are unusually well studied. Violin plots, slope charts, connected scatterplots, bump charts and most of the flow family are not.
- A page with nothing to inherit says so and stops. Padding it with plausible practitioner advice dressed as findings is the specific failure this structure exists to avoid. [hive-plot.md](hive-plot.md) is the page where that discipline costs the most: two papers describe the form in detail and neither ran a user study, so the page separates what follows from the construction (secure, and stated flatly) from what would need an experiment (absent, and stated as absent).

## Coverage

**Type pages**

| Page | Relationships | Evidence |
|---|---|---|
| [pie-and-donut.md](pie-and-donut.md) | Part-to-whole | Two studies, one a direct channel decomposition |
| [stacked-bar.md](stacked-bar.md) | Part-to-whole, Change over Time, Magnitude | Directly tested; it was the 1984 stimulus |
| [treemap.md](treemap.md) | Part-to-whole, Magnitude | One study, incl. the aspect-ratio result |
| [node-link.md](node-link.md) | Network and topology | Two studies that disagree |
| [adjacency-matrix.md](adjacency-matrix.md) | Network and topology | Same two |
| [hive-plot.md](hive-plot.md) | Network and topology | Two `primary-read` sources, **neither containing a user study** |

**Indexes**

| Index | Status |
|---|---|
| [part-to-whole.md](part-to-whole.md) | Written to depth. The shape-setter for the tier |
| [network-topology.md](network-topology.md) | Written. Ours, not the FT's |
| Deviation, Correlation, Ranking, Distribution, Change over Time, Magnitude, Spatial, Flow | Not written |

Part-to-whole was done first deliberately: it is where the channel evidence is densest, which forces the inheritance rule to be right before it gets applied to groups where there is nothing to inherit.

## See also

- [../concepts/channels.md](../concepts/channels.md) — the evidence tier these pages inherit from
- [../concepts/evidence-class.md](../concepts/evidence-class.md) — the labeling discipline, and the definitional exemption
- [../inventory.md](../inventory.md) — topic 5 is the chart-type-selection rule these pages serve
