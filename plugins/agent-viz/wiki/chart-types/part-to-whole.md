---
type: index
---

# Part-to-whole

One total, divided into parts that exhaust it.

## Before anything: does this need a chart?

The Urban Institute style guide, by [Jonathan Schwabish](../people/jonathan-schwabish.md), names three ways out ([urban-institute.md](../sources/urban-institute.md)):

> "If you find explanatory sentences do a better job of distilling the information you want to convey, consider going without a chart. If your main goal is to present detailed information as opposed to showing patterns, or if it's important that the reader can accurately determine the values of your data, consider using a table instead. You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

So, in order:

- **One share is the message.** "62% of revenue comes from a single client" set large, with a line of context under it. No chart. A pie drawn to deliver one number, where the other slices are packaging, is the common miss in this group.
- **The reader needs exact values.** A table.
- **The division itself is the message.** That is this group.

`authority-asserted`. No experiment here compares a big number against a pie.

## Is composition the right frame?

Two tests, both of which have to pass.

**Is the total a real quantity the reader cares about?** A budget, a population, all traffic in a period, a full genome. Where the total is an artifact of which categories were included, the "whole" is not a thing and the drawing is the composition of nothing. Percentages summing to 100 do not by themselves make a real whole.

**Does the reader need to see the parts are exhaustive?** Showing that nothing is hiding outside the frame is the one thing these forms do that a bar chart does not. Where "and that's all of it" is not part of the claim, the constraint is being paid for and not used.

If either test fails, the question belongs to another group:

| The reader's actual question | Group |
|---|---|
| How big is this one thing? | Magnitude. A bar chart |
| Which is biggest, and in what order? | [Ranking](ranking.md). A sorted bar chart |
| How did this change? | Change over time. A line chart |
| How do these two groups differ? | [Deviation](deviation.md), or a grouped bar |
| Does this add up, and to what? | **This group** |

## What composition costs

**These forms mostly abandon the most accurate channel available.** Only the [stacked bar](stacked-bar.md) keeps a position-along-a-common-scale reading, and only for its bottom segment; the [marimekko](marimekko-chart.md) keeps it for one corner mark and gives it up in both directions after that. Everything else moves the reader onto arc length, length with no shared baseline, or area, all of which are read less accurately than position ([channels.md](../concepts/channels.md)).

**The [waffle](waffle-chart.md) sits outside that sentence.** Its reading is a count of cells rather than a value read off a mark, and the accuracy ordering does not score counting at all. So nothing here measures the form in either direction: no evidence that it reads worse than the others, and none that it reads better.

On a direct pie-versus-bar comparison, [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md): "in only 3 of the 40 cases was the pie chart more accurate on average than the bar chart."

The whole-constraint is bought at a cost in value-reading accuracy. The trade holds exactly when both tests above pass.

## Choosing a form

| Form | Channel carrying share | Defined for |
|---|---|---|
| [Pie and donut](pie-and-donut.md) | Arc length and area, **not** angle | Few parts, and "these make a whole" is the point. Donut costs nothing over pie |
| [Stacked bar](stacked-bar.md) | Length, plus position for the bottom segment | The total also matters, or composition repeats across categories or time |
| [Marimekko](marimekko-chart.md) | Rectangular area, from a width and a height together | Two categorical dimensions, where the group sizes and the split inside each group both matter |
| [Stacked area](stacked-area-chart.md) | Band thickness, over a continuous axis | Composition changes continuously and the total is worth seeing. Indexed primarily under change over time |
| [Treemap](treemap.md) | Rectangular area | Many parts, or the parts nest in a hierarchy |
| [Sunburst](sunburst-chart.md) | Angular extent, with arc length and area varying by ring | A shallow hierarchy, where the top-level split and its subdivisions must be visible at once |
| [Waffle](waffle-chart.md) / grid plot | Count of discrete cells | The count is small and countable, and the parts are tallied rather than estimated |

[Stacked bar](stacked-bar.md) is also a magnitude and a change-over-time chart, and [treemap](treemap.md) is also a magnitude chart. [Schwabish](../sources/schwabish.md) files the marimekko and the waffle as comparison charts rather than part-to-whole ones, verified from his book's contents pages, and files the sunburst here. Which one a form *is* depends on the question brought to it.

Three constraints that follow from the evidence rather than from taste:

- **The series in question sits on the baseline** of a stacked bar. That moves it from floating length onto position, the largest single accuracy gain available in this group, and it costs nothing.
- **Comparison across two of these charts.** Slices sit at different rotational offsets and treemap layouts recompute per dataset, so nothing survives the comparison. For "how did composition change between A and B," the forms that carry it are grouped or small-multiple bars, or a plot of the change itself.
- **Many parts pushes toward the treemap, or out of the group.** `authority-asserted`: no study here tests the many-slice pie, but it is what the treemap exists for.

**Several of the forms above have a page and still have no controlled study behind them.** The [waffle](waffle-chart.md), [marimekko](marimekko-chart.md) and [sunburst](sunburst-chart.md) pages say what each form encodes and what that costs, and each one states that nothing in this wiki's sources measures it. Having a page is not evidence; those three are still chosen on structure and convention rather than on a result.

Venn / Euler diagrams and Voronoi treemaps have neither a study nor a page. The only thing this corpus carries on the first is the FT's gloss, "Generally only used for schematic representation" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)).

## Justifying the choice

**Defensible, evidence-backed:**

- "A bar chart reads values more accurately than a pie, measured and replicated. I chose the pie anyway because the reader needs to see the parts exhaust the total, and precise values are not the question."
- "I put revenue on the baseline so it reads as position rather than floating length."
- "These two periods are separate charts rather than two pies, because slices at different offsets are not comparable."

**Defensible, with the label said out loud:**

- "More than a handful of slices is too many. Practitioner consensus, not a measured result."
- "A single large number would have carried this better. I used a chart because the reader also needs the other three shares."

**Not defensible:**

- ~~"Pies are bad because they encode angle and angle is a weak channel."~~ Both halves fail. [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) isolated the three cues and found angle the *least* used. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) tested length against angle head to head: "the results do not support this."

Bars beat pies for value extraction. The mechanism everyone gives for it does not hold.

**Also not defensible:** the case against donuts. It rests on the missing center destroying the angle, and angle was carrying the least. Skau & Kosara measured pie and donut as virtually identical.

## The failure mode this group invites

**Using composition to answer a comparison question.** The form makes every part visible and every part look comparable, which invites readers to compare parts across charts or track one part over time. These forms are bad at both.

Where the title or caption compares *across* wholes rather than *within* one, the reading it asks for is one the form does not support.

## Types in this index

- [pie-and-donut.md](pie-and-donut.md)
- [stacked-bar.md](stacked-bar.md), which is also magnitude and change over time
- [treemap.md](treemap.md), which is also a magnitude chart
- [marimekko-chart.md](marimekko-chart.md), which is also a magnitude chart
- [sunburst-chart.md](sunburst-chart.md)
- [waffle-chart.md](waffle-chart.md), which is also a magnitude chart when the question is how many
- [stacked-area-chart.md](stacked-area-chart.md), which is indexed primarily under [change-over-time.md](change-over-time.md)

Venn and Euler diagrams and Voronoi treemaps have no page and no study here. The FT files Venn under this
relationship and glosses it "Generally only used for schematic representation".

## See also

- [../concepts/channels.md](../concepts/channels.md) — the evidence tier these pages inherit from
- [magnitude.md](magnitude.md) — the group this one is defined against
- [aliases.md](aliases.md) — the name index, for arriving with a name rather than a question
- [README.md](README.md) — the page template and the inheritance rule

