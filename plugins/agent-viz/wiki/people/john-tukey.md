---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# John Tukey

**What they are known for.** Naming and arguing for *exploratory data analysis*, the idea of asking data what it suggests before asking what it establishes, and building the hand-drawable displays that make that possible: the box-and-whisker plot and the stem-and-leaf.

**How this was read.** `primary-read` on the 1962 manifesto, `not reached` on the 1977 book. Retrieved 2026-08-23.

- **"The Future of Data Analysis"** (*Annals of Mathematical Statistics* 33(1):1-67, March 1962) was downloaded and extracted locally with `pypdf`, 68 pages. Every Tukey quote below is from that extraction. **Provenance caveat:** Project Euclid, which hosts it open access, returns a robots interstitial to `curl` and to the WebFetch tool alike. The copy read is a JSTOR scan (stable URL `2237638`) mirrored on a university course page at `mat.ufrgs.br`. It is the article, page numbering intact, but it is not the publisher's file.
- ***Exploratory Data Analysis*** (Addison-Wesley, 1977) is **not reached**. Not on the Internet Archive under any identifier tried, in copyright, no open deposit. Nothing on this page quotes it.
- **The box plot's history** comes from Wickham & Stryjewski, *40 years of boxplots* (2011), fetched and extracted locally from `vita.had.co.nz/papers/boxplots.pdf`. `primary-read` as to that paper, which is itself a secondary account of Tukey.

**What they are good for.** The question he answers: *am I plotting this to find something out, or to show somebody something*. Tukey is the canon's clearest statement that those are different jobs with different standards, and the origin of the position that the exploratory figure is allowed to be ugly, ad hoc, and thrown away.

**What they do not settle.** Whether any of his displays are read accurately. Tukey ran no perceptual experiments. The box plot is the most-used statistical graphic invented in the twentieth century and it entered the world entirely [authority-asserted](../concepts/evidence-class.md).

---

## "In the style of Tukey" means, concretely

**The medium cannot do anything fancy.** His displays were designed for pencil, graph paper, and a line printer. Monochrome. No fills. No gradients. Nothing that needs a rendering pipeline. That constraint is the aesthetic, and it is why the box plot survived the transition to every plotting library ever written: it is five numbers and some line segments.

**The data appears twice, at two resolutions.** The stem-and-leaf is a histogram whose bars are the actual digits, so the shape and the values are the same object. That is the move: a summary that has not thrown the numbers away.

**Robust summaries located at real data points.** Median not mean, fourths not standard deviations, whisker ends at an actual observation rather than at a computed distance. Nothing on a Tukey plot is at a coordinate no datum occupies.

**No tuning parameters.** A kernel density estimate has a bandwidth that can be adjusted until the answer looks right. A box plot has nothing to adjust. That is a deliberate property.

**Many small identical displays, side by side.** His plots exist to compare groups, and the comparison is done by repeating one very simple mark across a strip.

**Residuals get plotted.** Something crude is fitted, subtracted, and what is left is plotted. Half of the 1962 paper's machinery is about examining what a fit failed to absorb rather than the fit itself.

**The parts are named oddly, on purpose.** Hinge, fourth, fence, whisker, out-lier, straggler, wild shot, vacuum cleaner, FUNOP, FUNOR-FUNOM. He coined a private vocabulary and then used it flatly, and the effect is that a Tukey procedure is memorable in a way a Greek-lettered one is not. In a figure that reads as his, the label on the part is doing real work.

**The figure is a working tool, not an artifact.** Nothing in this style is meant to be published, framed, or captioned for a general reader. It is what gets drawn on the way to knowing something. That distinction is [floor-and-ceiling](../concepts/floor-and-ceiling.md) fifty years early, and it is why importing Tukey wholesale into a presentation figure goes wrong.

## What they actually established, and what gets over-claimed in their name

### The EDA argument is stated in 1962, fifteen years before the book

The 1977 book gets the credit. The position is fully formed in the 1962 paper, section 45:

> "we must plan to learn to ask first of the data what it suggests, leaving for later consideration the question of what it establishes."

The same section asks for "a free use of ad hoc and informal procedures in seeking indications", on the grounds that when the purpose is to ask what the data suggests, "it would be foolish to be bound by formalities". And the paper's opening redefines the field around it: data analysis is "a larger and more varied field than inference, or incisive procedures, or allocation."

**So "Tukey invented EDA in 1977" is a book-publication date, not an intellectual one.**

### The famous maxim is in this paper, and he puts it in quotation marks

Section 11, on facing uncertainty, page 13:

> "Far better an approximate answer to the right question, which is often vague, than an exact answer to the wrong question, which can always be made precise."

Verified verbatim. One detail everyone drops: **Tukey sets it in quotation marks and attributes it to nobody.** He introduces it as "the most important maxim for data analysis to heed". Whether he is coining it or quoting an unnamed source is not resolvable from the text, and it is universally attributed to him without the quotation marks.

### He did not invent the box plot's shape

Wickham & Stryjewski are blunt about this:

> "The basic graphic form of the boxplot, the range-bar, was established in the early 1950's Spear (1952, pg. 164). Tukey's contribution was to think deeply about appropriate summary statistics that worked for a wide range of data and to connect those to the visual components of the range bar."

The invention is the choice of statistics, not the picture. Also from the same paper: what he first published in the 1970 preliminary edition he called a **schematic plot**, and "it did not become widely known until formal publication (Tukey, 1977)."

### The box plot does not show quartiles, and its whiskers are frequently misdescribed

Tukey's box ends are **hinges**, the upper and lower **fourths**, which are not identical to quartiles under most quantile definitions. Wickham & Stryjewski note that implementations differ further, citing Hyndman & Fan's nine quantile types, that some replace the extremes with fixed quantiles, and that multipliers other than 1.5 are in use.

**One thing to be careful about, flagged rather than resolved.** Wickham & Stryjewski describe the fences as lying "1.5 times the inter-fourth range from the **median**". The standard definition, and the one every implementation I know of uses, puts the inner fences at 1.5 times the H-spread from the **hinges**, not from the median. Those are different constructions and they give different plots. I could not settle it against the primary because *Exploratory Data Analysis* was not reached. **Neither phrasing is vouched as Tukey's own wording on the strength of this page.**

### The one perceptual result in the vicinity goes against a redesign, not against Tukey

Wickham & Stryjewski report that Tufte proposed a box-less **midgap** variant to improve the box plot's data-ink ratio, and that:

> "perceptual studies (Stock and Behrens, 1991) have found Tufte's variation to be substantially less accurate than the original."

**Stock & Behrens itself was not reached**, so that is a reported result. A data-ink minimization was measured against the thing it minimized, and it lost. It belongs on the [Tufte page](edward-tufte.md) as much as this one.

### What the box plot cannot do, and he knew

There is no display of group size, so no way to judge whether a difference between two boxes means anything. McGill & Larsen's 1978 variable-width and notched variants exist precisely to patch that, and almost nobody uses them.

More broadly, the box plot's five numbers hide multimodality completely, which is the argument [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) make for plotting the points at small n, and it is a Tukey-descended argument rather than an anti-Tukey one: show more of the data, not less.

### The coinages, which are folklore-adjacent

"Bit" (1947) is securely his. **"Software" is not settled**: his 1958 *American Mathematical Monthly* article carries the earliest known printed use in the computing sense, and there are competing priority claims for earlier unpublished use. `secondary-only` here; neither source was opened, and the confident "Tukey coined software" is more confident than the record.

### The over-claim to avoid

"Tukey showed that you should look at your data before modeling it." He argued it, at length and persuasively, and produced tools for doing it. He did not show it. No experiment in this material compares an exploratory-first workflow against a model-first one on any outcome. It is a strong and probably correct piece of authority assertion by a formidable authority, and it is not evidence.

## Works, and where they sit in this wiki

- **"The Future of Data Analysis"** (1962). **No study page**, though it earns one more than most things here. Read in full for this page.
- ***Exploratory Data Analysis*** (1977). **No page, not reached.** The box plot, the stem-and-leaf, the fences and the hinges all have their definitive statement here and this wiki has never opened it. That is the single largest reachability gap on this page.
- **"Some Graphic and Semigraphic Displays"** (1972). **Not reached, not covered.**
- ***The Collected Works of John W. Tukey***, volumes on graphics. On the Internet Archive as a lending item (`collectedworksof0001tuke`), so text extraction was not attempted.

**Coverage before this page: zero.** Tukey appeared nowhere in this wiki, which is odd given that [Cleveland & McGill](../studies/cleveland-mcgill-1984.md), the study the whole [channels](../concepts/channels.md) tier rests on, comes directly out of the Bell Labs statistical-graphics tradition he built. See [william-cleveland.md](william-cleveland.md).

## Links

- [concepts/floor-and-ceiling.md](../concepts/floor-and-ceiling.md), the exploratory-versus-presentation split, which is his distinction
- [concepts/evidence-class.md](../concepts/evidence-class.md), where "the box plot is standard practice" actually sits
- [studies/weissgerber-2015-beyond-bar-line.md](../studies/weissgerber-2015-beyond-bar-line.md), plot the points at small n
- [studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md), which measures bar-and-whisker against gradient and violin and finds the encoding changes the decision
- [edward-tufte.md](edward-tufte.md), whose redesign of the box plot is the one Tukey artifact anybody has measured
- [jacques-bertin.md](jacques-bertin.md), working the same decade on the opposite question: not what to compute, but what a mark can carry
