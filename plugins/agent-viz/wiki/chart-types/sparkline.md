---
type: chart-type
relationships: [change-over-time]
aliases: [Bar sparkline, Datawords, Inline chart, Micro chart, Sparkline, Win/loss sparkline, Word-sized graphic]
---

# Sparklines

A [line chart](line-chart.md) with the guides slot emptied and the whole graphic sized to sit inside a line of text, so the only thing on offer is the shape of the series.

It is also called a word-sized graphic, an inline chart or a micro chart. [Tufte](../people/edward-tufte.md), who coined "sparkline", calls them "datawords". Bar and win/loss sparklines swap in a different mark, and no source here defines either.

The term comes from *Beautiful Evidence* (2006), which nobody here has opened. [sources/tufte.md](../sources/tufte.md) covers only *The Visual Display of Quantitative Information*, is `secondary-only`, and says nothing on sparklines. What was read is an excerpt of the sparklines chapter that Tufte posted on his site, fetched and read locally, recorded on [people/edward-tufte.md](../people/edward-tufte.md), and covering the line form only. Everything attributed to him below comes from it and is `authority-asserted`, since he ran no experiments.

## When to reach for it, and when not

The form is defined for a reading of "rising, falling, spiky, flat, above the band, below the band", inside a sentence or scanned down a table. Tufte shows a clinical glucose series in running text and a financial table stacking hundreds of series. Without axes, every reading is relative and no value can be extracted from the mark.

| The question | Alternative |
|---|---|
| What is the value? | The number Tufte prints beside the line |
| How much did it change? | A chart with an axis, or two numbers and a subtraction |
| Is this series higher than that one? | A [line chart](line-chart.md) on shared, drawn axes |
| There are three or four points | A number, a sentence or a table |
| A conclusion drawn from it has to be defended | A full chart, with an axis to check it against |
| One figure is the whole message | A single large number ([part-to-whole.md](part-to-whole.md)) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (time, value), for one series |
| Transform | None. The y range is per graphic unless shared on purpose, and the drawing does not record which |
| Geometry | Path, optionally with the endpoint or the min and max marked. Bar and win/loss variants swap the mark |
| Scale | Time to x, value to y, over a range that is **not shown** |
| Coordinates | Cartesian, sized to the type. Tufte gives 14 letterspaces as a working width |
| Guides | **None.** Optionally a gray normal-range band and a printed number |

[slope-chart.md](slope-chart.md) empties the same slot and fills the gap with direct labels. This form leaves it empty.

## Channels

Position along a common scale, on a scale the reader cannot see. That is inherited from [channels.md](../concepts/channels.md), where the chart-to-channel mapping is conjecture. The reading holds within one sparkline. Between two it holds only if the scale was shared on purpose, which neither graphic records.

A gray normal-range band turns the task into a categorical above, inside or below judgment, the one question the form can answer without an axis, and the point of Tufte's clinical example.

Shape, spikes and turning points are not value extraction, which the ranking's authors scope out ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What is measured

No study in this corpus tests a sparkline. Two nearby results do not settle it.

[Gillan & Richman (1994)](../studies/gillan-richman-1994-data-ink.md), the one measurement of removing axis furniture, found that removing the y-axis line and the x axis generally *increased* response time, while removing tick marks helped. Each effect depended on graph type, task and the other elements present. The study page is `secondary-only`, the graphs were ordinary size, and trading guides for a place in a sentence was never tested.

[Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) moved reader judgments by 129.5% on a line chart by changing the aspect ratio alone, with true values printed on the chart. On a sparkline the typography sets the height ([change-over-time.md](change-over-time.md)), and no study measured that case.

Nothing about this form is contested. The data-ink argument it takes to its limit is `contested` ([refutations.md](../refutations.md)), and Tufte's midgap box plot, the one minimization of his anybody has measured, came out worse than the original ([edward-tufte.md](../people/edward-tufte.md)). Neither is evidence about sparklines.

## The failure mode it invites

**Reading a value off it.** There is no axis, so there is no value, and nothing warns the reader.

**Comparing sparklines that do not share a scale.** Stacked in a column they look comparable, but independently scaled, a flat series and a violent one can draw the same picture.

**Using one where a number would do.** A four-point series has no shape to show.

All three follow from the structure and are untested on readers. `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing.

**Defensible, with the label said out loud:**

- "The most recent value is printed beside the line, tied to it by one accent color." Tufte's construction, `authority-asserted`.
- "The normal range is a gray band behind the line, so the reading is above, inside or below rather than a number." Same source, `authority-asserted`.
- "All forty sparklines in this table share one vertical scale, and the caption says so." Follows from the structure, untested on readers. `absence of evidence`.
- "About fourteen letterspaces wide, so it sits in the line of text rather than interrupting it." Tufte's working width, `authority-asserted`.
- "Its purpose is to be approximately right at a glance rather than exactly wrong at length." His defense of the resolution trade, under his stated target: "General idea = max[data], min[design]." `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"Sparklines let readers see the value at a glance."~~ There is a shape and no value.
- ~~"Stripping the axes makes it cleaner, so it reads better."~~ The one measurement found the effect element-conditional, and removing the axis lines *hurt*.
- ~~"A sparkline is just a small line chart."~~ It is a line chart without the guides that made values readable.
- ~~"Tufte showed that sparklines work."~~ He proposed and demonstrated them. Nobody has tested them.

## See also

- [line-chart.md](line-chart.md): the same chart with guides, and this group's evidence
- [slope-chart.md](slope-chart.md): the other form that empties the guides slot
- [change-over-time.md](change-over-time.md): the group
- [../people/edward-tufte.md](../people/edward-tufte.md): the sparklines excerpt, the Tufte material read directly
- [../sources/tufte.md](../sources/tufte.md): the 1983 book, not where sparklines come from
- [tables.md](tables.md): where a column of sparklines lives
