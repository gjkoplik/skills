---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Jonathan Schwabish

**What they are known for.** An economist who made chart redesign a teachable procedure for researchers, starting with a 2014 *Journal of Economic Perspectives* article that walks eight published graphs through a before-and-after. Four books followed, including *Better Data Visualizations* (2021) and *Data Visualization in Excel* (2023). He made the **Graphic Continuum**, a chart-type poster, with Severino Ribecca, and is a Senior Fellow at the Urban Institute.

The Urban Institute style guide is not independent of him. It has no byline but names him as its sole contact ("Contact Jon Schwabish", `jschwabish@urban.org`, on the live page). That shows non-independence, not authorship, and makes [urban-institute.md](../sources/urban-institute.md) and [schwabish.md](../sources/schwabish.md) one voice in a corroboration count. The [FT Visual Vocabulary](../sources/ft-visual-vocabulary.md) credits the Graphic Continuum as its inspiration, so his reach through this corpus is wider than any other single person's.

**How this was read.** `primary-read` for the 2014 article, downloaded with `curl` from `pubs.aeaweb.org` and extracted locally with `pdftotext -layout`. Every quote comes from that file. Six of its pages were rendered to PNG at 100dpi and their pixel colors measured with PIL for the palette numbers. The biography line is from `policyviz.com/about`, fetched and stripped locally. The books were not opened, and anything touching them is marked `secondary-only`.

**What they are good for.** What to change in a bad published figure. He works in diffs: an original, a redesign, and a numbered account of what moved and why.

**What they do not settle.** He has no evidence of his own. The article cites Few, Ware, Cleveland and others and runs no experiment. It targets researchers publishing static figures, so there is little on interaction beyond a taxonomy and nothing on uncertainty or production pipelines. His position on decluttering may have moved by 2021 (below).

---

## "In the style of Jonathan Schwabish" means, concretely

Mostly his own narrated reasoning, quoted back. The palette is measured on one article and may not generalize past a journal printed in black and white.

**Palette habits.** Two hues. On the six rendered pages, 98.9% of saturated pixels fall in two bands: 20 to 40 degrees (orange, 25.0%) and 200 to 220 degrees (blue, 73.9%). Nothing else clears half a percent. The recurring values are `#17375E` (dark navy) and `#E36D25` (orange), with tints `#788BA2` and `#FAB17B` for de-emphasis. Both base colors are stock Microsoft Office theme colors, and the redesigns "were constructed in Excel and required slight variations from the program's default settings."

The pair is a production constraint: "The print JEP does not use color, but **all graphs that use color in the electronic version of the JEP are designed to work in greyscale for print readers.**" Orange and dark blue differ in luminance, so they survive grayscale. One figure states the mapping: "the color contrast (or what appears as different shades of grey in the black-and-white printed version) identifies which categories increased over time (blue; darker) and those that declined (orange; lighter)."

**Title and annotation voice.** A fixed header block, top-left. The title sits above the graph, left-aligned, because "some publishers place titles below graphs even though readers tend to start reading from the top left, move down along the left margin, and then move to the right." Units go on the next line in parentheses, literally `(Percent)`, replacing the rotated y-axis title: "there is nothing inherently wrong with using rotated text on the vertical axis, but it does require readers to turn the page sideways or tilt their heads." The legend joins that block or disappears: "Integrated legends, right below the title, directly on the chart, or at the end of a line, are more accessible."

Abbreviations are spelled out: "what do AO, NC, WE, and SS mean in the figure? In this article, these terms are explained on the third and fourth pages, 15 pages before this figure is presented. It seems unfair to ask a reader to search the paper to decode the meaning of those labels." Redundant symbols go: "the y-axis labels and percentage signs are redundant and add clutter (**there are 28 percentage signs in all!**)." He labels only the points he discusses: "I eliminated all labels other than those for the five countries under discussion, which I spelled out, and I made the five data points darker, thus deemphasizing the other points but still showing the important information."

**Chart-type preferences and aversions.** He reaches for small multiples (his fix for spaghetti), horizontal bars for long labels, slope charts, paired columns, and stacked bars for two-period part-to-whole. He expects readers to learn less common forms: "scatterplots, not so long ago a novelty in mainstream publishing, now appear regularly. Just as our text literacy can expand with experience and exposure, so can our graphic literacy."

He refuses 3D: "No point of the column touches the gridline for that value... most readers will perceive the actual value of the column as less than 6 percent." He refuses non-zero bar baselines: "a first rule is to start the chart at zero." He refuses mixed encodings for like data: "the same kinds of data are plotted using different types of encoding so that it is difficult to compare location (diamonds) with length (bars)."

On pies he argues that labeling every slice "results in what amounts to two sets of information: the labels and the values for the slices... This defeats the very purpose of the chart." He grants the form its job, which is "to individually compare each part to the whole," and shows it with small-multiple mini-pies.

**Density and restraint.** Restrained, not minimal, and governed by relative weight rather than removal. Clutter often outweighs the data: "a graph should emphasize the data, but **the darkest and thickest line on these graphs is the 0 percent gridline.** Your eye is immediately drawn to that thick, horizontal gridline rather than to the important parts of the graph." The fix is a hierarchy: "The darkest line now shows the data... The gridlines have been lightened, but leaving the 0 percent gridline slightly darker so it can provide a baseline for the series that dip below zero." He drops an axis as a stated judgment: "the (subjective) decision to omit the y-axis; the usefulness of the y-axis is doubtful with data labels placed on top of each column." He names the costs: "One potential shortcoming of the redesign is the lack of vertical gridlines."

His three principles are show the data, reduce the clutter, and integrate the text and the graph. The third targets the "slideshow effect," in which the writer narrates the text elements that appear in the graph.

**The tell.** A left-aligned title stack with a parenthesized unit line under it, a legend that has climbed into that stack or run off the end of a line, no rotated axis title, no percent signs on the tick labels, gridlines lighter than the data with one darker reference line at zero, and everything in one blue and one orange. The same dataset shown twice as a before-and-after pair is the format he invented for this purpose.

## What they would say about a figure first

He would first check whether the heaviest ink is data, or whether a gridline, frame or tick mark outranks the series. Then he would count redundant marks and look for labels that send the eye elsewhere to decode them. Chart type comes last, and the question there is whether two encodings compete to say the same thing. He names "line thickness, series order, axis label style" as taste before starting and flags subjective calls as he makes them. [Knaflic](cole-nussbaumer-knaflic.md) starts from what the audience should do. Schwabish starts from a published figure and a paper deadline.

## Which Schwabish is being imitated

[Muth](lisa-charlotte-muth.md) quotes *Better Data Visualizations* (2021) as saying that "bar charts and line charts and pie charts [...] are often boring" and that "our job is to encourage people to read and use [...] graph[s], even if we 'violate' perceptual rules that we know will hamper someone's ability to make the most accurate conclusions." Those quotes are `secondary-only`, taken from her post, not from the unopened book. If they are accurate in context, the 2021 Schwabish trades accuracy for engagement in a way the 2014 article does not, and a profile built on the article alone misses it.

## Works, and where they sit in this wiki

- "An Economist's Guide to Visualizing Data," *Journal of Economic Perspectives* 28(1), 2014, pages 209 to 234, open access at `pubs.aeaweb.org`. No page in this wiki covers it. It is the source for everything above.
- The Urban Institute Data Visualization Style Guide: [sources/urban-institute.md](../sources/urban-institute.md), the most rule-shaped style guide in the canon. It is published institutionally. His authorship was not verified from a primary source, and this page does not claim it.
- *Better Presentations* (2016), *Elevate the Debate* (2020), *Better Data Visualizations* (2021), *Data Visualization in Excel* (2023): none covered or opened. *Better Data Visualizations* is the largest gap, given the tension above.
- The Graphic Continuum and the PolicyViz DataViz Catalog: chart choosers, not covered. They would sit beside [sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md).
- "Ten Guidelines for Better Tables," *Journal of Benefit-Cost Analysis*: not reached.

[Wilke's](claus-wilke.md) *Fundamentals of Data Visualization* thanks him in its acknowledgments as a commenter on the book.

## Links

- [sources/urban-institute.md](../sources/urban-institute.md): the style guide from the organization he works at
- [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md): the evidence behind the pie argument he summarizes
- [concepts/channels.md](../concepts/channels.md): the perceptual ranking his "location versus length" diagnosis leans on
- [claus-wilke.md](claus-wilke.md): the closest neighbor on defaults
- [lisa-charlotte-muth.md](lisa-charlotte-muth.md): argues with him in print about whether simple charts are boring
