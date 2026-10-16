---
type: chart-type
relationships: [magnitude, ranking]
aliases: [Lollipop chart]
---

# Lollipop charts

A dot at the value with a thin stem back to the baseline, which makes it a [bar chart](bar-chart.md) with the fill taken out.

## When to reach for it, and when not

The form is defined for long sorted lists, where filled bars become a block of ink. The FT's gloss ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Lollipop charts draw more attention to the data value than standard bar/column -- **does not HAVE to start at zero (but preferable)**"

Both halves are `authority-asserted` and untested.

| The question | Alternative |
|---|---|
| How many times bigger is this than that? | [Bar chart](bar-chart.md), which has measured support for ratios |
| There are six categories | [Bar chart](bar-chart.md). At six bars there is no ink to save |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). Neither form asserts a total |
| Two values per category, and the gap is the point | [Dumbbell plot](dumbbell-plot.md), where the stem spans the gap |
| What does the distribution look like? | A histogram or a univariate scatterplot |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with a magnitude |
| Transform | None, usually |
| Geometry | A point at the value, plus a rule from the baseline to the point |
| Scale | Magnitude to position |
| Coordinates | Cartesian |
| Guides | One quantitative axis, a category axis, labels |

It differs from a bar chart only in the geometry slot.

## Channels

The value is position along a common scale, read at the dot instead of the bar's end, a mapping that is conjecture in the source literature ([channels.md](../concepts/channels.md)). The stem is a guide, not an encoding. Without it the chart is a dot plot.

With no filled area, the zero baseline is `contested` among authorities and untested on either side. The FT says the lollipop "does not HAVE to start at zero (but preferable)", against "Must always start at 0 on the axis" for the filled column ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). Both sit in Magnitude, so the FT scopes the rule by mark *within* size comparison. Datawrapper says "Readers don't expect dot plots (or, for two values, range plots) to start at zero because there's no filled bar or column that would indicate that" ([datawrapper-academy.md](../sources/datawrapper-academy.md)). Urban releases marks that "do not use length or height as the primary encoding" ([urban-institute.md](../sources/urban-institute.md)). [Vega-Lite](../sources/vega-lite.md) forces zero on every quantitative positional scale. Each position is `authority-asserted`.

## What is measured

No study in this corpus tests the form. `absence of evidence`. Sharing a bar's channel does not license "as accurate as a bar chart." Three nearby results do not transfer.

- [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) note that "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots." A lollipop keeps its stem, so it is not a dot plot.
- [Skau, Harrison & Kosara (2015)](../studies/skau-2015-embellished-bars.md) found that rounded or pointed bar tops raised error while a strong horizontal cap did not. They proposed that readers "rely on strong lines at the ends of bars to mentally extend the bar end to the value axis." A lollipop swaps that terminator for a circle. They did not test one, and the mechanism is a hypothesis, so applying it here is extrapolation.
- [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) found that truncating a **bar** axis moved size judgments 91%. Whether a stem acts like a bar is untested.

## The failure mode it invites

**Relaxing the baseline on a chart read as bars.** The stem runs from the axis as a bar does, so "no filled area, so no proportional-ink claim" may be weaker in a reader's eye than on paper. `absence of evidence`, not a prohibition, and the FT hedges with "but preferable."

**Using it at small category counts to look less ordinary.** At six categories a bar chart is more familiar and better evidenced. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The inherited sentence is true of a [bar chart](bar-chart.md) too: "the value is on position along a common scale, which is the most accurately read channel."

**Defensible, with the label said out loud:**

- "Forty categories in filled bars is a wall of ink, so the fill comes out. That is a legibility judgment, not a measured improvement."
- "The axis does not start at zero, because the mark is not filled. A taxonomy, a chart tool and a style guide all scope the rule that way, none of them tested it, and one plotting library disagrees outright."
- "This draws attention to the value point rather than the bar's mass. Asserted by the FT in one line, and unmeasured."

**Commonly repeated, and the evidence does not support it:**

- ~~"A lollipop is as accurate as a bar chart, with less ink."~~ Unmeasured, and the one proposed mechanism predicts slightly worse.
- ~~"Dot-based charts are safe to truncate, and it has been shown."~~ The scoping is a practitioner default. Only truncating a *filled bar* was shown to move readers.

## See also

- [bar-chart.md](bar-chart.md): the filled version, and the evidence
- [magnitude.md](magnitude.md): the group, and the zero-baseline scoping
- [../concepts/evidence-class.md](../concepts/evidence-class.md#what-is-exempt-and-why-the-exemption-matters): why the decomposition carries no label
