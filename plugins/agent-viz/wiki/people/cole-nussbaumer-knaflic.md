# Cole Nussbaumer Knaflic

**What they are known for.** *storytelling with data* (Wiley, 2015), the book most business analysts have actually read, and the training company of the same name that grew out of it. Her contribution is a **sequence**, not a catalog: understand the context, choose the visual, remove clutter, direct attention, think like a designer, tell a story.

**Status: `primary-read`, partial.** Retrieved 2026-08-23. Three things were opened locally and nothing came from a fetch summary:

- Wiley's own 6-page chapter-1 excerpt PDF (`catalogimages.wiley.com/images/db/pdf/9781119002253.excerpt.pdf`), text-extracted with `pdftotext`. All book quotes below are from that.
- Two `storytellingwithdata.com` blog posts pulled with `curl` and stripped to text locally. One carries her own byline ("can design be taught?", 18 June 2026) and is the source of every 2026 quote here. The other ("apply color thoughtfully in your graphs", 11 August 2026) is bylined **Amy Esselman**, not Knaflic, and is labeled as such wherever it is used.
- Five rendered figures from those posts, downloaded and measured pixel-by-pixel with PIL. Those measurements are reported as measurements.

Chapters 2 through 10 of the book were not read here. See [sources/knaflic-swd.md](../sources/knaflic-swd.md), which reached the contents page and the full index.

**What they are good for.** Come back here with: *what am I asking this audience to do, and what should I delete*. She is the best source in the canon on the pre-figure questions and on decluttering as a named procedure. She is also the person your stakeholder is most likely quoting when they say your chart is missing something basic.

**What they do not settle.** Anything statistical. The frame is business communication, so there is nothing on uncertainty, intervals, distribution versus summary, log scales, maps, or reproducibility. And her most-repeated rule has no experiment behind it; see the color section below.

---

## "In the style of Cole Nussbaumer Knaflic" means, concretely

**How much of this is inference.** The principles are her own stated words, from chapter 1 and from a 2026 post under her byline. The **palette numbers** are inference from measurement: I sampled five rendered figures from two 2026 posts on her company's site. Five figures is a thin sample and it is her current organization's house style, not the 2015 book's. Treat the hex codes as "what SWD ships in 2026," not as "the storytelling with data palette."

**Palette habits.** The rule, in her own 2026 words: "if you're trying to direct attention in a graph or a slide, a different logic applies. **A mostly neutral palette with one intentional color used sparingly is far more effective than many competing colors.**"

That sentence is worth flagging, because this wiki has carried an open question about it. [refutations.md](../refutations.md) records that the gray-plus-one-accent rule everyone attributes to Knaflic has no controlled study behind it, and [sources/knaflic-swd.md](../sources/knaflic-swd.md) warns that the book's chapter-4 color passage was never read, so no quotation marks should be put around any statement of the rule. **The attribution is now confirmed from a bylined primary.** The evidence status is unchanged: it is still authority-asserted, and she asserts it as a designer, not as a finding.

Measured, from two figures in the "apply color thoughtfully" post (Esselman, SWD team):

- Context bars sit at `#7F7F7F`, which is exactly 50% gray, and account for 2.5% of all pixels in the finished figure.
- The accent is `#ED7D31`, give or take a JPEG artifact. That is Excel's stock **Accent 2** orange, unmodified.
- Saturated pixels are 3.8% of the finished figure. Everything else is white or gray.

Measured, from two figures in her own 18 June post, which use the current SWD brand rather than a makeover palette:

- `#001855` dark navy, `#0E7C6E` teal, `#0270DE` blue, with `#BFBFBF` for de-emphasis and `#404040` for text.
- Three saturated hues, no red, no green in the categorical sense.

The 50%-gray plus stock-Excel-orange combination is the more imitable of the two, because it is what the makeovers actually use.

**Title and annotation voice.** Titles assert. So does the body copy: her prose style is short declaratives, lowercase chapter titles, and second person. Direct labeling over legends is the house move, and the book's chapter 3 has "label data directly" as a named decluttering step.

Her most transferable text rule is about **alignment**, not wording, and she flags it as a personal irritant: "One particular pet peeve worth calling out: center-aligned text. It doesn't align to anything, which leaves it floating unmoored on the page. When it runs to multiple lines, you end up with two jagged edges." (Note that [Muth](lisa-charlotte-muth.md) independently states the same rule. Two of the five people in this section have a named position on text alignment, and they agree.)

**Chart-type preferences and aversions.** The aversions are the loud part, and her company puts one of them in its own site footer: "Helping rid the world of ineffective graphs, one 3D pie at a time!" The book has a named "visuals to avoid" section covering pie charts, donut charts, 3D, and secondary y-axis. What she reaches for instead is unglamorous and deliberate: simple text, tables, points, lines, slopegraphs, bars, area graphs.

**Density and restraint.** Sparse, and mechanically so. The chapter-3 decluttering list is a checklist you can run: remove chart border, remove gridlines, remove data markers, clean up axis labels, label data directly, leverage consistent color. Chapter 5 adds whitespace as a positive: "Whitespace... is not wasted space. It is doing work."

The 2026 formulation of why is sharper than the book's: "**When something in your design is different, viewers read that difference as meaningful.**... Inconsistency reads as noise, while intentional variation reads as signal." That is a better justification for decluttering than the data-ink ratio, and it is testable against a figure: does every difference in this design mean something, and does everything that should look the same actually look the same?

**The tell.** An Excel chart that has been beaten into shape. The book's own download page says it plainly: "graphs were created using Excel for Mac 2011 Version 14.1.0." If you see a figure with 50% gray context bars, one orange or blue accent, no chart border, no gridlines, no data markers, direct labels instead of a legend, a left-aligned asserting title, and Excel's default proportions underneath all of it, that is the SWD look. The giveaway is the specific combination of **stock tool defaults for geometry and deliberate override for everything that carries meaning.** She names this as the principle: "Accepting defaults uncritically isn't the same as making no design choice. It's making an unconsidered one."

## What they would say about your figure first

Before anything about the figure, she would ask who it is for and what you want them to do. That is not a warm-up question in her framework, it is the gate: "You should always want your audience to know or do something. If you can't concisely articulate that, you should revisit whether you need to communicate in the first place." She would push back on a vague answer, hard, because the book names the failure explicitly: "Avoid general audiences, such as 'internal and external stakeholders' or 'anyone who might be interested'." Then she would ask whether you are showing exploratory work in an explanatory setting, which is her opening move in chapter 1: "Too often, people err and think it's OK to show exploratory analysis (simply present the data, all 100 oysters) when they should be showing explanatory... You are making your audience reopen all of the oysters!" Only after those does she look at the pixels, and then the first pixel question is what your eye lands on first and whether that was your decision or your tool's. Notice how different this is from [Cairo](alberto-cairo.md), who starts by asking whether the chart is *true*. Knaflic starts by asking whether it has a *point*. Both are first questions; they are not the same first question.

One thing she would not do is tell you it comes down to talent. "It's not a talent you either have or you don't. It's a skill. Like any skill, it can be cultivated."

## Works, and where they sit in this wiki

- ***storytelling with data*** (2015; 10th Anniversary Edition, December 2025) has a full page at [sources/knaflic-swd.md](../sources/knaflic-swd.md), including both editions' ISBNs, the chapter-and-section structure recovered from the book's own index, a trap about which excerpt Wiley serves from which product page, and the topics it grounds. Do not duplicate it.
- ***storytelling with you*** (2022) and ***Daphne Draws Data*** (a children's book, referenced in her own 2026 post) are **not covered anywhere in this wiki**.
- **The SWD blog, chart guide, and `#SWDchallenge` archive** are not covered. The chart guide in particular is a chart-chooser artifact and would be a natural neighbor to [sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) if anyone reaches it.
- **The book's figure downloads** are published on her site under a stated attribution license, in Excel, plus third-party reimplementations in matplotlib, ggplot2 and Highcharts. Nobody here has opened them. They are the most direct route to a measured, non-inferred palette for the 2015 book, and this page's five-figure sample is a poor substitute.

## Links

- [sources/knaflic-swd.md](../sources/knaflic-swd.md), the book
- [refutations.md](../refutations.md), the gray-plus-one-accent negative result, which this page's new quote confirms the attribution of and does nothing to strengthen
- [lisa-charlotte-muth.md](lisa-charlotte-muth.md), the nearest working writer on the same emphasis-through-color problem, with a more granular treatment of desaturation
- [alberto-cairo.md](alberto-cairo.md), for the contrast in first questions
