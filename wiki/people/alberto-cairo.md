# Alberto Cairo

**What they are known for.** Four books that between them taught a generation of journalists and researchers to argue about graphics: *The Functional Art* (2012), *The Truthful Art* (2016), *How Charts Lie* (2019), and *The Art of Insight* (2023). He is a professor at the University of Miami, a former newsroom graphics director in Spain and Brazil, and co-editor with Tamara Munzner of CRC Press's visualization book series.

**Status: `primary-read`, partial.** Retrieved 2026-08-23, all locally extracted, nothing from a fetch summary:

- **The Functional Art**, Pearson's 46-page sample PDF (`ptgmedia.pearsoncmg.com/images/9780321834737/samplepages/0321834739.pdf`), `curl` plus `pdftotext -layout`. Contains the full contents page, the complete introduction, **chapter 1 in full**, the About-the-DVD section, and the index.
- **The Truthful Art**, Peachpit's 46-page sample. Contents, preface, **chapter 4 in full**, index. This is the same file the existing [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md) page was built from.
- **His blog**, `thefunctionalart.com`, front page fetched and stripped to text. This is where the 2023 material comes from, including a preamble to *The Art of Insight* that he published himself in draft.

***How Charts Lie* remains `not-reached`,** as it was before. It was not attempted here beyond noting that the results for it are dominated by pirated copies and AI summary sites, none of which are usable.

**What they are good for.** Come back here with: *am I over-reading this data, and would I be comfortable if someone checked*. He is the only author in this section who spends real pages on conjecture, study quality, sample variation, standard error, and significance versus effect size. Bring him the question of whether your figure is **honest**, not whether it is clean.

**What they do not settle.** Chartcraft detail. He gives less usable instruction on color, type, and layout than any of the other four, and he would probably say so himself. And, bluntly for the purposes of this section: **he is the hardest of the five to imitate**, for reasons set out below.

---

## "In the style of Alberto Cairo" means, concretely

**How much of this is inference, and a warning.** This is the weakest style profile on these pages, and the weakness is structural rather than a retrieval failure. Cairo's published work is overwhelmingly **about other people's graphics.** He is a critic, a teacher, an interviewer, and an editor. *The Art of Insight* is a book of conversations with designers; *The Functional Art* contains long profiles of other practitioners; *How Charts Lie* is written for readers, not makers. So there is far less Cairo-made output to profile than there is Cairo doctrine.

What follows rests on **one figure of his own** that could be examined here, the cover chart of *The Functional Art*, read through the sample PDF's text layer. One figure is not a style. Everything else in this section is his stated method, and it is labeled as stated method.

**Palette habits.** **Not established.** Nothing retrieved here supports a claim about his palette, and the one figure available was read as text, not measured. Do not invent one. If you want a defensible color position from this canon, take [Muth's](lisa-charlotte-muth.md) or [Wilke's](claus-wilke.md).

The one adjacent thing he does state, from the *Truthful Art* contents and confirmed at name level only, is that color sits inside his **Beautiful** quality, which he places third of five behind Truthful and Functional. That ordering is the position, not a palette.

**Title and annotation voice.** Heavily annotated, and this is the best-grounded part of the profile because his cover chart is built from annotation.

The chart pairs each US state's share of adults with a BA or higher against its obesity rate, as two labeled columns of state abbreviations with connecting geometry. Its text layer contains, besides the fifty state labels twice over:

- Two block annotations naming what each region of the chart means: "States with a larger percentage of people with higher education than with obesity," and "States with a larger percentage of obese people than of people with a higher education."
- An explicit reference callout: "the US average / 27.2% BA or higher / 27.0% Obese."

So: **every point directly labeled, no legend, a stated reference value, and prose blocks that tell the reader what a region of the plot means rather than leaving them to derive it.** That last move is the imitable one. He is not annotating outliers; he is annotating the *interpretation of the geometry.*

His blog confirms this is what he values in other people's work. Reviewing an Eldiario.es piece in December 2023, what he singles out is "the combination of different types of charts, dot maps, scatter plots, stacked bar graphs, the effective annotations and highlights that emphasize the main points of the narrative, the use of color, and the addition of individual stories to exemplify the patterns displayed in the visualizations."

Note **"the addition of individual stories to exemplify the patterns."** He wants the aggregate and a named case, together. That is a Cairo preference you can act on.

**Chart-type preferences and aversions.** Pluralist to a fault, and there is one recorded aversion, from a chapter title in *The Functional Art*: "The Bubble Plague" (page 39). The chapter is not in the sample, so what he says inside it is **unread**. The chapter it sits in is called "Forms and Functions: Visualization as a Technology," and its section list runs "What Shape Should My Data Have?", "The Origins of 'Form Follows Function'", "Functions Constrain Forms", then "The Bubble Plague", then "More Flexible Than It Seems." Read as a sequence, that is an argument that the *purpose* constrains the form and that bubbles get reached for when the purpose has not been decided.

His positive preference, from the Eldiario praise above and from the cover chart, is for **combinations**: several chart types in one narrative, with annotation carrying the connective tissue.

**Density and restraint.** He explicitly refuses the minimalist position, and this is where he splits from everyone else in this section. His *Functional Art* contents page carries a section titled "Is All 'Chartjunk' Junk?" (page 64), sitting between "Minimalism and Efficiency" and "Fun and Functionality," and immediately after a section called "Engineers vs. Designers: Edward Tufte and Nigel Holmes." **Section titles only; the arguments were not read.** But the structure of the chapter is unambiguous about where the question is being posed. He also warns against the opposite error, in a section titled "Graphics Don't 'Simplify' Information" (page 78), and one called "Seek Depth" (page 76).

**The tell.** Three things, in descending confidence.

1. **An annotated interpretation of the plot's regions**, written as sentences on the figure, plus a labeled reference line or average value, plus direct labels on everything.
2. **A named individual case sitting alongside the aggregate pattern.**
3. **Excel plus Illustrator.** He says this outright, describing his own DVD lesson: "I also explain how I developed the chart on the front cover of *The Functional Art*. You will see how **I use Microsoft Excel and Adobe Illustrator**, and why I call my approach 'low-tech visualization.'" That is a direct collision with [Wilke](claus-wilke.md), who writes that "interactive plot programs are a bad idea" and that Excel "is not recommended for figure preparation." Both of them are stating a considered position. They are incompatible, and this wiki has no evidence on the question, only two authorities.

**The review instruments, which are the more useful thing to imitate.** Cairo's real transferable artifact is not a look, it is two rubrics.

- **The Visualization Wheel** (*The Functional Art*, chapter 3, page 50), six named axes: Abstraction-Figuration, Functionality-Decoration, Density-Lightness, Multidimensionality-Unidimensionality, Originality-Familiarity, Novelty-Redundancy. **Names and page numbers are primary, from the contents page. The definitions were not read.** The point of the wheel, from its structure, is that a graphic is positioned on each axis by its audience and purpose rather than scored against a fixed ideal.
- **The Five Qualities** (*The Truthful Art*, chapter 2): Truthful (45), Functional (50), Beautiful (53), Insightful (59), Enlightening (60). Same status, names and pages only. See [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md), which also records that a widely quoted line about truthfulness being "paramount among these five" **could not be found anywhere in the sample** and remains unverified.

## What they would say about your figure first

He would ask whether it is true, and he would mean something specific and statistical by that. Not "did you mislabel the axis" but: how much of what I am looking at is noise? His chapter 4 opens on it. "Here's a dirty little secret about data: it's always noisy and uncertain," and the reason is not sloppiness but the world: "Data always vary randomly because the object of our inquiries, nature itself, is also random." He would want to know your sample, your uncertainty, and whether you have zoomed in far enough to be fooled. His own worked example is weighing himself daily for six weeks: the downward trend "only becomes visible when I display more than five or six days in a row. If I zoom in too much to the chart and just pay attention to two or three days, I'd be fooled into thinking that the noise in the data means something." And he would ask where the numbers came from, because he is caustic about the shortcut: "reporting on a study after reading just its abstract is dangerous."

Then, and this is what distinguishes him from a pure statistician, he would ask what the reader is supposed to *understand*, because his frame for the whole enterprise is order-making: "The role of an information architect is to anticipate this process and generate order before people's brains try to do it on their own."

**One thing he has publicly said he would try not to do.** In a November 2023 blog post he quotes Federica Fragapane on the pattern of technical criticism arriving in place of engagement with a subject: "data on rights violations take second place to the fact that 'it should have been a bar chart'." His own comment on it is one line. "**I've been the type of person that Federica describes. We must strive to do better.**" Anyone imitating Cairo's critical voice should imitate that too, and not just the rubrics. Compare [Knaflic](cole-nussbaumer-knaflic.md), who opens on what the audience should do, and [Schwabish](jonathan-schwabish.md), who opens by ranking your figure's elements by ink weight. Cairo opens on whether the thing is *true*, and then on whether he is being fair to it.

## Works, and where they sit in this wiki

- ***The Truthful Art*** (2016) has a page at [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md), covering the four-part structure, the five qualities at name level, chapter 4's verbatim quotes, and the two claims the project carries that are still unverified. Read it there.
- ***The Functional Art*** (2012) has **no page in this wiki.** This page is the first thing here built on its sample. Its chapters 2 and 3, the chartjunk discussion and the Visualization Wheel, are the highest-value unread material about Cairo in the canon, and they bear directly on [refutations.md](../refutations.md)'s chartjunk section and on [studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md).
- ***How Charts Lie*** (2019) is **`not-reached`**, and the [main README](../README.md) already names it as a structural gap: it would sharpen the truncation, inverted-axis and map-projection topics. Still true.
- ***The Art of Insight*** (2023) is **not covered anywhere.** It is a book of conversations with designers rather than a rules book, and he describes it himself as "my most personal book to date" and "much more personal and idiosyncratic" than the others. It is unlikely to ground inventory topics and likely to be the best source on how working practitioners actually decide things.
- **His blog**, `thefunctionalart.com`, is not covered. Its post labels are themselves a preference list: Annotations, Critique, Data Journalism, Data storytelling, Graphical literacy.

One attribution warning for anyone mining *The Functional Art*: a large part of the book is **interviews**. The much-quoted "annotation layer" passage in the sample, for instance, is **John Grimwade speaking**, not Cairo. Check the speaker before attributing.

## Links

- [sources/cairo-truthful-art.md](../sources/cairo-truthful-art.md), the book page
- [refutations.md](../refutations.md), the chartjunk record his unread chapter 3 argues into
- [studies/bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) and [studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md), the evidence on embellishment
- [claus-wilke.md](claus-wilke.md), for the direct and unresolved disagreement about figure-production toolchains
- [cole-nussbaumer-knaflic.md](cole-nussbaumer-knaflic.md), for the contrast in first questions
