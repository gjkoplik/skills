---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Jonathan Schwabish

**What they are known for.** An economist who turned chart redesign into a teachable procedure for researchers, first in a 2014 *Journal of Economic Perspectives* article that walks eight real published graphs through a before-and-after, then in four books including *Better Data Visualizations* (2021) and *Data Visualization in Excel* (2023). He is also the author of the **Graphic Continuum**, a chart-type poster, and a Senior Fellow at the Urban Institute.

**The Urban Institute style guide, which this wiki treats as its broadest single source, is not independent of him.** That is the claim the evidence supports, and it is deliberately weaker than authorship: the guide carries no byline, but names him as its sole point of contact ("Contact Jon Schwabish", `jschwabish@urban.org`, verified on the live page 2026-08-25). **Consequence for citation: [urban-institute.md](../sources/urban-institute.md) and his own work are one voice, not two.** Corroboration counts that list both are wrong by one; one such error has been corrected in [schwabish.md](../sources/schwabish.md). **Non-independence is enough for that consequence and is all that is established**; see the Works section below, which declines to claim he wrote it.

His reach through this corpus is wider than any other single person as a result: the Urban guide, the Graphic Continuum (which the [FT Visual Vocabulary](../sources/ft-visual-vocabulary.md) credits as its inspiration), the JEP article, and four books.

**How this was read.** `primary-read` for the 2014 article. Retrieved 2026-08-23. The full 26-page JEP article was downloaded with `curl` from `pubs.aeaweb.org` and text-extracted locally with `pdftotext -layout`; every quote below comes from that file. Six pages of it were separately rendered to PNG at 100dpi and their pixel colors measured with PIL, which is where the palette numbers come from. His biography line comes from his own `policyviz.com/about` page, fetched and stripped locally.

**His four books were not opened.** Anything below that touches them is marked `secondary-only` inline.

**What they are good for.** Come back here with: *this figure is already published and it is bad, what specifically do I change*. He is the only person in this section who works almost entirely in **diffs**. The JEP article does not give you principles and leave you to apply them; it gives you an original, a redesign, and a numbered account of what moved and why. That makes him the most directly copyable of the five.

**What they do not settle.** No evidence of his own; the 2014 article cites Few, Ware, Cleveland and others but runs nothing. The audience is researchers publishing static figures in reports and journals, so there is little on interaction beyond a taxonomy, nothing on uncertainty visualization, and nothing on production pipelines. And his own position on decluttering appears to have moved between 2014 and 2021 in a direction this page can only report secondhand; see below.

---

## "In the style of Jonathan Schwabish" means, concretely

**How much of this is inference.** Very little for the 2014 work. He redesigns eight figures and narrates every decision, so the profile is mostly his own reasoning quoted back. The **palette numbers are measurement**, from six rendered pages of that one article. Whether that palette generalizes past a black-and-white-printed economics journal is not established here, and he explicitly says the constraint shaped it.

**Palette habits.** Two hues. That is not a summary, it is a count.

Across the six rendered figure pages I sampled, **98.9% of saturated pixels fall into two hue bands**: 20 to 40 degrees (orange, 25.0%) and 200 to 220 degrees (blue, 73.9%). Nothing else clears half a percent. No green, no red, no purple, anywhere.

The recurring exact values are `#17375E` (dark navy) and `#E36D25` (orange), with tints `#788BA2` and `#FAB17B` used for de-emphasis. Both base colors are stock Microsoft Office theme colors, which fits, since he says the redesigns "were constructed in Excel and required slight variations from the program's default settings."

The reason for exactly this pair is stated, and it is a production constraint rather than a taste: "The print JEP does not use color, but **all graphs that use color in the electronic version of the JEP are designed to work in greyscale for print readers.**" Orange and dark blue separate in luminance as well as hue, so they survive the conversion. He annotates one figure with the mapping directly: "the color contrast (or what appears as different shades of grey in the black-and-white printed version) identifies which categories increased over time (blue; darker) and those that declined (orange; lighter)."

If you want one sentence for a style guide: **blue and orange, chosen so the figure still reads in grayscale, with tints of the same two hues doing the de-emphasis.**

**Title and annotation voice.** A rigid and reproducible header block, top-left:

1. **Title above the graph**, left-aligned. His reason is reading order: "some publishers place titles below graphs even though readers tend to start reading from the top left, move down along the left margin, and then move to the right."
2. **Units on the next line, in parentheses.** Literally `(Percent)`, `(Income in thousands)`. This replaces the rotated y-axis title, which he does not want you to have: "there is nothing inherently wrong with using rotated text on the vertical axis, but it does require readers to turn the page sideways or tilt their heads."
3. **Legend integrated into that block**, or gone. "Integrated legends, right below the title, directly on the chart, or at the end of a line, are more accessible." In practice the series names end up as colored words directly under the units line, or as labels at the end of each line.

He spells out abbreviations rather than making the reader hunt: "what do AO, NC, WE, and SS mean in the figure? In this article, these terms are explained on the third and fourth pages, 15 pages before this figure is presented. It seems unfair to ask a reader to search the paper to decode the meaning of those labels."

He also strips redundant symbols with a precision that reads as a tic, and it is a good one to imitate: "the y-axis labels and percentage signs are redundant and add clutter (**there are 28 percentage signs in all!**)."

Annotation density is moderate. He labels the points he discusses and lets the rest go quiet. On a scatter with a hundred country codes: "I eliminated all labels other than those for the five countries under discussion, which I spelled out, and I made the five data points darker, thus deemphasizing the other points but still showing the important information."

**Chart-type preferences and aversions.**

Reaches for: **small multiples** (his first redesign move on a four-series line chart, and his fix for spaghetti), **horizontal bars** whenever category labels are long, **slope charts**, **paired columns**, **stacked bars for two-period part-to-whole**, and the occasional less-common form he expects readers to grow into. That last is a real position: "scatterplots, not so long ago a novelty in mainstream publishing, now appear regularly. Just as our text literacy can expand with experience and exposure, so can our graphic literacy."

Refuses: **3D**, flatly, and he demonstrates the problem rather than asserting it. On a 3D column labeled 6 percent: "No point of the column touches the gridline for that value... most readers will perceive the actual value of the column as less than 6 percent." **Non-zero bar baselines**: "a first rule is to start the chart at zero." **Mixed encodings for like data**, which is the diagnosis he leads with on the OECD chart: "the same kinds of data are plotted using different types of encoding so that it is difficult to compare location (diamonds) with length (bars)."

On **pie charts** he is more careful than his reputation. He walks the standard objections, then makes an argument most pie critics skip: labeling every slice "results in what amounts to two sets of information: the labels and the values for the slices... This defeats the very purpose of the chart." And he grants the form its real job, that a pie exists "to individually compare each part to the whole," which is what his mini-pie small-multiple figure demonstrates.

**Density and restraint.** Restrained but not minimal, and the rule is about **relative weight, not removal**. His single sharpest observation is that clutter usually wins the ink contest against the data: "a graph should emphasize the data, but **the darkest and thickest line on these graphs is the 0 percent gridline.** Your eye is immediately drawn to that thick, horizontal gridline rather than to the important parts of the graph."

The redesign move that follows is not "delete the gridlines." It is a hierarchy: "The darkest line now shows the data... The gridlines have been lightened, but leaving the 0 percent gridline slightly darker so it can provide a baseline for the series that dip below zero." He does delete axes when they have stopped working, and says so as a judgment rather than a rule: "the (subjective) decision to omit the y-axis; the usefulness of the y-axis is doubtful with data labels placed on top of each column." He also concedes the cost each time, which is unusual: "One potential shortcoming of the redesign is the lack of vertical gridlines."

His three principles, stated as the spine of the whole article: **show the data, reduce the clutter, integrate the text and the graph.** The third is the one nobody else in this section names as a top-level principle, and it is aimed at a specific failure mode he calls the "slideshow effect," in which the writer narrates the text elements that appear in the graph.

**The tell.** A left-aligned title stack with a parenthesized unit line under it, a legend that has climbed into that stack or run off the end of a line, no rotated axis title, no percent signs on the tick labels, gridlines lighter than the data with one darker reference line at zero, and everything in one blue and one orange. If you also see the same dataset presented twice in a *before and this* pair, that is the format he invented for this purpose.

## What they would say about your figure first

He would look for what your eye lands on and check whether that thing is data. That is his opening diagnosis on the very first figure he redesigns, and it is a mechanical test you can run in a second: rank every element by ink weight and see whether a gridline, a frame, or a tick mark outranks the series. Then he would count the redundant marks, the percent signs, the repeated axis labels, the abbreviations you have not spelled out, and the legend sitting off to the right. He would ask whether the reader has to move their eyes anywhere to decode a label, because his third principle is that text and graph should be one object. Then, and only then, chart type, where he would probably not tell you the type is wrong so much as ask whether two different encodings are competing to say the same thing. And he would keep saying which of his calls are subjective: he flags "line thickness, series order, axis label style" as taste before he begins, and then flags individual choices as subjective as he makes them. Compare [Knaflic](cole-nussbaumer-knaflic.md), who would stop you before the figure to ask what the audience is supposed to do. Schwabish assumes you have a published figure and a paper deadline, and starts editing.

**A caveat about which Schwabish you are imitating.** [Muth](lisa-charlotte-muth.md) quotes *Better Data Visualizations* (2021) as saying that "bar charts and line charts and pie charts [...] are often boring" and advising readers that "our job is to encourage people to read and use [...] graph[s], even if we 'violate' perceptual rules that we know will hamper someone's ability to make the most accurate conclusions." Those quotes are **`secondary-only`**: they come from her post, not from the book, which nobody here has opened. If they are accurate in context, the 2021 Schwabish is willing to trade accuracy for engagement in a way the 2014 declutterer is not, and a style profile built only on the JEP article will miss it. Somebody should open the book.

## Works, and where they sit in this wiki

- **"An Economist's Guide to Visualizing Data,"** *Journal of Economic Perspectives* 28(1), 2014, pages 209 to 234. **No page in this wiki covers it**, and it is open access at `pubs.aeaweb.org`. It is the source for everything above and arguably deserves its own source page.
- **The Urban Institute Data Visualization Style Guide** has a page at [sources/urban-institute.md](../sources/urban-institute.md) and is the most rule-shaped style guide in the canon. He is a Senior Fellow at Urban and works on data visualization there. **This page does not claim he authored the guide**; that relationship was not verified from a primary source and the guide is published institutionally.
- ***Better Presentations*** (2016), ***Elevate the Debate*** (2020), ***Better Data Visualizations*** (2021), ***Data Visualization in Excel*** (2023): **none covered, none opened.** *Better Data Visualizations* is the obvious gap, both as the current statement of his position and because of the tension flagged above.
- **The Graphic Continuum** and the PolicyViz DataViz Catalog are chart-chooser artifacts and are **not covered**. They would sit next to [sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md).
- **"Ten Guidelines for Better Tables,"** *Journal of Benefit-Cost Analysis*, is not covered and was not reached in this pass.

One cross-link: he is thanked in the acknowledgments of [Wilke's](claus-wilke.md) *Fundamentals of Data Visualization* as one of the people who commented on the book.

## Links

- [sources/urban-institute.md](../sources/urban-institute.md), the style guide from the organization he works at
- [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md), for the evidence behind the pie argument he summarizes
- [concepts/channels.md](../concepts/channels.md), the perceptual ranking his "location versus length" diagnosis leans on
- [claus-wilke.md](claus-wilke.md), the closest neighbor on defaults
- [lisa-charlotte-muth.md](lisa-charlotte-muth.md), who argues with him in print about whether simple charts are boring
