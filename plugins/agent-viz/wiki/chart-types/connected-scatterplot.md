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

Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series" (*TVCG*), tests the form directly against the dual-axis line chart, in four studies. Read at primary, with the PDF from `media.eagereyes.org` extracted locally; it has no study page, and its authors are on [robert-kosara.md](../people/robert-kosara.md) and [steven-franconeri.md](../people/steven-franconeri.md).

- **Understanding.** Fourteen college students read two news datasets in both forms, in a lab, on paper. Objective understanding was high on both. The three qualitative errors were all on the connected scatterplot, and the authors attribute two of them to habits from the line chart: reading opposite trends as a mirror flip, and reading a low y-value as both values low. When asked to predict the next segment from a statement such as "Y1 increases, and Y2 is constant," scores were 6.5 of 7 on the line chart and 6.1 of 7 on the connected scatterplot. Correlational language appeared 28 times in descriptions of the line charts and 3 times for the connected scatterplots, a post-hoc count the authors say "warrants further evaluation."
- **Direction.** Thirty-five Mechanical Turk workers translated five-point datasets between the two forms, with 8 excluded for chance-level copying. Performance was 92% overall. Time was reversed on 13% of translation trials in each direction and on 5% of trials that only copied a connected scatterplot to a connected scatterplot; the horizontal axis was flipped on 1.6% of translations into a line chart, and the vertical axis never.
- **Engagement.** Shown six thumbnails, three of each form, readers "chose to look at it first more often than at standard line charts." The authors cannot say whether that is the form or its novelty.

`evidence-backed`, on small samples and five-point stimuli. The paper's own guideline: "If a major purpose of a graph is to leave the viewer with an understanding of negative or positive correlation in a dataset, a more traditional DALC may make this conclusion far more salient." Nothing here measures accuracy of a value read off either form, or the dual-axis chart's own failure mode, the free scaling of its second axis.

## The failure mode it invites

**No direction marks.** A closed scribble with no beginning. `authority-asserted`.

**Loops read as structure.** A path that returns near an earlier point could be a cycle, a reversal or a coincidence. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- "Readers understand it with little explanation. College students scored 6.1 of 7 predicting the next segment against 6.5 of 7 on a dual-axis line chart, and crowdsourced workers translated between the two forms correctly 92% of the time."
- "Direction is marked. In the one study, readers reversed time on 13% of translations between the two forms and on 5% of plain copies of a connected scatterplot."

**Defensible, with the label said out loud:**

- "I used a connected scatterplot instead of a dual-axis line chart. That substitution is a stated editorial preference at the Urban Institute, not a measured result, and the case against dual axes has no experiment under it either."
- "Both variables are on positional axes rather than one being on a second y-scale, so the apparent relationship is not a free parameter of how I scaled the second axis. That follows from the construction; that readers *do better* with it is untested."
- "Two line charts rather than a connected scatterplot, because the correlation is the message. Readers described the dual-axis version in correlational terms 28 times and the connected scatterplot 3 times, and the authors say the line chart may make that conclusion far more salient." A post-hoc count on 14 students.

**Not defensible:**

- ~~"Connected scatterplots are easier to read than dual-axis charts."~~ The one test found understanding high on both and the errors on the connected scatterplot: all three qualitative errors, and time reversed on 13% of translations. What it measured in the form's favor is that readers chose to look at it first.
- ~~"The path shows that x drove y."~~ Time order is in the data. Causation is not.

## See also

- [scatterplot.md](scatterplot.md)
- [correlation.md](correlation.md)
- [../people/robert-kosara.md](../people/robert-kosara.md) and [../people/steven-franconeri.md](../people/steven-franconeri.md): two of the paper's authors, with the PDF location
- [../sources/wilke-fundamentals.md](../sources/wilke-fundamentals.md): Wilke's summary of the same paper
