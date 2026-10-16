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

Only the guides differ from a [scatterplot](scatterplot.md). Without a direction mark, time is unreadable.

## Channels

Both axes are position along a common scale ([channels.md](../concepts/channels.md)). Segments carry direction, which [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) tie with length and angle: "there is not enough information to separate the ties." Time is on path order, which no ranking includes.

## What is measured

Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series," tests the form directly. It has no study page, and [Robert Kosara's page](../people/robert-kosara.md) records it as `primary-read` without its results. Those reach this corpus only through [Wilke's summary](../sources/wilke-fundamentals.md), not the paper. Wilke reports that readers confused order and direction more often on a connected scatterplot than on line graphs, and reported correlation less often, while the form drew higher engagement. `evidence-backed` at secondhand ([evidence-class.md](../concepts/evidence-class.md)). Effect sizes, stimuli and sample are not recorded here, and whether the comparison line graphs were dual-axis is not stated.

## The failure mode it invites

**No direction marks.** A closed scribble with no beginning. `authority-asserted`.

**Loops read as structure.** A path that returns near an earlier point could be a cycle, a reversal or a coincidence. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing read at primary. The one test of the form is known here through Wilke.

**Defensible, with the label said out loud:**

- "I used a connected scatterplot instead of a dual-axis line chart. That substitution is a stated editorial preference at the Urban Institute, not a measured result, and the case against dual axes has no experiment under it either."
- "Both variables are on positional axes rather than one being on a second y-scale, so the apparent relationship is not a free parameter of how I scaled the second axis. That follows from the construction; that readers *do better* with it is untested."
- "Two line charts rather than a connected scatterplot, because the reader needs the order of events. A study summarized secondhand reports more confusion of order and direction on this form than on line graphs."

**Not defensible:**

- ~~"Connected scatterplots are easier to read than dual-axis charts."~~ No test against dual axes is recorded here, and the one summary on file reports more confusion of order and direction than line graphs, not less.
- ~~"The path shows that x drove y."~~ Time order is in the data. Causation is not.

## See also

- [scatterplot.md](scatterplot.md)
- [correlation.md](correlation.md)
- [../people/robert-kosara.md](../people/robert-kosara.md)
- [../sources/wilke-fundamentals.md](../sources/wilke-fundamentals.md): the secondhand summary of Haroz et al.
