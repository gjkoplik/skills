---
type: chart-type
relationships: [change-over-time]
aliases: [Horizon graph, Horizon chart]
---

# Horizon graphs

A filled time series cut into bands of equal value range, with the bands layered into one short strip and darker shading for higher bands, and negative values usually mirrored above the baseline in a second hue.

[Schwabish](../sources/schwabish.md) files **Horizon** under Time (contents pages only), and his publisher's description names "horizon charts". [people/jeffrey-heer.md](../people/jeffrey-heer.md) says horizon graph. The [FT](../sources/ft-visual-vocabulary.md) has no entry.

## When to reach for it, and when not

The form is defined for many time series stacked in little vertical space, where each series' values are compared and the full-height chart would not fit. Mirroring halves the height, and each added band divides it again.

| The question | Alternative |
|---|---|
| A few series, with values read off an axis | [Line chart](line-chart.md) |
| Shape only, inside a sentence or a table row | [Sparkline](sparkline.md) |
| How fast is it changing, or where does it turn? | [Line chart](line-chart.md). The one study of this form scored value comparison only |
| The series are parts of a total | [Stacked area chart](stacked-area-chart.md) |
| The area under the curve is the quantity | [Area chart](area-chart.md) |
| What are the exact values? | [A table](tables.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (series, time, value), usually for many series |
| Transform | Subtract the baseline, split the range into n bands of equal width, and fold negatives above the baseline. Each point becomes a sign, a band index and a remainder |
| Geometry | Filled area per band, overlaid in one strip |
| Scale | Remainder to height within the strip, band index to lightness or saturation, sign to hue |
| Coordinates | Cartesian, one fixed-height strip per series |
| Guides | A time axis and a key from shade and hue to value range and sign. Usually no y axis per strip |

Unfolded, it is an [area chart](area-chart.md). With one band and no mirroring it is a filled line chart.

## Channels

Within a band, value is height in the strip, position along a common scale ([channels.md](../concepts/channels.md)). Across bands it is shading or saturation, at the bottom of the Cleveland & McGill ordering, a rank that page records as `authority-asserted`. So a value is read by combining a band, judged from shade, with a height inside it. Sign is hue used for identity, a job hue does well. The step from mark to channel is conjecture in the source literature.

## What is measured

[Heer, Kong & Agrawala (2009)](../studies/heer-2009-horizon-graphs.md), *Sizing the Horizon*, compared line charts with mirrored and layered variants across heights, scoring value-comparison error against a within-5-values target. Every result below is `evidence-backed` for that task only.

- **Mirroring.** Flipping negatives above the axis in a different color "neither slowed estimation time nor hurt estimation accuracy," at half the height.
- **Layering.** Bands increased time and error at constant height. Below 24 pixels, two-band mirrored charts were more accurate than line charts and one-band mirrored charts of the same height. In the data the three were comparable at 12 pixels and the two-band advantage showed at 6, and the analysis found no significant chart-by-height interaction. Four bands, the most tested, were worse on both measures, and subjects called them tiring.
- **Size.** For line charts and one-band mirror charts, 24 pixels minimized estimation time without costing accuracy.

Rates of change were not measured. The authors note that "graphical perception of time series typically involves observing rates of change in addition to comparing values." Whether horizon graphs serve trend or turning-point reading is `absence of evidence`.

## The failure mode it invites

**Too many bands.** Each band saves height and adds a shade to decode. Four measured worse, above.

**Reading height as the value.** Two points at the same height in different bands differ by a whole band's range, and only the shade and the key say so. That follows from the structure. Whether readers make the error is untested, `absence of evidence`.

**Strips that do not share a band width.** As with stacked [sparklines](sparkline.md), independently scaled strips look comparable and are not, and the drawing does not record which was done. Untested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

- "Negatives are mirrored above the baseline in a second hue. In the one study of this form, mirroring cost neither time nor accuracy, at half the height."
- "Two bands rather than four. Four bands were slower and less accurate on value comparison, and subjects found them tiring."
- "Each strip is about 24 pixels tall. In that study, 24 pixels minimized estimation time for line charts and one-band mirror charts without costing accuracy." Value comparison only.

**Defensible, with the label said out loud:**

- "Every strip shares one band width, and the key says what each shade spans." Follows from the structure, untested.
- "The task is comparing values across thirty series. That is what the study measured; trend reading is not."

**Commonly repeated, and the evidence does not support it:**

- ~~"Horizon graphs show trends better than line charts."~~ Only value comparison was measured.
- ~~"More bands means more resolution, so more accuracy."~~ Four bands measured worse on time and error.
- ~~"Folding the negatives over confuses readers."~~ Mirroring measured as free.

## See also

- [change-over-time.md](change-over-time.md): the group
- [area-chart.md](area-chart.md): the unfolded form
- [sparkline.md](sparkline.md): the other form built for little height
- [line-chart.md](line-chart.md): the comparison form in the study
- [../studies/heer-2009-horizon-graphs.md](../studies/heer-2009-horizon-graphs.md): the study, read at primary
