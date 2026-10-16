---
type: chart-type
relationships: [change-over-time, part-to-whole]
aliases: [100% stacked area, Band chart, Normalized stacked area, Stacked area chart]
---

# Stacked area charts

Several series drawn as filled bands stacked on top of one another over a continuous axis, so each band's thickness is that series' value and the outer boundary is the running total.

It is also called a band chart, a name no source here vouches for. The 100% (normalized) version rescales each column to shares and deletes the total, as on [stacked-bar.md](stacked-bar.md), so it makes a different claim.

[Schwabish](../sources/schwabish.md) files Area and Stacked Area separately. [The FT](../sources/ft-visual-vocabulary.md) has one Area chart gloss, whose warning about "seeing change in components" only applies once series are stacked. [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) use "area chart" for a pie-cue stimulus that is neither form ([area-chart.md](area-chart.md)).

## When to reach for it, and when not

The form is defined for a total the reader cares about, a few components, and a continuous, ordered x. It offers the shape of the total and the coarse relative size of the bands.

| The question | Alternative |
|---|---|
| How did this one component change? | [Line chart](line-chart.md) of that component, or small multiples. The FT's own gloss on area charts: "Use with care -- these are good at showing changes to total, but seeing change in components can be very difficult" |
| How do these four series' trends compare? | [Line chart](line-chart.md). Each band's position depends on everything below it |
| Only the shares matter | A 100% stacked area. If the total was never the point, share lines are simpler |
| There is one series | [Area chart](area-chart.md) |
| Composition across a few discrete periods | [Stacked bar](stacked-bar.md). A continuous x asserts a path between periods |
| Many components, legibility already the problem | [Streamgraph](streamgraph.md), which gives up the last fixed baseline, or the tail aggregated into "other" |
| Exact values per component per period | A table |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Cumulative sum across series at each x, optionally normalized to 100%. The series order is a choice |
| Geometry | One filled band per series, between its lower and upper cumulative boundaries |
| Scale | Time to x, cumulative value to y, so each series' value is the **thickness** of its band |
| Coordinates | Cartesian |
| Guides | Both axes including the zero baseline, and a legend or direct labels |

Series added to an [area chart](area-chart.md)'s transform give this form. Categories in place of the continuous x give [stacked-bar.md](stacked-bar.md). A baseline computed from the data gives [streamgraph.md](streamgraph.md). The zero baseline is definitional: the stack starts at zero, so cropping the axis cuts into the bottom band.

## Channels

The total and the bottom band are position along a common scale. Every band above floats. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured that structure on divided bars, and [stacked-bar.md](stacked-bar.md) carries the quote and the 40% to 250% figure. The transfer from bars to bands is reasoning, and the mark-to-channel step is conjecture, as everywhere in [channels.md](../concepts/channels.md).

One difference is definitional. A bar segment sits between straight parallel edges. A band sits between two curves, so no two thickness readings share a straight reference edge. Whether that costs the reader anything is unmeasured. `absence of evidence`.

Hue carries series identity, which is not scored as a magnitude channel ([what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means)).

## What is measured

No study in this corpus tests a stacked area chart against anything, on any task. Two nearby results reach it only by inheritance, alongside the divided-bar result in Channels.

- A band boundary is a line, so the line chart's measured exposures apply to it: aspect ratio, truncation, silently repaired gaps, log axes ([line-chart.md](line-chart.md#what-is-measured)). None was measured on a stack.
- Axis inversion ([area-chart.md](area-chart.md#what-is-measured)). The [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) reversal used a single-series line-area chart, not a stack. It is the one distortion in that paper that reversed the reading rather than exaggerating it: 39 of 40 correct in the control against 7 of 38 in the deceptive condition, in one chart and one scenario.

Nothing is contested. A stack starts at zero by construction, so the zero-baseline dispute does not arise; [area-chart.md](area-chart.md#what-is-measured) carries that record, including that its four agreeing sources are fewer independent voices than they look. The FT's claim that the fill serves the total and hurts the components is `authority-asserted` and untested, as is any ordering of the components. `absence of evidence`.

## The failure mode it invites

**Tracking a middle band.** Every band looks equally readable, but following one off the baseline is a run of unanchored thickness judgments, two steps of reasoning from the divided-bar result. The fix on [stacked-bar.md](stacked-bar.md) applies: that series goes on the baseline or comes out as its own line.

**The total standing in for the parts.** A smoothly rising total can hide one component collapsing while another grows.

**Unannounced normalization.** Counts and shares look almost identical, and only a labeled axis says which is drawn.

All three follow from the structure, `authority-asserted` where the FT and practitioners say the same, and untested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing native to this form. The inherited sentences (axis not inverted, not truncated, gaps drawn as gaps, linear scale) live on [line-chart.md](line-chart.md#justifying-the-choice) and [area-chart.md](area-chart.md).

**Defensible, with the label said out loud:**

- "The series the reader most needs to follow is on the baseline, so it is read as position rather than as a floating thickness." Transferred from divided bars, untested on bands. `absence of evidence`.
- "Three components, because more than a handful stops being readable." Convention, with no measured threshold. `absence of evidence`.
- "The components are also drawn as small multiples, because seeing change in a component inside a stack is the thing this form is worst at." `authority-asserted`, including by the FT, and never tested.
- "Counts rather than shares, and the axis says so, because the total is part of the point."

**Commonly repeated, and the evidence does not support it:**

- ~~"Readers can follow each band."~~ Only the bottom one and the outer boundary. On bars, the floating version carries 40% to 250% more error than position.
- ~~"The stacked bar evidence applies directly, so this is well understood."~~ Only to the total and the bottom band. Bands bounded by curves are unmeasured.
- ~~"A 100% stacked area is the safer choice."~~ It is a different claim, and it deletes the total, the one accurately read quantity.
- ~~"It is a line chart with the areas filled in."~~ Yes, and the fill brings back the zero baseline, occludes what is behind it, and makes every series above the first float.

## See also

- [area-chart.md](area-chart.md): the single-series parent and the zero-baseline record
- [stacked-bar.md](stacked-bar.md): the same stack over categories, where the floating-segment cost was measured
- [streamgraph.md](streamgraph.md): this chart with a free baseline
- [line-chart.md](line-chart.md): the band boundary unfilled, and most of the inherited evidence
- [change-over-time.md](change-over-time.md): the group, indexed first because the axis is what the form is built around
- [part-to-whole.md](part-to-whole.md): the composition argument
