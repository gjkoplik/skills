---
type: source
status: secondary-only
status_partial: true
retrieved: 2026-08-23
---

# Tufte, *The Visual Display of Quantitative Information*

Edward R. Tufte, *The Visual Display of Quantitative Information* (Graphics Press; 1st ed. 1983, 2nd ed. 2001, 197 pp). The origin document for "chartjunk", the "data-ink ratio", the "lie factor", and small multiples. It is the most-cited book in visualization and the least-read one in this project.

**How this was read.** `secondary-only`, and thinly. The book is not free and was not read. Retrieved 2026-08-23:

- **Chapter list**: a library catalog contents note, obtained from the Internet Archive metadata API for the cataloged 1983 edition (`archive.org/metadata/visualdisplayofq00tuft`). A cataloger's transcription of the book's own contents page, so reliable for structure and useless for wording.
- **Publisher description**: reachable, and this page's status is upgradeable as a result. It was previously recorded here as unreachable, wrongly. Someone should redo this section from the source.
- **Tufte's two load-bearing sentences**: quoted verbatim **inside Wilke chapter 23**, which was primary-read. See [wilke-fundamentals.md](wilke-fundamentals.md).

**Do not treat the Tufte quotes below as read from Tufte.** They are read from Wilke quoting Tufte. That is a quote of a quote, and the distinction is the entire point of this wiki.

Archive.org's full-text search-inside endpoint was tried for verification and returned `Invalid filename`. The scanned item is a lending copy; no attempt was made to obtain the text, and none should be.

**What it is good for.** Come back here for the vocabulary, and for the two ideas that survive intact: **small multiples** and **graphical integrity** (the lie factor, design variation versus data variation). Also come back before citing "data-ink" at anyone, because the phrase is almost always deployed as if it were a finding.

**What it does not settle.** Whether removing non-data ink helps anybody read anything. See below. The book also predates color displays, screens, accessibility, and plotting software entirely, so it says nothing about most of what a modern figure bar owes.

---

## Structure

From the library catalog contents note:

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

Chapters 4, 5 and 6, three of the nine, are the data-ink argument: the contested idea is not a corner of the book, it is the spine of Part II.

## The data-ink ratio, as Wilke quotes it

Tufte's definition of the ratio, quoted in Wilke chapter 23:

> the "proportion of a graphic's ink devoted to the non-redundant display of data-information"

and the instruction:

> Maximize the data-ink ratio, within reason.

**The italics on *within reason* are Wilke's, not Tufte's.** Wilke says so and says why:

> I have emphasized the phrase "within reason" because it is critical and frequently forgotten. In fact, I think that Tufte himself forgets it in the remainder of his book, where he advocates overly minimalistic designs that, in my opinion, are neither elegant nor easy to decipher.

Wilke then splits the instruction into two readings, which is the most useful thing anyone in the canon has done with it:

> If we interpret the phrase "maximize the data-ink ratio" to mean "remove clutter and strive for clean and elegant designs," then I think it is reasonable advice. But if we interpret it as "do everything you can to remove non-data ink" then it will result in poor design choices.

## Where its advice is contested, which is most of it

**This page will not restate the empirical record. It is in [refutations.md](../refutations.md), under "Chartjunk and the data-ink ratio as settled", and that entry carries its own caveats.** The short version, with the caveats attached:

- **Data-ink specifically.** Gillan & Richman (1994) ran four experiments and found the effect **element-conditional**. Removing the y-axis line and the x axis generally *increased* response time, meaning removal hurt. Removing y-axis tick marks did the opposite. Each element's effect was conditional on graph type, task, and which other elements were present. **Caveat, from refutations.md: that experiment-by-experiment breakdown was reached via secondary summaries; the primary was not read.**
- **Chartjunk.** Contested in both directions. Bateman et al. (CHI 2010) found accuracy on embellished charts "no worse than for plain charts" and recall after two to three weeks significantly better; Inbar, Tractinsky & Meyer found a preference for non-minimalist bar graphs; Borkin et al. found pictograms act as memory hooks. Against embellishment, Skau et al. (2015) found that changing bar *shape* raises error rates. **Caveat: a methodological critique of Bateman was unreachable (403).**

The accurate phrasing this project settled on is short: **strip decoration, keep orientation. "Maximize" is the verb the data does not support.**

Two things that are *not* contested and should not be thrown out with the ratio: small multiples (chapter 8) and graphical integrity (chapter 2). Nothing in the record argues against either.

## Inventory topics it grounds

**None directly, and that is the finding.** Tufte has no row in [roll-call.md](../roll-call.md), and his name appears nowhere in [inventory.md](../inventory.md) or [refutations.md](../refutations.md). The canon's most-cited author entered the 92-topic inventory **only secondhand**, through Wilke chapter 23, which maps to topics **66** (gridline discipline) and **67** (data-ink discipline, and its contested status).

Small multiples (topic 62) is Tufte's chapter 8, but the roll-call sources that topic to Wilke ch. 21, Munzner ch. 12, the BBC cookbook and Urban. The idea's origin and its citation in this project are different things.

## What the project got wrong about it

Two things, one small and one structural.

**Small.** Inventory topic 67 cites `Wilke ch. 23: "Maximize the data-ink ratio, within reason."` The sentence is Tufte's; Wilke is quoting it and adding the emphasis. The citation should read "Tufte, quoted in Wilke ch. 23." The topic's substance, that this is the canonical case where a bar must not present an authority claim as an empirical one, is right.

**Structural.** The roll-call's whole method is "enumerate a source's published outline, map every entry to a topic or a stated exclusion, so an omission shows up as a visibly unmapped chapter." Tufte was never enumerated. He has no chapter rows, no exclusions, and therefore no visible gap. The method's own guarantee does not cover him, because he was never entered into it. A source that is absent from the roll-call is invisible to the roll-call's audit, which is a weakness of the artifact rather than of the source.

Nine chapters are listed above. Someone with a copy could map them in an afternoon.

## Links

- [refutations.md](../refutations.md), the data-ink and chartjunk record, with its caveats
- [roll-call.md](../roll-call.md), the audit Tufte is absent from
- [wilke-fundamentals.md](wilke-fundamentals.md), the primary-read source of every Tufte quote on this page
- [knaflic-swd.md](knaflic-swd.md), where the data-ink argument shows up in practitioner form, as a decluttering checklist
- [concepts/evidence-class.md](../concepts/evidence-class.md), evidence-backed versus authority-asserted, the distinction at stake on this page
