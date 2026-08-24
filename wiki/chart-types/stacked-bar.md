# Stacked bar charts

**What it is.** A bar divided into segments, each segment's length encoding a part's share of the bar's total. The only part-to-whole form that keeps a rank-1 reading, and it keeps it for exactly one segment.

**Status.** Directly tested. Cleveland & McGill's position-length experiment used divided bar charts as its stimuli, so this type is measured rather than inherited.

**What it is good for.** Understanding why the bottom segment is trustworthy and the rest are not.

**What it does not settle.** The grouped-versus-stacked choice, which depends on the reader's question rather than on perception.

**Relationships.** [Part-to-whole](part-to-whole.md), Change over Time, Magnitude. An unlinked relationship means that index is not written yet.

---

## When to reach for it, and when not

**Reach for it when** the total matters as well as the composition, or when composition repeats across categories or across time. It is the only part-to-whole form that keeps a rank-1 reading, and it keeps it for the total and the bottom segment.

**Order the segments deliberately.** Whichever series the reader most needs to compare goes on the baseline. That single decision moves it from rank 3 to rank 1 and costs nothing.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| How does one middle series move across categories? | Small multiples, or a line chart of that series. Middle segments float with no shared baseline |
| Only composition matters, and there is one whole | [Pie or donut](pie-and-donut.md). Simpler, and nothing is lost |
| There are many parts per bar | [Treemap](treemap.md), or aggregate the tail into "other" |
| Precise values per segment | Any chart with an axis per value. This is the form's measured weakness |

**Normalizing to 100%** removes the total, which is the rank-1 reading you came for. Sometimes right, always a real loss, and worth making knowingly.

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (category, part) with a magnitude |
| Transform | Cumulative sum within category to get segment boundaries. Optionally normalize to 100% |
| Geometry | Rectangle |
| Scale | Magnitude to length |
| Coordinates | Cartesian |
| Guides | One quantitative axis, category axis, legend |

A **grouped** bar chart differs in the transform slot alone: no cumulative sum, and the position slot changes with it. That one-slot difference is the whole of the grouped-versus-stacked question, which is why the decomposition is worth keeping.

A **coxcomb** is this chart with the coordinates slot set to polar. A **100% stacked bar** is this chart with a normalization added to the transform.

## Channels

Segment length, on a scale with **no common baseline except for the first segment**.

The first segment starts at the axis, so it is read as position along a common scale: rank 1. Every subsequent segment floats, so it is read as length: rank 3. Cleveland & McGill spell this out for the divided bar chart:

> "For each of the three, the totals of A and B can be compared by perceiving position along the scale. ... All other values must be compared by the elementary task of perceiving different bar lengths"

**So a stacked bar is two charts stuck together.** The totals and the bottom segment are read accurately. Everything above the bottom is read on a demonstrably worse channel.

## What it is measurably good at

**Totals.** The overall bar height is position along a common scale. Rank 1, evidence-backed.

**The bottom segment.** Same reading, same rank.

## What it is measurably bad at

**Every segment that is not on the baseline.** [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured exactly this substitution:

> "the average errors for length judgments are 40%-250% larger than those for position judgments"

The five judgment types in that experiment were built from grouped and divided bar charts precisely to isolate this. Types 1-3 are position readings, types 4-5 are the floating-segment length readings. Replicated by [Heer & Bostock (2010)](../studies/heer-bostock-2010.md), who found types 4 and 5 somewhat more accurate than the original but with position still significantly ahead.

This is the most directly measured claim about any chart type in this wiki. It is not inherited and it is not a conjecture.

## What is contested

Very little, which is unusual here. The perceptual account of stacked bars is about as settled as visualization gets.

What is *unmeasured* is the comparison people actually care about: whether a stacked bar beats a grouped bar or a set of small multiples for a given question. No study in this source set tests it.

## The failure mode it invites

**Tracking a middle series across categories.** The reader's eye wants to compare the orange segment across five bars. Each of those segments floats at a different offset, so the comparison is a set of length judgments with no shared baseline, which is the worst case this form supports. `authority-asserted`, and it follows directly from the measured channel split rather than resting on taste.

**The remedy is ordering.** Put the series you want compared on the baseline. It costs nothing and moves that series from rank 3 to rank 1. This follows from the evidence rather than being separately tested.

**100% stacking hides the totals.** Normalizing removes the one rank-1 reading the form had for magnitude and keeps only composition. That is sometimes exactly right, and it is a real loss to make knowingly.

## Justifying the choice

**Defensible, evidence-backed:**

- "I put the series in question on the baseline. Floating segments are read as length, which carries 40% to 250% more error than position, measured on exactly this chart form."
- "The total is a rank-1 reading here, which is why this is a stacked bar rather than a pie: the reader needs the total and its composition."
- "I did not normalize to 100%, because that removes the only accurately-read quantity on the chart."

**Defensible, with the label said out loud:**

- "Three or four segments is about the practical limit before the middle becomes unreadable. Convention, not a measured threshold."

**Not defensible:**

- ~~"Readers can compare the orange segments across these bars."~~ They cannot do it well, and that is this form's one well-measured weakness rather than a matter of taste.

## See also

- [../studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) — the divided-bar stimuli and the 40-250% figure
- [pie-and-donut.md](pie-and-donut.md) — the same job in polar coordinates
- [../concepts/channels.md](../concepts/channels.md)
