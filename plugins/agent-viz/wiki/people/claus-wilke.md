---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Claus Wilke

**What they are known for.** *Fundamentals of Data Visualization* (O'Reilly, 2019), the broadest single chartcraft reference in this wiki's canon and free in full at [clauswilke.com/dataviz](https://clauswilke.com/dataviz/). He is also the author of several R packages that shape how a lot of scientific figures actually look, including `cowplot`, `ggridges`, and `ggtext`.

**How this was read.** Retrieved 2026-08-23. Eleven chapter pages of the free book were pulled with `curl` and stripped to text locally; the quotes below are re-extracted from that HTML. Four rendered figure PNGs were downloaded and their pixel colors measured locally with PIL. His own homepage supplied the affiliation line. Nothing here comes from a fetch summary.

**What they are good for.** The question he answers: *what should the defaults be, and can each one be defended*. Wilke is the person in this set who documents his own house style rather than leaving it to be inferred, and he documents the reasoning too. He is also the only one who treats reproducibility and the figure-generation pipeline as a quality question rather than a workflow preference.

**What they do not settle.** Almost nothing here is evidence. Wilke runs no experiments and cites few, and his own preface warns against treating him as gospel. His accessibility coverage stops at color-vision deficiency. And, importantly for anyone wanting a single "Wilke look": he deliberately refuses to have one on grids, and says so in the text.

---

## "In the style of Claus Wilke" means, concretely

**How much of this is inference.** Less than for anyone else on these pages. Chapters 4, 19, 22, 23 and 24 are Wilke stating his own defaults and his reasons, in his own words, about his own figures. What follows is mostly quotation and paraphrase of that, not a read of his output. Where I did check his output, I say so and give the measurement.

**Palette habits.** One named default, stated flatly: "My preferred qualitative color scale, which I use extensively throughout this book" is Okabe-Ito. He prints the hex codes in Table 19.1, which makes this the most literally copyable palette in the canon:

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

Eight colors, and he ties that number to a cap: "you should probably not color-code more than eight different items in a plot anyways."

**Checked against his output.** I sampled the saturated pixels of `popgrowth-US-1.png` from chapter 4 and found four hues at 37.6°, 204.4°, 157.3° and 56.4°, against Okabe-Ito's stated 41°, 202°, 164° and 56°. The rendered fills read a little darker than the table (`#DE8E08`, `#48A4E3`, `#138F60`, `#ECE134`), which is what alpha and PNG rendering do to them. The palette claim survives contact with the figures.

For sequential he wants perceptual uniformity and multi-hue ramps that follow "color gradients that can be seen in the natural world, such as dark red, green, or blue to light yellow." He names the reverse (dark yellow to light blue) as the thing that "looks unnatural." Diverging scales must be balanced around a light midpoint, "so that the progression from light colors in the center to dark colors on the outside is approximately the same in either direction."

For highlighting he uses **accent scales**, not gray-plus-one. The distinction matters for anyone imitating him: his baseline categories keep a little color, and he is explicit about the trap. "Notice how drab the baseline colors are... It is easy to make the mistake of using baseline colors that are too colorful, so that they end up competing for the reader's attention against the accent colors." He allows the full-gray version as the "easy remedy," not as the first move.

**Title and annotation voice.** The title asserts, and the assertion is the first thing in the caption. From chapter 22, both halves in the same paragraph: "It does not begin with 'This figure shows how corruption is related to human development.' The first part of the caption is always the title, not a description of the contents of the figure." And: "A title does not have to be a complete sentence, though short sentences making a clear assertion can serve as titles."

His captions follow a recognizable three-part shape: an asserting first sentence, then whatever the reader needs to decode the marks, then a `Data source:` trailer. That trailer is countable. It appears 13 times in chapter 23 alone and 12 times in chapter 29.

He does **not** annotate heavily on the plotting surface. The explanatory weight lives in the caption, which is a scientific-publishing habit and is the main thing separating him from the newsroom writers in this section. He does label directly rather than by legend where the geometry allows it (chapter 20 is a whole chapter on designing figures without legends), but he is not laying prose over the data region the way [Muth](lisa-charlotte-muth.md) does.

**Chart-type preferences and aversions.** Chapters 25 and 26 are the flat refusals, by title: avoid line drawings, don't go 3D. He is unusually permissive elsewhere. Chapter 10 has a section called "A case for pie charts," which puts him at odds with most of this wiki's style guides. His directory of visualizations is organized by data relationship rather than by taste, and he reaches for ECDFs, q-q plots, ridgelines and hypothetical outcome plots more readily than any business-communication author here.

**Density and restraint.** He sits deliberately in the middle, and the sentence that scopes it is chapter 23's: "Both overloading a figure with non-data ink and excessively erasing non-data ink can result in poor figure design." He labels an over-stripped figure "bad" the same as an over-inked one.

His stated grid preference: "I prefer minimal, light grids on a white background." He draws grid lines "orthogonally to direction along which the numbers of interest vary" and only at major ticks, so horizontal lines for a time series and vertical lines for horizontal bars. His own scatter-plot default is "an open background grid and no axis lines or frame around the plot panel," which he likes because it "conveys to the reader that range of possible data values extends beyond the axis limits."

That preference does not generalize into a fixed rule. He is explicit: "Throughout this book I am using a variety of different grid styles, to highlight that there isn't necessarily one best choice." Reasonable people can disagree, and he says so in the text. Anyone selling a fixed "Wilke grid" is selling something he declined to write.

One rule he does state maximally, as the single lesson to take if you take one: "Pay attention to your axis labels, axis tick labels, and other assorted plot annotations. Chances are they are too small."

**The tell.** Three things together. First, an Okabe-Ito hue sitting where a default ggplot2 hue would be expected. Second, a figure caption whose first sentence is a claim and whose last words are `Data source:` something. Third, and this one is unique to him in the whole canon: figures **labeled with their own verdict**. Chapter 1 defines ugly, bad and wrong, and then the book stamps figures with those words, including his own deliberately-broken ones. A figure captioned with an assertion and then a self-assessment of "this figure is labeled as 'bad' because it is overly complex" is Wilke.

A fourth, visible in the source: it was generated by code with no manual retouching. He is doctrinaire about this. "The moment you manually edit a figure, your final figure becomes irreproducible," and "interactive plot programs are a bad idea... Please be aware that Excel is an interactive plot program as well and is not recommended for figure preparation."

## What they would say about a figure first

He would ask what the caption's first sentence claims, and then check whether the figure supports that claim or merely describes its own contents. Then, almost immediately, he would say the axis labels are too small, because he says that is the one lesson to take from the whole book. From there it goes to color: is the palette safe under color-vision deficiency, and is information encoded with color that is already encoded by position? He would classify the problem before proposing a fix, because his own vocabulary forces it: is this *ugly* (aesthetic, and he concedes that judgment is the most subjective), *bad* (perceptual), or *wrong* (mathematically incorrect)? A review that cannot say which of the three it is looking at will treat a taste call and an arithmetic error as the same finding. And he would want to know how the figure was made, because an answer involving Illustrator or a mouse is, to him, a reproducibility defect independent of how the figure looks.

## Works, and where they sit in this wiki

- ***Fundamentals of Data Visualization*** (2019) has a full page at [sources/wilke-fundamentals.md](../sources/wilke-fundamentals.md), including the chapter structure, the topics it grounds, and the one attribution error the project made about it.
- **`cowplot`, `ggridges`, `ggtext`, and his ggplot2 contributions** are not covered anywhere in this wiki. They are the mechanism by which his defaults reach other people's figures, and the [checks](../checks/matplotlib.md) directory is matplotlib-only, so nothing here covers reproducing his look in R or anywhere else.
- **His blog and talks** at clauswilke.com are not covered.

Two cross-links. His acknowledgments thank **Jon Schwabish** among the people who commented on the book, so the overlap between [schwabish's](jonathan-schwabish.md) redesign rules and Wilke's is not coincidence. And the empirical status of his data-ink position, which he inherits from Tufte and then argues down, is in [refutations.md](../refutations.md) and [sources/tufte.md](../sources/tufte.md).

## Links

- [sources/wilke-fundamentals.md](../sources/wilke-fundamentals.md), the book
- [concepts/channels.md](../concepts/channels.md), the evidence his color and encoding advice does and does not rest on
- [refutations.md](../refutations.md), data-ink and chartjunk
- [jonathan-schwabish.md](jonathan-schwabish.md), the closest neighbor in this section on defaults, and further from him on chart-type permissiveness
