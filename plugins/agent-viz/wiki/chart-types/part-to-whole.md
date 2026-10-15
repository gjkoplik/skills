---
type: index
---

# Part-to-whole

One total, divided into parts that exhaust it.

## Before anything: does this need a chart?

The Urban Institute style guide, by [Jonathan Schwabish](../people/jonathan-schwabish.md), names three ways out ([urban-institute.md](../sources/urban-institute.md)):

> "If you find explanatory sentences do a better job of distilling the information you want to convey, consider going without a chart. If your main goal is to present detailed information as opposed to showing patterns, or if it's important that the reader can accurately determine the values of your data, consider using a table instead. You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

- **One share is the message.** "62% of revenue comes from a single client" set large with a line of context, and no chart. A pie drawn to deliver one number is the common miss in this group.
- **The reader needs exact values.** A [table](tables.md).
- **The division itself is the message.** This group.

`authority-asserted`. No experiment here compares a big number against a pie.

## Is composition the right frame?

Both tests have to pass.

**Is the total a real quantity the reader cares about?** A budget, a population, a full genome. Where the total is an artifact of which categories were included, there is no whole to show, and percentages summing to 100 do not make one.

**Does the reader need to see that the parts are exhaustive?** Showing that nothing sits outside the frame is the one thing these forms do that a bar chart does not. Where "and that's all of it" is not part of the claim, the constraint is paid for and unused.

If either test fails, the question belongs elsewhere:

| The reader's question | Group |
|---|---|
| How big is this one thing? | [Magnitude](magnitude.md). A bar chart |
| Which is biggest, and in what order? | [Ranking](ranking.md). A sorted bar chart |
| How did this change? | [Change over time](change-over-time.md). A line chart |
| How do these two groups differ? | [Deviation](deviation.md), or a grouped bar |
| Does this add up, and to what? | **This group** |

## What composition costs

Only the [stacked bar](stacked-bar.md) keeps a position-along-a-common-scale reading, and only for its bottom segment. The [marimekko](marimekko-chart.md) keeps it for one corner mark. Everything else puts the reader on arc length, length with no shared baseline, or area, all read less accurately than position ([channels.md](../concepts/channels.md)). The [waffle](waffle-chart.md) is read by counting cells, which the accuracy ordering does not score, and nothing here measures it in either direction.

On a direct pie-versus-bar comparison, [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) found that "in only 3 of the 40 cases was the pie chart more accurate on average than the bar chart." The whole-constraint costs value-reading accuracy, and the trade holds exactly when both tests above pass.

## Choosing a form

| Form | Channel carrying share | Defined for |
|---|---|---|
| [Pie and donut](pie-and-donut.md) | Arc length and area, **not** angle | Few parts, and "these make a whole" is the point. Donut costs nothing over pie |
| [Stacked bar](stacked-bar.md) | Length, plus position for the bottom segment | The total also matters, or composition repeats across categories or time |
| [Marimekko](marimekko-chart.md) | Rectangular area, width times height | Two categorical dimensions, where group sizes and the split within each both matter |
| [Stacked area](stacked-area-chart.md) | Band thickness, over a continuous axis | Composition changes continuously and the total is worth seeing |
| [Treemap](treemap.md) | Rectangular area | Many parts, or the parts nest in a hierarchy |
| [Sunburst](sunburst-chart.md) | Angular extent, with arc length and area varying by ring | A shallow hierarchy, with the top-level split and its subdivisions visible at once |
| [Waffle](waffle-chart.md) / grid plot | Count of discrete cells | A small count, tallied rather than estimated |

[Schwabish](../sources/schwabish.md)'s contents pages file the marimekko and the waffle as comparison charts and the sunburst here, so a form's group depends on the question brought to it. No study in this wiki's sources measures the waffle, marimekko or sunburst. They are chosen on structure and convention.

Three constraints that follow from the evidence rather than from taste:

- **The series in question sits on the baseline** of a stacked bar. That moves it from floating length onto position, the largest free accuracy gain in this group.
- **No comparison across two of these charts.** Slices sit at different rotational offsets and treemap layouts recompute per dataset. For "how did composition change between A and B," grouped or small-multiple bars carry it, or a plot of the change.
- **Many parts push toward the treemap, or out of the group.** `authority-asserted`: no study here tests the many-slice pie, but the treemap exists for it.

## Justifying the choice

**Defensible, evidence-backed:**

- "A bar chart reads values more accurately than a pie, measured and replicated. I chose the pie anyway because the reader needs to see the parts exhaust the total, and precise values are not the question."
- "I put revenue on the baseline so it reads as position rather than floating length."
- "These two periods are separate charts rather than two pies, because slices at different offsets are not comparable."

**Defensible, with the label said out loud:**

- "More than a handful of slices is too many. Practitioner consensus, not a measured result."
- "A single large number would have carried this better. I used a chart because the reader also needs the other three shares."

**Not defensible:**

- ~~"Pies are bad because they encode angle and angle is a weak channel."~~ Both halves fail. [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) isolated the three cues and found angle the *least* used. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) tested length against angle head to head: "the results do not support this." Bars still beat pies for value extraction, but not for the usual reason.
- The case against donuts. It rests on the missing center destroying the angle, and angle was carrying the least. Skau & Kosara measured pie and donut as virtually identical.

## The failure mode this group invites

Using composition to answer a comparison question. These forms make every part look comparable, which invites comparing parts across charts or tracking one part over time, and they are bad at both. A title or caption that compares across wholes, rather than within one, asks for a reading the form does not support.

## Types in this index

- [pie-and-donut.md](pie-and-donut.md)
- [stacked-bar.md](stacked-bar.md), also magnitude and change over time
- [treemap.md](treemap.md), also magnitude
- [marimekko-chart.md](marimekko-chart.md), also magnitude
- [sunburst-chart.md](sunburst-chart.md)
- [waffle-chart.md](waffle-chart.md), also magnitude when the question is how many
- [stacked-area-chart.md](stacked-area-chart.md), indexed primarily under [change-over-time.md](change-over-time.md)

Venn and Euler diagrams and Voronoi treemaps have no page and no study here. The FT files Venn under this relationship and glosses it "Generally only used for schematic representation" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)).

## See also

- [../concepts/channels.md](../concepts/channels.md): the evidence these pages inherit
- [magnitude.md](magnitude.md): the group this one is defined against
- [aliases.md](aliases.md): lookup by chart name
- [README.md](README.md): the page template and the inheritance rule
