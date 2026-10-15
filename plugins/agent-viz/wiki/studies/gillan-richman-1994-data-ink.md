---
type: study
status: secondary-only
status_partial: true
retrieved: 2026-08-23
---

# Gillan & Richman 1994: Minimalism and the Syntax of Graphs

Douglas J. Gillan, Edward H. Richman. *Human Factors* 36(4):619-644, December 1994. DOI [10.1177/001872089403600405](https://doi.org/10.1177/001872089403600405).

Four experiments testing Tufte's rule that graphs should maximize the data-ink ratio. The effect of removing ink is **element-conditional**: it depends on the element, the graph type, the task, and what else is present.

**How this was read.** The full text was not reached. SAGE returned 403, OpenAlex reports `oa_status: closed` with no repository fulltext, and the article is not indexed in PubMed. Institutional SAGE access, interlibrary loan and an author request to D. J. Gillan at NC State are untried. The abstract below is verbatim from the publisher's own Crossref deposit (`api.crossref.org/works`, JATS `<jats:abstract>` under the DOI above), not from a search-engine summary. Everything beyond the abstract is still secondary, as [refutations.md](../refutations.md) records. The 1998 HFES guidelines below were downloaded from the HFES site and read locally.

## What it is good for

It turns data-ink from a rule ("maximize") into a heuristic with exceptions, from inside human factors rather than the visualization design canon.

## What it does not settle

Sample sizes, effect sizes, stimuli and per-experiment designs, so no specific numbers can be attributed to this paper. The abstract does not describe Experiment 4, and its "psychological principles" discussion is unread.

## The abstract, verbatim

> "Four experiments examined Tufte's syntactic rule that graphs should have maximal data-ink ratios produced by erasing non-data-ink and redundant data-ink. In Experiment 1, the data-ink ratios of bar and line graphs affected the accuracy and response times for comparison, difference, and mean questions: the higher the data-ink ratio, the faster the response time and the greater the accuracy. Experiments 2 and 3 showed that the effects of ink in the syntactic elements of a graph depend on the location and function of the element: redundant ink in the indicators had limited effects on performance, pictorial backgrounds generally increased response time and decreased accuracy, y axis tick marks generally increased response time, and the y axis line and the x axis generally decreased response time. The effect of each graphical element was conditional on the type of graph and task and the presence of other graphical elements. The discussion focuses on psychological principles that may underlie the effects of each syntactic element."

## What the abstract supports

Experiment 1 supports Tufte. Across comparison, difference and mean questions on bar and line graphs, a higher data-ink ratio produced faster responses and greater accuracy.

Experiments 2 and 3 split the rule by element, in the abstract's order:

| Element | Effect of *including* it |
|---|---|
| Redundant ink in the indicators | Limited effect on performance |
| Pictorial backgrounds | Increased response time, decreased accuracy (removal helps) |
| y-axis tick marks | Increased response time (removal helps) |
| y-axis line and x-axis | **Decreased response time** (removal hurts) |

> "The effect of each graphical element was conditional on the type of graph and task and the presence of other graphical elements."

So the aggregate direction is Tufte's and the element-level decomposition is not. Erasing ink helps on average and hurts for the elements that carry orientation. [refutations.md](../refutations.md) phrases this as "strip decoration, keep orientation."

"Pictorial backgrounds generally increased response time and decreased accuracy" is a 1994 result against embellishment, so the chartjunk record is not one-sided. It does not conflict directly with [Bateman et al.](bateman-2010-useful-junk.md), who measured verbal description and recall on integrated Holmes imagery, not backgrounds behind a plot, and found no accuracy penalty.

## Corroboration from the same author

`primary-read`, and corroboration rather than independent confirmation. Gillan later co-authored *Guidelines for Presenting Quantitative Data in HFES Publications* (Gillan, Wickens, Hollands & Carswell, *Human Factors* 40(1), 1998), which cites the 1994 paper and turns its conclusions into guidance. Guideline 2.2.6:

> "Although axes and tick marks do not communicate meaning directly, they help readers to determine the meaning of other elements of the graph. Specifically, axes help the reader to parse the graph; tick marks can help the reader to estimate the value of an indicator."

> "Make the axes salient (e.g., by use of wide lines and high contrast between dark axes and the light background). However, the axes should not be more salient than the labels or indicators."

> "Tick marks will be of no value if they provide information also provided by the quantitative labels for the scale values. Placing tick marks only next to each label is redundant and can increase the time to read a graph. Accordingly, either use tick marks between infrequent scale values on the y or x axis or use frequent scale values and no tick marks."

This confirms the direction of the two axis results from a primary source, and adds that the tick-mark penalty is about redundancy with the scale labels, not tick marks in general.

## Links

- [refutations.md](../refutations.md), "Chartjunk and the data-ink ratio as settled." Confirmed, with the Experiment 1 caveat.
- [bateman-2010-useful-junk.md](bateman-2010-useful-junk.md)
- [skau-2015-embellished-bars.md](skau-2015-embellished-bars.md)
- [inventory.md](../inventory.md), topic 67 (data-ink discipline, and its contested status)
