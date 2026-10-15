---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
author: jonathan-schwabish
---

# Jonathan Schwabish

An Urban Institute economist who teaches research communication through four books, the Graphic Continuum, PolicyViz and the One Chart at a Time videos. A synthesizer, not an experimentalist.

**What it is good for.** Chart-type breadth and when-to-use judgment, written for people who make charts as part of another job.

**What it does not settle.** Nothing here is evidence-backed on its own authority. The JEP article sources its claims to Few, Healey and Enns, Cleveland, Tufte, Skau and others, and the books are catalogs of judgment. The 2014 article's tool sections are dated (Adobe Kuler, Flash, TileMill). Every chapter's prose is unread, so this page says where a type sits ([Chapter memberships](#chapter-memberships-verified-from-the-contents-pages)), never what the book argues about it.

**How this was read.** The status is split.

- `primary-read`: **"An Economist's Guide to Visualizing Data"** (*Journal of Economic Perspectives* 28(1), Winter 2014, 209-234), the complimentary PDF downloaded from aeaweb.org with `curl`, a browser user-agent and a referer, and extracted locally with `pdftotext`.
- `primary-read`: the PolicyViz pages quoted below (the Graphic Continuum and One Chart at a Time announcements, the "Inside *Better Data Visualizations*" post, the About page, the June 2025 post on legends in titles) and the Columbia University Press product page with its contents listing, all fetched and converted locally.
- `primary-read`: the chapter memberships of *Better Data Visualizations*, from its contents pages (pp. viii-x) in the Google Books preview. The preview warns "some pages are omitted", but the contents pages were fully legible.
- `secondary-only`: the text of all four books, known only from the publisher, the author's summary or a blurb, labeled inline. No free excerpt of *Better Data Visualizations* was found, unlike [knaflic-swd.md](knaflic-swd.md). A paid PDF e-book exists (ISBN 9780231550154, Columbia UP app), despite a February 2021 comment by Schwabish that there would be none.

---

## The body of work, and which parts are reachable

| Artifact | Year | Reachable free | What it covers |
|---|---|---|---|
| Graphic Continuum (with Severino Ribecca) | 2014 | Announcement post yes, poster is a paid print | ~90 chart types across six categories |
| "An Economist's Guide to Visualizing Data", *JEP* | 2014 | **Yes, full text** | Three principles, eight redesigns, a form/function grid |
| *Better Presentations* (Columbia UP) | 2016 | No | Preparing, designing and delivering data-rich talks |
| *Elevate the Debate* (Wiley) | 2020 | No | A multilayered research-communication strategy, co-authored with Urban's communications staff |
| *Better Data Visualizations* (Columbia UP) | 2021 | No | The chart-type catalog. 464 pages |
| One Chart at a Time | 2021 | **Yes, YouTube** | 50+ short videos, one chart type each, 50+ different presenters |
| *Data Visualization in Excel* (A K Peters/CRC) | 2023 | No | How to build the charts, one chapter per chart |

Andy Kirk's blurb for the Excel book on the Routledge page: "there are three core questions: what, when, and how. What different options exist. When should I use. How do I make them." *Better Data Visualizations* is the what and the when, the question [../inventory.md](../inventory.md) topic 5 asks.

## His taxonomy, as content source and as index

The best candidate in the corpus for type-page content, and a poor index scheme ([../chart-types/README.md](../chart-types/README.md)).

### The scheme

> "We've plotted nearly 90 different graphics across five main categories: Distribution, Time, Comparing Categories, Geospatial, Part-to-Whole, and Relationships."

The Graphic Continuum announcement says five and lists six. The book reorganizes the same space, per "Inside *Better Data Visualizations*":

> "Here, I discuss each of more than eighty different graphs, charts, and diagrams split across six different data categories: comparing categories, time, distribution, geospatial, relationship, and part-to-whole. There is also a chapter on visualizing qualitative data, which is something that seems to have escaped many data visualization books to date. Finally, I've included a chapter on good table design"

On the lineage: "The organization of the book mimics my Graphic Continuum projects." The CUP contents listing, verbatim:

```
Part II: Chart Types
4. Comparing Categories
5. Time
6. Distribution
7. Geospatial
8. Relationship
9. Part-to-Whole
10. Qualitative
11. Tables
```

### Chapter memberships, verified from the contents pages

Part Two runs pp. 65-346, 282 of 464 pages, about 61% of the book.

| Chapter | Types, in the book's order |
|---|---|
| **4. Comparing Categories** (65) | Bar, Paired Bar, Stacked Bar, Diverging Bar, Dot Plot, Marimekko and Mosaic, Unit/Isotype/Waffle, Heatmap, Gauge and Bullet, Bubble Comparison and Nested Bubbles, **Sankey Diagram**, **Waterfall** |
| **5. Time** (133) | Line, Circular Line, Slope, Sparklines, Bump, Cycle, Area, Stacked Area, Streamgraph, Horizon, Gantt, Flow Charts and Timelines, Connected Scatterplot |
| **6. Distribution** (179) | Histogram, Pyramid, **Visualizing Statistical Uncertainty with Charts** (187), Box-and-Whisker, Candlestick, Violin, Ridgeline, **Visualizing Uncertainty by Showing the Data** (204), Stem-and-Leaf |
| **7. Geospatial** (217) | Choropleth, Cartogram, Proportional Symbol and Dot Density, Flow Map |
| **8. Relationship** (249) | Scatterplot, Parallel Coordinates, **Radar**, **Chord Diagram**, **Arc Chart**, Correlation Matrix, **Network Diagrams**, **Tree Diagrams** |
| **9. Part-to-Whole** (289) | Pie, Treemap, Sunburst, **Nightingale**, Voronoi |
| **10. Qualitative** (311) | Icons, Word Clouds and Specific Words, Word Trees, Specific Words, Quotes, Coloring Phrases, Matrices and Lists |
| **11. Tables** (327) | The Ten Guidelines of Better Tables, plus two worked redesigns |

The two uncertainty sections (pp. 187 and 204) are the one place his catalog overlaps this wiki's statistical-honesty studies on something measured.

### Where he and the FT disagree about membership

Names map cleanly to the [FT's](ft-visual-vocabulary.md) scheme. Memberships do not.

- **Networks.** He files Network Diagrams, Chord, Arc and Tree under Relationship. The FT files Chord and Network under Flow. That corroborates this wiki's split of [network-topology](../chart-types/network-topology.md) out of Flow (a network is a dataset, not a message), which remains `authority-asserted`.
- **Sankey and Waterfall** are comparison charts to him. The FT puts Sankey under Flow and Waterfall under Part-to-whole and Flow. Two charts in three categories across two schemes: the taxonomies are retrieval aids, not facts about charts.
- **Radar** is relationship to him, magnitude to the FT.
- **Arc** is a relationship chart to him. The FT's "Arc" is a parliament hemicycle under part-to-whole, a different form under the same name.
- **Heatmap** is Comparing Categories to him. The FT has XY heatmap under Correlation and Heat map under Spatial.

He is a source for what belongs on a type page, not for where the type is filed.

### Types he covers that the FT list does not

Gauge and Bullet, Nested Bubbles, Circular Line, Sparklines, Bump, Cycle, Streamgraph, Horizon, Gantt, Ridgeline, Stem-and-Leaf, Correlation Matrix, Tree Diagrams, Sunburst, Nightingale, and the Qualitative and Tables chapters, which have no FT equivalent. Marimekko, Pyramid and Candlestick appear in the FT under other names (Proportional stacked bar, Population pyramid, Stock price).

### Mapped against the FT nine

Names only, not contents.

| Schwabish (BDV Part II) | FT Visual Vocabulary |
|---|---|
| Comparing Categories | Magnitude **and** Ranking |
| Time | Change over Time |
| Distribution | Distribution |
| Geospatial | Spatial |
| Relationship | Correlation |
| Part-to-Whole | Part-to-Whole |
| Qualitative | *no equivalent* |
| Tables | *no equivalent* |
| *no equivalent* | Deviation |
| *no equivalent* | Flow |

His scheme is strictly coarser. Comparing Categories absorbs Magnitude and Ranking, losing the FT's definition of Part-to-Whole and Magnitude against each other by what the reader wants. Deviation and Flow have no home in it.

The FT has no relationship for text and none for "this should be a table". Schwabish is the citable precedent for `tables.md` and `qualitative.md` indexes beside the FT nine, on the footing of `network-topology.md`. A Tables index would give [../inventory.md](../inventory.md) topic 4 ("should this be a chart at all") a place in the tier.

His value is per-type text (slots 2 to 6 of a type page). CUP says the book covers "more than eighty visualization types, from histograms to horizon charts, ridgeline plots to choropleth maps, and explains how each has its place in the visual toolkit", which is unvouched. That text stays `secondary-only` until the book is opened, a different evidence class from [../chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md).

### One Chart at a Time

More than fifty free videos, one type each, built as a companion to the book: "One of my goals in that book is to help expand readers' graphic literacy. Instead of relying on the tried-and-true bar, line, and pie charts, what about trying a slope chart, dot plot, or tile grid map?" The brief to every contributor:

> "Can you please describe the graph?"
>
> "Can you please describe any considerations chart makers need to take into account when creating this type of chart?"
>
> "Can you please share an example of this chart you really like?"

Those match slots 1 and 6 of the type-page template, plus an example. Each video is one presenter's `authority-asserted` view, and there are fifty-odd presenters. The series does not mirror the book: "Not every graph, chart, and diagram in the book is covered in this video series." Contributors include Claus Wilke, Cole Nussbaumer Knaflic, Robert Kosara, Steve Franconeri, Steve Haroz, Kenneth Field, Alice Feng and Severino Ribecca.

## The five guidelines

*Better Data Visualizations* chapter 2 is "Five Guidelines for Better Data Visualizations". His post about the book lists them:

> "Show the Data
>
> Reduce the Clutter
>
> Integrate Graphics and Text
>
> Small Multiples (or, as I call it in the book, Avoid the Spaghetti Chart)
>
> Start with Gray."

He adds: "I think this last guideline can be especially helpful -- make everything gray so that you are forced to make purposeful decisions about your data visualizations."

The book's types-of-visualization chapter "is largely based on this blog post and this article I wrote for the *Journal of Economic Perspectives* in 2014." That article states the first three as "Three basic principles", readable at primary:

> "First, show the data."
>
> "Second, reduce the clutter. Chart clutter, the use of unnecessary or distracting visual elements, will tend to reduce effectiveness."
>
> "Third, integrate the text and the graph. Standard research reports often suffer from the 'slideshow effect,' in which the writer narrates the text elements that appear in the graph. A better model is one in which visualizations are constructed to complement the text and at the same time to contain enough information to stand alone"

The article is a free, vouched proxy for those three, not for the catalog, which did not exist in 2014.

## Audience

"Presenting to non-expert audiences" describes *Better Presentations* and *Elevate the Debate* (a multiplatform communication strategy, written with Urban's communications department). *Better Data Visualizations* names the makers in its subtitle ("Scholars, Researchers, and Wonks").

The JEP article states [../inventory.md](../inventory.md) topic 3, the exploratory/explanatory distinction, as an obligation on research figures:

> "One thing researchers should keep in mind is that graphs in research reports or articles, and even those shown in verbal presentations, are not meant for the author, but for the reader or the seminar audience. The line chart that a researcher uses in the data exploration phase -- with default gridlines, tick marks, and colors -- may not be the one that will best communicate the researcher's ideas to others."

## Where he touches rules this wiki has argued about

**Zero baselines.** In 2014 he scopes the rule to the mark:

> "When it comes to bar and column charts, a first rule is to start the chart at zero. Otherwise, the differences between the columns are overemphasized."

That puts him with Observable Plot and the FT on the stronger form of topic 9, against Vega-Lite's by-axis default. He and the Urban Institute style guide count as one voice. He is a Senior Fellow at Urban and the guide's sole named contact ("Contact Jon Schwabish", at an `@urban.org` address, [urban-institute.md](urban-institute.md)).

**Pie charts.** The angle mechanism [refutations.md](../refutations.md) records as refuted appears here. He first reports it as one side of a debate, beginning "But others argue that":

> "But others argue that because pie charts force readers to make comparisons using the areas of the slices or the angles formed by the slices -- something that our visual perception does not accurately support -- they are not an effective way to communicate information."

The next paragraph is in his own voice, and angle-based:

> "Pie chart slices that form 90-degree right angles -- that is, slices that form one-quarter increments -- are the most familiar to our eyes. Other amounts can be far more difficult to discern."

The article predates [../studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md) by two years. He notes "much of the discussion in this section is based on Few 2007", so it is Few's argument relayed, not independent support. Whether the 2021 book repeats it is unknown.

He calls the debate "among the most contentious in the field of data visualization" and gives pies a job: "Figure 8C shows the true purpose of the pie chart, which is to individually compare each part to the whole". His Figures 7A and 7B rotate the largest slice to 12 o'clock with the same data, and "One small change obscures the information". That anchoring effect is not covered on [../concepts/channels.md](../concepts/channels.md) or [../chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md).

**Start with Gray.** The [refutations.md](../refutations.md) entry on "gray plus one accent" finds no controlled study and credits the rule to Knaflic. Schwabish independently states a stronger version as a core rule. The evidence class is unchanged. The entry under-credits how widespread the rule is, and "one author's house style" and "the field's shared default with no experiment behind it" are different problems.

**Color in the title as a legend.** A June 2025 PolicyViz post concludes:

> "Use color in the title when it reinforces categories already made clear through other visual cues -- like bar direction or grouping. When done right, this technique can add clarity without sacrificing accessibility."

The repo's guidance recommends the technique without the condition. It is redundant encoding (inventory topic 69) applied to text, and testable: the title carries color only when removing the color loses nothing. On a red-and-green chart in the same post: "my testing shows that the red and green colors are consistent for readers with color vision deficiencies. But even if they hadn't, the colors are not critical to understanding the chart." That is the scoped red-versus-green rule, checked by simulation.

**Qualitative data has no inventory topic.** He calls it "something that seems to have escaped many data visualization books to date", and nothing in this corpus covers text or coded qualitative material. It is a candidate missing topic, like Few's *validity*.

## Lineage of the FT nine

[../chart-types/README.md](../chart-types/README.md) says the FT nine "descends from Schwabish and Ribecca (2014) by way of the FT (2016)", and his side confirms it. His own scheme gained Qualitative and Tables by 2021. The FT kept the 2014 snapshot.

## Links

- [An Economist's Guide to Visualizing Data](https://www.aeaweb.org/articles?id=10.1257/jep.28.1.209), *JEP* 28(1), 2014. Full text is complimentary
- [Better Data Visualizations](https://cup.columbia.edu/book/better-data-visualizations/9780231193115), Columbia University Press
- [Inside Better Data Visualizations](https://policyviz.com/2021/02/11/inside-better-data-visualizations-a-guide-for-scholars-researchers-and-wonks/), the author's own chapter-by-chapter summary
- [The Graphic Continuum](https://policyviz.com/2014/09/09/graphic-continuum/)
- [One Chart at a Time](https://policyviz.com/one-chart-at-a-time/)
- [PolicyViz](https://policyviz.com/), blog, podcast and workshops
- Related: [ft-visual-vocabulary.md](ft-visual-vocabulary.md), [urban-institute.md](urban-institute.md), [knaflic-swd.md](knaflic-swd.md), [../chart-types/README.md](../chart-types/README.md)
