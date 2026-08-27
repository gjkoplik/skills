---
type: chart-type
relationships: [correlation, change-over-time]
aliases: [Connected scatterplot]
---

# Connected scatterplot

Two variables measured on the same units over time, drawn as points in the x-y plane and joined in time order.

## When to reach for it, and when not

**Reach for it when** two quantities move over time on the same units, the joint trajectory is the message, and the alternative on the table is a dual-axis line chart. The [Urban Institute guide](../sources/urban-institute.md) states the substitution as an editorial fact rather than a rule, which is the honest form: connected scatterplots are "a clearer substitute for dual-axis line charts, which Urban does not publish." `authority-asserted`. Note what it is a substitute *for*: the case against dual axes is itself `absence of evidence`, so this is one unmeasured preference standing in for another ([refutations.md](../refutations.md#a-flat-ban-on-dual-axes)).

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| When did this happen, or how fast? | A line chart per variable. Time is not on an axis here, it is only in the order of the path |
| How did one variable move? | A line chart. Reading one variable alone means projecting the path onto an axis |
| Is there a relationship across many units? | A plain [scatterplot](scatterplot.md). This form is one unit traced through time, not a population |
| The observations are not ordered | A plain [scatterplot](scatterplot.md). The line is the ordering, and drawing it without one asserts something false |
| There are many time points, or the path crosses itself repeatedly | Two stacked panels sharing an x-axis. The tangle is not a finding |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per time point, carrying two quantitative values for the same unit |
| Transform | None. The ordering by time is a sort, not a statistic |
| Geometry | Point per observation, plus a path connecting consecutive observations in time order |
| Scale | Each variable maps to one spatial axis. Time maps to nothing spatial |
| Coordinates | Cartesian |
| Guides | Two axes, plus whatever marks the direction and endpoints of the path: arrows, labeled start and end, or labeled time points |

The guides row is the whole difference from a [scatterplot](scatterplot.md). Time is carried entirely by the order of the path, so if nothing marks direction, one of the chart's three variables is unreadable. That is `definitional`, not a claim about readers.

## Channels

Both axes are position along a common scale, inherited from [channels.md](../concepts/channels.md) rather than restated. Path segments put the reader on **direction**, which [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) place at the **same rank as length and angle**, with the authors' own note that "there is not enough information to separate the ties."

**Time is on path order, which appears in neither ranking.** Nobody has scored it, so nothing about it can be inherited from anywhere.

## What it is measurably good at

**Nothing has been measured in this wiki.**

One directly relevant study exists and is in this corpus's reading list without a page: Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series," recorded as `primary-read` on [Robert Kosara's page](../people/robert-kosara.md) with no findings written up here. Until it is, this page has nothing to inherit and should not pretend otherwise. That is a gap with a name and a PDF behind it.

## What it is measurably bad at

Nothing measured, for the same reason and from the same missing page.

## What is contested

**Nothing.** Contested requires a record that disagrees with itself, and here there is no record. `absence of evidence`, which [evidence-class.md](../concepts/evidence-class.md) keeps distinct from contested and from refuted.

## The failure mode it invites

**Shipping it without direction marks**, which leaves the reader a closed scribble with no beginning. `authority-asserted`.

**Reading loops as structure.** A path that returns near an earlier point means the two variables returned to earlier values; whether that is a cycle, a reversal or a coincidence is not in the picture. Same shape as reading clusters off a force-directed layout: the geometry is a consequence of the encoding, not a finding.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. No study here bears on this form, and the honest version of this bucket is empty.

**Defensible, with the label said out loud:**

- "I used a connected scatterplot instead of a dual-axis line chart. That substitution is a stated editorial preference at more than one publisher, not a measured result, and the case against dual axes has no experiment under it either."
- "Both variables are on positional axes rather than one being on a second y-scale, so the apparent relationship is not a free parameter of how I scaled the second axis. That follows from the construction; that readers *do better* with it is untested."

**Not defensible:**

- ~~"Connected scatterplots are easier to read than dual-axis charts."~~ Untested here. Not contested, not refuted: nobody in this source set has measured it.
- ~~"The path shows that x drove y."~~ Ordering in time is in the data; the causal claim is not, and no chart supplies it.

## See also

- [scatterplot.md](scatterplot.md) — the same marks without the path
- [correlation.md](correlation.md) — the group argument
- [../people/robert-kosara.md](../people/robert-kosara.md) — where the unwritten study on this form is recorded
