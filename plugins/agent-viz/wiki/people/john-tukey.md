---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# John Tukey

**What they are known for.** *Exploratory data analysis*, asking data what it suggests before what it establishes, and the hand-drawable displays for it: the box-and-whisker plot and the stem-and-leaf.

**How this was read.** `primary-read` on the 1962 manifesto, `not reached` on the 1977 book.

- **"The Future of Data Analysis"** (*Annals of Mathematical Statistics* 33(1):1-67, March 1962), extracted locally with `pypdf`. Every Tukey quote below is from it. Project Euclid, the open-access host, serves `curl` and WebFetch a robots interstitial, so the copy read is a JSTOR scan (stable URL `2237638`) mirrored on a course page at `mat.ufrgs.br`: the article with page numbering intact, not the publisher's file.
- ***Exploratory Data Analysis*** (Addison-Wesley, 1977): in copyright, no open deposit, not on the Internet Archive under any identifier tried.
- **Box plot history**: Wickham & Stryjewski, *40 years of boxplots* (2011), extracted locally from `vita.had.co.nz/papers/boxplots.pdf`. `primary-read` as to that paper, itself a secondary account of Tukey.

**What they are good for.** *Am I plotting this to find something out, or to show somebody something?* He is the canon's clearest statement that those are different jobs with different standards, and that an exploratory figure may be ugly, ad hoc and thrown away.

**What they do not settle.** Whether any of his displays are read accurately. He ran no perceptual experiments. The box plot is the most-used statistical graphic invented in the twentieth century, and it entered the world entirely [authority-asserted](../concepts/evidence-class.md).

---

## "In the style of Tukey" means, concretely

- **Pencil, graph paper, line printer**: monochrome, no fills, no gradients. The box plot survived into every plotting library because it is five numbers and some line segments.
- **The data at two resolutions.** A stem-and-leaf is a histogram whose bars are the digits.
- **Robust summaries at data points.** Median not mean, fourths not standard deviations, whiskers ending at an observation. With an odd count, nothing on a Tukey plot is at a coordinate no datum occupies.
- **No tuning parameters**, unlike a kernel density estimate's bandwidth, which can be adjusted until the answer looks right.
- **Many small identical displays, side by side**, to compare groups.
- **Residuals get plotted**, and half the 1962 paper's machinery examines what a crude fit failed to absorb.
- **Odd names for the parts**: hinge, fourth, fence, whisker, out-lier, straggler, wild shot, vacuum cleaner, FUNOP, FUNOR-FUNOM. They make a procedure memorable in a way a Greek-lettered one is not.
- **A working tool, not an artifact**, never meant for a general reader. That is the [floor-and-ceiling](../concepts/floor-and-ceiling.md) distinction fifty years early, and why importing Tukey wholesale into a presentation figure goes wrong.

## What they established, and what gets over-claimed in their name

### EDA is stated in 1962, fifteen years before the book

Section 45 of the 1962 paper:

> "we must plan to learn to ask first of the data what it suggests, leaving for later consideration the question of what it establishes."

The same section asks for "a free use of ad hoc and informal procedures in seeking indications", since when asking what the data suggests "it would be foolish to be bound by formalities". The opening calls data analysis "a larger and more varied field than inference, or incisive procedures, or allocation." "Tukey invented EDA in 1977" is a publication date, not an intellectual one.

### The famous maxim is in quotation marks in the original

Section 11, page 13:

> "Far better an approximate answer to the right question, which is often vague, than an exact answer to the wrong question, which can always be made precise."

Tukey sets it in quotation marks, attributes it to nobody, and introduces it as "the most important maxim for data analysis to heed". Whether he coined it or quoted someone is not resolvable from the text. It is universally attributed to him, without the quotation marks.

### He did not invent the box plot's shape

> "The basic graphic form of the boxplot, the range-bar, was established in the early 1950's Spear (1952, pg. 164). Tukey's contribution was to think deeply about appropriate summary statistics that worked for a wide range of data and to connect those to the visual components of the range bar."

He first published it in the 1970 preliminary edition as a **schematic plot**, and "it did not become widely known until formal publication (Tukey, 1977)."

### Hinges are not quartiles, and the whiskers are often misdescribed

Tukey's box ends are **hinges**, the upper and lower **fourths**, which differ from quartiles under most quantile definitions. Wickham & Stryjewski list further variation: Hyndman & Fan's nine quantile types, fixed quantiles replacing the extremes, and multipliers other than 1.5.

They place the fences "1.5 times the inter-fourth range from the **median**". The standard definition, and every implementation known to this page's author, puts the inner fences 1.5 H-spreads from the **hinges**, which gives a different plot. Without *Exploratory Data Analysis* this cannot be settled, so neither phrasing is vouched for as Tukey's wording.

### The one perceptual result nearby goes against a redesign, not against Tukey

Of Tufte's box-less **midgap** variant, built to improve the data-ink ratio, Wickham & Stryjewski report:

> "perceptual studies (Stock and Behrens, 1991) have found Tufte's variation to be substantially less accurate than the original."

Stock & Behrens was not reached, so this is a reported result. See the [Tufte page](edward-tufte.md).

### What the box plot cannot do, and he knew

It hides group size, so nothing shows whether a difference between two boxes means anything. McGill, Tukey & Larsen's 1978 variable-width and notched variants patch that, and almost nobody uses them. The five numbers also hide multimodality. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) argue for plotting the points at small n, a Tukey-descended argument: show more of the data, not less.

### The coinages

"Bit" (1947) is securely his. **"Software" is not settled**: his 1958 *American Mathematical Monthly* article carries the earliest known printed use in the computing sense, and there are competing priority claims for earlier unpublished use. `secondary-only` here; neither source was opened, and the confident "Tukey coined software" is more confident than the record.

### The over-claim

"Tukey showed that you should look at your data before modeling it." He argued it and built tools for it, but did not show it. No experiment in this material compares exploratory-first and model-first workflows on any outcome. It is a strong, probably correct authority assertion, not evidence.

## Works, and where they sit in this wiki

- **"The Future of Data Analysis"** (1962). **No study page.** Read in full.
- ***Exploratory Data Analysis*** (1977). **No page, not reached**, though the box plot, stem-and-leaf, fences and hinges have their definitive statement there.
- **"Some Graphic and Semigraphic Displays"** (1972). **Not reached.**
- ***The Collected Works of John W. Tukey***, graphics volumes. An Internet Archive lending item (`collectedworksof0001tuke`), not extracted.

[Cleveland & McGill](../studies/cleveland-mcgill-1984.md), the study the [channels](../concepts/channels.md) tier rests on, comes out of the Bell Labs statistical-graphics tradition he built ([william-cleveland.md](william-cleveland.md)).

## Links

- [concepts/floor-and-ceiling.md](../concepts/floor-and-ceiling.md): his exploratory-versus-presentation split
- [concepts/evidence-class.md](../concepts/evidence-class.md): where "the box plot is standard practice" sits
- [studies/weissgerber-2015-beyond-bar-line.md](../studies/weissgerber-2015-beyond-bar-line.md): plot the points at small n
- [studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md): bar-and-whisker measured against gradient and violin, where the encoding changes the decision
- [edward-tufte.md](edward-tufte.md): the box plot redesign, the one Tukey artifact anybody has measured
- [jacques-bertin.md](jacques-bertin.md): the same decade, on what a mark can carry rather than what to compute
