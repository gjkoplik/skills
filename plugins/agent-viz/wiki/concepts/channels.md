---
type: concept
---

# Channels, and why the evidence lives here

**What it is.** The perceptual channels a mark can carry a value on (position, length, angle, area and the rest), their accuracy ordering, and the case that the graphical-perception literature makes claims only at this level.

**Status.** Synthesis over three `primary-read` sources, [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) and [Siqueira Rodrigues et al. (2026)](../studies/siqueira-rodrigues-2026-vr-graphical-perception.md). Munzner's marks-and-channels chapter, the standard textbook treatment, is [`secondary-only`](../sources/munzner-vad.md) here and serves as a pointer, not a warrant.

**What it is good for.** Deciding what a chart-type page may claim, such as "bar charts are more accurate than pie charts".

**What it does not settle.** Which channel a given chart puts the reader on. That step is conjecture in the source literature and here.

---

## The idea the tier rests on

No controlled study has tested a chart type. Cleveland & McGill measured how accurately people read a proportion off position, length, angle and area. Heer & Bostock repeated this on Mechanical Turk and added rectangular area. Both used a stripped proportional-judgment task on stimuli drawn to look like a chart, not "the pie chart" as an artifact in the world.

So every claim about a chart type is two steps: this chart puts the reader on that channel, and that channel is read with this accuracy. The second is measured. The first is a guess, and Cleveland & McGill flag it each time. On pie charts: "we conjecture that the primary elementary visual task ... is perception of angle, but the areas and arc lengths of the pie slices are variable and probably are also involved." They hedge bar charts the same way for position.

A type page that states an accuracy claim flatly has upgraded that guess into a finding, the failure [evidence-class.md](evidence-class.md) names. Type pages inherit the evidence from here, with the uncertainty in the first step.

## The working ranking

Cleveland & McGill p. 536, ten tasks in six ranks:

| Rank | Tasks |
|---|---|
| 1 | Position along a common scale |
| 2 | Positions along nonaligned scales |
| 3 | Length, direction, angle |
| 4 | Area |
| 5 | Volume, curvature |
| 6 | Shading, color saturation |

Ranks 3, 5 and 6 are ties, and the authors state that "at the moment there is not enough information to separate the ties."

The familiar `position > length > angle > area > volume > color` list reproduces a different table, published by the same authors in *Science* the following year and usually cited to 1984. It has seven fully ordered ranks: length at 3 and angle at 4, curvature gone, density added, color hue last. [../people/william-cleveland.md](../people/william-cleveland.md) reproduces both. The 1985 paper calls its ordering provisional:

> "The ordering should be thought of as a tentative working hypothesis, based on current information, that can be expected to evolve. With the information now available we have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle. Aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them."

Its separation of length from angle has no new experimental support.

| Comparison | Status | Source |
|---|---|---|
| Position beats length | Evidence-backed, errors 40% to 250% larger | CM84, HB10, SR26 |
| Position beats angle | Evidence-backed, factor ~2 | CM84, HB10 |
| Position beats area | Evidence-backed | HB10, SR26 |
| Angle beats area | Evidence-backed | HB10 |
| Length beats area | Evidence-backed | SR26 |
| **Length beats angle** | **Contested. Predicted by theory, not found in the one head-to-head test** | HB10 |
| Rectangular area ≈ circular area | Evidence-backed | HB10 |
| Everything at ranks 5 and 6 | Authority-asserted, from psychophysics and reasoning | CM84 |

CM84 is [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), HB10 is [Heer & Bostock (2010)](../studies/heer-bostock-2010.md), SR26 is [Siqueira Rodrigues, Israel & Kosch (2026)](../studies/siqueira-rodrigues-2026-vr-graphical-perception.md).

SR26 ran the ratio task in a head-mounted display. Mean absolute error was 3.68% for aligned bars, 6.61% for unaligned lengths and 12.05% for circle areas, with every pairwise contrast significant at d = 1.28 or larger. All three conditions sat in one design, a comparability [Cleveland & McGill's own two experiments lack](../studies/cleveland-mcgill-1984.md#the-comparability-caveat-that-kills-the-popular-reading). Angle was not a condition.

## The one joint where the folk ranking breaks

Heer & Bostock built judgment types 6 and 7 to a common format so angle could be compared against length:

> "Theory also suggests that angle should perform worse than length, but the results do not support this."

Cleveland & McGill did not find it either, and could not have, because their length and angle results come from two experiments they say may not be compared. The tie has never been broken, and the one attempt failed. Bars beat pies on proportional judgment, measured directly and repeatedly. The usual explanation, that length beats angle, is the unmeasured part.

## What the ranking is not about

The scope limit is in the source, p. 531:

> "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one."

The task is reading a value off a mark as a number, and the ranking says nothing about spotting a trend, cluster, outlier or gap, comparing shapes, remembering the figure, finding one item among many, or the figure-set level. Hue is unrankable for magnitude and good for identity and grouping.

Bertini, Correll & Franconeri, *Why Shouldn't All Charts Be Scatter Plots?* (2020), argue against the assumption "that the ranking derived from this two-value ratio judgment represents an atomic unit for visualization, so that the additional precision conveyed by position should transfer to better perceptual performance in more complex tasks." Ratio judgment is one of a dozen value-related tasks in their tabulation: "Empirical evidence about the precision of visual encodings for other tasks is often sparse or counter to existing recommendations." On ordinal and multi-pair tasks they find two studies, and "because both rely primarily on position encodings, they cannot confirm whether the Cleveland & McGill position ranking holds for these alternative tasks."

This is `authority-asserted`, a position paper with no experiment. The authors decline the strong reading: "Of course we are not proposing to throw the baby out with the bathwater." It scopes the ranking without moving it. See [../people/michael-correll.md](../people/michael-correll.md).

## What "color is the worst channel" actually means

The 1984 paper excludes hue, p. 532:

> "color hue and texture (Bertin 1973) are two elementary tasks excluded from the list because they do not have an unambiguous single method of ordering from small to large and thus might be regarded as better for encoding categories rather than real variables."

The 1985 paper ranks it last, at rank 7, below volume, density and saturation. Given the 1984 reason, that rank scores hue on a job it is not shaped for. The claim "color is the least accurate channel" holds only for magnitude. Ordered lightness reads magnitude poorly. Hue is unsuited to magnitude, a different defect with a different remedy. A bar chart colored by category uses hue for identity, which neither table scores.

## How chart-type pages use this

Each page in [../chart-types/](../chart-types/) names the channels its marks use, labels that mapping conjecture unless a study decomposed it, and links here instead of restating a number. Where a study did decompose a type, as Skau & Kosara did for pie and donut charts, the result is a finding for the type page. That is why the pie page says more than this one.

## See also

- [../studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md): the ordering and its stated limits
- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md): the replication and the contested joint
- [../people/michael-correll.md](../people/michael-correll.md): the scope critique
- [evidence-class.md](evidence-class.md): the labeling discipline
- [../chart-types/README.md](../chart-types/README.md): the types that inherit from here
