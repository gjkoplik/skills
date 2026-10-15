---
type: source
status: secondary-only
status_partial: true
retrieved: 2026-08-23
author: edward-tufte
---

# Tufte, *The Visual Display of Quantitative Information*

Edward R. Tufte, *The Visual Display of Quantitative Information* (Graphics Press; 1st ed. 1983, 2nd ed. 2001). The origin of "chartjunk", the "data-ink ratio", the "lie factor", and small multiples, and the most-cited book in visualization.

**What it is good for.** The vocabulary, and two ideas that survive: **small multiples** and **graphical integrity** (the lie factor, design variation versus data variation). Also the status of "data-ink", usually deployed as if it were a finding.

**What it does not settle.** Whether removing non-data ink helps anybody read anything (below). The book predates color displays, screens, accessibility and plotting software, and says nothing about them.

**How this was read.** `secondary-only`; the book was not read. The chapter list is a library catalog contents note for the 1983 edition, from the Internet Archive metadata API (`archive.org/metadata/visualdisplayofq00tuft`): reliable for structure, useless for wording. The publisher description is reachable but unused; the status is upgradeable. The two Tufte sentences here are quoted from **Wilke chapter 23**, which was primary-read ([wilke-fundamentals.md](wilke-fundamentals.md)), so they are quotes of a quote. Archive.org's search-inside endpoint returned `Invalid filename`; the scan is a lending copy and its text was not obtained.

---

## Structure

**Part I, Graphical practice**

1. Graphical excellence
2. Graphical integrity
3. Sources of graphical integrity and sophistication

**Part II, Theory of data graphics**

4. Data-ink and graphical redesign
5. Chartjunk: vibrations, grids, and ducks
6. Data-ink maximization and graphical design
7. Multifunctioning graphical elements
8. Data density and small multiples
9. Aesthetics and technique in data graphical design

plus an epilogue, "Designs for the display of information".

Chapters 4, 5 and 6 are the data-ink argument, so the contested idea is the spine of Part II.

## The data-ink ratio, as Wilke quotes it

Tufte's definition, via Wilke:

> the "proportion of a graphic's ink devoted to the non-redundant display of data-information"

and the instruction:

> Maximize the data-ink ratio, within reason.

The italics on *within reason* are Wilke's, and he says why:

> I have emphasized the phrase "within reason" because it is critical and frequently forgotten. In fact, I think that Tufte himself forgets it in the remainder of his book, where he advocates overly minimalistic designs that, in my opinion, are neither elegant nor easy to decipher.

He splits the instruction in two:

> If we interpret the phrase "maximize the data-ink ratio" to mean "remove clutter and strive for clean and elegant designs," then I think it is reasonable advice. But if we interpret it as "do everything you can to remove non-data ink" then it will result in poor design choices.

The correct citation is "Tufte, quoted in Wilke ch. 23."

## Where its advice is contested

The record, with caveats, is in [refutations.md](../refutations.md) under "Chartjunk and the data-ink ratio as settled".

- **Data-ink.** Gillan & Richman (1994), across four experiments, found the effect **element-conditional**. Removing the y-axis line and the x axis generally *increased* response time; removing y-axis tick marks did the opposite. Each effect depended on graph type, task and the other elements present. That breakdown comes from secondary summaries, not the primary.
- **Chartjunk.** `contested` in both directions. Bateman et al. (CHI 2010) found accuracy on embellished charts "no worse than for plain charts" and recall after two to three weeks significantly better. Inbar, Tractinsky & Meyer found a preference for non-minimalist bar graphs. Borkin et al. found pictograms act as memory hooks. Against embellishment, Skau et al. (2015) found that changing bar *shape* raises error rates. A methodological critique of Bateman was unreachable (403).

Stripping decoration is supported, keeping orientation is supported, and "maximize" is the verb the data does not support.

Nothing in the record argues against small multiples (chapter 8) or graphical integrity (chapter 2).

## Inventory topics it grounds

Tufte grounds no topic directly. He has no row in [roll-call.md](../roll-call.md), and [inventory.md](../inventory.md) names him only in topic 67. He enters the inventory through Wilke chapter 23, which maps to topics **66** (gridline discipline) and **67** (data-ink discipline, and its contested status).

Small multiples (topic 62) is Tufte's chapter 8, but the roll-call sources it to Wilke ch. 21, Munzner ch. 12, the BBC cookbook and Urban.

The roll-call's method is to "enumerate a source's published outline, map every entry to a topic or a stated exclusion, so an omission shows up as a visibly unmapped chapter." Tufte was never enumerated, so his chapters leave no visible gap. The nine chapters above are unmapped.

## Links

- [refutations.md](../refutations.md): the data-ink and chartjunk record
- [roll-call.md](../roll-call.md): the audit Tufte is absent from
- [wilke-fundamentals.md](wilke-fundamentals.md): the source of every Tufte quote here
- [knaflic-swd.md](knaflic-swd.md): the data-ink argument as a decluttering checklist
- [concepts/evidence-class.md](../concepts/evidence-class.md): evidence-backed versus authority-asserted
