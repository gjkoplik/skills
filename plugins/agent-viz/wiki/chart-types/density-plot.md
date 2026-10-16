---
type: chart-type
relationships: [distribution]
aliases: [Density curve, Density plot, KDE plot, Kernel density estimate]
---

# Density plots

A smooth curve over one continuous variable, built by placing a kernel at every observation and summing, so the height at any value is the estimated density there.

[Wilke](../sources/wilke-fundamentals.md) files it with the histogram in chapter 7, "Histograms and density plots", and gives "kernel density estimate" as its other name.

## When to reach for it, and when not

The form is defined for one variable, or a few groups overlaid on one axis, each with enough observations that the curve describes the data rather than the bandwidth, where the question is shape: modes, skew, tails. It answers the [histogram](histogram.md)'s question with a bandwidth in place of a bin width. Wilke, opening chapter 8 (quoted on [ecdf-plot.md](ecdf-plot.md)), says the two "share the limitation that the resulting figure depends to a substantial degree on parameters the user has to choose, such as the bin width for histograms and the bandwidth for density plots."

| The question | Alternative |
|---|---|
| There are eight observations | The observations. A density over a handful of points pictures the bandwidth |
| How many observations fall in this range? | [Histogram](histogram.md) on a count axis |
| What fraction falls below this threshold? | [ECDF](ecdf-plot.md), which has no bandwidth |
| How do twelve groups compare? | [Box plot](boxplot.md) or [violin](violin-plot.md). Overlaid curves cross and hide each other |
| Many groups in a known order | [Ridgeline plot](ridgeline-plot.md) |
| Is this difference between means real? | An estimate, not a sample ([distribution.md](distribution.md)) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, optionally a grouping variable |
| Transform | Kernel density estimate: a kernel and a bandwidth, evaluated on a grid, scaled to integrate to 1, or multiplied by n to encode count |
| Geometry | A line, often filled to the baseline |
| Scale | Value to position on one axis, density to height from zero on the other |
| Coordinates | Cartesian |
| Guides | Value axis with units, a density axis or none, the bandwidth, and n |

It is a histogram with the bins replaced by a kernel, half a [violin](violin-plot.md) without the mirror, and one row of a [ridgeline plot](ridgeline-plot.md). The kernel-estimate consequences on the violin page hold here by definition: density lands where no observation lies, including past a bound unless the kernel is truncated, and bandwidth decides modality.

## Channels

Value is position along a common scale. Density is height from a shared zero, so several curves in one panel also compare on a common scale. Both come from [channels.md](../concepts/channels.md), and the step from mark to channel is conjecture in the source literature. The form is drawn for shape, which the ranking does not measure ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What is measured

No study in this corpus tests the form. Two nearby results do not transfer. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found symmetric, continuous encodings, the violin among them, beat bars with error bars on inferential tasks, but their violins encoded a mean and its error, not a sample, and a density plot is not symmetric. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) measured published group sizes, a median smallest group of 4, not how anyone reads a density.

## The failure mode it invites

**A bandwidth that hides a mode or invents one.** Too wide merges two peaks, too narrow draws a peak per cluster, and a library default sets it without appearing on the chart. Wilke concludes that both forms "have to be considered as an interpretation of the data rather than a direct visualization of the data itself." [inventory.md](../inventory.md) topic 52, from Wilke chapters 7 and 14, treats bandwidth as an analysis choice to set explicitly and check at another setting. `authority-asserted`, and Wilke gives no rule. [checks/matplotlib.md](../checks/matplotlib.md) flags a bare `kdeplot` call.

**Density past the data's bounds.** Durations, counts and proportions show mass below zero or above one. [seaborn](../sources/seaborn.md) warns that symmetric error bars "may extend to 'impossible' values", and the transfer to a kernel is by construction, as on [violin-plot.md](violin-plot.md). Topic 51. `authority-asserted`.

**A density read as a count.** Unless scaled by n, the curve integrates to 1. Two groups normalized separately draw equal areas at eight observations and at eight hundred, and the curve is as smooth at n = 6 as at n = 600. The hazard is definitional. How often readers make the error is `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The one inheritance is the value axis: where the mass sits is position along a common scale ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "Bandwidth is stated, and the second mode survives a wider and a narrower one. Wilke treats bandwidth as an analysis choice with no rule, and no study here sets one."
- "The kernel is truncated at zero, because the quantity cannot be negative."
- "The curves are scaled by count, so the taller group is the larger one, and n is in the legend."

**Commonly repeated, and the evidence does not support it:**

- ~~"A density plot shows the data."~~ It shows an estimate whose shape depends on the bandwidth.
- ~~"Smoother than a histogram, so more accurate."~~ The smoothness is the bandwidth. No study here compares the two.

## See also

- [histogram.md](histogram.md): the same question with a bin width
- [violin-plot.md](violin-plot.md): this curve mirrored, per group
- [ecdf-plot.md](ecdf-plot.md): the distribution with no smoothing parameter
- [distribution.md](distribution.md): the group, and the sample-size gate
