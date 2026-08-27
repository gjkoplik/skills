---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Jacques Bertin

**What they are known for.** *Sémiologie graphique* (1967), the book that first treated graphics as a formal sign system rather than a craft, and the source of the visual variables. Almost every modern vocabulary for encoding data, marks and channels, expressiveness, levels of measurement, is a re-lexicalization of his.

**How this was read.** There is a large caveat about which edition. Retrieved 2026-08-23. The full 415-page French text was downloaded and extracted locally:

Three things a later reader needs to know before leaning on this page:

- **It is the French 3rd edition (EHESS, 1999), which is a reprint of the 1973 2nd edition** with an added preface and a chapter on *la graphique*. Bertin says so in that preface: the book was written in 1965, published 1967, revised 1971, and it is the 1973 text being reissued.
- **The standard English translation (Berg, 1983; ESRI Press, 2010) was not consulted.** Every English term below is my rendering of Bertin's French. Where the English literature has settled on a word (*value* for `valeur`, *grain* or *texture* for `grain`), I say which French word it came from so you can check.
- **The scan is an in-copyright book on Monoskop**, and the OCR is poor. Accents and word breaks are frequently destroyed. Quotes below are only those fragments that extracted cleanly; everywhere the OCR was mangled I paraphrase and say so rather than repairing text and presenting the repair as a quote.

**What they are good for.** Come back here with: *what am I actually allowed to encode this on, and what will the reader be able to do with it*. Bertin's levels of organization answer a question the accuracy literature does not: not "how precisely can this be read" but "can this variable be selected, ordered, or measured at all". He is also the only source in this wiki that treats networks as a first-class graphic problem with its own construction rules.

**What they do not settle.** Anything empirically. There are no experiments in this book. What Bertin calls a *Test* is a demonstration addressed to you, the reader, over a facing-page figure: isolate one category, then see whether you could. Introspection with a control figure is not a controlled study, and his orderings are [authority-asserted](../concepts/evidence-class.md) throughout.

---

## "In the style of Bertin" means, concretely

**Monochrome by default, and texture where you would reach for color.** The plates are print-shop artifacts from a cartography lab. Black ink, white paper, and differentiation carried by `grain` (dot density and coarseness) and `valeur` (lightness) rather than by hue. This is not nostalgia. It follows from his own ordering: `grain` and `valeur` are ordered variables and `couleur` is not, so a Bertin figure spends hue on categories and lightness or texture on anything with a sequence.

**Tiny marks, many of them, in a grid.** The characteristic Bertin page is a matrix of small multiples: dozens of miniature maps or dot-fields laid out in rows and columns so the whole set is one image. He is not making one big figure with a lot in it; he is making many small figures that add up to a readable field.

**The reorderable matrix.** His most distinctive object is the *matrice ordonnable*: rows and columns as physical strips, permuted by hand until structure appears. If you want a figure that reads as his, the sorting is the analysis. An unsorted matrix is an unfinished one.

**The legend states the invariant and the components.** His information analysis starts by separating what is constant across the whole graphic (the *invariant*) from what varies (the *composantes*). A Bertin-style title says what the invariant is, and the legend enumerates the components with their length and level of organization. This is more structured than a modern caption and it is the part most imitations drop.

**No decoration whatsoever, and no apology for density.** He is blunt about it in the third-edition preface: graphics is not an art, it is a scientific language ("la graphique n'est pas un art. C'est un langage scientifique").

**For networks specifically**, and this is unusually concrete for 1967: he names a *rectilinear construction*, elements ordered along a line with links drawn as curves distributed to either side, and a *circular construction*, elements placed on a circle so every link becomes a straight chord. Those are the arc diagram and the chord diagram, described as construction options with stated trade-offs, decades before either got its modern name. He argues the circular one gives the least confused image a priori, whatever the number of crossings in the raw data.

## What they actually established, and what gets over-claimed in their name

### There are eight visual variables, not seven

The number in circulation is seven. The book says eight, and says it in one sentence: **"Le dessinateur dispose ainsi de huit variations sensibles."** The eight are the **two dimensions of the plane**, plus six *retinal* variables that a mark fixed at a point in the plane can still vary on:

| French | Usual English |
|---|---|
| les deux dimensions du plan | the two planar dimensions |
| taille | size |
| valeur | value (lightness) |
| grain | grain, usually translated texture |
| couleur | color (hue) |
| orientation | orientation |
| forme | shape |

Lists that report seven have collapsed the plane's two dimensions into one item called "position". That is not a harmless simplification in his system, because the plane is the only variable that carries **every** perceptual property, and the reason it does is that it has two dimensions to spend.

### The four levels of organization, which are the actual contribution

A variable is characterized by its *niveau d'organisation*: whether perception on it can be

- **associative**, so the variable can be ignored, and marks differing on it still read as one family,
- **selective**, so all marks in one category can be isolated in a glance,
- **ordered**, so categories sort themselves without consulting the legend,
- **quantitative**, so the reader can say *this is twice that*.

His summary ordering, quoted from the table's own text, is **`dimension du plan - taille - valeur - grain - couleur - orientation - forme`**, ordered by how many of those properties each one has.

Two findings inside that table that citations drop:

**Only size is quantitative.** "Il apparaît immédiatement que seule la variation de taille est quantitative" (spacing normalized from the OCR). Value is not: white cannot serve as a unit for measuring gray. Grain is not either, though he allows that a ratio between two coarse grains can be judged.

**Associativity breaks the pattern.** He flags it himself: no retinal variable has all the properties the way the plane does, and the inclusive nesting of properties is disturbed because associativity is **absent** from size and value. Both are *dissociative*: they dominate whatever else you combine them with. Vary size and the hue in the small marks stops being readable. That is a composition rule, and it is the part of Bertin that survives contact with practice most directly.

He also puts numbers on size that are testable and rarely quoted: roughly 20 distinguishable steps between two points whose areas stand in a 1:10 ratio, but only 4 or 5 steps that are reliably **selective**.

### Efficiency, defined as a measurable thing, in 1967

His definition is operational, not aesthetic. Paraphrasing the passage tightly: given a question, and all else equal, the construction that yields a correct and complete answer in a shorter perception time is the more efficient one for that question. He attributes the underlying idea of mental cost to Zipf.

That is a specification for an experiment. Nobody in the book runs it. Everything that later got measured, [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) onward, is testing a version of a question Bertin had already posed in a testable form.

Alongside it sits his definition of the **image**, which does extract cleanly: **"Nous appelerons IMAGE la forme visuelle significative perceptible dans l'instant minimum de vision."** The significant visual form perceptible in the minimum instant of vision. The most efficient constructions are the ones where any question, at any level, is answered inside a single image.

### What gets attributed to later authors

- **"Marks and channels"** is [Munzner's](tamara-munzner.md) vocabulary. The underlying split is Bertin's `implantation` (point, line, zone) crossed with the retinal variables. This wiki's [channels.md](../concepts/channels.md) rests on Cleveland & McGill and mentions Bertin exactly once, inside a quotation of Cleveland & McGill.
- **"Expressiveness and effectiveness"** is Mackinlay (1986), which formalizes Bertin's levels of organization into automatable criteria. Mackinlay's paper was **not reached** for this page (403 at two hosts), so treat that lineage as reported rather than verified.
- **The channel ranking** everyone quotes is [Cleveland](william-cleveland.md) & McGill's, and it is an *accuracy* ordering derived from experiments. Bertin's ordering is by *number of perceptual properties* and rests on no experiment. Conflating the two is common and it produces a specific, checkable error: **Bertin puts `taille` immediately after the plane and calls it the only quantitative retinal variable, while Cleveland & McGill measure area at rank 4**, below length and angle. For a point mark, Bertin's `taille` is area. The two orderings disagree, because they are ordering different things.

### The thing he is not credited for at all

A third of the book is networks and maps. The subtitle is *les diagrammes, les réseaux, les cartes*. His network chapter states, as a definition rather than a caveat, that in a network the size of the dots and the length and shape of the lines carry **no meaning in the plane** by default: only their presence signifies. That is the same observation this wiki's [network-topology.md](../chart-types/network-topology.md) index builds its central argument on, arrived at independently, and Bertin has priority on it by about fifty years.

## Works, and where they sit in this wiki

- ***Sémiologie graphique*** (1967; 2nd ed. 1973; 3rd ed. EHESS 1999). **No source page in this wiki.** This is the page that would have to be written to close the gap; everything above is a person-level summary and does not substitute for a chapter-by-chapter enumeration in [roll-call.md](../roll-call.md).
- ***La graphique et le traitement graphique de l'information*** (Flammarion, 1977), the shorter restatement he says shows that nothing essential changed. **Not reached, not covered.**
- ***Semiology of Graphics*** (Berg trans., Wisconsin 1983; ESRI Press 2010), the English text everyone actually cites. **Not consulted.** Anyone quoting Bertin in English should be quoting Berg, and this page cannot vouch for Berg's wording.

**The scale of the gap, stated precisely.** Before this page, Bertin appeared in this wiki twice: once inside a [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) quotation excluding hue from their ranking, and once in [skau-kosara-2016.md](../studies/skau-kosara-2016.md) as one of the authors who treated angle as the pie chart's mechanism. He has no row in [roll-call.md](../roll-call.md) and no entry in [inventory.md](../inventory.md). That is the same structural failure the [Tufte page](../sources/tufte.md) records, and for the same reason: the roll-call's audit only catches omissions in sources somebody enumerated.

## Links

- [concepts/channels.md](../concepts/channels.md), the accuracy ordering, which is not his ordering
- [concepts/evidence-class.md](../concepts/evidence-class.md), why "no experiments" is a label rather than a criticism here
- [chart-types/network-topology.md](../chart-types/network-topology.md), which reaches his network conclusion independently
- [chart-types/hive-plot.md](../chart-types/hive-plot.md), a coordinate-assigning network layout, which is his circular construction with a rule attached
- [edward-tufte.md](edward-tufte.md), the other theorist in this section whose most-cited rule is authority-asserted
- [tamara-munzner.md](tamara-munzner.md) and [sources/munzner-vad.md](../sources/munzner-vad.md), the textbook that carries his framework into the modern literature under different names
- [william-cleveland.md](william-cleveland.md), who measured what Bertin only specified a way to measure
