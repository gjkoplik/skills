---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Stephen Few

**What they are known for.** Few wrote *Show Me the Numbers* and *Information Dashboard Design*, taught a generation of business analysts that a dashboard is a display problem rather than a decoration problem, and designed the bullet graph as a replacement for the gauges he spent years attacking. He is also the field's most sustained public critic, running two decades of the *Visual Business Intelligence* newsletter and blog against infographics, dashboards, vendors, "big data," data storytelling, and academic visualization research itself.

**How this was read.** Five of his articles were downloaded from perceptualedge.com and extracted locally: the effectiveness profile, *The Chartjunk Debate*, *Dual-Scaled Axes*, *Information Visualization Research as Pseudo-Science*, and the *Bullet Graph Design Specification*. His books were not read. Retrieval date: **2026-08-23**.

**What they are good for.** Two things nobody else in this set does. First, the **informative versus emotive** split: is this figure understandable, and separately, will anyone look at it. Second, **an argued critique of a specific published paper**, which is a genre the rest of the canon does not write. If you want to know what a hostile expert reader would say about a study before you cite it, Few has often already said it in print.

**What they do not settle.** Anything empirical. There is no experiment anywhere in his corpus. He is one man with strong opinions, a lot of worked examples, and an explicit refusal to pretend otherwise: "I'm not suggesting that these criteria provide scientific rigor." That refusal is the reason he is usable as an authority source and unusable as an evidentiary anchor.

---

## What their work actually established

### The effectiveness profile, which the wiki already has

Seven criteria in two groups, target *ranges* rather than target scores, and the only appearance of **construct validity** as a chart criterion anywhere in this canon. Full treatment at [sources/few-effectiveness-profile.md](../sources/few-effectiveness-profile.md), including the two inventory holes its primary reading exposed and the retrieval failure that hid them.

### The bullet graph, which is a designed artifact and not a finding

A five-component linear replacement for dashboard gauges, published as a specification: label, one linear quantitative scale, a featured measure, one or two comparative measures, and two to five qualitative ranges. It is now implemented in most BI tools. The spec argues from footprint and reading efficiency ("Its linear design not only gives it a small footprint, but also supports more efficient reading than radial meters") and cites no test. It is a good design with no study behind it, which is the correct thing to say about most good designs.

### The criticism, which is the part with a track record

**On chartjunk.** *The Chartjunk Debate* (2011) is an eleven-page attack on Bateman et al.'s *Useful Junk?*, and it is a **methodological** critique rather than a replication. He lists the assumptions he thinks the study made without warrant, including that Nigel Holmes charts represent extreme chartjunk, that the plain charts were what minimalists actually advocate, and that "a study involving 20 university students can produce trustworthy results." He also catches the authors overreaching in their own conclusion, and points out that they reported their results using plain unembellished graphs.

**This is where he earns his keep.** The wiki's [refutations.md](../refutations.md) records that Bateman's headline long-term recall result **did not replicate cleanly** in a four-way 2023 replication. Few said the sample and design would not support the claim, twelve years before the replication, without running one. He is not always right, and the same file records that Bateman's accuracy finding survives and that Skau's later bar-deformation result is compatible with it rather than opposed. But a critic with a hit rate is a different thing from a scold.

**On academic visualization research generally.** *Information Visualization Research as Pseudo-Science* (2015) opens with "Research in the field of information visualization is usually mediocre, often severely flawed, and only occasionally well done," then works a single paper (Borkin et al., *Beyond Memorability*) in detail. Before doing so he sorts vis research into four categories and insists on judging each by its own standard, which is a more careful move than the title advertises. The stance overlaps substantially with [Kosara's](robert-kosara.md) *An Empire Built On Sand*, from the opposite side of the fence and a year earlier.

### Where his name is used as authority for more than he showed

**The flat dual-axis ban, and this one is a correction worth carrying.** [refutations.md](../refutations.md) traces every strong statement of the ban to design authority, naming Few first. That is right about the lineage and it overstates his position. His 2008 article ends:

> "I certainly cannot conclude, once and for all, that graphs with dual-scaled axes are never useful; only that I cannot think of a situation that warrants them in light of other, better solutions. I invite you to propose viable exceptions, which I will welcome with open arms."

The one thing he does state flatly is narrower: "a graph with a dual-scaled axis should never exclusively encode values as bars." So the absolute ban in circulation is downstream of Few rather than from Few, which is the same degradation pattern the wiki documents for Cleveland and for Munzner, running through a practitioner instead of through a paper.

**Any rule of his quoted with "research shows" attached.** The single-screen dashboard rule is the standard case. It is mislabeled by definition, because he ran no research. His dashboard books are `not-reached` here, so the specific wording is not vouched; what is vouched is that nothing in his corpus can support a "research shows" preamble.

**"Few debunked the chartjunk study."** He critiqued it. The distinction matters and this wiki's [evidence-class.md](../concepts/evidence-class.md) exists to hold it: an argued critique moves a claim toward **contested**, and only a replication moves it to refuted. His hit rate is good. His method is reading, not measuring.

---

## What they would object to in your figure

*Reconstruction from his stated priorities. He has not seen your figure, and if he had, this would be shorter and ruder.*

He would ask, first, whether the number in the figure means anything without a comparison, because his *Completeness* criterion is about comparison context and almost every chart he critiques fails it: a value with no target, no norm, and no history. Then he would ask whether the measure is **valid**, meaning whether it measures what the title claims it measures, which is the question nobody else in this set asks. Then he would strip the figure: every gradient, every shadow, every 3D effect, every gauge, every unit chart, and the pie chart, on the grounds that they cost perceptibility and buy nothing. He would tell you the title asserts something the data cannot support. He would be unimpressed by "but it's engaging," and then, unusually, he would concede that engagement is a real criterion with a real acceptable range, just a much wider one than truthfulness gets. And if you cited a study at him, he would go read it and come back with a list.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| "Data Visualization Effectiveness Profile," *Visual Business Intelligence Newsletter*, Jan-Mar 2017 | `primary-read` | [sources/few-effectiveness-profile.md](../sources/few-effectiveness-profile.md). Grounds inventory topics 1, 3, 5, 6, 9, 10, 11, 16, 31, 33, 42, 45, 46, 89, 91, with corrections on that page. |
| "Dual-Scaled Axes in Graphs: Are They Ever the Best Solution?" (2008) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/visual_business_intelligence/dual-scaled_axes.pdf), extracted locally. | No page. Bears directly on [refutations.md](../refutations.md), "A flat ban on dual axes," and softens it. |
| "The Chartjunk Debate: A Close Examination of Recent Findings" (Apr-Jun 2011) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/visual_business_intelligence/the_chartjunk_debate.pdf), extracted locally. | No page. Pairs with [bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) and [gillan-richman-1994-data-ink.md](../studies/gillan-richman-1994-data-ink.md). |
| "Information Visualization Research as Pseudo-Science" (Oct-Dec 2015) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/visual_business_intelligence/infovis_research_as_pseudo-science.pdf), extracted locally. | No page. |
| "Bullet Graph Design Specification" (rev. 2013) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/misc/Bullet_Graph_Design_Spec.pdf), extracted locally. | Read into [chart-types/gauge-and-bullet.md](../chart-types/gauge-and-bullet.md), which cites the five components and notes the spec reports no test. |
| *Show Me the Numbers*, 2nd ed. (2012) | `not-reached`. | No page. The table-and-graph design reference the business-analytics world runs on. |
| *Information Dashboard Design*, 2nd ed. (2013) | `not-reached`. | No page. Nothing in [inventory.md](../inventory.md) covers multi-figure dashboard layout, which is a real gap for anyone building a page of charts rather than a chart. |
| *Now You See It* (2009), *Signal* (2015), *Big Data, Big Dupe* (2018) | `not-reached`. | No page. |
| The rest of the *Visual Business Intelligence Newsletter* archive | Unread; 121 open PDFs are indexed at [perceptualedge.com/library.php](https://www.perceptualedge.com/library.php). | Several are directly on-topic for uncovered inventory areas: "Save the Pies for Dessert," "Unit Charts Are For Kids," "Our Irresistible Fascination with All Things Circular," "Are Mosaic Plots Worthwhile," "Distribution Displays," "Rules for Using Color." |

**Retrieval note.** The archive is open and free; 121 PDFs are indexed at the library page linked above.

## See also

- [sources/few-effectiveness-profile.md](../sources/few-effectiveness-profile.md), the one Few page that exists
- [concepts/floor-and-ceiling.md](../concepts/floor-and-ceiling.md), his acceptable-range figure is the same idea from another direction
- [concepts/evidence-class.md](../concepts/evidence-class.md), the labeling discipline that keeps a good critic from being read as a study
- [robert-kosara.md](robert-kosara.md), the same skepticism about the field's foundations, argued from inside it and with experiments attached
