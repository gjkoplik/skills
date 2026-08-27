---
type: index
---

# Ranking

Items in an ordered list, where the reader's question is about the order and not about the sizes.

## Is the order really the question?

The FT's definition is the whole test ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Use where an item's position in an ordered list is more important than its absolute or relative value. Don't be afraid to highlight the points of interest."

`authority-asserted`. **This is the one group defined by what the reader is not asking for.** Part-to-whole wants a total, magnitude wants a size, correlation wants a co-movement. Ranking wants a place in a sequence, and says explicitly that the value is not the message.

Two tests follow from that.

**Would your sentence survive replacing every value with its position?** "Germany is third" is a ranking sentence. "Germany is 3.2 times Poland" is a magnitude sentence wearing an ordering. If the number has to be in the sentence, you are next door.

**Is the ordering stable enough to be the message?** Rank is discrete and the underlying values are not. Two items a hair apart get different places, and the chart draws that gap the same way it draws a landslide. This is definitional rather than a hazard someone measured, and it is what the group costs.

If a test fails, you are in a different group:

| The reader's actual question | Go to |
|---|---|
| How big is each of these, and by how much do they differ? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md), sorted |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| How did this move across many periods, and by how much? | [Change over time](change-over-time.md). A [line chart](line-chart.md) |
| How are the values spread out? | [Distribution](distribution.md) |
| Do two variables move together? | [Correlation](correlation.md). A [scatterplot](scatterplot.md) |
| How far is each item above or below a reference? | Deviation. A diverging bar off that reference |
| Which is biggest, and in what order? | **Stay here** |
| Who overtook whom? | **Stay here**, and see [bump-chart.md](bump-chart.md) |
| Did the order change between two dates? | **Stay here**, and see [slope-chart.md](slope-chart.md) |
| Two values per item, and the gap between them is the point | **Stay here**, and see [dumbbell-plot.md](dumbbell-plot.md) |

**The usual right answer here is a sorted bar chart, and it is indexed under [magnitude](magnitude.md).** That index says the same thing from its side, that magnitude and ranking mostly hand you the same object. This group earns a separate index because a handful of forms exist that only make sense once the value has stopped being the message, not because the ordinary case needs a special shape. If you arrived here and a sorted bar chart answers the question, take it: it is the best-evidenced form in this wiki.

## What this group costs

**The evidence does not follow you into this group.** Almost the whole graphical-perception literature measures one task: read a value off a mark and report it as a number. Cleveland & McGill state the scope limit themselves, and it is quoted in [the scope-limit section of channels.md](../concepts/channels.md#what-the-ranking-is-not-about). A group whose entry condition is *the value is not what the reader wants* has, by construction, defined itself out of the task that was measured.

That does not make the forms here suspect. It makes the accuracy ordering irrelevant to choosing among them. Nothing in this corpus measures how accurately anyone reads an order off anything.

Two words called "ranking" collide in this wiki and they are unrelated. This page is about charts of an ordered list. [channels.md](../concepts/channels.md) is about Cleveland & McGill's accuracy ordering over channels, which they call a ranking and which is a ranking of *tasks*, not of items in a dataset.

**Sorting is a free parameter, and the reader cannot see it.** It sits in the same family as aspect ratio in [change over time](change-over-time.md): a choice you make that changes what the figure says, with nothing on the figure to mark that a choice was made. Alphabetical order is a choice, and so is sorting by the value. The BBC cookbook treats the alphabetical default as a bug rather than a design decision, "By default, R will display your data in alphabetical order, but arranging it by size instead is simple: just wrap `reorder()` around the x or y variable" ([bbc-cookbook.md](../sources/bbc-cookbook.md)). The Urban Institute reaches the same place from the other direction, and its version is the one worth keeping ([urban-institute.md](../sources/urban-institute.md)):

> "Many graphs and tables encode data by demographic group. Graph producers should take an active role in choosing how to order and present data values for different groups. Urban does not have universal rules about ordering demographic data in visuals, but a few considerations can help you make decisions about order."

`authority-asserted` on both sides, and unusually cheap to comply with: pick an order, and be able to say why.

**A rank is relative to the set, so the set is a second free parameter.** Add an item and every rank below it moves; drop one and they move back. Nothing about the remaining items changed. Definitional, secure, and invisible on every form in this group. It is why two rank charts built from different item sets cannot be compared, and why a rank quoted without its population is not a number.

## Choosing a form

| Form | What carries the order | Reach for it when |
|---|---|---|
| Sorted [bar chart](bar-chart.md) *(indexed under [magnitude](magnitude.md))* | Arrangement, with the value still on position | The default. Few enough categories to label, and the reader benefits from seeing the sizes too |
| [Lollipop chart](lollipop-chart.md) | Arrangement, with the value on a dot | Enough categories that filled bars become a block of ink. Untested as a form |
| [Dot strip plot](dot-strip-plot.md) | Position on one shared axis, several groups stacked | Many items across several groups, in one axis-height, where seeing them all at once is the point |
| [Dumbbell plot](dumbbell-plot.md) | Two positions per row on one shared axis, with the segment between them drawing the gap | Two values per item, and the levels matter as well as the gap. If only the gap matters, plot the differences instead |
| [Slope chart](slope-chart.md) | Two endpoint positions, with crossings marking the reorderings | Exactly two periods or two conditions, and which items changed places is the story |
| [Bump chart](bump-chart.md) | Position in the order, on the axis itself | Several periods, and who overtook whom is the whole question. The only form here that discards the value |

Ordered columns are a sorted bar chart with the axes swapped, which is a layout decision rather than a different form. Ordered proportional symbols put the value on area, which is measured as read less accurately than position ([channels.md](../concepts/channels.md)); neither has a page.

Three constraints that follow from the structure rather than from taste:

- **Keep the value on the chart unless you have a reason to remove it.** Four of the five forms above do. The [bump chart](bump-chart.md) is the exception, and the discard is the whole trade it offers.
- **State the sort, and state the population.** Both are choices the figure cannot show. A caption line does it.
- **Do not compare two rank charts with different item sets.** The ranks are not on the same scale, because a rank has no scale independent of the set it came from.

## Justifying the choice

**Defensible, evidence-backed:**

Almost nothing, and the reason is structural rather than an accident of coverage. The one evidence-backed sentence available anywhere near this group is about reading values off position along a common scale, which is the task you said was not the question when you filed the chart here. It is worth having anyway, and only for the sorted bar:

- "The bars are sorted, and the reader can also read the values off them, because the value sits on position along a common scale. That is the most accurately read channel measured, and the step from this chart to that channel is conjecture, as it is for every chart type."

Nothing in this bucket is about the ordering itself.

**Defensible, with the label said out loud:**

- "Sorted by value rather than alphabetically. Practitioner consensus, not a measured result, and the alternative is whatever order the data arrived in."
- "These groups are ordered by size, and the ordering is an editorial act I made deliberately rather than inherited from the file." Urban's framing, `authority-asserted`.
- "Two periods and eighteen categories, so a slope chart. Convention, endorsed by several practitioners, and no study here tests it."
- "The three items of interest are in color and the rest are gray. The FT says not to be afraid to highlight; the wiki finds no controlled study behind gray-plus-one-accent at all ([refutations.md](../refutations.md#gray-plus-one-accent-as-an-evidence-backed-rule))."

**Commonly repeated, and the evidence does not support it:**

- ~~"Bars beat pies, so a sorted bar chart is the most accurate ranking chart."~~ Two different claims spliced together. What was measured is value extraction, which is by definition not this group's task. Nobody has tested which form supports reading an *order* best, so "most accurate ranking chart" names a comparison that has never been run.
- ~~"A rank chart is easy because the order is right there."~~ Unmeasured, on every form in this group. What is secure is only that the order is drawn without the reader having to compute it.
- ~~"Lines crossing on a bump chart shows a meaningful change."~~ Definitionally, a crossing shows a reordering of any size, including a trivial one. How large it was is the information the rank axis removed.

## The failure mode this group invites

**Publishing a league table whose order is inside the noise.** Every form here gives each item a separate, definite place, and none of them shows how far apart the items are, or how firmly. The drawing makes the ordering look like the most certain fact on the page when it is frequently the least certain thing in the data.

A usable check: perturb each value by whatever uncertainty you have on it, re-sort, and look at the figure again. If the sentence under the chart stops being true, the sentence was about the sorting rather than about the items. `authority-asserted`, and it follows from the structure rather than from a study.

## Types in this index

- [dot-strip-plot.md](dot-strip-plot.md)
- [dumbbell-plot.md](dumbbell-plot.md)
- [bump-chart.md](bump-chart.md)
- [lollipop-chart.md](lollipop-chart.md), which is primarily a magnitude chart
- [slope-chart.md](slope-chart.md), which is primarily a change-over-time chart

None of the five has a study behind it. The sorted [bar chart](bar-chart.md) is where the evidence in this neighborhood lives, and it is indexed under [magnitude](magnitude.md).

## A note on filing

**Schwabish has no ranking category.** *Better Data Visualizations* folds this group and magnitude together into one chapter, **Comparing Categories**, and files Dot Plot there and Bump under Time ([schwabish.md](../sources/schwabish.md), memberships verified from the book's contents pages; his prose is unread and nothing here reports what he argues).

That page already calls the merge a downgrade, because "Comparing Categories swallowing both Magnitude and Ranking loses the FT's sharpest definitional move." The judgment holds up from inside this index: what makes ranking worth separating is precisely that it names a question the value does not answer, and a merged category cannot state that. It is also a taxonomy disagreement between two practitioner schemes with no experiment on either side, which is most of what it is worth saying about it. Two schemes descended from the same 2014 poster disagree about whether this group exists.

## See also

- [magnitude.md](magnitude.md) — where the sorted bar chart lives, and the group this one is hardest to separate from
- [../concepts/channels.md](../concepts/channels.md) — the evidence tier, and why it bears on this group less than on any other
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) — the definition this index is built on
- [README.md](README.md) — the page template and the inheritance rule
