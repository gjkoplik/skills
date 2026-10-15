---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Cole Nussbaumer Knaflic

**What they are known for.** *storytelling with data* (Wiley, 2015), the book most business analysts have read, and the training company of the same name. Her contribution is a **sequence**, not a catalog: understand the context, choose the visual, remove clutter, direct attention, think like a designer, tell a story.

**How this was read.** Partial coverage, all opened locally:

- Wiley's chapter-1 excerpt PDF (`catalogimages.wiley.com/images/db/pdf/9781119002253.excerpt.pdf`), extracted with `pdftotext`. Every book quote here is from it.
- Two `storytellingwithdata.com` blog posts, pulled with `curl` and stripped to text. "can design be taught?" (18 June 2026) carries her byline and is the source of every 2026 quote. "apply color thoughtfully in your graphs" (11 August 2026) is bylined **Amy Esselman**, not Knaflic.
- Five rendered figures from those posts, measured pixel by pixel with PIL.

Chapters 2 through 10 of the book were not read. [sources/knaflic-swd.md](../sources/knaflic-swd.md) reached the contents page and the full index.

**What they are good for.** *What am I asking this audience to do, and what should I delete*. She is the canon's best source on pre-figure questions and on decluttering as a procedure, and the person a stakeholder is likely quoting when they say a chart is missing something basic.

**What they do not settle.** Anything statistical: uncertainty, intervals, distribution versus summary, log scales, maps, reproducibility. Her most-repeated rule has no experiment behind it.

---

## "In the style of Cole Nussbaumer Knaflic" means, concretely

**How much of this is inference.** The principles are her own words, from chapter 1 and her 2026 post. The palette numbers are measurements of her current company's house style, not the 2015 book's, from a thin sample. The hex codes are "what SWD ships in 2026," not "the storytelling with data palette."

**Palette habits.** Her 2026 rule:

> "if you're trying to direct attention in a graph or a slide, a different logic applies. **A mostly neutral palette with one intentional color used sparingly is far more effective than many competing colors.**"

That bylined sentence confirms the attribution of the gray-plus-one-accent rule. [refutations.md](../refutations.md) finds no controlled study behind it, so it stays authority-asserted, stated as design advice rather than a finding. The book's chapter-4 color passage was not read ([sources/knaflic-swd.md](../sources/knaflic-swd.md)), so no book wording of the rule is quoted.

From two figures in the Esselman post (SWD team):

- Context bars sit at `#7F7F7F`, which is exactly 50% gray, and account for 2.5% of all pixels.
- The accent is `#ED7D31`, within JPEG artifacts: Excel's stock **Accent 2** orange, unmodified.
- Saturated pixels are 3.8% of the figure. Everything else is white or gray.

From two figures in her own 18 June post, in the current SWD brand: `#001855` dark navy, `#0E7C6E` teal and `#0270DE` blue, with `#BFBFBF` for de-emphasis and `#404040` for text. Three saturated hues, no red, no categorical green. The makeovers use the 50%-gray plus stock-orange version.

**Title and annotation voice.** Titles assert. Her prose runs to short declaratives, lowercase chapter titles and second person. Direct labeling replaces legends (chapter 3, "label data directly"). Her text rule is about alignment, which [Muth](lisa-charlotte-muth.md) independently shares:

> "One particular pet peeve worth calling out: center-aligned text. It doesn't align to anything, which leaves it floating unmoored on the page. When it runs to multiple lines, you end up with two jagged edges."

**Chart-type preferences and aversions.** Her company's site footer: "Helping rid the world of ineffective graphs, one 3D pie at a time!" The book's "visuals to avoid" are pie charts, donut charts, 3D and secondary y-axes. She uses simple text, tables, points, lines, slopegraphs, bars and area graphs.

**Density and restraint.** Sparse, by checklist. Chapter 3's decluttering steps: remove chart border, remove gridlines, remove data markers, clean up axis labels, label data directly, leverage consistent color. Chapter 5: "Whitespace... is not wasted space. It is doing work." The 2026 post gives the reason, and it can be checked against any figure:

> "**When something in your design is different, viewers read that difference as meaningful.**... Inconsistency reads as noise, while intentional variation reads as signal."

**The tell.** An Excel chart beaten into shape. The book's download page says "graphs were created using Excel for Mac 2011 Version 14.1.0." 50% gray context bars, one orange or blue accent, no border, gridlines or markers, direct labels, a left-aligned asserting title, and Excel's default proportions underneath: stock geometry, deliberate overrides for everything that carries meaning. Her principle: "Accepting defaults uncritically isn't the same as making no design choice. It's making an unconsidered one."

## What they would say about a figure first

Her first question is who the figure is for and what its author wants them to do. In her framework that is the gate:

> "You should always want your audience to know or do something. If you can't concisely articulate that, you should revisit whether you need to communicate in the first place."

She rejects vague answers by name: "Avoid general audiences, such as 'internal and external stakeholders' or 'anyone who might be interested'." Next she asks whether exploratory work is shown in an explanatory setting, her opening move in chapter 1:

> "Too often, people err and think it's OK to show exploratory analysis (simply present the data, all 100 oysters) when they should be showing explanatory... You are making your audience reopen all of the oysters!"

Then the pixels: what the eye lands on first, and whether the author or the tool chose it. [Cairo](alberto-cairo.md) first asks whether a chart is *true*. Knaflic first asks whether it has a *point*. She treats design as learnable: "It's not a talent you either have or you don't. It's a skill. Like any skill, it can be cultivated."

## Works, and where they sit in this wiki

- ***storytelling with data*** (2015; 10th Anniversary Edition, December 2025): [sources/knaflic-swd.md](../sources/knaflic-swd.md), with both ISBNs, the structure from the index, and the topics it grounds.
- ***storytelling with you*** (2022) and ***Daphne Draws Data*** (a children's book, mentioned in her 2026 post): not covered.
- The SWD blog, chart guide and `#SWDchallenge` archive: not covered. The chart guide is a chart chooser, a neighbor to [sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md).
- The book's figure downloads: on her site in Excel under a stated attribution license, with third-party reimplementations in matplotlib, ggplot2 and Highcharts. Not opened. They are the direct route to a measured 2015 palette.

## Links

- [sources/knaflic-swd.md](../sources/knaflic-swd.md): the book
- [refutations.md](../refutations.md): the gray-plus-one-accent rule and its missing controlled study
- [lisa-charlotte-muth.md](lisa-charlotte-muth.md): the same emphasis-through-color problem, with a finer treatment of desaturation
- [alberto-cairo.md](alberto-cairo.md): the contrast in first questions
