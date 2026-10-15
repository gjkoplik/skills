---
type: chart-type
relationships: [correlation, change-over-time]
aliases: [Connected scatterplot]
---

# Connected scatterplot

Two variables measured on the same units over time, drawn as points in the x-y plane and joined in time order.

## When to reach for it, and when not

The form is defined for two quantities tracked together over time, where the joint path is the message. The [Urban Institute guide](../sources/urban-institute.md) states an editorial preference, not a rule: connected scatterplots are "a clearer substitute for dual-axis line charts, which Urban does not publish." `authority-asserted`. The case against dual axes is itself `absence of evidence` ([refutations.md](../refutations.md#a-flat-ban-on-dual-axes)).

| The question | Alternative |
|---|---|
| When did this happen, or how fast? | A line chart per variable. Time is only in the path order |
| How did one variable move? | A line chart |
| Is there a relationship across many units? | A [scatterplot](scatterplot.md). This form traces one unit |
| The observations are not ordered | A [scatterplot](scatterplot.md). The line would assert a false order |
| Many time points, or a self-crossing path | Two stacked panels sharing an x-axis |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per time point, two values for one unit |
| Transform | None. Time order is a sort |
| Geometry | Points, joined by a path in time order |
| Scale | Each variable to a spatial axis. Time to nothing spatial |
| Coordinates | Cartesian |
| Guides | Two axes, plus arrows or labeled time points for direction |

Only the guides differ from a [scatterplot](scatterplot.md). Without a direction mark, time is unreadable, which is `definitional`.

## Channels

Both axes are position along a common scale ([channels.md](../concepts/channels.md)). Segments carry direction, which [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) tie with length and angle: "there is not enough information to separate the ties." Time is on path order, which no ranking includes.

## What it is measurably good at

Nothing measured here. Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series," tests the form but is only recorded as `primary-read` on [Robert Kosara's page](../people/robert-kosara.md).

## What it is measurably bad at

Nothing measured.

## What is contested

Nothing contested. The record is `absence of evidence` ([evidence-class.md](../concepts/evidence-class.md)).

## The failure mode it invites

**No direction marks.** A closed scribble with no beginning. `authority-asserted`.

**Loops read as structure.** A path that returns near an earlier point could be a cycle, a reversal or a coincidence.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. No study here bears on this form.

**Defensible, with the label said out loud:**

- "I used a connected scatterplot instead of a dual-axis line chart. That substitution is a stated editorial preference at the Urban Institute, not a measured result, and the case against dual axes has no experiment under it either."
- "Both variables are on positional axes rather than one being on a second y-scale, so the apparent relationship is not a free parameter of how I scaled the second axis. That follows from the construction; that readers *do better* with it is untested."

**Not defensible:**

- ~~"Connected scatterplots are easier to read than dual-axis charts."~~ Untested, so neither contested nor refuted.
- ~~"The path shows that x drove y."~~ Time order is in the data. Causation is not.

## See also

- [scatterplot.md](scatterplot.md)
- [correlation.md](correlation.md)
- [../people/robert-kosara.md](../people/robert-kosara.md)
