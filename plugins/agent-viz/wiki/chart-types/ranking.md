---
type: index
---

# Ranking

Items in an ordered list, where the reader's question is about the order and not about the sizes.

## Is the order really the question?

The FT's definition is the test ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Use where an item's position in an ordered list is more important than its absolute or relative value. Don't be afraid to highlight the points of interest."

`authority-asserted`. This is the one group defined by what the reader is not asking for. Part-to-whole wants a total, magnitude a size, correlation a co-movement. Ranking wants a place in a sequence, and the value is not the message.

Schwabish's *Better Data Visualizations* has no ranking category. It folds this group and magnitude into Comparing Categories, with Dot Plot there and Bump under Time ([schwabish.md](../sources/schwabish.md); contents pages only, prose unread). That page calls the merge a downgrade: "Comparing Categories swallowing both Magnitude and Ranking loses the FT's sharpest definitional move." A merged category cannot name a question the value does not answer. The two schemes descend from the same 2014 poster, and no experiment sits on either side.

Two tests.

**Would the sentence survive replacing every value with its position?** "Germany is third" is a ranking sentence. "Germany is 3.2 times Poland" is a magnitude sentence dressed as an ordering. If the number has to be in the sentence, the question is next door.

**Is the ordering stable enough to be the message?** Rank is discrete and the values are not. Two items a hair apart get different places, and the chart draws that gap the same way it draws a landslide. This is definitional, not a measured hazard, and it is what the group costs.

| The reader's question | Group |
|---|---|
| How big is each of these, and by how much do they differ? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md), sorted |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| How did this move across many periods, and by how much? | [Change over time](change-over-time.md). A [line chart](line-chart.md) |
| How are the values spread out? | [Distribution](distribution.md) |
| Do two variables move together? | [Correlation](correlation.md). A [scatterplot](scatterplot.md) |
| How far is each item above or below a reference? | Deviation. A diverging bar off that reference |
| Which is biggest, and in what order? | **This group** |
| Who overtook whom? | **This group**, and see [bump-chart.md](bump-chart.md) |
| Did the order change between two dates? | **This group**, and see [slope-chart.md](slope-chart.md) |
| Two values per item, and the gap between them is the point | **This group**, and see [dumbbell-plot.md](dumbbell-plot.md) |

The usual form here is a sorted bar chart, indexed under [magnitude](magnitude.md), since the two groups mostly produce the same object. A handful of forms only make sense once the value has stopped being the message, and they are indexed here. Where a sorted bar chart answers the question, it is the best-evidenced form in this wiki.

## What this group costs

The graphical-perception literature almost entirely measures one task, reading a value off a mark, and Cleveland & McGill state that scope limit themselves ([the scope-limit section of channels.md](../concepts/channels.md#what-the-ranking-is-not-about)). This group's entry condition excludes that task. So the accuracy ordering is irrelevant to choosing among these forms, which does not make them suspect. Nothing in this corpus measures how accurately anyone reads an order off anything.

The accuracy ordering in [channels.md](../concepts/channels.md), which Cleveland & McGill call a ranking, ranks *tasks*. It is unrelated to this page's ranking of items in a dataset.

**Sort order** is a free parameter the reader cannot see, like aspect ratio in [change over time](change-over-time.md). It changes what the figure says, and nothing on the figure marks it. Alphabetical order is a choice too. The BBC cookbook treats it as a bug: "By default, R will display your data in alphabetical order, but arranging it by size instead is simple: just wrap `reorder()` around the x or y variable" ([bbc-cookbook.md](../sources/bbc-cookbook.md)). The Urban Institute reaches the same place from the other direction ([urban-institute.md](../sources/urban-institute.md)):

> "Many graphs and tables encode data by demographic group. Graph producers should take an active role in choosing how to order and present data values for different groups. Urban does not have universal rules about ordering demographic data in visuals, but a few considerations can help you make decisions about order."

`authority-asserted` on both sides.

**The item set** is a second free parameter, because a rank is relative to the set. Add or drop an item and every rank below it moves, though nothing about the other items changed. This is definitional and invisible on every form here, and a rank quoted without its population is not a number.

## Choosing a form

| Form | What carries the order | Defined for |
|---|---|---|
| Sorted [bar chart](bar-chart.md) *(indexed under [magnitude](magnitude.md))* | Arrangement, with the value still on position | The default. Few enough categories to label, and the reader benefits from seeing the sizes too |
| [Lollipop chart](lollipop-chart.md) | Arrangement, with the value on a dot | Enough categories that filled bars become a block of ink. Untested as a form |
| [Dot strip plot](dot-strip-plot.md) | Position on one shared axis, several groups stacked | Many items across several groups, in one axis-height, where seeing them all at once is the point |
| [Dumbbell plot](dumbbell-plot.md) | Two positions per row on one shared axis, with the segment between them drawing the gap | Two values per item, and the levels matter as well as the gap. Where only the gap matters, the differences themselves are the plot |
| [Slope chart](slope-chart.md) | Two endpoint positions, with crossings marking the reorderings | Exactly two periods or two conditions, and which items changed places is the story |
| [Bump chart](bump-chart.md) | Position in the order, on the axis itself | Several periods, and who overtook whom is the whole question. The only form here that discards the value |

Ordered columns are a sorted bar chart with the axes swapped, a layout decision rather than a different form. Ordered proportional symbols put the value on area, which is read less accurately than position ([channels.md](../concepts/channels.md)). Neither has a page.

Three constraints follow from the structure:

- **The value stays on the chart unless something takes it off.** Only the [bump chart](bump-chart.md) drops it, and the drop is the trade it offers.
- **The sort and the population go in a caption line**, since the figure cannot show either.
- **Two rank charts with different item sets are not compared**, because a rank has no scale apart from its set.

## Justifying the choice

**Defensible, evidence-backed:**

The one evidence-backed sentence near this group is about reading values off position, the task this group rules out, and it applies only to the sorted bar:

- "The bars are sorted, and the reader can also read the values off them, because the value sits on position along a common scale. That is the most accurately read channel measured, and the step from this chart to that channel is conjecture, as it is for every chart type."

Nothing in this bucket is about the ordering itself.

**Defensible, with the label said out loud:**

- "Sorted by value rather than alphabetically. Practitioner consensus, not a measured result, and the alternative is whatever order the data arrived in."
- "These groups are ordered by size, and the ordering is an editorial act I made deliberately rather than inherited from the file." Urban's framing, `authority-asserted`.
- "Two periods and eighteen categories, so a slope chart. Convention, endorsed by several practitioners, and no study here tests it."
- "The three items of interest are in color and the rest are gray. The FT says not to be afraid to highlight; the wiki finds no controlled study behind gray-plus-one-accent at all ([refutations.md](../refutations.md#gray-plus-one-accent-as-an-evidence-backed-rule))."

**Commonly repeated, and the evidence does not support it:**

- ~~"Bars beat pies, so a sorted bar chart is the most accurate ranking chart."~~ Two claims spliced together. What was measured is value extraction, which is not this group's task. Nobody has tested which form best supports reading an *order*.
- ~~"A rank chart is easy because the order is right there."~~ Unmeasured on every form here. Only that the order is drawn, rather than computed by the reader, is secure.
- ~~"Lines crossing on a bump chart shows a meaningful change."~~ A crossing shows a reordering of any size, including a trivial one. How large it was is what the rank axis removed.

## The failure mode this group invites

**Publishing a league table whose order is inside the noise.** Every form here gives each item a separate, definite place, and none shows how far apart the items are or how firmly. The ordering looks like the most certain fact on the page when it is often the least certain thing in the data. Perturbing each value by its uncertainty and re-sorting changes the figure. A sentence under the chart that stops being true was about the sorting, not the items. `authority-asserted`, and it follows from the structure rather than from a study.

## Types in this index

- [dot-strip-plot.md](dot-strip-plot.md)
- [dumbbell-plot.md](dumbbell-plot.md)
- [bump-chart.md](bump-chart.md)
- [lollipop-chart.md](lollipop-chart.md): primarily a magnitude chart
- [slope-chart.md](slope-chart.md): primarily a change-over-time chart

None has a study behind it. The evidence in this neighborhood is on the sorted [bar chart](bar-chart.md), indexed under [magnitude](magnitude.md).

## See also

- [magnitude.md](magnitude.md): where the sorted bar chart lives, and the group hardest to separate from this one
- [../concepts/channels.md](../concepts/channels.md): the evidence tier, and why it bears on this group less than on the others
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md): the definition this index is built on
- [README.md](README.md): the page template and the inheritance rule
