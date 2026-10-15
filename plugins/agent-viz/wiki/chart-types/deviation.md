---
type: index
---

# Deviation

Signed distance from a reference point: how far each item sits above or below the thing it is measured against, and on which side of it.

## Is deviation the right frame, and how to tell

The FT defines the family ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Emphasise variations (+/-) from a fixed reference point. Typically the reference point is zero but it can also be a target or a long-term average. Can also be used to show sentiment (positive/neutral/negative)."

The reference point is a free parameter of the chart, and nothing on the chart shows the reader that it was picked. That is the argument for treating this as a group.

Schwabish's *Better Data Visualizations* has no such category. It files Diverging Bar in chapter 4, Comparing Categories, and [schwabish.md](../sources/schwabish.md) records that "Deviation and Flow have no home in his scheme." The memberships are from the contents pages, and the prose is unread. So two practitioner taxonomies descended from the same 2014 poster disagree about where a diverging bar belongs, `authority-asserted` on both sides. The group is a retrieval aid, not a fact about the chart.

Three tests.

**Is there a reference the reader already accepts?** Zero, a budget, a published target, a long-run average, the national rate, last year. If the caption has to argue for the reference, the reference carries the claim. That can be the job, as a decision rather than a library default.

**Does the reader need the difference, or the level?** Plotting a deviation discards the base. Two items at +4 might be 104 and 4004, and the chart cannot tell them apart. Where the level matters too, the form is a magnitude chart with a reference line, or both charts.

**Does the sign mean something?** If above and below are not different in kind, or everything lands on one side, the drawing is a [bar chart](bar-chart.md) with an extra line. That works, and it is not this group.

| The reader's question | Group |
|---|---|
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md) |
| Which is biggest, and in what order? | Ranking. A sorted bar chart |
| How did this move over time? | [Change over time](change-over-time.md). A line chart, with the reference drawn as a rule |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| How spread out are the values? | [Distribution](distribution.md) |
| Do these two variables move together? | [Correlation](correlation.md) |
| Which items are above the line, which below, and by how much? | **This group** |

## The reference point is a rhetorical choice the reader cannot see

A deviation chart draws `value - reference`. Change the reference and every bar changes length, some change side, and no number in the data has moved. Zero, the target and the long-run average give three charts of one dataset that can disagree about who is failing, and the picture does not show which was chosen. This is definitional, the same problem as the aspect ratio and axis window in [change-over-time.md](change-over-time.md).

Whether moving the reference moves a reader's conclusion is untested in this corpus. `absence of evidence`.

The nearest measured manipulation, axis truncation, is a different one. [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) moved a bar chart's baseline off zero with the axis in raw units. Mean response on a "how much bigger" scale went from 1.45 to 2.77, up 91.0%, with the true values printed on the chart. [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) found the same direction, F(2, 76) = 89, p < 0.0001, and the mark type did not rescue it.

Truncation moves the origin under an unchanged quantity, so the ink stops being proportional to the plotted number. A deviation chart redefines the quantity as the difference, and the ink is proportional to that. Urban names this move as a remedy for truncation: "consider adjusting the data to show percent change, difference, or some other similar adjustment" ([urban-institute.md](../sources/urban-institute.md)). The axis label discloses the subtraction but not the choice of reference, and what that freedom does to readers is untested.

## What else this group costs

Every bar starts at one shared reference line, so a bar's end reads as position along a common scale, as on a plain bar chart, for items on the same side ([channels.md](../concepts/channels.md)). The step from chart to channel is conjecture in the source literature, as for every type.

Comparing a bar running left with one running right means comparing two lengths in opposite directions from a common origin, which nobody in this corpus has measured. `absence of evidence`, and it is the judgment a diverging bar most often invites.

The sign is a categorical read, which the Cleveland & McGill orderings do not score ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). It is usually doubled in hue, which is [inventory](../inventory.md) topic 69 (redundant coding) and puts hue on identity, the job it does well.

Stacking gives the accuracy away. Once segments accumulate outward from the center, everything past the innermost segment floats, and floating segments carry 40% to 250% more error than position readings, measured on divided bars ([stacked-bar.md](stacked-bar.md)). It is the one measured number this group reaches.

## Choosing a form

| Form | What carries the value | Where it applies |
|---|---|---|
| [Diverging bar chart](diverging-bar-chart.md) | Bar length from a shared reference line, side carrying the sign | One signed number per category, and above/below is the point |
| [Spine chart](spine-chart.md) | Two component lengths growing outward from a shared center | Each row splits one total into two contrasting parts |
| Diverging stacked bar | Segment lengths accumulating outward from a center | Ordered response categories per row, usually Likert data. Covered on [diverging-bar-chart.md](diverging-bar-chart.md), since it is that chart with a cumulative sum added |
| Surplus / deficit filled line *(no page here)* | Filled area between a series and a reference line, shaded by side | The deviation runs over time and the periods of surplus and shortfall are read as shapes |

A bullet chart puts one value against a target and a qualitative range, and a population pyramid is a [spine chart](spine-chart.md) whose rows are age bands. Neither has a page, because no study in this corpus tests either.

Two constraints follow from the structure:

- **The reference line carries its value and its identity.** "0" is not a label. "2019 average, 4.1%" is. [inventory](../inventory.md) topic 32 states the same rule for the midpoint of a diverging color scale, which "must be set to a meaningful value and labeled" (`authority-asserted`, from Urban). The geometric version is the same problem and mostly goes unstated.
- **The sort is by the deviation, not the raw value.** Sorting on the base answers a question the chart is not about.

## Justifying the choice

**Defensible, evidence-backed:**

- "Bars run from the reference line, so their ends read as position along a common scale for every item on the same side of it." This inherits the best-measured comparison in the literature ([channels.md](../concepts/channels.md)).
- "I plotted the difference instead of truncating the axis under a bar. Truncating a bar axis moved readers' size judgments 91% in a controlled test, and this transform keeps the ink proportional to the quantity actually drawn."

Nothing else here is native to the group. No study here tests any chart in it.

**Defensible, with the label said out loud:**

- "The reference is the five-year average rather than zero, and the subtitle says so." That the reader cannot otherwise recover the choice is structural. That stating it helps is unmeasured practitioner convention.
- "Above and below are colored differently as well as pointed differently, so the sign does not rest on one channel." Redundant coding, inventory topic 69, `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A diverging bar makes the gap between any two items easy to compare."~~ The side is there by construction. Comparing across the line is the unmeasured opposite-direction judgment above.
- ~~"The reference line and the color midpoint are the same decision."~~ A color scale pivoting away from the reference line puts two midpoints on one chart, and both need setting and labeling (inventory topic 32).

## The failure mode this group invites

**Picking the reference that produces the picture.** Every candidate reference is arguable, each is honest on its own, and the chart shows none of the alternatives. A figure here can be arithmetically perfect, correctly labeled, and still an argument won before the reader arrived. The check, also recorded in [change-over-time.md](change-over-time.md), states the conclusion and redraws against zero and against the long-run average. A sentence that stops being true was about the reference.

**Reading a deviation as a level.** A reader who takes "+9" for "a lot" cannot know whether the base was 12 or 12,000, and the form gives no cue that the question exists.

## Types in this index

- [diverging-bar-chart.md](diverging-bar-chart.md): also covers the diverging stacked bar
- [spine-chart.md](spine-chart.md)

## See also

- [bar-chart.md](bar-chart.md): the form these are built from, and where the evidence is
- [magnitude.md](magnitude.md): the group for when the level matters as much as the gap
- [../concepts/channels.md](../concepts/channels.md): the evidence tier these pages inherit from
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md): the taxonomy this index belongs to
- [README.md](README.md): the page template and the inheritance rule
