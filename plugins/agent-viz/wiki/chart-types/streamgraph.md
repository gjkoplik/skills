---
type: chart-type
relationships: [change-over-time]
aliases: [River plot, Stream chart, Streamgraph, ThemeRiver]
---

# Streamgraphs

A [stacked area chart](stacked-area-chart.md) whose baseline is computed from the data rather than fixed at zero, usually so the bands sit symmetrically about a center, so each band's thickness is that series' value and the silhouette's overall thickness is the total.

Also called a **ThemeRiver**, which is the older research name, and a **stream chart** or a **river plot**. **None of those names, including "streamgraph" itself, is defined by any source in this wiki.** The one vouched fact about the form in this corpus is a filing: [Schwabish](../sources/schwabish.md) lists **Streamgraph** as a type in his Time chapter, read from the book's own contents pages. What he argues about it is unread, and the aliases above are recorded as names in circulation rather than as definitions. Nothing in the corpus fixes which form any of those names refers to, and the page stands unchecked against any source later opened that defines one.

## When to reach for it, and when not

The form is defined for the case where there are many components over many time points, and the reading on offer is the silhouette of the total plus which bands are large and roughly when they grew. That reading is qualitative, and it is the only one the form supports.

**The baseline is the whole difference from a stacked area, and it costs the last fixed reference on the chart.** A stacked area keeps two accurate readings, the total and the bottom band. Removing the fixed baseline removes both. What it returns is that no single series is forced to absorb every wiggle underneath it.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| What was the total at each point? | [Line chart](line-chart.md) or [area chart](area-chart.md) of the total. Here the total is a thickness with no axis under it |
| How did this one component change? | [Line chart](line-chart.md) of that component, or small multiples. The FT's caution on area charts is about exactly this, and this is the extreme case of it |
| What is each component's share? | A 100% stacked area, or lines of shares. See [stacked-area-chart.md](stacked-area-chart.md) |
| Any question with a number in the answer | Anything with an axis. A table, if the numbers are the point |
| There are few components | [Stacked area chart](stacked-area-chart.md), which keeps the baseline and the total |
| A few discrete periods | [Stacked bar](stacked-bar.md) |
| The reader has to defend a conclusion drawn from it | A form whose readings can be checked against an axis |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | Cumulative sum across series at each x, **plus a baseline offset computed from the data**, commonly to center the bands or to smooth their overall movement. The series order is also usually computed rather than chosen |
| Geometry | One filled band per series, between two computed boundaries |
| Scale | Time to position on x, value to **band thickness** at each x. No series' value maps to a position on a fixed scale |
| Coordinates | Cartesian |
| Guides | An x axis. A y axis is usually absent, and where one is drawn its origin is a computed offset rather than zero. Direct labels on the bands, or a legend |

**This is [stacked-area-chart.md](stacked-area-chart.md) with the baseline slot turned into a free parameter**, and that single change is the whole of the form. A baseline fixed at zero gives a stacked area back.

**No source in this wiki describes the layout algorithms**, so the transform row above says what the offset does and not how any particular implementation computes it. No named algorithm is recorded here.

## Channels

**Band thickness, for every series, with no common baseline anywhere on the chart.**

That is definitional. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured the divided bar, where the first segment sits on the axis and every segment above it floats; [stacked-bar.md](stacked-bar.md) carries the quote and the 40% to 250% figure. A stacked area keeps that split: the bottom band and the total are still read against the axis. **A streamgraph keeps neither, because the baseline is itself a function of the data.** Nothing on the chart is a position reading against a fixed scale, including the total.

Two further steps separate this from the thing that was measured, and both are reasoning rather than measurement: the bands are bounded by curves rather than by straight parallel edges, and the reference those thicknesses are judged against moves along the x axis. **Neither has been tested on readers in this corpus.**

**Hue carries series identity**, which is not a magnitude channel and is not scored as one ([what "color is the worst channel" actually means](../concepts/channels.md#what-color-is-the-worst-channel-actually-means)).

## What it is measurably good at

**Nothing. No study in this corpus tests a streamgraph.**

## What it is measurably bad at

Nothing measured on this form.

**The aspect ratio exposure is inherited and it is undiluted.** Vertical scaling changes every band thickness on the chart at once, and [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) moved reader judgments by 129.5% on a line chart by changing nothing else. That was a line chart with the true values printed on it, not a streamgraph, and the transfer is inheritance rather than a native finding; the group-level statement is in [change-over-time.md](change-over-time.md).

**Truncation is the one inherited hazard that does not land cleanly.** [Correll et al. (2020)](../studies/correll-2020-truncating-the-y-axis.md) measured cropping a quantitative axis, and this form usually has no meaningful y axis to crop. That is not an exemption. It means the reader has nothing to check the vertical extent against at all, which is a different problem and an unmeasured one.

## What is contested

**Nothing. There is no record here to disagree with itself, and there is barely a record.**

The nearest thing to a position anyone in this corpus takes is the FT's one-line gloss on area charts: "Use with care -- these are good at showing changes to total, but seeing change in components can be very difficult" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). That is `authority-asserted`, it was written about area charts rather than about this form, and applying it here is reasoning from the reason the FT gave rather than a gloss the FT wrote. Components are what this form is made of, and it has fewer fixed references than the chart the caution was written for.

## The failure mode it invites

**Presenting a qualitative picture as if it were a readable chart.** The form is dense, continuous and attractive, and it looks like it supports the questions a stacked area supports. It supports fewer of them, because it has fewer fixed references, and nothing on the drawing tells the reader that.

**Leaving the baseline and the series order unrecorded.** Both are computed, both change the picture completely, and neither is visible to the reader as a choice. This is the same hazard [waterfall-chart.md](waterfall-chart.md) names for step order, and the same one [change-over-time.md](change-over-time.md) names for aspect ratio: a free parameter that decides what the figure says and leaves no trace in the figure.

Both follow from the structure. Neither has been tested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing. No study in this corpus touches this form, and unlike a stacked area it has no fixed baseline from which to inherit the position reading.

**Defensible, with the label said out loud:**

- "Many series, and what the reader is meant to take away is the shape of the whole and which bands are large. No value is claimed to be readable off it." That is a statement about what the form is, and what a reader actually takes away is untested.
- "The caption names the series order and how the baseline was set." Follows from the structure, untested, and it costs one sentence.
- "The components that matter are also drawn separately." Widely asserted, including by the FT's gloss on the parent form, and never tested.

**Commonly repeated, and the evidence does not support it:**

- ~~"A streamgraph shows how each component changed over time."~~ It shows each component's thickness against a moving reference. The one version of that comparison anybody measured, on divided bars, was the most expensive reading on the chart, and this form has strictly less to anchor it.
- ~~"The flowing baseline makes the bands easier to read."~~ The baseline is chosen to satisfy a geometric criterion. Whether it helps a reader is untested here, and no source in this wiki even states the criterion.
- ~~"It is a prettier stacked area chart."~~ It is a stacked area chart with the last common baseline removed, which takes the total and the bottom band with it.
- ~~"The total is easy to see, it is the outline."~~ The thickness of the silhouette is the total, and there is no axis under it. Reading it is a thickness judgment like every other one on the chart.

## See also

- [stacked-area-chart.md](stacked-area-chart.md) — the same chart with the baseline fixed at zero, and where the inherited evidence is closest
- [area-chart.md](area-chart.md) — the single-series parent, and the zero-baseline record
- [stacked-bar.md](stacked-bar.md) — the one place the floating-segment cost was actually measured
- [change-over-time.md](change-over-time.md) — the group, and the free parameters it leaves open
- [../concepts/channels.md](../concepts/channels.md) — the inheritance rule this page leans on and then declines to complete
