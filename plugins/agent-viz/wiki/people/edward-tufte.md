---
type: person
status: secondary-only
status_partial: true
retrieved: 2026-08-23
---

# Edward Tufte

**What they are known for.** *The Visual Display of Quantitative Information* (1983) and three self-published successors, which gave the field its working vocabulary: data-ink, chartjunk, the lie factor, small multiples, sparklines. He is the most-cited author on this subject and the one whose central rule has held up worst.

**How this was read.** `secondary-only`, with two exceptions read directly: `tufte.css`, and Tufte's own excerpt of the sparklines chapter of *Beautiful Evidence*, fetched with `curl` and stripped to text locally (<https://www.edwardtufte.com/notebook/sparkline-theory-and-practice-edward-tufte/>). That excerpt is reachable, so the unreachable status on [sources/tufte.md](../sources/tufte.md) is upgradeable. The four books are not free and were not read. Data-ink and chartjunk live on [sources/tufte.md](../sources/tufte.md) and [refutations.md](../refutations.md), with their caveats.

**What they are good for.** The vocabulary. Small multiples and graphical integrity, which nothing in the record argues against. The most fully specified visual house style in the canon. The status of citations made in his name, which almost always deploy an assertion as a finding.

**What they do not settle.** Whether removing non-data ink helps anyone read anything. He ran no experiments, and the books contain no user studies.

---

## "In the style of Tufte" means, concretely

The look is codified in his books and in `tufte-css`, a third-party stylesheet that reverse-engineers them, maintained under his GitHub organization:

| | |
|---|---|
| Background | `#fffff8`, a warm off-white, never pure white |
| Text | `#111`, never pure black |
| Body face | `et-book`, a Bembo derivative; fallbacks `Palatino`, `Palatino Linotype`, `Book Antiqua`, `Georgia` |
| Text column | `55%` of the container |
| Margin notes and side figures | `40%`, in the space the text column does not use |
| Full-width figures | `100%`, breaking the text measure entirely |

The margin is a second column. Notes, small figures and asides sit beside the sentence that refers to them, so many figures need no number.

**Chart marks.** The **range-frame** trims the axis to the span of the data, so the frame reports min and max. The **dot-dash plot** replaces the axis with a rug of the observations. The **midgap** box plot deletes the box and reduces the median to a dot. Gridlines become hairlines or go, direct labels replace legends, and color is one accent against gray.

**Sparklines**, from his excerpt: small word-sized graphics in text, which he calls "datawords". His clinical glucose example is a bare line with no axis or frame, sized to the type (14 letterspaces wide), with the latest value printed beside it, tied to the rightmost point by a shared accent color, and a gray band for the normal range. Stacked in a table, hundreds of series compare in parallel. In a financial table he uses red for the oldest and newest values and blue for the yearly low and high. His stated design target is **"General idea = max[data], min[design]."** He defends the low resolution as approximately right rather than exactly wrong.

**The tell.** Cream paper, a very small serif face, a live margin column, a chart with no frame, no legend and one accent color, and the graphic inside the sentence.

## What they established, and what gets over-claimed in their name

### Data-ink is not settled

The record is on [refutations.md](../refutations.md) under "Chartjunk and the data-ink ratio as settled", and on [sources/tufte.md](../sources/tufte.md).

- [Gillan & Richman (1994)](../studies/gillan-richman-1994-data-ink.md) found the effect element-conditional. Experiment 1 supports Tufte in aggregate. Later experiments found that removing the y-axis line and the x axis generally increased response time, while removing tick marks helped. That page is `secondary-only`, since the full text was not reached.
- Chartjunk is contested in both directions. Decoration around the marks is contested. Deformation of the marks is not.

Stripping decoration is supported, keeping orientation is supported, deforming the mark is not, and "maximize" is the verb the element-level data does not support.

### "Within reason" is Tufte's sentence with Wilke's italics

**"Maximize the data-ink ratio, within reason"** is Tufte, quoted by Wilke in chapter 23 of *Fundamentals*. The italics on *within reason* are Wilke's, and in the same passage he says he thinks Tufte forgets the qualifier for the rest of the book. Correct form: *Tufte, quoted in Wilke ch. 23.*

### One of his redesigns was measured, and it lost

The midgap box plot removes no information and is more compact, so by his own criterion it is a strict improvement. Wickham & Stryjewski, *40 years of boxplots*, report:

> "perceptual studies (Stock and Behrens, 1991) have found Tufte's variation to be substantially less accurate than the original."

Stock & Behrens was not reached. This is one study of one redesign, reported by a `primary-read` secondary source. It is the clearest available case of a data-ink minimization losing to the original. Gillan & Richman's axis-line finding points the same way. See [john-tukey.md](john-tukey.md).

### He ran no experiments

The first book is argument, historical example and redesign, with no controlled study. Every rule in it is [authority-asserted](../concepts/evidence-class.md). The characteristic failure is citing "Tufte showed that chartjunk hurts comprehension." Nothing showed that. Bateman et al. later tested something adjacent and found accuracy no worse on embellished charts.

### What survives

**Small multiples** (chapter 8) and **graphical integrity** (chapter 2: the lie factor, design variation versus data variation). Nothing in the record argues against either. The term "small multiples" is his, the practice older. Nightingale's 1858 plate is two panels on a shared area scale, and Bertin's matrix method is small multiples with the sorting made explicit ([florence-nightingale.md](florence-nightingale.md), [jacques-bertin.md](jacques-bertin.md)).

### Minard, and the missing Nightingale

Tufte calls Minard's 1869 march-on-Moscow figure possibly the best statistical graphic ever drawn, his most widely repeated judgment. [Hugh Small](https://www.york.ac.uk/depts/maths/histstat/small.htm) points out that Minard's temperature curve implies the army froze to death, while roughly 300,000 were lost on the advance against 90,000 on the retreat. Small also notes that the book, whose history runs from Playfair to Minard, never mentions Nightingale. Both points are `secondary-only`, from Small.

## Works, and where they sit in this wiki

- ***The Visual Display of Quantitative Information*** (1983; 2nd ed. 2001). [sources/tufte.md](../sources/tufte.md) has the chapter list and the two Tufte quotes that arrived through Wilke.
- ***Envisioning Information*** (1990), ***Visual Explanations*** (1997), ***Beautiful Evidence*** (2006). **No pages.** The sparklines chapter of the last is pages 46-63.
- ***The Cognitive Style of PowerPoint*** and ***Visual and Statistical Thinking***. Out of scope for a figure bar.
- **`tufte-css`** (`edwardtufte.github.io/tufte-css`). **Not a Tufte work.** A third-party codification, and the most executable specification of the look.

He has no row in [roll-call.md](../roll-call.md) and appears in [inventory.md](../inventory.md) only through Wilke. The roll-call's guarantee needs the book enumerated, and [sources/tufte.md](../sources/tufte.md) lists nine chapters without mapping them.

## Links

- [sources/tufte.md](../sources/tufte.md): the work, the quote provenance, the audit gap
- [refutations.md](../refutations.md): the data-ink and chartjunk record
- [studies/gillan-richman-1994-data-ink.md](../studies/gillan-richman-1994-data-ink.md): the element-conditional finding
- [concepts/evidence-class.md](../concepts/evidence-class.md): the distinction his reputation erases
- [claus-wilke.md](claus-wilke.md): inherits the data-ink position, then argues it down
- [john-tukey.md](john-tukey.md): whose box plot beat Tufte's redesign under test
- [jacques-bertin.md](jacques-bertin.md): the other theorist whose most-cited rule rests on assertion, sixteen years earlier
