---
type: chart-type
relationships: [change-over-time, part-to-whole]
aliases: [100% stacked area, Band chart, Normalized stacked area, Stacked area chart]
---

# Stacked area charts

Several series drawn as filled bands stacked on top of one another over a continuous axis, so each band's thickness is that series' value and the outer boundary is the running total.

Also called a **band chart**. A **100% stacked area**, sometimes called a normalized stacked area, is the same chart with each column rescaled to shares, and it makes a different claim: it shows composition and deletes the total, exactly as the 100% case does on [stacked-bar.md](stacked-bar.md). The two are not interchangeable.

It is also a part-to-whole chart, for the same reason [stacked-bar.md](stacked-bar.md) is: the bands partition a total, and here they do it over a continuous axis. It is indexed under [change-over-time](change-over-time.md) first because the axis is what the form is built around.

**Two naming problems, both real, both from sources in this wiki.** [Schwabish](../sources/schwabish.md) files **Area** and **Stacked Area** as two separate types in his Time chapter, while [the FT](../sources/ft-visual-vocabulary.md) carries a single **Area chart** gloss whose warning is about "seeing change in components", and components only exist once the series are stacked. So one scheme separates the forms and the other writes one entry that is really about this one. Separately, [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) use the phrase "area chart" for a pie-cue isolation stimulus that is neither form; [area-chart.md](area-chart.md) records that collision because it produces confident miscitations. The name **band chart** is not vouched by any source in this wiki, so it is recorded here as a name in circulation rather than as a definition.

## When to reach for it, and when not

The form is defined for the case where the total is a real quantity the reader cares about, the components are few, x is continuous and ordered, and the reading on offer is the shape of the total plus the coarse relative size of the bands. That is the whole of its range.

**It is not the single-series [area chart](area-chart.md) with more lines.** That form's argument is about whether the amount under one curve is a quantity. This form's argument is about what happens to the parts once they are stacked, and only the bottom one is still sitting on the axis.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How did this one component change? | [Line chart](line-chart.md) of that component, or small multiples. The FT's own gloss on area charts: "Use with care -- these are good at showing changes to total, but seeing change in components can be very difficult" |
| How do these four series' trends compare? | [Line chart](line-chart.md). Stacked bands above the bottom have no shared baseline and each one's position depends on everything below it |
| Only the shares matter | A 100% stacked area, which removes the total. Where the total was not the reason for stacking, a set of share lines is simpler |
| There is one series | [Area chart](area-chart.md), where the fill is the only question |
| Composition across a few discrete periods | [Stacked bar](stacked-bar.md). A continuous x asserts a path between periods |
| Many components, and legibility is already the problem | [Streamgraph](streamgraph.md), which trades away the last fixed baseline for it, or aggregate the tail into "other" |
| Exact values per component per period | A table |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Cumulative sum across series at each x. Optionally normalize each x to 100%. The series order is part of the transform and it is a choice |
| Geometry | One filled band per series, between its lower and upper cumulative boundaries |
| Scale | Time to position on x, cumulative value to position on y, so each series' own value is the **thickness** of its band |
| Coordinates | Cartesian |
| Guides | Two axes including the zero baseline, legend or direct labels on the bands |

**Three one-slot relationships.** Series added to the transform slot of an [area chart](area-chart.md) give this form. The continuous x replaced with categories gives [stacked-bar.md](stacked-bar.md). A baseline computed from the data instead of fixed at zero gives [streamgraph.md](streamgraph.md).

The zero baseline is not optional here in the way it is on an unfilled line. The stack is a cumulative sum starting from zero, so cropping the axis cuts into the bottom band rather than into empty space. Definitional.

## Channels

**The total is position along a common scale.** The outer boundary is a cumulative sum read off the y axis, which is the same reading a stacked bar's overall height gets, inherited from [channels.md](../concepts/channels.md) rather than measured here.

**The bottom band is position along a common scale. Every band above it floats.** That is the structure [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured directly on divided bars, and [stacked-bar.md](stacked-bar.md) carries the quote and the 40% to 250% figure. That inheritance lives there; the transfer from bars to bands is reasoning, not measurement.

**One thing is different from the stacked bar, and it is definitional.** A stacked bar's segment sits between two straight, parallel edges, so its length is read against a straight reference. A stacked area's band sits between two curves, so the reader is judging thickness perpendicular to a baseline that is itself moving. No two thickness readings on the chart share a straight reference edge. **Whether that costs the reader anything, and how much, is unmeasured in this corpus.**

**Hue carries series identity**, which is not a magnitude channel and is not scored as one ([what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means)).

## What it is measurably good at

**Nothing. No study in this corpus tests a stacked area chart**, against a line chart, against small multiples, or against anything else, on any task.

## What it is measurably bad at

Nothing measured on this form. Three exposures are inherited and all three are real.

**Everything the line chart is bad at**, since a band boundary is a line: aspect ratio, truncation, silently repaired gaps and log axes. See [what it is measurably bad at](line-chart.md#what-it-is-measurably-bad-at).

**Axis inversion**, from [area-chart.md](area-chart.md#what-it-is-measurably-bad-at). The [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) reversal condition was a single-series line-area chart, not a stack, and it is the largest effect in that paper: 39 of 40 correct in the control against 7 of 38 in the deceptive condition. One chart, one scenario, and the direction is not in doubt.

**Tracking a band that is not on the baseline.** Inherited from the divided-bar measurement through [stacked-bar.md](stacked-bar.md), one step of reasoning away, and then a second step away because of the curving reference edge above.

## What is contested

**The zero baseline argument is settled here in a way it is not for a line chart, and [area-chart.md](area-chart.md#what-is-contested) carries the whole record**, including the caution that four agreeing sources are fewer independent voices than they look. The addition this form makes is structural rather than contested: a stack begins at zero by construction, so there is nothing to argue about.

**Whether the fill and the stack help at all.** Unmeasured in either direction. The FT's gloss says the fill serves the total and hurts the components, and no study here tests that split. `absence of evidence`.

**Whether the components should be ordered by size, by importance, or by convention.** Nobody in this corpus has tested any ordering. What follows from the evidence rather than from taste is that the series placed on the baseline is the one read as position, and that comes from the measured bar result rather than from a study of orderings.

## The failure mode it invites

**Inviting the reader to track a middle band.** The chart shows every component at once and makes them all look equally readable. Following the orange band across the chart is a set of thickness judgments with no shared reference, which is the one comparison the divided-bar literature measured and found expensive. The remedy [stacked-bar.md](stacked-bar.md) names is the same: the series in question sits on the baseline, or comes out of the stack and is drawn as its own line.

**Letting the total's shape stand in for the components' stories.** A total that rises smoothly can be hiding one component collapsing while another grows. Nothing on the chart flags that, and the reader has no way to notice it.

**Normalizing to 100% without saying so.** A stack of counts and a stack of shares look almost identical and answer different questions, and the normalized version removes the total, which was the reason to stack in the first place. Both are legitimate; the chart does not say which one it is without a labeled axis.

All three follow from the structure. `authority-asserted` where the FT and the practitioner literature say the same thing, and untested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing native to this form. Everything in this bucket is inherited: the axis is not inverted, the axis is not truncated, gaps are drawn as gaps, and the scale is linear. Each of those has a measurement behind it and each of them lives on [line-chart.md](line-chart.md#justifying-the-choice) or [area-chart.md](area-chart.md).

**Defensible, with the label said out loud:**

- "The series the reader most needs to follow is on the baseline, so it is read as position rather than as a floating thickness." That transfer comes from a measurement on divided bars and has never been tested on bands over a continuous axis.
- "Three components, because more than a handful stops being readable." Convention, with no measured threshold behind it.
- "The components are also drawn as small multiples, because seeing change in a component inside a stack is the thing this form is worst at." Widely asserted, including by the FT's one-line gloss, and never tested.
- "Counts rather than shares, and the axis says so, because the total is part of the point."

**Commonly repeated, and the evidence does not support it:**

- ~~"Readers can follow each band."~~ They can follow the bottom one and the outer boundary. Everything in between floats, and the bar version of that comparison carries 40% to 250% more error than a position reading.
- ~~"The stacked bar evidence applies directly, so this is well understood."~~ It applies to the total and the bottom band. The floating bands here are bounded by curves rather than by straight parallel edges, and nobody in this corpus measured that.
- ~~"A 100% stacked area is the safer choice."~~ It is a different chart making a different claim. It deletes the total, which is the one accurately read quantity the stack had.
- ~~"It is a line chart with the areas filled in."~~ It is, and the fill is what puts the zero baseline back in force, occludes everything behind it, and makes every series above the first one float.

## See also

- [area-chart.md](area-chart.md) — the parent, the single-series case, and where the zero-baseline record lives
- [stacked-bar.md](stacked-bar.md) — the same stack over categories, and the one place the floating-segment cost was measured
- [streamgraph.md](streamgraph.md) — this chart with the baseline turned into a free parameter
- [line-chart.md](line-chart.md) — the band boundary, unfilled, and most of the inherited evidence
- [change-over-time.md](change-over-time.md) — the group, and the two free parameters it leaves open
- [part-to-whole.md](part-to-whole.md) — the composition argument this form also belongs to
