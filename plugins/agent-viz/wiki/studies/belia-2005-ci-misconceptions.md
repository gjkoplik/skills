---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Belia, Fidler, Williams & Cumming 2005: Researchers misunderstand confidence intervals and standard error bars

Sarah Belia, Fiona Fidler, Jennifer Williams, Geoff Cumming. *Psychological Methods* 10(4):389-396, December 2005. DOI [10.1037/1082-989X.10.4.389](https://doi.org/10.1037/1082-989X.10.4.389).

Published authors in psychology, behavioral neuroscience and medicine were asked to drag one mean up or down until two means with error bars looked "just statistically significantly different." 473 of them did it. Most got it badly wrong.

**How this was read.** PDF retrieved from `edmeasurement.net/5245/Belia-2005-CIs-SEs.pdf` and re-extracted locally with `pdftotext -layout`.

One extraction caveat: the text layer drops several math glyphs, so `p < .05` comes out as `p  .05` and `M ± tC × SE` comes out as `M  tC  SE`. Quotes below were chosen to avoid passages where a dropped glyph would change the meaning. If a figure ever needs quoting where a comparison operator matters, re-check against the APA version.

## What it is good for

The evidentiary backing for "label your error bars, and do not expect the label to save you." This is the paper to cite when someone argues that a figure's uncertainty encoding is fine because the audience is expert. The respondents *were* the experts. Everyone in the sample had published in a leading journal in their field.

## What it does not settle

It measures one narrow task, positioning two means to a target p-value, and treats error bars purely as significance indicators, which the authors themselves say is not the best way to think about them. It says nothing about whether a different *encoding* would fix the problem, which is [Correll & Gleicher](correll-gleicher-2014-error-bars-harmful.md)'s question. And the 15.2% response rate is a real limitation, discussed below.

## The finding

Four separate misconceptions, which the paper enumerates.

**First, spread and inaccuracy.**

> "responses were very widely spread and inaccurate: Only 22% of respondents set the means so the p value was between .025 and .10."

That accuracy window is deliberately generous. It is not "correct," it is "the p-value is within a factor of 2 of the target .05."

**Second, CIs and SE bars were not distinguished.** The correct answer for the SE task (614) sits 160 units above the correct answer for the CI task (454). The observed gap between the two groups' averages was 48.

> "It is seriously unfortunate that an identical graphic, the error bar, can have two such different meanings."

**Third, the just-touching rule.** 31.5% (99 of 314) positioned the means so the two intervals just touched, which is the widely believed and wrong heuristic. When 95% CIs on independent means just touch, two-tailed p is about .006, not .05. When SE bars just touch, p is about .16. Respondents applied the rule to SE bars (29.9%) about as often as to CIs (33.6%), which is the second misconception showing up again in a different measurement.

**Fourth, repeated measures were ignored.** A third of participants saw a display explicitly labeled Pre Test and Post Test for a single group of n = 36, where the drawn bars simply cannot answer the question. Only 11% gave any sign of noticing. By discipline: 6% in psychology, 17% in behavioral neuroscience, 11% in medicine.

The direction of error flips between tasks. CI respondents were **too strict**, setting means too far apart, mean response corresponding to p ≈ .009. SE respondents were **too lax**, mean response corresponding to p ≈ .109. Both errors follow from failing to notice which graphic they were looking at.

## Method

E-mail invitations went to 3,944 authors of research articles in 21 psychology, 6 behavioral neuroscience and 5 medicine journals, selected for high impact factor, sampling every second issue back from the most recent available (earliest 1998). Work ran in 2001 and early 2002.

Each respondent saw exactly one of three tasks, split roughly in thirds within each discipline: the CI task, the SE task, or the repeated-measures (RM) task. Group 1's mean was fixed at 300. An applet let the respondent click Group 2's mean up or down, with roughly three-unit granularity, until the two were judged just significantly different at p < .05 two-tailed.

Design details worth carrying forward, because they are the kind of thing a sloppy replication would skip:

- The invitation and the site URLs contained no clue to the authors' psychology affiliation or to which discipline a participant had been sorted into.
- **Pilot testing found an anchoring effect**, so half of each discipline-by-task cell started with Group 2 at 800 and half at 300. The overall anchoring difference was 53 units, and all reported responses are adjusted for it. The authors read the size of that effect as itself diagnostic: "This sizable anchoring effect suggests that many respondents may not have been very confident in their ability to accurately carry out the task."
- The just-touching analysis was run on the *unadjusted* histograms with narrower bins, because the anchoring correction would have smeared the peak.

## Sample size and population

473 usable responses from 3,122 deliverable invitations, a 15.2% response rate. A further 22.1% visited the site and did not complete. The CI and SE tasks together account for 314 of the responses; the RM task drew 159 (51 psychology, 47 behavioral neuroscience, 61 medicine).

A separate preliminary survey of 978 empirical articles from 1999-2001 in 33 journals established each field's baseline exposure. CIs or SE bars appeared in 12% or fewer of articles in nearly every cell, except that 64% of medicine articles reported CIs as numerical values and 44% of behavioral neuroscience articles included a figure with SE bars. Three fields, three very different habits, and no meaningful difference in accuracy between them.

## Limits the authors state themselves

They name the response rate and argue about its direction:

> "Our response rate was low, but we think it reasonable to assume that nonrespondents, including those who visited the site and elected not to complete the task, would if anything be less statistically confident and competent than respondents. If so, our findings are underestimates of the severity and prevalence of misconception among researchers in the three disciplines."

That is an argument, not a measurement. It is a plausible one, and it should be reported as the authors' inference rather than as an established fact about nonrespondents.

They also flag that the framing is not their preferred one:

> "We investigated the interpretation of error bars in relation to statistical significance. This may not be the best way to think of error bars ... but is worthy of study because of the current dominance of NHST and p values."

They kept the follow-up questions minimal on purpose, to avoid prompting an analytic attitude, which means there is very little data about *why* individual respondents answered as they did. 59% typed a free-text comment; 61% of those comments contained a statement that was clearly or probably statistically incorrect.

Their recommendation is partly a design recommendation, which is why this paper belongs in a visualization wiki at all:

> "we need better graphical conventions for displaying interval estimates that reduce ambiguity, make the status of independent variables salient, and signal more clearly how intervals may be used for data interpretation."

## Links

- [cumming-2007-error-bars.md](cumming-2007-error-bars.md), the same group's rules, with this paper as reference 1. Rule 1 and rule 8 are direct responses to misconceptions 2 and 4 here.
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md), which cites this paper and tests whether changing the encoding helps
- [inventory.md](../inventory.md), topic 49 (error-bar semantics must be stated)
