---
type: person
status: primary-read
retrieved: 2026-08-23
---

# Robert Kosara

**What they are known for.** He tested whether pie charts are read by angle, found they are not, and spent several papers narrowing down what they *are* read by. He writes the eagereyes blog and argues that visualization rests on untested assumptions.

**How this was read.** The papers marked `primary-read` in the table were downloaded from `media.eagereyes.org` and extracted locally with `pdftotext`. Skau & Kosara (2016) and Skau, Harrison & Kosara (2015) come from the wiki's existing primary readings. Affiliations are as printed on each paper (UNC Charlotte, then Tableau Research), not where he works now.

**What they are good for.** Whether a study stands behind a rule. He is the canon's most productive source of **decompositions**, experiments that split a chart type into the cues it carries instead of comparing two whole charts. [concepts/channels.md](../concepts/channels.md) identifies that step as the weak link in every chart-type claim.

**What they do not settle.** Whether pie charts are a good idea, which he does not claim. Nothing on color, low-level perception, or narrative. His pie work is almost all about reading one value off a chart, the same narrow task as the 1984 lineage.

---

## What their work established

### The pie chart program

**2016, with Drew Skau: angle is not the primary cue.** Six variants isolating each cue, 92 retained participants. The two angle-only conditions had the *highest* error. Donut and pie were "virtually identical." See [studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md).

**2016, with Skau: pie variants cost accuracy.** Exploded, enlarged-slice, elliptical and square pies against a plain pie: "even variants that do not distort central angle cause greater error than regular pie charts. Charts that distort the shape show the highest error." [skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md) found the same shape-deformation effect in bars.

**2019: area is the best-fitting cue.** A preregistered study of parallel-projected 3D pies, since projection distorts angle and arc length by an order of magnitude but keeps slice area proportional to value. 80 participants on Prolific. AIC ranks area first, angle second, arc length last. He argues against re-projection from his orientation data but leaves it open:

> "While this study suggests that the charts are read by area, it is not conclusive. In particular, the possibility of pie chart users re-projecting the chart to read them cannot be ruled out. Further experiments are therefore needed to zero in on the exact mechanism by which this common chart type is read."

**2019: the design space around the pie.** Prompted by an untested chart in the 2016 study that matched the pie. Centered shapes did much worse than the same shapes off-center.

**2019: the multi-slice case.** Pie, treemap, stacked bar and two circular variants, two tail distributions, questions about the largest or a middle slice. 81 participants recruited on Mechanical Turk, 75 retained.

> "The poor showing of the treemap for this task is notable: they have higher error and people take longer to read them in all conditions. While many in the visualization community would perhaps want to recommend them over pie charts, we find no evidence that they perform better for a small number of slices."

Long-tail distributions, expected to be easier, showed no significant difference in absolute or signed error. [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) records the many-slices case as untested, and this paper narrows that gap without closing it. It tests treemap against pie at multiple slices, not bar against pie.

### The methodological work

**Crowdsourcing, 2010, with Caroline Ziemkiewicz.** *Do Mechanical Turks Dream of Square Pie Charts?* ran MTurk studies, including a rerun of their own lab study, and cataloged what goes wrong. [Heer & Bostock](../studies/heer-bostock-2010.md), the same year, showed a crowdsourced study could reproduce a lab result. Most later studies here run on that platform.

**Embellishment, 2015, with Steve Haroz and Steven Franconeri.** The ISOTYPE paper splits two cases the chartjunk debate merges: "superfluous images can distract. But we find no user costs, and some intriguing benefits, when pictographs are used to represent the data." [refutations.md](../refutations.md) reaches the same split from Bateman and Skau.

**Position, 2016.** *An Empire Built On Sand* is a BELIV position paper with no experiment. It lists beliefs the field holds without testing:

> "A seminal paper does not lose its importance if limitations are found, or if parts of it are found to not or no longer be true. The value of the paper is not in providing facts, but in establishing a way of thinking, showing a new direction, introducing a methodology."

He says Cleveland & McGill's log-error measure, which everyone copied (himself included), is "arguably the wrong choice in many cases," especially for pies, where the error is a difference in percentages.

**Replication, 2018, with Steve Haroz.** *Skipping the Replication Crisis in Visualization* finds replications rare, names six threats to validity, and proposes publication models that let a replication clear a novelty bar. It grants that "it is not unreasonable to believe that they would show a similar rate of unreproducible results as in the psychological and social sciences." It names [Heer & Bostock](../studies/heer-bostock-2010.md) on Cleveland & McGill among the few replication chains.

### Where his name is used for more than he showed

**"Kosara proved pie charts are fine."** He did not, and says so. Bar-beats-pie for value extraction is measured in Cleveland & McGill and in Heer & Bostock, and none of his studies tests bars against pies. He removed the usual *mechanism* for that result, not the result.

**"Kosara showed 3D pie charts are okay."** The 60-degree view matched flat 2D in absolute error, and 30 and 15 degrees did not. At 60 degrees the chart "does not appear to be compressed, and thus might just be read as a 2D pie chart." Projection was a method, and he was "not interested in 3D pie charts per se."

**"Donut charts are fine because Kosara."** True for two-slice value reading. No one has tested multi-slice donuts against multi-slice pies.

### Where he compresses a caveat himself

*An Empire Built On Sand* says banking to 45 degrees "was based on a faulty analysis," that including more angles "would have revealed a much lower optimal angle," and that "the real maximum precision in line slope comparisons happens at a much shallower angle." [talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md) finds Cleveland's model scope-limited, not faulty. It fits the regime he sampled, and the shift below 30 degrees is ANGLE-only, while Cleveland's subjects were told to use HEIGHT. Kosara grants in the next sentence that the 45 rule remains useful.

His 2019 related work says Cleveland & McGill "equate their pie chart stimulus with angle perception without questioning it." They did question it, with the word *conjecture*, which [cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) quotes. Both lines compress toward the cleaner story, the failure his position papers describe.

---

## What they would object to in a figure

*Reconstruction from his stated priorities, not a response to any actual figure.*

He would ask what study supports the rule behind the figure, counting "everyone knows" as the finding, and whether the figure is for analysis or presentation, two jobs the field conflates. Chartjunk would not bother him. "Never use a pie chart" would, because its usual reason is false. He would ask whether a comparison was replicated, and which cue a supposedly bad chart asks the reader to use.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Skau & Kosara (2016), "Arcs, Angles, or Areas," *CGF* 35(3) | `primary-read` | [studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md), [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) |
| Skau, Harrison & Kosara (2015), embellished bar charts, *CGF* 34(3) | `primary-read` | [studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md) |
| Kosara (2019), "Evidence for Area as the Primary Visual Cue in Pie Charts," IEEE VIS short | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2019/Kosara-VISShort-2019.pdf). Preregistration, data and code at [osf.io/7y842](https://osf.io/7y842/). | No page. The follow-up to the 2016 study on the pie page. |
| Kosara (2019), "The Impact of Distribution and Chart Type on Part-to-Whole Comparisons," EuroVis short | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2019/Kosara-EuroVis-2019b.pdf) | No page. Tests the many-slices case that [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) records as untested and [chart-types/treemap.md](../chart-types/treemap.md) would want. |
| Kosara (2019), "Circular Part-to-Whole Charts Using the Area Visual Cue," EuroVis short | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2019/Kosara-EuroVis-2019a.pdf) | No page. Design space around the pie. |
| Kosara & Skau (2016), "Judgment Error in Pie Chart Variations," EuroVis short | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2016/Kosara-EuroVis-2016.pdf) | No page. Pie variants against a plain pie, the one a style guide needs. |
| Kosara & Haroz (2018), "Skipping the Replication Crisis in Visualization," BELIV | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2018/Kosara-BELIV-2018.pdf) | No page. Position paper. |
| Kosara & Ziemkiewicz (2010), "Do Mechanical Turks Dream of Square Pie Charts?", BELIV | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2010/Kosara-BELIV-2010.pdf) | No page. Method background for most post-2010 studies here. |
| Haroz, Kosara & Franconeri (2015), "ISOTYPE Visualization," CHI | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2015/Haroz-CHI-2015.pdf) | No page. Belongs beside [bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md). |
| Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series," *TVCG* | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2016/Haroz-TVCG-2016.pdf) | No page. Bears on dual axes, since the connected scatterplot is the usual proposed alternative. |
| Kosara (2016), "An Empire Built On Sand: Reexamining What We Think We Know About Visualization," BELIV | `primary-read`, [media.eagereyes.org](https://media.eagereyes.org/papers/2016/Kosara-BELIV-2016.pdf) | No page. Not a study, and would need the handling [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md) gets. |
| Kosara & Mackinlay (2013), "Storytelling: The Next Step for Visualization," *IEEE Computer* | `not-reached` | No page. |
| The eagereyes blog and the rest of the publication list | Unread. Index with per-paper PDFs at [kosara.net/publications](https://kosara.net/publications/). | The blog carries his re-readings of other papers, including the [Ware, Stone & Szafir 2023](../studies/ware-2023-rainbow-colormaps.md) essay. |

## See also

- [studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md): the decomposition this wiki treats as the model case
- [concepts/channels.md](../concepts/channels.md): why decompositions are the rare kind of study
- [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md): the type page that inherits from him
- [stephen-few.md](stephen-few.md): the same skepticism about the field's foundations, without experiments
- [william-cleveland.md](william-cleveland.md): the lineage he re-tests
