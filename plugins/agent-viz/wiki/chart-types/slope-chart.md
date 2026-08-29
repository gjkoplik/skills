---
type: chart-type
relationships: [change-over-time, ranking]
aliases: [Slope chart, Slopegraph]
---

# Slope charts

Two parallel value axes, one per period, with each category drawn as a single segment joining its two values, so direction and steepness carry the change and crossings carry the reordering.

## When to reach for it, and when not

The form is defined for exactly two time points or two conditions, more categories than a reader would follow across a full line chart, and a question about which rose, which fell, and which changed places. It is a change-over-time chart and a ranking chart at once, which is the reason it exists.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| What happened in between? | [Line chart](line-chart.md). Two points assert nothing about the path |
| How did the order move across six periods? | [Bump chart](bump-chart.md). Still no study, but there is a page |
| What are the exact values? | A table, or a labeled dot plot |
| Only the size of the change matters, not the levels | A sorted bar chart of the differences. Datawrapper offers this as one of its three replacements for a truncated axis ([datawrapper-academy.md](../sources/datawrapper-academy.md)) |
| How did the composition of a total shift between two periods? | [Stacked bar](stacked-bar.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with a value at each of two periods |
| Transform | None. Optionally rank within each period |
| Geometry | One segment per category, usually with endpoint markers |
| Scale | Value to position on a **single vertical scale shared by both columns** |
| Coordinates | Cartesian, with x taking exactly two positions |
| Guides | Two labeled columns, direct labels per category, often no y axis at all |

**This is a [line chart](line-chart.md) with two x positions and the guides slot traded for direct labels.** That is the whole difference, and it is why the page inherits its evidence and has almost none of its own. The shared scale is load-bearing: two independently scaled columns make the segments uncomparable, and nothing on the chart shows that.

## Channels

**Position along a common scale** at each endpoint, inherited from [channels.md](../concepts/channels.md) with the usual caveat that the mapping is conjecture rather than measurement, plus **direction and slope** for the change itself. Cleveland & McGill put slope judgment among the tasks they could not separate: the authors "have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle," and they call their ordering "a tentative working hypothesis." So the channel this form is named after is the one the ranking is least sure about.

## What it is measurably good at

**Nothing. No study in this corpus tests a slope chart.**

The nearest stimulus in the corpus is [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md), which is pairs of isolated line segments judged for slope ratio, and it is closer to this chart than to any other. It does not transfer cleanly: their segments sit in opposite quadrants specifically so that y-extents cannot be compared across the pair, while a slope chart's whole design puts both segments on one scale where they can be. What does carry over is the finding that slope-ratio judgment is error-prone, that people spontaneously use different strategies without noticing, and that a visible baseline nearly eliminated the error below 45 degrees while doing nothing above it.

## What it is measurably bad at

Nothing measured. The inherited exposure is real: the vertical scale is a free parameter that changes every slope on the chart at once, exactly as on a [line chart](line-chart.md#what-it-is-measurably-bad-at), where that manipulation was measured and moved reader judgments substantially.

## What is contested

Nothing. There is no record here to disagree with itself.

## The failure mode it invites

**Two cherry-picked endpoints.** The form makes the choice of periods invisible, and with two points there is no shape to contradict the story. Whether the message survives a third point is not recoverable from the figure. `authority-asserted`, and it follows from the structure rather than from taste.

**Too many categories.** Segments converge and labels collide in the middle, and the crossings that were the point become a tangle. Practitioner convention with no measured threshold, from the same people who recommend the form: Schwabish and Knaflic both reach for slope charts routinely ([jonathan-schwabish.md](../people/jonathan-schwabish.md), [cole-nussbaumer-knaflic.md](../people/cole-nussbaumer-knaflic.md)) and neither has an experiment behind the advice.

## Justifying the choice

**Defensible, evidence-backed:**

- "Both columns share one vertical scale, so the two endpoints of every segment are read as position along a common scale." That inherits the best-measured comparison in the literature, and the step from this chart to that channel is conjecture, as it is for every chart type.

Nothing else in this bucket is native to the form.

**Defensible, with the label said out loud:**

- "Two periods and eighteen categories, so a slope chart rather than eighteen two-point lines or a grouped bar. That is practitioner convention, endorsed by several of them, and no study here tests it."
- "The categories that reversed are in color and the rest are gray. Widely recommended, never measured."

**Commonly repeated, and the evidence does not support it:**

- ~~"A slope chart shows the change accurately."~~ Nobody has measured what readers take from one. What it is built to show is the direction of change and the reordering.
- ~~"A steeper segment means a bigger change."~~ Only relative to the scale that was chosen, and only if both columns share it. Steepness is a property of the drawing as much as of the data, which is the standing hazard of this whole group.

## See also

- [line-chart.md](line-chart.md) — the same chart with more than two x positions, and where the evidence is
- [change-over-time.md](change-over-time.md) — the group, and the free parameters it leaves open
- [../concepts/channels.md](../concepts/channels.md) — including why slope sits among the tasks the ordering could not separate
