---
type: chart-type
relationships: [spatial, magnitude]
aliases: [Cartogram, Dorling cartogram, Hex grid map, Tile grid map]
---

# Cartograms

A map whose regions are resized, or replaced by simpler shapes, so that each region's area encodes a value and the geography distorts to fit.

In a value-by-area cartogram (contiguous, non-contiguous, Dorling circles) area is the encoding. A tile or hex grid map gives every region an identical cell, removing area as both distortion and encoding, so the value goes back to fill color. **A tile grid map is a [choropleth](choropleth-map.md) on a schematic base geography.** This page covers the value-by-area kind.

## When to reach for it, and when not

The form is defined for a total whose distribution is badly out of proportion to the base geography's land areas, where the mismatch is part of the message. The sentence it makes is "the map you are picturing is the wrong shape for this quantity."

| The question | Alternative |
|---|---|
| Which is biggest, and in what order? | Sorted bar chart. Area does not support reliable ordering by eye |
| The value is a rate | [Choropleth](choropleth-map.md). Rates do not add up over area |
| The reader has to find their own region | [Choropleth](choropleth-map.md), or a table. The form spends recognizability |
| The audience does not already know this map well | Almost anything else. Distortion reads only against a map the reader already holds |
| What are the exact values? | A table, or a sorted bar chart |
| How did it change between two years? | Not two cartograms. The layout is recomputed per dataset |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per region, with a boundary and a magnitude, normally a total |
| Transform | An area-equalizing layout algorithm that resizes and relocates regions under contiguity, shape and topology constraints |
| Geometry | Distorted polygon, circle (Dorling), or uniform tile |
| Scale | Magnitude to area, anchored at zero for the encoding to be proportional |
| Coordinates | A named projection, with a distortion applied on top |
| Guides | An area legend with at least two reference sizes, region labels (shape no longer identifies anything), and often an inset of the true geography |

The layout algorithm sits in the transform slot, as on a [treemap](treemap.md), so choosing it is an encoding decision. Zero is required, as on a [bubble chart](bubble-chart.md).

## Channels

Area, plus geographic position degraded on purpose. Area is read less accurately than angle and much less accurately than position ([channels.md](../concepts/channels.md); [Heer & Bostock 2010](../studies/heer-bostock-2010.md)), and circular and rectangular area are comparably accurate. Contiguous cartogram shapes are neither.

Heer & Bostock's Experiment 1B "extended circular area judgment to rectangles, motivated by treemaps and cartograms." It was a 3x2x6 factorial, 108 trials, on pairs of marked rectangles shown bare and inside a full treemap, at 380x380 pixels, with aspect ratios from a squarified treemap layout. Rectangular area was about as accurate as circular, and aspect ratio 1 was the worst case. No map, distorted polygon or recognizability task was tested, so only the channel-level claim transfers.

## What it is measurably good at

No study in this corpus tests the form.

## What it is measurably bad at

Nothing measured beyond the inherited area channel. The native cost is definitional. A cartogram fixes the [choropleth](choropleth-map.md)'s land-area weighting by distorting the geography, and pays in recognizability, since the shapes and adjacencies a reader navigates by are what the algorithm moved.

Whether readers lose more from the distortion than they gain from the weighting is untested. `absence of evidence`.

## What is contested

Nothing contested in this corpus.

## The failure mode it invites

**Assuming the reader knows the map.** Without that mental image, a cartogram is an unlabeled abstract shape diagram. `authority-asserted`, following from the construction.

**Sizing a rate.** Area adds over regions and a rate does not, so a region sized by its unemployment rate asserts a quantity that does not exist. It mirrors the choropleth's totals error.

**Scaling by a linear dimension instead of area.** Large values inflate quadratically and it does not look wrong ([bubble-chart.md](bubble-chart.md)).

**Comparing two cartograms.** Each region changes place and shape, as with two [treemaps](treemap.md).

**Calling a tile grid map a cartogram** and claiming area honesty it lacks. Every [choropleth](choropleth-map.md) caution applies.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing native. The one inherited sentence is a caution, not a justification: "area is read less accurately than angle and much less accurately than position, measured, so the reader is not expected to take numbers off this figure" ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "A cartogram because the choropleth of this total was a map of land area with a color layer on it. That reasoning is structural rather than measured, and no study here tests whether readers do better on the cartogram."
- "Region areas are proportional to the count and anchored at zero, so the visual weight in this figure comes from the variable." Definitional, and the entire claim the form supports.
- "An inset shows the true geography, and every region is labeled." Practitioner convention, no measured value.
- "The layout algorithm is named in the caption, because a different one gives a different picture."

**Commonly repeated, and the evidence does not support it:**

- ~~"Heer & Bostock validated cartograms."~~ They named cartograms as a motivation and measured rectangles. There is no map in that paper.
- ~~"A cartogram is more accurate than a choropleth."~~ Neither has been measured. Only the weighting claim is structural.
- ~~"Distortion is fine, people adjust."~~ Untested either way. The form trades a certain defect for an uncertain one.

## See also

- [spatial.md](spatial.md): the group, and the area argument for all three forms
- [choropleth-map.md](choropleth-map.md): the form this one reacts to
- [treemap.md](treemap.md): the other layout algorithm in the transform slot
- [bubble-chart.md](bubble-chart.md): area scaling, zero anchoring, and the size legend
- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md): the rectangle experiment, and what it did not measure
