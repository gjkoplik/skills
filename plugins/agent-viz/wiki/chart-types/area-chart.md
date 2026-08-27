---
type: chart-type
relationships: [change-over-time]
aliases: [Area chart]
---

# Area charts

A [line chart](line-chart.md) with the region between the path and a baseline filled, so the quantity is carried by the filled area as well as by the boundary's position.

## When to reach for it, and when not

**Reach for it when** the accumulated amount under the curve is a real quantity the reader cares about (volume shipped, hours logged, total spend), or when a stacked set has a total that matters as much as its parts. One series, or a small number of stacked ones.

**The fill is the whole difference from a line chart, and it is not free.** It puts a second encoding on the same number, it occludes anything behind it, and it brings the zero baseline back into scope. Fill because the area means something, not because the chart looked empty.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| How do these four series' trends compare? | [Line chart](line-chart.md). Fills occlude each other, and stacked bands above the bottom have no shared baseline |
| How did this one component change? | [Line chart](line-chart.md) of that component, or small multiples. The FT's own gloss: area charts are "good at showing changes to total, but seeing change in components can be very difficult" |
| The interesting range excludes zero | [Line chart](line-chart.md). A filled mark that does not start at its baseline breaks the one rule this whole corpus agrees on |
| The quantity is a rate, an index, a temperature | [Line chart](line-chart.md). If the integral under the curve is not a thing, the area is decoration standing in for data |
| Composition across a few discrete periods | [Stacked bar](stacked-bar.md) |
| Only the shares matter | A 100% stacked area, knowing it removes the total, which is the reason you filled it in the first place. Same trade [stacked-bar.md](stacked-bar.md) documents |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | None for a single series. Cumulative sum across series for a stacked area, optionally normalized to 100% |
| Geometry | Filled polygon between the path and a baseline, usually with the boundary drawn |
| Scale | Time to position on x, value to position on y, and simultaneously to the height of the fill at each x |
| Coordinates | Cartesian |
| Guides | Two axes including the baseline, legend or direct labels on the bands |

**One slot from a line chart, one slot from a stacked bar.** Add a fill to [line-chart.md](line-chart.md) and you get this. Replace the continuous x with categories and you get [stacked-bar.md](stacked-bar.md), which is why the stacked version inherits that page's channel problem rather than having one of its own.

## Channels

**Position along a common scale** for the boundary, and **area** for the fill, both inherited from [channels.md](../concepts/channels.md) rather than measured on this form. Area is measured below position and below angle, and the mapping from this chart to those channels is the conjectural step the inheritance rule exists to flag.

For a **stacked** area, only the bottom band sits on the axis. Every band above it floats, which is the structure Cleveland & McGill measured directly on divided bars: "All other values must be compared by the elementary task of perceiving different bar lengths" ([stacked-bar.md](stacked-bar.md) carries the full quote and the 40% to 250% error figure). That transfer from bars to bands over a continuous axis is reasoning, not measurement.

**A caution about miscitation.** [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) report that error was smaller for their "area chart" than for their angle-only conditions. That stimulus is a pie-cue isolation condition, not this chart. It says nothing about area charts.

## What it is measurably good at

**Nothing in this corpus measures it.** No study here tests an area chart against a line chart, or against anything else, on any task. The form's stated purpose, making a total legible while its parts stay visible, is `authority-asserted` across the practitioner literature and unmeasured.

## What it is measurably bad at

**Everything the line chart is bad at**, since it is a line chart plus a fill: aspect ratio, truncation, silently repaired gaps and log axes all apply unchanged. See [what it is measurably bad at](line-chart.md#what-it-is-measurably-bad-at) rather than a restatement here.

**Surviving an inverted axis.** This is the closest thing to a native finding. The reversal condition in [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) was a line-area chart with a flipped y-axis, and the effect is the largest in that paper. From its Table 3: in the control condition 39 of 40 participants answered correctly; in the deceptive condition 7 of 38 answered correctly and 30 answered incorrectly, Fisher exact p < 0.0001. **Quote the table and not the Discussion**, which mislabels these figures and swaps the conditions; see [refutations.md](../refutations.md). Caveats: one chart, one scenario, n of 38 against 40. The effect is enormous and the test is exact, so the direction is not in doubt, but this is not a well-powered study.

**Tracking a band that is not on the baseline**, in the stacked variant. Inherited from the divided-bar measurement rather than measured here.

## What is contested

Less than you would expect: the disagreement that lives on [line-chart.md](line-chart.md) mostly evaporates here.

**The zero baseline.** Every source in this corpus binds the rule to the mark, and this mark is the one it binds to. Wilke's proportional-ink principle covers shaded areas; the Urban Institute scopes its absolute to charts that use length or height as the primary encoding and releases lines and scatterplots by name; Observable Plot forces zero exactly where area encodes the value; Vega-Lite forces zero for area marks at the mark level, before its broader default even applies. Four sources, one answer.

**That agreement is `authority-asserted`, not evidence-backed, and a headcount overstates it.** No experiment in this corpus tests a truncated filled area against an untruncated one. Wilke states the principle rather than measuring it ([wilke-fundamentals.md](../sources/wilke-fundamentals.md)); two of the four are software defaults, which is a design position shipped as code. And before adding the FT and Schwabish to the tally, note that the Urban guide names Schwabish as its sole point of contact and the FT credits his Graphic Continuum as its own inspiration ([urban-institute.md](../sources/urban-institute.md), [ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)), so several of the voices are one voice. The nearest measurement, Pandey et al.'s area-as-quantity condition, is a bubble chart where area is the only encoding, which is a different mark doing a different job. The rule is sound reasoning that everybody endorses, and it is not a finding.

**Whether the fill helps at all.** Unmeasured in either direction. The FT's gloss and the general practitioner position are that the fill helps the total and hurts the components, and no study here tests that split. `absence of evidence`.

## The failure mode it invites

**Stacking until the bands stop being readable, then inviting the reader to track one.** Each band above the baseline floats, so following the orange band across the chart is a set of length judgments with no shared reference, which is the one thing the divided-bar literature measured and found expensive. The remedy is the same as for stacked bars: put the series in question on the baseline, or take it out and draw it as its own line.

**Filling because it looks better.** A fill asserts that the area is a quantity. On a rate, an index, a price or a temperature it is not, and the reader is being handed an encoding that means nothing. `authority-asserted`, and it follows from what the mark is rather than from taste.

## Justifying the choice

**Defensible, evidence-backed:**

- "The axis is not inverted, and I checked. The one reversal experiment in this corpus used a line-area chart and 30 of 38 readers reached the opposite conclusion from the correct one."
- Everything on [line-chart.md](line-chart.md#justifying-the-choice) about truncation, missing values and log axes, inherited unchanged.

**Defensible, with the label said out loud:**

- "It starts at zero because the mark is filled, and proportional ink is scoped by mark. That is four sources agreeing and no experiment, and two of the four are software defaults rather than findings."
- "I filled it because cumulative volume is the quantity the reader wants, and I stacked only three components. Both of those are convention, not measured thresholds."
- "The components are also drawn as small multiples, because seeing change in a component inside a stack is the thing this form is worst at." Widely asserted, including by the FT's own one-line gloss, and never tested.

**Commonly repeated, and the evidence does not support it:**

- ~~"Readers can follow each band in a stacked area."~~ They can follow the bottom one. Everything above it floats, and the bar version of exactly that comparison carries 40% to 250% more error than a position reading.
- ~~"The fill makes the trend easier to see."~~ No study in this corpus tests a filled series against an unfilled one. Absence of evidence, not a refutation, and not a justification either.
- ~~"An area chart is just a prettier line chart."~~ It is a line chart with one slot changed, and that slot is what puts the zero baseline back in force and what occludes everything behind it.

## See also

- [line-chart.md](line-chart.md) — the same chart minus the fill, and where most of the evidence lives
- [stacked-bar.md](stacked-bar.md) — the measured version of the floating-band problem
- [change-over-time.md](change-over-time.md) — the group
- [../concepts/channels.md](../concepts/channels.md) — the inheritance rule this page leans on twice
