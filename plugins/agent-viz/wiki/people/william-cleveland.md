# William S. Cleveland

**What they are known for.** With Robert McGill at Bell Labs, Cleveland turned "which chart is better" from an argument into an experiment, producing the ranking of visual encodings that most of visualization practice still runs on. He is also the source of loess, the dot chart, banking to 45 degrees, and (with Becker and Shyu) trellis display, the ancestor of every faceted small-multiple grid in modern plotting libraries.

**Status: `primary-read` for Cleveland & McGill (1985) and Cleveland (2001), unread for the books.** The 1985 *Science* paper was pulled as a JSTOR scan; its text layer is three-column and interleaves badly, so the quotes and the table below were **transcribed from rendered page images at 200 dpi**, not from a `-layout` dump and not from a summary. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) is already `primary-read` in this wiki by the same method. The book contents below come from library-catalog contents scans, extracted locally. Retrieval date: **2026-08-23**.

**What they are good for.** Come here before citing "the Cleveland-McGill ranking," because there are **two of them**, they disagree, and the one everybody reproduces is not the one this wiki has a page for.

**What they do not settle.** Almost everything past rank 1, by their own statement. Also: nothing about attention, memory, narrative, or aesthetics. Cleveland's entire program is about the accuracy of reading a number off a mark, and he says so in both papers.

---

## What their work actually established

### There are two rankings, published thirteen months apart

This wiki's [cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) reproduces the JASA table: **ten tasks in six ranks**, with length, direction and angle tied at rank 3, curvature at rank 5, shading and color saturation at rank 6, and color hue explicitly excluded.

The *Science* paper from August 1985 prints a different table. Verbatim from Table 1, p. 830, caption included:

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

**Read the two side by side.** Length and angle are no longer tied. Color hue is no longer excluded; it is ranked, and it is last. Curvature has disappeared and density has appeared. Slope enters with a caveat about its own working range.

**This resolves a puzzle the wiki currently records as an error.** [refutations.md](../refutations.md) says the fully ordered `position > length > angle > area > volume > color` list "is not the version in the paper," and [cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) says that a ranking putting color at the bottom and meaning hue "is not reporting this paper." Both are correct about the 1984 paper and both are incomplete, because the list in circulation is an accurate reproduction of the 1985 *Science* table. The citation is not fabricated. It is pointed at the wrong one of two papers by the same two authors.

### What the 1985 paper says about its own ranking

The important part, because it is what the citation chain drops. From p. 829, under *Ordering the Elementary Graphical-Perception Tasks*:

> "The ordering should be thought of as a tentative working hypothesis, based on current information, that can be expected to evolve. With the information now available we have been unable to distinguish the relative accuracy of some tasks, such as judging slope and judging angle. Aspects of the ordering are partly conjectural in that we have no controlled experimentation to support them."

And on p. 830, immediately after stating the design principle:

> "The ordering does not result in a precise prescription for displaying data but rather is a framework within which to work."

So the 1985 separation of length from angle is **not a new measurement**. No third experiment broke the 1984 tie. The same evidence was reorganized, the ties were resolved on theoretical grounds, and the authors labeled that reorganization a working hypothesis in the same section that presents it. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) later built stimuli specifically to test length against angle on a common format and did not find the predicted difference.

**The accurate statement:** the seven-rank list is genuinely Cleveland & McGill's, and its warrant is theory plus two experiments, self-labeled partly conjectural. The problem with the citation is not the list. It is the confidence.

### Where else his name carries more than his results

**Banking to 45 degrees.** Real result, real scope limit, and the wiki already handles it. See [talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md) and [refutations.md](../refutations.md). The one-line version: Cleveland's model fits inside the moderate regime he sampled and does not extrapolate, and his subjects were *instructed* to compare heights, which most people spontaneously do not do. "Refuted" is the wrong word and "general" is also the wrong word.

**"Cleveland proved bars beat pies because length beats angle."** He did not, in either paper. 1984 measured length against position in one experiment and angle against position in another, and states that the two may not be compared. 1985 separates them in a table it calls conjectural. Bar-beats-pie is measured and replicated; the mechanism attached to it is not. See [concepts/channels.md](../concepts/channels.md).

**"Cleveland founded data science."** His 2001 *International Statistical Review* paper is six pages long and is a **curriculum and resource-allocation proposal**. It names six technical areas for a university department with a percentage attached to each (multidisciplinary investigations 25%, models and methods 20%, computing with data 15%, pedagogy 15%, tool evaluation 5%, theory 20%), and applies the same percentages to the course catalog. The naming is deliberate and it is a renaming, not a founding:

> "Because the plan is ambitious and implies substantial change, the altered field will be called 'data science'."

There is no experiment in it and no claim of priority over the term. Cite it for what it is: a statistician proposing that his own department reallocate a fifth of its effort away from theory.

### The prescriptive half, which almost nobody cites

Both papers end by telling you to change what you draw, and both prescriptions are ignored relative to the rankings. 1984's abstract conclusion is "radical surgery on these popular graphs is needed," with dot charts and framed-rectangle charts offered as the replacements. The 1985 paper closes on the same list: dot charts, Tukey box plots, graphing on a log base 2 scale, two-tiered error bars, and lowess.

One of those prescriptions predates a study this wiki already has, by thirty years. From p. 832:

> "Graphing means and sample standard deviations, the most commonly used graphical method for conveying the distributions of groups of measurements, is frequently a poor method. We cannot expect to reduce distributions to two numbers and succeed in capturing the widely varied behavior that data sets in science can have."

That is [weissgerber-2015-beyond-bar-line.md](../studies/weissgerber-2015-beyond-bar-line.md)'s conclusion, in *Science*, in 1985, from the person the field cites for something else entirely.

### Sample and era, same caveat as 1984

The 1985 paper reports its subject groups did not differ by technical training, and treats that as unsurprising: "the preattentive visual tasks are very basic judgments that the visual system performs daily." Bell Labs convenience samples of roughly 50, static charts on paper, mid-1980s. That is not a defect. It matters because the result gets quoted as a population constant.

---

## What they would object to in your figure

*Reconstruction from his stated priorities. He has not seen your figure.*

He would go straight to the encoding and ignore everything around it. Is a comparison the reader has to make encoded as position along a **common** scale, or did you split it across panels and demote it to rank 2 for no reason? Is anything important riding on area, or on color saturation, when a dot chart would put it on position? Are you showing means and standard deviations where the distribution is the actual finding? Is the aspect ratio destroying the rate of change you are asking people to see? He would not comment on your title, your palette's taste, or whether the figure tells a story, because none of those are in his frame. He would also, and this is the part people forget, tell you to stop drawing the chart and draw a different one: his conclusions are prescriptive, and the prescription is usually a dot chart.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Cleveland & McGill (1984), "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *JASA* 79(387), 531-554 | `primary-read` | [studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) |
| Cleveland & McGill (1985), "Graphical Perception and Graphical Methods for Analyzing Scientific Data," *Science* 229(4716), 828-833 | `primary-read`. JSTOR scan; quotes transcribed from rendered page images. | **No page.** It carries the seven-rank ordering everyone actually cites. |
| *The Elements of Graphing Data*, revised ed. (Hobart Press) | `not-reached`. Contents verified from the [GBV catalog scan](http://www.gbv.de/dms/weimar/toc/172079535_toc.pdf), extracted locally. | No page. Section list below. |
| *Visualizing Data* (Hobart Press, 1993) | `not-reached`. Contents verified from a [GBV catalog scan](http://www.gbv.de/dms/hbz/toc/ht006295728.pdf) (image-only). | No page. Loess, coplots, multiway dot plots, and a chapter each on univariate through multiway data. |
| Becker, Cleveland & Shyu (1996), "The Visual Design and Control of Trellis Display," *JCGS* 5(2) | `not-reached`. **No PDF exists**: the Bell Labs originals were PostScript only, and no OA copy is recorded by OpenAlex or Semantic Scholar. The reachable substitutes are *A Tour of Trellis Graphics* and the Trellis user manual, which are not the paper. | No page, and it is the paper R's lattice package implements, with the faceted-grid idiom in ggplot2 and seaborn downstream of the same idea. [inventory.md](../inventory.md) topic 62 (small multiples with shared scales) is sourced to Urban, BBC, Wilke and Munzner, and not to the paper that specified the idiom. |
| Cleveland (2001), "Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics," *International Statistical Review* 69(1), 21-26 | `primary-read`. JSTOR scan, extracted locally. | No page. Out of scope for a figure bar; read so the attribution claim above is checkable rather than flagged. |
| Cleveland, McGill & McGill (1988), "The Shape Parameter of a Two-Variable Graph," *JASA* 83(402) | `not-reached`. Closed on both OpenAlex and Semantic Scholar; no repository copy anywhere. | The banking paper. Covered indirectly through [talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md) and [refutations.md](../refutations.md), never directly. |
| Cleveland & Devlin (1988), loess, *JASA* | Reachable, not read: [sites.stat.washington.edu](https://sites.stat.washington.edu/courses/stat527/s13/readings/Cleveland_Delvin_JASA_1988.pdf) | No page. Out of scope here, listed for completeness. |

**Where the banking guidance actually lives in book form.** *The Elements of Graphing Data* gives it two sections, one prescriptive and one perceptual: **2.4 Banking to 45°** under *Principles of Graph Construction*, and **4.7 Banking to 45°** under *Graphical Perception*. Chapter 4 also carries 4.1 The Model, 4.6 Order on Dot Plots, 4.9 Graphing Along a Common Scale, and 4.10 Pop Charts, which is the prescriptive half of the 1984 paper turned into a chapter. Anyone chasing the scope of the banking result to its source should start at 4.7 rather than at the 1988 JASA paper, which has no open copy at all.

## See also

- [studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md), the six-rank table and its ties
- [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md), the replication, and the length-versus-angle test that failed
- [concepts/channels.md](../concepts/channels.md), what the ranking is used for and how far it carries
- [studies/talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md), banking to 45, scope-limited
- [tamara-munzner.md](tamara-munzner.md), the textbook that carries his ranking forward, and what happens to a caveat in transit
