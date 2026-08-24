# Gillan & Richman 1994: Minimalism and the Syntax of Graphs

Douglas J. Gillan, Edward H. Richman. *Human Factors* 36(4):619-644, December 1994. DOI [10.1177/001872089403600405](https://doi.org/10.1177/001872089403600405).

## What it is

Four experiments testing Tufte's rule that graphs should maximize the data-ink ratio. The result this wiki uses it for: the effect of removing ink is **element-conditional**. Some non-data ink helps, some hurts, and which is which depends on the graph type, the task, and what other elements are present.

## Status

**`secondary-only`, with one upgrade.**

The full text was **not reached**. The article is closed at SAGE (403), OpenAlex reports `oa_status: closed` with no repository fulltext, and it is not indexed in PubMed. No experiment-by-experiment detail, no sample sizes, no per-condition statistics.

**The upgrade:** the abstract is now available **verbatim from the publisher's own Crossref deposit** (`api.crossref.org/works`, JATS `<jats:abstract>` under the DOI above), rather than from a search-engine summary. [refutations.md](../refutations.md) records this material as reached through secondary summaries only. The abstract text below is no longer in that category. Everything beyond the abstract still is.

Retrieval date: **2026-08-23**.

## What it is good for

Killing the word "maximize." This is the paper that turns data-ink from a rule into a heuristic with exceptions, and it does so from inside human factors rather than from within the visualization design canon.

## What it does not settle

Without the body, the sample sizes, effect sizes, stimuli and per-experiment designs are unknown. Do not attribute specific numbers to this paper. See also the wrinkle below, which the wiki's current summary omits.

## The abstract, verbatim

Reproduced in full because it is the only primary text available, and because the wiki's existing summary of it is incomplete in a way that matters.

> "Four experiments examined Tufte's syntactic rule that graphs should have maximal data-ink ratios produced by erasing non-data-ink and redundant data-ink. In Experiment 1, the data-ink ratios of bar and line graphs affected the accuracy and response times for comparison, difference, and mean questions: the higher the data-ink ratio, the faster the response time and the greater the accuracy. Experiments 2 and 3 showed that the effects of ink in the syntactic elements of a graph depend on the location and function of the element: redundant ink in the indicators had limited effects on performance, pictorial backgrounds generally increased response time and decreased accuracy, y axis tick marks generally increased response time, and the y axis line and the x axis generally decreased response time. The effect of each graphical element was conditional on the type of graph and task and the presence of other graphical elements. The discussion focuses on psychological principles that may underlie the effects of each syntactic element."

## What the abstract actually supports

**Experiment 1 is a point in Tufte's favor**, and the wiki's current phrasing does not mention it. At the aggregate level, higher data-ink ratio produced faster responses and greater accuracy across comparison, difference and mean questions on bar and line graphs. That is the rule working.

**Experiments 2 and 3 are where it decomposes.** Four separate directions, in the abstract's own order:

| Element | Effect of *including* it |
|---|---|
| Redundant ink in the indicators | Limited effect on performance |
| Pictorial backgrounds | Increased response time, decreased accuracy (removal helps) |
| y-axis tick marks | Increased response time (removal helps) |
| y-axis line and x-axis | **Decreased response time** (removal hurts) |

And the sentence that is the whole reason this paper is in the wiki:

> "The effect of each graphical element was conditional on the type of graph and task and the presence of other graphical elements."

So the honest reading is not "the data-ink ratio is wrong." It is: **the aggregate direction is Tufte's, and the element-level decomposition is not.** Erasing ink helps on average and hurts specifically for the elements that carry orientation. [refutations.md](../refutations.md) already lands on the right phrasing, "strip decoration, keep orientation," but a reader arriving cold should know that Experiment 1 supports the rule before Experiments 2 and 3 qualify it.

Note also that "pictorial backgrounds generally increased response time and decreased accuracy" is a result *against* embellishment, from 1994, sixteen years before [Bateman et al.](bateman-2010-useful-junk.md). The two are not in direct conflict, since Bateman measured verbal description and recall on integrated Holmes imagery rather than backgrounds behind a plot, and found no accuracy penalty. But anyone treating the chartjunk record as one-sided in the pro-embellishment direction should have this line in front of them.

## What the fourth experiment tested

Unknown. The abstract accounts for Experiments 1, 2 and 3 and does not describe the fourth. Do not assume.

## Corroboration from the same author

`primary-read`, and it is corroboration rather than independent confirmation.

Gillan later co-authored *Guidelines for Presenting Quantitative Data in HFES Publications* (Gillan, Wickens, Hollands & Carswell, *Human Factors* 40(1), 1998), which cites the 1994 paper and encodes its conclusions as guidance. PDF retrieved 2026-08-23 from the HFES site and read locally. Guideline 2.2.6 is the element-conditional result turned into advice:

> "Although axes and tick marks do not communicate meaning directly, they help readers to determine the meaning of other elements of the graph. Specifically, axes help the reader to parse the graph; tick marks can help the reader to estimate the value of an indicator."

> "Make the axes salient (e.g., by use of wide lines and high contrast between dark axes and the light background). However, the axes should not be more salient than the labels or indicators."

> "Tick marks will be of no value if they provide information also provided by the quantitative labels for the scale values. Placing tick marks only next to each label is redundant and can increase the time to read a graph. Accordingly, either use tick marks between infrequent scale values on the y or x axis or use frequent scale values and no tick marks."

This confirms the *direction* of the two axis-related results without going through a third-party summary, and it adds something the abstract does not: the tick-mark penalty is specifically about **redundancy with the scale labels**, not about tick marks in general.

## What would improve this page

Reading the actual article. It would supply sample sizes, the design of Experiment 4, effect sizes, and the "psychological principles" discussion the abstract advertises, which is likely the most transferable part. Routes not yet tried: institutional SAGE access, interlibrary loan, or an author request to D. J. Gillan at NC State.

## Links

- [refutations.md](../refutations.md), "Chartjunk and the data-ink ratio as settled." Confirmed, with the Experiment 1 caveat above added.
- [bateman-2010-useful-junk.md](bateman-2010-useful-junk.md)
- [skau-2015-embellished-bars.md](skau-2015-embellished-bars.md)
- [inventory.md](../inventory.md), topic 67 (data-ink discipline, and its contested status)
