---
type: index
---

# Deviation

Signed distance from a reference point: how far each item sits above or below the thing you are measuring it against, and on which side of it.

## Is deviation the right frame, and how to tell

The FT's definition of this family does more than name it ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Emphasise variations (+/-) from a fixed reference point. Typically the reference point is zero but it can also be a target or a long-term average. Can also be used to show sentiment (positive/neutral/negative)."

**The reference point is a free parameter of the chart, and nothing on the chart shows the reader that you picked it.** That is the argument for treating this as a group.

**Not everyone agrees this is a category.** Schwabish's scheme has no Deviation in it at all. *Better Data Visualizations* files Diverging Bar in chapter 4, Comparing Categories, and [schwabish.md](../sources/schwabish.md) puts it flatly: "Deviation and Flow have no home in his scheme." The memberships there are verified from the book's contents pages; what the book argues about any type is unread. Two practitioner taxonomies descended from the same 2014 poster disagree about whether a diverging bar is a deviation chart or a comparison chart. `authority-asserted` on both sides, and it is a useful reminder that the group is a retrieval aid rather than a fact about the chart.

Three tests.

**Is there a reference the reader already accepts?** Zero, a budget, a published target, a long-run average, the national rate, last year. If the caption has to argue for the reference, the reference is carrying the claim and the chart is illustrating it. Sometimes that is exactly the job. It should be a decision rather than a library default.

**Does the reader need the difference, or the level?** Plotting a deviation throws the base away. Two items both at +4 might be 104 and 4004, and the chart cannot tell them apart. If the level matters too, you need a magnitude chart with a reference line drawn on it, or both charts.

**Does the sign mean something?** This group spends its whole design on which side of a line an item falls. If above and below are not different in kind, or if everything lands on one side anyway, you have a [bar chart](bar-chart.md) with an extra line on it, which is fine and is not this group.

| The reader's actual question | Go to |
|---|---|
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md) |
| Which is biggest, and in what order? | Ranking. A sorted bar chart |
| How did this move over time? | [Change over time](change-over-time.md). A line chart, with the reference drawn as a rule |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| How spread out are the values? | [Distribution](distribution.md) |
| Do these two variables move together? | [Correlation](correlation.md) |
| Which items are above the line, which below, and by how much? | **Stay here** |

## The reference point is a rhetorical choice the reader cannot see

This is the group's real cost, and its two halves carry different warrants.

**What follows from the structure, and is secure.** A deviation chart draws `value - reference`. Change the reference and every bar changes length, some bars change side, and not one number in the underlying data has moved. Zero, the target, and the long-run average are three different charts of one dataset, and they can disagree about who is failing. The chart displays the result of the subtraction and not the choice of what to subtract, so the reader has no way to recover the decision from the picture. That is definitional, and it is the same shape of problem as the aspect ratio and the axis window in [change-over-time.md](change-over-time.md).

**What is not measured here, and must not be run together with the above.** Nobody in this corpus has tested whether moving a reference point moves a reader's conclusion. `absence of evidence`.

The nearest measured thing is **axis truncation**, and it is a different manipulation. [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) moved a bar chart's baseline off zero while the axis stayed in raw units, and mean response on a "how much bigger" scale went from 1.45 to 2.77, an increase of 91.0%, with the true values printed on the chart. [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) got the same direction, F(2, 76) = 89, p < 0.0001, and found the mark type did not rescue it.

A deviation chart is not that. Truncation leaves the quantity alone and moves the origin under it, so the ink stops being proportional to the plotted number. A deviation chart **redefines the quantity** to be the difference, and the ink is then proportional to that difference, which is why Urban names exactly this move as a legitimate remedy for a truncation temptation: "consider adjusting the data to show percent change, difference, or some other similar adjustment" ([urban-institute.md](../sources/urban-institute.md)). The subtraction is disclosed by the axis label; the choice of what was subtracted is not.

So the honest pair of sentences is: the deviation transform is the *fix* for truncation, not an instance of it, and the freedom it hands you sits one level up, in choosing the reference. What that freedom does to readers is untested.

## What else this group costs

**The accuracy is mostly intact, which is unusual for an index here.** Every bar starts at one shared reference line, so a bar's end is read as position along a common scale, the same reading the plain bar chart gets ([channels.md](../concepts/channels.md)). The step from this chart to that channel is conjecture in the source literature, as it is for every type in this tier.

**Except across the line.** That reading holds cleanly for items on the same side. Comparing a bar running left against a bar running right is a comparison of two lengths in opposite directions from a common origin, which is not a task anyone in this corpus has measured. `absence of evidence`, and it is the judgment a diverging bar is most often drawn to invite.

**The sign is not on a magnitude channel at all.** Which side of the line a bar falls on is a categorical read, and the Cleveland & McGill orderings score nothing of the kind ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). It is usually doubled in hue, which is [inventory](../inventory.md) topic 69 (redundant coding) and is hue doing the job hue is actually good at, identity rather than magnitude.

**Stacking gives that accuracy away.** The moment segments accumulate outward from the center, everything past the innermost segment floats, and floating segments carry 40% to 250% more error than position readings, measured directly on divided bars ([stacked-bar.md](stacked-bar.md)). That is the cost of the diverging stacked bar and it is the one measured number this group can reach.

## Choosing a form

| Form | What carries the value | Reach for it when |
|---|---|---|
| [Diverging bar chart](diverging-bar-chart.md) | Bar length from a shared reference line, side carrying the sign | One signed number per category, and above/below is the point |
| [Spine chart](spine-chart.md) | Two component lengths growing outward from a shared center | Each row splits one total into two contrasting parts |
| Diverging stacked bar | Segment lengths accumulating outward from a center | Ordered response categories per row, Likert data being the usual case. Covered on [diverging-bar-chart.md](diverging-bar-chart.md), because it is that chart with a cumulative sum added |
| Surplus / deficit filled line *(no page here)* | Filled area between a series and a reference line, shaded by side | The deviation runs over time and you want the periods of surplus and shortfall as shapes |

A bullet chart puts one value against a target and a qualitative range, and a population pyramid is a [spine chart](spine-chart.md) whose rows are age bands. Neither has a page, because no study in this corpus tests either.

Two constraints that follow from the structure rather than from taste:

- **Label the reference line with its value and with what it is.** "0" is not a label; "2019 average, 4.1%" is. This is the same rule [inventory](../inventory.md) topic 32 states for the midpoint of a diverging color scale, which "must be set to a meaningful value and labeled" (`authority-asserted`, from Urban). The color-scale version got written down; the geometric version is the identical problem and mostly did not.
- **Sort by the deviation, not by the raw value.** Sorting on the base leaves a picture whose ordering answers a question the chart is not about.

## Justifying the choice

**Defensible, evidence-backed:**

- "Bars run from the reference line, so their ends read as position along a common scale for every item on the same side of it." That inherits the best-measured comparison in the literature ([channels.md](../concepts/channels.md)), and the step from chart to channel is conjecture, as it is everywhere in this tier.
- "I plotted the difference instead of truncating the axis under a bar. Truncating a bar axis moved readers' size judgments 91% in a controlled test, and this transform keeps the ink proportional to the quantity actually drawn."

Nothing else in this bucket is native to the group. No study here tests any chart in it.

**Defensible, with the label said out loud:**

- "The reference is the five-year average rather than zero, and the subtitle says so." That the reader cannot otherwise recover the choice follows from the structure; that stating it helps is practitioner convention with nothing measured behind it.
- "Above and below are colored differently as well as pointed differently, so the sign does not rest on one channel." Redundant coding, inventory topic 69, `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A diverging bar makes the gap between any two items easy to compare."~~ Which side each item is on is there by construction. Comparing an item above the line against an item below it means comparing two lengths running in opposite directions, and nobody in this corpus has measured that judgment.
- ~~"The reference line and the color midpoint are the same decision."~~ They are two, and a diverging color scale that pivots somewhere other than the reference line puts the two midpoints in different places on one chart. Inventory topic 32 asks for the color midpoint to be meaningful and labeled; the geometric reference needs the same treatment and usually does not get it.

## The failure mode this group invites

**Picking the reference that produces the picture.** Every candidate reference is arguable, all of them are honest one at a time, and the chart shows none of the alternatives. This is the group where a figure can be arithmetically perfect, correctly labeled, and still be an argument won before the reader arrived.

A usable check, borrowed from the same move in [change-over-time.md](change-over-time.md): say the conclusion out loud, then redraw against zero and against the long-run average. If the sentence stops being true, the sentence was about the reference you chose.

**Reading a deviation as a level.** The base is not on the chart. A reader who takes "+9" for "a lot" has no way to know whether the base was 12 or 12,000, and the form gives no cue that the question exists.

## Types in this index

- [diverging-bar-chart.md](diverging-bar-chart.md), which also covers the diverging stacked bar
- [spine-chart.md](spine-chart.md)

## See also

- [bar-chart.md](bar-chart.md) — the form these are built out of, and where the evidence is
- [magnitude.md](magnitude.md) — the group to fall back to when the level matters as much as the gap
- [../concepts/channels.md](../concepts/channels.md) — the evidence tier these pages inherit from, and the conjecture in the inheritance
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) — the taxonomy this index belongs to
- [README.md](README.md) — the page template and the inheritance rule
