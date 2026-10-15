---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Cleveland & McGill (1984), *Graphical Perception*

William S. Cleveland and Robert McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods," *Journal of the American Statistical Association* 79(387), September 1984, pp. 531-554. The paper behind the ranking of visual encodings that most visualization practice still runs on.

**What it is good for.** The ordering as published, which differs from the one in circulation, and the authors' own limits on it.

**What it does not settle.** Most of what it is cited for beyond rank 1. The ordering has ties the authors could not break, only two comparisons were tested, and the authors say their two experiments are not comparable.

**How this was read.** The reachable copies are JSTOR scans with no text layer, so local text extraction returns only the JSTOR cover sheet. Quotes were transcribed from rendered page images of the article, not from OCR or a fetch summary. Page numbers are the journal's.

The ranking reproduced everywhere, seven ranks fully ordered with color hue last, is from the 1985 *Science* paper, so citing this one for it is the wrong reference. Both tables and the 1985 hedges are in [../people/william-cleveland.md](../people/william-cleveland.md).

## The ordering, as published

From p. 536, under "The following are the 10 elementary tasks in Figure 1, ordered from most to least accurate":

1. Position along a common scale
2. Positions along nonaligned scales
3. Length, direction, angle
4. Area
5. Volume, curvature
6. Shading, color saturation

Six ranks, ten tasks. On p. 537:

> "Three of the ranks—3, 5, and 6—have more than one task; at the moment there is not enough information to separate the ties."

Reproductions usually run seven to nine fully ordered items, with length above angle above area. Here length, direction and angle share a rank.

## What was tested

Two experiments, not ten:

- **Position-length.** 55 subjects, 51 retained. Five judgment types across grouped and divided bar charts. Types 1-3 are position along a common scale, types 4-5 are length.
- **Position-angle.** 54 subjects, 51 retained. Pie chart versus bar chart, ten sets of five values summing to 100.

Accuracy was log base 2 of (absolute error plus one eighth), summarized by midmeans because the log errors showed "discrete data," "mild skewness" and "frequent outliers."

Position-length (p. 541):

> "The larger of the two length values is 1.32 log units greater than the smallest of the three position values, which is a factor of 2^1.32 = 2.5. The smaller length value is .51 log units greater than the largest position value, which is a factor of 1.4. Thus the average errors for length judgments are 40%-250% larger than those for position judgments."

Position-angle:

> "The difference is .97 on the log scale, which is a factor of 2^.97 = 1.96, and is statistically significant."

Pie versus bar (p. 540): "In only 3 of the 40 cases was the pie chart more accurate on average than the bar chart."

## The comparability caveat that kills the popular reading

Also p. 541:

> "Within an experiment it is reasonable to compare the means of the judgments because the set of true percentages is the same for each judgment, but it would be inappropriate to compare the means of the first experiment with those of the second."

Length was measured against position in one experiment and angle against position in the other. So the paper has no test of length versus angle, which is why rank 3 is a tie, and it does not support "Bars beat pies because length beats angle". [heer-bostock-2010.md](heer-bostock-2010.md) ran that comparison under a common format, and it did not come out that way.

## Four qualifications the citation record drops

**Color hue and texture are excluded, not ranked last.** From p. 532:

> "color hue and texture (Bertin 1973) are two elementary tasks excluded from the list because they do not have an unambiguous single method of ordering from small to large and thus might be regarded as better for encoding categories rather than real variables."

Rank 6 is shading and color saturation, meaning ordered lightness and intensity. A ranking with hue at the bottom is not reporting this paper.

**The ordering is hypothesized, and only partly from experiment.** From p. 537:

> "The hypothesized ordering of the elementary tasks is based on information from a variety of sources: our own reasoning and experimentation with various graph forms, results of psychophysical experiments, and the theory of psychophysics. The following discussion attempts only a partial documentation."

**The list is neither exhaustive nor distinct.** From p. 532:

> "We do not pretend that the items on our list are completely distinct tasks; for example, judging angle and direction are clearly related. We do not pretend that our list is exhaustive"

followed by "Nevertheless the list in Figure 1 is a reasonable first try."

**The scope is accuracy of value extraction.** From p. 531:

> "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one."

It ranks reading a number off a mark, not finding a trend, cluster, outlier or shape.

## Which task a chart uses is conjecture, not measurement

Section 2 offers the mapping from chart type to elementary task as conjecture. On pie charts (p. 533):

> "we conjecture that the primary elementary visual task for extracting the numerical information is perception of angle, but the areas and arc lengths of the pie slices are variable and probably are also involved in judging the data."

On bar charts, position is primary, "but judgments of area and length probably also play a role."

Skau and Kosara later tested the pie decomposition directly. The result is on [pie-and-donut.md](../chart-types/pie-and-donut.md).

## Sample and era limits

Subjects fell into two groups: "a group of females, mostly housewives, without substantial technical experience," and "a mixture of males and females with substantial technical training and working in technical jobs." A Bell Labs convenience sample of about 50 per experiment, in 1984, judging static charts printed on 8.5x11 sheets. The authors found no accuracy difference between the groups and treated the sample as homogeneous. It does not support quoting the result as a population-level constant.

## The paper's prescription

The abstract's conclusion is not "use position." It is:

> "The conclusion is that radical surgery on these popular graphs is needed"

with dot charts, grouped dot charts and framed-rectangle charts as replacements. Citations largely ignore this half.

## Evidence class of what this paper supports

- **Evidence-backed.** Position along a common scale is read more accurately than length, by a factor of 1.4 to 2.5. Position is read more accurately than angle, by a factor of about 2. Bar beats pie for value extraction on this task.
- **Authority-asserted.** The full six-rank ordering, a hypothesis built from theory, reasoning and prior psychophysics and tested at two points.
- **Not supported at all.** Any ordering within rank 3, any claim about color hue, and any claim about tasks other than reading a value off a mark.

## See also

- [heer-bostock-2010.md](heer-bostock-2010.md): the replication, and the head-to-head that 1984 could not run
- [../concepts/channels.md](../concepts/channels.md): what the ranking is used for, and how far it carries
- [../concepts/evidence-class.md](../concepts/evidence-class.md): the labeling discipline this page applies
