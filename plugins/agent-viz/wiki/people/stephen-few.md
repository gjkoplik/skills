---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Stephen Few

**What they are known for.** *Show Me the Numbers* and *Information Dashboard Design*, which taught business analysts to treat a dashboard as a display problem, and the bullet graph, his replacement for gauges. Also the field's most sustained public critic, in two decades of the *Visual Business Intelligence* newsletter and blog against infographics, vendors, "big data," data storytelling and academic visualization research.

**How this was read.** Five articles from perceptualedge.com, the `primary-read` rows in the table below, were extracted locally. His books were not read.

**What they are good for.** The **informative versus emotive** split (is it understandable, and separately, will anyone look) and **argued critiques of specific published papers**, which the rest of the canon does not write. He has often already put in print what a hostile expert would say about a study.

**What they do not settle.** Anything empirical. His corpus contains no experiment, and he says so: "I'm not suggesting that these criteria provide scientific rigor." That makes him an authority source, not an evidentiary anchor.

---

## What their work established

**The effectiveness profile.** Seven criteria in two groups, with target *ranges*, not scores. No other source in this canon uses **construct validity** as a chart criterion. [sources/few-effectiveness-profile.md](../sources/few-effectiveness-profile.md) covers it, including two inventory holes it exposed.

**The bullet graph.** Five components: label, one linear quantitative scale, a featured measure, one or two comparative measures, and two to five qualitative ranges. Most BI tools implement it. The spec argues from footprint and reading efficiency ("Its linear design not only gives it a small footprint, but also supports more efficient reading than radial meters") and cites no test.

**The chartjunk critique.** *The Chartjunk Debate* (2011) attacks Bateman et al.'s *Useful Junk?* on method, without a replication, listing unwarranted assumptions: that Nigel Holmes charts represent extreme chartjunk, that the plain charts were what minimalists advocate, and that "a study involving 20 university students can produce trustworthy results." He notes the authors overreached and reported their own results in plain graphs. Bateman's long-term recall result, which Few said the sample could not support, did not replicate cleanly in a four-way 2023 replication ([refutations.md](../refutations.md)). Its accuracy finding survives, compatible with Skau's bar-deformation result.

**The critique of the field.** *Information Visualization Research as Pseudo-Science* (2015) opens with "Research in the field of information visualization is usually mediocre, often severely flawed, and only occasionally well done," then works through Borkin et al.'s *Beyond Memorability*, after sorting vis research into four categories each judged by its own standard. The stance overlaps with [Kosara's](robert-kosara.md) *An Empire Built On Sand*, argued from outside academia a year earlier.

## Where his name is used as authority for more than he showed

**The flat dual-axis ban.** [refutations.md](../refutations.md) names Few first in the ban's lineage, which overstates his position. His 2008 article ends:

> "I certainly cannot conclude, once and for all, that graphs with dual-scaled axes are never useful; only that I cannot think of a situation that warrants them in light of other, better solutions. I invite you to propose viable exceptions, which I will welcome with open arms."

The rule he states flatly is narrower: "a graph with a dual-scaled axis should never exclusively encode values as bars." The absolute ban is downstream of Few, the same degradation the wiki records for Cleveland and Munzner.

**Any rule of his quoted with "research shows" attached.** The single-screen dashboard rule is the standard case. It is mislabeled by definition, because he ran no research. His dashboard books are `not-reached` here, so the specific wording is not vouched; what is vouched is that nothing in his corpus can support a "research shows" preamble.

**"Few debunked the chartjunk study."** He critiqued it. Under [evidence-class.md](../concepts/evidence-class.md), an argued critique moves a claim toward **contested**; only a replication moves it to refuted.

## What they would object to in a figure

*Reconstruction from his stated priorities, not a response to any actual figure.*

A number with no target, norm or history fails his *Completeness* criterion. Next he would ask whether the measure is **valid** for what the title claims. Then out go gradients, shadows, 3D, gauges, unit charts and the pie. Engagement counts, with a wider acceptable range than truthfulness. Handed a cited study, he would read it and return a list.

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| "Data Visualization Effectiveness Profile," *Visual Business Intelligence Newsletter*, Jan-Mar 2017 | `primary-read` | [sources/few-effectiveness-profile.md](../sources/few-effectiveness-profile.md). Grounds inventory topics 1, 3, 5, 6, 9, 10, 11, 16, 31, 33, 42, 45, 46, 89, 91, with corrections on that page. |
| "Dual-Scaled Axes in Graphs: Are They Ever the Best Solution?" (2008) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/visual_business_intelligence/dual-scaled_axes.pdf) | No page. Softens [refutations.md](../refutations.md), "A flat ban on dual axes," as above. |
| "The Chartjunk Debate: A Close Examination of Recent Findings" (Apr-Jun 2011) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/visual_business_intelligence/the_chartjunk_debate.pdf) | No page. Pairs with [bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) and [gillan-richman-1994-data-ink.md](../studies/gillan-richman-1994-data-ink.md). |
| "Information Visualization Research as Pseudo-Science" (Oct-Dec 2015) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/visual_business_intelligence/infovis_research_as_pseudo-science.pdf) | No page. |
| "Bullet Graph Design Specification" (rev. 2013) | `primary-read`. [perceptualedge.com](https://www.perceptualedge.com/articles/misc/Bullet_Graph_Design_Spec.pdf) | [chart-types/gauge-and-bullet.md](../chart-types/gauge-and-bullet.md) notes the spec reports no test. |
| *Show Me the Numbers*, 2nd ed. (2012) | `not-reached` | No page. |
| *Information Dashboard Design*, 2nd ed. (2013) | `not-reached` | No page. Nothing in [inventory.md](../inventory.md) covers multi-figure dashboard layout. |
| *Now You See It* (2009), *Signal* (2015), *Big Data, Big Dupe* (2018) | `not-reached` | No page. |
| The rest of the *Visual Business Intelligence Newsletter* archive | Unread. 121 open PDFs indexed at [perceptualedge.com/library.php](https://www.perceptualedge.com/library.php). | On uncovered inventory areas: "Save the Pies for Dessert," "Unit Charts Are For Kids," "Our Irresistible Fascination with All Things Circular," "Are Mosaic Plots Worthwhile," "Distribution Displays," "Rules for Using Color." |

## See also

- [sources/few-effectiveness-profile.md](../sources/few-effectiveness-profile.md): the profile
- [concepts/floor-and-ceiling.md](../concepts/floor-and-ceiling.md): his acceptable ranges, from another angle
- [concepts/evidence-class.md](../concepts/evidence-class.md): critique versus study
- [robert-kosara.md](robert-kosara.md): the same skepticism, with experiments
