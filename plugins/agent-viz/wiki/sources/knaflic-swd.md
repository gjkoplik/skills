---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
author: cole-nussbaumer-knaflic
---

# Knaflic, *Storytelling with Data*

Cole Nussbaumer Knaflic, *storytelling with data: a data visualization guide for business professionals* (Wiley, 2015; 10th Anniversary Edition, December 2025). Ten chapters that argue a sequence: understand the context, choose the visual, remove clutter, direct attention, design, and tell a story.

**What it is good for.** What the audience is being asked to do, and what can be deleted. Knaflic is the canon's main source on the pre-figure questions (who, what, how), on decluttering as a named procedure rather than taste, and on narrative structure.

**What it does not settle.** It is design authority with no evidence base of its own, and the inventory labels it so. The frame is business communication (slides, dashboards, stakeholders), so it says nothing on statistical honesty (uncertainty, intervals, distribution versus summary), log or nonlinear scales, maps, or reproducibility and export. The "gray plus one accent" rule usually attributed here has no controlled study behind it ([refutations.md](../refutations.md)).

**How this was read.** `primary-read`, partial. Wiley's own excerpt PDFs were downloaded with `curl` and text-extracted locally with `pypdf`: chapter 1 in full, the contents page of both editions, and the complete index. Chapters 2 through 10 were not read. The section structure below comes from the book's own index. Quotes are from chapter 1 only.

---

## Editions

| | 1st edition | 10th Anniversary Edition |
|---|---|---|
| ISBN | 978-1-119-00225-3 | 978-1-394-38809-7 |
| Date | November 2015 | December 2025 |
| Pages | 288 | 336 |

The ten chapters and their page numbers are identical across editions. The anniversary edition adds a "reflecting on the past 10 years" front piece and three appendices: A, the narrative arc (257); B, your role in storytelling with data (277); C, more model visuals (293).

Wiley serves the anniversary-edition excerpts from the first edition's product page. The "Chapter 01 (PDF)" there carries a 2025 typesetting date and references *storytelling with you* (2022). The contents PDF on that page is the genuine first-edition one (bibliography 257, index 261). A page-number citation has to name the edition.

## Structure

Verbatim from the contents page:

```
introduction 1
chapter 1  the importance of context 19
chapter 2  choosing an effective visual 35
chapter 3  clutter is your enemy! 71
chapter 4  focus your audience's attention 99
chapter 5  think like a designer 127
chapter 6  dissecting model visuals 151
chapter 7  lessons in storytelling 165
chapter 8  pulling it all together 187
chapter 9  case studies 207
chapter 10 final thoughts 241
```

The roll-call's chapter titles match, and the contents page and index confirm its four exclusions (6, 8, 9, 10 as worked examples and closing matter).

## Section structure, from the book's index

Page ranges are the index's own.

**Ch. 3, clutter is your enemy!** Cognitive load (71 to 73), including "data-ink/signal-to-noise ratio, 72". Gestalt Principles of Visual Perception (74 to 81): proximity, similarity, enclosure, closure, continuity, connection. Lack of visual order (81 to 86): alignment, white space. Nonstrategic use of contrast (86 to 90). Decluttering (90 to 97): remove chart border, remove gridlines, remove data markers, clean up axis labels, label data directly, leverage consistent color.

**Ch. 4, focus your audience's attention.** Memory: iconic, short-term, long-term (100 to 102). Preattentive attributes in text (106 to 109) and in graphs (109 to 116). Color: using sparingly (118 to 120), using consistently (120 to 121), designing with colorblind in mind (121 to 122), considering tone conveyed (122 to 123), brand colors (123 to 124). Position on page (124 to 126).

**Ch. 5, think like a designer.** Four sections, the four A's: affordances (128 to 138, covering highlighting effects, eliminating distractions, and creating a clear visual hierarchy), accessibility (138 to 145, covering overcomplicating, poor design, and thoughtful use of text), aesthetics (145 to 148), acceptance (149 to 150).

**Ch. 2, choosing an effective visual.** Simple text, tables (borders, heatmap), points, lines, slopegraphs, bars, area graphs, infographics. A named "visuals to avoid" section (61 to 68): pie charts, donut charts, 3D, secondary y-axis.

**Ch. 7, lessons in storytelling.** The magic of story (cinema, plays, written word), constructing the story (plot, rising action, climax, falling action, resolution, tension), narrative structure and flow, repetition ("Bing, Bang, Bongo"), and clarity tactics: horizontal logic, vertical logic, reverse storyboarding.

The index puts Tufte at ix, 72 and 231, and *The Visual Display of Quantitative Information* at 72, inside the cognitive-load section. By the index, that is the whole of Knaflic's engagement with data-ink.

## Quotes verified verbatim (chapter 1 only)

On exploratory versus explanatory analysis, the book's opening move:

> When we do exploratory analysis, it's like hunting for pearls in oysters. We might have to open 100 oysters (test 100 different hypotheses or look at the data in 100 different ways) to find perhaps two pearls.

> Too often, people err and think it's OK to show exploratory analysis (simply present the data, all 100 oysters) when they should be showing explanatory... You are making your audience reopen all of the oysters!

On audience:

> Avoid general audiences, such as "internal and external stakeholders" or "anyone who might be interested"

Her reason, in the same sentence, is that a communicator addressing too many disparate needs at once reaches none of them as effectively.

On having a point:

> You should always want your audience to know or do something. If you can't concisely articulate that, you should revisit whether you need to communicate in the first place.

On showing only the supporting data:

> You might assume that showing only the data that backs up your point and ignoring the rest will make for a stronger case. I do not recommend this. Beyond being misleading by painting a one-sided story, this is very risky.

## Where its advice is contested

- **Gray plus one accent.** Authority-asserted. A search for a controlled experiment testing one accent against two saturated colors returned nothing ([refutations.md](../refutations.md)). The index shows a "using color sparingly, 118 to 120" section, consistent with the attribution, but that passage was not read, so no statement of the rule here is quoted.
- **Decluttering.** Chapter 3's removals (border, gridlines, data markers) are the working form of data-ink maximization, and the empirical record on that is contested in both directions ([tufte.md](tufte.md), [refutations.md](../refutations.md)). Gillan & Richman found removals to be element-conditional, with some hurting reading speed.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), not recomputed here: 1, 3, 4, 5, 6, 29, 37, 41, 47, 65, 66, 67, 71, 79, 85, 86, 87, 89. The anniversary edition's Appendix A, the narrative arc (257 to 275), bears on topics 85 through 87 and postdates the roll-call.

## What the project got wrong about it

Only the status. The roll-call's chapter titles were right. It had noted that "any gloss on chapter 5's contents is from background familiarity, not a retrieved quote, and is unvouched." The index confirms that gloss: affordances, accessibility, aesthetics, acceptance.

## Links

- [inventory.md](../inventory.md): the topics this source grounds
- [roll-call.md](../roll-call.md): the chapter mapping and its stated exclusions
- [refutations.md](../refutations.md): the gray-plus-one-accent negative result
- [tufte.md](tufte.md): the data-ink lineage behind chapter 3
