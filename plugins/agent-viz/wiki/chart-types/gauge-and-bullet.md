---
type: chart-type
relationships: [magnitude]
aliases: [Bullet chart, Bullet graph, Dial, Gauge, Radial gauge, Speedometer chart]
---

# Gauges and bullet graphs

One value against a band of context, in two geometries: a **gauge** (dial, speedometer chart, radial gauge) puts it on angular position inside an arc, and a **bullet graph** or bullet chart puts it on the length of a bar against a reference marker.

[Schwabish](../sources/schwabish.md) files them as one "Gauge and Bullet" entry under Comparing Categories, verified from the contents pages; his prose is unopened. The bullet graph was designed to replace the gauge.

## When to reach for it, and when not

The bullet graph is defined for one measure against a target and a few qualitative ranges, in a small footprint, often stacked down a page. A gauge delivers one value, and [part-to-whole.md](part-to-whole.md) opens with the alternative, from the Urban Institute style guide ([urban-institute.md](../sources/urban-institute.md)):

> "You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

That is `authority-asserted`, with no experiment in this corpus comparing a big number against anything. [magnitude.md](magnitude.md) states it for the group.

| The question | Alternative |
|---|---|
| How do these several items compare? | [Bar chart](bar-chart.md). One value per gauge means one gauge per value |
| How did it get here? | A [line chart](line-chart.md) shows the path a dial cannot |
| One number, no reference to hold it against | A printed number |
| Which items are over target, and by how much? | [Deviation](deviation.md). A [diverging bar](diverging-bar-chart.md) off the target puts the gap on position |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). Neither form asserts a total |
| What is the spread behind this number? | [Distribution](distribution.md). Both forms show only a summary |

## Structural decomposition

| Slot | Gauge | Bullet graph |
|---|---|---|
| Data | One row, one measure | One row: a featured measure, one or two comparative measures, and the range breaks |
| Transform | None | None on the value. The range breaks are chosen, not computed |
| Geometry | A needle, or a filled arc segment, inside a fixed arc, usually over colored zones | A bar, a perpendicular marker for the comparative measure, and background bands behind both |
| Scale | Value to angular position along the arc | Value to length along a linear quantitative scale |
| Coordinates | Polar, restricted to a sector | Cartesian, one quantitative axis |
| Guides | The arc's tick labels, and the zone boundaries | A label, one linear quantitative scale, and the band breaks |

The difference is the channel, and it is definitional: angular position for the gauge, position and length along a common scale for the bullet. The bullet's five components (a label, one linear quantitative scale, a featured measure, one or two comparative measures, two to five qualitative ranges) come from its design specification, `primary-read` through [people/stephen-few.md](../people/stephen-few.md). A gauge spends a figure on one number, so eight measures take eight dials. The bullet's small footprint is its design case.

## Channels

The bullet graph reads like a [bar chart](bar-chart.md), position along a common scale, with the comparative marker on the same scale. The step from mark to channel is conjecture ([channels.md](../concepts/channels.md)). The specification says "Its linear design not only gives it a small footprint, but also supports more efficient reading than radial meters" ([people/stephen-few.md](../people/stephen-few.md)), and cites no test. `authority-asserted`.

The gauge's angle-in-an-arc has no entry in the Cleveland & McGill list. Its nearest tasks in the 1984 table are position along nonaligned scales and angle, and which applies is a guess. Both rank below position along a common scale in proportional-judgment tasks, `evidence-backed` and replicated. Nobody has decomposed a gauge the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed the pie.

[Stephen Few](../people/stephen-few.md) spent years attacking dashboard gauges, then designed the replacement, and nobody here argues back. No experiment in this source set supports the familiar criticisms (an imprecise needle, arbitrary zones, a wasteful footprint). `absence of evidence`.

Zones and bands use color for which qualitative range a value falls in, identity work that hue and lightness steps do well and no accuracy table scores.

## What is measured

No study in this corpus tests the form. None uses either geometry as a stimulus, tests one against the other, or tests either against a bar chart or a printed number. `absence of evidence`. The gauge's angle penalty is inherited from channel studies, not observed on gauges.

## The failure mode it invites

**A chart drawn to deliver one number**, the failure the [magnitude](magnitude.md) index opens with. Where the caption reads "utilization is at 71%", the dial adds nothing. `authority-asserted`.

**Zone breaks nobody chose.** Default thresholds assert that some values are good and some bad. A threshold in the drawing is a claim, like the diverging midpoint in [inventory.md](../inventory.md) topic 32, by practitioner default rather than measurement.

**No scale.** A dial with no tick labels, or a bullet with no axis, carries no quantities.

**Too many bands.** Past the specification's two to five, the background competes with the bar. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. No experiment in this corpus involves either form.

**Defensible, with the label said out loud:**

- "A bullet graph rather than a gauge, because the value stays on position and length instead of moving to angle, and it fits in a row. The channel difference is definitional; the reading advantage is asserted in the design specification and was never tested."
- "The number is set large with a line of context, and there is no gauge. That is a style-guide recommendation with no experiment behind it, and the alternative was a figure delivering one value."
- "Three qualitative bands, with the breaks stated in the caption, because the thresholds are the policy and not the data."

**Commonly repeated, and the evidence does not support it:**

- ~~"Gauges are known to be hard to read."~~ Not by anything here. Nobody in this source set checked.
- ~~"Bullet graphs are more accurate than gauges."~~ The channel substitution is definitional. The accuracy claim needs an experiment on these two forms, and there is none.
- ~~"Research shows the bullet graph is more efficient."~~ There is a specification saying so, by its designer, and [people/stephen-few.md](../people/stephen-few.md) records that nothing in his corpus supports a "research shows" preamble.
- ~~"Use a bar chart instead; it is more accurate."~~ A bullet graph already is one, with a marker and bands. Against a gauge, the argument is inherited, not measured.

## See also

- [magnitude.md](magnitude.md): the group, and the big-number alternative
- [bar-chart.md](bar-chart.md): the form the bullet graph varies, and its evidence
- [../people/stephen-few.md](../people/stephen-few.md): the designer, the specification, and the limits of his authority
- [../concepts/channels.md](../concepts/channels.md): position against angle
- [../concepts/evidence-class.md](../concepts/evidence-class.md): absence of evidence, distinct from contested and refuted
