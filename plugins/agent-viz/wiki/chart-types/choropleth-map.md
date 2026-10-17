---
type: chart-type
relationships: [spatial]
aliases: [Choropleth map]
---

# Choropleth maps

A base geography drawn as filled polygons, each region's fill color encoding one value for the whole region.

## When to reach for it, and when not

The form is defined for regions the reader already thinks in, a rate or other intensive quantity that holds at every point inside a region, and a geographic rather than ordinal pattern. The FT's gloss carries two rules: a basic choropleth "should always be rates rather than totals and use a sensible base geography" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The base geography sets the units of analysis, and administrative boundaries were not drawn for the variable. Because each value sits where its region is, a reader who does not know the region names can still see a regional pattern, `absence of evidence`.

| The question | Alternative |
|---|---|
| Which regions are highest, and in what order? | Sorted bar chart. Lightness does not order by eye the way position does |
| How big is the total in each region? | A proportional symbol map (no page here; FT: "Use for totals rather than rates"), or a [cartogram](cartogram.md) |
| Where *within* the region are the things? | [Dot density](dot-density-map.md), where sub-region locations exist |
| What is the value for my region? | A table. Finding one region is a lookup through a color scale |
| How much did it change? | The change itself, mapped |
| The regions vary enormously in size | [Cartogram](cartogram.md), or a tile grid map. Here, land area sets the visual weight |
| The value is a count | [Dot density](dot-density-map.md), a proportional symbol map, or a denominator that makes it a rate |

## Structural decomposition

| Slot | |
|---|---|
| Data | One value per region, keyed to a boundary in a geographic file |
| Transform | Usually two: normalize a count to a rate by a denominator, and bin the values into classes (or not) |
| Geometry | Filled polygon, outlined by the base geography, not the data |
| Scale | Value to fill color, on a sequential or diverging ramp |
| Coordinates | A named map projection |
| Guides | A color legend or colorbar with units, and the projection named. No axis exists |

The geometry takes no input from the data. Every mark's shape, position and size are fixed before any value arrives, where in every other filled-area chart the extent is the encoding. So land area sets a region's visual weight, and large sparse regions dominate while small dense ones vanish. The transform holds the two decisions that change the picture most, the denominator and the binning, and the drawing shows neither.

The rates rule follows from the geometry. The mark asserts one value across a whole territory, which a rate, a property of points inside the region, can bear. A total painted across a polygon claims the count is spread evenly and matters in proportion to land area. A proportional symbol map instead sets the mark's area by the value and uses geography only to place it.

## Channels

The value sits on color lightness, usually with saturation, and position on the map is only location. The 1984 Cleveland & McGill table ranks shading and color saturation last, below area and volume ([channels.md](../concepts/channels.md); the step from chart to channel is conjecture). Ordered lightness is low-accuracy for magnitude. Hue, with no order from small to large, is unsuited to it. So a sequential ramp read imprecisely is a working choropleth, and a categorical palette on an ordered variable is not, which is why inventory topic 23 forbids crossing colormap class with data type.

For [Bertin](../people/jacques-bertin.md), `valeur` (lightness) is ordered but not quantitative, since white cannot serve as a unit for measuring gray. A choropleth supports "more here than there" and not "twice as much there as here". `authority-asserted`; Bertin ran no experiments.

## What is measured

No study in this corpus tests the form, or any map ([spatial.md](spatial.md)). Whether land-area weighting biases readers' conclusions is untested, `absence of evidence`.

## The failure mode it invites

**The population map.** Urban, inventory topic 22: "If the map only shows where people live, it is a population map." Munzner's slides name the same failure, "most attributes just show where people live", and prescribe "normalize when appropriate" ([munzner-vad.md](../sources/munzner-vad.md)). Both `authority-asserted`. Many rates still track density, so a population map is the check.

**An accidental diverging midpoint.** A midpoint left where the library put it asserts a neutral value nobody chose. Topic 32, and Urban's rule: "The center of the diverging palette should always be labeled to avoid confusing the reader." `authority-asserted`.

**Two choropleths on two color scales.** The comparison fails while every cue invites it. One fixed scale across panels, or the difference mapped, avoids it.

**The default binning**, chosen for no particular distribution. How many bins, where the breaks fall, or none, is the biggest open decision on the form, and a different break set can create or erase a pattern without any number changing. Cairo's *The Truthful Art* covers it by its contents and is [`secondary-only`](../sources/cairo-truthful-art.md), so nothing it recommends is vouched here. [Wilke](../sources/wilke-fundamentals.md), read at primary, gives four to six bins as a working range, `authority-asserted`. No reader experiment here tests classification, `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- "The rate is on fill color and the exact values are in the table beneath. Color is read less accurately than position, measured, so nothing precise rides on the map." Inherited from [channels.md](../concepts/channels.md), and the only entry here.

**Defensible, with the label said out loud:**

- "Rates, not totals, and the denominator is stated. That is the FT's rule for this chart and the reasoning is structural; no experiment here tests reader behavior on it."
- "A sequential ramp, because the variable is ordered and has no meaningful midpoint." Topic 23, `authority-asserted` from matplotlib's documentation.
- "Albers Equal Area, named in the caption." Urban's rule for US print maps, topic 21.
- "The palette was run through a color-vision-deficiency check rather than eyeballed." Datawrapper ships the check; topic 26.
- "Five classes with stated breaks, not a continuous ramp." A judgment call, unsupported here.

**Commonly repeated, and the evidence does not support it:**

- ~~"A choropleth shows where the quantity is."~~ It shows where the *rate* is, weighted by land area.
- ~~"Color is the worst channel, so choropleths are the worst chart."~~ The ranking concerns magnitude and separates imprecise lightness from unsuited hue. No study here tests a choropleth.
- ~~"An equal-area projection makes the areas honest."~~ It removes the projection's distortion, not the usually larger mismatch between land area and where the quantity lives.

## See also

- [spatial.md](spatial.md): the group, with nothing evidence-backed
- [cartogram.md](cartogram.md): trades recognizability to fix the area problem
- [dot-density-map.md](dot-density-map.md): handles counts, at the cost of placing dots
- [../concepts/channels.md](../concepts/channels.md): ordered lightness versus hue
- [../people/jacques-bertin.md](../people/jacques-bertin.md): lightness as ordered, not quantitative
