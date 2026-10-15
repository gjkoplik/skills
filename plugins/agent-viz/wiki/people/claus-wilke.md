---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Claus Wilke

**What they are known for.** *Fundamentals of Data Visualization* (O'Reilly, 2019), the broadest single chartcraft reference in this canon, free at [clauswilke.com/dataviz](https://clauswilke.com/dataviz/). He also wrote R packages that shape many scientific figures, including `cowplot`, `ggridges` and `ggtext`.

**How this was read.** Eleven chapter pages of the free book were pulled with `curl` and stripped to text locally; the quotes are re-extracted from that HTML. Four rendered figure PNGs were downloaded and their pixel colors measured with PIL. His homepage supplied the affiliation line.

**What they are good for.** *What should the defaults be, and can each one be defended*. He documents his house style with reasons, and alone in this set treats reproducibility of the figure pipeline as a quality question.

**What they do not settle.** Almost nothing here is evidence. He runs no experiments, cites few, and his preface warns against treating him as gospel. His accessibility coverage stops at color-vision deficiency. On grids he declines, in the text, to have a single house look.

---

## "In the style of Claus Wilke" means, concretely

**How much of this is inference.** Little. Chapters 4, 19, 22, 23 and 24 state his defaults in his own words. Where his output was checked, the measurement is given.

**Palette habits.** "My preferred qualitative color scale, which I use extensively throughout this book" is Okabe-Ito, with hex codes in Table 19.1:

| Name | Hex |
|---|---|
| orange | `#E69F00` |
| sky blue | `#56B4E9` |
| bluish green | `#009E73` |
| yellow | `#F0E442` |
| blue | `#0072B2` |
| vermilion | `#D55E00` |
| reddish purple | `#CC79A7` |
| black | `#000000` |

Eight colors, matching his cap: "you should probably not color-code more than eight different items in a plot anyways." The saturated pixels of `popgrowth-US-1.png` (chapter 4) sample to hues of 37.6°, 204.4°, 157.3° and 56.4°, against Okabe-Ito's stated 41°, 202°, 164° and 56°. The rendered fills (`#DE8E08`, `#48A4E3`, `#138F60`, `#ECE134`) are slightly darker, consistent with alpha and PNG rendering.

Sequential ramps should be perceptually uniform and follow "color gradients that can be seen in the natural world, such as dark red, green, or blue to light yellow." Dark yellow to light blue "looks unnatural." Diverging scales must be balanced around a light midpoint, "so that the progression from light colors in the center to dark colors on the outside is approximately the same in either direction."

For highlighting he uses **accent scales**, not gray-plus-one. Baseline categories keep a little color, and full gray is his "easy remedy," not his first move:

> "Notice how drab the baseline colors are... It is easy to make the mistake of using baseline colors that are too colorful, so that they end up competing for the reader's attention against the accent colors."

**Title and annotation voice.** The title is an assertion and opens the caption. From chapter 22:

> "It does not begin with 'This figure shows how corruption is related to human development.' The first part of the caption is always the title, not a description of the contents of the figure."

> "A title does not have to be a complete sentence, though short sentences making a clear assertion can serve as titles."

Captions run asserting sentence, decoding notes, then a `Data source:` trailer (13 times in chapter 23, 12 in chapter 29). Explanation lives in the caption, a scientific-publishing habit, not on the plot. He labels directly where geometry allows (chapter 20 covers designing figures without legends) but does not lay prose over the data region as [Muth](lisa-charlotte-muth.md) does.

**Chart-type preferences and aversions.** Chapters 25 and 26 refuse by title: avoid line drawings, don't go 3D. Chapter 10 has a section called "A case for pie charts," against most style guides in this wiki. His directory of visualizations is organized by data relationship, and he reaches for ECDFs, q-q plots, ridgelines and hypothetical outcome plots more readily than any business-communication author here.

**Density and restraint.** The middle. Chapter 23: "Both overloading a figure with non-data ink and excessively erasing non-data ink can result in poor figure design." An over-stripped figure is "bad" just as an over-inked one is. "I prefer minimal, light grids on a white background." He draws them "orthogonally to direction along which the numbers of interest vary" at major ticks only. His scatter-plot default is "an open background grid and no axis lines or frame around the plot panel," which "conveys to the reader that range of possible data values extends beyond the axis limits." He declines a fixed grid rule:

> "Throughout this book I am using a variety of different grid styles, to highlight that there isn't necessarily one best choice."

The one rule he states maximally: "Pay attention to your axis labels, axis tick labels, and other assorted plot annotations. Chances are they are too small."

**The tell.** An Okabe-Ito hue where a ggplot2 default would be. A caption that opens with a claim and ends `Data source:` something. Figures labeled with their own verdict, which no one else in the canon does: chapter 1 defines ugly, bad and wrong, and the book stamps figures with them, including his deliberately broken ones, as in "this figure is labeled as 'bad' because it is overly complex". And code generation with no retouching, on which he is doctrinaire: "The moment you manually edit a figure, your final figure becomes irreproducible," and "interactive plot programs are a bad idea... Please be aware that Excel is an interactive plot program as well and is not recommended for figure preparation."

## What they would say about a figure first

He would first ask whether the figure supports the caption's first sentence or only describes its contents. Then he would say the axis labels are too small. Then whether the palette survives color-vision deficiency, and whether color re-encodes what position already shows. He classifies before fixing: *ugly* (aesthetic, which he concedes is the most subjective), *bad* (perceptual) or *wrong* (mathematically incorrect). A review that cannot say which treats a taste call and an arithmetic error as the same finding. Illustrator or a mouse in the workflow is, to him, a reproducibility defect.

## Works, and where they sit in this wiki

- ***Fundamentals of Data Visualization*** (2019): [sources/wilke-fundamentals.md](../sources/wilke-fundamentals.md), with the chapter structure, the topics it grounds, and a Tufte quotation that gets cited as Wilke's.
- `cowplot`, `ggridges`, `ggtext` and his ggplot2 contributions, which carry his defaults into other people's figures: not covered. The [checks](../checks/matplotlib.md) directory is matplotlib-only.
- His blog and talks at clauswilke.com: not covered.

His acknowledgments thank **Jon Schwabish** among the book's commenters, so the overlap with [Schwabish's](jonathan-schwabish.md) redesign rules is not coincidence. His data-ink position, inherited from Tufte and argued down, is assessed in [refutations.md](../refutations.md) and [sources/tufte.md](../sources/tufte.md).

## Links

- [sources/wilke-fundamentals.md](../sources/wilke-fundamentals.md): the book
- [concepts/channels.md](../concepts/channels.md): the evidence his color and encoding advice does and does not rest on
- [refutations.md](../refutations.md): data-ink and chartjunk
- [jonathan-schwabish.md](jonathan-schwabish.md): the closest neighbor on defaults, further from him on chart-type permissiveness
