---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Alberto Cairo

**What they are known for.** Four books on how to argue about graphics: *The Functional Art* (2012), *The Truthful Art* (2016), *How Charts Lie* (2019) and *The Art of Insight* (2023). A University of Miami professor, former newsroom graphics director in Spain and Brazil, and co-editor with Tamara Munzner of CRC Press's visualization series.

**How this was read.** Partial, all extracted locally.

- *The Functional Art*: Pearson's sample PDF (`ptgmedia.pearsoncmg.com/images/9780321834737/samplepages/0321834739.pdf`), via `curl` and `pdftotext -layout`. Full contents page, introduction, chapter 1 in full, the About-the-DVD section, index.
- *The Truthful Art*: Peachpit's sample, the file [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md) was built from. Contents, preface, chapter 4 in full, index.
- His blog, `thefunctionalart.com`: front page, fetched and stripped to text. The source of the 2023 material, including a draft preamble to *The Art of Insight* he published himself.
- *How Charts Lie*: `not-reached`. Search results are dominated by pirated copies and AI summary sites, none usable.

**What they are good for.** Whether a figure over-reads its data. He spends pages on conjecture, study quality, sample variation, standard error, and significance versus effect size, which the other practitioners here mostly skip. His test is honesty, not cleanness.

**What they do not settle.** Chartcraft detail. He gives less usable instruction on color, type and layout than the other practitioners here, and little of his published work is his own figures.

## "In the style of Alberto Cairo" means, concretely

Most of his work is about other people's graphics. One figure of his own was examined, the cover chart of *The Functional Art*, through the sample's text layer. One figure is not a style, so the rest is his stated method, labeled as such.

**Palette.** Not established, since the figure was read as text and not measured. The *Truthful Art* contents put color inside his **Beautiful** quality, third of five behind Truthful and Functional, which is an ordering rather than a palette. [Muth's](lisa-charlotte-muth.md) and [Wilke's](claus-wilke.md) pages carry stated color positions.

**Annotation.** Heavy, and the best-grounded part. The cover chart sets each US state's share of adults with a BA or higher against its obesity rate, as two labeled columns of state abbreviations joined by connecting geometry. Two block annotations name what each region means: "States with a larger percentage of people with higher education than with obesity," and "States with a larger percentage of obese people than of people with a higher education." A callout gives the reference value: "the US average / 27.2% BA or higher / 27.0% Obese." Every point is labeled, there is no legend, and the prose annotates the interpretation of the geometry rather than the outliers.

Reviewing an Eldiario.es piece in December 2023, he praises "the combination of different types of charts, dot maps, scatter plots, stacked bar graphs, the effective annotations and highlights that emphasize the main points of the narrative, the use of color, and the addition of individual stories to exemplify the patterns displayed in the visualizations." He wants the aggregate and a named case together: "the addition of individual stories to exemplify the patterns."

**Chart types.** Pluralist, with several types in one narrative and annotation connecting them. The one recorded aversion is a section title in *The Functional Art*, "The Bubble Plague" (page 39), outside the sample and unread. Its chapter, "Forms and Functions: Visualization as a Technology," runs "What Shape Should My Data Have?", "The Origins of 'Form Follows Function'", "Functions Constrain Forms", "The Bubble Plague", then "More Flexible Than It Seems." Read as titles only, the sequence argues that purpose constrains form and that bubbles get reached for when the purpose is undecided.

**Density.** He rejects minimalism, which splits him from the other practitioners here. *The Functional Art* has a section titled "Is All 'Chartjunk' Junk?" (page 64), between "Minimalism and Efficiency" and "Fun and Functionality," right after "Engineers vs. Designers: Edward Tufte and Nigel Holmes." He also warns against the opposite error in "Graphics Don't 'Simplify' Information" (page 78) and "Seek Depth" (page 76). Only the titles were read.

**The tell.** In descending confidence:

1. Sentences on the figure interpreting the plot's regions, a labeled reference value, and direct labels on everything.
2. A named individual case alongside the aggregate pattern.
3. Excel plus Illustrator. On his DVD lesson: "I also explain how I developed the chart on the front cover of *The Functional Art*. You will see how **I use Microsoft Excel and Adobe Illustrator**, and why I call my approach 'low-tech visualization.'" [Wilke](claus-wilke.md) writes that "interactive plot programs are a bad idea" and that Excel "is not recommended for figure preparation." The positions are incompatible, and this wiki has no evidence on the question, only the two authorities.

**Review rubrics.** His transferable artifact is two rubrics, known here at name and page level only.

- **The Visualization Wheel** (*The Functional Art*, chapter 3, page 50): Abstraction-Figuration, Functionality-Decoration, Density-Lightness, Multidimensionality-Unidimensionality, Originality-Familiarity, Novelty-Redundancy. Its structure places a graphic on each axis by audience and purpose rather than scoring it against a fixed ideal.
- **The Five Qualities** (*The Truthful Art*, chapter 2): Truthful (45), Functional (50), Beautiful (53), Insightful (59), Enlightening (60). A widely quoted line about truthfulness being "paramount among these five" is not in the sample and remains unverified ([sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md)).

## What they would say about a figure first

Whether it is true, in a statistical sense. Chapter 4 of *The Truthful Art* opens: "Here's a dirty little secret about data: it's always noisy and uncertain," because "Data always vary randomly because the object of our inquiries, nature itself, is also random." His worked example is weighing himself daily for six weeks. The downward trend "only becomes visible when I display more than five or six days in a row. If I zoom in too much to the chart and just pay attention to two or three days, I'd be fooled into thinking that the noise in the data means something." He also asks where the numbers came from: "reporting on a study after reading just its abstract is dangerous."

Then he asks what the reader is meant to understand: "The role of an information architect is to anticipate this process and generate order before people's brains try to do it on their own."

In a November 2023 blog post he quotes Federica Fragapane on technical criticism displacing engagement with a subject: "data on rights violations take second place to the fact that 'it should have been a bar chart'." His comment: "**I've been the type of person that Federica describes. We must strive to do better.**" [Knaflic](cole-nussbaumer-knaflic.md) opens on what the audience should do, and [Schwabish](jonathan-schwabish.md) on ranking a figure's elements by ink weight. Cairo opens on whether the figure is true, then on whether he is being fair to it.

## Works, and where they sit in this wiki

- ***The Truthful Art*** (2016): [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md), with the four-part structure, the five qualities at name level, chapter 4's quotes, and two unverified claims the project carries.
- ***The Functional Art*** (2012): no page. Its unread chapters 2 and 3, the chartjunk discussion and the Visualization Wheel, bear on the chartjunk section of [refutations.md](../refutations.md) and on [studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md). Much of the book is interviews. The much-quoted "annotation layer" passage in the sample is John Grimwade speaking, not Cairo.
- ***How Charts Lie*** (2019): `not-reached`, a gap the [main README](../README.md) names. It bears on the truncation, inverted-axis and map-projection topics.
- ***The Art of Insight*** (2023): not covered. Conversations with designers, which he calls "my most personal book to date" and "much more personal and idiosyncratic" than the others. Likely the best source on how practitioners decide, unlikely to ground inventory topics.
- **His blog**, `thefunctionalart.com`: not covered. Its post labels are Annotations, Critique, Data Journalism, Data storytelling, Graphical literacy.

## Links

- [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md): the book page
- [refutations.md](../refutations.md): the chartjunk record his unread chapter 3 argues into
- [studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) and [studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md): the evidence on embellishment
- [claus-wilke.md](claus-wilke.md): the unresolved disagreement about figure-production toolchains
- [cole-nussbaumer-knaflic.md](cole-nussbaumer-knaflic.md): the contrast in first questions
