# Robert Kosara

**What they are known for.** Kosara is the person who went and checked whether pie charts are read by angle, found they are not, and then spent several more papers narrowing down what they *are* read by. He writes the eagereyes blog and has spent a decade arguing, in print and to the field's own venues, that visualization rests on a large stock of untested assumptions it mistakes for knowledge.

**Status: `primary-read`.** Eight of his papers were downloaded from `media.eagereyes.org` and extracted locally with `pdftotext`, plus the wiki's existing primary readings of Skau & Kosara (2016) and Skau, Harrison & Kosara (2015). Retrieval date: **2026-08-23**. Affiliations below are as printed on each paper (UNC Charlotte, then Tableau Research); no claim is made about where he works now.

**What they are good for.** Come here with *is there actually a study behind this rule*. He is the canon's most productive source of **decompositions**, meaning experiments that take a chart type apart into the cues it carries instead of comparing two whole charts. That is the step [concepts/channels.md](../concepts/channels.md) identifies as the weak link in every chart-type claim, and Kosara has run it more times than anyone else.

**What they do not settle.** Whether pie charts are a good idea, which he is careful not to claim. Nothing about color, nothing about perception below the level of a chart, and nothing about narrative beyond arguing it deserves study. His pie work is also almost entirely about **reading one value off a chart**, which is the same narrow task the 1984 lineage runs on.

---

## What their work actually established

### The pie chart program, in four steps

**Step 1, 2016, with Drew Skau: angle is not the primary cue.** Six chart variants isolating each cue, 92 retained participants. The two angle-only conditions had the *highest* error. Donut and pie were "virtually identical." Full treatment at [studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md).

**Step 2, 2019, alone: area is the best-fitting cue.** A preregistered study using **parallel-projected 3D pie charts**, on the reasoning that projection distorts angle and arc length by an order of magnitude while leaving a slice's area proportional to its value. 80 participants on Prolific. Model fit by AIC ranks area first, angle second, arc length last. His own conclusion, hedge included:

> "While this study suggests that the charts are read by area, it is not conclusive. In particular, the possibility of pie chart users re-projecting the chart to read them cannot be ruled out. Further experiments are therefore needed to zero in on the exact mechanism by which this common chart type is read."

He also names the alternative explanation himself and then argues against it from his own orientation data, which is the right way round.

**Step 2b, 2016, again with Skau: the popular pie variants all cost accuracy.** Exploded pie, pie with an enlarged slice, elliptical pie and square pie, against a plain pie baseline. Their finding is the one a design guide should be quoting: "even variants that do not distort central angle cause greater error than regular pie charts. Charts that distort the shape show the highest error." That is the same shape-deformation principle [skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md) found in bars, arrived at independently in a different chart type.

**Step 3, 2019: the design space around the pie.** After the isolating conditions in the 2016 study threw up a chart nobody had tested that performed as well as a pie, he went looking for more. Centered shapes turned out much worse than the same shape off-center.

**Step 4, 2019: the multi-slice case, which is the one everybody argues about.** Pie, treemap, stacked bar and two circular variants, with multiple slices, two tail distributions, and questions about either the largest or a middle slice. 81 participants recruited on Mechanical Turk, 75 retained. Two results:

> "The poor showing of the treemap for this task is notable: they have higher error and people take longer to read them in all conditions. While many in the visualization community would perhaps want to recommend them over pie charts, we find no evidence that they perform better for a small number of slices."

and the distribution result, which is a null he reports plainly: he expected long-tail distributions to be easier and found no significant difference in absolute or signed error.

**This closes a gap the wiki currently records as open.** [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) lists "the many-slices case" as `absence of evidence`, "not tested by any study here," correctly noting that Skau & Kosara deliberately used two segments. The 2019 EuroVis short paper tests multiple slices directly. It does not test bar-versus-pie at multiple slices, so the gap narrows rather than closes, and the specific claim it does settle is treemap-versus-pie.

### The methodological work

**Crowdsourcing, 2010, with Caroline Ziemkiewicz.** *Do Mechanical Turks Dream of Square Pie Charts?* ran several studies on MTurk, one of them a deliberate rerun of a study they had already done in the lab, and reported on what breaks. It is contemporaneous with [heer-bostock-2010.md](../studies/heer-bostock-2010.md) and does the complementary job: Heer & Bostock showed a crowdsourced perception study could reproduce a lab result, and this one catalogues the ways such a study goes wrong. Nearly every post-2010 study in this wiki runs on the platform these two papers validated.

**Embellishment, 2015, with Steve Haroz and Steven Franconeri.** The ISOTYPE paper is the most useful thing in the chartjunk literature because it separates two cases the debate keeps merging: "superfluous images can distract. But we find no user costs, and some intriguing benefits, when pictographs are used to represent the data." That is the same distinction [refutations.md](../refutations.md) arrives at from Bateman and Skau, and this paper states it directly as a finding rather than leaving it to be reconstructed across two studies.

**Position, 2016.** *An Empire Built On Sand* is a **BELIV position paper**, not a study, and it should never be cited as evidence for anything. What it is good for is its inventory of things the field believes without testing, and its argument about how seminal papers go wrong in transit:

> "A seminal paper does not lose its importance if limitations are found, or if parts of it are found to not or no longer be true. The value of the paper is not in providing facts, but in establishing a way of thinking, showing a new direction, introducing a methodology."

Its concrete complaint is worth carrying: everyone copied Cleveland & McGill's log-error measure, himself included, and he argues it is "arguably the wrong choice in many cases," in particular for pie charts where the error is a difference in percentages rather than a proportional error.

**Replication, 2018, with Steve Haroz.** *Skipping the Replication Crisis in Visualization* is a second position paper, and it is the one that turns the 2016 complaint into a program: survey how rare replications are, name six threats to study validity, and propose publication models that let a replication clear a novelty bar. It opens by stating the field's exposure rather than its innocence: replications are rare, and "it is not unreasonable to believe that they would show a similar rate of unreproducible results as in the psychological and social sciences." It also names the few real replication chains the field has, including [Heer & Bostock](../studies/heer-bostock-2010.md) on Cleveland & McGill.

### Where his name is used as authority for more than he showed

**"Kosara proved pie charts are fine."** He proved nothing of the sort and says so repeatedly. Bar-beats-pie for value extraction is measured in Cleveland & McGill and again in Heer & Bostock, and none of his studies tests bars against pies. What his program removes is the *mechanism* usually given for that result, which is a different and smaller thing.

**"Kosara showed 3D pie charts are okay."** His 2019 study found the 60-degree view condition did not differ from flat 2D in absolute error, while 30 and 15 degrees did. He explains that himself: at 60 degrees the chart "does not appear to be compressed, and thus might just be read as a 2D pie chart." Projection was a **method for separating cues**, not a design endorsement, and he says he was "not interested in 3D pie charts per se."

**"Donut charts are fine because Kosara."** Accurate, and narrower than it sounds: measured on two-slice value reading. Nobody has tested a multi-slice donut against a multi-slice pie.

### Even the most careful re-tester compresses a caveat at speed

This is not a gotcha. It is the strongest available demonstration of why this wiki's method exists, because it happens to the person whose whole argument is that it happens.

**On banking to 45.** *An Empire Built On Sand* says the recommendation "was based on a faulty analysis," that including more angles "would have revealed a much lower optimal angle," and that "the real maximum precision in line slope comparisons happens at a much shallower angle." [talbot-2012-slope-ratio.md](../studies/talbot-2012-slope-ratio.md) says something more careful: Cleveland's model fits within the regime he sampled, fails to extrapolate outside it, and the shift below 30 degrees belongs to the ANGLE submodel only, while Cleveland's subjects were instructed to use HEIGHT. "Faulty analysis" is stronger than "scope-limited." He does hedge in the next sentence, granting that the 45 rule remains useful.

**On pie charts.** His 2019 related-work section says Cleveland & McGill "equate their pie chart stimulus with angle perception without questioning it." They did question it, in the text, in the word *conjecture*, and [cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md) quotes the sentence.

Both are one-line summaries in sections that are not the paper's contribution, and both compress in the direction that makes the story cleaner. That is exactly the failure mode he is warning about, which is why it is worth recording rather than ignoring.

---

## What they would object to in your figure

*Reconstruction from his stated priorities. He has not seen your figure.*

He would not start with the figure. He would start with whatever rule you applied to make it and ask what study supports that rule, and if the answer is "everyone knows," he would treat that as the interesting finding. He would ask whether the figure is for **analysis or presentation**, on the grounds that those are different jobs with different standards and the field keeps conflating them. He would be unmoved by chartjunk objections and actively annoyed by "never use a pie chart," not because pies are good but because the reason usually given for it is false. If you showed him a comparison, he would want to know whether anyone had replicated it. And if you told him a chart type is bad, he would ask which cue you think the reader is using, and then whether that has ever been measured.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Skau & Kosara (2016), "Arcs, Angles, or Areas," *CGF* 35(3) | `primary-read` | [studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md), [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) |
| Skau, Harrison & Kosara (2015), embellished bar charts, *CGF* 34(3) | `primary-read` | [studies/skau-2015-embellished-bars.md](../studies/skau-2015-embellished-bars.md) |
| Kosara (2019), "Evidence for Area as the Primary Visual Cue in Pie Charts," IEEE VIS short | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2019/Kosara-VISShort-2019.pdf), extracted locally. Preregistration, data and code at [osf.io/7y842](https://osf.io/7y842/). | **No page.** It is step 2 of the argument the pie page tells step 1 of. |
| Kosara (2019), "The Impact of Distribution and Chart Type on Part-to-Whole Comparisons," EuroVis short | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2019/Kosara-EuroVis-2019b.pdf), extracted locally. | **No page**, and it tests the many-slices case that [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md) records as untested and [chart-types/treemap.md](../chart-types/treemap.md) would want. |
| Kosara (2019), "Circular Part-to-Whole Charts Using the Area Visual Cue," EuroVis short | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2019/Kosara-EuroVis-2019a.pdf), extracted locally. | No page. Design-space exploration around the pie. |
| Kosara & Skau (2016), "Judgment Error in Pie Chart Variations," EuroVis short | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2016/Kosara-EuroVis-2016.pdf), extracted locally. | **No page.** Exploded, enlarged-slice, elliptical and square pies all measured against a plain pie. This is the one a style guide actually needs. |
| Kosara & Haroz (2018), "Skipping the Replication Crisis in Visualization," BELIV | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2018/Kosara-BELIV-2018.pdf), extracted locally. | No page. **Position paper**, same handling as *Empire*. |
| Kosara & Ziemkiewicz (2010), "Do Mechanical Turks Dream of Square Pie Charts?", BELIV | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2010/Kosara-BELIV-2010.pdf), extracted locally. | No page. Method background for most post-2010 studies here. |
| Haroz, Kosara & Franconeri (2015), "ISOTYPE Visualization," CHI | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2015/Haroz-CHI-2015.pdf), extracted locally. | **No page**, and it belongs beside [bateman-2010-useful-junk.md](../studies/bateman-2010-useful-junk.md) in the chartjunk file. |
| Haroz, Kosara & Franconeri (2016), "The Connected Scatterplot for Presenting Paired Time Series," *TVCG* | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2016/Haroz-TVCG-2016.pdf), extracted locally. | No page. Relevant to the dual-axis question, since the connected scatterplot is the alternative usually proposed. |
| Kosara (2016), "An Empire Built On Sand: Reexamining What We Think We Know About Visualization," BELIV | `primary-read`. [media.eagereyes.org](https://media.eagereyes.org/papers/2016/Kosara-BELIV-2016.pdf), extracted locally. | No page. **Not a study.** Same handling as [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md) would need. |
| Kosara & Mackinlay (2013), "Storytelling: The Next Step for Visualization," *IEEE Computer* | `not-reached`. | No page. |
| The eagereyes blog and the rest of the publication list | Unread. Full index with per-paper PDFs at [kosara.net/publications](https://kosara.net/publications/). | The blog is where his re-readings of other people's papers land, including the [Ware, Stone & Szafir 2023](../studies/ware-2023-rainbow-colormaps.md) essay. |

## See also

- [studies/skau-kosara-2016.md](../studies/skau-kosara-2016.md), the decomposition this wiki treats as the model case
- [concepts/channels.md](../concepts/channels.md), why decompositions are the rare and valuable kind of study
- [chart-types/pie-and-donut.md](../chart-types/pie-and-donut.md), the type page that inherits from him
- [stephen-few.md](stephen-few.md), the same skepticism about the field's foundations, argued from outside it and without experiments
- [william-cleveland.md](william-cleveland.md), the lineage he is re-testing, including the log-error measure he thinks everyone copied without thinking
