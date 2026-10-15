---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Belia, Fidler, Williams & Cumming 2005: Researchers misunderstand confidence intervals and standard error bars

Sarah Belia, Fiona Fidler, Jennifer Williams, Geoff Cumming. *Psychological Methods* 10(4):389-396, December 2005. DOI [10.1037/1082-989X.10.4.389](https://doi.org/10.1037/1082-989X.10.4.389).

Published authors in psychology, behavioral neuroscience and medicine dragged one mean until two means with error bars looked "just statistically significantly different." Most of the 473 got it badly wrong.

**How this was read.** PDF from `edmeasurement.net/5245/Belia-2005-CIs-SEs.pdf`, re-extracted locally with `pdftotext -layout`. The text layer drops math glyphs (`p < .05` becomes `p  .05`, `M ± tC × SE` becomes `M  tC  SE`), so quotes avoid passages where a dropped glyph would change the meaning. Passages where a comparison operator carries the meaning are unchecked against the APA version.

## What it is good for

The evidence behind "label your error bars, and do not expect the label to save you." It answers the argument that an expert audience reads uncertainty encodings correctly: everyone in the sample had published in a leading journal.

## What it does not settle

One narrow task, positioning two means to a target p-value, with error bars treated purely as significance indicators, which the authors say is not the best way to think about them. Whether a different encoding would help, which is [Correll & Gleicher](correll-gleicher-2014-error-bars-harmful.md)'s question. The 15.2% response rate limits it.

## The finding

**Spread and inaccuracy.**

> "responses were very widely spread and inaccurate: Only 22% of respondents set the means so the p value was between .025 and .10."

That window is generous: "the p-value is within a factor of 2 of the target .05."

**CIs and SE bars not distinguished.** The correct answer for the SE task (614) sits 160 units above the correct answer for the CI task (454). The observed gap between the two groups' averages was 48.

> "It is seriously unfortunate that an identical graphic, the error bar, can have two such different meanings."

**The just-touching rule.** 31.5% (99 of 314) positioned the means so the two intervals just touched. When 95% CIs on independent means just touch, two-tailed p is about .006, not .05. When SE bars just touch, p is about .16. Respondents applied the rule to SE bars (29.9%) about as often as to CIs (33.6%), the second misconception again.

**Repeated measures ignored.** A third of participants saw a display labeled Pre Test and Post Test for a single group of n = 36, where the bars cannot answer the question. Only 11% showed any sign of noticing: 6% in psychology, 17% in behavioral neuroscience, 11% in medicine.

The error flips direction between tasks. CI respondents were too strict (mean response p ≈ .009) and SE respondents too lax (p ≈ .109), both consistent with not noticing which graphic was on screen.

## Method

E-mail invitations went to 3,944 authors in 21 psychology, 6 behavioral neuroscience and 5 medicine journals with high impact factors, sampling every second issue back from the most recent (earliest 1998), in 2001 and early 2002.

Each respondent saw one task, split roughly in thirds within each discipline: CI, SE, or repeated measures (RM). Group 1's mean was fixed at 300, and the respondent moved Group 2's mean in roughly three-unit steps until the two were just significantly different at p < .05 two-tailed.

- Invitations and site URLs did not reveal the authors' psychology affiliation or a participant's discipline group.
- Pilot testing found an anchoring effect, so half of each discipline-by-task cell started Group 2 at 800 and half at 300. The overall anchoring difference was 53 units, and all reported responses are adjusted for it. The authors: "This sizable anchoring effect suggests that many respondents may not have been very confident in their ability to accurately carry out the task."
- The just-touching analysis used unadjusted histograms with narrower bins, since the correction would smear the peak.

## Sample size and population

473 usable responses from 3,122 deliverable invitations, a 15.2% response rate. Another 22.1% visited the site and did not complete. The CI and SE tasks account for 314 responses and the RM task for 159 (51 psychology, 47 behavioral neuroscience, 61 medicine).

A preliminary survey of 978 empirical articles from 1999-2001 in 33 journals measured each field's exposure. CIs or SE bars appeared in 12% or fewer of articles in nearly every cell, except that 64% of medicine articles reported CIs numerically and 44% of behavioral neuroscience articles had a figure with SE bars. Accuracy did not differ meaningfully between the fields.

## Limits the authors state themselves

On the response rate:

> "Our response rate was low, but we think it reasonable to assume that nonrespondents, including those who visited the site and elected not to complete the task, would if anything be less statistically confident and competent than respondents. If so, our findings are underestimates of the severity and prevalence of misconception among researchers in the three disciplines."

That is an inference about nonrespondents, not a measurement.

On the framing:

> "We investigated the interpretation of error bars in relation to statistical significance. This may not be the best way to think of error bars ... but is worthy of study because of the current dominance of NHST and p values."

Follow-up questions were minimal, to avoid prompting an analytic attitude, so there is little data on why individuals answered as they did. 59% left a free-text comment, and 61% of those contained a clearly or probably incorrect statistical statement.

Their recommendation is partly a design one:

> "we need better graphical conventions for displaying interval estimates that reduce ambiguity, make the status of independent variables salient, and signal more clearly how intervals may be used for data interpretation."

## Links

- [cumming-2007-error-bars.md](cumming-2007-error-bars.md): the same group's rules, with this paper as reference 1. Rules 1 and 8 respond directly to misconceptions 2 and 4 here.
- [correll-gleicher-2014-error-bars-harmful.md](correll-gleicher-2014-error-bars-harmful.md): cites this paper and tests whether changing the encoding helps
- [inventory.md](../inventory.md), topic 49 (error-bar semantics must be stated)
