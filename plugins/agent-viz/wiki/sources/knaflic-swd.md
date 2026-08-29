---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
author: cole-nussbaumer-knaflic
---

# Knaflic, *Storytelling with Data*

Cole Nussbaumer Knaflic, *storytelling with data: a data visualization guide for business professionals* (Wiley, 2015; 10th Anniversary Edition, December 2025). Ten chapters that argue a sequence rather than catalog a space: understand the context, choose the visual, remove clutter, direct attention, design, and tell a story.

**How this was read.** `primary-read`, partial. Retrieved 2026-08-23 from Wiley's own excerpt PDFs, downloaded with `curl` and text-extracted locally with `pypdf`:

- **chapter 1 in full** (16 pages)
- the **contents page** of both editions
- the **complete index** (12 pages)

Chapters 2 through 10 were not read. The section-level structure below comes from the index, which is the book's own, and is labeled as such. Quotes are from chapter 1 only and are verbatim.

**This retires the roll-call's self-declared weakest link.** The previous state was a chapter list from search aggregation, with the note that "any gloss on chapter 5's contents is from background familiarity, not a retrieved quote, and is unvouched." The chapter list is now confirmed against the publisher's own contents page, and chapter 5's four sections are confirmed from the index.

**What it is good for.** The question it answers: *what am I actually asking this audience to do, and what should I delete*. Knaflic is the best source in the canon on the pre-figure questions (who, what, how), on decluttering as a **named procedure** rather than a taste, and on narrative structure. She is the source a practitioner is most likely to be quoting when they say a bar is missing something basic.

**What it does not settle.** No evidence base of its own: this is design authority, and the inventory labels it that way. The frame is business communication (slides, dashboards, stakeholders), so there is nothing on statistical honesty (uncertainty, intervals, distribution versus summary), nothing on log or nonlinear scales, nothing on maps, and nothing on reproducibility or export. And per [refutations.md](../refutations.md), the "gray plus one accent" rule usually attributed here has **no controlled study** behind it.

---

## Editions, because Wiley's own pages are confusing

| | 1st edition | 10th Anniversary Edition |
|---|---|---|
| ISBN | 978-1-119-00225-3 | 978-1-394-38809-7 |
| Date | November 2015 | December 2025 |
| Pages | 288 | 336 |

**The ten chapters and their page numbers are identical across both editions.** The anniversary edition adds a "reflecting on the past 10 years" front piece and three appendices: A, the narrative arc (257); B, your role in storytelling with data (277); C, more model visuals (293).

One trap: Wiley serves the **anniversary-edition** excerpt files from the **first edition's** product page. The "Chapter 01 (PDF)" linked off the 2015 listing carries a 2025 typesetting date and references *storytelling with you* (2022) in its text. The contents PDF on that page is the genuine first-edition one (bibliography 257, index 261). A page-number citation therefore has to name the edition.

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

The roll-call's chapter titles match this exactly, and its four exclusions (6, 8, 9, 10 as worked examples and closing matter) are confirmed by the contents page and the index.

## Section structure, from the book's index

This is the part that was previously unvouched. Page ranges are the index's own.

**Ch. 3, clutter is your enemy!** Cognitive load (71 to 73), including "data-ink/signal-to-noise ratio, 72". Gestalt Principles of Visual Perception (74 to 81): proximity, similarity, enclosure, closure, continuity, connection. Lack of visual order (81 to 86): alignment, white space. Nonstrategic use of contrast (86 to 90). Decluttering (90 to 97): remove chart border, remove gridlines, remove data markers, clean up axis labels, label data directly, leverage consistent color.

**Ch. 4, focus your audience's attention.** Memory: iconic, short-term, long-term (100 to 102). Preattentive attributes in text (106 to 109) and in graphs (109 to 116). Color: using sparingly (118 to 120), using consistently (120 to 121), designing with colorblind in mind (121 to 122), considering tone conveyed (122 to 123), brand colors (123 to 124). Position on page (124 to 126).

**Ch. 5, think like a designer.** Four sections, the four A's: affordances (128 to 138, covering highlighting effects, eliminating distractions, and creating a clear visual hierarchy), accessibility (138 to 145, covering overcomplicating, poor design, and thoughtful use of text), aesthetics (145 to 148), acceptance (149 to 150).

**Ch. 2, choosing an effective visual.** Simple text, tables (borders, heatmap), points, lines, slopegraphs, bars, area graphs, infographics. A named "visuals to avoid" section (61 to 68): pie charts, donut charts, 3D, secondary y-axis.

**Ch. 7, lessons in storytelling.** The magic of story (cinema, plays, written word), constructing the story (plot, rising action, climax, falling action, resolution, tension), narrative structure and flow, repetition ("Bing, Bang, Bongo"), and clarity tactics: horizontal logic, vertical logic, reverse storyboarding.

Two entries matter for cross-referencing: the index puts **Tufte at ix, 72, 231**, and *The Visual Display of Quantitative Information* at 72, which is inside the clutter chapter's cognitive-load section. That is the whole of Knaflic's engagement with data-ink.

## Quotes verified verbatim (chapter 1 only)

On exploratory versus explanatory analysis, which is the book's opening move:

> When we do exploratory analysis, it's like hunting for pearls in oysters. We might have to open 100 oysters (test 100 different hypotheses or look at the data in 100 different ways) to find perhaps two pearls.

> Too often, people err and think it's OK to show exploratory analysis (simply present the data, all 100 oysters) when they should be showing explanatory... You are making your audience reopen all of the oysters!

On audience:

> Avoid general audiences, such as "internal and external stakeholders" or "anyone who might be interested"

Her reason, in the same sentence: communicating to too many people with disparate needs at once leaves the communicator unable to reach any one of them as effectively.

On having a point at all:

> You should always want your audience to know or do something. If you can't concisely articulate that, you should revisit whether you need to communicate in the first place.

On the temptation to show only supporting data, which is a stronger statement than the book's reputation suggests:

> You might assume that showing only the data that backs up your point and ignoring the rest will make for a stronger case. I do not recommend this. Beyond being misleading by painting a one-sided story, this is very risky.

## Where its advice is contested

- **Gray plus one accent.** The rule everyone attributes here is authority-asserted and a search for a controlled experiment testing one-accent against two-saturated-color emphasis returned nothing. See [refutations.md](../refutations.md). The index confirms a "using color sparingly, 118 to 120" section exists, which is consistent with the attribution, but **that passage was not read**, so no statement of the rule here carries quotation marks.
- **Decluttering.** Chapter 3's remove-the-border, remove-the-gridlines, remove-the-data-markers list is the practical form of data-ink maximization, and the empirical record on that is contested in both directions. See [tufte.md](tufte.md) and [refutations.md](../refutations.md). Gillan & Richman found removals to be **element-conditional**, with some removals hurting reading speed.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), not recomputed here: 1, 3, 4, 5, 6, 29, 37, 41, 47, 65, 66, 67, 71, 79, 85, 86, 87, 89.

One addition the roll-call could not have made: the anniversary edition's **Appendix A, the narrative arc** (257 to 275) is new material bearing on topics 85 through 87. The roll-call predates that edition.

## What the project got wrong about it

Only the status, and it was correctly flagged as the weak link rather than hidden. The chapter titles the roll-call recorded were right. The gloss on chapter 5 that it flagged as unvouched turns out to be right too: affordances, accessibility, aesthetics, acceptance.

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the chapter mapping and its stated exclusions
- [refutations.md](../refutations.md), the gray-plus-one-accent negative result
- [tufte.md](tufte.md), the data-ink lineage behind chapter 3
