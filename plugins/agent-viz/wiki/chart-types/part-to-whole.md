# Part-to-whole

**What it is.** Charts whose subject is composition: one total, divided into parts that exhaust it. The FT's sixth relationship.

**Status.** The best-evidenced group in this wiki. Cleveland & McGill's second experiment was a part-to-whole experiment, Heer & Bostock extended it to area and treemaps, and Skau & Kosara decomposed the pie slice into its individual channels, which almost no other chart type has had done to it.

**What it is good for.** Two decisions, in order. Whether composition is your reader's actual question, which is the one people get wrong. Then, given that it is, which form to pay for it with and what that costs.

**What it does not settle.** Whether to draw a chart at all. If the point is "one part is 80% of the total," a sentence carries it better than any of these.

---

## First: is composition actually the question?

**This group is over-chosen.** Most of the time someone reaches for a pie chart, the reader's real question is "which is biggest" or "how big is this one," and a sorted bar chart answers both more accurately. Composition is the right frame only when the *summing to a whole* is itself part of the message.

Two tests, and the form needs both:

**Is the total a real quantity the reader cares about?** A budget, a population, all traffic in a period, a full genome. If the total is meaningful, its division is meaningful. If the total is an artifact of which categories you happened to include, then the "whole" is not a thing and you are drawing composition of nothing. Percentages summing to 100 do not by themselves make a real whole.

**Does the reader need to see that the parts are exhaustive?** The distinctive thing these forms do, which no bar chart does, is show that nothing is hiding outside the frame. If "and that's all of it" is part of what you are asserting, you want this group. If it is not, you are paying for a constraint you do not need.

If either test fails, go elsewhere:

| The reader's actual question | Go to |
|---|---|
| How big is this one thing? | Magnitude. A bar chart |
| Which is biggest, and in what order? | Ranking. A sorted bar chart |
| How did this change? | Change over time. A line chart |
| How do these two groups differ? | Deviation, or a grouped bar |
| Does this add up, and to what? | **Stay here** |

## What composition costs

Stated plainly, because it is the trade you are making and you should be able to name it:

**These forms mostly abandon the most accurate channel available.** Only the [stacked bar](stacked-bar.md) keeps a position-along-a-common-scale reading, and only for its bottom segment. Everything else moves the reader onto arc length, area, or non-aligned position, which the evidence places at ranks 3 and 4 rather than rank 1. See [channels.md](../concepts/channels.md).

Concretely, from [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md): on a direct pie-versus-bar comparison, "in only 3 of the 40 cases was the pie chart more accurate on average than the bar chart."

**You buy the whole-constraint and you pay in value-reading accuracy.** That is the whole trade, and it is a good trade exactly when the two tests above pass.

## Choosing a form

| Form | Channel carrying share | Reach for it when |
|---|---|---|
| [Pie and donut](pie-and-donut.md) | Arc length and area, **not** angle | Few parts, and "these make a whole" is the point. Donut costs nothing over pie |
| [Stacked bar](stacked-bar.md) | Length, plus position for the bottom segment | The total also matters, or composition repeats across categories or time |
| [Treemap](treemap.md) | Rectangular area | Many parts, or the parts nest in a hierarchy |
| Waffle / grid plot | Count of discrete cells | The count is small and countable, and you want parts to be tallied rather than estimated |

Three practical constraints that follow from the evidence rather than from taste:

- **Put the series you care about on the baseline** of a stacked bar. It moves that series from rank 3 to rank 1 and costs nothing.
- **Do not compare across two of these charts.** Slices sit at different rotational offsets and treemap layouts recompute per dataset, so nothing survives the comparison. If your question is "how did composition change between A and B," use grouped or small-multiple bars, or plot the change itself.
- **Many parts pushes you to treemap or away from the group entirely.** No study here tests the many-slice pie, so this is `authority-asserted`, but it is near-universal and it is what the treemap exists for.

Waffle, Venn / Euler and Voronoi treemaps have **no controlled study** in this wiki's source set and get no page. That is a gap, not a judgment on the forms.

## Justifying the choice

Since the point of this page is to help someone defend a decision, here is what is defensible and what is not.

**Defensible, evidence-backed:**

- "A bar chart reads values more accurately than a pie, measured directly and replicated. I chose the pie anyway because the reader needs to see the parts exhaust the total, and precise values are not the question."
- "I put revenue on the baseline so it reads as position rather than floating length."
- "These two periods are separate charts rather than two pies, because slices at different offsets are not comparable."

**Defensible, and say the label out loud:**

- "Conventionally, more than a handful of slices is too many. That is practitioner consensus, not a measured result."

**Not defensible, and it is the most commonly repeated claim in this group:**

- ~~"Pies are bad because they encode angle and angle is a weak channel."~~ Both halves fail. [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) isolated the three cues and found angle the *least* used, not the primary one. And [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) tested length against angle head to head and reported that "the results do not support this."

The conclusion survives. The mechanism does not. State the finding, drop the explanation.

**Also not defensible:** the case against donut charts. It rests entirely on the missing center destroying the angle, and angle was carrying the least. Skau & Kosara measured pie and donut as virtually identical.

## The failure mode this group invites

**Using composition to answer a comparison question.** The form makes every part visible and every part look comparable, which invites readers to compare parts across charts or track one part over time. These forms are bad at both. `authority-asserted`, though it follows directly from the measured channel split.

A usable check: if the title or caption compares *across* wholes rather than *within* one, the form is probably wrong.

## Types in this index

- [pie-and-donut.md](pie-and-donut.md)
- [stacked-bar.md](stacked-bar.md) — also indexed under magnitude and change over time
- [treemap.md](treemap.md) — also indexed under magnitude

A type can sit in several indexes, and none of those readings is more real than the others. A stacked bar is genuinely a composition chart and genuinely a magnitude chart; which one it is depends on the question you brought.

## See also

- [../concepts/channels.md](../concepts/channels.md) — where the accuracy claims come from and how far they carry
- [README.md](README.md) — the page template and the inheritance rule
