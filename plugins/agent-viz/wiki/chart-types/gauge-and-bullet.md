---
type: chart-type
relationships: [magnitude]
aliases: [Bullet chart, Bullet graph, Dial, Gauge, Radial gauge, Speedometer chart]
---

# Gauges and bullet graphs

Two forms for the same job, one value against a band of context, drawn in two different geometries: a **gauge** puts the value on an angular position inside an arc, and a **bullet graph** puts it on the length of a bar against a reference marker.

The gauge is also called a **dial**, a **speedometer chart** or a **radial gauge**. The bullet is called a **bullet graph** (its designer's term) or a **bullet chart**.

[Schwabish](../sources/schwabish.md) files them together, as a single "Gauge and Bullet" entry under **Comparing Categories**, and that filing is verified from the book's own contents pages. What he argues about either one is not vouched here, because the book's prose is unopened. **This page keeps them apart, because they are not the same argument.** One spends a whole figure on a single number in the least convenient geometry available; the other is a bar with context added, designed as the replacement.

## When to reach for it, and when not

**Reach for a bullet graph when** one measure has to be shown against a target and a small number of qualitative ranges, in a small footprint, usually stacked with several others down a page. That is the case it was designed for and the case it still serves.

**Before reaching for a gauge, take the escape hatch.** A gauge delivers one value, and [part-to-whole.md](part-to-whole.md) opens with the route out of exactly that situation, quoting the Urban Institute style guide ([urban-institute.md](../sources/urban-institute.md)):

> "You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

A single large number, set large, with one line of context under it, frequently beats a chart drawn to deliver one value. That is the honest recommendation for most gauges and it is `authority-asserted`; no experiment in this corpus compares a big number against a gauge, or against anything else. [magnitude.md](magnitude.md) states the same escape hatch for the group.

**Do not reach for either when:**

| The question | Use instead |
|---|---|
| How do these several items compare? | [Bar chart](bar-chart.md). One value per gauge means one gauge per value |
| How did it get here? | Change over time. A [line chart](line-chart.md) shows the path a dial cannot |
| There is one number and no reference to hold it against | Write the number. There is no chart to make |
| Which items are over target, and by how much? | [Deviation](deviation.md). A [diverging bar](diverging-bar-chart.md) off the target puts the gap on position |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). Neither form asserts a total |
| What is the spread behind this number? | [Distribution](distribution.md). Both forms show a summary and nothing behind it |

## Structural decomposition

The slots diverge, so they are laid out side by side. Definitional, and nothing here asserts anything empirical.

| Slot | Gauge | Bullet graph |
|---|---|---|
| Data | One row, one measure | One row: a featured measure, one or two comparative measures, and the range breaks |
| Transform | None | None on the value. The range breaks are chosen, not computed |
| Geometry | A needle, or a filled arc segment, inside a fixed arc, usually over colored zones | A bar, a perpendicular marker for the comparative measure, and background bands behind both |
| Scale | Value to angular position along the arc | Value to length along a linear quantitative scale |
| Coordinates | Polar, restricted to a sector | Cartesian, one quantitative axis |
| Guides | The arc's tick labels, and the zone boundaries | A label, one linear quantitative scale, and the band breaks |

**The channel is the whole of the difference, and it is definitional.** The gauge spends angular position on the value; the bullet keeps the value on position and length along a common scale. Everything else about the two forms is decoration on that one substitution.

The bullet graph's five components come from its design specification, which is `primary-read` in this wiki through [people/stephen-few.md](../people/stephen-few.md): a label, one linear quantitative scale, a featured measure, one or two comparative measures, and two to five qualitative ranges.

## Channels

**The bullet graph puts the value on position along a common scale**, the same channel a [bar chart](bar-chart.md) uses, read at the bar's end, with the comparative measure's marker sitting on the same scale so the comparison is a position comparison too. Inherited from [channels.md](../concepts/channels.md) with the standard caveat that the step from mark to channel is conjecture in the source literature.

**The gauge puts the value on angular position inside an arc**, and the Cleveland & McGill list has no entry for exactly that. The nearest tasks in the 1984 table are positions along nonaligned scales and angle, both of which sit below position along a common scale, and choosing between the two for this form is a guess. Nobody has decomposed a gauge the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed the pie ([channels.md](../concepts/channels.md)).

**Both forms use color for categories rather than for magnitude.** The gauge's zones and the bullet's bands say which qualitative range a value falls in, which is identity work, and that is what hue and ordered lightness steps are actually good at. Neither table in [channels.md](../concepts/channels.md) scores that use, and it is not the low-accuracy case.

So: **position and length on one side, angle on the other, which is definitional and is the reason to prefer the bullet.** Whether readers actually do better on a bullet graph than on a gauge is **unmeasured in this corpus**. Both halves of that are true and neither implies the other.

## What it is measurably good at

**Nothing. No study in this corpus uses either form as a stimulus**, tests one against the other, or tests either against a bar chart or a printed number. `absence of evidence`.

## What it is measurably bad at

**Also nothing measured.** Two exposures are worth naming with their status attached.

**Value extraction on the gauge is not on the best channel available**, which is inherited from [channels.md](../concepts/channels.md) and not a finding about gauges. Position along a common scale is read more accurately than angle in proportional-judgment tasks, measured and replicated; that the gauge puts a reader on angle is the conjectural step, and nobody has run the comparison on these two forms.

**A gauge spends an entire figure on one number.** That is arithmetic about layout rather than a claim about perception: whatever the reader does with it, one dial holds one value, so a page of eight measures is eight dials. The bullet graph's small footprint is the entire design case for it, and it is argued rather than tested. The specification's own sentence, quoted from [people/stephen-few.md](../people/stephen-few.md), which read the spec at primary: "Its linear design not only gives it a small footprint, but also supports more efficient reading than radial meters". **The specification cites no test**, which is the correct thing to say about most good designs.

## What is contested

**Nothing, and that is not a compliment.** Contested requires a record that disagrees with itself ([evidence-class.md](../concepts/evidence-class.md)), and here there is no record. [Stephen Few](../people/stephen-few.md) spent years attacking dashboard gauges and then designed the replacement, and nobody in this corpus argues back, so what exists is one designer's position rather than a disagreement. The familiar criticisms of the gauge, that the needle is imprecise, that the zones are arbitrary, that the footprint is indefensible, are plausible and none of them is supported by an experiment in this source set. `absence of evidence`, which is not the same as refuted and not the same as endorsed.

## The failure mode it invites

**Drawing a chart to deliver one number.** The gauge's defining property is that it is a whole figure for a single value, so it invites the failure the [magnitude](magnitude.md) index opens with. The check is one sentence: if the caption you would write is "utilization is at 71%", write that instead. `authority-asserted`.

**Zone breaks nobody chose.** The colored bands assert that some values are good and some are bad, and a default set of thresholds asserts it on your behalf. Same obligation the diverging midpoint carries in [inventory.md](../inventory.md) topic 32: a threshold in the drawing is a claim, so it gets set deliberately and gets a label. Stated in this wiki's own voice as a practitioner default, not as a measured result.

**Dropping the scale.** A dial with colored zones and no tick labels, or a bullet bar with no quantitative axis, is a picture with no quantities in it. The bullet specification lists one linear quantitative scale among its five components for that reason.

**Too many bands.** The specification's range is two to five. Past that the background competes with the bar it is supposed to sit behind, which is a design judgment and is `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. There is no experiment in this corpus involving either form, in either direction.

**Defensible, with the label said out loud:**

- "A bullet graph rather than a gauge, because the value stays on position and length instead of moving to angle, and it fits in a row. The channel difference is definitional; the reading advantage is asserted in the design specification and was never tested."
- "The number is set large with a line of context, and there is no gauge. That is a style-guide recommendation with no experiment behind it, and the alternative was a figure delivering one value."
- "Three qualitative bands, with the breaks stated in the caption, because the thresholds are the policy and not the data."

**Commonly repeated, and the evidence does not support it:**

- ~~"Gauges are known to be hard to read."~~ Not by anything here. It may well be true; nobody in this source set checked.
- ~~"Bullet graphs are more accurate than gauges."~~ The channel substitution is definitional and secure. The accuracy conclusion needs an experiment on these two forms, and there is not one.
- ~~"Research shows the bullet graph is more efficient."~~ There is no research. There is a design specification that says so, by the person who designed it, and [people/stephen-few.md](../people/stephen-few.md) records that nothing in his corpus can support a "research shows" preamble.
- ~~"Use a bar chart instead; it is more accurate."~~ A bullet graph already is a bar chart with a reference marker and bands. Against a gauge, the accuracy argument is an inheritance from the channel literature and not a measurement of either form.

## See also

- [magnitude.md](magnitude.md) — the group, and the big-number escape hatch stated once
- [bar-chart.md](bar-chart.md) — the form the bullet graph is a variant of, and the evidence it inherits
- [../people/stephen-few.md](../people/stephen-few.md) — the designer, the specification, and what his authority does and does not cover
- [../concepts/channels.md](../concepts/channels.md) — position against angle, and why the mapping step stays a conjecture
- [../concepts/evidence-class.md](../concepts/evidence-class.md) — absence of evidence, kept distinct from contested and from refuted
