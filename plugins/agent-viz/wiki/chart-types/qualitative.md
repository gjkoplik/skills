---
type: index
---

# Qualitative

Figures whose input is text or coded qualitative material rather than a measured quantity.

Like [network-topology.md](network-topology.md) and [tables.md](tables.md), this index is ours. None of the FT's nine relationships has a slot for text or qualitative data ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The precedent is chapter 10 of *Better Data Visualizations*, which covers icons, word clouds, word trees, specific words, quotes, coloring phrases, and matrices and lists ([schwabish.md](../sources/schwabish.md)). Only its contents pages were read.

No study, no style-guide section and no [inventory](../inventory.md) topic covers this group. Schwabish calls the territory "something that seems to have escaped many data visualization books to date", which holds for this corpus too. The missing inventory topic is a candidate rather than an asserted omission, since one publisher's contents line is thin ground.

## Is this group the right frame?

One test decides almost every case: has anything been counted yet? Coded interviews, tagged responses and word frequencies become quantities once counted, and a count goes on a bar chart like any other.

| The reader's question | Group |
|---|---|
| How often does each code appear? | [Magnitude](magnitude.md). A sorted bar chart of the counts |
| How do two coded groups differ? | [Deviation](deviation.md), or a grouped bar in [magnitude](magnitude.md) |
| How did the coding shift over the interviews? | [Change over time](change-over-time.md) |
| What did people say? | [Tables](tables.md). Quotes, matrices and lists are text, and the text is the artifact |
| Which words are frequent, and nothing beyond that? | **This group** |

## What this group costs

Nothing measured. A word cloud puts frequency on text size, an area-like channel, and discards word order, adjacency and context, so it answers "which words are frequent" and nothing else.

- Area is read less accurately than position or angle, inherited from [channels.md](../concepts/channels.md) with the usual conjectural step from chart to channel. [treemap.md](treemap.md) and [bubble-chart.md](bubble-chart.md) carry that inheritance in full.
- The mark's area is not a clean function of the value. Frequency usually maps to font size, so glyph area grows as the square of the value, and a long word covers more canvas than a short one at the same size. That is arithmetic, and it adds to the ordinary area penalty.

## Choosing a form

No basis here for choosing among the forms.

## Justifying the choice

**Defensible, evidence-backed:** nothing.

**Defensible, with the label said out loud:**

- "The codes were counted and the counts went on a bar chart." A magnitude chart with a text-derived variable, inheriting everything on [magnitude.md](magnitude.md).
- "The quotes are printed as quotes." A published catalog files quotes, matrices and lists in this group. `authority-asserted`, from a chapter whose prose nobody here has read.

**Commonly repeated, and the evidence does not support it:**

- ~~"The word cloud shows what the document is about."~~ It shows which words are frequent. Frequency is not aboutness, and order, negation and context are discarded by construction. Nothing here refutes the claim, but it asserts more than the drawing delivers.
- ~~"Bigger words are more important."~~ Bigger words are more frequent, to the extent word length does not interfere.

## The failure mode this group invites

Text made to look measured. These forms carry counts on an unlabeled size channel, with no axis, scale or guide, from material that was often never a quantity, and the picture reads as a result. This is structural, not measured. Where the number behind the figure is a count, it belongs on a magnitude chart.

## Types in this index

None. Most questions that arrive here route out, to [magnitude.md](magnitude.md) or [tables.md](tables.md). Candidates, none with a study or a page: word cloud, word tree, icon array, and coloring phrases inside a printed passage.

## See also

- [../sources/schwabish.md](../sources/schwabish.md): chapter 10's contents, and the candidate inventory topic
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md): the nine relationships, none of which covers this
- [tables.md](tables.md): where quotes, matrices and lists land
- [../concepts/channels.md](../concepts/channels.md): the area evidence a word cloud inherits
- [network-topology.md](network-topology.md): the pattern for an index of ours
