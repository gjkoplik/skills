---
type: chart-type
relationships: [change-over-time]
aliases: [River plot, Stream chart, Streamgraph, ThemeRiver]
---

# Streamgraphs

A [stacked area chart](stacked-area-chart.md) whose baseline is computed from the data rather than fixed at zero, usually so the bands sit symmetrically about a center, so each band's thickness is that series' value and the silhouette's thickness is the total.

ThemeRiver is the older research name; stream chart and river plot are also in circulation. No source in this wiki defines any of these names, "streamgraph" included. [Schwabish](../sources/schwabish.md) lists Streamgraph in his Time chapter (contents pages only, his argument unread).

## When to reach for it, and when not

The form is defined for many components over many time points, read qualitatively: the silhouette of the total, and which bands are large and roughly when. Dropping the fixed baseline costs the stacked area's two accurate readings, the total and the bottom band. It buys freedom from one series absorbing every wiggle beneath it. The FT's gloss on area charts extends here by its own reason: "Use with care -- these are good at showing changes to total, but seeing change in components can be very difficult" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). `authority-asserted`.

| The question | Alternative |
|---|---|
| What was the total at each point? | [Line chart](line-chart.md) or [area chart](area-chart.md) of the total. Here the total is a thickness with no axis |
| How did this one component change? | [Line chart](line-chart.md) of that component, or small multiples. The extreme case of the FT's area-chart caution |
| What is each component's share? | A 100% stacked area, or lines of shares ([stacked-area-chart.md](stacked-area-chart.md)) |
| Any question with a number in the answer | Anything with an axis, or a table |
| There are few components | [Stacked area chart](stacked-area-chart.md), which keeps the baseline and the total |
| A few discrete periods | [Stacked bar](stacked-bar.md) |
| The reader has to defend a conclusion drawn from it | A form whose readings can be checked against an axis |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Cumulative sum across series at each x, plus a baseline offset computed from the data, commonly to center or smooth the bands. Series order is usually computed too |
| Geometry | One filled band per series, between two computed boundaries |
| Scale | Time to position on x, value to band thickness at each x. No value is position on a fixed scale |
| Coordinates | Cartesian |
| Guides | An x axis. A y axis is usually absent, and where drawn its origin is a computed offset. Direct labels or a legend |

Fixing the baseline at zero gives the stacked area back. No source here describes the layout algorithms.

## Channels

Every series is band thickness, with no common baseline anywhere. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured the divided bar, where only the first segment sits on the axis ([stacked-bar.md](stacked-bar.md) has the quote and the 40% to 250% figure). A streamgraph puts nothing on the axis, and adds curved edges and a reference that moves along x, both untested on readers here. The mark-to-channel step is conjecture in the source literature.

Hue carries series identity, which is not a magnitude channel and is not scored as one ([what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means)).

## What is measured

No study in this corpus tests the form, and nothing is contested. Two nearby results do not transfer directly. [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) moved judgments by 129.5% through aspect ratio alone, on a line chart with values printed. Vertical scaling here changes every thickness at once, so that exposure is inherited, not measured ([change-over-time.md](change-over-time.md)). [Correll et al. (2020)](../studies/correll-2020-truncating-the-y-axis.md) measured cropping an axis this form usually lacks. That is no exemption, since the reader has nothing to check vertical extent against, and what that costs is unmeasured.

## The failure mode it invites

**A qualitative picture presented as a readable chart.** Nothing on the drawing says it supports fewer questions than a stacked area.

**Baseline and series order left unrecorded.** Both are computed, change the picture, and leave no trace, like step order on [waterfall-chart.md](waterfall-chart.md) and aspect ratio on [change-over-time.md](change-over-time.md). Both failures are structural and untested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. No study touches the form, and without a fixed baseline it cannot inherit a position reading.

**Defensible, with the label said out loud:**

- "Many series, and what the reader is meant to take away is the shape of the whole and which bands are large. No value is claimed to be readable off it." What readers take away is untested.
- "The caption names the series order and how the baseline was set." Structural and untested.
- "The components that matter are also drawn separately." Widely asserted, including by the FT's gloss on the parent form, and never tested. `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A streamgraph shows how each component changed over time."~~ Thickness against a moving reference. The divided-bar version, with more anchoring, was the costliest reading measured.
- ~~"The flowing baseline makes the bands easier to read."~~ It satisfies a geometric criterion no source here states. Its effect on readers is untested.
- ~~"It is a prettier stacked area chart."~~ It has lost the last common baseline, and the total and bottom band with it.
- ~~"The total is easy to see, it is the outline."~~ The total is the silhouette's thickness, with no axis under it.

## See also

- [stacked-area-chart.md](stacked-area-chart.md): the same chart with the baseline at zero, and the closest inherited evidence
- [area-chart.md](area-chart.md): the single-series parent, and the zero-baseline record
- [stacked-bar.md](stacked-bar.md): where the floating-segment cost was measured
- [change-over-time.md](change-over-time.md): the group, and its free parameters
- [../concepts/channels.md](../concepts/channels.md): the inheritance rule, and where it stops applying
