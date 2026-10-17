---
type: chart-type
relationships: [uncertainty, change-over-time]
aliases: [Fan chart, Fan chart (projection)]
---

# Fan chart

A projected series drawn as a central path with nested bands around it, each band a stated probability interval, widening as the projection runs further from the last observation.

The [FT](../sources/ft-visual-vocabulary.md) files **Fan chart (projection)** under Change over Time: "Use to show the uncertainty in future projections - usually this grows the further forward to projection". No other source here defines the form.

## When to reach for it, and when not

The form is defined for one quantity projected forward from a known history, where the reader's question is how wide the plausible range is at each horizon and how fast it widens. It needs a predictive distribution per period, not a single path, and the bands are the claim rather than decoration around a forecast.

| The question | Alternative |
|---|---|
| What happened? | A [line chart](line-chart.md). History has no fan |
| How sure is this one estimate? | An [interval plot](interval-plot.md) or [gradient plot](gradient-plot.md), the group's tested forms |
| Which of several scenarios? | One line per named scenario. A scenario is not a quantile, and a fan pools them into a probability |
| How spread out were past values? | [Distribution](distribution.md) per period. A fan shows what the model does not know, not what the data did |
| Do the bounds have to be read as numbers? | A table of quantiles per horizon |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per future period with a point projection and a set of quantiles, or a sample of simulated paths from which quantiles are taken |
| Transform | Quantiles of the predictive distribution per period, paired into nested intervals at stated probabilities |
| Geometry | A line for the central path and a filled band between each quantile pair, stacked outward |
| Scale | Value to vertical position along a common scale shared with the observed series. Interval probability to shade, darker toward the center |
| Coordinates | Cartesian, time on the horizontal axis, with a boundary between observed and projected |
| Guides | Both axes, the observed-to-projected boundary, and a key stating what each band is and how the distribution was produced |

In construction it is a [gradient plot](gradient-plot.md) along a time axis: a symmetric spread around an estimate, shaded by probability. It differs in having hard edges between bands and a central path that reads as a line.

## Channels

The central path is position along a common scale, the most accurately read channel in [channels.md](../concepts/channels.md). The width at any horizon is length against a vertical scale, and the probability of each band is shading, which sits at the bottom of the measured ordering. The step from mark to channel is conjecture in the source literature, and no study here tests the form.

## What is measured

No study in this corpus tests the form. The nearest result does not transfer. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) found that a continuous gradient around a mean avoided the within-the-bar bias a bar with error bars showed, on a categorical axis with one estimate per group, not nested bands along a time axis. [Belia et al. (2005)](../studies/belia-2005-ci-misconceptions.md) measured published authors misreading labeled CI and SE bars; a fan's bands can be any interval type and look the same, and whether nested bands are read better or worse than a single whisker is untested. `absence of evidence`.

## The failure mode it invites

**The central path read as the forecast and the fan as decoration.** The path is one quantile or point estimate, and the bands are what the model asserts. A reading that keeps the line and discards the fan keeps the one number the chart exists to qualify. `authority-asserted`.

**Bands without a stated probability.** A 90 percent interval and a one-standard-deviation band draw identically. The interval's meaning sits on no channel ([uncertainty.md](uncertainty.md)), and only the key carries it.

**A wide fan read as a large value.** Whether readers take the band's extent for the quantity's rather than for its probability is untested here. `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing qualifies. No experiment here involves the form.

**Defensible, with the label said out loud:**

- "The key names each band's probability and the model that produced it. Published authors misread even labeled intervals, measured, so the label is necessary and not sufficient."
- "A fan rather than a single forecast line. The line alone asserts a precision the model does not have, which is a fact about the model and not a measured fact about readers."
- "Three bands rather than a continuous gradient. A newsroom taxonomy describes the banded form, and nobody here has tested bands against a ramp."

**Commonly repeated, and the evidence does not support it:**

- ~~"Readers see that the fan widens because uncertainty grows."~~ The FT says the uncertainty "usually" grows with horizon. Whether readers read the widening that way is untested.
- ~~"Fan charts communicate uncertainty better than error bars."~~ No study here compares them.
- ~~"The darkest band is where the value will be."~~ The darkest band is the most probable interval at its stated probability, and the outer bands hold the rest of the mass.

## See also

- [uncertainty.md](uncertainty.md): the group, and why the interval's meaning lives in the key
- [change-over-time.md](change-over-time.md): where the FT files the form
- [gradient-plot.md](gradient-plot.md): the tested form it most resembles in construction
- [interval-plot.md](interval-plot.md): one estimate with a labeled interval
