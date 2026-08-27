---
type: person
status: secondary-only
status_partial: true
retrieved: 2026-08-23
---

# Edward Tufte

**What they are known for.** *The Visual Display of Quantitative Information* (1983) and three successors, self-published through his own press, which gave the field its working vocabulary: data-ink, chartjunk, the lie factor, small multiples, sparklines. He is the most-cited author on this subject and the one whose central rule has held up worst.

**How this was read.** There is one upgrade and one reachability correction. Retrieved 2026-08-23.

**The upgrade.** Tufte posted an excerpt of the sparklines chapter of *Beautiful Evidence* on his own site, and it is reachable and readable: <https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/>. The page was fetched with `curl` and stripped to text locally. The sparkline material below is **read from Tufte**, which makes it the only thing in this wiki that is.

**Reachability.** [sources/tufte.md](../sources/tufte.md) records this source as unreachable. It is not, and that page's status is upgradeable.

**Everything else remains secondhand.** The four books are not free and were not read. The data-ink and chartjunk material on this page is deliberately not restated; it lives at [sources/tufte.md](../sources/tufte.md) and [refutations.md](../refutations.md), which carry their own caveats, and this page points rather than repeats.

**What they are good for.** Come back here for the vocabulary, for small multiples and graphical integrity, which nothing in the record argues against, and for the most fully specified visual house style anyone in the canon has produced. Also come back before citing him at anybody, because the citation almost always deploys an assertion as a finding.

**What they do not settle.** Whether removing non-data ink helps anyone read anything. He ran no experiments; the books contain no user studies.

---

## "In the style of Tufte" means, concretely

Unusually tractable, because the look is codified twice over: in his own typeset books, and in `tufte-css`, the third-party stylesheet that reverse-engineers them and is maintained under his GitHub organization.

**The page, with numbers.** From `tufte.css`, fetched and read directly:

| | |
|---|---|
| Background | `#fffff8`, a warm off-white, never pure white |
| Text | `#111`, never pure black |
| Body face | `et-book`, a Bembo derivative; fallbacks `Palatino`, `Palatino Linotype`, `Book Antiqua`, `Georgia` |
| Text column | `55%` of the container |
| Margin notes and side figures | `40%`, in the space the text column does not use |
| Full-width figures | `100%`, breaking the text measure entirely |

The load-bearing decision is that **the margin is not empty space, it is a second column**. Notes, small figures and asides live beside the sentence that refers to them, so nothing is deferred to a footnote or a numbered figure elsewhere. Figures sit at the exact point of reference. Many are not numbered at all, because numbering is what you need when the figure is somewhere else.

**The chart marks.** Reductive to the point of austerity: the **range-frame**, where the axis line is trimmed to run only across the span the data occupies, so the frame itself reports the min and max; the **dot-dash plot**, where the axis is replaced by a marginal rug of the actual observations; the **midgap** box plot, with the box deleted and the median reduced to a dot. Gridlines removed or reduced to hairlines. Legends replaced by direct labels. Color used sparingly and usually as one accent against gray or against the paper.

**Sparklines, which is the one part read from him directly.** From his own excerpt: a sparkline is a small word-sized graphic embedded in text, and he calls them "datawords". The construction he demonstrates, on a clinical glucose series, is worth copying literally:

- a bare line, no axis and no frame, sized to the type around it (he gives 14 letterspaces as a working width),
- the most recent value printed as a **number** beside the line, with the line's rightmost point and that number tied together by a shared color accent,
- the normal range shown as a **gray band** behind the line, so "above the band" and "below the band" are the reading,
- stacked into a table so hundreds of series compare in parallel.

For a financial table he uses red for the oldest and newest values in the series and blue for the yearly low and high. His stated design target on the same page is compact: **"General idea = max[data], min[design]."** And his defense of the resolution trade is that the idea is to be approximately right rather than exactly wrong.

**The tell.** Cream paper, a very small serif face, a live margin column, a chart with no frame and no legend and one accent color, and text and graphic interleaved so tightly that the graphic is inside the sentence.

## What they actually established, and what gets over-claimed in their name

### Data-ink is not settled, and this page will not pretend otherwise

**The empirical record is at [refutations.md](../refutations.md) under "Chartjunk and the data-ink ratio as settled", with its caveats attached, and at [sources/tufte.md](../sources/tufte.md).** Read those. The compressed version, with the caveats intact:

- [Gillan & Richman (1994)](../studies/gillan-richman-1994-data-ink.md) found the effect **element-conditional**. Their Experiment 1 supports Tufte in aggregate. The later experiments found removing the y-axis line and the x axis generally **increased** response time, meaning removal hurt, while removing tick marks helped. That page is `secondary-only`; the full text was not reached.
- Chartjunk is contested in both directions, and the sharper reading in `refutations.md` is that decoration **around** the marks is contested while deformation **of** the marks is not.

The phrasing this project settled on: **strip decoration, keep orientation, never deform the mark. "Maximize" is the verb the element-level data does not support.**

### The attribution point, recorded so it stays fixed

The sentence **"Maximize the data-ink ratio, within reason"** is **Tufte's**, quoted by Wilke in chapter 23 of *Fundamentals*. The italics on *within reason* are **Wilke's**, added deliberately, and Wilke says in the same passage that he thinks Tufte forgets the qualifier for the rest of the book. This wiki previously cited the sentence as Wilke's own. Correct form: *Tufte, quoted in Wilke ch. 23.* Full detail at [sources/tufte.md](../sources/tufte.md), which is where the correction was made.

### One of his own redesigns has been measured, and it lost

This is new to this wiki.

Tufte's **midgap** box plot deletes the box to raise the data-ink ratio, keeping only the whiskers and a dot for the median. No information is removed and the plot gets substantially more compact, so on his own criterion it is a strict improvement. Wickham & Stryjewski, *40 years of boxplots*, report that it was tested:

> "perceptual studies (Stock and Behrens, 1991) have found Tufte's variation to be substantially less accurate than the original."

**Stock & Behrens was not reached**, so this is a reported result from a `primary-read` secondary source, and it is one study on one redesign. Take it for what it is: the clearest available case of a data-ink minimization being run against the thing it minimized under measurement, and coming out worse. It sits well next to Gillan & Richman's axis-line finding, which points the same direction from a different angle. See [john-tukey.md](john-tukey.md).

### He ran no experiments, and this is the thing most often forgotten

*The Visual Display of Quantitative Information* is 197 pages of argument, historical example and redesign. It contains no controlled study. Every rule in it is [authority-asserted](../concepts/evidence-class.md), by an unusually good authority, and the characteristic failure in his name is people citing "Tufte showed that chartjunk hurts comprehension." Nothing showed that. Bateman et al. later tested something adjacent and found accuracy no worse on embellished charts.

### What survives untouched

**Small multiples** (chapter 8) and **graphical integrity** (chapter 2, the lie factor, design variation versus data variation). Nothing in the record argues against either, and they should not be discarded along with the ratio.

One qualification on small multiples: **the term is his, the practice is much older**. Nightingale's 1858 plate is two panels on a shared area scale with a leader line tying them together, and Bertin's entire matrix method is small multiples with the sorting made explicit. See [florence-nightingale.md](florence-nightingale.md) and [jacques-bertin.md](jacques-bertin.md).

### The Minard problem, and the omission behind it

Tufte calls Minard's 1869 march-on-Moscow figure possibly the best statistical graphic ever drawn, and that judgment has propagated further than almost anything else he wrote. [Hugh Small](https://www.york.ac.uk/depts/maths/histstat/small.htm) points out that Minard's temperature curve implies the army froze to death, while roughly 300,000 were lost on the advance against 90,000 on the retreat. Small also notes that **Tufte does not mention Nightingale in the book at all**, which is a real omission in a history that reaches back to Playfair and forward to Minard, and part of why the canon this project sampled had no route to her. Both points are `secondary-only`, from Small.

## Works, and where they sit in this wiki

- ***The Visual Display of Quantitative Information*** (1983; 2nd ed. 2001, 197 pp) has a page at [sources/tufte.md](../sources/tufte.md), including the chapter list, the two Tufte quotes that reached this project through Wilke, and the structural argument for why a thin page here is worse than a thin page elsewhere. Read that rather than duplicating it.
- ***Envisioning Information*** (1990), ***Visual Explanations*** (1997), ***Beautiful Evidence*** (2006). **No pages.** The sparklines chapter of the last is pages 46-63 and its excerpt is the one thing here read from him.
- ***The Cognitive Style of PowerPoint*** (essay) and ***Visual and Statistical Thinking***. **Not covered**, and out of scope for a figure bar.
- **`tufte-css`**, at `edwardtufte.github.io/tufte-css`. **Not a Tufte work.** A third-party codification under his GitHub organization. Read directly for this page, and it is the most executable specification of the look that exists.

**The structural gap has not closed.** He still has no row in [roll-call.md](../roll-call.md) and no entry in [inventory.md](../inventory.md) except by quotation through Wilke. This page is about the person and the style; it does not enumerate the book, and enumerating the book is what the roll-call's own guarantee requires. Nine chapters are listed on [sources/tufte.md](../sources/tufte.md) and somebody with a copy could map them in an afternoon.

## Links

- [sources/tufte.md](../sources/tufte.md), the work, the quote provenance, and the audit gap
- [refutations.md](../refutations.md), the data-ink and chartjunk record with its caveats
- [studies/gillan-richman-1994-data-ink.md](../studies/gillan-richman-1994-data-ink.md), the element-conditional finding
- [concepts/evidence-class.md](../concepts/evidence-class.md), the distinction his reputation routinely erases
- [claus-wilke.md](claus-wilke.md), who inherits the data-ink position and then argues it down in the text
- [john-tukey.md](john-tukey.md), whose box plot he redesigned, and whose original beat the redesign under test
- [jacques-bertin.md](jacques-bertin.md), the other theorist whose most-cited rule rests on assertion, and who got there sixteen years earlier
