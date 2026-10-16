---
type: chart-type
relationships: [change-over-time]
aliases: [Area chart]
---

# Area charts

A [line chart](line-chart.md) with the region between the path and a baseline filled, so the quantity is carried by the filled area as well as by the boundary's position.

## When to reach for it, and when not

The form applies where the amount under the curve is a quantity (volume shipped, hours logged, total spend), or where a few stacked series have a total that matters as much as the parts. The fill double-encodes the number, occludes what is behind it, and brings the zero baseline into scope.

| The question | Alternative |
|---|---|
| How do these four series' trends compare? | [Line chart](line-chart.md). Fills occlude, and upper bands share no baseline |
| How did this one component change? | [Line chart](line-chart.md) of that component, or small multiples. The FT: area charts are "good at showing changes to total, but seeing change in components can be very difficult" |
| The interesting range excludes zero | [Line chart](line-chart.md). A filled mark off its baseline breaks the one rule every source here agrees on |
| The quantity is a rate, an index, a temperature | [Line chart](line-chart.md). If the integral is not a thing, the area is decoration |
| Composition across a few discrete periods | [Stacked bar](stacked-bar.md) |
| Only the shares matter | A 100% stacked area, which drops the total the fill was for ([stacked-bar.md](stacked-bar.md) has the same trade) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value) |
| Transform | None for one series. Cumulative sum across series when stacked, optionally normalized to 100% |
| Geometry | Filled polygon between the path and a baseline, usually with the boundary drawn |
| Scale | Time to position on x. Value to position on y, and to the fill's height at each x |
| Coordinates | Cartesian |
| Guides | Two axes including the baseline, and a legend or direct labels on the bands |

It is a line chart plus a fill. With categories on x it becomes a [stacked bar](stacked-bar.md), whose channel problem the stacked version inherits.

## Channels

The boundary is position along a common scale and the fill is area, which ranks below position and angle ([channels.md](../concepts/channels.md); the mark-to-channel step is conjecture in the source literature). In a stacked area only the bottom band sits on the axis, the structure Cleveland & McGill measured on divided bars: "All other values must be compared by the elementary task of perceiving different bar lengths" ([stacked-bar.md](stacked-bar.md) has the full quote and the 40% to 250% error figure). The transfer from bars to bands is reasoning.

## What is measured

No study in this corpus tests what the form is for, a legible total with visible parts. That purpose is `authority-asserted`. The "area chart" in [Skau & Kosara (2016)](../studies/skau-kosara-2016.md), which beat their angle-only conditions, is a pie-cue isolation stimulus, not this form, so it does not transfer.

The line chart's exposures apply unchanged: aspect ratio, truncation, silently repaired gaps, log axes ([line-chart.md](line-chart.md#what-is-measured)).

Inverted axes reverse the reading. The reversal condition in [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) was a line-area chart with a flipped y-axis, the paper's largest effect. Per Table 3, 39 of 40 control participants answered correctly, against 7 of 38 in the deceptive condition, where 30 answered incorrectly (Fisher exact p < 0.0001). The paper's Discussion swaps the conditions, and the table is the record ([refutations.md](../refutations.md)). With one chart, one scenario and 38 against 40, the direction holds but the study is not well powered. `evidence-backed`.

**The zero baseline.** Most of the disagreement on [line-chart.md](line-chart.md) disappears here, because every source binds the rule to the mark and this is the mark. Wilke's proportional ink covers shaded areas. The Urban Institute scopes its absolute to length or height encodings. Observable Plot forces zero where area encodes the value, and Vega-Lite forces it for area marks before its broader default applies. That agreement is `authority-asserted`, and the headcount overstates it. No experiment here tests a truncated filled area. Wilke states the principle without measuring it ([wilke-fundamentals.md](../sources/wilke-fundamentals.md)), and two of the four are software defaults. The FT and Schwabish are not independent voices: Urban names Schwabish its sole contact, and the FT credits his Graphic Continuum ([urban-institute.md](../sources/urban-institute.md), [ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The nearest measurement, Pandey et al.'s area-as-quantity condition, is a bubble chart, a different mark.

**Whether the fill helps.** Practitioners, the FT included, say it helps the total and hurts the components. Untested here. `absence of evidence`.

## The failure mode it invites

**Stacking until the bands are unreadable, then asking the reader to track one.** The stacked-bar remedy applies: the series in question on the baseline, or drawn as its own line.

**Filling because it looks better.** A fill asserts the area is a quantity, which a rate, index, price or temperature is not. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- "The axis is not inverted, and I checked. The one reversal experiment in this corpus used a line-area chart and 30 of 38 readers reached the opposite conclusion from the correct one."
- Everything on [line-chart.md](line-chart.md#justifying-the-choice) about truncation, missing values and log axes, inherited unchanged.

**Defensible, with the label said out loud:**

- "It starts at zero because the mark is filled, and proportional ink is scoped by mark. That is four sources agreeing and no experiment; two of the four are software defaults, and the other two, the FT and Schwabish, descend from the same poster."
- "I filled it because cumulative volume is the quantity the reader wants, and I stacked only three components. Both of those are convention, not measured thresholds."
- "The components are also drawn as small multiples, because seeing change in a component inside a stack is the thing this form is worst at." Widely asserted, including by the FT's gloss, and never tested. `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"Readers can follow each band in a stacked area."~~ Only the bottom one. On bars, the floating comparison carries 40% to 250% more error than position.
- ~~"The fill makes the trend easier to see."~~ Untested here. `absence of evidence`.
- ~~"An area chart is just a prettier line chart."~~ The fill restores the zero baseline and occludes what is behind it.

## See also

- [line-chart.md](line-chart.md): the same chart without the fill, and most of the evidence
- [stacked-bar.md](stacked-bar.md): the measured version of the floating-band problem
- [change-over-time.md](change-over-time.md): the group
- [../concepts/channels.md](../concepts/channels.md): the inherited channel evidence
