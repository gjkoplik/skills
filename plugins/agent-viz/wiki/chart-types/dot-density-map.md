---
type: chart-type
relationships: [spatial]
aliases: [Dot density map]
---

# Dot density maps

A map carrying one dot per fixed number of units, each dot placed where those units are, so the count reads as the density of ink over the page.

## When to reach for it, and when not

**The form applies where** the variable is a count of discrete things, the locations of those things within each region are known, and the message is where the concentration falls rather than what any one region's number is.

The FT gloss is the only one of its three spatial glosses that is about annotation rather than about the encoding: a dot density map should "make sure to annotate any patterns the reader should see" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). That gloss is a statement about the form: the figure does not deliver a reading on its own.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| How many, exactly, in this region? | A table, or a sorted bar chart |
| The value is a rate | [Choropleth](choropleth-map.md). Density of dots is a count per area, not a rate per person |
| Region totals with no sub-region locations | [Choropleth](choropleth-map.md), or a proportional symbol map. Scattering dots inside a polygon invents locations the data does not contain |
| The concentrations are urban | The dots merge into solid fill and the encoding saturates. A hex-grid binning, or a rate mapped |
| There are twelve things | Labeled points. Density is not the reading at that count |
| Which region is highest? | Sorted bar chart. Comparing two ink densities by eye is not a judgment this corpus supports |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per unit with a location, or one row per region with a count plus some rule for placing units inside it |
| Transform | Divide the count by a **dot value** (one dot equals n units), then place the dots |
| Geometry | A small uniform dot, identical for every observation |
| Scale | Count to number of dots, linear and exact by construction. The reader reads dots per unit of area |
| Coordinates | A named map projection |
| Guides | The dot value, stated in the legend or subtitle, and annotation naming the pattern |

**The dot value and the placement rule decide what the map says, and neither is visible in the drawing.** Definitional. A dot value set too high erases small concentrations; set too low, everything saturates into a solid field. Placement is the worse of the two: if dots are scattered at random inside an administrative polygon, the map shows a fabricated distribution at every scale finer than that polygon, and nothing on the page marks the boundary between what was measured and what was generated.

**Total ink is proportional to the count**, which is the one structural advantage this form has over a [choropleth](choropleth-map.md). The reader's visual field is weighted by the variable rather than by land area, and that is why the form can carry totals where the choropleth must not. Definitional, and it is the whole offer.

## Channels

**Density of marks over area**, which is a channel almost nobody has measured.

Cleveland & McGill's 1985 *Science* table does include density, grouped with volume and color saturation, below area and above color hue. It is not in the 1984 *JASA* table at all. Both tables are reproduced side by side on [william-cleveland.md](../people/william-cleveland.md), and the 1985 paper says of its own ordering: "The ordering should be thought of as a tentative working hypothesis ... Aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them." Density is one of the aspects with no experiment behind it.

[Bertin](../people/jacques-bertin.md) is the better source here, because dot density is one of his primary variables. `grain`, which covers dot density and coarseness, is **ordered** but not quantitative, though he allows that a ratio between two coarse grains can be judged. `authority-asserted`; there are no experiments in Bertin. Practically: the form supports "more here than there" and does not support "twice as much here as there."

## What it is measurably good at

**Nothing. No study in this corpus tests a dot density map**, and unlike area or angle, the channel it runs on has not been isolated in an experiment either. This is the thinnest evidence position of the three spatial forms.

## What it is measurably bad at

Nothing measured. Two exposures worth naming.

**The channel is untested and the one ranking that includes it says so.** See above. "Readers can compare these two densities" is unsupported rather than refuted.

**Saturation.** Above some density the dots overlap into a solid field and every further unit adds nothing. The encoding stops responding to the data in exactly the places where the data is most concentrated, which is usually where the story is. Definitional; the threshold depends on dot size, dot value and output resolution, and no source here puts a number on it.

## What is contested

**Nothing. There is no record here to disagree with itself.**

## The failure mode it invites

**Random placement presented as location.** The most damaging failure in this form, because it is undetectable from the figure and it looks like precision. Data that is county counts stays county counts however finely the dots are scattered. `authority-asserted`, and the underlying point is definitional: nothing in the drawing distinguishes a measured position from a generated one.

**Not stating the dot value.** Without it the map is unreadable as a quantity, and there is no axis to fall back on.

**Reading density as a rate.** Dense means many, not high per capita. A dot density map of anything counted per person tends toward the population map for the same reason a choropleth of totals does. Urban, inventory topic 22: "If the map only shows where people live, it is a population map." Munzner's slides give dot density maps the same caution in their own terms, "show population density (correlated with attribute), not effect of interest" ([munzner-vad.md](../sources/munzner-vad.md)). Both `authority-asserted`.

**Leaving the pattern to the reader.** This is what the FT gloss is about. A field of dots supports noticing a concentration and does not tell anyone what it means, so the annotation is part of the figure rather than a nicety.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing. No study in this corpus tests this form, and none tests the channel it uses either.

**Defensible, with the label said out loud:**

- "Dots rather than a choropleth, because the quantity is a count and total ink is proportional to it. That is structural: the visual weight comes from the variable rather than from land area. It is not a claim that readers read the counts well."
- "One dot per 100 households, stated in the subtitle." Convention, and the minimum that makes the figure legible as a quantity.
- "Dots are placed at the address level, not scattered inside tracts." The line between measured and generated location.
- "The three concentrations are annotated." The FT's own instruction for this chart. `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A dot map shows where people are."~~ Only if the placement came from the data. Scattered inside polygons, it shows where the polygons are, at a resolution the data never had.
- ~~"Dot density avoids the choropleth's problems."~~ It avoids the land-area weighting, which is the real one. It does not avoid the population map, and it adds a placement problem the choropleth does not have.
- ~~"Readers can judge these densities accurately."~~ Untested. The only ranking that includes density calls its own ordering partly conjectural, and Bertin puts dot density among the ordered but non-quantitative variables.

## See also

- [spatial.md](spatial.md) — the group, and the rates-versus-totals pair this form sits on the totals side of
- [choropleth-map.md](choropleth-map.md) — the alternative, and the land-area weighting this form escapes
- [../people/jacques-bertin.md](../people/jacques-bertin.md) — `grain` as an ordered but not quantitative variable
- [../people/william-cleveland.md](../people/william-cleveland.md) — the 1985 table, which is the only one that ranks density
