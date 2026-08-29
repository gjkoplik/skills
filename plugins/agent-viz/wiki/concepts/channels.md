---
type: concept
---

# Channels, and why the evidence lives here

**What it is.** The perceptual channels a mark can carry a value on (position, length, angle, area, and the rest), the accuracy ordering over them, and the argument that this is the *only* level at which the graphical-perception literature actually says anything.

**Status.** Synthesis over two `primary-read` sources: [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) and [Heer & Bostock (2010)](../studies/heer-bostock-2010.md). Munzner's marks-and-channels chapter is the standard textbook treatment and is [`secondary-only`](../sources/munzner-vad.md) in this wiki, so it is used here as a pointer rather than as a warrant. Nothing below rests on it.

**What it is good for.** Deciding what a chart-type page is allowed to claim. A sentence like "bar charts are more accurate than pie charts" resolves here.

**What it does not settle.** Which channel a given chart actually puts the reader on. That step is conjecture in the source literature and stays conjecture here.

---

## The idea the tier rests on

**No controlled study has ever tested a chart type. They test channels.**

Cleveland & McGill measured how accurately people read a proportion off position, length, angle and area. Heer & Bostock measured the same on Mechanical Turk and added rectangular area. Neither measured "the pie chart" as an artifact in the world. Both measured a stripped proportional-judgment task on stimuli drawn to look like one.

So every claim about a chart type is a two-step inference:

1. **This chart puts the reader on that channel.**
2. **That channel is read with this accuracy.**

Step 2 is measured. Step 1 is a guess, and Cleveland & McGill flag it as one every single time they make it. On pie charts: "we conjecture that the primary elementary visual task ... is perception of angle, but the areas and arc lengths of the pie slices are variable and probably are also involved." On bar charts, the same hedge for position.

**Step 1 is the weak link, and it is the step routinely skipped.** A chart-type page that states an accuracy claim flatly has silently upgraded a conjecture into a finding, which is the exact failure [evidence-class.md](evidence-class.md) exists to prevent.

This is why the wiki splits the tiers. Channel pages carry the evidence. Type pages inherit it, and inherit the uncertainty in step 1 along with it.

## The working ranking

From Cleveland & McGill p. 536, ten tasks in six ranks, reproduced exactly as published:

| Rank | Tasks |
|---|---|
| 1 | Position along a common scale |
| 2 | Positions along nonaligned scales |
| 3 | Length, direction, angle |
| 4 | Area |
| 5 | Volume, curvature |
| 6 | Shading, color saturation |

Ranks 3, 5 and 6 hold more than one task each, and the authors state that "at the moment there is not enough information to separate the ties."

**There is a second ranking, and it is the one people actually reproduce.** Cleveland & McGill published a different table in *Science* the following year: seven ranks, fully ordered, length at 3 and angle at 4 rather than tied, curvature gone, density added, and **color hue present and ranked last**. See [../people/william-cleveland.md](../people/william-cleveland.md), which reproduces both tables side by side.

So the familiar `position > length > angle > area > volume > color` list is not a corruption of anything. It is an accurate reproduction of the 1985 table, usually cited to the 1984 paper. The citation is pointed at the wrong one of two papers by the same two authors.

**This does not rescue the ordering's authority, and the 1985 paper says so itself:**

> "The ordering should be thought of as a tentative working hypothesis, based on current information, that can be expected to evolve. With the information now available we have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle. Aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them."

Both tables are hypotheses, both authors say so, and the 1985 one separates length from angle without new experimental support for that particular separation.

**What is actually measured, versus inherited from theory:**

| Comparison | Status | Source |
|---|---|---|
| Position beats length | Evidence-backed, errors 40% to 250% larger | CM84, HB10 |
| Position beats angle | Evidence-backed, factor ~2 | CM84, HB10 |
| Position beats area | Evidence-backed | HB10 |
| Angle beats area | Evidence-backed | HB10 |
| **Length beats angle** | **Contested. Predicted by theory, not found in the one head-to-head test** | HB10 |
| Rectangular area ≈ circular area | Evidence-backed | HB10 |
| Everything at ranks 5 and 6 | Authority-asserted, from psychophysics and reasoning | CM84 |

## The one joint where the folk ranking breaks

The chain `position > length > angle > area` is right at every step except one. Heer & Bostock built judgment types 6 and 7 to a common format specifically so angle could be compared against length, and reported:

> "Theory also suggests that angle should perform worse than length, but the results do not support this."

Cleveland & McGill did not find it either, and structurally could not have: their length result and their angle result come from two experiments they explicitly say may not be compared.

**Length and angle sit at the same rank, that tie has never been broken, and one attempt to break it failed.** The claim that bars beat pies *because* length beats angle cites a result that does not exist. Bars do beat pies on proportional judgment, measured directly and repeatedly. The mechanism usually given for it is not the measured part.

## What the ranking is not about

The scope limit is in the source, p. 531:

> "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one."

The task under test is: *read a value off a mark and report it as a number.* The ranking says nothing about

- spotting a trend, a cluster, an outlier or a gap,
- comparing shapes,
- remembering the figure afterward,
- finding one item among many,
- or anything at the figure-set level.

A channel that reads values poorly can still be the right channel for a task that is not value extraction. Color hue is the standard case: unrankable for magnitude, excellent for identity and grouping.

Bertini, Correll & Franconeri, *Why Shouldn't All Charts Be Scatter Plots?* (2020), argue against the assumption "that the ranking derived from this two-value ratio judgment represents an atomic unit for visualization, so that the additional precision conveyed by position should transfer to better perceptual performance in more complex tasks." Their tabulation puts ratio judgment as one row among a dozen value-related tasks: "Empirical evidence about the precision of visual encodings for other tasks is often sparse or counter to existing recommendations." On the ordinal and multi-pair tasks they find two studies, and "because both rely primarily on position encodings, they cannot confirm whether the Cleveland & McGill position ranking holds for these alternative tasks."

`authority-asserted`: a position paper with no experiment in it. Its authors decline the strong reading, writing "Of course we are not proposing to throw the baby out with the bathwater." It scopes the ranking rather than moving it. See [../people/michael-correll.md](../people/michael-correll.md).

## What "color is the worst channel" actually means

The two papers handle hue differently.

**1984 excludes it**, p. 532:

> "color hue and texture (Bertin 1973) are two elementary tasks excluded from the list because they do not have an unambiguous single method of ordering from small to large and thus might be regarded as better for encoding categories rather than real variables."

**1985 ranks it, last.** Rank 7, below volume, density and saturation.

These are not in conflict; the second is the first with a decision made. The stated reason in 1984 gives the 1985 rank its content: hue has **no unambiguous ordering from small to large**, so a magnitude ranking is measuring how badly it does a job it is not shaped for.

Practical consequence, and it survives both versions: **"color is the least accurate channel" is true only for magnitude, and misleading as usually stated.** Ordered lightness is low-accuracy for magnitude. Hue is not low-accuracy for magnitude, it is *unsuited* to it, which is a different defect with a different remedy. A bar chart colored by category is not using a bottom-ranked channel badly. It is using hue for identity, which is what hue is good at and what neither table scores.

## How chart-type pages use this

The template every type page in [../chart-types/](../chart-types/) follows:

1. **The channels the mark puts the reader on** are named, primary and secondary, and that mapping is labeled as conjecture unless a study decomposed it.
2. **The accuracy claim is inherited from this page**, with a link, rather than restated as a number.
3. **The task the type is actually for** is stated, and it is frequently not value extraction, in which case the ranking does not bear on it at all.
4. **No upgrading.** If the mapping in step 1 is a conjecture, the conclusion in step 2 is a conjecture too, no matter how well measured the channel is.

Where a study *has* decomposed a specific type into its channels, that is a finding and belongs on the type page. Skau & Kosara on pie and donut charts is the model case, and it is the reason the pie page can say more than this one.

## See also

- [../studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) — the ordering and its stated limits
- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md) — the replication and the contested joint
- [../people/michael-correll.md](../people/michael-correll.md) — the scope critique above, and what it does and does not claim
- [evidence-class.md](evidence-class.md) — the labeling discipline
- [../chart-types/README.md](../chart-types/README.md) — the types that inherit from here
