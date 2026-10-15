---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# William S. Cleveland

**What they are known for.** With Robert McGill at Bell Labs, Cleveland turned "which chart is better" from an argument into an experiment and a ranking of visual encodings. Also loess, the dot chart, banking to 45 degrees, and (with Becker and Shyu) trellis display, the ancestor of faceted small multiples.

**How this was read.** `primary-read` for Cleveland & McGill (1985) and Cleveland (2001), unread for the books. The 1985 *Science* JSTOR scan's three-column text layer interleaves badly, so its quotes and table were transcribed from page images rendered at 200 dpi, as for [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md). Book contents come from library-catalog scans, extracted locally.

**What they are good for.** The status of "the Cleveland-McGill ranking". There are two, they disagree, and the one everybody reproduces is not the one this wiki has a page for.

**What they do not settle.** Almost everything below the top rank, by their own statement. Attention, memory, narrative and aesthetics are outside both papers, which concern the accuracy of reading a number off a mark.

## What their work established

### There are two rankings, published under a year apart

[cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) reproduces the *JASA* table: ten tasks in six ranks, with length, direction and angle tied at rank 3, curvature at rank 5, shading and color saturation at rank 6, and color hue explicitly excluded.

The August 1985 *Science* paper prints a different table. Table 1, p. 830, with its caption:

> "Table 1. Ordering elementary tasks by accuracy, according to theoretical arguments and experimental results. Graphs should exploit tasks as high in the ordering as possible. The tasks are ordered from most accurate to least."

| Rank | Aspect judged |
|---|---|
| 1 | Position along a common scale |
| 2 | Position on identical but nonaligned scales |
| 3 | Length |
| 4 | Angle; Slope (with θ not too close to 0, π/2, or π radians) |
| 5 | Area |
| 6 | Volume; Density; Color saturation |
| 7 | Color hue |

Length and angle are untied, hue is ranked last, curvature is gone, density has appeared, and slope carries a caveat on its working range.

[refutations.md](../refutations.md) says the fully ordered `position > length > angle > area > volume > color` list "is not the version in the paper," and [cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) says a ranking with color at the bottom, meaning hue, "is not reporting this paper." Both are right about 1984. The circulating list accurately reproduces the 1985 table, so the citation is misdirected, not fabricated.

### What the 1985 paper says about its own ranking

From p. 829, under *Ordering the Elementary Graphical-Perception Tasks*:

> "The ordering should be thought of as a tentative working hypothesis, based on current information, that can be expected to evolve. With the information now available we have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle. Aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them."

On p. 830, right after the design principle:

> "The ordering does not result in a precise prescription for displaying data but rather is a framework within which to work."

No third experiment broke the 1984 length-angle tie. The ties were resolved on theory. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) later tested length against angle on a common format and did not find the predicted difference. The seven-rank list is Cleveland & McGill's, its warrant is theory plus two experiments self-labeled partly conjectural, and what the citation chain overstates is the confidence.

### Where his name carries more than his results

**Banking to 45 degrees.** Neither refuted nor general ([talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md), [refutations.md](../refutations.md)). The model fits the moderate regime he sampled and does not extrapolate, and his subjects were told to compare heights, which most people do not do unprompted.

**"Cleveland proved bars beat pies because length beats angle."** Neither paper shows this. The 1984 paper tested length and angle against position in separate experiments it says may not be compared, and 1985 separates them in a table it calls conjectural. Bar-beats-pie is measured and replicated, and the mechanism is not ([concepts/channels.md](../concepts/channels.md)).

**"Cleveland founded data science."** The 2001 paper is a curriculum and resource-allocation proposal for a university department: multidisciplinary investigations 25%, models and methods 20%, computing with data 15%, pedagogy 15%, tool evaluation 5%, theory 20%, with the same shares applied to the course catalog. The name is a renaming, not a founding:

> "Because the plan is ambitious and implies substantial change, the altered field will be called 'data science'."

It has no experiment and claims no priority over the term: a statistician proposing that his own department reallocate a fifth of its effort away from theory.

### The prescriptive half, cited far less than the rankings

Both papers end by prescribing what to draw. The 1984 abstract concludes "radical surgery on these popular graphs is needed," offering dot charts and framed-rectangle charts. The 1985 paper closes on dot charts, Tukey box plots, log base 2 scales, two-tiered error bars and lowess. Its p. 832 states the conclusion of [weissgerber-2015-beyond-bar-line.md](../studies/weissgerber-2015-beyond-bar-line.md) thirty years early:

> "Graphing means and sample standard deviations, the most commonly used graphical method for conveying the distributions of groups of measurements, is frequently a poor method. We cannot expect to reduce distributions to two numbers and succeed in capturing the widely varied behavior that data sets in science can have."

### Sample and era

The 1985 paper finds no difference by technical training and expects none: "the preattentive visual tasks are very basic judgments that the visual system performs daily." Its subjects were Bell Labs convenience samples of roughly 50 judging static charts on paper, yet the result is quoted as a population constant.

## What they would object to in a figure

*Reconstruction from his stated priorities, not a response to any actual figure.*

The encoding only: whether a key comparison sits on a common scale or is split across panels, whether anything rides on area or saturation that a dot chart would put on position, whether means and standard deviations replace a distribution, and whether the aspect ratio hides a rate of change. His usual prescription is a dot chart.

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Cleveland & McGill (1984), "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *JASA* 79(387), 531-554 | `primary-read` | [studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) |
| Cleveland & McGill (1985), "Graphical Perception and Graphical Methods for Analyzing Scientific Data," *Science* 229(4716), 828-833 | `primary-read`. JSTOR scan, quotes transcribed from rendered page images. | No page. It carries the seven-rank ordering everyone cites. |
| *The Elements of Graphing Data*, revised ed. (Hobart Press) | `not-reached`. Contents verified from the [GBV catalog scan](http://www.gbv.de/dms/weimar/toc/172079535_toc.pdf), extracted locally. | No page. Section list below. |
| *Visualizing Data* (Hobart Press, 1993) | `not-reached`. Contents verified from a [GBV catalog scan](http://www.gbv.de/dms/hbz/toc/ht006295728.pdf) (image-only). | No page. Loess, coplots, multiway dot plots, and a chapter each on univariate through multiway data. |
| Becker, Cleveland & Shyu (1996), "The Visual Design and Control of Trellis Display," *JCGS* 5(2) | `not-reached`. No open-access PDF was found: the Bell Labs originals were PostScript only, and OpenAlex and Semantic Scholar record no OA copy. *A Tour of Trellis Graphics* and the Trellis user manual are reachable substitutes, not the paper. | No page. R's lattice implements it, and ggplot2 and seaborn facets descend from it. [inventory.md](../inventory.md) topic 62 (small multiples with shared scales) cites Urban, BBC, Wilke and Munzner, not this paper. |
| Cleveland (2001), "Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics," *International Statistical Review* 69(1), 21-26 | `primary-read`. JSTOR scan, extracted locally. | No page. Out of scope for a figure bar; read so the attribution claim above is checkable. |
| Cleveland, McGill & McGill (1988), "The Shape Parameter of a Two-Variable Graph," *JASA* 83(402) | `not-reached`. Closed on OpenAlex and Semantic Scholar, no repository copy. | The banking paper. Covered indirectly through [talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md) and [refutations.md](../refutations.md). |
| Cleveland & Devlin (1988), loess, *JASA* | Reachable, not read: [sites.stat.washington.edu](https://sites.stat.washington.edu/courses/stat527/s13/readings/Cleveland_Delvin_JASA_1988.pdf) | No page. Out of scope here. |

*The Elements of Graphing Data* treats banking in **2.4 Banking to 45°** (*Principles of Graph Construction*) and **4.7 Banking to 45°** (*Graphical Perception*), and with the 1988 paper closed, the result's scope traces to 4.7. Chapter 4 also has 4.1 The Model, 4.6 Order on Dot Plots, 4.9 Graphing Along a Common Scale and 4.10 Pop Charts.

## See also

- [studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md): the six-rank table and its ties
- [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md): the replication, and the length-versus-angle test that failed
- [concepts/channels.md](../concepts/channels.md): how far the ranking carries
- [studies/talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md): banking to 45, scope-limited
- [tamara-munzner.md](tamara-munzner.md): the textbook that carries his ranking forward, and how its caveat fares
