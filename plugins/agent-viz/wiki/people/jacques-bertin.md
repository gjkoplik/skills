---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Jacques Bertin

**What they are known for.** *Sémiologie graphique* (1967), the first treatment of graphics as a formal sign system, and the source of the visual variables. Modern encoding vocabularies (marks and channels, expressiveness, levels of measurement) re-lexicalize his.

**How this was read.** The full French text was downloaded and extracted locally, with three limits.

- It is the 3rd edition (EHESS, 1999), a reprint of the 1973 2nd edition plus a new preface and a chapter on *la graphique*. The preface dates the book (written 1965, published 1967, revised 1971) and confirms the 1973 text is what was reissued.
- The English translation (Berg, 1983; ESRI Press, 2010) was not consulted. English terms here render the French, with the French word named where the literature has settled on one (*value* for `valeur`, *grain* or *texture* for `grain`).
- The scan is an in-copyright book on Monoskop with poor OCR. Quotes are only fragments that extracted cleanly. Mangled passages are paraphrased, and marked as such.

**What they are good for.** What a variable can carry. His levels of organization ask not "how precisely can this be read" but "can this variable be selected, ordered, or measured at all". He also treats networks as a graphic problem with its own construction rules.

**What they do not settle.** Anything empirical. The book has no experiments, and its *Tests* are demonstrations over a facing-page figure (isolate one category, then judge whether that was possible), and his orderings are [authority-asserted](../concepts/evidence-class.md) throughout.

## "In the style of Bertin" means, concretely

**Monochrome, with texture for sequence.** Black ink on white paper, differentiated by `grain` (dot density and coarseness) and `valeur` (lightness). In his ordering `grain` and `valeur` are ordered and `couleur` is not, so hue goes to categories and lightness or texture to anything with a sequence.

**Grids and the reorderable matrix.** Dozens of miniature maps or dot-fields in rows and columns read as one image. The *matrice ordonnable* makes rows and columns physical strips, permuted by hand until structure appears, so the sorting is the analysis.

**A legend with the invariant and the components.** His analysis separates what is constant across the graphic (the *invariant*) from what varies (the *composantes*). The title names the invariant, and the legend lists the components with their length and level of organization. Imitations usually drop this.

**No decoration.** The third-edition preface: "la graphique n'est pas un art. C'est un langage scientifique".

**Network layouts.** His *rectilinear construction* (elements on a line, links curving to either side) and *circular construction* (elements on a circle, links as straight chords) are the arc and chord diagrams, given with trade-offs in 1967. He argues the circular one gives the least confused image a priori, whatever the crossings in the raw data.

## What they established, and what gets over-claimed in their name

### There are eight visual variables, not seven

The book says eight: **"Le dessinateur dispose ainsi de huit variations sensibles."** They are the two dimensions of the plane plus six *retinal* variables a mark fixed in the plane can still vary on.

| French | Usual English |
|---|---|
| les deux dimensions du plan | the two planar dimensions |
| taille | size |
| valeur | value (lightness) |
| grain | grain, usually translated texture |
| couleur | color (hue) |
| orientation | orientation |
| forme | shape |

Lists of seven fold the two planar dimensions into one "position", but in his system the plane has every perceptual property because it has two dimensions to spend.

### The four levels of organization

His central contribution. A variable's *niveau d'organisation* says whether perception on it is

- **associative**: marks differing on it still read as one family,
- **selective**: one category can be isolated at a glance,
- **ordered**: categories sort themselves without the legend,
- **quantitative**: the reader can say *this is twice that*.

His summary ordering, from the table's own text, is **`dimension du plan - taille - valeur - grain - couleur - orientation - forme`**, by how many of those properties each has.

**Only size is quantitative.** "Il apparaît immédiatement que seule la variation de taille est quantitative" (spacing normalized from the OCR). Value is not, since white cannot be a unit for measuring gray. Grain is not either, though a ratio between two coarse grains can be judged.

**Size and value are dissociative.** Associativity is absent from both, which breaks the nesting of properties. They dominate whatever they are combined with, so varying size makes the hue of small marks unreadable. This composition rule carries over to practice most directly.

**Size steps.** About 20 distinguishable steps between two points whose areas stand in a 1:10 ratio, but only 4 or 5 that are reliably **selective**.

### Efficiency, defined in testable terms

In close paraphrase: for a given question, all else equal, the construction that gives a correct and complete answer in less perception time is more efficient. He credits the idea of mental cost to Zipf. The book never runs this experiment. Later measurement, from [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) on, tests versions of it.

He defines the **image** as the significant form seen in the minimum instant of vision: **"Nous appelerons IMAGE la forme visuelle significative perceptible dans l'instant minimum de vision."** The most efficient constructions answer any question inside a single image.

### What gets attributed to later authors

- **Marks and channels** is [Munzner's](tamara-munzner.md) vocabulary for Bertin's `implantation` (point, line, zone) crossed with the retinal variables. [channels.md](../concepts/channels.md) rests on Cleveland & McGill and mentions Bertin once, inside a quotation of them.
- **Expressiveness and effectiveness** is Mackinlay (1986), formalizing the levels of organization as automatable criteria. Mackinlay was not reached (403 at two hosts), so the lineage is reported, not verified.
- **The channel ranking** usually quoted is [Cleveland](william-cleveland.md) & McGill's accuracy ordering, from experiments. Bertin's counts perceptual properties and has no experiment. They disagree checkably: Bertin puts `taille`, which for a point mark is area, right after the plane as the only quantitative retinal variable, while Cleveland & McGill measure area below length and angle.

### Networks, uncredited

A third of the book is networks and maps (subtitle *les diagrammes, les réseaux, les cartes*). His network chapter defines that, by default, dot size and line length and shape carry no meaning in the plane: only presence signifies. [network-topology.md](../chart-types/network-topology.md) rests its central argument on the same observation, reached independently about fifty years later.

## Works, and where they sit in this wiki

- ***Sémiologie graphique*** (1967; 2nd ed. 1973; 3rd ed. EHESS 1999). No source page, and no chapter-by-chapter enumeration in [roll-call.md](../roll-call.md).
- ***La graphique et le traitement graphique de l'information*** (Flammarion, 1977), a shorter restatement he says changes nothing essential. Not reached.
- ***Semiology of Graphics*** (Berg trans., Wisconsin 1983; ESRI Press 2010), the English text everyone cites. Not consulted, so Berg's wording is unvouched here.

He is cited in a [Cleveland & McGill](../studies/cleveland-mcgill-1984.md) quotation excluding hue, and in [skau-kosara-2016.md](../studies/skau-kosara-2016.md) among authors who treated angle as the pie's mechanism. He has no row in [roll-call.md](../roll-call.md) and no entry in [inventory.md](../inventory.md), the gap [sources/tufte.md](../sources/tufte.md) records for Tufte: the roll-call audit only catches omissions in sources somebody enumerated.

## Links

- [concepts/channels.md](../concepts/channels.md): the accuracy ordering, which is not his
- [concepts/evidence-class.md](../concepts/evidence-class.md): why "no experiments" is a label here, not a criticism
- [chart-types/network-topology.md](../chart-types/network-topology.md): reaches his network conclusion independently
- [chart-types/hive-plot.md](../chart-types/hive-plot.md): his circular construction with a coordinate rule attached
- [edward-tufte.md](edward-tufte.md): the other theorist here whose most-cited rule is authority-asserted
- [tamara-munzner.md](tamara-munzner.md) and [sources/munzner-vad.md](../sources/munzner-vad.md): his framework under modern names
- [william-cleveland.md](william-cleveland.md): who measured what Bertin specified a way to measure
