---
type: index
---

# Qualitative

Figures whose input is text or coded qualitative material rather than a measured quantity.

This index is ours rather than the FT's, on the same footing as [network-topology.md](network-topology.md) and [tables.md](tables.md): the nine relationships stay as published and this one sits alongside them. The FT taxonomy has no slot for text or qualitative data at all ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The citable precedent for putting one in a chart catalog is *Better Data Visualizations*, whose chapter 10 is Qualitative and covers icons, word clouds, word trees, specific words, quotes, coloring phrases, and matrices and lists ([schwabish.md](../sources/schwabish.md)). That is the chapter's existence and contents, verified from the book's own contents pages; what it argues is unread in this corpus and is not cited below.

**This page is short because the tier has almost nothing to say here.** No study, no style-guide section, and no [inventory](../inventory.md) topic. Schwabish calls a chapter's worth of this "something that seems to have escaped many data visualization books to date", and that holds for this corpus too, so a missing inventory topic is recorded as a candidate rather than asserted as an omission. One publisher's contents line is thin ground.

## Is this group the right frame?

One test decides almost every case: **has anything been counted yet?** Coded interviews, tagged responses and word frequencies become quantities the moment the count exists, and a count goes on a bar chart like any other count. Once you are counting, you have left this group.

| The reader's actual question | Go to |
|---|---|
| How often does each code appear? | [Magnitude](magnitude.md). A sorted bar chart of the counts |
| How do two coded groups differ? | [Deviation](deviation.md), or a grouped bar in [magnitude](magnitude.md) |
| How did the coding shift over the interviews? | [Change over time](change-over-time.md) |
| What did people actually say? | [Tables](tables.md). Quotes, matrices and lists are text, and the text is the artifact |
| Which words are frequent, and nothing beyond that? | **Stay here** |

## What this group costs

Nothing measured. No study in this corpus tests any form in this group, and no style guide here has a section on it.

One thing follows from the structure, and it is the only claim on this page: **a word cloud puts frequency on text size, which is an area-like channel, and it discards word order, adjacency and context entirely.** So it answers "which words are frequent" and nothing else. Two consequences:

- Area is read less accurately than position or angle, inherited from [channels.md](../concepts/channels.md) with the same conjectural step every type page takes to get from a chart to a channel. [treemap.md](treemap.md) and [bubble-chart.md](bubble-chart.md) carry that inheritance in full and nothing here adds to it.
- **The mark's area is not a clean function of the value.** Frequency is normally mapped to font size, so glyph area grows as the square of the value, and a long word covers more canvas than a short one set at the same size. That is arithmetic rather than measurement, and it is a defect on top of the ordinary area penalty rather than the same one.

## Choosing a form

No basis here for choosing among them. The one catalog in this corpus with such a chapter files icons, word clouds, word trees, specific words, quotes, coloring phrases, and matrices and lists under it, and its prose is unread here.

## Justifying the choice

**Defensible, evidence-backed:** nothing. Nothing in this group has been measured.

**Defensible, with the label said out loud:**

- "The codes were counted and the counts went on a bar chart." That is a magnitude chart with a text-derived variable, and it inherits everything on [magnitude.md](magnitude.md). Say it that way rather than calling it qualitative visualization.
- "The quotes are printed as quotes." A published catalog files quotes, matrices and lists as forms in this group, so the precedent exists. `authority-asserted`, from a chapter nobody here has opened.

**Commonly repeated, and the evidence does not support it:**

- ~~"The word cloud shows what the document is about."~~ It shows which words are frequent. Frequency is not aboutness, and order, negation and context are discarded by construction. Nothing here refutes the claim; it simply asserts more than the drawing delivers.
- ~~"Bigger words are more important."~~ Bigger words are more frequent, to the extent that word length is not getting in the way.

## The failure mode this group invites

**Text made to look measured.** These forms produce a figure with no axis, no scale and no guide, carrying counts on an unlabeled size channel, from material that was often never a quantity. The picture reads as a result. Structural rather than measured, and the cheap check is whether you could put a number on the figure: if the answer is a count, draw the count.

## Types in this index

None, and the index does not want any. For most questions that arrive here the honest route is out, into [magnitude.md](magnitude.md) or [tables.md](tables.md).

Candidates, none of which has a study or a page: word cloud, word tree, icon array, and coloring phrases inside a printed passage.

## See also

- [../sources/schwabish.md](../sources/schwabish.md) — chapter 10's contents, and the candidate missing inventory topic
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) — the nine relationships, none of which covers this
- [tables.md](tables.md) — where quotes, matrices and lists actually land
- [../concepts/channels.md](../concepts/channels.md) — the area evidence a word cloud inherits, and the conjectural step it takes to get there
- [network-topology.md](network-topology.md) — the pattern for an index of ours sitting alongside the FT nine
