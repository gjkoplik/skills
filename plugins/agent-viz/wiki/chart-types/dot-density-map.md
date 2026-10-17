---
type: chart-type
relationships: [spatial]
aliases: [Dot density map]
---

# Dot density maps

A map carrying one dot per fixed number of units, each dot placed where those units are, so the count reads as the density of ink over the page.

## When to reach for it, and when not

The form is defined for counts of discrete things with known locations, where the message is where they concentrate. The FT's gloss says to "make sure to annotate any patterns the reader should see" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)), since the figure does not deliver a reading alone.

| The question | Alternative |
|---|---|
| How many, exactly, in this region? | A table, or a sorted bar chart |
| The value is a rate | [Choropleth](choropleth-map.md). Dot density is count per area, not rate per person |
| Region totals with no sub-region locations | [Choropleth](choropleth-map.md), or a proportional symbol map |
| The concentrations are urban | Hex-grid binning, or a rate mapped. Dots there saturate |
| There are twelve things | Labeled points |
| Which region is highest? | A sorted bar chart. Comparing ink densities by eye is unsupported |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per unit with a location, or one row per region with a count plus a placement rule |
| Transform | Divide the count by a **dot value** (one dot equals n units), then place the dots |
| Geometry | A small uniform dot, identical for every observation |
| Scale | Count to number of dots, linear and exact. The reader reads dots per unit of area |
| Coordinates | A named map projection |
| Guides | The dot value, in the legend or subtitle, and annotation naming the pattern |

The dot value and placement rule decide what the map says, and neither is visible. Too high a dot value erases small concentrations, and too low saturates everything. Dots scattered at random inside a polygon fabricate a distribution at every finer scale.

Total ink is proportional to the count, so weight follows the variable, not land area, and the form can carry totals where a [choropleth](choropleth-map.md) must not. Past some density the dots fill solid and stop responding, exactly where the data concentrates. The threshold depends on dot size, dot value and resolution, and no source gives it. All three points are definitional.

## Channels

The count sits on density of marks over area. Cleveland & McGill's 1985 *Science* table ranks density with volume and color saturation, below area and above hue. Their 1984 *JASA* table omits it ([william-cleveland.md](../people/william-cleveland.md)). The 1985 paper: "The ordering should be thought of as a tentative working hypothesis ... Aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them." Density is one of those aspects.

[Bertin](../people/jacques-bertin.md) treats dot density as `grain`, ordered but not quantitative, though he allows ratios between coarse grains. `authority-asserted`, since Bertin ran no experiments. The form supports "more here than there", not "twice as much here as there."

## What is measured

No study in this corpus tests the form or isolates its channel, and nothing about it is contested. "Readers can compare these two densities" is `absence of evidence`, unsupported rather than refuted.

## The failure mode it invites

**Random placement presented as location.** It looks like precision, but county counts stay county counts. `authority-asserted`.

**No stated dot value.** Without it, and with no axis, the map cannot be read as a quantity.

**Density read as a rate.** Dense means many, not high per capita, so the map drifts toward a population map. Urban, inventory topic 22: "If the map only shows where people live, it is a population map." Munzner's slides warn they "show population density (correlated with attribute), not effect of interest" ([munzner-vad.md](../sources/munzner-vad.md)). Both `authority-asserted`.

**The pattern left to the reader.** Dots show a concentration without saying what it means.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing.

**Defensible, with the label said out loud:**

- "Dots rather than a choropleth, because the quantity is a count and total ink is proportional to it. That is structural: the visual weight comes from the variable rather than from land area. It is not a claim that readers read the counts well."
- "One dot per 100 households, stated in the subtitle." Convention, and the minimum for a quantity.
- "Dots are placed at the address level, not scattered inside tracts." The line between measured and generated location.
- "The three concentrations are annotated." The FT's instruction. `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A dot map shows where people are."~~ Only if placement came from the data. Otherwise it shows the polygons.
- ~~"Dot density avoids the choropleth's problems."~~ It avoids land-area weighting but not the population map, and adds placement.
- ~~"Readers can judge these densities accurately."~~ Untested. Cleveland & McGill call their ordering partly conjectural, and Bertin calls density non-quantitative.

## See also

- [spatial.md](spatial.md): the group, and rates versus totals
- [choropleth-map.md](choropleth-map.md): the alternative, weighted by land area
- [../people/jacques-bertin.md](../people/jacques-bertin.md): `grain` as ordered but not quantitative
- [../people/william-cleveland.md](../people/william-cleveland.md): the 1985 table, the only one that ranks density
