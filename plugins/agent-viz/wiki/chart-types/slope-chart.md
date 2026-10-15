---
type: chart-type
relationships: [change-over-time, ranking]
aliases: [Slope chart, Slopegraph]
---

# Slope charts

Two parallel value axes, one per period, with each category drawn as a single segment joining its two values, so direction and steepness carry the change and crossings carry the reordering.

## When to reach for it, and when not

The form is defined for exactly two periods or conditions, more categories than a line chart carries, and a question about which rose, fell or changed places.

| The question | Alternative |
|---|---|
| What happened in between? | [Line chart](line-chart.md). Two points assert nothing about the path |
| How did the order move across six periods? | [Bump chart](bump-chart.md) |
| What are the exact values? | A table, or a labeled dot plot |
| Only the size of the change matters | A sorted bar chart of differences, one of Datawrapper's three replacements for a truncated axis ([datawrapper-academy.md](../sources/datawrapper-academy.md)) |
| How did a total's composition shift? | [Stacked bar](stacked-bar.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, a value at each of two periods |
| Transform | None. Optionally a rank within each period |
| Geometry | One segment per category, usually with endpoint markers |
| Scale | Value to position on a **single vertical scale shared by both columns** |
| Coordinates | Cartesian, x taking exactly two positions |
| Guides | Two labeled columns and direct labels, often no y axis |

It is a [line chart](line-chart.md) with two x positions and direct labels, and inherits its evidence. Without the shared scale, segments are silently incomparable.

## Channels

Endpoints are position along a common scale ([channels.md](../concepts/channels.md)). As for every form, the step from mark to channel is conjecture. The change is on slope, which Cleveland & McGill could not rank: the authors "have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle," and call their ordering "a tentative working hypothesis."

## What it is measurably good at

No study in this corpus tests the form. The nearest stimulus, [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md), put segment pairs in opposite quadrants so their y-extents could not be compared, unlike a slope chart. Three findings transfer: slope-ratio judgment is error-prone, people spontaneously use different strategies without noticing, and a visible baseline nearly eliminated the error below 45 degrees and did not eliminate it above.

## What it is measurably bad at

Nothing measured. The vertical scale sets every slope at once, a manipulation measured on the [line chart](line-chart.md#what-it-is-measurably-bad-at) to move judgments substantially.

## What is contested

Nothing contested in this corpus.

## The failure mode it invites

**Cherry-picked endpoints.** Two points hide the choice of periods and leave no shape to contradict the story. `authority-asserted`.

**Too many categories.** Segments converge, labels collide and crossings tangle. The threshold is unmeasured convention. Schwabish and Knaflic recommend the form routinely ([jonathan-schwabish.md](../people/jonathan-schwabish.md), [cole-nussbaumer-knaflic.md](../people/cole-nussbaumer-knaflic.md)) without experiments.

## Justifying the choice

**Defensible, evidence-backed:**

- "Both columns share one vertical scale, so the two endpoints of every segment are read as position along a common scale." That inherits the best-measured comparison. Nothing else is native to the form.

**Defensible, with the label said out loud:**

- "Two periods and eighteen categories, so a slope chart rather than eighteen two-point lines or a grouped bar. That is practitioner convention, endorsed by several of them, and no study here tests it."
- "The categories that reversed are in color and the rest are gray. Widely recommended, never measured."

**Commonly repeated, and the evidence does not support it:**

- ~~"A slope chart shows the change accurately."~~ Unmeasured.
- ~~"A steeper segment means a bigger change."~~ Steepness depends on the chosen scale as much as on the data.

## See also

- [line-chart.md](line-chart.md): the same chart with more x positions
- [change-over-time.md](change-over-time.md): the group
- [../concepts/channels.md](../concepts/channels.md): the slope tie
